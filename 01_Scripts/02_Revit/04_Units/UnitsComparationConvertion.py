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

#region Convert Units

value = 32

# Convert to internal revit 2021 and next versions
convertToInternal = UnitUtils.ConvertToInternalUnits(value, UnitTypeId.Meters)
# Convert to internal revit before 2021
convertToInternal = UnitUtils.ConvertToInternalUnits(value, DisplayUnitType.DUT_Meters) #type: ignore

# Convert from internal 2021 and next versions
convertFromInternal = UnitUtils.ConvertFromInternalUnits(value, UnitTypeId.Meters) 
# Convert from internal revit before 2021
convertToInternal = UnitUtils.ConvertFromInternalUnits(value, DisplayUnitType.DUT_Meters) #type: ignore

OUT = convertFromInternal, convertToInternal

#endregion