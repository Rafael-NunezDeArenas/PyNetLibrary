import clr

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from Autodesk.Revit.DB import *
from System.Windows.Forms import *
from System.Drawing import *
from Autodesk.Revit.UI import TaskDialog, TaskDialogCommonButtons, TaskDialogIcon

uidoc = __revit__.ActiveUIDocument  #type:ignore
doc = uidoc.Document


class TaskdialogResults:
    @staticmethod
    def ShowCancelTaskDialog():
        dialog = TaskDialog("Activate views")
        dialog.MainInstruction = "Nothing selected"
        dialog.MainContent = "It is necessary to select at least one view to activate."
        dialog.TitleAutoPrefix = False
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconWarning
        dialog.Show()


class ViewManager:
    @staticmethod
    def ActivateView(elementId):
        try:
            view = doc.GetElement(elementId)
            uidoc.RequestViewChange(view)
        except:
            pass


class ActivateViewsScript:
    @staticmethod
    def Run(uidoc):
        if uidoc.Selection.GetElementIds().Count > 0:
            viewIds = uidoc.Selection.GetElementIds()
            for elementId in viewIds:
                ViewManager.ActivateView(elementId)
            print(f"Activated {viewIds.Count} view(s).")
        else:
            TaskdialogResults.ShowCancelTaskDialog()


ActivateViewsScript.Run(uidoc)
