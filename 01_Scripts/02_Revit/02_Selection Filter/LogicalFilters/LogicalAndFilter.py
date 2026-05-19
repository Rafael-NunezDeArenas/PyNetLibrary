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

# endregion

# region Logical And Filter

# Element Is Element Type Filter
elementTypeFilter = ElementIsElementTypeFilter()

# MultiCategoryFilter
categories = [BuiltInCategory.OST_Walls, BuiltInCategory.OST_Doors]
categories = List[BuiltInCategory](categories)
multiCategoryFilter = ElementMulticategoryFilter(categories)

# Logical And Filter
filters = List[ElementFilter]([multiCategoryFilter, elementTypeFilter])
logicalFilter = LogicalAndFilter(filters)

# Collect Elements
collector = FilteredElementCollector(doc).WherePasses(logicalFilter).ToElements()

OUT = collector 

# endregion