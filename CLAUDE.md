# Project Context — PyNET Platform (Navisworks & Revit)

## 1. Execution Environment

PyNET supports two hosts: **Autodesk Navisworks** and **Autodesk Revit**. Both execute Python scripts via **Python.NET** (CPython 3.10+ with `pythonnet` — not IronPython). Full Python 3 syntax is supported, along with the `clr` bridge to access .NET and Autodesk APIs.

Scripts are sent to the plugin through the MCP bridge and executed locally inside the host process. Always check `list_active_instances` first to identify which host is running (Navisworks or Revit) and its PID — the boilerplate and available APIs differ between hosts.

> **Timeout rule:** Always use a minimum timeout of **60 seconds** when calling `send_command`. Scripts can take longer than expected depending on model size.

> **MCP bridge version:** Run `pip show pynet-mcp-bridge` (NOT `pynet-bridge`) using the Python 3.10 pip at `C:\Users\34655\AppData\Local\Programs\Python\Python310\Scripts\pip.exe`. Current installed version: **1.4.7**.

---

## 2. Execution Responses

### Scenario A: Success

```json
{
  "ScriptName": "SayHi_AI_Running",
  "ExecutionDate": "2026-03-30T15:42:12.8640716+02:00",
  "Status": "Success",
  "Message": "Script executed successfully",
  "PrintMessages": [
    "Hello Pablo"
  ],
  "Duration": "00:00:00.0312442",
  "Data": []
}
```

### Scenario B: Error (PythonException with StackTrace)
This is the format received when Python code fails. Analyze `Message` to auto-correct:

```json
{
  "ScriptName": "SayHi_AI_Running",
  "ExecutionDate": "2026-03-30T15:52:56.1204577+02:00",
  "Status": "Error",
  "Message": "Python.Runtime.PythonException: '(' was never closed (<string>, line 2)...",
  "PrintMessages": [],
  "Duration": "00:00:00",
  "Data": []
}
```

---

## 3. Script Output

Scripts can return structured data via a global variable that the plugin collects automatically.

### Output Variable

The variable name must be:

```
ia_Result
```

The system will look for this variable after script execution. If it does not exist, no data output will be generated.

### Print vs ia_Result

The Navisworks plugin has a visible **Output Window** where every `print()` is displayed to the user in real time. This means:

- **During iterative development** (scripts sent via `send_command`): use `ia_Result` as the primary channel to return structured data back to the AI. Keep `print` usage minimal — only for brief status messages (e.g. `"Found 41 wall types"`). Do NOT flood the Output Window with per-element or per-iteration prints.
- **When saving a script for the user** (deployed to a button or saved to source): add meaningful `print` statements so the user gets clear feedback when running the script manually (progress, results summary, confirmations). In this case, `ia_Result` is optional since the user reads the Output Window directly.

In short: `ia_Result` is for AI consumption, `print` is for user consumption. During development keep prints quiet; in final saved scripts make them informative.

Do not abbreviate output values or apply any transformation unless explicitly requested.

### Data Format

`ia_Result` must contain a JSON-serializable structure, typically:

- a list of dicts
- or a single dict

Recommended example (list of items):

```python
ia_Result = [
    {
        "type": "Wall",
        "id": 1,
        "name": "Wall A",
        "height": 3.2
    }
]
```

### Important Rules

- Data must be serializable (numbers, strings, lists, dicts)
- Never return complex Python objects (classes, API references, etc.)
- Always convert objects to `dict` before returning them
- Always include a `"type"` field in each object for easy interpretation
- Maintain a consistent structure across scripts

---

## 4. Security & Execution Restrictions

All scripts are validated by a static analyzer before execution. The scope is strictly limited to **Autodesk Navisworks automation** — no file system access, no network operations, no system-level actions.

### Allowed CLR Assemblies
Only these .NET references are permitted via `clr.AddReference`:
- `Autodesk.Navisworks.Api`, `.ComApi`, `.Interop.ComApi`, `.Clash`
- `System`, `System.Windows.Forms`, `System.Drawing`, `System.Collections.Generic`
- `Raen.Core.Pynet.*`, `Raen.Navisworks.Pynet.*` (any version)

Any other assembly will be rejected.

### Allowed Python Imports
`clr`, `sys`, `json`, `re`, `time`, `datetime`, `pathlib`, `typing`, `threading`, `collections`, `xml`, `pandas`, `plotly`, `matplotlib`, `dash`, `webbrowser`, `psutil`, `openpyxl`

> **Note (Revit):** `openpyxl` requires bridge **≥ 1.4.7** — it was not whitelisted in 1.4.6.

### Blocked Python Imports
`os`, `subprocess`, `shutil`, `socket`, `ctypes`, `pickle`, `importlib`, `http`, `urllib`, `signal`, `multiprocessing`, `tempfile`, `glob`, `inspect`, `code`, `codeop`

### Blocked Calls
`eval`, `exec`, `compile`, `__import__`, `getattr`, `setattr`, `delattr`, `globals`, `locals`, `vars`, `breakpoint`

### Blocked Attribute Access
`__builtins__`, `__subclasses__`, `__globals__`, `__code__`

### Execution Confirmation Policy
- **Read-only scripts** (querying data, exporting info, listing elements): execute directly without asking for confirmation.
- **Write scripts** (modifying the document, creating elements, deleting, updating models): ask the user for confirmation **once** before the first execution.
- If a confirmed script fails with an exception and you fix it, **re-execute immediately without asking again** — the user already approved the intent.

### Important
- Do NOT attempt to bypass these restrictions. If a script requires a blocked import or call, inform the user and suggest an alternative within the allowed scope.
- Use `pathlib.Path` instead of `os.path` for any path operations.
- All development is focused on Navisworks API interaction — never generate scripts that interact with the file system, network, or operating system directly.

---

## 5. Script Creation

When asked to generate a script, since it is an iterative process, **scripts are not saved to source until the user explicitly says so**. Prepare the script and send it directly via `send_command`.

There are multiple sources of context available. Use them in this order to be efficient:

### 1. AI History (check first)
**`AI_History/`** — Full log of every script executed through the MCP bridge across all sessions:
- **`Requests/`** — `Req_YYYYMMDD_HHMMSS_XXX.json` with the script content sent to Navisworks
- **`Responses/`** — `Res_YYYYMMDD_HHMMSS_XXX.json` with execution results (status, errors, output data)
- **Session logs** — `Pipe_Session_YYYYMMDD.log` with session-level activity

Always check here first. If a similar problem was already solved, reuse the validated pattern instead of writing from scratch.

### 2. Example Scripts (Handbook)

> **MANDATORY — Always inspect the library before writing any script from scratch.**
> Use `Glob` to list scripts in the relevant folder, then `Read` the closest match.
> The library contains validated, production-ready patterns for both Navisworks and Revit.
> Writing from scratch when a working example exists wastes time and introduces unnecessary risk.

**`01_Scripts/01_Navisworks/`** — Proven Navisworks scripts organized by use case:
- `01_ModelManagement/` — open, append, list and publish NWD files
- `02_SearchSets/` — create Search Sets from property conditions
- `03_ClashDetection/` — export, import and rename clash test results
- `dataAnalysis/` — chart generation from clash data

**`01_Scripts/02_Revit/`** — Proven Revit scripts organized by use case:
- `00_Workflow/` — model sync, NWC export, parameter updates, key schedules
- `02_Selection Filter/` — quick filters, slow filters, logical filters
- `03_Edit and Create Objects/` — walls, floors, families, transforms
- `10_Parameters/` — shared parameters, project parameters, value transfer
- `24_MEP/` — duct and electrical creation
- `23_Structure/` — beams, columns, foundations

Use `Glob("01_Scripts/02_Revit/**/*.py")` or `Glob("01_Scripts/01_Navisworks/**/*.py")` to discover scripts, then read the relevant one before writing anything.

### 3. Live API Exploration
When you need to understand a specific object in the user's model, write a short script via `send_command` to inspect it at runtime (e.g. iterate properties, check types, list available methods). The live model is always the most accurate and up-to-date reference.

### 4. API Stubs (targeted lookups only)
**`02_PyNet Stubs/`** — Complete Python-style stubs mirroring .NET API surface with type hints and method signatures.

> **Warning:** These files are very large (50k+ lines each). Do NOT read them in full. Only search for a specific method, property, or class name when the other sources don't provide the answer.

### References
**`00_References/iconsMin.txt`** — Full catalog of available icon names for button deployment.

### Standard Boilerplate — Navisworks

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

### Standard Boilerplate — Revit

When the active instance is Revit, the plugin injects a `__revit__` global that gives access to the running Autodesk Revit application. **Do not use `Application` from the Navisworks namespace — it does not exist in Revit scripts.**

```python
import clr
import System
from System import Enum, Environment
from pathlib import Path

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

# __revit__ is injected by the plugin — always use this to get the document
doc = __revit__.ActiveUIDocument.Document
```

#### Key differences from Navisworks

| | Navisworks | Revit |
|---|---|---|
| Document access | `Application.ActiveDocument` | `__revit__.ActiveUIDocument.Document` |
| Main assembly | `Autodesk.Navisworks.Api` | `RevitAPI` |
| UI access | `Application` | `__revit__.ActiveUIDocument` |
| Transaction needed for writes | No | Yes — wrap changes in `Transaction` |

#### Transactions (required for any write operation in Revit)

```python
t = Transaction(doc, "Transaction name")
t.Start()
try:
    # ... write operations ...
    t.Commit()
except:
    t.RollBack()
    raise
```

#### Getting special folder paths

Never hardcode `Path.home() / "Desktop"` — it fails when OneDrive redirects the Desktop. Use .NET's `Environment.GetFolderPath` instead:

```python
from System import Environment
desktop = Environment.GetFolderPath(Environment.SpecialFolder.Desktop)
out_path = Path(desktop) / "output.csv"
```

#### Iterating BuiltInCategory enum

```python
from System import Enum
from Autodesk.Revit.DB import BuiltInCategory

for bic in Enum.GetValues(BuiltInCategory):
    bic_int = int(bic)
    if bic_int >= 0:
        continue  # skip non-negative (invalid) values
    cat = doc.Settings.Categories.get_Item(bic)
    if cat is not None and str(cat.CategoryType) == "Model":
        ...
```

---

### CastUtils — Critical for Type Casting

pythonnet sometimes returns incorrect types, especially with interfaces. The PyNET plugin includes a static utility class `CastUtils` to correctly map objects. **Always use it when working with Clash or other interface-heavy APIs.**

```python
bundlePath = (Path.home() / "AppData" / "Roaming" / "Autodesk" / "ApplicationPlugins" / "RAEN.Navisworks.PyNET.bundle" / "Contents" / "2024")
sys.path.append(str(bundlePath))

clr.AddReference("Raen.Core.Pynet.Resources")
from Raen.Core.Pynet.Resources import CastUtils
```

Example — accessing clash tests:

```python
def ExportResults(document):
    clashDocument = CastUtils.CastTo[DocumentClash](document.Clash)
    tests = clashDocument.TestsData.Tests
```

Without `CastUtils`, `document.Clash` may return an unusable proxy object. This applies to any Navisworks API property that returns an interface type.

### Code Structure Convention

All scripts follow a class-based pattern with a single entry-point call at the bottom.

**When saving a script** (to source or deploying to a button), always use the full class-based structure and include `print` statements that give the user clear feedback (progress, summary, results). The script must be self-contained and user-friendly — the user will run it without the AI in the loop.

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
        # business logic
        print("Processing...")
        return result

class DialogManager:
    @staticmethod
    def ShowResult(data):
        MessageBox.Show(str(data), "PyNet", MessageBoxButtons.OK, MessageBoxIcon.Information)

# Entry point
FeatureManager.Run(doc)
```

---

## 6. Windows Forms in Revit Scripts

Using WinForms from PyNET inside Revit is supported but has several hard-won rules. Ignore them and you get crashes or silent context loss.

### Import order — critical

`System.Windows.Forms` contains its own `TaskDialog` class (.NET 6+). If you do `from System.Windows.Forms import *` **after** `from Autodesk.Revit.UI import TaskDialog`, the WinForms `TaskDialog` silently overwrites the Revit one and the constructor fails with "No method matches".

**Always import WinForms before Revit UI:**

```python
from Autodesk.Revit.DB import *
from System.Windows.Forms import *      # WinForms first
from System.Drawing import *
from Autodesk.Revit.UI import TaskDialog, TaskDialogCommonButtons, TaskDialogIcon  # Revit UI last — wins
```

### super().__init__() is mandatory

Python.NET 3.x requires explicit `super().__init__()` as the first line of any class that inherits from a .NET type. Without it, accessing `.Text`, `.Location`, or any .NET property crashes with `NullReferenceException`.

```python
class MyForm(Form):
    def __init__(self):
        super().__init__()   # MANDATORY — must be first
        self.Text = "Title"  # safe only after super().__init__()
```

### Application.EnableVisualStyles() / SetCompatibleTextRenderingDefault

Revit has already created Win32 windows, so both calls may throw. Wrap in try/except and never call `SetCompatibleTextRenderingDefault`:

```python
try:
    Application.EnableVisualStyles()
except Exception:
    pass
# Never call Application.SetCompatibleTextRenderingDefault() — always throws in Revit
```

### No Revit API calls inside form event handlers

Scripts run inside `IExternalEventHandler.Execute()`. When `form.ShowDialog()` starts a WinForms message loop, Revit's context is in an ambiguous state. Any Revit API call (opening documents, transactions, collectors) inside a button click handler **will fail or crash Revit**.

**Pattern: form is UI-only, all API work happens after ShowDialog returns.**

```python
class MyForm(Form):
    def __init__(self):
        super().__init__()
        self.confirmed = False
        # ... build UI

    def OnExecute(self, sender, args):
        self.confirmed = True
        self.Close()   # just close — no API calls here

    def OnCancel(self, sender, args):
        self.Close()

form = MyForm()
form.ShowDialog()

if form.confirmed:
    # All Revit API work here — we're still inside ExternalEventHandler.Execute()
    app = __revit__.Application
    doc = app.OpenDocumentFile(...)
    # transactions, collectors, etc.
```

### No Application.DoEvents()

`Application.DoEvents()` inside an ExternalEventHandler causes Revit re-entrancy and crashes. Never use it.

### TaskDialog — string hell

`Autodesk.Revit.UI.TaskDialog` is unusually painful with Python.NET 3.x. Follow these rules exactly:

**Use plain Python `str` — never `System.String(...)`.**  
`System.String` in .NET has no constructor that accepts a string (you can't `new String("text")` in C#). Python.NET exposes this, so `System.String("PyNET")` throws "No method matches". Plain `str` works because Python.NET converts it automatically.

```python
# WRONG — System.String has no string constructor
dlg = TaskDialog(System.String("PyNET"))
dlg.MainInstruction = System.String("Done!")   # same problem on properties

# CORRECT
dlg = TaskDialog("PyNET")
dlg.MainInstruction = "Done!"
```

**Import order matters — see above.** If `from System.Windows.Forms import *` comes after the Revit UI import, `TaskDialog` resolves to `System.Windows.Forms.TaskDialog` (a completely different class), and even plain `str` fails. Always import WinForms before `Autodesk.Revit.UI`.

**Full working pattern:**

```python
from Autodesk.Revit.DB import *
from System.Windows.Forms import *
from System.Drawing import *
from Autodesk.Revit.UI import TaskDialog, TaskDialogCommonButtons, TaskDialogIcon

dlg = TaskDialog("PyNET")
dlg.TitleAutoPrefix = False
dlg.MainInstruction = "Done!"
dlg.MainContent = "Both models processed correctly."
dlg.CommonButtons = TaskDialogCommonButtons.Ok
dlg.MainIcon = TaskDialogIcon.TaskDialogIconInformation
dlg.Show()
```

### Reference script

`01_Scripts/02_Revit/16_WindowsForms/OpenModelsCreateWallTest.py` — validated end-to-end example: form for confirmation, full Revit API work (open/transaction/save/close) after ShowDialog, TaskDialog result.

---

## 7. UI Management via MCP (Navisworks)

PyNET Platform allows dynamic management of the Navisworks Ribbon via the MCP protocol. You can create persistent modules and buttons that execute Python scripts.

### UI Inspection
* **Tool:** `get_pynet_ui_layout` — Returns the full UI structure. Essential for obtaining `Id` values before updating or deleting elements.

### Creation and Deployment
| Action | MCP Tool | Main Input |
| :--- | :--- | :--- |
| **Create Module** | `create_pynet_module` | Name of the new module |
| **Deploy Button** | `deploy_script_button` | `module_id`, script path, button name, icon |

### Editing and Cleanup
* **Update Button:** `update_script_button` — changes metadata (name, icon, tooltip) of an existing button.
* **Delete Button:** `delete_script_button` — removes a button from the module.
* **Delete Module:** `delete_pynet_module` — removes a module and all its buttons.

### Icons

To give buttons a professional appearance, use predefined icon names when calling `deploy_script_button`. See the full catalog in **`00_References/iconsMin.txt`** (e.g. `Gear`, `Python`, `Database`, `Search`, `Eye`, `ChartBar`, `ShieldSearch`). If none is specified, the system assigns the `Default` icon.

---

## 8. Output Window

Control the visibility of the console where `print()` results and script errors are displayed:
* **Tool:** `configure_output_window(pid, is_available=True/False)`
* Useful for debugging complex scripts at runtime.

---

## 9. Running Python — Use MCP, Always

**The MCP bridge (`send_command`) is the right tool for executing any Python task** — file generation, data processing, Excel creation, API queries — not Bash, not PowerShell. The plugin runs CPython 3.10 with pandas, openpyxl (via sys.modules), matplotlib, etc. already available.

Only fall back to Bash/PowerShell for operations that genuinely require the local OS (e.g. installing packages with pip, or git commands). If a package is missing, install it once with pip locally and then use it from MCP going forward.

If a library is missing from the whitelist and needed regularly, flag it so it can be added.

---

## 10. Interaction Mode

**Default mode: Production.** Unless the user has invoked `/DevMode developer` in the current session, always behave in Production Mode:

- Act as an AI with direct integration into the software — no mention of scripts, Python, JSON, MCP, PIDs, API names, or technical internals
- Describe actions and results in natural language ("I scanned the models and found 7 element groups", "I've set a 10mm tolerance for MEP tests")
- If something fails, explain it in user-friendly terms

Use **Developer Mode** only when explicitly activated with `/DevMode developer`. In that mode, show full script content, JSON responses, technical details, and stack traces.

See `/DevMode` skill for full behavioral spec.
