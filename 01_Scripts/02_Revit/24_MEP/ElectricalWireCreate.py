#region References

# Load the Python Standard and DesignScript Libraries
from platform import system_alias
import string
import sys
import clr

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import *
from Autodesk.Revit.DB.Electrical import *

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


electricalSystems = FilteredElementCollector(doc).OfClass(ElectricalSystem).ToElements()

with Transaction(doc) as tx:
    tx.Start("Generate Wires in Active View")

    for electricalSystem in electricalSystems:
        if doc.ActiveView.__class__ == ViewPlan:
            electricalSystem.NewWires(doc.ActiveView, WiringType.Arc)

    tx.Commit()

if doc.ActiveView.__class__ != ViewPlan:
    OUT = "Not possible to create Wires, active view is not View Plan"

OUT = "Wires Created in Active View"