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
        return result
    # If Unit Filter None Return None
    elif unitFilter == None:
        return None

gridRange = range(0, 5)
gridDiference = 3

def CreateGrids(start, end, range, diference, bool = True):
    grids = []
    if bool == True:
        for value in range:
            line = Line.CreateBound(start, end)
            grid = Grid.Create(doc, line)
            grid.Name = "Grid_Y_" + str(value)
            grid.SetVerticalExtents(ConvertUnits(-1, "meters"), ConvertUnits(5, "meters"))
            start = XYZ(start.X + ConvertUnits(diference, "meters"), start.Y, start.Z)
            end = XYZ(end.X + ConvertUnits(diference, "meters"), end.Y, end.Z)
            grids.append(grid)
    if bool == False:
        for value in range:
            line = Line.CreateBound(start, end)
            grid = Grid.Create(doc, line)
            grid.Name = "Grid_X_" + str(value)
            grid.SetVerticalExtents(ConvertUnits(-1, "meters"), ConvertUnits(5, "meters"))
            start = XYZ(start.X, start.Y + ConvertUnits(diference, "meters") , start.Z)
            end = XYZ(end.X, end.Y + ConvertUnits(diference, "meters"), end.Z)
            grids.append(grid)
    
    return grids

with Transaction(doc) as tx:
    tx.Start("Create Grids")
    
    gridStartPoint = XYZ.Zero
    gridEndPoint = XYZ(0, ConvertUnits(5, "meters"), 0)
    gridsX = CreateGrids(gridStartPoint, gridEndPoint, gridRange, gridDiference)
    gridStartPoint = XYZ.Zero
    gridEndPoint = XYZ(ConvertUnits(5, "meters"), 0, 0)
    gridsY = CreateGrids(gridStartPoint, gridEndPoint, gridRange, gridDiference, False)

    tx.Commit()

OUT = gridsX, gridsY