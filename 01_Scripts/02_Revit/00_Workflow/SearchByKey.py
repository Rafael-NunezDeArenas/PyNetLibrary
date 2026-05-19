#region References

# Load the Python Standard and DesignScript Libraries
import clr
import sys

sys.path.append("C:\\Program Files (x86)\\IronPython 2.7\\Lib")
import os

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import *
import Autodesk

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

#Import Windows form
clr.AddReference("System.Windows.Forms")
# Import System Drawing
clr.AddReference("System.Drawing")

from System.Windows.Forms import*
from System.Drawing import*
from System.Collections.Generic import List
from datetime import date

uidoc = __revit__.ActiveUIDocument #type:ignore
doc = uidoc.Document

#endregion

'''collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsElementType().ToElements()

for element in collector:
    if element.LookupParameter("BM_DTM_type_mark").AsString() == "FF36":
        print(Element.Name.__get__(element))'''

# FF03, 25, 26, 27

print("test1")
print("test2")
print("test3")
print("test4")