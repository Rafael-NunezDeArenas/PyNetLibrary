import clr

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

doc = __revit__.ActiveUIDocument.Document  #type:ignore


class SearchByKeyScript:
    @staticmethod
    def Run(document):
        parameter_name = "BM_DTM_type_mark"
        search_value = "FF36"

        collector = FilteredElementCollector(document).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsElementType().ToElements()
        results = []
        for element in collector:
            p = element.LookupParameter(parameter_name)
            if p is not None and p.AsString() == search_value:
                results.append(Element.Name.__get__(element))

        if results:
            print(f"Found {len(results)} element(s) with {parameter_name} = '{search_value}':")
            for name in results:
                print(f"  {name}")
        else:
            print(f"No elements found with {parameter_name} = '{search_value}'.")

        return results


SearchByKeyScript.Run(doc)
