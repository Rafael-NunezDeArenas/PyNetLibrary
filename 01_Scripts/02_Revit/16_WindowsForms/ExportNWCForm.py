#region References

# Load the Python Standard and DesignScript Libraries
from datetime import date
import string
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

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

# Import Windows form
clr.AddReference("System.Windows.Forms")
# Import System Drawing
clr.AddReference("System.Drawing")

import System
from System.Windows.Forms import*
from System.Drawing import*

#endregion

#region Windows Form Classes

# Generate NWC Exportation Form
class WindowExport(Form):

# Generate Exportation
	@staticmethod
	def executeExportation(self, object):
		if object.Options.ExportScope == NavisworksExportScope.View:
			self.Close()
			if object.Output == None:
				dialog = TaskDialog("NWC Exporter")
				dialog.MainContent = "No Views Selected"
				dialog.CommonButtons = TaskDialogCommonButtons.Ok
				dialog.MainIcon = TaskDialogIcon.TaskDialogIconInformation
				dialog.Show()
			else:
				object.Close()
# Create a Txt Log
				if object.log != None:
					log = open(object.log + "/" + "NWC_Exporter_" + str(date.today()) + ".txt" ,"w")
					log.write("Document" + "\t" + "Status" + "\t" + "Exportation" + "\t" + "Output Exportation")
					log.close()
				else:
					log = None
# Collect all 3D Views and Determinate if the Views are Empty
				views = FilteredElementCollector(doc).OfClass(View3D).ToElements()
				filterViews = [n for n in views if n.Name in object.Output]
				opts = Options()
				opts.DetailLevel = ViewDetailLevel.Fine
# Iterate Views and Collect only Views that have Elements modelled
				viewsNotEmpty = object.EmptyViewFilter(views, opts)
# Export views to NWC
				for n in filterViews:
					if viewsNotEmpty.Contains(n) == True:
						object.Options.ViewId = n.Id
						doc.Export(object.Path, n.Name, object.Options)
						if object.log != None:
							log = open(object.log + "/" + "NWC_Exporter_" + str(date.today()) + ".txt" ,"a")
							log.write("\n" + doc.Title + "\t" + "Info" + "\t" + n.Name + ": View Exported" + "\t" + object.Path)
							log.close()
						self.ViewsExported.append(n.Name + ": View Exported")
					else:
						self.Errors.append(n.Name + ": Not Possible to Export the View. Empty View")
						if object.log != None:
							log = open(Exporterform.log + "/" + "NWC_Exporter_" + str(date.today()) + ".txt" ,"a")
							log.write("\n" + doc.Title + "\t" + "Error" + "\t" + n.Name + ": Not Possible to Export the View. Empty View" + "\t" + "Null")
							log.close()				
				self.Cancelled = False
				Exporterform.Cancelled = False
# If Export Scope option selected is Model
		elif Exporterform.Options.ExportScope == NavisworksExportScope.Model:
# Create a Txt Log and export Model to NWC
			if Exporterform.log != None:
				log = open(Exporterform.log + "/" + "NWC_Exporter_" + str(date.today()) + ".txt" ,"w")
				log.write("Document" + "\t" + "Status" + "\t" + "Exportation" + "\t" + "Output Exportation")
				log.close
			else:
				log = None
			try:
				doc.Export(Exporterform.Path, str(doc.Title), Exporterform.Options)
				self.ModelExported.append(doc.Title + ": Model Exported")
				if log != None:
					log = open(Exporterform.log + "/" + "NWC_Exporter_" + str(date.today()) + ".txt" ,"a")
					log.write("\n" + doc.Title + "\t" + "Info" + "\t" + doc.Title + ": Model Exported" + "\t" + Exporterform.Path)
					log.close
			except:
				self.Errors.append(str(doc.Title) + ": Not Possible to Export the Model")
				if log != None:
					log = open(Exporterform.log + "/" + "NWC_Exporter_" + str(date.today()) + ".txt" ,"a")
					log.write("\n" + doc.Title + "\t" + "Error" + "\t" + doc.Title + ": Not Possible to Export the View. Empty View" + "\t" + "Null")
					log.close
			self.Cancelled = False			
			object.Cancelled = False

# Determinate if the View is Empty
	@classmethod
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
								else:
									pass
					else:
						pass
			else:
				pass
		return viewsResult

# Export Button
	def Export(self, sender, args):
		self.Cancelled = False
# Output with the name of the link selected
		Resultform = WindowResult(self.Options.ExportScope)
		Resultform.ShowDialog()
		self.Resultform = Resultform
# Get Result Window
	def GetResultForm(self):
		return self.Resultform
# ComboBox buttons
	def CheckCOR(self, sender, args):
		if sender.SelectedItem == "Shared":
			self.Options.Coordinates = NavisworksCoordinates.Shared
		else:
			self.Options.Coordinates = NavisworksCoordinates.Internal			
	def CheckEO(self, sender, args):
		if sender.SelectedItem == "View":
			self.Options.ExportScope = NavisworksExportScope.View
		else:
			self.Options.ExportScope = NavisworksExportScope.Model	
# CheckBox Buttons
	def CheckCEP(self, sender, args):
		if sender.Checked:
			self.Options.ConvertElementProperties = True
		else:
			self.Options.ConvertElementProperties = False			
	def CheckCL(self, sender, args):
		if sender.Checked:
			self.Options.ConvertLights = True
		else:
			self.Options.ConvertLights = False	
	def CheckCCF(self, sender, args):
		if sender.Checked:
			self.Options.ConvertLinkedCADFormats = True
		else:
			self.Options.ConvertLinkedCADFormats = False
	def CheckDFL(self, sender, args):
		if sender.Checked:
			self.Options.DivideFileIntoLevels = True 
		else:
			self.Options.DivideFileIntoLevels = False		
	def CheckEID(self, sender, args):
		if sender.Checked:
			self.Options.ExportElementIds = True
		else:
			self.Options.ExportElementIds = False
	def CheckEL(self, sender, args):
		if sender.Checked:
			self.Options.ExportLinks = True
		else:
			self.Options.ExportLinks = False
	def CheckEP(self, sender, args):
		if sender.Checked:
			self.Options.ExportParts = True
		else:
			self.Options.ExportParts = False
	def CheckER(self, sender, args):
		if sender.Checked:
			self.Options.ExportRoomAsAttribute = True
		else:
			self.Options.ExportRoomAsAttribute = False
	def CheckERG(self, sender, args):
		if sender.Checked:
			self.Options.ExportRoomGeometry = True
		else:
			self.Options.ExportRoomGeometry = False		
	def CheckURL(self, sender, args):
		if sender.Checked:
			self.Options.ExportUrls = True
		else:
			self.Options.ExportUrls = False		
	def CheckMAT(self, sender, args):
		if sender.Checked:
			self.Options.FindMissingMaterials = True
		else:
			self.Options.FindMissingMaterials = False			
# Browser Button		
	def Browser(self, sender, args):
		if sender.Click:
			path = ""
			dialog = FolderBrowserDialog()
			dr = dialog.ShowDialog()
			if (dr == DialogResult.OK):
				path = dialog.SelectedPath
			self.Path = path
# Log Button		
	def logBrowser(self, sender, args):
		if sender.Click:
			log = ""
			dialog = FolderBrowserDialog()
			dr = dialog.ShowDialog()
			if (dr == DialogResult.OK):
				path = dialog.SelectedPath
			self.log = path
# CheckedBoxList Button
	def Include(self, sender, args):
		self.Output = sender.SelectedItems
# Cancel Button
	def Cancel(self, sender, args):
		if sender.Click:
			self.Close()
# Constructor Method
	def __init__(self, values):
#Scale window with resolution
		screenSize = Screen.GetWorkingArea(self)
		self.Width = 910
		self.Height = 620
		self.viewNames = values
		self.WIndowResult = None
# Include Icon
		self.Icon = Icon("NWCExporter.ico")
# Generate Tittle Value
		self.Text = "NWC Exporter"
# Generate Exporter Form Variables
		self.Output = None
		self.Path = None
		self.log = None
		self.Options = NavisworksExportOptions()
		self.Cancelled = True
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
# Description
		labelSheetName = Label(Text = "Select the 3DViews to Export to NWC and Select the Navisworks Setings to Configure the Exportation: ")
		labelSheetName.Parent = self
		labelSheetName.Width = 800
		labelSheetName.Height = 50
		labelSheetName.Location = Point(20, 10)
# Selection List
		lBox = ListBox()
		lBox.Location = Point(50, 90)
		lBox.Width = 300
		lBox.Height = 400
		lBox.SelectionMode = SelectionMode.MultiExtended
		lBox.Items.AddRange(tuple(self.viewNames))
		lBox.SelectedIndexChanged += self.Include
		self.Controls.Add(lBox)
# Generate Group	
		gB = GroupBox()
		gB.Text = "3D Views in Current Model: "
		gB.Size = Size(400, 450)
		gB.Location = Point(20, 60)
		gB.Parent = self
# Generate CheckBox	1
		checkboxCEP = CheckBox()
		checkboxCEP.Text = "Convert Element Properties"
		checkboxCEP.Location = Point(470, 100)
		checkboxCEP.Width = 250
		checkboxCEP.Font= Font("OpenSans", 8)
		checkboxCEP.CheckedChanged += self.CheckCEP
		self.Controls.Add(checkboxCEP)
		checkboxCEP.Checked = True
# ComboBox 1
		cBoxCoor = ComboBox()
		cBoxCoor.Location = Point(650, 125)
		cBoxCoor.Width = 100
		cBoxCoor.Items.AddRange(("Shared", "Project Internal"))
		cBoxCoor.DropDownStyle = ComboBoxStyle.DropDownList
		cBoxCoor.SelectedIndexChanged += self.CheckCOR
		self.Controls.Add(cBoxCoor)	
# Description ComboBox
		labelCoor = Label(Text = "Navisworks Coordinates")
		labelCoor.Parent = self
		labelCoor.Width = 250
		labelCoor.Height = 30
		labelCoor.Font= Font("OpenSans",8)
		labelCoor.Location = Point(470, 130)	
# Generate CheckBox	2	
		checkboxCL = CheckBox()
		checkboxCL.Text = "Convert Lights"
		checkboxCL.Location = Point(470, 160)
		checkboxCL.Width = 250
		checkboxCL.Font= Font("OpenSans",8)
		checkboxCL.CheckedChanged += self.CheckCL
		self.Controls.Add(checkboxCL)
# Generate CheckBox	3	
		checkboxCCF = CheckBox()
		checkboxCCF.Text = "Convert Linked CAD Formats"
		checkboxCCF.Location = Point(470, 190)
		checkboxCCF.Width = 250
		checkboxCCF.Font= Font("OpenSans",8)
		checkboxCCF.CheckedChanged += self.CheckCCF
		self.Controls.Add(checkboxCCF)
# Generate CheckBox	4	
		checkboxDFL = CheckBox()
		checkboxDFL.Text = "Divide File Into Levels"
		checkboxDFL.Location = Point(470, 220)
		checkboxDFL.Width = 250
		checkboxDFL.Font= Font("OpenSans",8)
		checkboxDFL.CheckedChanged += self.CheckDFL
		self.Controls.Add(checkboxDFL)
		checkboxDFL.Checked = True
# Generate CheckBox	5	
		checkboxEID = CheckBox()
		checkboxEID.Text = "Export Element IDs"
		checkboxEID.Location = Point(470, 250)
		checkboxEID.Width = 250
		checkboxEID.Font= Font("OpenSans",8)
		checkboxEID.CheckedChanged += self.CheckEID
		self.Controls.Add(checkboxEID)
		checkboxEID.Checked = True
# Generate CheckBox	6	
		checkboxEL = CheckBox()
		checkboxEL.Text = "Export Links"
		checkboxEL.Location = Point(470, 280)
		checkboxEL.Width = 250
		checkboxEL.Font= Font("OpenSans",8)
		checkboxEL.CheckedChanged += self.CheckEL
		self.Controls.Add(checkboxEL)
# Generate CheckBox	7	
		checkboxEP = CheckBox()
		checkboxEP.Text = "Export Parts"
		checkboxEP.Location = Point(470, 310)
		checkboxEP.Width = 250
		checkboxEP.Font= Font("OpenSans",8)
		checkboxEP.CheckedChanged += self.CheckEP
		self.Controls.Add(checkboxEP)
# Generate CheckBox	8	
		checkboxER = CheckBox()
		checkboxER.Text = "Export Rooms As Atribute"
		checkboxER.Location = Point(470, 340)
		checkboxER.Width = 250
		checkboxER.Font= Font("OpenSans",8)
		checkboxER.CheckedChanged += self.CheckER
		self.Controls.Add(checkboxER)
		checkboxER.Checked = True
# Generate CheckBox	9	
		checkboxERG = CheckBox()
		checkboxERG.Text = "Export Rooms Geometry"
		checkboxERG.Location = Point(470, 370)
		checkboxERG.Width = 250
		checkboxERG.Font= Font("OpenSans",8)
		checkboxERG.CheckedChanged += self.CheckERG
		self.Controls.Add(checkboxERG)
# ComboBox 2
		cBoxEO = ComboBox()
		cBoxEO.Location = Point(650, 395)
		cBoxEO.Width = 100
		cBoxEO.Items.AddRange(("View", "Model"))
		cBoxEO.DropDownStyle = ComboBoxStyle.DropDownList
		cBoxEO.SelectedIndexChanged += self.CheckEO
		self.Controls.Add(cBoxEO)	
# Description ComboBox 2
		labelExport = Label(Text = "Export Scope")
		labelExport.Parent = self
		labelExport.Width = 250
		labelExport.Height = 30
		labelExport.Font= Font("OpenSans",8)
		labelExport.Location = Point(470, 400)
# Generate CheckBox	10
		checkboxURL = CheckBox()
		checkboxURL.Text = "Export URLs"
		checkboxURL.Location = Point(470, 430)
		checkboxURL.Width = 250
		checkboxURL.Font= Font("OpenSans",8)
		checkboxURL.CheckedChanged += self.CheckURL
		self.Controls.Add(checkboxURL)
# Generate CheckBox	11
		checkboxMAT = CheckBox()
		checkboxMAT.Text = "Find Missing Materials"
		checkboxMAT.Location = Point(470, 460)
		checkboxMAT.Width = 250
		checkboxMAT.Font= Font("OpenSans",8)
		checkboxMAT.CheckedChanged += self.CheckMAT
		self.Controls.Add(checkboxMAT)	   		
# Generate Group
		gB = GroupBox()
		gB.Text = "Navisworks Settings:  "
		gB.Size = Size(400, 450)
		gB.Location = Point(450, 60)
		gB.Parent = self
# Generate Export Button
		bExport = Button()
		bExport.Text = "Export"
		bExport.Width = 120
		bExport.Location = Point(730, 530)
		bExport.Click += self.Export
		self.Controls.Add(bExport)
# Generate Browser Button
		bBrowser = Button()
		bBrowser.Width = 120
		bBrowser.Text = "Folder Browser"
		bBrowser.Location = Point(600, 530)
		bBrowser.Click += self.Browser
		self.Controls.Add(bBrowser)
# Generate Cancel Button
		bCancel = Button()
		bCancel.Width = 120
		bCancel.Text = "Cancel"
		bCancel.Location = Point(470, 530)
		bCancel.Click += self.Cancel
		self.Controls.Add(bCancel)
# Generate Log Button
		blog = Button()
		blog.Width = 120
		blog.Text = "Log Output"
		blog.Location = Point(20, 530)
		blog.Click += self.logBrowser
		self.Controls.Add(blog)

# Generate Accept or Cancel View Exportation to NWC
class WindowResult(Form):		
# Define Accept Button. Generate NWC Exportation		
	def Accept(self, sender, args):
		if sender.Click:
			WindowExport.executeExportation(self, Exporterform)
# Cancel Method
	def Cancel(self, sender, args):
		if sender.Click:
			self.Close()
# Constructor Method
	def __init__(self, exportOptions):
# Include Icon
		self.Icon = Icon("NWCExporter.ico")
# Generate Tittle Value
		self.Text = "NWC Exporter"
# Generate Variables
		self.Cancelled = True
		self.ViewsExported = []
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
# Description
		if self.ExportOption == NavisworksExportScope.View:
			labelSheetName = Label(Text = "View Scope Option Generate a NWC exportation of Each of the Selected Views, Are you sure you want to Continue?")
			labelSheetName.Parent = self
			labelSheetName.Width = 400
			labelSheetName.Height = 50
			labelSheetName.Location = Point(20, 20)
		elif self.ExportOption == NavisworksExportScope.Model:
			labelSheetName = Label(Text = "Model Scope Option Only Generate One Exportation With All the Model, Are you sure you want to Continue?")
			labelSheetName.Parent = self
			labelSheetName.Width = 400
			labelSheetName.Height = 50
			labelSheetName.Location = Point(20, 20)
# Generate Button
		bAccept = Button()
		bAccept.Text = "Accept"
		bAccept.Location = Point(320, 100)
		bAccept.Click += self.Accept
		self.Controls.Add(bAccept)
# Generate Button
		bCancel = Button()
		bCancel.Text = "Cancel"
		bCancel.Location = Point(400, 100)
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

#region Filter Form Output

# Determinate if the Input is a String, String Input is a finish Process Message
if isinstance(IN[0], str): #type: ignore
	OUT = IN[0] #type: ignore
# Determinate if the Input is a List. If it is a List there a are Filtered Views Ontained
if isinstance(IN[0][3], list): #type: ignore
	viewNames = tuple(IN[0][3]) #type: ignore
# Run Exporter Form
	Exporterform = WindowExport(viewNames)
	Exporterform.ShowDialog()

# endregion

#region NWC Export Output

# If the process is not cancelled
	if Exporterform.Cancelled == False:
		resultForm = Exporterform.GetResultForm()
		if resultForm.Cancelled == False:
# Determinate if the exportation have no errors and prepare the Output
			if resultForm.Errors.Count == 0:
				TaskdialogResults().ShowCorrectTaskDialog()
				OUT = resultForm.ViewsExported, resultForm.Errors	
			else:
				TaskdialogResults().ShowErrorsTaskDialog()
				OUT = resultForm.ViewsExported, resultForm.Errors
	else:
		TaskdialogResults().ShowCancelTaskDialog()
		OUT = "Operation Cancelled"

#endregion