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

#region Transfer Parameter Value to other parameter Definition

# Definition Set parameter Value depending the Storage Type
def SetParameterValue(nameOrigin, nameResult, collector):
	count = 0
	if collector.Count > 0:
		for element in collector:
			parameterOrigin = element.LookupParameter(nameOrigin)
			parameterResult = element.LookupParameter(nameResult)
			if parameterOrigin != None and parameterResult != None and parameterOrigin.StorageType == StorageType.String and parameterResult.StorageType == StorageType.String:
				if parameterOrigin.HasValue != False and parameterOrigin.AsString() != "":
					parameterResult.Set(parameterOrigin.AsString())
					count += 1
			elif parameterOrigin != None and parameterResult != None and parameterOrigin.StorageType == StorageType.Integer and parameterResult.StorageType == StorageType.Integer:
				if parameterOrigin.HasValue != False:
					parameterResult.Set(parameterOrigin.AsInteger())
					count += 1
			elif parameterOrigin != None and parameterResult != None and parameterOrigin.StorageType == StorageType.Double and parameterResult.StorageType == StorageType.Double:
				if parameterOrigin.HasValue != False:
					parameterResult.SetValueString(parameterOrigin.AsValueString())
					count += 1
	return count

# Collect Elements by Category and Set the Parameter
def TransferValueParameter(nameOrigin, nameResult, category, typeOrInstance):
	categoryFilter = ElementCategoryFilter(category.Id)
	if typeOrInstance == True:
		collector = FilteredElementCollector(doc).WherePasses(categoryFilter).WhereElementIsElementType().ToElements()
		count = SetParameterValue(nameOrigin, nameResult, collector)
		return count 
	if typeOrInstance == False:
		collector = FilteredElementCollector(doc).WherePasses(categoryFilter).WhereElementIsNotElementType().ToElements()
		count = SetParameterValue(nameOrigin, nameResult, collector)
		return count 

# Get Revit categories and filter to Category Type equals to Model Type
categories = doc.Settings.Categories
modelCategories = [category for category in categories if category.CategoryType == CategoryType.Model]
		
# Set Parameter Transaction

with Transaction(doc) as tx:
	result = 0
	for category in modelCategories:
		count = TransferValueParameter(IN[0], IN[1], category, IN[2]) #type:ignore
		result += count

	tx.Commit()
#Iterate Categories and Set Parameters Value

OUT = "Process Finished, " + "Total Filled: " + str(result)

#endregion