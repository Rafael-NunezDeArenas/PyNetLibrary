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

# region Pick Objects In User Interface merging with a Preselection

# Get Current Selection
currentSelection = uidoc.Selection.GetElementIds()

# Obtain Reference for Selection
currentReferences = []
for id in currentSelection:
    element = doc.GetElement(id)
    currentReferences.append(Reference.ParseFromStableRepresentation(uidoc.Document, element.UniqueId))

currentReferences = List[Reference](currentReferences)

# Create ISelectionFilter Class. Select Elements that are Walls
class WallSelectionFilter(ISelectionFilter):
    def AllowElement(self, element):
        if element.__class__ == Wall:
            return True
        else:
            return False
    def AllowReference(self, reference, position):
        return True

# Get Reference in the Revit Interface including the Current Selection
references = None
try:
    references = uidoc.Selection.PickObjects(ObjectType.Element, WallSelectionFilter(), "Select a Walls and Select Finish: ", currentReferences)
except OperationCanceledException as ex:
    TaskDialog.Show("Revit API", ex.Message)

# Get Element
if references != None:
    elements = [doc.GetElement(reference) for reference in references]
    OUT = elements
else:
    OUT = ex.Message

# endregion