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

#Import Windows form
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

# Sync Transfer Form

class InputData():
    @staticmethod
    def CreateJson(dictionary):
        if not os.path.exists(os.path.join(app.CurrentUserAddinsLocation, "Balio\\Support")):
            os.makedirs(os.path.join(app.CurrentUserAddinsLocation, "Balio\\Support"))
        path = os.path.join(app.CurrentUserAddinsLocation, "PythonRunner\\Support\\OpenModels.json")
        with open(path, "w") as file:
            json.dump(dictionary, file)
    @staticmethod
    def ReadJson():
        try:
            path = os.path.join(app.CurrentUserAddinsLocation, "PythonRunner\\Support\\OpenModels.json")
            with open(path, "r") as file:
                return json.load(file)
        except:
            return None

class UpdateForm(Form):
    # Update Legends Button
    def Update(self, sender, args):
        if self.Selection != None:
            for data in self.Selection:
                modelsData = []
                for data in self.Selection:
                    for model in self.ModelData:
                        if (data == model.Model):
                            modelsData.append(model)
                
            for model in modelsData:
                document = ModelManager.OpenCloudModel(model, self.Application)
                ModelManager.SynchronizeModel(document)
                document.Close(False)

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
                openDialog.Filter = "Txt files (*.xlsx)|*.xlsx|All files (*.*)|*.*"
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
    # Windows Form Configuration
    def ConfigureForm(self, application):
    # Include Icon
    #Generate Tittle Value
        self.Text = "Update models"
    #Form Variables
        self.ModelData = None
        self.Headers = ["Model Name", "Description", "Project", "HUB", "Type"]
        self.Application = application
        self.DocumentNames = None
        self.Selection = None
        self.DataPath = None
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
        labelGeneralDescription = Label(Text = "Select multiple BIM360 or ACC documents to open with closed worksets, Synchronize and close to update the information in the platform.")
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
        groupBoxViews.Text = "Models to update"
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
        dataGrid.Size = Size(900, 400)
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
        buttonBrowser.Text = "Browse Data"
        buttonBrowser.Location = Point(20, 570)
        buttonBrowser.Anchor = AnchorStyles.Left | AnchorStyles.Bottom
        buttonBrowser.Click += self.Browser
        self.Controls.Add(buttonBrowser)
        # Generate Update Button
        buttonUpdate = Button()
        buttonUpdate.Text = "Update"
        buttonUpdate.Width = 120
        buttonUpdate.Location = Point(850, 570)
        buttonUpdate.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
        buttonUpdate.Click += self.Update
        self.Controls.Add(buttonUpdate)
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
    # Constructor Class
    def __init__(self, application):
        self.ConfigureForm(application)
        self.GenerateFormLabels()
        data = InputData.ReadJson()
        if data != None and os.path.isfile(data["path"]):
            data = DataReader.ReadExcelData(data["path"])
            self.ModelData  = data[1]
            self.Headers = data[0]
            self.GenerateFormSelectionList(data[1])
        else:
            self.GenerateFormSelectionList(None)
        self.GenerateTextBox()        
        self.GenerateFormButtons()
        self.GenerateFormGroups()

class ModelData():
    def __init__(self, model, description, project, hub, type, projectGuid, modelGuid):
        self.modelName = model
        self.description = description
        self.projectName = project
        self.hub = hub
        self.type = type
        self.projectGuid = projectGuid
        self.modelGuid = modelGuid
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

class DataReader():
    @staticmethod
    def ReadExcelData(path):

        return None

class ModelManager():
    @staticmethod
    def OpenCloudModel(modelData, application):
        if modelData.Model not in ModelManager.GetModels(application):
            projectGuid = System.Guid(modelData.ProjectGuid)
            modelGuid = System.Guid(modelData.ModelGuid)       
            options = OpenOptions()
            openConfiguration = WorksetConfiguration(WorksetConfigurationOption.OpenLastViewed)
            options.SetOpenWorksetsConfiguration(openConfiguration)
            try:
                modelPath = ModelPathUtils.ConvertCloudGUIDsToCloudPath(ModelPathUtils.CloudRegionEMEA, projectGuid, modelGuid)
                document = application.Application.OpenDocumentFile(modelPath, options)
                print("Document opened: {name}".format(name = document.Title))
                return document
            except:
                modelPath = ModelPathUtils.ConvertCloudGUIDsToCloudPath(ModelPathUtils.CloudRegionUS, projectGuid, modelGuid)
                document = application.Application.OpenDocumentFile(modelPath, options)
                print("Document opened: {name}".format(name = document.Title))
                return document
    @staticmethod
    def GetModels(application):
        documents = application.Application.Documents
        return [document.Title + ".rvt" for document in documents if document.IsLinked == False]
    @staticmethod
    def SynchronizeModel(document):
        transactWithCentralOptions = TransactWithCentralOptions()
        transactCallBack = SyncLockCallback()
        transactWithCentralOptions.SetLockCallback(transactCallBack)
        synchronizeWithCentralOptions = SynchronizeWithCentralOptions()
        relinquishOptions = RelinquishOptions(False)
        relinquishOptions.CheckedOutElements = True
        relinquishOptions.FamilyWorksets = True
        relinquishOptions.StandardWorksets = True
        relinquishOptions.UserWorksets = True
        relinquishOptions.ViewWorksets = True
        synchronizeWithCentralOptions.SetRelinquishOptions(relinquishOptions)
        synchronizeWithCentralOptions.Comment = "Python Runner synchronize"

        document.SynchronizeWithCentral(transactWithCentralOptions, synchronizeWithCentralOptions)
        print("Document synchronized: {name}".format(name = document.Title))

# Generate TaskDialog Options Class
class TaskdialogResults:
# Define Show Cancel TaskDialog Method
    @staticmethod
    def ShowCancelTaskDialog():
        dialog = TaskDialog("Update models")
        dialog.MainInstruction = "Update process cancelled"
        dialog.MainContent = "Update multiple models process cancelled."
        dialog.TitleAutoPrefix = False
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconWarning
        dialog.Show()
# Define Show Process Finish TaskDialog Method
    @staticmethod
    def ShowCorrectTaskDialog():
        dialog = TaskDialog("Update models")
        dialog.TitleAutoPrefix = False
        dialog.MainInstruction = "Update process finished"
        dialog.MainContent = "Update multiple models process finished correctly."
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconInformation
        dialog.Show()

class SyncLockCallback(ICentralLockedCallback):
    def ShouldWaitForLockAvailability(self):
        return False


UpdateForm(uiapp).ShowDialog()