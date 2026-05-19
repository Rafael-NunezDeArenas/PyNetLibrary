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

#endregion

#region Create a Transform Class Instance that generate a Rotation

# Convert Angle to internal Unit
angle = UnitUtils.ConvertToInternalUnits(5, UnitTypeId.Degrees) #type: ignore

# Point instance 
point = XYZ(3, 3, 6)
plane = Plane.CreateByNormalAndOrigin(XYZ.BasisZ, XYZ.Zero)

# Create Rotation and Reflection Transform. This class have different Transformation Methods applied to Points or Vectors.
rotate = Transform.CreateRotationAtPoint(XYZ.BasisZ, angle, XYZ.Zero)
reflection = Transform.CreateReflection(plane)

# Rotate Point
result = rotate.OfPoint(point)
result = reflection.OfPoint(point)

OUT = result

#endregion