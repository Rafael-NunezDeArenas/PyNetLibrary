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

from difflib import SequenceMatcher

#endregion

#region Convert Units

value = IN[0] #type:ignore
unitName = IN[1] #type:ignore
bool = IN[2] #type:ignore

def ConvertUnits(value, unitName, bool = True):
    # Get All Units
    units = UnitUtils.GetAllUnits()
    unit = None
    # Search a Unit Almost Equal to Input
    for unit in units:
        name = UnitUtils.GetTypeCatalogStringForUnit(unit)
        ratio = SequenceMatcher(a = name, b = unitName.ToUpper()).ratio()
        if ratio > 0.85:
            unitFilter = unit
            break
        else:
            pass
    # Convert Unit if Unit is Diferent to None
    if unitFilter != None:
        if bool == True:
            result = UnitUtils.ConvertToInternalUnits(value, unitFilter)
            name = UnitUtils.GetTypeCatalogStringForUnit(unit)
        if bool == False:
            result = UnitUtils.ConvertFromInternalUnits(value, unitFilter)
            name = UnitUtils.GetTypeCatalogStringForUnit(unit)
        return result, name
    # If Unit Filter None Return None
    elif unitFilter == None:
        return None

OUT = ConvertUnits(value, unitName)

#endregion