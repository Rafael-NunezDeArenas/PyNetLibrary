"""
NavisworksPNT_IFC — Exports a .pnt coordination package from the active NWF,
using IFC4 tessellated geometry instead of GLB.

.pnt is a ZIP archive containing:
    manifest.json     – project metadata
    clashes.json      – clash results in dashboard-compatible format
    properties.json   – full element property data keyed by pnt_id
    models/<n>.ifc    – IFC4 with tessellated geometry + PNT_Identity pset

Element identity:
    Each element receives a UUID4 as pnt_id, stored as the IFC GlobalId
    and in a PNT_Identity property set. Clash results are linked to elements
    by (nwc_stem, bbox_center_ft) lookup — same lookup key as GlbExporter.

Requirements:
    pip install ifcopenshell
"""

import clr
import sys
import uuid
import json
import re
import time
import zipfile
from pathlib import Path
from datetime import datetime
from collections import defaultdict

try:
    sys.stdout.reconfigure(line_buffering=True)
except Exception:
    pass

clr.AddReference("Autodesk.Navisworks.Api")
clr.AddReference("Autodesk.Navisworks.ComApi")
clr.AddReference("Autodesk.Navisworks.Interop.ComApi")
clr.AddReference("Autodesk.Navisworks.Clash")

from Autodesk.Navisworks.Api import Application
from Autodesk.Navisworks.Api.ComApi import ComApiBridge
from Autodesk.Navisworks.Api.Interop.ComApi import InwOaFragment3
from Autodesk.Navisworks.Api.Clash import DocumentClash

_bundle = (Path.home() / "AppData" / "Roaming" / "Autodesk" / "ApplicationPlugins"
           / "RAEN.Navisworks.PyNET.bundle" / "Contents" / "2027")
sys.path.append(str(_bundle))

clr.AddReference("Raen.Core.Pynet.Resources")
clr.AddReference("Raen.Navisworks.Pynet.2027")

from Raen.Core.Pynet.Resources import CastUtils  # type: ignore
from Raen.Navisworks.Pynet.Utils import TriangleMeshCollector  # type: ignore

import ifcopenshell
import ifcopenshell.guid

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from System.Windows.Forms import (Form, Label, ProgressBar, ProgressBarStyle,  # type: ignore
                                   FormBorderStyle, FormStartPosition,
                                   Application as WinApp)
from System.Drawing import Size, Font, FontStyle  # type: ignore


FEET_TO_METERS = 0.3048

# Set to False to skip clash test execution (avoids potential crash on heavy models).
EXPORT_CLASHES = True

_SKIP_CATS = {
    "Elemento", "Element",
    "Geometría", "Geometry",
    "TimeLiner",
    "Material de Autodesk", "Autodesk Material",
    "Material",
    "Transformar", "Transform",
    "Identidad", "Identity",
    "Proyecto", "Project",
    "Ubicación", "Location",
    "Orientation", "DemolishedPhaseId", "CreatedPhaseId",
    "Id", "WorksetId", "Document",
}

# Properties are stored in properties.json only — IFC elements carry just the
# PNT_Identity pset (pnt_id) so consumers can cross-reference without bloating
# the IFC files with redundant pset data.
EXPORT_PSETS_IN_IFC = False


# ─── Progress Window ──────────────────────────────────────────────────────────

class ProgressWindow:
    """Non-modal WinForms dialog — shows phase, detail line, and elapsed time."""

    def __init__(self, title: str):
        self._start = time.time()

        self._form = Form()
        self._form.Text            = "PNT/IFC Export"
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


# ─── Element Extractor ────────────────────────────────────────────────────────

class ElementExtractor:
    """
    Extracts tessellated geometry, color, material, properties and bbox center
    from each element via TriangleMeshCollector (COM callback).

    Returns list of tuples:
        (name, verts_m, faces, color, mat_name, props, cx_ft, cy_ft, cz_ft)

    cx/cy/cz are in native Navisworks feet — the same units and rounding used
    by item.BoundingBox().Center, so the bbox_index lookup matches clash items.
    """

    def __init__(self):
        self._collector = TriangleMeshCollector()

    def extract(self, model_index: int) -> list:
        """Streaming grouping by name|instanceNodeHash.
        Fragments are collected from the instance node (child of Tipo/Type) to avoid
        the Revit COM multi-instance quirk where the geometry leaf level returns all
        instances of a type combined instead of just the current one."""
        model = Application.ActiveDocument.Models[model_index]

        results    = []
        grp_key    = None
        grp_first  = None
        grp_items  = []
        grp_inst   = None  # instance node for current group

        for item in model.RootItem.DescendantsAndSelf:
            if not item.HasGeometry:
                continue

            inst_node = self._get_instance_node(item)
            inst_hash = (inst_node.GetHashCode() if inst_node is not None
                         else (item.Parent.GetHashCode() if item.Parent is not None
                               else item.GetHashCode()))
            key = str(inst_hash)

            if key != grp_key:
                result = self._flush(grp_first, grp_items, grp_inst)
                if result is not None:
                    results.append(result)
                grp_key   = key
                grp_first = item
                grp_items = []
                grp_inst  = inst_node

            grp_items.append(item)

        result = self._flush(grp_first, grp_items, grp_inst)
        if result is not None:
            results.append(result)

        return results

    @staticmethod
    def _get_instance_node(geom_leaf):
        """Walk up to find the instance node — the child of the Tipo/Type node.
        At this level Fragments() returns only this instance's geometry."""
        prev = geom_leaf
        node = geom_leaf.Parent
        while node is not None:
            cls = ""
            try: cls = node.ClassDisplayName or ""
            except: pass
            if cls == "Tipo" or cls == "Type":
                return prev
            prev = node
            node = node.Parent
        return None

    def _flush(self, first_item, items, inst_node):
        """Returns (name, sub_meshes, mat, props, cx, cy, cz) or None.
        sub_meshes = list of (verts_m, faces_1based, color) — one per geometry leaf,
        or one combined mesh when the Revit COM multi-instance quirk is detected."""
        if first_item is None:
            return None

        # Detect multi-instance quirk: instance node returns fewer frags than the leaf.
        # When detected, collect once from the instance node (avoids all-instances blob).
        # When not detected (or no inst_node), collect per leaf to preserve per-layer colors.
        multi_instance = False
        if inst_node is not None:
            try:
                inst_path = ComApiBridge.ToInwOaPath(inst_node)
                inst_fc = sum(1 for rf in inst_path.Fragments()
                              if CastUtils.CastTo[InwOaFragment3](rf) is not None)
                leaf_path = ComApiBridge.ToInwOaPath(items[0])
                leaf_fc = sum(1 for rf in leaf_path.Fragments()
                              if CastUtils.CastTo[InwOaFragment3](rf) is not None)
                multi_instance = leaf_fc > inst_fc
            except Exception:
                pass

        sub_meshes = []
        ft = FEET_TO_METERS

        def _tessellate(node):
            self._collector.Reset()
            try:
                path = ComApiBridge.ToInwOaPath(node)
                for rf in path.Fragments():
                    frag = CastUtils.CastTo[InwOaFragment3](rf)
                    if frag is not None:
                        self._collector.CollectFromFragment(frag)
            except Exception:
                pass
            if self._collector.Faces.Count == 0:
                return None, None
            verts = [[float(v[0]) * ft, float(v[1]) * ft, float(v[2]) * ft]
                     for v in self._collector.Vertices]
            faces = [[f[0]+1, f[1]+1, f[2]+1] for f in self._collector.Faces]
            return verts, faces

        if multi_instance:
            # Single mesh from instance node — color from first leaf
            verts, faces = _tessellate(inst_node)
            if verts:
                sub_meshes.append((verts, faces, self._item_color(items[0])))
        else:
            # Per-leaf tessellation — each leaf keeps its own color
            for item in items:
                verts, faces = _tessellate(item)
                if verts:
                    sub_meshes.append((verts, faces, self._item_color(item)))

        if not sub_meshes:
            return None
        return self._make_result(first_item, items, sub_meshes)

    def _make_result(self, item, group_items, sub_meshes) -> tuple:
        bmin_x = bmin_y = bmin_z = float('inf')
        bmax_x = bmax_y = bmax_z = float('-inf')
        for it in group_items:
            try:
                bb     = it.BoundingBox()
                bmin_x = min(bmin_x, float(bb.Min.X))
                bmin_y = min(bmin_y, float(bb.Min.Y))
                bmin_z = min(bmin_z, float(bb.Min.Z))
                bmax_x = max(bmax_x, float(bb.Max.X))
                bmax_y = max(bmax_y, float(bb.Max.Y))
                bmax_z = max(bmax_z, float(bb.Max.Z))
            except Exception:
                pass

        cx = cy = cz = 0.0
        if bmax_x > bmin_x:
            cx = round((bmin_x + bmax_x) / 2.0, 3)
            cy = round((bmin_y + bmax_y) / 2.0, 3)
            cz = round((bmin_z + bmax_z) / 2.0, 3)

        return (self._item_name(item), sub_meshes,
                self._item_material(item), self._item_props(item), cx, cy, cz)

    def _item_name(self, item) -> str:
        try:
            p = item
            while p is not None:
                if p.DisplayName:
                    return p.DisplayName
                p = p.Parent
            return "element"
        except Exception:
            return "element"

    def _item_color(self, item):
        try:
            col = item.FindFirstGeometry().ActiveColor
            return (col.R, col.G, col.B)
        except Exception:
            return None

    def _item_material(self, item) -> str:
        try:
            p = item.Parent
            if p and p.DisplayName:
                return p.DisplayName
            return ""
        except Exception:
            return ""

    def _item_props(self, item) -> dict:
        collected = {}
        node = item
        while node is not None:
            try:
                for pc in node.PropertyCategories:
                    cat = pc.DisplayName
                    if cat in _SKIP_CATS or cat in collected:
                        continue
                    props = {}
                    for p in pc.Properties:
                        try:
                            val = p.Value.ToDisplayString()
                            if val and val != "?":
                                props[p.DisplayName] = val
                        except Exception:
                            pass
                    if props:
                        collected[cat] = props
            except Exception:
                pass
            node = node.Parent
        return collected


# ─── IFC Writer ───────────────────────────────────────────────────────────────

class IFCWriter:
    """Builds and writes a single IFC4 file with tessellated geometry, colors,
    materials, property sets and a PNT_Identity pset carrying the pnt_id."""

    def __init__(self, project_name: str):
        self._ifc       = ifcopenshell.file(schema="IFC4")
        self._pending   = []
        self._materials = {}
        self._build_skeleton(project_name)

    def add_element(self, name: str, sub_meshes: list,
                    mat_name: str = "", pnt_id: str = None):
        """sub_meshes: list of (verts, faces, color) — one IfcTriangulatedFaceSet per entry."""
        if not sub_meshes:
            return
        ifc_guid  = ifcopenshell.guid.compress(pnt_id) if pnt_id else self._guid()
        tri_sets  = []
        for verts, faces, color in sub_meshes:
            if not verts or not faces:
                continue
            coord_list = self._ifc.createIfcCartesianPointList3D([list(v) for v in verts])
            tri_set    = self._ifc.createIfcTriangulatedFaceSet(coord_list, None, None, faces, None)
            if color is not None:
                self._apply_color(tri_set, *color)
            tri_sets.append(tri_set)
        if not tri_sets:
            return
        shape = self._ifc.createIfcShapeRepresentation(
            self._body_ctx, "Body", "Tessellation", tri_sets
        )
        geo   = self._ifc.createIfcProductDefinitionShape(None, None, [shape])
        place = self._world_placement()
        elem  = self._ifc.createIfcBuildingElementProxy(
            ifc_guid, None, name, None, None, place, geo, None
        )
        self._add_pnt_identity(elem, pnt_id or ifc_guid)
        if mat_name:
            self._associate_material(elem, mat_name)
        self._pending.append(elem)

    def save(self, path: Path) -> Path:
        if self._pending:
            self._ifc.createIfcRelContainedInSpatialStructure(
                self._guid(), None, None, None, self._pending, self._storey
            )
        self._ifc.write(str(path))
        return path

    def _guid(self) -> str:
        return ifcopenshell.guid.compress(uuid.uuid4().hex)

    def _pt(self, xyz):
        return self._ifc.createIfcCartesianPoint(list(xyz))

    def _world_placement(self):
        ax = self._ifc.createIfcAxis2Placement3D(self._pt([0.0, 0.0, 0.0]), None, None)
        return self._ifc.createIfcLocalPlacement(None, ax)

    def _tessellation(self, verts: list, faces: list, color=None):
        coord_list = self._ifc.createIfcCartesianPointList3D([list(v) for v in verts])
        tri_set    = self._ifc.createIfcTriangulatedFaceSet(coord_list, None, None, faces, None)
        if color is not None:
            self._apply_color(tri_set, *color)
        shape = self._ifc.createIfcShapeRepresentation(
            self._body_ctx, "Body", "Tessellation", [tri_set]
        )
        return self._ifc.createIfcProductDefinitionShape(None, None, [shape])

    def _apply_color(self, tri_set, r: float, g: float, b: float):
        colour    = self._ifc.createIfcColourRgb(None, r, g, b)
        rendering = self._ifc.createIfcSurfaceStyleRendering(
            colour, 0.0, None, None, None, None, None, None, "FLAT"
        )
        style = self._ifc.createIfcSurfaceStyle(None, "BOTH", [rendering])
        self._ifc.createIfcStyledItem(tri_set, [style], None)

    def _associate_material(self, element, material_name: str):
        if material_name not in self._materials:
            self._materials[material_name] = self._ifc.createIfcMaterial(
                material_name, None, None
            )
        self._ifc.createIfcRelAssociatesMaterial(
            self._guid(), None, None, None, [element], self._materials[material_name]
        )

    def _add_pnt_identity(self, element, pnt_id: str):
        ifc_props = [
            self._ifc.createIfcPropertySingleValue(
                "pnt_id", None,
                self._ifc.createIfcLabel(pnt_id),
                None
            )
        ]
        pset = self._ifc.createIfcPropertySet(
            self._guid(), None, "PNT_Identity", None, ifc_props
        )
        self._ifc.createIfcRelDefinesByProperties(
            self._guid(), None, None, None, [element], pset
        )

    def _build_skeleton(self, name: str):
        units = self._ifc.createIfcUnitAssignment([
            self._ifc.createIfcSIUnit(None, "LENGTHUNIT",  None, "METRE"),
            self._ifc.createIfcSIUnit(None, "AREAUNIT",    None, "SQUARE_METRE"),
            self._ifc.createIfcSIUnit(None, "VOLUMEUNIT",  None, "CUBIC_METRE"),
        ])
        ax2p = self._ifc.createIfcAxis2Placement3D(
            self._pt([0.0, 0.0, 0.0]),
            self._ifc.createIfcDirection([0.0, 0.0, 1.0]),
            self._ifc.createIfcDirection([1.0, 0.0, 0.0]),
        )
        self._ctx = self._ifc.createIfcGeometricRepresentationContext(
            None, "Model", 3, 1.0e-5, ax2p, None
        )
        self._body_ctx = self._ifc.createIfcGeometricRepresentationSubContext(
            "Body", "Model", None, None, None, None, self._ctx, None, "MODEL_VIEW", None
        )
        self._project = self._ifc.createIfcProject(
            self._guid(), None, name, None, None, None, None, [self._ctx], units
        )
        p0 = self._world_placement()
        self._site = self._ifc.createIfcSite(
            self._guid(), None, "Site", None, None, p0, None, None,
            "ELEMENT", None, None, None, None, None
        )
        self._building = self._ifc.createIfcBuilding(
            self._guid(), None, "Building", None, None, p0, None, None,
            "ELEMENT", None, None, None
        )
        self._storey = self._ifc.createIfcBuildingStorey(
            self._guid(), None, "Level 0", None, None, p0, None, None,
            "ELEMENT", 0.0
        )
        self._agg(self._project,  [self._site])
        self._agg(self._site,     [self._building])
        self._agg(self._building, [self._storey])

    def _agg(self, parent, children):
        self._ifc.createIfcRelAggregates(self._guid(), None, None, None, parent, children)


# ─── Clash Extractor ─────────────────────────────────────────────────────────

class ClashExtractor:
    """
    Runs all clash tests and collects results.
    Links each clash element to its pnt_id via (nwc_stem, cx, cy, cz) lookup.
    """

    def __init__(self, bbox_index: dict, doc):
        self._bix = bbox_index
        self._model_stems = {}
        for i in range(doc.Models.Count):
            model = doc.Models[i]
            self._model_stems[model.RootItem] = Path(model.FileName).stem

    def run(self, doc) -> tuple:
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
            t0      = datetime.now()
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
                all_clashes.append({
                    "Test":         test.DisplayName,
                    "Discipline":   self._discipline(test.DisplayName),
                    "Clash":        result.DisplayName,
                    "Status":       str(result.Status),
                    "Distance (m)": round(float(result.Distance), 4) if result.Distance else 0,
                    "X": round(float(center.X), 3) if center else None,
                    "Y": round(float(center.Y), 3) if center else None,
                    "Z": round(float(center.Z), 3) if center else None,
                    "Element A": self._item_name(item_a),
                    "ID A":      self._element_id(item_a),
                    "Source A":  self._nwc_stem(item_a),
                    "Type A":    self._revit_category(item_a),
                    "Element B": self._item_name(item_b),
                    "ID B":      self._element_id(item_b),
                    "Source B":  self._nwc_stem(item_b),
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
    def _element_id(item) -> str:
        if item is None:
            return ""
        try:
            parent = item.Parent
            if parent is not None:
                for cat in parent.PropertyCategories:
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
    PARAM_NAME = "PYNET_Classification"
    PARAM_CAT  = "lcldrevit_tab_type"

    @staticmethod
    def run(doc) -> list:
        results = []
        for model in doc.Models:
            model_name         = Path(model.FileName).stem
            classified_types   = {}
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

            code_counts        = defaultdict(int)
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
                "model":                   model_name,
                "total_type_nodes":        len(classified_types) + len(unclassified_types),
                "classified_types":        len(classified_types),
                "unclassified_type_count": len(unclassified_types),
                "unclassified_type_names": unclassified_types,
                "total_geometry_elements": total_geo,
                "classified_geo":          classified_geo,
                "unclassified_geo":        total_geo - classified_geo,
                "coverage_pct":            coverage_pct,
                "elements_per_code":       dict(sorted(code_counts.items())),
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

        progress = ProgressWindow(f"{proj_label} — PNT/IFC Export  ({n} model(s))")
        try:
            return self._run(n, progress, t_total)
        finally:
            progress.close()

    def _run(self, n: int, progress, t_total) -> Path:
        print(f"━━━ PNT/IFC Export — {n} model(s) ━━━")

        extractor   = ElementExtractor()
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

            elements = extractor.extract(i)
            elapsed  = (datetime.now() - t0).total_seconds()
            print(f"  {len(elements)} elements in {elapsed:.1f}s")

            if not elements:
                print("  No geometry — skipping")
                continue

            progress.update(phase=f"[{i+1}/{n}] {stem} — writing IFC...", detail="")
            t0       = datetime.now()
            ifc_path = self._tmp / f"{stem}.ifc"
            writer   = IFCWriter(stem)

            for name, sub_meshes, mat, props, cx, cy, cz in elements:
                pnt_id = uuid.uuid4().hex
                writer.add_element(name, sub_meshes, mat, pnt_id)
                properties[pnt_id] = {
                    "pnt_id": pnt_id,
                    "name":   name,
                    "model":  stem,
                    "psets":  props or {},
                }
                if cx != 0.0 or cy != 0.0 or cz != 0.0:
                    bbox_index[(stem, cx, cy, cz)] = pnt_id

            writer.save(ifc_path)
            elapsed = (datetime.now() - t0).total_seconds()
            mb = ifc_path.stat().st_size / 1_048_576
            print(f"  → {mb:.1f} MB IFC in {elapsed:.1f}s")

            ifc_files.append(ifc_path)
            model_infos.append({
                "name":     stem,
                "fileName": f"{stem}.ifc",
                "fullPath": model.FileName,
            })

        print(f"\n━━━ Clash extraction ({len(model_infos)} models) ━━━")
        if EXPORT_CLASHES:
            progress.update(phase="Running clash tests...", detail="")
            clash_extractor         = ClashExtractor(bbox_index, self._doc)
            tests_summary, all_clashes = clash_extractor.run(self._doc)
            print(f"  Total: {len(all_clashes)} results across {len(tests_summary)} tests")
        else:
            tests_summary, all_clashes = [], []
            print("  (skipped — EXPORT_CLASHES=False)")

        print("\n━━━ PYNET_Classification coverage ━━━")
        progress.update(phase="Analysing classification coverage...", detail="")
        t0             = datetime.now()
        classification = ClassificationAnalyzer.run(self._doc)
        elapsed        = (datetime.now() - t0).total_seconds()
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
            "format":        "pnt-ifc",
            "project":       project,
            "created":       datetime.now().isoformat(),
            "models":        [m["fileName"] for m in model_infos],
            "element_count": len(properties),
            "clash_count":   len(all_clashes),
        }

        out_path = out_dir / f"{project}.pnt"
        print(f"\n━━━ Packaging → {out_path.name} ━━━")
        progress.update(phase="Packaging .pnt archive...", detail="")
        t0 = datetime.now()
        PNTPackager().pack(ifc_files, clash_data, properties, manifest, out_path)
        mb_out       = out_path.stat().st_size / 1_048_576
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
        work_dir = Path(doc.FileName).parent / "PNT_IFC_Export"
    except Exception:
        work_dir = Path(doc.Models[0].FileName).parent / "PNT_IFC_Export"

    ExportManager(doc, work_dir).run()
