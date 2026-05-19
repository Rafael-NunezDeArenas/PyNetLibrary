#region References

# Load the Python Standard and DesignScript Libraries
import string
import sys
import clr

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from System.Collections.Generic import List

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

# Import Windows form
clr.AddReference("System.Windows.Forms")
# Import System Drawing
clr.AddReference("System.Drawing")

import System
from System.Windows.Forms import*
from System.Drawing import*

from datetime import date

# Analyze the Coincidence of the Unit Names
from difflib import SequenceMatcher

#endregion

#region Transaction

polygons = IN[0] #type: ignore
floorType = UnwrapElement(IN[1]) #type: ignore
wallType = UnwrapElement(IN[2]) #type: ignore
offset = IN[3]  #type: ignore

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

def GetPolygonCenter(elements):
	result = []
	for element in elements:
		center = Polygon.Center(element).ToXyz()
		result.append(center)	
	return result

def GetPolygonArrays(elements):
	result = []
	for element in elements:
		lines = Polygon.Curves(element)
		curves = [line.ToRevitType() for line in lines]
		array = CurveArray()
		for curve in curves:
			array.Append(curve) 
		result.append(array)
	return result
	
def GenerateLevels(points, prefix):
	levels = []
	currentLevels = FilteredElementCollector(doc).OfClass(Level).WhereElementIsNotElementType().ToElements()
	for point in points:
		updated = False
		for current in currentLevels:
			if current.Elevation == point.Z and current.Name.Contains(prefix):
				updated = True
				levels.append(current)
				pass
			if current.Elevation == point.Z and current.Name.Contains(prefix) == False:
				current.Name = prefix + str(points.index(point))
				updated = True
				levels.append(current)
				pass
		if updated == False:
			level = Level.Create(doc, point.Z)
			level.Name = prefix + str(points.index(point)) 
			levels.append(level)
					
	return levels
	
def GenerateFloors(arrays, levels, offset = 0):
	floors = []
	for array, level in zip(arrays, levels):
		floor = doc.Create.NewFloor(array, floorType, level, False)
		parameter = floor.get_Parameter(BuiltInParameter.FLOOR_HEIGHTABOVELEVEL_PARAM)
		parameter.Set(offset)
		floors.append(floor)
	return floors

def GenerateWalls(document, arrays, wallType, levels):
    walls = []
    for level, curves in zip(levels, arrays):
        try:	
            for curve in curves:
                wall = Wall.Create(document, curve, wallType, level.Id, 1, 0, False, False)
                topLevel = levels[levels.index(level) + 1]
                wall.LookupParameter("Top Constraint").Set(topLevel)
                walls.append(wall)
        except:
            pass

    return walls

if polygons != None:
	with TransactionGroup(doc) as txGroup:
		txGroup.Start("Generate Building")
		
		with Transaction(doc) as txFirst:
			txFirst.Start("Generate Levels")
			centers = GetPolygonCenter(polygons)
			levels = GenerateLevels(centers, "Level_RNM_")
			txFirst.Commit()
		
		with Transaction(doc) as txSecond:
			txSecond.Start("GenerateFloors")
			curves = GetPolygonArrays(polygons)
			floors = GenerateFloors(curves, levels)
			modCurves = curves.pop(-1)
			modLevels = levels.pop(0)
			floors = GenerateFloors(modCurves, modLevels, ConvertUnits(offset, "meters"))
			txSecond.Commit()
		
		with Transaction(doc) as txThird:
			txThird.Start("Generate Levels")
			walls = GenerateWalls(doc, curves, wallType, levels)
			txThird.Commit()
		
		txGroup.Commit()
	OUT = floors

else:
	OUT = None

#endregion