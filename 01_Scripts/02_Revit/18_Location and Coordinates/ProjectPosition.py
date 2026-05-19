#region References

# Load the Python Standard and DesignScript Libraries
import string
import sys
from tokenize import Ignore
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

#endregion

def ConvertUnits(value):
    result = UnitUtils.ConvertToInternalUnits(value, UnitTypeId.Meters) #type:ignore
    return result

# Get Internal Origin
collector = FilteredElementCollector(doc).OfClass(InternalOrigin).ToElements() #type:ignore
internalOrigin = next ((point for point in collector if point.__class__ == InternalOrigin), None) #type:ignore
internalPoint = internalOrigin.Position
internalSharedPoint = internalOrigin.SharedPosition

# Get the Project Location
projectLocation = doc.ActiveProjectLocation
projectPosition = projectLocation.GetProjectPosition(internalPoint)

# Create New Project Position
newProjectPosition = doc.Application.Create.NewProjectPosition(ConvertUnits(60), ConvertUnits(50), ConvertUnits(30), 0.5)

# Create Transaction Modify Project Position
TransactionManager.Instance.EnsureInTransaction(doc)

if None != newProjectPosition:
    projectLocation.SetProjectPosition(internalPoint, newProjectPosition)
    
TransactionManager.Instance.TransactionTaskDone()

OUT = "Process Finished"