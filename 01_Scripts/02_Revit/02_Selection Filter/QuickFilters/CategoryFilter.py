#region References

# Load the Python Standard and DesignScript Libraries
import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

from System.Collections.Generic import List

#Import Windows form
clr.AddReference("System.Windows.Forms")
# Import System Drawing
clr.AddReference("System.Drawing")

from System.Windows.Forms import*
from System.Drawing import*

uidoc = __revit__.ActiveUIDocument #type:ignore
doc = uidoc.Document

#region Category Filter

# This Category Filter accept a Inverse including true
categoryFilter = ElementCategoryFilter(BuiltInCategory.OST_Walls)
collectorFilter = FilteredElementCollector(doc).WherePasses(categoryFilter).WhereElementIsNotElementType().ToElements()

# Collect Elements without Filter Creation
collectorSimplified = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()

# Show Elements in Revit
ids = List[ElementId]()

for n in collectorSimplified:
    ids.Add(n.Id)

uidoc.Selection.SetElementIds(ids)
uidoc.ShowElements(ids)

print("\n".join([e.Name for e in collectorFilter]))

OUT = collectorFilter, collectorSimplified

#endregion