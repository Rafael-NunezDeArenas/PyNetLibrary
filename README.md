<p align="center">
  <img src="https://github.com/rafa2403nunez-droid/PyNetLibrary/blob/main/Assets/PyNetLibrary.png" width="300"/>
</p>

# 📚 PyNet Library — Autodesk Apps API Context

**API context and reference scripts for Autodesk applications (Navisworks, Revit, Civil 3D)**, designed for the **[PyNet Platform](https://github.com/rafa2403nunez-droid/PyNet)**. This repo provides Python-style **stubs** of the Autodesk .NET APIs and example scripts, so that AI models (and developers) have the context they need to generate and understand automation code that runs through PyNet's embedded **Python.NET** engine.

> **AI Users:** This README and the stub files under `01_Scripts/` are the primary context sources for generating scripts. Read the execution environment and boilerplate sections before writing any code.

---

## ⚡ Quick Start

If you are an AI model or developer, you can quickly verify the environment with a minimal script (Navisworks example):

```python
import clr
from Autodesk.Navisworks.Api import Application

doc = Application.ActiveDocument
print(doc.Title)
```

If this executes successfully inside PyNet, the environment is correctly configured.

This confirms:
- Python.NET is working
- The Autodesk API is accessible
- Active document context is available

---

## ⚙️ Execution Environment

Scripts run via **Python.NET** (CPython 3.10+ + `pythonnet` — not IronPython). This means standard Python 3 syntax is fully supported, along with the `clr` bridge to access .NET and Autodesk APIs.

| Property | Value |
| :--- | :--- |
| **CLR bridge** | `import clr` |
| **Standard Python** | ✅ Full Python 3.10+ |
| **pip packages** | ✅ Available |

**Key rules:**
- Always call `clr.AddReference(...)` before importing any Autodesk or System namespace.
- Use `List[T]` from `System.Collections.Generic` when passing collections to .NET methods.
- All UI dialogs use `System.Windows.Forms.MessageBox`.  


## 🧠 AI Usage Guidelines

When generating scripts for PyNet (Navisworks, Revit, Civil 3D), follow these rules:

### Structure
- Always use a class-based architecture
- Separate logic, UI, and orchestration
- Provide a single entry point (e.g. FeatureManager.Run(doc))

### Imports
- Always include required clr.AddReference(...) calls before importing .NET namespaces
- Only include imports that are required for the script to function

### API Usage
- Use Application.ActiveDocument as the entry point to the model
- Prefer strongly typed Navisworks API classes over dynamic access

### UI interaction
- Use System.Windows.Forms for dialogs
- Avoid blocking UI threads unnecessarily

### Output
- Scripts should be self-contained and executable
- Avoid external dependencies unless explicitly allowed

### Safety
- Do not use restricted Python modules
- Do not attempt file system or system-level operations

### Deterministic Behavior
- Generate predictable and repeatable scripts
- Avoid ambiguous or dynamic runtime decisions
- Prefer explicit API calls over reflection or introspection

### Consistency
- Maintain consistent naming conventions across classes
- Follow the same structure across all generated scripts

---

## 📋 Standard Boilerplate

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

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import *
from System.Drawing import *

from System.Collections.Generic import List

from Autodesk.Navisworks.Api import Application
doc = Application.ActiveDocument
```

For clash detection, add:
```python
clr.AddReference("Autodesk.Navisworks.Clash")
from Autodesk.Navisworks.Api.Clash import *
```

## 🧪 Minimal Working Example

This example verifies that the Navisworks API and PyNet execution environment are correctly configured:

```python
import clr

clr.AddReference("Autodesk.Navisworks.Api")
from Autodesk.Navisworks.Api import Application

from System.Windows.Forms import MessageBox

doc = Application.ActiveDocument

class FeatureManager:
    @staticmethod
    def Run(document):
        MessageBox.Show("Document loaded: " + document.Title)

FeatureManager.Run(doc)
```

---

## 🏗️ Code Structure Convention

All scripts follow a class-based pattern with a single entry-point call at the bottom:

```python
class FeatureManager:
    '''
    Main orchestrator class — coordinates the workflow
    by calling helper classes and presenting results to the user.
    Each public method represents a complete user action.
    '''
    @staticmethod
    def Run(document):
        data = DataProcessor.Process(document)
        DialogManager.ShowResult(data)

class DataProcessor:
    '''
    Business logic class — reads and transforms data from
    the Navisworks document. Returns plain Python objects
    that the rest of the script can consume.
    '''
    @staticmethod
    def Process(document):
        # business logic
        return result

class DialogManager:
    '''
    UI helper class — displays results or collects user input
    via System.Windows.Forms dialogs (MessageBox, OpenFileDialog, etc.).
    '''
    @staticmethod
    def ShowResult(data):
        MessageBox.Show(str(data), "PyNet", MessageBoxButtons.OK, MessageBoxIcon.Information)

# Entry point
FeatureManager.Run(doc)
```

---

## 🔍 Stub Usage

The stub files (e.g. `01_Scripts/01_Navisworks/00_Stubs/`) provide a Python-style representation of the Autodesk .NET APIs.

### Purpose
- Provide type hints and method signatures
- Help AI models understand available API surfaces
- Improve code generation accuracy
- Assist developers in navigating the API

### How to Use
- Use stubs as a reference when writing scripts manually
- Use them as context for AI-generated code
- Explore them in an IDE for navigation and API understanding
- They are not required at runtime and should not be executed directly

### Notes
- Stubs mirror the structure of the Autodesk .NET assemblies
- They are purely informational and not executed at runtime

---

## 📂 Repository Structure

This repository contains two main types of resources:

- API stubs for Autodesk .NET APIs
- Example scripts demonstrating real-world usage patterns

### Navisworks — 01_Scripts/01_Navisworks/

Working scripts organized by use case:

- **Model Management** (`01_ModelManagement/`) — open, append, list and publish NWD files using the core Document API.
- **Search Sets** (`02_SearchSets/`) — create Search Sets from property conditions (`SearchCondition`, `VariantData`, `SearchLocations`).
- **Clash Detection** (`03_ClashDetection/`) — export, import, rename and run clash tests, working with `doc.Clash.TestsData.Tests`.
- **Data Analysis** (`04_DataAnalysis/`) — chart generation from clash data (bar charts, pie charts, stacked bars).
- **Query Elements** (`05_QueryElements/`) — search and isolate model elements by property filters.
- **Workflows** (`06_Workflows/`) — end-to-end automation: model federation updates, coordination workflows with backup, clash execution, and NWD publishing.

### Revit — 01_Scripts/02_Revit/ *(coming soon)*

### Civil 3D — 01_Scripts/03_Civil3D/ *(coming soon)*

Example — `SearchSetsManager.CreateSet` from 02_SearchSets/GenerateSearchSets.py:

```python
import clr

clr.AddReference("Autodesk.Navisworks.Api")
from Autodesk.Navisworks.Api import *

clr.AddReference("Autodesk.Navisworks.ComApi")
from Autodesk.Navisworks.Api.ComApi import *

clr.AddReference("Autodesk.Navisworks.Interop.ComApi")
from Autodesk.Navisworks.Api.Interop.ComApi import *

clr.AddReference("Autodesk.Navisworks.Clash")
from Autodesk.Navisworks.Api.Clash import *

from System.Collections.Generic import List

from Autodesk.Navisworks.Api import Application 
doc = Application.ActiveDocument

class SearchSetsManager():
    @staticmethod
    def CreateSet(value, selectionSets):
        '''
        Creates a new Search Set filtered by a property value.
        Searches "Clash Test Code" under both "Revit Type" and "Element"
        categories (OR logic via separate groups), then registers the
        resulting set in the document's SelectionSets collection.
        '''
        searchSet = Search()
        searchSet.Locations = SearchLocations.DescendantsAndSelf
        searchSet.Selection.SelectAll()

        # First condition group — match by "Revit Type" category
        condition = SearchCondition.HasPropertyByDisplayName("Revit Type", "Clash Test Code")
        conditionValue = condition.EqualValue(VariantData.FromDisplayString(value))
        searchSet.SearchConditions.AddGroup(List[SearchCondition]([conditionValue]))

        # Second condition group (OR) — match by "Element" category
        conditionOr = SearchCondition.HasPropertyByDisplayName("Element", "Clash Test Code")
        conditionValueOr = conditionOr.EqualValue(VariantData.FromDisplayString(value))
        searchSet.SearchConditions.AddGroup(List[SearchCondition]([conditionValueOr]))

        # Create the SelectionSet and add it to the document
        instance = SelectionSet(searchSet)
        instance.DisplayName = value
        selectionSets.AddCopy(instance)
```

---

## 🗒️ Common Patterns

Below are frequently used patterns when working with the Navisworks API:

```python
### Access Active Document

doc = Application.ActiveDocument

### Iterate Model Items

for item in doc.Models[0].RootItem.DescendantsAndSelf:
    print(item.DisplayName)

### Access Properties

props = item.PropertyCategories

### Working with Selection Sets

selection_sets = doc.SelectionSets

### Run a Search

search = Search()
search.Selection.SelectAll()
```

---

## ❓ FAQs

Have questions about installation, configuration, or usage? Check the full FAQ page:

👉 [PyNet FAQs](https://github.com/rafa2403nunez-droid/PyNet/wiki/PyNET-FAQs)

---

## 🔗 How This Library Fits Into the Ecosystem

This library is part of a modular system designed to enable AI-driven BIM automation across Autodesk tools.

This repository is designed to work alongside:

- PyNet Platform → Executes scripts inside Navisworks via Python.NET  
- PyNet Bridge (MCP) → Connects AI models to PyNet using IPC  

Together, these components enable:

Natural Language → AI → Python Script → PyNet → Navisworks / Revit / Civil 3D → BIM Action

| Component | Repository | Purpose |
| :--- | :--- | :--- |
| **PyNet Platform** | [rafa2403nunez-droid/PyNet](https://github.com/rafa2403nunez-droid/PyNet) | Navisworks/Revit plugin — hosts the Python.NET engine |
| **PyNet Bridge (MCP)** | [rafa2403nunez-droid/PyNetBridge](https://github.com/rafa2403nunez-droid/PyNetBridge) | MCP server - connects AI models to PyNET with including secure scripts validation|
| **PyNet Library** | This repo | Script reference library and AI context |

To have AI generate and execute scripts live against Navisworks or Revit, install the MCP server:

```powershell
irm https://raw.githubusercontent.com/rafa2403nunez-droid/PyNetBridge/main/install.ps1 | iex
```

This auto-detects and configures **Claude Desktop**, **Claude Code**, **Cline**, and **Roo Code**.

---

## 🖥️ BIM Viewer & Coordination Dashboard (03_Viewer)

Embeddable web component built with **ThatOpen Components** for visualizing federated IFC models alongside coordination data (clash detection) exported from Navisworks.

### Structure

```
03_Viewer/
  src/           → Viewer TypeScript (ThatOpen + Three.js)
  dashboard/     → Dashboard HTML + Plotly (clash table, charts)
  server/        → Standalone Python HTTP server (serve.py)
  public/worker/ → Web Worker for fragment parsing
  dist/          → Production build (generated with vite build)
```

### Launch from Navisworks (recommended)

The dashboard is launched directly from Navisworks via a Ribbon button:

**Tab "Dashboard"** → Button **"Export Clashes"**

This opens a WinForms dialog with two actions:
1. **Export Clashes** — runs all clash tests and exports `clashes.json` to the IFC directory of the active model
2. **Launch Dashboard** — starts the web server in a thread, automatically kills any previous server on the same port, and opens the browser

The script is located at `01_Scripts/01_Navisworks/04_DataAnalysis/ExportClashDashboard.py`.

> **Important limitation:** The web server (Dash/Flask) only works when launched from a **WinForms** context (`Form.ShowDialog()`). Launching Dash from a direct MCP script (`send_command`) causes a deadlock due to the Python.NET GIL. This is why the script uses a Form as its entry point — the server thread is created from the Form button event, not from the MCP context.

### Launch from PowerShell (development/troubleshooting only)

> **This method requires user approval.** The standard workflow is always from Navisworks (button or MCP). PowerShell is only used for development or when the Ribbon button is not available.

<details>
<summary>Show PowerShell instructions</summary>

**Step 1 — Export data from Navisworks (via MCP or button)**

**Step 2 — Start the HTTP server**

```powershell
cd C:\Users\RafaelNúñezdeArenas\source\repos\GithubRNM\PyNetLibrary\03_Viewer
python server\serve.py --ifc-dir "C:\path\to\ifcs" --port 8095
```

**Step 3 — Open the dashboard**

```
http://localhost:8095/
```

**Standalone viewer (viewer only, no dashboard)**

```
http://localhost:8095/viewer/?models=model1.ifc,model2.ifc
```
</details>

### Rebuild the viewer (after changes in src/)

```powershell
cd C:\Users\RafaelNúñezdeArenas\source\repos\GithubRNM\PyNetLibrary\03_Viewer
npm install
npm run build
```

### Development with hot-reload

```powershell
cd C:\Users\RafaelNúñezdeArenas\source\repos\GithubRNM\PyNetLibrary\03_Viewer
npm run dev
# Vite at http://localhost:5173 — requires serve.py on port 8080 for IFC files
python server\serve.py --ifc-dir "C:\path\to\ifcs" --port 8080
```

### Viewer public API (for integration)

| Function | Description |
| :--- | :--- |
| `window.loadModel(url, name)` | Loads an IFC model by URL |
| `window.highlightElements(modelId, expressIds)` | Highlights elements (clash navigation) |
| `window.fitToAllModels()` | Fits camera to all loaded models |
| `postMessage({ type: "viewer-command", ... })` | iframe ↔ dashboard communication |

---

## ⚠️ Notes and Limitations

### Runtime Limitations
- Scripts run inside the Autodesk application context (Navisworks, Revit, Civil 3D)
- File system and OS-level operations are restricted
- Certain Python standard libraries are not available due to security constraints

### Compatibility
- Requires Autodesk applications with Python.NET support via PyNet Platform
- Compatible with Python 3.10+
- **Python 3.14 is not yet supported.** The `pythonnet` runtime currently supports Python 3.7 through 3.13. If you encounter a `System.NotSupportedException` mentioning an unsupported ABI version, install Python 3.12 or 3.13 and configure PyNet to use it.
- Behavior may vary depending on application version
- API access depends on Autodesk application version and edition compatibility

---

© 2026 RAEN Digital Tools. Todos los derechos reservados.
Obra inscrita en el Registro de la Propiedad Intelectual de la Comunidad de Madrid.

<p align="center">
  <img src="https://github.com/rafa2403nunez-droid/PyNetLibrary/blob/main/Assets/RAENDigitalTools.png" alt="RAEN Digital Tools" width="200">
</p>
