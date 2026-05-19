"""
NavisworksToPNT — Exports a .pnt coordination package from the active NWF.

.pnt is a ZIP archive containing:
    manifest.json     – project metadata
    clashes.json      – clash results in dashboard-compatible format
    properties.json   – full element property data keyed by pnt_id
    models/<n>.ifc    – lightweight IFC4 (geometry + PNT_Identity pset only)

Element identity:
    Each element receives a UUID4 as pnt_id, stored as the IFC GlobalId
    and in a PNT_Identity property set. Clash results are linked to IFC
    elements by display name when a match exists.

Requirements:
    pip install ifcopenshell
"""

import clr
import sys

try:
    sys.stdout.reconfigure(line_buffering=True)
except Exception:
    pass
import json
import re
import time
import zipfile
from pathlib import Path
from datetime import datetime
from collections import defaultdict  # used in ClassificationAnalyzer

clr.AddReference("Autodesk.Navisworks.Api")
clr.AddReference("Autodesk.Navisworks.ComApi")
clr.AddReference("Autodesk.Navisworks.Interop.ComApi")
clr.AddReference("Autodesk.Navisworks.Clash")

from Autodesk.Navisworks.Api import Application
from Autodesk.Navisworks.Api.Clash import DocumentClash

_bundle = (Path.home() / "AppData" / "Roaming" / "Autodesk" / "ApplicationPlugins"
           / "RAEN.Navisworks.PyNET.bundle" / "Contents" / "2027")
sys.path.append(str(_bundle))

clr.AddReference("Raen.Core.Pynet.Resources")
clr.AddReference("Raen.Navisworks.Pynet.2027")

from Raen.Core.Pynet.Resources import CastUtils  # type: ignore
from Raen.Navisworks.Pynet.Utils import GlbExporter  # type: ignore

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from System.Windows.Forms import (Form, Label, ProgressBar, ProgressBarStyle,  # type: ignore
                                   FormBorderStyle, FormStartPosition,
                                   Application as WinApp)
from System.Drawing import Size, Font, FontStyle  # type: ignore


FEET_TO_METERS = 0.3048

# Elements with more triangles than this threshold are replaced by their
# axis-aligned bounding box (12 triangles). They still appear in properties.json
# and clash linking — only their visual geometry is simplified.
#
# 20000 is a good default for BIM coordination: regular architectural elements
# (walls, slabs, beams, doors) typically use <500 triangles each and pass
# through unchanged, while heavy content (vegetation, RPC families, terrain
# meshes, curved generic models) collapses to bbox so the GLB stays light.
# A 15 MB NWC should produce a single-digit MB GLB. Tune higher only if you
# need to preserve curved geometry detail.
MAX_FACES_PER_ELEMENT = 20000

# Set to False for a geometry-only test run — skips all property extraction.
EXPORT_PROPERTIES = False

# Set to True to skip GenerateSimplePrimitives entirely — every element becomes a
# bounding box. Use this to test the full pipeline quickly without tessellation cost.
BBOX_ONLY = False

# Set to False to skip clash test execution (avoids potential crash on heavy models).
EXPORT_CLASHES = False


# ─── Progress Window ──────────────────────────────────────────────────────────

class ProgressWindow:
    """Non-modal WinForms dialog — shows phase, detail line, and elapsed time."""

    def __init__(self, title: str):
        self._start = time.time()

        self._form = Form()
        self._form.Text            = "PNT Export"
        self._form.ClientSize      = Size(520, 130)
        self._form.FormBorderStyle = FormBorderStyle.FixedDialog
        self._form.MaximizeBox     = False
        self._form.MinimizeBox     = False
        self._form.StartPosition   = FormStartPosition.CenterScreen
        self._form.TopMost         = True

        self._lbl_phase = Label()
        self._lbl_phase.Text   = title
        self._lbl_phase.Left   = 16
        self._lbl_phase.Top    = 12
        self._lbl_phase.Width  = 488
        self._lbl_phase.Height = 20
        self._lbl_phase.Font   = Font("Segoe UI", 9, FontStyle.Bold)

        self._lbl_detail = Label()
        self._lbl_detail.Text   = ""
        self._lbl_detail.Left   = 16
        self._lbl_detail.Top    = 36
        self._lbl_detail.Width  = 488
        self._lbl_detail.Height = 20

        self._bar = ProgressBar()
        self._bar.Left   = 16
        self._bar.Top    = 62
        self._bar.Width  = 488
        self._bar.Height = 18
        self._bar.Style  = ProgressBarStyle.Marquee

        self._lbl_time = Label()
        self._lbl_time.Text   = "00:00"
        self._lbl_time.Left   = 16
        self._lbl_time.Top    = 92
        self._lbl_time.Width  = 488
        self._lbl_time.Height = 20

        for ctrl in (self._lbl_phase, self._lbl_detail, self._bar, self._lbl_time):
            self._form.Controls.Add(ctrl)

        self._form.Show()
        WinApp.DoEvents()

    def update(self, phase: str = None, detail: str = None):
        if phase is not None:
            self._lbl_phase.Text = phase
        if detail is not None:
            self._lbl_detail.Text = str(detail)
        elapsed = int(time.time() - self._start)
        m, s = divmod(elapsed, 60)
        self._lbl_time.Text = f"Elapsed: {m:02d}:{s:02d}"
        WinApp.DoEvents()

    def close(self):
        try:
            self._form.Close()
            WinApp.DoEvents()
        except Exception:
            pass


# ─── Clash Extractor ─────────────────────────────────────────────────────────

class ClashExtractor:
    """
    Runs all clash tests and collects results.
    Links each clash element to its pnt_id via (nwc_stem, cx, cy, cz) lookup.
    The nwc_stem is resolved by walking up to the model root and matching
    against a pre-built root→stem map — consistent with the export side.
    """

    def __init__(self, bbox_index: dict, doc):
        # {(nwc_stem, round3_cx, round3_cy, round3_cz): pnt_id}
        self._bix = bbox_index
        self._model_stems = {}
        for i in range(doc.Models.Count):
            model = doc.Models[i]
            self._model_stems[model.RootItem] = Path(model.FileName).stem

    def run(self, doc) -> tuple:
        """Returns (tests_summary list, all_clashes list)."""
        clash_doc  = CastUtils.CastTo[DocumentClash](doc.Clash)
        tests_data = clash_doc.TestsData

        print("  Running all clash tests...")
        t0 = datetime.now()
        tests_data.TestsRunAllTests()
        elapsed = (datetime.now() - t0).total_seconds()
        print(f"  Tests computed in {elapsed:.1f}s")

        tests_summary = []
        all_clashes   = []
        all_tests     = list(tests_data.Value.TestsRoot.Children)
        n_tests       = len(all_tests)

        for ti, test in enumerate(all_tests, 1):
            print(f"  [{ti}/{n_tests}] {test.DisplayName}...", end="")
            t0 = datetime.now()
            results = list(self._iter_results(test))
            count   = len(results)

            status_counts = {}
            for r in results:
                s = str(r.Status)
                status_counts[s] = status_counts.get(s, 0) + 1
            dominant = max(status_counts, key=status_counts.get) if status_counts else "New"
            elapsed = (datetime.now() - t0).total_seconds()
            print(f" {count} clashes ({elapsed:.1f}s)")
            tests_summary.append({"name": test.DisplayName, "clashes": count, "status": dominant})

            for result in results:
                item_a = result.Item1
                item_b = result.Item2
                center = result.Center

                src_a  = self._nwc_stem(item_a)
                src_b  = self._nwc_stem(item_b)
                name_a = self._item_name(item_a)
                name_b = self._item_name(item_b)

                all_clashes.append({
                    "Test":         test.DisplayName,
                    "Discipline":   self._discipline(test.DisplayName),
                    "Clash":        result.DisplayName,
                    "Status":       str(result.Status),
                    "Distance (m)": round(float(result.Distance), 4) if result.Distance else 0,
                    "X": round(float(center.X), 3) if center else None,
                    "Y": round(float(center.Y), 3) if center else None,
                    "Z": round(float(center.Z), 3) if center else None,
                    "Element A": name_a,
                    "ID A":      self._element_id(item_a),
                    "Source A":  src_a,
                    "Type A":    self._revit_category(item_a),
                    "Element B": name_b,
                    "ID B":      self._element_id(item_b),
                    "Source B":  src_b,
                    "Type B":    self._revit_category(item_b),
                    "pnt_id_a":  self._resolve(item_a),
                    "pnt_id_b":  self._resolve(item_b),
                    "Comment":   self._last_comment(result),
                })

        return tests_summary, all_clashes

    @staticmethod
    def _item_name(item) -> str:
        if item is None:
            return ""
        try:
            node = item.Parent
            while node is not None:
                if node.DisplayName:
                    return node.DisplayName
                node = node.Parent
        except Exception:
            pass
        return ""

    def _nwc_stem(self, item) -> str:
        """NWC filename stem for the model the item belongs to."""
        if item is None:
            return ""
        try:
            node = item
            while node.Parent is not None:
                node = node.Parent
            return self._model_stems.get(node, "")
        except Exception:
            return ""

    @staticmethod
    def _revit_category(item) -> str:
        """Revit category from 'Tipo de Revit' > 'Categoría' on parent."""
        # TODO: test with English Revit ("Revit Type" / "Category")
        if item is None:
            return ""
        parent = item.Parent
        if parent is None:
            return ""
        try:
            for cat in parent.PropertyCategories:
                if cat.DisplayName == "Tipo de Revit":
                    for prop in cat.Properties:
                        if prop.DisplayName == "Categoría":
                            val = str(prop.Value.ToDisplayString())
                            if val and val != "?":
                                return val
        except Exception:
            pass
        return ""

    def _resolve(self, item):
        """Look up pnt_id by (nwc_stem, cx, cy, cz). Tries item then item.Parent
        because result.Item1 may be a geometry leaf or the named element."""
        if item is None:
            return None
        try:
            node = item
            while node.Parent is not None:
                node = node.Parent
            stem = self._model_stems.get(node, "")

            candidates = [item]
            if item.Parent is not None:
                candidates.append(item.Parent)
            for target in candidates:
                bb  = target.BoundingBox()
                key = (stem,
                       round(float(bb.Center.X), 3),
                       round(float(bb.Center.Y), 3),
                       round(float(bb.Center.Z), 3))
                found = self._bix.get(key)
                if found is not None:
                    return found
        except Exception:
            pass
        return None

    @staticmethod
    def _iter_results(test):
        for child in test.Children:
            if child.IsGroup:
                for r in child.Children:
                    yield r
            else:
                yield child

    @staticmethod
    def _get_prop(item, cat_name, prop_name) -> str:
        if item is None:
            return ""
        for target in (item.Parent, item):
            if target is None:
                continue
            try:
                for cat in target.PropertyCategories:
                    if cat.DisplayName == cat_name:
                        for prop in cat.Properties:
                            if prop.DisplayName == prop_name:
                                val = str(prop.Value.ToDisplayString())
                                if val and val != "?":
                                    return val
            except Exception:
                pass
        return ""

    @staticmethod
    def _element_id(item) -> str:
        if item is None:
            return ""
        try:
            parent = item.Parent
            if parent is not None:
                for cat in parent.PropertyCategories:
                    # TODO: test with English Revit ("Element ID" / "Value")
                    if cat.DisplayName.lower() == "id de elemento":
                        for prop in cat.Properties:
                            if prop.DisplayName == "Valor":
                                val = prop.Value.ToDisplayString()
                                if val and val != "?":
                                    return val
        except Exception:
            pass
        return ""

    @staticmethod
    def _last_comment(result) -> str:
        try:
            last = ""
            for c in result.Comments:
                body = str(c.Body)
                last = body.split("] ", 1)[-1] if "] " in body else body
            return last
        except Exception:
            return ""

    @staticmethod
    def _discipline(test_name: str) -> str:
        m = re.search(r'Instalaciones_([^_]+)', test_name)
        return m.group(1) if m else "Estructura"


# ─── Classification Analyser ─────────────────────────────────────────────────

class ClassificationAnalyzer:
    """
    Validates PYNET_Classification coverage at TYPE node level per model.
    Matches the logic in the ClashDetection skill (step 2b).
    """

    PARAM_NAME = "PYNET_Classification"
    PARAM_CAT  = "lcldrevit_tab_type"   # internal name of the "Tipo" category

    @staticmethod
    def run(doc) -> list:
        results = []
        for model in doc.Models:
            model_name = Path(model.FileName).stem
            classified_types   = {}   # hash(item) → code
            unclassified_types = []

            for item in model.RootItem.Descendants:
                if item.ClassDisplayName != "Tipo":
                    continue
                code = None
                for cat in item.PropertyCategories:
                    if cat.Name != ClassificationAnalyzer.PARAM_CAT:
                        continue
                    for prop in cat.Properties:
                        if prop.DisplayName != ClassificationAnalyzer.PARAM_NAME:
                            continue
                        try:
                            val = prop.Value.ToDisplayString()
                            if val:
                                code = val
                        except Exception:
                            pass
                if code:
                    classified_types[hash(item)] = code
                else:
                    if len(unclassified_types) < 20:
                        unclassified_types.append(item.DisplayName or "(sin nombre)")

            code_counts       = defaultdict(int)
            covered_geo_hashes = set()
            for item in model.RootItem.Descendants:
                if item.ClassDisplayName != "Tipo":
                    continue
                h = hash(item)
                if h not in classified_types:
                    continue
                code = classified_types[h]
                for desc in item.Descendants:
                    if desc.HasGeometry:
                        dh = hash(desc)
                        if dh not in covered_geo_hashes:
                            covered_geo_hashes.add(dh)
                            code_counts[code] += 1

            total_geo      = sum(1 for it in model.RootItem.Descendants if it.HasGeometry)
            classified_geo = sum(code_counts.values())
            coverage_pct   = round(classified_geo / total_geo * 100, 1) if total_geo > 0 else 0.0

            results.append({
                "model":                  model_name,
                "total_type_nodes":       len(classified_types) + len(unclassified_types),
                "classified_types":       len(classified_types),
                "unclassified_type_count": len(unclassified_types),
                "unclassified_type_names": unclassified_types,
                "total_geometry_elements": total_geo,
                "classified_geo":         classified_geo,
                "unclassified_geo":       total_geo - classified_geo,
                "coverage_pct":           coverage_pct,
                "elements_per_code":      dict(sorted(code_counts.items())),
            })
        return results


# ─── PNT Packager ─────────────────────────────────────────────────────────────

class PNTPackager:
    def pack(self, ifc_files: list, clash_data: dict,
             properties: dict, manifest: dict, out_path: Path) -> Path:
        with zipfile.ZipFile(out_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
            z.writestr("manifest.json",   json.dumps(manifest,   ensure_ascii=False, indent=2))
            z.writestr("clashes.json",    json.dumps(clash_data, ensure_ascii=False, indent=2))
            z.writestr("properties.json", json.dumps(properties, ensure_ascii=False, indent=2))
            for ifc_path in ifc_files:
                z.write(ifc_path, f"models/{ifc_path.name}")
        return out_path


# ─── Export Manager ───────────────────────────────────────────────────────────

class ExportManager:

    def __init__(self, doc, work_dir: Path):
        self._doc = doc
        self._tmp = work_dir / "_pnt_tmp"
        self._tmp.mkdir(parents=True, exist_ok=True)

    def run(self) -> Path:
        t_total = datetime.now()
        n = self._doc.Models.Count

        try:
            proj_label = Path(self._doc.FileName).stem
        except Exception:
            proj_label = "project"

        progress = ProgressWindow(f"{proj_label} — PNT Export  ({n} model(s))")
        try:
            return self._run(n, progress, t_total)
        finally:
            progress.close()

    def _run(self, n: int, progress, t_total) -> Path:
        print(f"━━━ PNT Export — {n} model(s) ━━━")

        # Shared origin offset for all GLBs in this .pnt — vital for float32
        # precision on geo-referenced models (UTM coordinates lose ~3cm/axis
        # of resolution at typical magnitudes). All models share one origin so
        # they remain co-located when loaded together.
        bb0 = self._doc.Models[0].RootItem.BoundingBox()
        origin = (
            float(bb0.Center.X) * FEET_TO_METERS,
            float(bb0.Center.Y) * FEET_TO_METERS,
            float(bb0.Center.Z) * FEET_TO_METERS,
        )
        print(f"  Origin offset: ({origin[0]:.1f}, {origin[1]:.1f}, {origin[2]:.1f}) m")

        ifc_files   = []
        model_infos = []
        properties  = {}
        bbox_index  = {}

        for i in range(n):
            model = self._doc.Models[i]
            stem  = Path(model.FileName).stem
            print(f"\n[{i+1}/{n}] {stem}")
            progress.update(phase=f"[{i+1}/{n}] {stem} — extracting geometry...", detail="")
            t0 = datetime.now()

            glb_path = self._tmp / f"{stem}.glb"

            exporter = GlbExporter()
            exporter.MaxFacesPerElement = MAX_FACES_PER_ELEMENT
            exporter.Scale       = FEET_TO_METERS
            exporter.BboxOnly    = BBOX_ONLY
            exporter.OriginX, exporter.OriginY, exporter.OriginZ = origin
            exporter.ProjectName = stem
            exporter.SkipCategoryNames.Add("Rooms")
            exporter.SkipCategoryNames.Add("Habitaciones")

            result = exporter.WriteGlb(model.RootItem, str(glb_path))
            elapsed = (datetime.now() - t0).total_seconds()
            count = int(result.ElementCount)
            mb = int(result.ByteLength) / 1_048_576
            hits = int(result.CacheHits)
            misses = int(result.CacheMisses)
            print(f"  → {count} elements, {result.OverflowedCount} bbox-replaced, "
                  f"{mb:.1f} MB GLB in {elapsed:.1f}s")
            print(f"    type cache: {misses} tessellated, {hits} reused "
                  f"({hits*100/max(count,1):.0f}% hit rate)")

            if count == 0:
                try: glb_path.unlink()
                except Exception: pass
                print("  (skipped — no geometry)")
                continue

            # Marshal per-element metadata in bulk (single bridge crossing each)
            names   = list(result.Names)
            pnt_ids = list(result.PntIds)
            centers = list(result.BboxCentersFlat)
            for k in range(count):
                pid = pnt_ids[k]
                properties[pid] = {
                    "pnt_id": pid,
                    "name":   names[k],
                    "model":  stem,
                    "psets":  {},
                }
                cx = centers[k*3]
                cy = centers[k*3 + 1]
                cz = centers[k*3 + 2]
                if cx != 0.0 or cy != 0.0 or cz != 0.0:
                    bbox_index.setdefault((stem, cx, cy, cz), []).append(pid)

            ifc_files.append(glb_path)
            model_infos.append({
                "name":     stem,
                "fileName": f"{stem}.glb",
                "fullPath": model.FileName,
            })

        print(f"\n━━━ Clash extraction ({len(model_infos)} models) ━━━")
        if EXPORT_CLASHES:
            progress.update(phase="Running clash tests...", detail="")
            clash_extractor = ClashExtractor(bbox_index, self._doc)
            tests_summary, all_clashes = clash_extractor.run(self._doc)
            print(f"  Total: {len(all_clashes)} results across {len(tests_summary)} tests")
        else:
            tests_summary, all_clashes = [], []
            print("  (skipped — EXPORT_CLASHES=False)")

        print("\n━━━ PYNET_Classification coverage ━━━")
        progress.update(phase="Analysing classification coverage...", detail="")
        t0 = datetime.now()
        classification = ClassificationAnalyzer.run(self._doc)
        elapsed = (datetime.now() - t0).total_seconds()
        for r in classification:
            print(f"  {r['model']}: {r['coverage_pct']}% coverage"
                  f"  ({r['classified_types']}/{r['total_type_nodes']} types)"
                  f"  ({r['unclassified_type_count']} unclassified)")
        print(f"  → done in {elapsed:.1f}s")

        clash_data = {
            "models":         model_infos,
            "tests":          tests_summary,
            "clashes":        all_clashes,
            "classification": classification,
            "summary": {
                "totalClashes": len(all_clashes),
                "activeTests":  sum(1 for t in tests_summary if t["clashes"] > 0),
                "totalModels":  len(model_infos),
            },
        }

        try:
            out_dir = Path(self._doc.FileName).parent
            project = Path(self._doc.FileName).stem
        except Exception:
            out_dir = self._tmp.parent
            project = "project"

        manifest = {
            "version":       "1.0",
            "format":        "pnt",
            "project":       project,
            "created":       datetime.now().isoformat(),
            "models":        [m["fileName"] for m in model_infos],
            "element_count": len(properties),
            "clash_count":   len(all_clashes),
            # World-space offset (meters) subtracted from every GLB vertex.
            # Consumers that need geo-referenced coordinates must add this back.
            "origin":        list(origin),
        }

        out_path = out_dir / f"{project}.pnt"
        print(f"\n━━━ Packaging → {out_path.name} ━━━")
        progress.update(phase="Packaging .pnt archive...", detail="")
        t0 = datetime.now()
        PNTPackager().pack(ifc_files, clash_data, properties, manifest, out_path)
        mb_out = out_path.stat().st_size / 1_048_576
        elapsed_pack = (datetime.now() - t0).total_seconds()
        print(f"  → {mb_out:.1f} MB in {elapsed_pack:.1f}s")

        for f in ifc_files:
            try:
                f.unlink()
            except Exception:
                pass
        try:
            self._tmp.rmdir()
        except Exception:
            pass

        total_s = (datetime.now() - t_total).total_seconds()
        m, s = divmod(int(total_s), 60)
        print(f"\nDone → {out_path}  (total {m}m {s}s)")
        return out_path


# ─── Entry point ──────────────────────────────────────────────────────────────

doc = Application.ActiveDocument
if doc.Models.Count == 0:
    print("No models loaded.")
else:
    try:
        work_dir = Path(doc.FileName).parent / "PNT_Export"
    except Exception:
        work_dir = Path(doc.Models[0].FileName).parent / "PNT_Export"

    ExportManager(doc, work_dir).run()
