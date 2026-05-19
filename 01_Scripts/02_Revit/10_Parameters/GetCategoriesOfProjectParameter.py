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

# endregion


#region Transaction

parameters = doc.ParameterBindings
iterator = parameters.ForwardIterator()

while iterator.MoveNext():
    name = iterator.Key.Name
    if name == "ExportParam":
        definition = iterator.Key
        if parameters.Contains(definition):
            elementBinding = parameters.get_Item(definition)
            categories = elementBinding.Categories
            break

names = [category.Name for category in categories]

OUT = names

#endregion