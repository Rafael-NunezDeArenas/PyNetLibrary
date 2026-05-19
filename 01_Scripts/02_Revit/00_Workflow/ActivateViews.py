#region References

# Load the Python Standard and DesignScript Libraries
import clr
import sys

sys.path.append("C:\\Program Files (x86)\\IronPython 2.7\\Lib")
import os

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import *
import Autodesk

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

#Import Windows form
clr.AddReference("System.Windows.Forms")
# Import System Drawing
clr.AddReference("System.Drawing")

from System.Windows.Forms import*
from System.Drawing import*
from System.Collections.Generic import List
from datetime import date

uidoc = __revit__.ActiveUIDocument #type:ignore
doc = uidoc.Document

#endregion

#region Activate Multiple Views

# Generate TaskDialog Options Class
class TaskdialogResults:
# Define Show Cancel TaskDialog Method
    @staticmethod
    def ShowCancelTaskDialog():
        dialog = TaskDialog("Activate views")
        dialog.MainInstruction = "Nothing selected"
        dialog.MainContent = "It is necessary to select at less one view to activate."
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


if uidoc.Selection.GetElementIds().Count > 0:
	viewIds = uidoc.Selection.GetElementIds()
	for elementId in viewIds:
		ViewManager.ActivateView(elementId)
else:
	TaskdialogResults.ShowCancelTaskDialog()


#endregion