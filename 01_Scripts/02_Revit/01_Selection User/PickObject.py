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
            height = UnitUtils.ConvertFromInternalUnits(element.get_Parameter(BuiltInParameter.WALL_USER_HEIGHT_PARAM).AsDouble(), UnitTypeId.Meters) #type: ignore
            if height < 3:
                return True
            else:
                return False
        else:
            return False
    def AllowReference(self, reference, position):
        return True

# Get Reference in the Revit Interface
reference = None
try:
    reference = uidoc.Selection.PickObject(ObjectType.Element, WallSelectionFilter(), "Select a Wall: ")
except OperationCanceledException as ex:
    TaskDialog.Show("Revit API", ex.Message)

# Get Element
if reference != None:
    element = doc.GetElement(reference)
    OUT = element
else:
    OUT = ex.Message

# endregion


