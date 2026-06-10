# Guide: Navisworks scripts

Read this guide **before writing any Navisworks script**. It holds the host boilerplate, CastUtils casting, and the saved-script structure convention.

Related: [revit.md](revit.md) · [autocad-civil.md](autocad-civil.md) · [winforms.md](winforms.md)

---

## Standard boilerplate

```python
import clr
import sys
from pathlib import Path

clr.AddReference("Autodesk.Navisworks.Api")
from Autodesk.Navisworks.Api import *

clr.AddReference("Autodesk.Navisworks.ComApi")
from Autodesk.Navisworks.Api.ComApi import *

clr.AddReference("Autodesk.Navisworks.Interop.ComApi")
from Autodesk.Navisworks.Api.Interop.ComApi import *

clr.AddReference("Autodesk.Navisworks.Clash")
from Autodesk.Navisworks.Api.Clash import *

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import *
from System.Drawing import *
from System.Collections.Generic import List

from Autodesk.Navisworks.Api import Application
doc = Application.ActiveDocument
```

> Navisworks uses `Application.ActiveDocument`. This `Application` does **not** exist in Revit scripts — see [revit.md](revit.md).

---

## CastUtils — critical for type casting

pythonnet sometimes returns incorrect types, especially with interfaces (Clash API). The PyNET plugin ships a static utility `CastUtils` to correctly map objects. **Always use it when working with Clash or other interface-heavy APIs.**

```python
bundlePath = (Path.home() / "AppData" / "Roaming" / "Autodesk" / "ApplicationPlugins"
              / "RAEN.Navisworks.PyNET.bundle" / "Contents" / "2027")
sys.path.append(str(bundlePath))

clr.AddReference("Raen.Core.Pynet.Resources")
from Raen.Core.Pynet.Resources import CastUtils
```

> **Version note:** this machine has Navisworks **2027** installed — use the `2027` folder, not `2024`. If `clr.AddReference` fails, detect the real version by reading `asm.Location` via reflection instead of hardcoding.

Example — accessing clash tests:

```python
def ExportResults(document):
    clashDocument = CastUtils.CastTo[DocumentClash](document.Clash)
    tests = clashDocument.TestsData.Tests
```

Without `CastUtils`, `document.Clash` may return an unusable proxy object. This applies to any Navisworks API property that returns an interface type.

---

## Key API patterns (this project)

- **Tolerances are in feet** when configuring clash tests.
- Create **SearchSets before clash tests** so the tests stay dynamic.
- See `01_Scripts/01_Navisworks/` for validated examples by use case:
  - `01_ModelManagement/` — open, append, list, publish NWD
  - `02_SearchSets/` — Search Sets from property conditions
  - `03_ClashDetection/` — export, import, rename, run clash tests
  - `04_DataAnalysis/` / `08_DataAnalysis/` — chart & dashboard generation
  - `05_QueryElements/` — isolate, query custom category values, measurements
  - `07_IFCExport/` — NWC/NWD → IFC export pipeline

---

## Code structure convention (saved scripts)

When **saving** a script (to source or deploying to a button), use the full class-based structure with a single entry-point call at the bottom, and add informative `print` statements (progress, summary, results). The user runs it without the AI in the loop.

```python
class FeatureManager:
    @staticmethod
    def Run(document):
        data = DataProcessor.Process(document)
        print(f"Processed {len(data)} elements")
        DialogManager.ShowResult(data)

class DataProcessor:
    @staticmethod
    def Process(document):
        print("Processing...")
        return result

class DialogManager:
    @staticmethod
    def ShowResult(data):
        MessageBox.Show(str(data), "PyNet", MessageBoxButtons.OK, MessageBoxIcon.Information)

# Entry point
FeatureManager.Run(doc)
```
