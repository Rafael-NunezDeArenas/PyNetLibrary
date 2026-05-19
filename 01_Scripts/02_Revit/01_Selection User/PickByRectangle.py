#region References

# Load the Python Standard and DesignScript Libraries
import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import *
from Autodesk.Revit.Exceptions import OperationCanceledException

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *


from System.Collections.Generic import List

#Import Windows form
clr.AddReference("System.Windows.Forms")
# Import System Drawing
clr.AddReference("System.Drawing")

from System.Windows.Forms import*
from System.Drawing import*

uidoc = __revit__.ActiveUIDocument #type:ignore
doc = uidoc.Document

# endregion

# region Pick Object In User Interface

# Create ISelectionFilter Class. Select Elements that are Walls
class WallSelectionFilter(ISelectionFilter):
    def AllowElement(self, element):
        if element.__class__ == Wall:
            return True
        else:
            return False
    def AllowReference(self, reference, position):
        return True

# Get Elements in the Revit Interface
elements = None
try:
    elements = uidoc.Selection.PickElementsByRectangle(WallSelectionFilter(), "Select a Walls with Rectangle Selection: ")
except OperationCanceledException as ex:
    TaskDialog.Show("Revit API", ex.Message)

# Get Element
if not elements:
    OUT = ex.Message
else:
    OUT = elements

# endregion