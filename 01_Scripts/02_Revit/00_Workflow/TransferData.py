#region References

# Load the Python Standard and DesignScript Libraries
import clr
import sys

sys.path.append("C:\\Program Files (x86)\\IronPython 2.7\\Lib")
import os

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
from System.Collections.Generic import List
from datetime import date

app = __revit__.Application #type:ignore
uidoc = __revit__.ActiveUIDocument #type:ignore 
doc = uidoc.Document

#endregion

# Generate view Filter Form
class WindowTransfer(Form):
# Generate Function for Next Button	
	def Transfer(self, sender, args):
		# If Click in the Button, Filter Views with a Project Parameter
		if sender.Click:
			if self.BaseDocument != None and self.Category != None and len(self.GetTransferDocuments()) > 0 and len(self.GetSelectedParameters()) > 0:
				if self.Category.__class__ != ProjectInfo:
					DataCollector.TransferData(self.BaseDocument, self.GetTransferDocuments(), self.Category, self.GetSelectedParameters())
				else:
					DataCollector.TransferProjectInformation(self.BaseDocument, self.GetTransferDocuments(), self.GetSelectedParameters())
				TaskdialogResults.ShowCorrectTaskDialog()
				self.Close()
# Generate Function for Cancel Button		
	def Cancel(self, sender, args):
		if sender.Click:
			TaskdialogResults.ShowCancelTaskDialog()
			self.Close()
# Generate Function for Cancel Button
	def GetBaseDocument(self, sender, args):
		self.BaseDocument = ModelManager.GetModel(self.Application, sender.SelectedItem)
		categoriesComboBox = [control for control in self.GroupBoxDocuments.Controls if control.Name == "categoryComboBox"][0]
		categoriesComboBox.Items.Clear()
		[categoriesComboBox.Items.Add(category) for category in ModelManager.GetCategories(ModelManager.GetModel(self.Application, sender.SelectedItem))]
		listControl = [control for control in self.GroupBoxDocuments.Controls if control.Name == "ModelsList"][0]
		listControl.Items.Clear()
		[listControl.Items.Add(document, CheckState.Unchecked) for document in self.BaseDocuments if sender.SelectedItem != document]
# Generate Function for Cancel Button
	def GetTransferDocuments(self):
		result = []
		listControl = [control for control in self.GroupBoxDocuments.Controls if control.Name == "ModelsList"][0]
		for count in range(listControl.Items.Count):
			if listControl.GetItemCheckState(count) == CheckState.Checked:
				result.append(ModelManager.GetModel(self.Application, listControl.Items[count]))
		return result
# Collect Data and get Category
	def GetCategory(self, sender, args):
		values = []
		if sender.SelectedItem != "Project Information":
			self.Category = ModelManager.GetCategory(self.Application, sender.SelectedItem)
			self.Parameters = DataCollector.GetTypes(self.BaseDocument, self.Category)[0].Parameters
		else:
			self.Category = ModelManager.GetProjectInformation(self.BaseDocument)
			self.Parameters = self.Category.GetOrderedParameters()
		listControl = [control for control in self.GroupBoxParameters.Controls if control.Name == "ParameterList"][0]
		listControl.Items.Clear()
		for parameter in self.Parameters:
			if parameter.IsReadOnly == False and parameter.StorageType == StorageType.String:
				values.append(parameter.Definition.Name)
		values.sort()
		[listControl.Items.Add(value, CheckState.Unchecked) for value in values]
# Generate Function for Cancel Button
	def ParametersFilter(self, sender, args):
		listControl = [control for control in self.GroupBoxParameters.Controls if control.Name == "ParameterList"][0]
		listControl.Items.Clear()
		values = []
		if sender.SelectedItem == "All Parameters":
			for parameter in self.Parameters:
				if parameter.IsReadOnly == False and parameter.StorageType == StorageType.String:
					values.append(parameter.Definition.Name)
			values.sort()
			[listControl.Items.Add(value, CheckState.Unchecked) for value in values]
		elif sender.SelectedItem == "BuiltIn Parameters":
			for parameter in self.Parameters:
				if parameter.IsReadOnly == False and parameter.StorageType == StorageType.String and parameter.Definition.BuiltInParameter != BuiltInParameter.INVALID:
					values.append(parameter.Definition.Name)
			values.sort()
			[listControl.Items.Add(value, CheckState.Unchecked) for value in values]
		elif sender.SelectedItem == "Shared Parameters":	
			for parameter in self.Parameters:
				if parameter.IsReadOnly == False and parameter.StorageType == StorageType.String and parameter.Definition.BuiltInParameter == BuiltInParameter.INVALID:
					values.append(parameter.Definition.Name)
			values.sort()
			[listControl.Items.Add(value, CheckState.Unchecked) for value in values]
# Check ListBox
	def CheckAll(self, sender, args):
		
		if len([control for control in self.GroupBoxDocuments.Controls if control.Name == sender.Name.replace("Check", "") + "List"]) > 0:
			listControl = [control for control in self.GroupBoxDocuments.Controls if control.Name == sender.Name.replace("Check", "") + "List"][0] 	
		else:
			listControl = [control for control in self.GroupBoxParameters.Controls if control.Name == sender.Name.replace("Check", "") + "List"][0]
		for count in range(listControl.Items.Count):
			if listControl.GetItemCheckState(count) == CheckState.Unchecked:
				listControl.SetItemCheckState(count, CheckState.Checked)
# Uncheck ListBox
	def UnCheckAll(self, sender, args):
		if len([control for control in self.GroupBoxDocuments.Controls if control.Name == sender.Name.replace("UnCheck", "") + "List"]) > 0:
			listControl = [control for control in self.GroupBoxDocuments.Controls if control.Name == sender.Name.replace("UnCheck", "") + "List"][0] 	
		else:
			listControl = [control for control in self.GroupBoxParameters.Controls if control.Name == sender.Name.replace("UnCheck", "") + "List"][0]
		for count in range(listControl.Items.Count):
			if listControl.GetItemCheckState(count) == CheckState.Checked:
				listControl.SetItemCheckState(count, CheckState.Unchecked)
# Windows Form Configuration
	def ConfigureForm(self, application):
		#Generate Tittle Value
		self.Text = "Transfer data"
		#Form Variables
		self.Application = application
		self.BaseDocuments = ModelManager.GetModels(application)
		self.TransferDocuments = ModelManager.GetModels(application)
		self.Categories = ModelManager.GetCategories([document  for document in application.Documents if document.IsLinked == False and document.IsWorkshared][0])
		self.BaseDocument = None
		self.Category = None
		self.Parameters = None
		#Window dimension
		self.WindowState = FormWindowState.Normal
		#Generate Window in Center
		self.CenterToScreen()
		#Window in front
		self.BringToFront()
		self.Topmost = True
		#Scale window with resolution
		self.screenSize = Screen.GetWorkingArea(self)
		self.MaximizeBox = True
		self.Width = 880
		self.Height = 690
		self.MinimumSize = Size(880, 690)
		#Block Dimension of window
		self.FormBorderStyle = FormBorderStyle.Sizable
# Get Selected Parameters
	def GetSelectedParameters(self):
		result = []
		listControl = [control for control in self.GroupBoxParameters.Controls if control.Name == "ParameterList"][0]
		for count in range(listControl.Items.Count):
			if listControl.GetItemCheckState(count) == CheckState.Checked:
				result.append(listControl.Items[count])
		return result
# Window Form Labels
	def GenerateFormLabels(self):
		# Main Description
		labelGeneralDescription = Label(Text = "Select the category to transfer the parameters data of all the common types between models.")
		labelGeneralDescription.Parent = self
		labelGeneralDescription.Width = 800
		labelGeneralDescription.Height = 40
		labelGeneralDescription.Padding = Padding(10, 0, 0, 0)
		labelGeneralDescription.Anchor = AnchorStyles.Left | AnchorStyles.Top
		self.TableLayout.Controls.Add(labelGeneralDescription, 0, 0)
		#Description 1	
		labelGeneralDescription = Label(Text = "Select source model:")
		labelGeneralDescription.Parent = self
		labelGeneralDescription.Width = 300
		labelGeneralDescription.Height = 20
		labelGeneralDescription.Location = Point(15, 40)
		labelGeneralDescription.Anchor = AnchorStyles.Left | AnchorStyles.Top
		self.GroupBoxDocuments.Controls.Add(labelGeneralDescription)
		#Description 2
		labelGeneralDescription = Label(Text = "Select category to collect types:")
		labelGeneralDescription.Parent = self
		labelGeneralDescription.Width = 300
		labelGeneralDescription.Height = 20
		labelGeneralDescription.Location = Point(15, 100)
		labelGeneralDescription.Anchor = AnchorStyles.Left | AnchorStyles.Top
		self.GroupBoxDocuments.Controls.Add(labelGeneralDescription)
		#Description 3
		labelGeneralDescription = Label(Text = "Select destination model:")
		labelGeneralDescription.Parent = self
		labelGeneralDescription.Width = 300
		labelGeneralDescription.Height = 20
		labelGeneralDescription.Location = Point(15, 160)
		labelGeneralDescription.Anchor = AnchorStyles.Left | AnchorStyles.Top
		self.GroupBoxDocuments.Controls.Add(labelGeneralDescription)
		#Description 4
		labelGeneralDescription = Label(Text = "Select parameters to transfer data:")
		labelGeneralDescription.Parent = self
		labelGeneralDescription.Width = 300
		labelGeneralDescription.Height = 20
		labelGeneralDescription.Location = Point(15, 40)
		labelGeneralDescription.Anchor = AnchorStyles.Left | AnchorStyles.Top
		self.GroupBoxParameters.Controls.Add(labelGeneralDescription)
# Window Form ComboBoxes
	def GenerateComboBoxes(self):
		#Selection Combo Box Bar
		baseBox = ComboBox()
		baseBox.Name = "BaseDocumentComboBox"
		baseBox.Location = Point(15, 65)
		baseBox.Width = 370
		baseBox.Anchor = AnchorStyles.Left | AnchorStyles.Top | AnchorStyles.Right | AnchorStyles.Bottom
		if len(self.BaseDocuments) > 0:
			[baseBox.Items.Add(document) for document in self.BaseDocuments]
			self.BaseDocument = ModelManager.GetModel(self.Application, self.BaseDocuments[0])
		baseBox.DropDownStyle = ComboBoxStyle.DropDownList
		baseBox.SelectedIndexChanged += self.GetBaseDocument
		self.GroupBoxDocuments.Controls.Add(baseBox)
		#Selection Combo Box Bar
		categoryBox = ComboBox()
		categoryBox.Name = "categoryComboBox"
		categoryBox.Location = Point(15, 125)
		categoryBox.Width = 370
		categoryBox.Anchor = AnchorStyles.Left | AnchorStyles.Top | AnchorStyles.Right | AnchorStyles.Bottom
		[categoryBox.Items.Add(category) for category in self.Categories]
		self.Category = ModelManager.GetCategory(self.Application, self.Categories[0])
		categoryBox.DropDownStyle = ComboBoxStyle.DropDownList
		categoryBox.SelectedIndexChanged += self.GetCategory
		self.GroupBoxDocuments.Controls.Add(categoryBox)
		#Selection Combo Box Bar
		parameterBox = ComboBox()
		parameterBox.Location = Point(15, 65)
		parameterBox.Width = 370
		parameterBox.Anchor = AnchorStyles.Left | AnchorStyles.Top | AnchorStyles.Right | AnchorStyles.Bottom
		parameterBox.DataSource = ["All Parameters", "BuiltIn Parameters", "Shared Parameters"]
		self.Category = ModelManager.GetCategory(self.Application, self.Categories[0])
		parameterBox.DropDownStyle = ComboBoxStyle.DropDownList
		parameterBox.SelectedIndexChanged += self.ParametersFilter
		self.GroupBoxParameters.Controls.Add(parameterBox)
# Window Checked Box list
	def GenerateFormSelectionList(self, documents):
		# Selection List
		checkedListBox = CheckedListBox()
		checkedListBox.Name = "ModelsList"
		checkedListBox.Location = Point(15, 180)
		checkedListBox.Width = 370
		checkedListBox.Height = 300
		checkedListBox.HorizontalScrollbar = True
		checkedListBox.CheckOnClick = True
		[checkedListBox.Items.Add(document, CheckState.Unchecked) for document in documents if self.BaseDocuments[0] != document]
		checkedListBox.Anchor =  AnchorStyles.Right | AnchorStyles.Left | AnchorStyles.Bottom | AnchorStyles.Top
		self.GroupBoxDocuments.Controls.Add(checkedListBox)
		# Selection List
		checkedListParametersBox = CheckedListBox()
		checkedListParametersBox.Name = "ParameterList"
		checkedListParametersBox.Location = Point(15, 100)
		checkedListParametersBox.Width = 370
		checkedListParametersBox.Height = 380
		checkedListParametersBox.HorizontalScrollbar = True
		checkedListParametersBox.CheckOnClick = True
		checkedListParametersBox.Anchor =  AnchorStyles.Right | AnchorStyles.Left | AnchorStyles.Bottom | AnchorStyles.Top
		self.GroupBoxParameters.Controls.Add(checkedListParametersBox)
# Window Form Buttons
	def GenerateButtons(self):
		#Generate Buttons
		buttonCheck = Button()
		buttonCheck.Name = "ModelsCheck"
		buttonCheck.Text = "Check All"
		buttonCheck.Width = 120
		buttonCheck.Location = Point(15, 485)
		buttonCheck.Anchor =   AnchorStyles.Left | AnchorStyles.Bottom
		buttonCheck.Click += self.CheckAll
		self.GroupBoxDocuments.Controls.Add(buttonCheck)
		#Generate Buttons
		buttonUncheck = Button()
		buttonUncheck.Text = "Check None"
		buttonUncheck.Name = "ModelsUnCheck"
		buttonUncheck.Width = 120
		buttonUncheck.Location = Point(150, 485)
		buttonUncheck.Anchor =  AnchorStyles.Left | AnchorStyles.Bottom
		buttonUncheck.Click += self.UnCheckAll
		self.GroupBoxDocuments.Controls.Add(buttonUncheck)
		#Generate Buttons
		buttonCheck = Button()
		buttonCheck.Text = "Check All"
		buttonCheck.Name = "ParameterCheck"
		buttonCheck.Width = 120
		buttonCheck.Location = Point(15, 485)
		buttonCheck.Anchor =   AnchorStyles.Left | AnchorStyles.Bottom
		buttonCheck.Click += self.CheckAll
		self.GroupBoxParameters.Controls.Add(buttonCheck)
		#Generate Buttons
		buttonUncheck = Button()
		buttonUncheck.Text = "Check None"
		buttonUncheck.Name = "ParameterUnCheck"
		buttonUncheck.Width = 120
		buttonUncheck.Location = Point(150, 485)
		buttonUncheck.Anchor =   AnchorStyles.Left | AnchorStyles.Bottom
		buttonUncheck.Click += self.UnCheckAll
		self.GroupBoxParameters.Controls.Add(buttonUncheck)
		#Generate Buttons
		bNext = Button()
		bNext.Text = "Transfer"
		bNext.Width = 120
		bNext.Location = Point(130, 0)
		bNext.Click += self.Transfer
		#Generate Buttons
		buttonCancel = Button()
		buttonCancel.Text = "Cancel"
		buttonCancel.Width = 120
		buttonCancel.Location = Point(0, 0)
		buttonCancel.Click += self.Cancel
		#Generate auxiliar panel	
		panel = Panel()
		panel.Width = 250
		panel.Margin = Padding(10, 10, 10, 10)
		panel.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
		panel.Controls.Add(bNext)
		panel.Controls.Add(buttonCancel)
		self.TableLayout.Controls.Add(panel, 2, 2)
# Windows Form Groups
	def GenerateFormGroups(self):
		# Generate Group Views	
		groupBoxDocuments = GroupBox()
		groupBoxDocuments.Text = "Documents configuration"
		groupBoxDocuments.Size = Size(400, 540)
		groupBoxDocuments.Location = Point(20, 50)
		groupBoxDocuments.Anchor =  AnchorStyles.Right | AnchorStyles.Left | AnchorStyles.Bottom | AnchorStyles.Top
		groupBoxDocuments.Margin = Padding(10, 10, 10, 0)
		self.TableLayout.Controls.Add(groupBoxDocuments, 0, 1)
		self.GroupBoxDocuments = groupBoxDocuments
		# Generate Group Views	
		groupBoxParameters = GroupBox()
		groupBoxParameters.Text = "Parameters configuration"
		groupBoxParameters.Size = Size(400, 540)
		groupBoxParameters.Location = Point(20, 50)
		groupBoxParameters.Anchor = AnchorStyles.Right | AnchorStyles.Left | AnchorStyles.Bottom | AnchorStyles.Top
		groupBoxParameters.Margin = Padding(10, 10, 10, 0)
		self.TableLayout.Controls.Add(groupBoxParameters, 1, 1)
		self.GroupBoxParameters = groupBoxParameters		
# Generate Layout
	def GenerateTableLayout(self):
		tableLayout = TableLayoutPanel()
		tableLayout.Anchor = AnchorStyles.Right | AnchorStyles.Left | AnchorStyles.Bottom | AnchorStyles.Top
		tableLayout.ColumnCount = 2
		tableLayout.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 50))
		tableLayout.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 50))
		tableLayout.Location = Point(0, 0)
		tableLayout.RowCount = 3
		tableLayout.RowStyles.Add(RowStyle(SizeType.Absolute, 50))
		tableLayout.RowStyles.Add(RowStyle(SizeType.Percent,90))
		tableLayout.RowStyles.Add(RowStyle(SizeType.Absolute, 50))
		tableLayout.Size = Size(870, 690)
		tableLayout.Padding = Padding(10, 10, 20, 50)
		tableLayout.TabIndex = 0
		self.Controls.Add(tableLayout)
		self.TableLayout = tableLayout
# Constructor Method
	def __init__(self, application):
		self.ConfigureForm(application)
		self.GenerateTableLayout()
		self.GenerateFormGroups()
		self.GenerateFormSelectionList(ModelManager.GetModels(application))
		self.GenerateFormLabels()
		self.GenerateComboBoxes()	
		self.GenerateButtons()
		
class ModelManager():
	@staticmethod
	def GetModels(application):
		return [document.Title + ".rvt" for document in application.Documents if document.IsLinked == False and document.IsWorkshared]
	@staticmethod
	def GetModel(application, name):
		return [document for document in application.Documents if document.IsWorkshared and document.IsLinked == False and document.Title in name][0]
	@staticmethod
	def GetCategories(document):
		categories = [category.Name for category in document.Settings.Categories if category.CategoryType == CategoryType.Model and len(FilteredElementCollector(document).OfCategoryId(category.Id).WhereElementIsElementType().ToElements()) > 0 and "DWG" not in category.Name.upper()]
		categories.append("Project Information")
		categories.sort()
		return categories
	@staticmethod
	def GetCategory(application, name):
		document = [document  for document in application.Documents if document.IsLinked == False][0]
		return [category for category in document.Settings.Categories if category.Name == name][0]
	@staticmethod
	def GetProjectInformation(document):
		return document.ProjectInformation
         
class DataCollector():
	@staticmethod
	def GetTypes(document, category):
		return FilteredElementCollector(document).OfCategoryId(category.Id).WhereElementIsElementType().ToElements()
	@staticmethod
	def TransferData(baseDocument, transferDocuments, category, parameterNames):
		collectorBase = DataCollector.GetTypes(baseDocument,category)

		for transferDocument in transferDocuments:
			
			collectorTransfer = DataCollector.GetTypes(transferDocument, category)

			with Transaction(transferDocument) as tx:
				tx.Start("Set parameters")
				for transferElement in collectorTransfer:
					for baseElement in collectorBase:
						if Element.Name.__get__(baseElement) == Element.Name.__get__(transferElement):
							for parameterName in parameterNames:
								if len(baseElement.GetParameters(parameterName)) == 1 and len(transferElement.GetParameters(parameterName)) == 1:
									baseParameter = baseElement.LookupParameter(parameterName)
									transferParameter = transferElement.LookupParameter(parameterName)
								else:
									baseParameter = [parameter for parameter in baseElement.GetParameters(parameterName) if parameter.StorageType == StorageType.String]
									transferParameter = [parameter for parameter in transferElement.GetParameters(parameterName) if parameter.StorageType == StorageType.String]
								if baseParameter != None and transferParameter != None:
									if baseParameter.AsString() != transferParameter.AsString():
										try:
											transferParameter.Set(baseParameter.AsString())
										except:
											pass
				tx.Commit()
	@staticmethod
	def TransferProjectInformation(baseDocument, transferDocuments, parameterNames):
		
		infoBase = ModelManager.GetProjectInformation(baseDocument)

		for transferDocument in transferDocuments:

			infoTransfer = ModelManager.GetProjectInformation(transferDocument)

			with Transaction(transferDocument) as tx:
				tx.Start("Set Project Information")

				for baseParameter in infoBase.GetOrderedParameters():
					for transferParameter in infoTransfer.GetOrderedParameters():
						if baseParameter.Definition.Name == transferParameter.Definition.Name and baseParameter.Definition.Name in parameterNames:
							try:
								transferParameter.Set(baseParameter.AsString())
							except:
								pass

				tx.Commit()
		
# Generate TaskDialog Options Class
class TaskdialogResults():
# Define Show Cancel TaskDialog Method
    @staticmethod
    def ShowCancelTaskDialog():
        dialog = TaskDialog("Transfer data")
        dialog.MainInstruction = "Transfer process cancelled"
        dialog.MainContent = "Transfer data between models cancelled."
        dialog.TitleAutoPrefix = False
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconWarning
        dialog.Show()
# Define Show Process Finish TaskDialog Method
    @staticmethod
    def ShowCorrectTaskDialog():
        dialog = TaskDialog("Transfer data")
        dialog.TitleAutoPrefix = False
        dialog.MainInstruction = "Transfer process finished"
        dialog.MainContent = "Transfer data between models process finished Correctly."
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconInformation
        dialog.Show()

WindowTransfer(app).ShowDialog()