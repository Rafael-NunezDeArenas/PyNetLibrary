import clr
import json
from pathlib import Path
from System import Environment

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from Autodesk.Revit.DB import *
from System.Windows.Forms import *
from System.Drawing import *
from Autodesk.Revit.UI import TaskDialog, TaskDialogCommonButtons, TaskDialogIcon, TaskDialogCommandLinkId

app = __revit__.Application
REVIT_ICON = Path.home() / "AppData" / "Roaming" / "Autodesk" / "ApplicationPlugins" / "Raen.Revit.Pynet.bundle" / "Revit.ico"  #type:ignore


class KeynotesManagerForm(Form):
    def __init__(self, application):
        super().__init__()
        self.ConfigureForm(application)
        self.GenerateFormLabels()
        self.GenerateFormSelectionList(DocumentManager.GetDocumentNames(application))
        data = InputData.ReadJson()
        if data is not None and Path(data["path"]).is_file():
            self.Data = DataReader.ReadExcelData(data["path"])
            self.DictionaryPath = data["path"]
        self.GenerateFormCheckBoxes()
        self.GenerateTextBox()
        self.GenerateFormButtons()
        self.GenerateFormGroups()

    def LoadData(self, sender, args):
        if self.Selection is not None:
            if self.LoadTxtFile:
                TransactionManager.LoadKeyNotes(self.Application, self.Selection, self.NotesPath)
            if not self.FillParameterData:
                TaskdialogResults.ShowCorrectTaskDialog()
            else:
                dialogResult = TaskdialogResults.LoadExecutionTaskDialog(self.DictionaryPath).Show()
                print("Txt File Loaded")
                if dialogResult == dialogResult.CommandLink1:
                    TransactionManager.FillKeyNotes(self.Application, self.Selection, self.Data)
                    print("Materials and elements Data Filled")
                    TaskdialogResults.ShowCorrectTaskDialog()
                elif dialogResult == dialogResult.CommandLink2:
                    self.BrowseExcel()
                    print("Excel data Reloaded")
                    TransactionManager.FillKeyNotes(self.Application, self.Selection, self.Data)
                    print("Materials and elements Data Filled")
                    TaskdialogResults.ShowCorrectTaskDialog()
                else:
                    TaskdialogResults.ShowCancelTaskDialog()
            self.Close()

    def Cancel(self, sender, args):
        self.DialogResult = DialogResult.Cancel
        self.Status = "Cancel"
        TaskdialogResults.ShowCancelTaskDialog()
        self.Close()

    def BrowserNotes(self, sender, args):
        self.NotesPath = StandardDialogs.CreateOpenDialog()

    def BrowserDiccionary(self, sender, args):
        self.BrowseExcel()

    def BrowseExcel(self):
        with OpenFileDialog() as openDialog:
            desktop = Environment.GetFolderPath(Environment.SpecialFolder.Desktop)
            openDialog.InitialDirectory = desktop
            openDialog.Filter = "Excel files (*.xlsx)|*.xlsx|All files (*.*)|*.*"
            if openDialog.ShowDialog() == DialogResult.OK:
                self.DataPath = openDialog.FileName
                self.Data = DataReader.ReadExcelData(openDialog.FileName)
                self.DictionaryPath = openDialog.FileName
                InputData.CreateJson({"path": openDialog.FileName})

    def ApplyFilter(self, sender, arg):
        listControl = [control for control in self.Controls if control.Name == "ModelsList"][0]
        listControl.Items.Clear()
        for m in [model for model in self.DocumentNames if sender.Text in model]:
            listControl.Items.Add(m)

    def LoadTxt(self, sender, args):
        self.LoadTxtFile = sender.Checked

    def FillData(self, sender, args):
        self.FillParameterData = sender.Checked

    def Include(self, sender, args):
        self.Selection = sender.SelectedItems

    def ConfigureForm(self, application):
        self.Text = "Keynotes manager"
        if REVIT_ICON.exists():
            self.Icon = Icon(str(REVIT_ICON))
        self.Application = application
        self.DocumentNames = None
        self.Selection = None
        self.NotesPath = None
        self.LoadTxtFile = True
        self.FillParameterData = False
        self.Data = None
        self.DictionaryPath = None
        self.WindowState = FormWindowState.Normal
        self.CenterToScreen()
        self.BringToFront()
        self.Topmost = True
        self.screenSize = Screen.GetWorkingArea(self)
        self.Width = 600
        self.Height = 650
        self.MinimumSize = Size(600, 650)
        self.FormBorderStyle = FormBorderStyle.Sizable
        self.MaximizeBox = True

    def GenerateFormLabels(self):
        label1 = Label()
        label1.Text = "Select multiple models to load or reload the Keynotes file and fill the KeyNotes values using a dictionary file."
        label1.Parent = self
        label1.Width = 400
        label1.Height = 50
        label1.Location = Point(20, 10)
        label1.Anchor = AnchorStyles.Left | AnchorStyles.Top
        label2 = Label()
        label2.Text = "Model name filter: "
        label2.Parent = self
        label2.Width = 120
        label2.Height = 25
        label2.Location = Point(200, 93)
        label2.Anchor = AnchorStyles.Right | AnchorStyles.Top

    def GenerateFormGroups(self):
        groupBoxViews = GroupBox()
        groupBoxViews.Text = "Documents to load data"
        groupBoxViews.Size = Size(550, 490)
        groupBoxViews.Location = Point(20, 60)
        groupBoxViews.Anchor = AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Bottom | AnchorStyles.Top
        groupBoxViews.Parent = self

    def GenerateFormSelectionList(self, documents):
        listBox = ListBox()
        listBox.Name = "ModelsList"
        listBox.Location = Point(50, 140)
        listBox.Width = 500
        listBox.Height = 370
        listBox.SelectionMode = SelectionMode.MultiExtended
        listBox.HorizontalScrollbar = True
        for doc_name in (documents or []):
            listBox.Items.Add(doc_name)
        self.DocumentNames = documents
        listBox.Anchor = AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Bottom | AnchorStyles.Top
        listBox.SelectedIndexChanged += self.Include
        self.Controls.Add(listBox)

    def GenerateFormButtons(self):
        buttonBrowserTxt = Button()
        buttonBrowserTxt.Width = 120
        buttonBrowserTxt.Text = "Browse txt"
        buttonBrowserTxt.Location = Point(20, 570)
        buttonBrowserTxt.Anchor = AnchorStyles.Left | AnchorStyles.Bottom
        buttonBrowserTxt.Click += self.BrowserNotes
        self.Controls.Add(buttonBrowserTxt)
        buttonBrowserDiccionary = Button()
        buttonBrowserDiccionary.Width = 130
        buttonBrowserDiccionary.Text = "Browse dictionary"
        buttonBrowserDiccionary.Location = Point(150, 570)
        buttonBrowserDiccionary.Anchor = AnchorStyles.Left | AnchorStyles.Bottom
        buttonBrowserDiccionary.Click += self.BrowserDiccionary
        self.Controls.Add(buttonBrowserDiccionary)
        buttonSync = Button()
        buttonSync.Text = "Load"
        buttonSync.Width = 120
        buttonSync.Location = Point(450, 570)
        buttonSync.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
        buttonSync.Click += self.LoadData
        self.Controls.Add(buttonSync)
        buttonCancel = Button()
        buttonCancel.Width = 120
        buttonCancel.Text = "Cancel"
        buttonCancel.Location = Point(320, 570)
        buttonCancel.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
        buttonCancel.Click += self.Cancel
        self.Controls.Add(buttonCancel)

    def GenerateTextBox(self):
        textBox = TextBox()
        textBox.Location = Point(325, 90)
        textBox.Width = 225
        textBox.Anchor = AnchorStyles.Top | AnchorStyles.Right
        textBox.TextChanged += self.ApplyFilter
        self.Controls.Add(textBox)

    def GenerateFormCheckBoxes(self):
        checkBoxLoadTxt = CheckBox()
        checkBoxLoadTxt.Text = "Load Data from Txt"
        checkBoxLoadTxt.Location = Point(50, 510)
        checkBoxLoadTxt.Width = 150
        checkBoxLoadTxt.Font = Font("OpenSans", 8)
        checkBoxLoadTxt.CheckedChanged += self.LoadTxt
        checkBoxLoadTxt.Anchor = AnchorStyles.Left | AnchorStyles.Top
        self.Controls.Add(checkBoxLoadTxt)
        checkBoxLoadTxt.Checked = True
        checkBoxDic = CheckBox()
        checkBoxDic.Text = "Fill keynote values"
        checkBoxDic.Location = Point(250, 510)
        checkBoxDic.Width = 150
        checkBoxDic.Font = Font("OpenSans", 8)
        checkBoxDic.Anchor = AnchorStyles.Left | AnchorStyles.Top
        checkBoxDic.CheckedChanged += self.FillData
        self.Controls.Add(checkBoxDic)
        checkBoxDic.Checked = False


class DocumentManager:
    @staticmethod
    def GetDocuments(application, names):
        return [document for document in application.Documents if document.Title in names and document.IsWorkshared and document.IsLinked == False]

    @staticmethod
    def GetDocumentNames(application):
        return [document.Title for document in application.Documents if document.IsWorkshared and document.IsLinked == False]


class TransactionManager:
    @staticmethod
    def LoadKeyNotes(application, names, browsePath):
        documents = DocumentManager.GetDocuments(application, names)
        filePath = None
        results = KeyBasedTreeEntriesLoadResults()
        for document in documents:
            if browsePath is None:
                externalReference = KeynoteTable.GetKeynoteTable(document).GetExternalResourceReference(ExternalResourceTypes.BuiltInExternalResourceTypes.KeynoteTable)
                if "SymbolicLinks" not in externalReference.InSessionPath:
                    if filePath is None:
                        filePath = StandardDialogs.CreateOpenDialog()
                    externalReference = ExternalResourceReference.CreateLocalResource(document, ExternalResourceTypes.BuiltInExternalResourceTypes.KeynoteTable, FilePath(filePath), PathType.Absolute)
            else:
                externalReference = ExternalResourceReference.CreateLocalResource(document, ExternalResourceTypes.BuiltInExternalResourceTypes.KeynoteTable, FilePath(browsePath), PathType.Absolute)
            t = Transaction(document, "Load KeyNotes")
            t.Start()
            try:
                KeynoteTable.GetKeynoteTable(document).LoadFrom(externalReference, results)
                t.Commit()
            except:
                t.RollBack()
                raise

    @staticmethod
    def FillKeyNotes(application, names, data):
        documents = DocumentManager.GetDocuments(application, names)
        for document in documents:
            t = Transaction(document, "Fill Keynotes Values")
            t.Start()
            try:
                collectorMaterials = FilteredElementCollector(document).OfCategory(BuiltInCategory.OST_Materials).WhereElementIsNotElementType().ToElements()
                collectorElements = FilteredElementCollector(document).WhereElementIsElementType().ToElements()
                for keyNote in data:
                    if keyNote.Type.upper() == "ELEMENT KEYNOTE":
                        for element in collectorElements:
                            if Element.Name.__get__(element) == keyNote.Name:
                                value = str(keyNote.Value)
                                if len(value.split(".")[1]) <= 1:
                                    value += "0"
                                element.LookupParameter("Keynote").Set(value)
                    if keyNote.Type.upper() == "MATERIAL KEYNOTE":
                        for material in collectorMaterials:
                            if material.Name == keyNote.Name:
                                value = str(keyNote.Value)
                                if len(value.split(".")[1]) <= 1:
                                    value += "0"
                                material.LookupParameter("Keynote").Set(value)
                t.Commit()
            except:
                t.RollBack()
                raise


class TaskdialogResults:
    @staticmethod
    def ShowCancelTaskDialog():
        dialog = TaskDialog("KeyNotes manager")
        dialog.MainInstruction = "Update keynotes process"
        dialog.MainContent = "Update keynotes in multiple documents process cancelled."
        dialog.TitleAutoPrefix = False
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconWarning
        dialog.Show()

    @staticmethod
    def ShowCorrectTaskDialog():
        dialog = TaskDialog("KeyNotes manager")
        dialog.TitleAutoPrefix = False
        dialog.MainInstruction = "Update keynotes process finished"
        dialog.MainContent = "Update keynotes in multiple documents process finished correctly."
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconInformation
        dialog.Show()

    @staticmethod
    def LoadExecutionTaskDialog(path):
        dialog = TaskDialog("KeyNotes manager")
        dialog.MainInstruction = "Update keynotes process"
        dialog.MainContent = "Update keynotes in multiple documents. Load txt files and fill data in elements and materials."
        dialog.TitleAutoPrefix = False
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconWarning
        dialog.AddCommandLink(TaskDialogCommandLinkId.CommandLink1, "Load data from: {name}".format(name=Path(path).name))
        dialog.AddCommandLink(TaskDialogCommandLinkId.CommandLink2, "Select new dictionary location", "Dictionary file contains the keynotes values.")
        return dialog


class StandardDialogs:
    @staticmethod
    def CreateOpenDialog():
        with OpenFileDialog() as openDialog:
            desktop = Environment.GetFolderPath(Environment.SpecialFolder.Desktop)
            openDialog.InitialDirectory = desktop
            openDialog.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*"
            if openDialog.ShowDialog() == DialogResult.OK:
                return openDialog.FileName


class InputData:
    @staticmethod
    def _get_path(app):
        support_dir = Path(app.CurrentUserAddinsLocation) / "Balio" / "Support"
        support_dir.mkdir(parents=True, exist_ok=True)
        return support_dir / "KeyNotes.json"

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


class DataReader:
    @staticmethod
    def ReadExcelData(path):
        return None


class KeyNoteData:
    def __init__(self, type, name, value):
        self.type = type
        self.name = name
        self.value = value

    @property
    def Type(self):
        return self.type

    @property
    def Name(self):
        return self.name

    @property
    def Value(self):
        return self.value


print("Opening Keynotes Manager...")
KeynotesManagerForm(app).ShowDialog()
