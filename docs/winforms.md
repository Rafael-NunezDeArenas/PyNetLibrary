# Guide: Windows Forms (Revit, AutoCAD & Civil 3D)

Read this guide **before writing any script that shows a form, dialog, or custom UI**. These rules are hard-won; ignoring them causes crashes or silent context loss.

Related: [revit.md](revit.md) · [autocad-civil.md](autocad-civil.md)

---

## Core rules (all hosts)

### Import order — critical

`System.Windows.Forms` has its own `TaskDialog` (.NET 6+). If `from System.Windows.Forms import *` runs **after** the Revit UI import, the WinForms `TaskDialog` silently overwrites the Revit one. **Always import WinForms before Revit UI:**

```python
from Autodesk.Revit.DB import *
from System.Windows.Forms import *      # WinForms first
from System.Drawing import *
from Autodesk.Revit.UI import TaskDialog, TaskDialogCommonButtons, TaskDialogIcon  # Revit UI last — wins
```

### super().__init__() is mandatory

Python.NET 3.x requires explicit `super().__init__()` as the first line of any class inheriting from a .NET type. Without it, accessing `.Text`, `.Location`, etc. crashes with `NullReferenceException`.

```python
class MyForm(Form):
    def __init__(self):
        super().__init__()   # MANDATORY — must be first
        self.Text = "Title"
```

### EnableVisualStyles / SetCompatibleTextRenderingDefault

The host already created Win32 windows, so these may throw. Wrap in try/except and never call `SetCompatibleTextRenderingDefault`:

```python
try:
    Application.EnableVisualStyles()
except Exception:
    pass
# Never call Application.SetCompatibleTextRenderingDefault() — always throws in the host
```

### No host API calls inside form event handlers

Scripts run inside `IExternalEventHandler.Execute()` (Revit) / a command context (AutoCAD). When `form.ShowDialog()` starts the WinForms message loop, the host context is ambiguous. **Any host API call inside a button click handler will fail or crash.**

**Pattern: form is UI-only; all API work happens after `ShowDialog()` returns.**

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
    # All host API work here — still inside ExternalEventHandler.Execute()
    ...
```

### No Application.DoEvents()

`Application.DoEvents()` inside an ExternalEventHandler causes re-entrancy and crashes. Never use it.

---

## Revit TaskDialog — string hell

`Autodesk.Revit.UI.TaskDialog` is painful with Python.NET 3.x.

**Use plain Python `str` — never `System.String(...)`.** `System.String` has no string constructor, so `System.String("PyNET")` throws "No method matches". Plain `str` is auto-converted.

```python
# WRONG
dlg = TaskDialog(System.String("PyNET"))
dlg.MainInstruction = System.String("Done!")

# CORRECT
dlg = TaskDialog("PyNET")
dlg.MainInstruction = "Done!"
```

Full working pattern:

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

---

## AutoCAD / Civil 3D specifics

The same core rules apply. For opening and saving external DWG files from a form, see the two validated patterns (Background / UI) in [autocad-civil.md](autocad-civil.md).

---

## Reference scripts

- `01_Scripts/02_Revit/16_WindowsForms/OpenModelsCreateWallTest.py` — Revit: confirmation form, full API work after ShowDialog, TaskDialog result.
- `01_Scripts/03_AutoCAD/04_WinForms/EditDwg_Background.py` — AutoCAD Pattern A.
- `01_Scripts/03_AutoCAD/04_WinForms/EditDwg_WithUI.py` — AutoCAD Pattern B.
