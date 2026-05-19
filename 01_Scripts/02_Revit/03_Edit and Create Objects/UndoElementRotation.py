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

# Analyze the Coincidence of the Unit Names
from difflib import SequenceMatcher

#endregion

#region Transaction For Loop

def GetCentroid(element):
    box = element.get_BoundingBox(None)
    maxPoint = box.Max
    minPoint = box.Min
    centroid = XYZ((maxPoint.X + minPoint.X)/2, (maxPoint.Y + minPoint.Y)/2, (maxPoint.Z + minPoint.Z)/2)
    return centroid

# Collect Planting Category
collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Planting).WhereElementIsNotElementType().ToElements()

initialRotation = [UnitUtils.ConvertFromInternalUnits(element.Location.Rotation, UnitTypeId.Degrees) for element in collector ] #type: ignore

with Transaction(doc) as tx:
    tx.Start("Undo Rotation") 
    for element in collector:
        rotation = element.Location.Rotation
        origin = GetCentroid(element)
        line = Line.CreateUnbound(origin, XYZ.BasisZ)
        ElementTransformUtils.RotateElement(doc, element.Id, line, -rotation)
    tx.Commit()

checkRotation = [UnitUtils.ConvertFromInternalUnits(element.Location.Rotation, UnitTypeId.Degrees) for element in collector ] #type: ignore

OUT = initialRotation, checkRotation

#endregion

#region Transation Map

def GetCentroid(element):
    box = element.get_BoundingBox(None)
    maxPoint = box.Max
    minPoint = box.Min
    centroid = XYZ((maxPoint.X + minPoint.X)/2, (maxPoint.Y + minPoint.Y)/2, (maxPoint.Z + minPoint.Z)/2)
    return centroid

def UndoRotation(element):
    rotation = element.Location.Rotation
    origin = GetCentroid(element)
    line = Line.CreateUnbound(origin, XYZ.BasisZ)
    ElementTransformUtils.RotateElement(element.Document, element.Id, line, -rotation)

# Collect Planting Category
collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Planting).WhereElementIsNotElementType().ToElements()

initialRotation = list(map(lambda x : UnitUtils.ConvertFromInternalUnits(x.Location.Rotation, UnitTypeId.Degrees), collector)) #type: ignore

with Transaction(doc) as tx:
    tx.Start("Undo Rotation") 
    map(UndoRotation, collector)
    tx.Commit()

checkRotation = list(map(lambda x : UnitUtils.ConvertFromInternalUnits(x.Location.Rotation, UnitTypeId.Degrees), collector)) #type: ignore

OUT = initialRotation, checkRotation

#endregion