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

#region Move Element

# Get Family Instance
instanceId = FilteredElementCollector(doc).OfClass(FamilyInstance).FirstElementId()

with Transaction(doc) as tx:
    tx.Start("Move Element")

    ElementTransformUtils.MoveElement(doc, instanceId, XYZ(20, 20, 0))

    tx.Commit()

OUT = "Element Moved"

#endregion
