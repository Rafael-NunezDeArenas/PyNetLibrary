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
app = __revit__.Application #type:ignore

from difflib import SequenceMatcher

#endregion

import webbrowser

# endregion

# region concatenate TaskDialogs

# Create Main Taskdialog
mainDialog = TaskDialog("Revit API")
mainDialog.TitleAutoPrefix = False
mainDialog.MainInstruction = "Information to Show"
mainDialog.MainContent = "Example of TaskDialog with Command Links"

# Include Command Links
mainDialog.AddCommandLink(TaskDialogCommandLinkId.CommandLink1, "Show information about Revit Version", "Aditional information")
mainDialog.AddCommandLink(TaskDialogCommandLinkId.CommandLink2, "Show information about Current Document", "Aditional information")

# Include Expanded Content
mainDialog.ExpandedContent = "Expanded Content information"

# Include Icon
mainDialog.MainIcon = TaskDialogIcon.TaskDialogIconInformation

# Include Standar Buttons
mainDialog.CommonButtons = TaskDialogCommonButtons.Cancel

# Include Footer text Link
mainDialog.FooterText = '<a href="https://github.com/rafa2403nunez-droid/PyNet">Click for more Info:</a>'

# Create Definitions of TaskDialogs
def ShowInfoApp(application):
    appInfoDialog = TaskDialog("Revit API")
    appInfoDialog.MainInstruction = "Revit Version: " + application.VersionName
    return appInfoDialog.Show()
def ShowInfoDoc(doc):
    docInfoDialog = TaskDialog("Revit API")
    docInfoDialog.MainInstruction = "Doc Title: " + doc.Title
    return docInfoDialog.Show()

mainDialogResult = mainDialog.Show()

# Define Diferent Results
if mainDialogResult == mainDialogResult.CommandLink1:
    ShowInfoApp(app)
elif mainDialogResult == mainDialogResult.CommandLink2:
    ShowInfoDoc(doc)
elif mainDialogResult == mainDialogResult.Cancel:
    TaskDialog.Show("Revit API", "Operation Cancelled")
else:
    TaskDialog.Show("Revit API", "Operation Cancelled")

OUT = "TaskDialog Example"

# endregion