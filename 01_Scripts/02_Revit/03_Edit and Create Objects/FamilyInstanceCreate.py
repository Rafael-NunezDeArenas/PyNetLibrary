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

# Analyze the Coincidence of the Unit Names
from difflib import SequenceMatcher

#endregion

#region Create Family Instances

familyName = "M_Desk"
symbolName = "1525 x 762mm"

# Get a Family symbol
familySymbols = FilteredElementCollector(doc).OfClass(FamilySymbol).ToElements()
familySymbol = None

for symbol in familySymbols:
    if symbol.Family.Name == familyName and Element.Name.__get__(symbol) == symbolName:
        familySymbol = symbol

with Transaction(doc) as tx:
    tx.Start("Create Family Instance")

    if familySymbol.IsActive == False:
        familySymbol.Activate()
    instance = doc.Create.NewFamilyInstance(XYZ.Zero, familySymbol, Structure.StructuralType.NonStructural) #type: ignore

    tx.Commit()

OUT = instance

#endregion