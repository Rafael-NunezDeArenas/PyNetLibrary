#region References

# Load the Python Standard and DesignScript Libraries
import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

#Import Windows form
clr.AddReference("System.Windows.Forms")
# Import System Drawing
clr.AddReference("System.Drawing")

from System.Windows.Forms import*
from System.Drawing import*

uidoc = __revit__.ActiveUIDocument #type:ignore
doc = uidoc.Document

#endregion

#region Classes

# Window Form Class
class WindowParameterUpdater(Form):

# Create Result Taskdialog and Show
	def ShowDialogProcess(self, correctSet = True):
		processDialog = TaskDialog("Parameter Value Updater")
		processDialog.TitleAutoPrefix = False
		if correctSet == True:
			processDialog.MainInstruction = "Parameter Value Updated"
			processDialog.MainIcon = TaskDialogIcon.TaskDialogIconInformation
		if correctSet == False:
			processDialog.MainInstruction = "Parameter Value Not Updated"
			processDialog.MainIcon = TaskDialogIcon.TaskDialogIconError
		processDialog.Show()
# Create Main Taskdialog and Show
	def ShowDialogExecute(self):
		mainDialog = TaskDialog("Parameter Value Updater")
		mainDialog.TitleAutoPrefix = False
		mainDialog.MainInstruction = "Update Parameter Value"
		mainDialog.MainContent = "Parameter Value Updater is goint to Update the Parameter Value of the Selected Type, Are you sure you want to Continue?"
		mainDialog.CommonButtons =  TaskDialogCommonButtons.Cancel | TaskDialogCommonButtons.Ok
		mainDialog.DefaultButton = TaskDialogResult.Ok
		mainDialogResult = mainDialog.Show()
# Define Diferent Results
		if mainDialogResult == mainDialogResult.Ok:
			self.SetParameterValue()

# Get Types of Category Selected
	def GetCategorySelected(self, sender, args):
		self.CategoryName = sender.SelectedItem
		for category in doc.Settings.Categories:
			if category.Name == self.CategoryName:
				filter = ElementCategoryFilter(category.Id)
				self.collector = FilteredElementCollector(doc).WherePasses(filter).WhereElementIsElementType().ToElements()
				self.TypeNames = [Element.Name.__get__(element) for element in self.collector]
				break
		self.typeBox.DataSource = None
		self.typeBox.DataSource = self.GetTypes()
# Get Parameters of Type Selected
	def GetTypeSelected(self, sender, args):
		self.TypeName = sender.SelectedItem
		parameterNames = []
		for element in self.collector:
			if Element.Name.__get__(element) == self.TypeName:
				parameters = element.Parameters
				iterator = parameters.ForwardIterator()
				while iterator.MoveNext():
					if iterator.Current.IsReadOnly == False:
						name = iterator.Current.Definition.Name
						parameterNames.append(name)
				break       
		self.ParameterNames = parameterNames
		self.parameterBox.DataSource = None
		self.parameterBox.DataSource = self.GetParameters()
# Get Parameter value of Parameter Selected          
	def GetParameterSelected(self, sender, args):
		self.ParameterName = sender.SelectedItem
		for element in self.collector:
			if Element.Name.__get__(element) == self.TypeName:
				parameters = element.Parameters
				iterator = parameters.ForwardIterator()
				while iterator.MoveNext():
					if iterator.Current.Definition.Name == self.ParameterName:
						self.Parameter = iterator.Current
						storage = iterator.Current.StorageType.ToString()
						paramType = iterator.Current.Definition.ParameterType.ToString()
						self.StorageLabel.Text = "Storage Type: " + storage
						self.TypeParamLabel.Text = "Parameter Type: " + paramType
						if iterator.Current.Definition.ParameterType.ToString() == "YesNo":
							yesNoValues = {1: "Yes", 0: "No"}
							value = yesNoValues.get(iterator.Current.AsInteger())
							self.textBox.Text = value
						if iterator.Current.StorageType.ToString() == "String":
							value = iterator.Current.AsString()
							self.textBox.Text = value
						else:
							value = iterator.Current.AsValueString()
							self.textBox.Text = value
						break

# Generate Function for Cancel Button
	def UpdateParameter(self, sender, args):
		self.ShowDialogExecute()
# Generate Function for Cancel Button
	def Cancel(self, sender, args):
		if sender.Click:
			self.DialogResult = DialogResult.Cancel
			self.Close()

# Generate def for Value Box	
	def GetValueBox(self, sender, args):
		self.Value = sender.Text
# Return all category Names
	def GetCategories(self):
		categories = [category.Name for category in doc.Settings.Categories if category.CategoryType == CategoryType.Model]
		categories.sort()
		return categories
# Return all Types Names
	def GetTypes(self):
		self.TypeNames.sort()
		return self.TypeNames
# Return all Parameters Names
	def GetParameters(self):
		self.ParameterNames.sort()
		return self.ParameterNames

# Set Type Parameter Value
	def SetParameterValue(self):
		conversionOptions = {"String": self.Value, "Double": self.ConvertValueFloat(), "Integer": self.ConvertValueInt()}
		setValue = conversionOptions.get(self.Parameter.StorageType.ToString())
		if self.Parameter.Definition.ParameterType.ToString() == "YesNo":
			setValue = self.ConvertValueYesNo()
		if setValue != None:
			with Transaction(doc) as tx:
				tx.Start("Parameter Value Update")
				self.Parameter.Set(setValue)
				tx.Commit()
				self.ShowDialogProcess()
			print("Parameter Value Updated:" + "\n Parameter: " + self.Parameter.Definition.Name + "Value:\n" + self.Value)
		if setValue == None:
			self.ShowDialogProcess(False)
			print("Not Possible to set Parameter. Incorrect value Format")
# Convert to Int
	def ConvertValueInt(self):
		try:
			return int(self.Value)
		except:
			return None
# Convert to Float
	def ConvertValueFloat(self):
		try:
			return float(self.Value)
		except:
			return None
# Convert to YesNo
	def ConvertValueYesNo(self):
		try:
			if self.Value == "Yes":
				return 1
			if self.Value == "No":
				return 0
		except:
			return None

# Windows Form Configuration
	def ConfigureForm(self):
	# Include Icon
		self.Icon = Icon("C:\\Program Files\\Autodesk\\Revit 2021\\Revit.ico")
	#Generate Tittle Value
		self.Text = "Parameter Value Updater"
	#Form Variables
		self.CategoryName = None
		self.TypeName = None
		self.ParameterName = None
		self.Parameter = None
		self.TypeNames = []
		self.ParameterNames = []
		self.Value = None
		self.Type = None
		self.collector = None
	#Window dimension
		self.WindowState = FormWindowState.Normal
	#Generate Window in Center
		self.CenterToScreen()
	#Window in front
		self.BringToFront()
		self.Topmost = True
	#Scale window with resolution
		self.screenSize = Screen.GetWorkingArea(self)
		self.Width = 400
		self.Height = 350
	#Block Dimension of window
		self.FormBorderStyle = FormBorderStyle.FixedDialog
		self.MaximizeBox = False
# Window Form Labels
	def GenerateFormLabels(self):
		#Description Category Label
		labelCategory = Label(Text = "Select Category to Filter Family Type:")
		labelCategory.Parent = self
		labelCategory.Width = 350
		labelCategory.Height = 20
		labelCategory.Location = Point(20, 20)
		#Description Type Label
		labelType = Label(Text = "Select Family Type to Filter Parameter Set:")
		labelType.Parent = self
		labelType.Width = 350
		labelType.Height = 20
		labelType.Location = Point(20, 80)
		#Description Parameter Label
		labelParameter = Label(Text = "Select Parameter to Modify Value:")
		labelParameter.Parent = self
		labelParameter.Width = 350
		labelParameter.Height = 20
		labelParameter.Location = Point(20, 140)
		#Description Text to include
		labelValue = Label(Text = "Introduce Parameter value to Set:")
		labelValue.Parent = self
		labelValue.Width = 350
		labelValue.Height = 20
		labelValue.Location = Point(20, 200)
		#Description Storage Type
		self.StorageLabel = Label(Text = "Storage Type:")
		self.StorageLabel.Parent = self
		self.StorageLabel.Width = 170
		self.StorageLabel.Height = 20
		self.StorageLabel.Location = Point(20, 250)
		#Description Storage Type
		self.TypeParamLabel = Label(Text = "Parameter Type:")
		self.TypeParamLabel.Parent = self
		self.TypeParamLabel.Width = 170
		self.TypeParamLabel.Height = 20
		self.TypeParamLabel.Location = Point(20, 270)
# Window Form ComboBoxes
	def GenerateComboBoxes(self):
		#Selection Combo Box Bar
		categoryBox = ComboBox()
		categoryBox.Location = Point(20, 40)
		categoryBox.Width = self.screenSize.Width / 7
		categoryBox.DataSource = self.GetCategories()
		categoryBox.DropDownStyle = ComboBoxStyle.DropDownList
		categoryBox.SelectedIndexChanged += self.GetCategorySelected
		self.Controls.Add(categoryBox)
	#Selection Combo Box Bar       
		self.typeBox = ComboBox()
		self.typeBox.Location = Point(20, 100)
		self.typeBox.Width = self.screenSize.Width / 7
		self.typeBox.DataSource = self.GetTypes()
		self.typeBox.DropDownStyle = ComboBoxStyle.DropDownList
		self.typeBox.SelectedIndexChanged += self.GetTypeSelected
		self.Controls.Add(self.typeBox)
	#Selection Combo Box Bar       
		self.parameterBox = ComboBox()
		self.parameterBox.Location = Point(20, 160)
		self.parameterBox.Width = self.screenSize.Width / 7
		self.parameterBox.DataSource = self.GetParameters()
		self.parameterBox.DropDownStyle = ComboBoxStyle.DropDownList
		self.parameterBox.SelectedIndexChanged += self.GetParameterSelected
		self.Controls.Add(self.parameterBox)
# Window Form TextBox
	def GenerateTextBox(self):
		#Generate TextBox
		self.textBox = TextBox()
		self.textBox.Location = Point(20, 220)
		self.textBox.Width = self.screenSize.Width / 7
		self.textBox.TextChanged += self.GetValueBox
		self.Controls.Add(self.textBox)
# Window Form Buttons
	def GenerateButtons(self):
		#Generate Buttons
		bUpdate = Button()
		bUpdate.Text = "Update"
		bUpdate.Location = Point(290, 260)
		bUpdate.Click += self.UpdateParameter
		self.Controls.Add(bUpdate)
	#Generate Buttons
		bCancel = Button()
		bCancel.Text = "Cancel"
		bCancel.Location = Point(200, 260)
		bCancel.Click += self.Cancel
		self.Controls.Add(bCancel)

# Constructor Method
	def __init__(self):
		self.ConfigureForm()
		self.GenerateFormLabels()
		self.GenerateComboBoxes()
		self.GenerateTextBox()
		self.GenerateButtons()

# endregion

# region Create Form Instance

updaterForm = WindowParameterUpdater()
updaterForm.ShowDialog()

# endregion