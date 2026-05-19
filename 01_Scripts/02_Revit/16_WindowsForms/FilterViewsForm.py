#region References

# Load the Python Standard and DesignScript Libraries
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

#Import Windows form
clr.AddReference("System.Windows.Forms")
# Import System Drawing
clr.AddReference("System.Drawing")

import System
from System.Windows.Forms import*
from System.Drawing import*

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

#endregion

#region Windows Form Classes

# Generate view Filter Form
class WindowFilter(Form):
# Get Parameter BIndings od the Project
	@staticmethod
	def GetParameterBindings(document):
		# Selection of Project Parameters in the current Document
		parameters = []
		iterador = document.ParameterBindings.ForwardIterator()
		while iterador.MoveNext():
			parameters.append(iterador.Key.Name)
# Generate a tupple to include in Selection Bar (ComboBox). Selection Bar only Accept Tuples
		parameters = tuple(parameters)
		return parameters
# Generate def for Combo Box
	def ParamCombo(self, sender, args):
		self.Param = sender.SelectedItem
# Generate def for Value Box	
	def ValueBox(self, sender, args):
		self.Value = sender.Text	
# Generate Function for Next Button	
	def Next(self, sender, args):
# If Click in the Button, Filter Views with a Project Parameter
		if sender.Click:
			provider = None
			iterator = doc.ParameterBindings.ForwardIterator()
			evaluator = FilterStringEquals()
# Iterate an Get Parameter Selected in Combo Box
			while iterator.MoveNext():
				if iterator.Key.Name == self.Param:
					provider = ParameterValueProvider(iterator.Key.Id)
					break
# Determinate if the Provider is not Null and Create a String Contains Filter	
			if provider == None or self.Value == None:
				self.Views = "Provider ot Parameter Value Not Specified"
			else:
				filter = FilterStringRule(provider, evaluator, self.Value, True)
				filterViews = ElementParameterFilter(filter)
# Filter Views with Conditions
				collector = FilteredElementCollector(doc).OfClass(View3D).WherePasses(filterViews).ToElements()
				self.Views = [view.Name for view in collector]
# Determinate of the Filter Views are not Zero				
				if self.Views.Count < 1:
					self.Views = "No 3DViews Collected with Current Information"
			self.Cancelled = False				
			self.Close()
# Generate Function for Cancel Button		
	def Cancel(self, sender, args):
		if sender.Click:
			self.Close()
# Constructor Method
	def __init__(self, parameters):
# Include Icon
		self.Icon = Icon("NWCExporter.ico")
#Generate Tittle Value
		self.Text = "NWC Exporter"
#Form Variables
		self.Parameters = parameters
		self.Param = None
		self.Value = None
		self.Views = None
		self.Cancelled = True
#Window dimension
		self.WindowState = FormWindowState.Normal
#Generate Window in Center
		self.CenterToScreen()
#Window in front
		self.BringToFront()
		self.Topmost = True
#Scale window with resolution
		screenSize = Screen.GetWorkingArea(self)
		self.Width = 400
		self.Height = 240
#Description 1	
		labelSheetName = Label(Text = "Select Project Parameter to use in the 3Dview Filter:")
		labelSheetName.Parent = self
		labelSheetName.Width = 350
		labelSheetName.Height = 20
		labelSheetName.Location = Point(20, 10)
#Description 2
		labelSheetName = Label(Text = "Add the Value of the Parameter to filter the 3Dviews: ")
		labelSheetName.Parent = self
		labelSheetName.Width = 350
		labelSheetName.Height = 20
		labelSheetName.Location = Point(20, 80)
#Block Dimension of window
		self.FormBorderStyle = FormBorderStyle.FixedDialog
#Spacing
		spacing = 10
#Selection Combo Box Bar
		cBox = ComboBox()
		cBox.Location = Point(20, 40)
		cBox.Width = screenSize.Width / 7
		cBox.Items.AddRange(self.Parameters)
		cBox.DropDownStyle = ComboBoxStyle.DropDownList
		cBox.SelectedIndexChanged += self.ParamCombo
		self.Controls.Add(cBox)		
#Generate TextBox
		tBox = TextBox()
		tBox.Location = Point(20, 110)
		tBox.Width = screenSize.Width / 7
		tBox.TextChanged += self.ValueBox
		self.Controls.Add(tBox)
#Generate Buttons
		bNext = Button()
		bNext.Text = "Next"
		bNext.Location = Point(290, 150)
		bNext.Click += self.Next
		self.Controls.Add(bNext)
#Generate Buttons
		bCancel = Button()
		bCancel.Text = "Cancel"
		bCancel.Location = Point(200, 150)
		bCancel.Click += self.Cancel
		self.Controls.Add(bCancel)

# Generate TaskDialog Options Class
class TaskdialogResults():
	
	@staticmethod
	def ShowCancelTaskDialog():
		dialog = TaskDialog("NWC Exporter")
		dialog.MainContent = "Export Cancelled"
		dialog.TitleAutoPrefix = False
		dialog.CommonButtons = TaskDialogCommonButtons.Ok
		dialog.MainIcon = TaskDialogIcon.TaskDialogIconWarning
		dialog.Show()
	@staticmethod
	def ShowCorrectTaskDialog():
		dialog = TaskDialog("NWC Exporter")
		dialog.TitleAutoPrefix = False
		dialog.MainContent = "Process Finished"
		dialog.CommonButtons = TaskDialogCommonButtons.Ok
		dialog.MainIcon = TaskDialogIcon.TaskDialogIconInformation
		dialog.Show()
	@staticmethod
	def ShowErrorsTaskDialog():
		dialog = TaskDialog("NWC Exporter")
		dialog.TitleAutoPrefix = False
		dialog.MainContent = "Process Finished with Errors"
		dialog.CommonButtons = TaskDialogCommonButtons.Ok
		dialog.MainIcon = TaskDialogIcon.TaskDialogIconWarning
		dialog.Show()

#endregion

# region ViewFilter Output

# Run View Filter Windows Form
Filterform = WindowFilter(WindowFilter.GetParameterBindings(doc))
Filterform.ShowDialog()
# Generate Outputs if you Click in Cancel Button. Show TaskDialog Operation Cancelled
if Filterform.Cancelled == True:
	TaskdialogResults().ShowCancelTaskDialog()
	OUT = "Operation Cancelled"
# If you not Cancell the Operation. Generate OUT if the Filter process do not Generate a Correct Result
else:
	if Filterform.Views == None:
		OUT = "No 3DViews Collected with Current Information"
	if Filterform.Views == "Provider ot Parameter Value Not Specified" or Filterform.Views == "No 3DViews Collected with Current Information":
		OUT = Filterform.Views
# Generate the OUT with a Correct Result
	else:
		OUT = "Project Parameter Selected: " + Filterform.Param, "Parameter Value Indicated: " + Filterform.Value, "Filtered Views: ", Filterform.Views

# endregion