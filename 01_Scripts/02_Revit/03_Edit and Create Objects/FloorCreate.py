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

#region Create Floors based in Rooms

# Collect Rooms
rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType().ToElements()
# Get Floor Type
floorTypeId = FilteredElementCollector(doc).OfClass(FloorType).FirstElementId()

# Create Geometry Options
opts = Options()
opts.DetailLevel = ViewDetailLevel.Fine

# Revit 2021 Floor Constructor available Document Class and use CurveArrays. Revit 2022 Floor Constructor available Floor Class and use CurveLoops
def GetRoomPerimeter(room, bool = True):

    geometries = room.get_Geometry(opts)
    for geometry in geometries:
        if geometry.__class__ is Solid and geometry.Volume > 0:
            faces = geometry.Faces
            for face in faces:
                if face.FaceNormal.IsAlmostEqualTo(XYZ.Negate(XYZ.BasisZ)):
                    loop = face.GetEdgesAsCurveLoops()
                    arrayList = face.EdgeLoops

    if bool == True:
        curveArray = CurveArray()
        for array in arrayList:
            for line in array:
                curveArray.Append(line.AsCurve())

        return curveArray
    
    return loop

with Transaction(doc) as tx:
    tx.Start("Create Floors")
    floors = []
    for room in rooms:
        array = GetRoomPerimeter(room)
        floor = doc.Create.NewFloor(array, doc.GetElement(floorTypeId), room.Level, False)
        floors.append(floor)

    tx.Commit()

OUT = floors

#endregion