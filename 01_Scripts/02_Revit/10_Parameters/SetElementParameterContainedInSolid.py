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


# region Set parameters with Element Solid Intersect
def SetElementParametersWithSolidIntersect(iteration, parameter, specialValue, options):
    result = []
    for instance in iteration:
        count = 0
        parameterInstance = m.LookupParameter(parameter) #type: ignore
    # Get Solid of Mass
        geoElem = instance.get_Geometry(options)
        for geoObject in geoElem:
            if geoObject.__class__ == Solid and geoObject.Volume > 0:
                solid = geoObject
                filter = ElementIntersectsSolidFilter(solid)
                elements = FilteredElementCollector(doc).WherePasses(filter).ToElements()
                result.append(elements)
                for element in elements:
                    parameter = element.LookupParameter(parameter) #type: ignore
                    if parameter != None: 
                        parameter.Set(parameterInstance.AsString())
                    if count - 1 >= 0 and element in result[count - 1]:
                        parameter.Set(specialValue) #type: ignore
        count += 1
    return None

# Obtain Link Doc.
links = FilteredElementCollector(doc).OfClass(RevitLinkInstance)
Documents = [n.GetLinkDocument() for n in links]
linkDoc = None
linkName = IN[0] #type: ignore

for document in Documents:
	if hasattr(document, "Title"):
		linkName == document.Title
		linkDoc = document
		break

# Get LinkDoc Mass ot spaces or element to Intersect Solid
mass = FilteredElementCollector(linkDoc).OfCategory(BuiltInCategory.OST_Mass).WhereElementIsNotElementType().ToElements()

# Create Geometry Options
opts = Options()
opts.DetailLevel = ViewDetailLevel.Fine

# Set Parameter With Mass Value. Iterate Mass and get Parameter Value
with Transaction(doc) as tx:

    tx.Start("Set Parameter Contained in Mass")

    SetElementParametersWithSolidIntersect(mass, IN[1], IN[2], opts) # type: ignore
    
    tx.Commit()

OUT = "Process Finished"

#endregion