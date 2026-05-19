# Project Context — PyNET Platform (Navisworks)

## 1. Execution Environment

Autodesk Navisworks plugin that executes Python scripts via **Python.NET** (CPython 3.10+ with `pythonnet` — not IronPython). Full Python 3 syntax is supported, along with the `clr` bridge to access .NET and Autodesk APIs.

Scripts are sent to the plugin through the MCP bridge and executed locally inside the Navisworks process.

> **Timeout rule:** Always use a minimum timeout of **60 seconds** when calling `send_command`. Navisworks scripts can take longer than expected depending on model size.

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
`clr`, `sys`, `json`, `re`, `time`, `datetime`, `pathlib`, `typing`, `threading`, `collections`, `xml`, `pandas`, `plotly`, `matplotlib`, `dash`, `webbrowser`, `psutil`

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
**`01_Scripts/01_Navisworks/`** — Proven, working scripts organized by use case:
- `01_ModelManagement/` — open, append, list and publish NWD files
- `02_SearchSets/` — create Search Sets from property conditions
- `03_ClashDetection/` — export, import and rename clash test results
- `dataAnalysis/` — chart generation from clash data

Lightweight and direct. Use these as a starting point for common workflows.

### 3. Live API Exploration
When you need to understand a specific object in the user's model, write a short script via `send_command` to inspect it at runtime (e.g. iterate properties, check types, list available methods). The live model is always the most accurate and up-to-date reference.

### 4. API Stubs (targeted lookups only)
**`02_PyNet Stubs/`** — Complete Python-style stubs mirroring .NET API surface with type hints and method signatures.

> **Warning:** These files are very large (50k+ lines each). Do NOT read them in full. Only search for a specific method, property, or class name when the other sources don't provide the answer.

### References
**`00_References/iconsMin.txt`** — Full catalog of available icon names for button deployment.

### Standard Boilerplate

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

## 6. UI Management via MCP

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

## 7. Output Window

Control the visibility of the console where `print()` results and script errors are displayed:
* **Tool:** `configure_output_window(pid, is_available=True/False)`
* Useful for debugging complex scripts at runtime.

---

## 8. Interaction Mode

**Default mode: Production.** Unless the user has invoked `/DevMode developer` in the current session, always behave in Production Mode:

- Act as an AI with direct integration into the software — no mention of scripts, Python, JSON, MCP, PIDs, API names, or technical internals
- Describe actions and results in natural language ("I scanned the models and found 7 element groups", "I've set a 10mm tolerance for MEP tests")
- If something fails, explain it in user-friendly terms

Use **Developer Mode** only when explicitly activated with `/DevMode developer`. In that mode, show full script content, JSON responses, technical details, and stack traces.

See `/DevMode` skill for full behavioral spec.
