# Reference: Security & execution restrictions

Full whitelists/blocklists. The summary lives in `CLAUDE.md`; this is the complete reference. It mirrors the
validator in `PyNetBridge/pynet_mcp/server.py` — keep both in sync.

> **Scope:** this static analyzer only runs for scripts sent through the **MCP bridge** into an Autodesk
> host (Navisworks / Revit / AutoCAD). **Standalone QGIS scripts** (`04_QGIS`) run in QGIS's own Python and
> do **not** pass through it — see [qgis.md](qgis.md). Scripts a user writes/saves and runs from a button
> also skip the validator.

> **Do NOT attempt to bypass these restrictions.** If a script needs a blocked import or call, tell the user and suggest an alternative within scope. Use `pathlib.Path`, never `os.path`.

---

## Allowed CLR assemblies (`clr.AddReference`)

- `Autodesk.Navisworks.Api`, `.ComApi`, `.Interop.ComApi`, `.Clash`
- `RevitAPI`, `RevitAPIUI` (Revit)
- `AcMgd`, `AcCoreMgd`, `AcDbMgd`, `AecBaseMgd`, `AecPropDataMgd`, `AeccDbMgd`, `ManagedMapApi` (AutoCAD / Civil 3D / Map 3D)
- `System`, `System.Windows.Forms`, `System.Drawing`, `System.Collections.Generic`
- `Raen.Core.Pynet.*`, `Raen.Navisworks.Pynet.*`, `Raen.Revit.Pynet.*`, `Raen.Civil3D.Pynet.*` (any version)

`from Autodesk.* import …` / `from System import …` pass because the import root (`Autodesk`, `System`) is
whitelisted. Any other assembly / root is rejected.

## Allowed Python imports

`clr`, `sys`, `json`, `re`, `time`, `datetime`, `pathlib`, `typing`, `threading`, `collections`, `xml`, `math`, `functools`, `pandas`, `plotly`, `matplotlib`, `dash`, `webbrowser`, `psutil`, `openpyxl`, `uuid`, `zipfile`, `io`, `mimetypes`, `difflib`, `csv`, `ifcopenshell`, `qgis`, `processing`, `webview`, `flask`

Project-local shared modules also allowed: `pynet_clash`, `CoordinationDashboard`.

- `openpyxl` requires bridge **≥ 1.4.7** (not whitelisted in 1.4.6).

### Submodule-level allows (the bare root is NOT allowed)

- `http.server` — serving local content (not `http.client` / `http.cookiejar`).
- `urllib.request` — **outbound network**, for GIS data fetches (catastro / WFS / MDT). `import urllib` alone is rejected.
- `urllib.parse` — URL building/encoding only (no network).

## Blocked Python imports

`os`, `subprocess`, `shutil`, `socket`, `ctypes`, `pickle`, `importlib`, `signal`, `multiprocessing`, `tempfile`, `glob`, `inspect`, `code`, `codeop`

## Blocked calls

`eval`, `exec`, `compile`, `__import__`, `getattr`, `setattr`, `delattr`, `globals`, `locals`, `vars`, `breakpoint`

## Blocked attribute access

`__builtins__`, `__subclasses__`, `__globals__`, `__code__`
