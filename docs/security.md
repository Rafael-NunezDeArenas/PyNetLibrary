# Reference: Security & execution restrictions

Full whitelists/blocklists. All scripts are validated by a static analyzer before execution. Scope is strictly **Autodesk automation** — no file system access, no network, no system-level actions. The summary lives in `CLAUDE.md`; this is the complete reference.

> **Do NOT attempt to bypass these restrictions.** If a script needs a blocked import or call, tell the user and suggest an alternative within scope. Use `pathlib.Path`, never `os.path`.

---

## Allowed CLR assemblies (`clr.AddReference`)

- `Autodesk.Navisworks.Api`, `.ComApi`, `.Interop.ComApi`, `.Clash`
- `RevitAPI`, `RevitAPIUI` (Revit)
- `AcMgd`, `AcCoreMgd`, `AcDbMgd`, `AecBaseMgd`, `AeccDbMgd` (AutoCAD / Civil 3D)
- `System`, `System.Windows.Forms`, `System.Drawing`, `System.Collections.Generic`
- `Raen.Core.Pynet.*`, `Raen.Navisworks.Pynet.*` (any version)

Any other assembly is rejected.

## Allowed Python imports

`clr`, `sys`, `json`, `re`, `time`, `datetime`, `pathlib`, `typing`, `threading`, `collections`, `xml`, `pandas`, `plotly`, `matplotlib`, `dash`, `webbrowser`, `psutil`, `openpyxl`

- `openpyxl` requires bridge **≥ 1.4.7** (not whitelisted in 1.4.6).
- `http.server` is allowed (serving local content); the rest of `http` (`http.client`, `http.cookiejar`) remains blocked.

## Blocked Python imports

`os`, `subprocess`, `shutil`, `socket`, `ctypes`, `pickle`, `importlib`, `urllib`, `signal`, `multiprocessing`, `tempfile`, `glob`, `inspect`, `code`, `codeop`

## Blocked calls

`eval`, `exec`, `compile`, `__import__`, `getattr`, `setattr`, `delattr`, `globals`, `locals`, `vars`, `breakpoint`

## Blocked attribute access

`__builtins__`, `__subclasses__`, `__globals__`, `__code__`
