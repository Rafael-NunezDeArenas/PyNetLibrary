#region References

# Load the Python Standard and DesignScript Libraries
import clr
import sys

sys.path.append("C:\\Program Files (x86)\\IronPython 2.7\\Lib")
import os
import json

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import *
import Autodesk

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

# Import Windows form
clr.AddReference("System.Windows.Forms")
# Import System Drawing
clr.AddReference("System.Drawing")

import System
from System.Windows.Forms import*
from System.Drawing import*
from System.Collections.Generic import List
from datetime import date

uiapp = __revit__ #type:ignore
app = __revit__.Application #type:ignore
uidoc = __revit__.ActiveUIDocument #type:ignore
doc = uidoc.Document

#endregion

class InputData():
    @staticmethod
    def CreateJson(dictionary):
        if not os.path.exists(os.path.join(app.CurrentUserAddinsLocation, "Balio\\Support")):
            os.makedirs(os.path.join(app.CurrentUserAddinsLocation, "Balio\\Support"))
        path = os.path.join(app.CurrentUserAddinsLocation, "Balio\\Support\\OpenModels.json")
        with open(path, "w") as file:
            json.dump(dictionary, file)
    @staticmethod
    def ReadJson():
        try:
            path = os.path.join(app.CurrentUserAddinsLocation, "Balio\\Support\\OpenModels.json")
            with open(path, "r") as file:
                return json.load(file)
        except:
            return None

class OpenForm(Form):
    # Update Legends Button
    def Open(self, sender, args):
        if self.Selection != None:
            modelsData = []
            for data in self.Selection:
                for model in self.ModelData:
                    if (data == model.Model):
                        modelsData.append(model)

            for model in modelsData:
                uiDocument = ModelManager.OpenCloudModel(model, self.Application, self.CloseModelWorksets)
                if uiDocument != None:
                    view = ModelManager.ChangeView(model, uiDocument)
                    if view != None:
                        ModelManager.CloseStartView(uiDocument, view)
                    
            TaskdialogResults.ShowCorrectTaskDialog() 
            self.Close()     
    # Generate Function for Cancel Button		
    def Cancel(self, sender, args):
        if sender.Click:
            self.DialogResult = DialogResult.Cancel
            self.Status = "Cancel"
            
            TaskdialogResults.ShowCancelTaskDialog()
            self.Close()    
    # Browser Button
    def Browser(self, sender, args):
        if sender.Click:
            with OpenFileDialog() as openDialog:
                openDialog.InitialDirectory = os.path.join(os.path.expanduser('~'), 'Desktop')
                openDialog.Filter = "Excel files (*.xlsx)|*.xlsx|All files (*.*)|*.*"
                if openDialog.ShowDialog() == DialogResult.OK:
                    self.DataPath = openDialog.FileName
                    data  = DataReader.ReadExcelData(openDialog.FileName)
                    self.ModelData  = data[1]
                    self.Headers = data[0]
                    listControl = [control for control in self.Controls if control.Name == "ModelsList"][0]
                    self.LoadModelListData(listControl, data[1])
                    InputData.CreateJson({"path": openDialog.FileName})
    # Filter Button
    def ApplyFilter(self, sender, arg):
        listControl = [control for control in self.Controls if control.Name == "ModelsList"][0]
        rows = listControl.Rows
        if len(sender.Text) > 0:
            for row in rows:
                if row.Visible == True and sender.Text not in row.Cells[0].Value:
                    row.Visible = False
                elif row.Visible == False and sender.Text in row.Cells[0].Value:
                    row.Visible = True
        else:
            for row in rows:
                row.Visible = True
    # Generate Function to include selected elements in Group Box
    def Include(self, sender, args):
        self.Selection = [row.Cells[0].Value for row in sender.SelectedRows if row.Visible == True]
    # CheckBox Buttons
    def CloseWorksets(self, sender, args):
        if sender.Checked:
            self.CloseModelWorksets = True
        else:
            self.CloseModelWorksets = False   
    # Windows Form Configuration
    def ConfigureForm(self, application):
    # Include Icon

    #Generate Tittle Value
        self.Text = "Open models"
    #Form Variables
        self.ModelData = None
        self.Headers = ["Model Name", "Description", "Project", "HUB", "Type"]
        self.Application = application
        self.DocumentNames = None
        self.Selection = None
        self.DataPath = None
        self.CloseModelWorksets = False
    #Window dimension
        self.WindowState = FormWindowState.Normal
    #Generate Window in Center
        self.CenterToScreen()
    #Window in front
        self.BringToFront()
        self.Topmost = True
    #Scale window with resolution
        self.screenSize = Screen.GetWorkingArea(self)
        self.Width = 1000
        self.Height = 650
        self.MinimumSize = Size(1000, 650)
    #Block Dimension of window
        self.FormBorderStyle = FormBorderStyle.Sizable
        self.MaximizeBox = True			
        screenSize = Screen.GetWorkingArea(self)
    # Windows Form Labels
    def GenerateFormLabels(self):
        # Description General
        labelGeneralDescription = Label(Text = "Select multiple BIM 360 or ACC documents to open.")
        labelGeneralDescription.Parent = self
        labelGeneralDescription.Width = 500
        labelGeneralDescription.Height = 50
        labelGeneralDescription.Location = Point(20, 10)
        labelGeneralDescription.Anchor = AnchorStyles.Left | AnchorStyles.Top
        # Filter Label
        labelGeneralDescription = Label(Text = "Model name filter: ")
        labelGeneralDescription.Parent = self
        labelGeneralDescription.Width = 120
        labelGeneralDescription.Height = 25
        labelGeneralDescription.Location = Point(600, 93)
        labelGeneralDescription.Anchor = AnchorStyles.Right | AnchorStyles.Top
    # Windows Form Groups
    def GenerateFormGroups(self):
        # Generate Group Views	
        groupBoxViews = GroupBox()
        groupBoxViews.Text = "Models to open"
        groupBoxViews.Size = Size(950, 490)
        groupBoxViews.Location = Point(20, 60)
        groupBoxViews.Anchor = AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Bottom | AnchorStyles.Top
        groupBoxViews.Parent = self
    # Windows Form Datagrid
    def GenerateFormSelectionList(self, documents):
        dataGrid = DataGridView()
        dataGrid.Name = "ModelsList"
        dataGrid.BackgroundColor = Color.White
        dataGrid.Location = Point(50, 140)
        dataGrid.Size = Size(900, 360)
        dataGrid.Anchor = AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Bottom | AnchorStyles.Top
        dataGrid.ColumnCount = 5
        dataGrid.AllowUserToAddRows = False
        dataGrid.AllowUserToDeleteRows = False
        dataGrid.RowHeadersVisible = False
        dataGrid.ReadOnly = True
        dataGrid.AllowUserToResizeRows = False
        dataGrid.SelectionMode = DataGridViewSelectionMode.FullRowSelect
        dataGrid.ColumnHeadersHeight = 40
        dataGrid.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.DisableResizing
        for count in range(len(self.Headers)):
            dataGrid.Columns[count].AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill
            dataGrid.Columns[count].HeaderCell.Value = self.Headers[count]
        if documents != None:
            self.LoadModelListData(dataGrid, documents)
        dataGrid.SelectionChanged += self.Include
        self.Controls.Add(dataGrid)
    # Load Data in Datagrid View 
    def LoadModelListData(self, dataGrid, documents):
        dataGrid.Rows.Clear()
        for count in range(len(documents)):
            dataGrid.Rows.Add()
            row = dataGrid.Rows[count]
            row.Cells[0].Value = documents[count].Model
            row.Cells[1].Value = documents[count].Description
            row.Cells[2].Value = documents[count].Project
            row.Cells[3].Value = documents[count].Hub
            row.Cells[4].Value = documents[count].Type
    # Windows Form Buttons
    def GenerateFormButtons(self):
        # Generate Browser Button
        buttonBrowser = Button()
        buttonBrowser.Width = 120
        buttonBrowser.Text = "Browse data"
        buttonBrowser.Location = Point(20, 570)
        buttonBrowser.Anchor = AnchorStyles.Left | AnchorStyles.Bottom
        buttonBrowser.Click += self.Browser
        self.Controls.Add(buttonBrowser)
        # Generate Update Button
        buttonOpen = Button()
        buttonOpen.Text = "Open"
        buttonOpen.Width = 120
        buttonOpen.Location = Point(850, 570)
        buttonOpen.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
        buttonOpen.Click += self.Open
        self.Controls.Add(buttonOpen)
    # Generate Cancel Button
        buttonCancel = Button()
        buttonCancel.Width = 120
        buttonCancel.Text = "Cancel"
        buttonCancel.Location = Point(720, 570)
        buttonCancel.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
        buttonCancel.Click += self.Cancel
        self.Controls.Add(buttonCancel)
    # Windows Form Text Box
    def GenerateTextBox(self):
        textBox = TextBox()
        textBox.Location = Point(725, 90)
        textBox.Width = 225
        textBox.Anchor = AnchorStyles.Right | AnchorStyles.Top
        textBox.TextChanged += self.ApplyFilter
        self.Controls.Add(textBox)
    # Windows Form Check Boxes
    def GenerateFormCheckBoxes(self):
        # Generate CheckBox	Convert Element Properties
        checkBoxWorkSets = CheckBox()
        checkBoxWorkSets.Text = "Close worksets"
        checkBoxWorkSets.Location = Point(50, 510)
        checkBoxWorkSets.Width = 250
        checkBoxWorkSets.Font= Font("OpenSans", 8)
        checkBoxWorkSets.Anchor = AnchorStyles.Left | AnchorStyles.Bottom
        checkBoxWorkSets.CheckedChanged += self.CloseWorksets
        self.Controls.Add(checkBoxWorkSets)
        checkBoxWorkSets.Checked = False
    # Constructor Class
    def __init__(self, application):
        self.ConfigureForm(application)
        self.GenerateFormLabels()
        data = InputData.ReadJson()
        if data != None and os.path.isfile(data["path"]):
            data = DataReader.ReadExcelData(data["path"])
            self.ModelData = data[1]
            self.Headers = data[0]
            self.GenerateFormSelectionList(data[1])
        else:
            self.GenerateFormSelectionList(None)
        self.GenerateFormCheckBoxes()     
        self.GenerateTextBox()        
        self.GenerateFormButtons()
        self.GenerateFormGroups()

class ModelData():
    def __init__(self, model, description, project, hub, type, projectGuid, modelGuid, defaultView):
        self.modelName = model
        self.description = description
        self.projectName = project
        self.hub = hub
        self.type = type
        self.projectGuid = projectGuid
        self.modelGuid = modelGuid
        self.defaultView = defaultView
    @property
    def Model(self):
        return self.modelName
    @property
    def Description(self):
        return self.description
    @property
    def Project(self):
        return self.projectName
    @property
    def Hub(self):
        return self.hub
    @property
    def Type(self):
        return self.type
    @property
    def ProjectGuid(self):
        return self.projectGuid
    @property
    def ModelGuid(self):
        return self.modelGuid
    @property
    def DefaultView(self):
        return self.defaultView

class DataReader():
    @staticmethod
    def ReadExcelData(path):
        return None
class ModelManager():
    @staticmethod
    def OpenCloudModel(modelData, application, worksetConfiguration):
        if modelData.Model not in ModelManager.GetModels(application):
            projectGuid = System.Guid(modelData.ProjectGuid)
            modelGuid = System.Guid(modelData.ModelGuid)       
            options = OpenOptions()
            if worksetConfiguration == True:
                openConfiguration = WorksetConfiguration(WorksetConfigurationOption.CloseAllWorksets)
            else:
                openConfiguration = WorksetConfiguration(WorksetConfigurationOption.OpenAllWorksets)
            options.SetOpenWorksetsConfiguration(openConfiguration)
            try:
                modelPath = ModelPathUtils.ConvertCloudGUIDsToCloudPath(ModelPathUtils.CloudRegionEMEA, projectGuid, modelGuid)
                uiDocument = application.OpenAndActivateDocument(modelPath, options, False)
                print("Document opened: {name}".format(name = uiDocument.Document.Title))
                return uiDocument
            except:
                modelPath = ModelPathUtils.ConvertCloudGUIDsToCloudPath(ModelPathUtils.CloudRegionUS, projectGuid, modelGuid)
                uiDocument = application.OpenAndActivateDocument(modelPath, options, False)
                print("Document opened: {name}".format(name = uiDocument.Document.Title))
                return uiDocument
        else:
            print("Document already open: {name}".format(name = modelData.Model.split(".")[0]))
    @staticmethod
    def GetModels(application):
        documents = application.Application.Documents
        return [document.Title + ".rvt" for document in documents if document.IsLinked == False and document.IsWorkshared]
    @staticmethod
    def ChangeView(modelData, uiDocument):        
        defaultView = ModelManager.GetDefaultView(modelData, uiDocument.Document)
        if defaultView != None:
            uiDocument.ActiveView = defaultView
            print("Default view opened: {name}".format(name = defaultView.Name))
            return defaultView
        return None
    @staticmethod
    def GetDefaultView(modelData, document):
        collector = FilteredElementCollector(document).OfCategory(BuiltInCategory.OST_Views).WhereElementIsNotElementType().ToElements()
        for view in collector:
            if view.Name == modelData.DefaultView:
                return view
        return None
    @staticmethod 
    def CloseStartView(uidoc, view):
        for uiView in uidoc.GetOpenUIViews():
            if uiView.ViewId != view.Id:
                uiView.Close()
     
# Generate TaskDialog Options Class
class TaskdialogResults:
# Define Show Cancel TaskDialog Method
    @staticmethod
    def ShowCancelTaskDialog():
        dialog = TaskDialog("Open models")
        dialog.MainInstruction = "Open process cancelled"
        dialog.MainContent = "Open multiple models process cancelled."
        dialog.TitleAutoPrefix = False
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconWarning
        dialog.Show()
# Define Show Process Finish TaskDialog Method
    @staticmethod
    def ShowCorrectTaskDialog():
        dialog = TaskDialog("Open models")
        dialog.TitleAutoPrefix = False
        dialog.MainInstruction = "Open process finished"
        dialog.MainContent = "Open multiple models process finished correctly."
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconInformation
        dialog.Show()


OpenForm(uiapp).ShowDialog()