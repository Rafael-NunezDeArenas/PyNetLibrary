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

# region Logical Or Filter

# Element Category Door
doorsFilter = ElementCategoryFilter(BuiltInCategory.OST_Doors)

# Element Category Windows
windowsFilter = ElementCategoryFilter(BuiltInCategory.OST_Windows)

# Logical Or Filter
filters = List[ElementFilter]([doorsFilter, windowsFilter])
logicalFilter = LogicalOrFilter(filters)

# Collect Elements
collector = FilteredElementCollector(doc).WherePasses(logicalFilter).ToElements()

OUT = collector 

# endregion