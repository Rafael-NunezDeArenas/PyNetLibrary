#region References

# Load the Python Standard and DesignScript Libraries
from datetime import date, datetime
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

#region Windows Form Classes

# Generate Log Class
class NWCExporterLog():
	# Open NWC Exporter Log Method
	def OpenLog(self):
		log = open(self.logPath ,"a")
		return log
	# Write Model Exported Lines Method
	def WriteLogModel(self, document, bool = True):
		log = self.OpenLog()
		if bool == True:
			log.write("{line}{date}{tab}{doc}{tab}Info{tab}{doc}: Model Exported{tab}{path}".format(line = "\n", tab = "\t", date = str(datetime.now()), doc = document.Title, path = self.logPath))
		else:
			log.write("{line}{date}{tab}{doc}{tab}Error{tab}{doc}: Not Possible to Export the Model{tab}Null".format(line = "\n", tab = "\t", date = str(datetime.now()), doc = document.Title))
		log.close()
	# Write View Exported Lines Method
	def WriteLogView(self, view, document, bool = True):
		log = self.OpenLog()
		if bool == True:
			log.write("{line}{date}{tab}{doc}{tab}Info{tab}{view}: View Exported{tab}{path}".format(line = "\n", tab = "\t", date = str(datetime.now()), doc = document.Title, view = view.Name, path = self.logPath))
		else:
			log.write("{line}{date}{tab}{doc}{tab}Error{tab}{view}: Not Possible to Export the View. Empty View{tab}Null".format(line = "\n", tab = "\t", date = str(datetime.now()), doc = document.Title, view = view.Name))
		log.close()
	# Constructor Method
	def __init__(self, path):
		if path != None:
			self.logPath = "{browser}/NWC_Exporter_{date}.txt".format(browser = path, date = str(date.today()))
			log = open(self.logPath,"w")
			log.write("Tracking{tab}Document{tab}Status{tab}Exportation{tab}Output Exportation".format(tab = "\t"))
			log.close()

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
		return parameters

# Generate def for Combo Box
	def GetParameter(self, sender, args):
		self.Param = sender.SelectedItem
# Generate def for Value Box	
	def GetValue(self, sender, args):
		self.Value = sender.Text	

# Get Parameter Provider
	def GetParameterProvider(self):
		iterator = doc.ParameterBindings.ForwardIterator()
		self.evaluator = FilterStringEquals()
		# Iterate an Get Parameter Selected in Combo Box
		while iterator.MoveNext():
			if iterator.Key.Name == self.Param:
				self.provider = ParameterValueProvider(iterator.Key.Id)
				break
# Get Filter Views
	def GetFilterViews(self):
		filter = FilterStringRule(self.provider, self.evaluator, self.Value, True)
		filterViews = ElementParameterFilter(filter)
		# Filter Views with Conditions
		collector = FilteredElementCollector(doc).OfClass(View3D).WherePasses(filterViews).ToElements()
		self.Views = [view.Name for view in collector]

# Generate Function for Next Button	
	def Next(self, sender, args):
		# If Click in the Button, Filter Views with a Project Parameter
		if sender.Click:
			self.GetParameterProvider()
		# Determinate if the Provider is not Null and Create a String Contains Filter	
			if self.provider == None or self.Value == None:
				self.Status = "Missing"
			else:
				self.GetFilterViews()
		# Determinate of the Filter Views are not Zero				
				if self.Views.Count < 1:
					self.Status = "Empty"
			self.DialogResult = DialogResult.OK
			self.Close()
# Generate Function for Cancel Button		
	def Cancel(self, sender, args):
		if sender.Click:
			self.DialogResult = DialogResult.Cancel
			self.Status = "Cancel"
			self.Close()

# Windows Form Configuration
	def ConfigureForm(self, parameters):
		# Include Icon
		self.Icon = Icon("C:\\Program Files\\Autodesk\\Revit 2021\\Revit.ico")
		#Generate Tittle Value
		self.Text = "NWC Exporter"
		#Form Variables
		self.Parameters = parameters
		self.Param = None
		self.Value = None
		self.Views = None
		self.provider = None
		self.evaluator = None
		self.Status = None
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
		self.Height = 240
		#Block Dimension of window
		self.FormBorderStyle = FormBorderStyle.FixedDialog
# Window Form Labels
	def GenerateFormLabels(self):
		#Description 1	
		labelGeneralDescriptio = Label(Text = "Select Project Parameter to use in the 3Dview Filter:")
		labelGeneralDescriptio.Parent = self
		labelGeneralDescriptio.Width = 350
		labelGeneralDescriptio.Height = 20
		labelGeneralDescriptio.Location = Point(20, 10)
		#Description 2
		labelGeneralDescriptio = Label(Text = "Add the Value of the Parameter to filter the 3Dviews: ")
		labelGeneralDescriptio.Parent = self
		labelGeneralDescriptio.Width = 350
		labelGeneralDescriptio.Height = 20
		labelGeneralDescriptio.Location = Point(20, 80)
# Window Form ComboBoxes
	def GenerateComboBoxes(self):
		#Selection Combo Box Bar
		cBox = ComboBox()
		cBox.Location = Point(20, 40)
		cBox.Width = self.screenSize.Width / 7
		cBox.DataSource = self.Parameters
		cBox.DropDownStyle = ComboBoxStyle.DropDownList
		cBox.SelectedIndexChanged += self.GetParameter
		self.Controls.Add(cBox)	
# Window Form TextBox
	def GenerateTextBox(self):
		#Generate TextBox
		tBox = TextBox()
		tBox.Location = Point(20, 110)
		tBox.Width = self.screenSize.Width / 7
		tBox.TextChanged += self.GetValue
		self.Controls.Add(tBox)
# Window Form Buttons
	def GenerateButtons(self):
		#Generate Buttons
		bNext = Button()
		bNext.Text = "Next"
		bNext.Location = Point(290, 150)
		bNext.Click += self.Next
		self.Controls.Add(bNext)
		#Generate Buttons
		buttonCancel = Button()
		buttonCancel.Text = "Cancel"
		buttonCancel.Location = Point(200, 150)
		buttonCancel.Click += self.Cancel
		self.Controls.Add(buttonCancel)

# Constructor Method
	def __init__(self, parameters):
		self.ConfigureForm(parameters)
		self.GenerateFormLabels()
		self.GenerateComboBoxes()
		self.GenerateTextBox()
		self.GenerateButtons()

# Generate NWC Exportation Form
class WindowExport(Form):
# Generate Exportation
	@staticmethod
	def ExecuteExportation(result, object):
		if object.Options.ExportScope == NavisworksExportScope.View:
			result.Close()
			if object.Output == None:
				object.ShowNotViewsSelectedDialog()
			else:
				object.Close()
				object.ExportViews(object, result)

# If Export Scope option selected is Model
		if object.Options.ExportScope == NavisworksExportScope.Model:
			result.Close()
# Create a Txt Log and export Model to NWC
			if object.Output != None:
				object.ExportModel(object, result)

# Determinate if the View is Empty
	def EmptyViewFilter(self, viewsToAnalyze, options):
		viewsResult = []
		for n in viewsToAnalyze:
			if n.IsTemplate == False:
				collector = FilteredElementCollector(doc, n.Id)
				elementsInView = collector.WhereElementIsViewIndependent().ToElements()
				for m in elementsInView:
					if viewsResult.Contains(n) == False:
						if m.Category != None and hasattr(m.Category, "CategoryType") and m.Category.CategoryType == CategoryType.Model and m.get_Geometry(options) != None:
							geometry = m.get_Geometry(options)
							for geoElem in geometry:
								if hasattr(geoElem, "Volume") and geoElem.Volume > 0:
									viewsResult.append(n)
		return viewsResult
# Not Filter TaskDialog
	def ShowNotViewsSelectedDialog(self):
		dialog = TaskDialog("NWC Exporter")
		dialog.MainContent = "No Views Selected"
		dialog.CommonButtons = TaskDialogCommonButtons.Ok
		dialog.MainIcon = TaskDialogIcon.TaskDialogIconInformation
		dialog.Show()
# Export Views to NWC
	def ExportViews(self, object, result):
		# Create a Txt Log
		exporterLog = NWCExporterLog(object.log)
		# Collect all 3D Views and Determinate if the Views are Empty
		views = FilteredElementCollector(doc).OfClass(View3D).ToElements()
		filterViews = [n for n in views if n.Name in object.Output]
		opts = Options()
		opts.DetailLevel = ViewDetailLevel.Fine
		# Iterate Views and Collect only Views that have Elements modelled
		viewsNotEmpty = object.EmptyViewFilter(views, opts)
		# Export views to NWC
		for view in filterViews:
			if viewsNotEmpty.Contains(view) == True:
				object.Options.ViewId = view.Id
				doc.Export(object.Path, view.Name, object.Options)
				result.ElementsExported.append(view.Name + ": View Exported")
				if object.log != None:
					exporterLog.WriteLogView(view, doc)
			else:
				result.Errors.append(view.Name + ": Not Possible to Export the View. Empty View")
				if object.log != None:
					exporterLog.WriteLogView(view, doc, False)
# Export Model to NWC
	def ExportModel(self, object, result):
	# Create a Txt Log and export Model to NWC
		if object.log != None:
			log = NWCExporterLog(object.log)
		try:
			doc.Export(object.Path, str(doc.Title), object.Options)
			result.ElementsExported.append(doc.Title + ": Model Exported")
			if object.log != None:
				log.WriteLogModel(doc)
		except:
			result.Errors.append(str(doc.Title) + ": Not Possible to Export the Model")
			if object.log != None:
				log.WriteLogModel(doc, False)

# Export Button
	def Export(self, sender, args):
		self.DialogResult = DialogResult.OK
# Output with the name of the link selected
		Resultform = WindowResult(self.Options.ExportScope)
		Resultform.ShowDialog()
		self.Resultform = Resultform
# Cancel Button
	def Cancel(self, sender, args):
		if sender.Click:
			self.DialogResult = DialogResult.Cancel
			self.Close()
# Get Result Window
	def GetResultForm(self):
		return self.Resultform
# ComboBox buttons
	def CheckCoordinates(self, sender, args):
		if sender.SelectedItem == "Shared":
			self.Options.Coordinates = NavisworksCoordinates.Shared
		else:
			self.Options.Coordinates = NavisworksCoordinates.Internal			
	def CheckExportScope(self, sender, args):
		if sender.SelectedItem == "View":
			self.Options.ExportScope = NavisworksExportScope.View
		else:
			self.Options.ExportScope = NavisworksExportScope.Model	
# CheckBox Buttons
	def CheckConvertElementProperties(self, sender, args):
		if sender.Checked:
			self.Options.ConvertElementProperties = True
		else:
			self.Options.ConvertElementProperties = False			
	def CheckConverLights(self, sender, args):
		if sender.Checked:
			self.Options.ConvertLights = True
		else:
			self.Options.ConvertLights = False	
	def CheckConvertLinkedCadFormat(self, sender, args):
		if sender.Checked:
			self.Options.ConvertLinkedCADFormats = True
		else:
			self.Options.ConvertLinkedCADFormats = False
	def CheckDivideFileIntoLevels(self, sender, args):
		if sender.Checked:
			self.Options.DivideFileIntoLevels = True 
		else:
			self.Options.DivideFileIntoLevels = False		
	def CheckExportElementIds(self, sender, args):
		if sender.Checked:
			self.Options.ExportElementIds = True
		else:
			self.Options.ExportElementIds = False
	def CheckExportLinks(self, sender, args):
		if sender.Checked:
			self.Options.ExportLinks = True
		else:
			self.Options.ExportLinks = False
	def CheckExportParts(self, sender, args):
		if sender.Checked:
			self.Options.ExportParts = True
		else:
			self.Options.ExportParts = False
	def CheckExportRoomAsAttribute(self, sender, args):
		if sender.Checked:
			self.Options.ExportRoomAsAttribute = True
		else:
			self.Options.ExportRoomAsAttribute = False
	def CheckExportRoomGeometry(self, sender, args):
		if sender.Checked:
			self.Options.ExportRoomGeometry = True
		else:
			self.Options.ExportRoomGeometry = False		
	def CheckExportUrl(self, sender, args):
		if sender.Checked:
			self.Options.ExportUrls = True
		else:
			self.Options.ExportUrls = False		
	def CheckFindMissingMaterials(self, sender, args):
		if sender.Checked:
			self.Options.FindMissingMaterials = True
		else:
			self.Options.FindMissingMaterials = False			
# Browser Button		
	def Browser(self, sender, args):
		if sender.Click:
			path = None
			with FolderBrowserDialog() as dialog:
				if dialog.ShowDialog() == DialogResult.OK:
					path = dialog.SelectedPath
				self.Path = path
# Log Button		
	def LogBrowser(self, sender, args):
		if sender.Click:
			log = None
			with FolderBrowserDialog() as dialog:
				if (dialog.ShowDialog() == DialogResult.OK):
					log = dialog.SelectedPath
				self.log = log
# CheckedBoxList Button
	def Include(self, sender, args):
		self.Output = sender.SelectedItems

# Windows Form Configuration
	def ConfigureForm(self, values):
		#Scale window with resolution
		screenSize = Screen.GetWorkingArea(self)
		self.Width = 910
		self.Height = 620
		self.viewNames = values
		self.WindowResult = None
		# Include Icon
		self.Icon = Icon("C:\\Program Files\\Autodesk\\Revit 2021\\Revit.ico")
		# Generate Tittle Value
		self.Text = "NWC Exporter"
		# Generate Exporter Form Variables
		self.Output = None
		self.Path = None
		self.log = None
		self.Options = NavisworksExportOptions()
		self.Resultform = None
		# Window dimension
		self.WindowState = FormWindowState.Normal
		# Generate Window in Center
		self.CenterToScreen()
		# Window in front
		self.BringToFront()
		self.Topmost = True
		# Block Dimension of window
		self.FormBorderStyle = FormBorderStyle.FixedDialog
		# Scale window with resolution			
		screenSize = Screen.GetWorkingArea(self)
# Windows Form ComboBoxes
	def GenerateFormComboBoxes(self):
		# ComboBox Coordinates
		comboBoxCoordinates = ComboBox()
		comboBoxCoordinates.Location = Point(650, 125)
		comboBoxCoordinates.Width = 100
		comboBoxCoordinates.Items.AddRange(("Shared", "Project Internal"))
		comboBoxCoordinates.DropDownStyle = ComboBoxStyle.DropDownList
		comboBoxCoordinates.SelectedIndexChanged += self.CheckCoordinates
		self.Controls.Add(comboBoxCoordinates)	
		# ComboBox Export Scope
		combBoxExportScope = ComboBox()
		combBoxExportScope.Location = Point(650, 395)
		combBoxExportScope.Width = 100
		combBoxExportScope.Items.AddRange(("View", "Model"))
		combBoxExportScope.DropDownStyle = ComboBoxStyle.DropDownList
		combBoxExportScope.SelectedIndexChanged += self.CheckExportScope
		self.Controls.Add(combBoxExportScope)
# Windows Form Labels
	def GenerateFormLabels(self):
		# Description General
		labelGeneralDescription = Label(Text = "Select the 3DViews to Export to NWC and Select the Navisworks Setings to Configure the Exportation: ")
		labelGeneralDescription.Parent = self
		labelGeneralDescription.Width = 800
		labelGeneralDescription.Height = 50
		labelGeneralDescription.Location = Point(20, 10)
		# Description ComboBox Coordinates
		labelCoordinates = Label(Text = "Navisworks Coordinates")
		labelCoordinates.Parent = self
		labelCoordinates.Width = 250
		labelCoordinates.Height = 30
		labelCoordinates.Font= Font("OpenSans",8)
		labelCoordinates.Location = Point(470, 130)
		# Description ComboBox export Scope
		labelExportScope = Label(Text = "Export Scope")
		labelExportScope.Parent = self
		labelExportScope.Width = 250
		labelExportScope.Height = 30
		labelExportScope.Font= Font("OpenSans",8)
		labelExportScope.Location = Point(470, 400)
# Windows Form Selection List
	def GenerateFormSelectionList(self):
		# Selection List
		listBox = ListBox()
		listBox.Location = Point(50, 90)
		listBox.Width = 300
		listBox.Height = 400
		listBox.SelectionMode = SelectionMode.MultiExtended
		listBox.DataSource = self.viewNames
		listBox.SelectedIndexChanged += self.Include
		self.Controls.Add(listBox)
# Windows Form Groups
	def GenerateFormGroups(self):
		# Generate Group Views	
		groupBoxViews = GroupBox()
		groupBoxViews.Text = "3D Views in Current Model: "
		groupBoxViews.Size = Size(400, 450)
		groupBoxViews.Location = Point(20, 60)
		groupBoxViews.Parent = self
		# Generate Group Settings
		groupBoxSettings = GroupBox()
		groupBoxSettings.Text = "Navisworks Settings:  "
		groupBoxSettings.Size = Size(400, 450)
		groupBoxSettings.Location = Point(450, 60)
		groupBoxSettings.Parent = self
# Windows Form Check Boxes
	def GenerateFormCheckBoxes(self):
		# Generate CheckBox	Convert Element Properties
		checkBoxConvertElementProperties = CheckBox()
		checkBoxConvertElementProperties.Text = "Convert Element Properties"
		checkBoxConvertElementProperties.Location = Point(470, 100)
		checkBoxConvertElementProperties.Width = 250
		checkBoxConvertElementProperties.Font= Font("OpenSans", 8)
		checkBoxConvertElementProperties.CheckedChanged += self.CheckConvertElementProperties
		self.Controls.Add(checkBoxConvertElementProperties)
		checkBoxConvertElementProperties.Checked = True
		# Generate CheckBox	Convert Lights
		checkBoxConverLights = CheckBox()
		checkBoxConverLights.Text = "Convert Lights"
		checkBoxConverLights.Location = Point(470, 160)
		checkBoxConverLights.Width = 250
		checkBoxConverLights.Font= Font("OpenSans",8)
		checkBoxConverLights.CheckedChanged += self.CheckConverLights
		self.Controls.Add(checkBoxConverLights)
		# Generate CheckBox	Convert Link Cad Format
		checkBoxConvertLinkedCadFormat = CheckBox()
		checkBoxConvertLinkedCadFormat.Text = "Convert Linked CAD Formats"
		checkBoxConvertLinkedCadFormat.Location = Point(470, 190)
		checkBoxConvertLinkedCadFormat.Width = 250
		checkBoxConvertLinkedCadFormat.Font= Font("OpenSans",8)
		checkBoxConvertLinkedCadFormat.CheckedChanged += self.CheckConvertLinkedCadFormat
		self.Controls.Add(checkBoxConvertLinkedCadFormat)
		# Generate CheckBox	Divide File Into Levels
		checkBoxDivideFileIntoLevels = CheckBox()
		checkBoxDivideFileIntoLevels.Text = "Divide File Into Levels"
		checkBoxDivideFileIntoLevels.Location = Point(470, 220)
		checkBoxDivideFileIntoLevels.Width = 250
		checkBoxDivideFileIntoLevels.Font= Font("OpenSans",8)
		checkBoxDivideFileIntoLevels.CheckedChanged += self.CheckDivideFileIntoLevels
		self.Controls.Add(checkBoxDivideFileIntoLevels)
		checkBoxDivideFileIntoLevels.Checked = True
		# Generate CheckBox	Check Export Elements Ids
		checkBoxExportElementIds = CheckBox()
		checkBoxExportElementIds.Text = "Export Element IDs"
		checkBoxExportElementIds.Location = Point(470, 250)
		checkBoxExportElementIds.Width = 250
		checkBoxExportElementIds.Font= Font("OpenSans",8)
		checkBoxExportElementIds.CheckedChanged += self.CheckExportElementIds
		self.Controls.Add(checkBoxExportElementIds)
		checkBoxExportElementIds.Checked = True
		# Generate CheckBox	Export Links
		CheckBoxExportLinks = CheckBox()
		CheckBoxExportLinks.Text = "Export Links"
		CheckBoxExportLinks.Location = Point(470, 280)
		CheckBoxExportLinks.Width = 250
		CheckBoxExportLinks.Font= Font("OpenSans",8)
		CheckBoxExportLinks.CheckedChanged += self.CheckExportLinks
		self.Controls.Add(CheckBoxExportLinks)
		# Generate CheckBox	Export Parts
		CheckBoxExportParts = CheckBox()
		CheckBoxExportParts.Text = "Export Parts"
		CheckBoxExportParts.Location = Point(470, 310)
		CheckBoxExportParts.Width = 250
		CheckBoxExportParts.Font= Font("OpenSans",8)
		CheckBoxExportParts.CheckedChanged += self.CheckExportParts
		self.Controls.Add(CheckBoxExportParts)
		# Generate CheckBox	Export Rooms As Atributes
		CheckBoxExportRoomAsAttribute = CheckBox()
		CheckBoxExportRoomAsAttribute.Text = "Export Rooms As Atribute"
		CheckBoxExportRoomAsAttribute.Location = Point(470, 340)
		CheckBoxExportRoomAsAttribute.Width = 250
		CheckBoxExportRoomAsAttribute.Font= Font("OpenSans",8)
		CheckBoxExportRoomAsAttribute.CheckedChanged += self.CheckExportRoomAsAttribute
		self.Controls.Add(CheckBoxExportRoomAsAttribute)
		CheckBoxExportRoomAsAttribute.Checked = True
		# Generate CheckBox	Export Room Geometry
		CheckBoxCheckExportRoomGeometry = CheckBox()
		CheckBoxCheckExportRoomGeometry.Text = "Export Rooms Geometry"
		CheckBoxCheckExportRoomGeometry.Location = Point(470, 370)
		CheckBoxCheckExportRoomGeometry.Width = 250
		CheckBoxCheckExportRoomGeometry.Font= Font("OpenSans",8)
		CheckBoxCheckExportRoomGeometry.CheckedChanged += self.CheckExportRoomGeometry
		self.Controls.Add(CheckBoxCheckExportRoomGeometry)
		# Generate CheckBox	Export Urls
		CheckBoxExportUrl = CheckBox()
		CheckBoxExportUrl.Text = "Export URLs"
		CheckBoxExportUrl.Location = Point(470, 430)
		CheckBoxExportUrl.Width = 250
		CheckBoxExportUrl.Font= Font("OpenSans",8)
		CheckBoxExportUrl.CheckedChanged += self.CheckExportUrl
		self.Controls.Add(CheckBoxExportUrl)
		# Generate CheckBox	Find Missing Materials
		CheckBoxFindMissingMaterials = CheckBox()
		CheckBoxFindMissingMaterials.Text = "Find Missing Materials"
		CheckBoxFindMissingMaterials.Location = Point(470, 460)
		CheckBoxFindMissingMaterials.Width = 250
		CheckBoxFindMissingMaterials.Font= Font("OpenSans",8)
		CheckBoxFindMissingMaterials.CheckedChanged += self.CheckFindMissingMaterials
		self.Controls.Add(CheckBoxFindMissingMaterials)	   
# Windows Form Buttons
	def GenerateFormButtons(self):
		# Generate Export Button
		buttonExport = Button()
		buttonExport.Text = "Export"
		buttonExport.Width = 120
		buttonExport.Location = Point(730, 530)
		buttonExport.Click += self.Export
		self.Controls.Add(buttonExport)
# Generate Browser Button
		buttonBrowser = Button()
		buttonBrowser.Width = 120
		buttonBrowser.Text = "Folder Browser"
		buttonBrowser.Location = Point(600, 530)
		buttonBrowser.Click += self.Browser
		self.Controls.Add(buttonBrowser)
# Generate Cancel Button
		buttonCancel = Button()
		buttonCancel.Width = 120
		buttonCancel.Text = "Cancel"
		buttonCancel.Location = Point(470, 530)
		buttonCancel.Click += self.Cancel
		self.Controls.Add(buttonCancel)
# Generate Log Button
		buttonLog = Button()
		buttonLog.Width = 120
		buttonLog.Text = "Log Output"
		buttonLog.Location = Point(20, 530)
		buttonLog.Click += self.LogBrowser
		self.Controls.Add(buttonLog)

# Constructor Method
	def __init__(self, values):
		self.ConfigureForm(values)
		self.GenerateFormComboBoxes()
		self.GenerateFormLabels()
		self.GenerateFormSelectionList()
		self.GenerateFormCheckBoxes()
		self.GenerateFormButtons()
		self.GenerateFormGroups()

# Generate Accept or Cancel View Exportation to NWC
class WindowResult(Form):		
# Define Accept Button. Generate NWC Exportation		
	def Accept(self, sender, args):
		if sender.Click:
			WindowExport.ExecuteExportation(self, Exporterform)
			self.DialogResult = DialogResult.OK
# Cancel Method
	def Cancel(self, sender, args):
		if sender.Click:
			self.DialogResult = DialogResult.Cancel
			self.Close()

# Windows Form Configuration
	def ConfigureForm(self, exportOptions):
		# Include Icon
		self.Icon = Icon("C:\\Program Files\\Autodesk\\Revit 2021\\Revit.ico")
		# Generate Tittle Value
		self.Text = "NWC Exporter"
		# Generate Variables
		self.ElementsExported = []
		self.Errors = []
		self.ExportOption = exportOptions
		# Window dimension
		self.WindowState = FormWindowState.Normal
		# Generate Window in Center
		self.CenterToScreen()
		# Window in front
		self.BringToFront()
		self.Topmost = True
		# Scale window with resolution
		screenSize = Screen.GetWorkingArea(self)
		self.Width = 510
		self.Height = 190
		# Block Dimension of window
		self.FormBorderStyle = FormBorderStyle.FixedDialog
# Window Form Labels
	def GenerateFormLabels(self):
		# Description
		if self.ExportOption == NavisworksExportScope.View:
			labelGeneralDescriptio = Label(Text = "View Scope Option Generate a NWC exportation of Each of the Selected Views, Are you sure you want to Continue?")
			labelGeneralDescriptio.Parent = self
			labelGeneralDescriptio.Width = 400
			labelGeneralDescriptio.Height = 50
			labelGeneralDescriptio.Location = Point(20, 20)
		if self.ExportOption == NavisworksExportScope.Model:
			labelGeneralDescriptio = Label(Text = "Model Scope Option Only Generate One Exportation With All the Model, Are you sure you want to Continue?")
			labelGeneralDescriptio.Parent = self
			labelGeneralDescriptio.Width = 400
			labelGeneralDescriptio.Height = 50
			labelGeneralDescriptio.Location = Point(20, 20)
# Window Form Buttons
	def GenerateButtons(self):
		# Generate Button
		bAccept = Button()
		bAccept.Text = "Accept"
		bAccept.Location = Point(320, 100)
		bAccept.Click += self.Accept
		self.Controls.Add(bAccept)
# Generate Button
		buttonCancel = Button()
		buttonCancel.Text = "Cancel"
		buttonCancel.Location = Point(400, 100)
		buttonCancel.Click += self.Cancel
		self.Controls.Add(buttonCancel)

# Constructor Method
	def __init__(self, exportOptions):
		self.ConfigureForm(exportOptions)
		self.GenerateFormLabels()
		self.GenerateButtons()

# Generate TaskDialog Options Class
class TaskdialogResults():
# Define Show Cancel TaskDialog Method
	@staticmethod
	def ShowCancelTaskDialog():
		dialog = TaskDialog("NWC Exporter")
		dialog.MainContent = "Export Cancelled"
		dialog.TitleAutoPrefix = False
		dialog.CommonButtons = TaskDialogCommonButtons.Ok
		dialog.MainIcon = TaskDialogIcon.TaskDialogIconWarning
		dialog.Show()
# Define Show Process Finish TaskDialog Method
	@staticmethod
	def ShowCorrectTaskDialog():
		dialog = TaskDialog("NWC Exporter")
		dialog.TitleAutoPrefix = False
		dialog.MainContent = "Process Finished"
		dialog.CommonButtons = TaskDialogCommonButtons.Ok
		dialog.MainIcon = TaskDialogIcon.TaskDialogIconInformation
		dialog.Show()
# Define Show Process Finish with Errors TaskDialog Method
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
filterform = WindowFilter(WindowFilter.GetParameterBindings(doc))
filterform.ShowDialog()
# Generate Outputs if you Click in Cancel Button. Show TaskDialog Operation Cancelled
if filterform.DialogResult == DialogResult.Cancel:
	filterFormResult = "Process Canceled"
	TaskdialogResults().ShowCancelTaskDialog()
# If you not Cancell the Operation. Generate OUT if the Filter process do not Generate a Correct Result
resultMesages = {"Cancel": "No 3DViews Collected with Current Information", "Missing": "Not possible to Collect 3DViews, missing Imput", "Empty": "Not possible to Collect 3DViews with Current Inputs"}
if filterform.DialogResult == DialogResult.OK:
	filterFormResult = resultMesages.get(filterform.Status)
# Generate the OUT with a Correct Result
if filterFormResult == None:
		filterFormResult = "Project Parameter Selected: {0}".format(filterform.Param), "Parameter Value Indicated: {0}".format(filterform.Value), "Filtered Views: {0}".format(filterform.Views)
# Determinate if the Input is a String, String Input is a finish Process Message
if isinstance(filterFormResult, str):
	nwcExporterResult  = filterFormResult
	print(filterFormResult)
# Determinate if the Input is a List. If it is a List there a are Filtered Views Ontained
if isinstance(filterFormResult, tuple):
# Run Exporter Form
	print(filterFormResult)
	Exporterform = WindowExport(filterform.Views)
	Exporterform.ShowDialog()

# endregion

#region NWC Export Output

# If the process is not cancelled
	if Exporterform.DialogResult == DialogResult.OK:
		resultForm = Exporterform.GetResultForm()
		if resultForm.DialogResult == DialogResult.OK:
# Determinate if the exportation have no errors and prepare the Output
			if resultForm.Errors.Count == 0:
				TaskdialogResults().ShowCorrectTaskDialog()
				nwcExporterResult = resultForm.ElementsExported, "Errors: {0}".format(resultForm.Errors)	
			else:
				TaskdialogResults().ShowErrorsTaskDialog()
				nwcExporterResult = resultForm.ElementsExported, resultForm.Errors
	if Exporterform.DialogResult == DialogResult.Cancel:
		TaskdialogResults().ShowCancelTaskDialog()
		nwcExporterResult = "Process Canceled"
	print(nwcExporterResult)

#endregion