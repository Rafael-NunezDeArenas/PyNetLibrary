import clr
import json
import System
from pathlib import Path
from System import Environment

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from Autodesk.Revit.DB import *
from System.Windows.Forms import *
from System.Drawing import *
from Autodesk.Revit.UI import TaskDialog, TaskDialogCommonButtons, TaskDialogIcon

uiapp = __revit__  #type:ignore
app = __revit__.Application
REVIT_ICON = Path.home() / "AppData" / "Roaming" / "Autodesk" / "ApplicationPlugins" / "Raen.Revit.Pynet.bundle" / "Revit.ico"  #type:ignore
uidoc = __revit__.ActiveUIDocument  #type:ignore
doc = uidoc.Document


class InputData:
    @staticmethod
    def _get_path(app):
        support_dir = Path(app.CurrentUserAddinsLocation) / "Balio" / "Support"
        support_dir.mkdir(parents=True, exist_ok=True)
        return support_dir / "OpenModels.json"

    @staticmethod
    def CreateJson(dictionary):
        path = InputData._get_path(app)
        path.write_text(json.dumps(dictionary))

    @staticmethod
    def ReadJson():
        try:
            path = InputData._get_path(app)
            return json.loads(path.read_text())
        except:
            return None


class UpdateForm(Form):
    def __init__(self, application):
        super().__init__()
        self.ConfigureForm(application)
        self.GenerateFormLabels()
        data = InputData.ReadJson()
        if data is not None and Path(data["path"]).is_file():
            data = DataReader.ReadExcelData(data["path"])
            self.ModelData = data[1]
            self.Headers = data[0]
            self.GenerateFormSelectionList(data[1])
        else:
            self.GenerateFormSelectionList(None)
        self.GenerateTextBox()
        self.GenerateFormButtons()
        self.GenerateFormGroups()

    def Update(self, sender, args):
        if self.Selection is not None:
            modelsData = []
            for data in self.Selection:
                for model in self.ModelData:
                    if data == model.Model:
                        modelsData.append(model)
            for model in modelsData:
                document = ModelManager.OpenCloudModel(model, self.Application)
                ModelManager.SynchronizeModel(document)
                document.Close(False)
            TaskdialogResults.ShowCorrectTaskDialog()
            self.Close()

    def Cancel(self, sender, args):
        self.DialogResult = DialogResult.Cancel
        self.Status = "Cancel"
        TaskdialogResults.ShowCancelTaskDialog()
        self.Close()

    def Browser(self, sender, args):
        with OpenFileDialog() as openDialog:
            desktop = Environment.GetFolderPath(Environment.SpecialFolder.Desktop)
            openDialog.InitialDirectory = desktop
            openDialog.Filter = "Excel files (*.xlsx)|*.xlsx|All files (*.*)|*.*"
            if openDialog.ShowDialog() == DialogResult.OK:
                self.DataPath = openDialog.FileName
                data = DataReader.ReadExcelData(openDialog.FileName)
                self.ModelData = data[1]
                self.Headers = data[0]
                listControl = [control for control in self.Controls if control.Name == "ModelsList"][0]
                self.LoadModelListData(listControl, data[1])
                InputData.CreateJson({"path": openDialog.FileName})

    def ApplyFilter(self, sender, arg):
        listControl = [control for control in self.Controls if control.Name == "ModelsList"][0]
        rows = listControl.Rows
        if len(sender.Text) > 0:
            for row in rows:
                if row.Visible and sender.Text not in row.Cells[0].Value:
                    row.Visible = False
                elif not row.Visible and sender.Text in row.Cells[0].Value:
                    row.Visible = True
        else:
            for row in rows:
                row.Visible = True

    def Include(self, sender, args):
        self.Selection = [row.Cells[0].Value for row in sender.SelectedRows if row.Visible]

    def ConfigureForm(self, application):
        self.Text = "Update models"
        if REVIT_ICON.exists():
            self.Icon = Icon(str(REVIT_ICON))
        self.ModelData = None
        self.Headers = ["Model Name", "Description", "Project", "HUB", "Type"]
        self.Application = application
        self.DocumentNames = None
        self.Selection = None
        self.DataPath = None
        self.WindowState = FormWindowState.Normal
        self.CenterToScreen()
        self.BringToFront()
        self.Topmost = True
        self.screenSize = Screen.GetWorkingArea(self)
        self.Width = 1000
        self.Height = 650
        self.MinimumSize = Size(1000, 650)
        self.FormBorderStyle = FormBorderStyle.Sizable
        self.MaximizeBox = True

    def GenerateFormLabels(self):
        label1 = Label()
        label1.Text = "Select multiple BIM360 or ACC documents to open, synchronize, and close to update the platform."
        label1.Parent = self
        label1.Width = 500
        label1.Height = 50
        label1.Location = Point(20, 10)
        label1.Anchor = AnchorStyles.Left | AnchorStyles.Top
        label2 = Label()
        label2.Text = "Model name filter: "
        label2.Parent = self
        label2.Width = 120
        label2.Height = 25
        label2.Location = Point(600, 93)
        label2.Anchor = AnchorStyles.Right | AnchorStyles.Top

    def GenerateFormGroups(self):
        groupBoxViews = GroupBox()
        groupBoxViews.Text = "Models to update"
        groupBoxViews.Size = Size(950, 490)
        groupBoxViews.Location = Point(20, 60)
        groupBoxViews.Anchor = AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Bottom | AnchorStyles.Top
        groupBoxViews.Parent = self

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
        if documents is not None:
            self.LoadModelListData(dataGrid, documents)
        dataGrid.SelectionChanged += self.Include
        self.Controls.Add(dataGrid)

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

    def GenerateFormButtons(self):
        buttonBrowser = Button()
        buttonBrowser.Width = 120
        buttonBrowser.Text = "Browse Data"
        buttonBrowser.Location = Point(20, 570)
        buttonBrowser.Anchor = AnchorStyles.Left | AnchorStyles.Bottom
        buttonBrowser.Click += self.Browser
        self.Controls.Add(buttonBrowser)
        buttonUpdate = Button()
        buttonUpdate.Text = "Update"
        buttonUpdate.Width = 120
        buttonUpdate.Location = Point(850, 570)
        buttonUpdate.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
        buttonUpdate.Click += self.Update
        self.Controls.Add(buttonUpdate)
        buttonCancel = Button()
        buttonCancel.Width = 120
        buttonCancel.Text = "Cancel"
        buttonCancel.Location = Point(720, 570)
        buttonCancel.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
        buttonCancel.Click += self.Cancel
        self.Controls.Add(buttonCancel)

    def GenerateTextBox(self):
        textBox = TextBox()
        textBox.Location = Point(725, 90)
        textBox.Width = 225
        textBox.Anchor = AnchorStyles.Right | AnchorStyles.Top
        textBox.TextChanged += self.ApplyFilter
        self.Controls.Add(textBox)


class ModelData:
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


class DataReader:
    @staticmethod
    def ReadExcelData(path):
        return None


class SyncLockCallback(ICentralLockedCallback):
    def ShouldWaitForLockAvailability(self):
        return False


class ModelManager:
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
                print("Document opened: {name}".format(name=document.Title))
                return document
            except:
                modelPath = ModelPathUtils.ConvertCloudGUIDsToCloudPath(ModelPathUtils.CloudRegionUS, projectGuid, modelGuid)
                document = application.Application.OpenDocumentFile(modelPath, options)
                print("Document opened: {name}".format(name=document.Title))
                return document

    @staticmethod
    def GetModels(application):
        documents = application.Application.Documents
        return [document.Title + ".rvt" for document in documents if not document.IsLinked]

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
        print("Document synchronized: {name}".format(name=document.Title))


class TaskdialogResults:
    @staticmethod
    def ShowCancelTaskDialog():
        dialog = TaskDialog("Update models")
        dialog.MainInstruction = "Update process cancelled"
        dialog.MainContent = "Update multiple models process cancelled."
        dialog.TitleAutoPrefix = False
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconWarning
        dialog.Show()

    @staticmethod
    def ShowCorrectTaskDialog():
        dialog = TaskDialog("Update models")
        dialog.TitleAutoPrefix = False
        dialog.MainInstruction = "Update process finished"
        dialog.MainContent = "Update multiple models process finished correctly."
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconInformation
        dialog.Show()


print("Opening Update Models dialog...")
UpdateForm(uiapp).ShowDialog()
