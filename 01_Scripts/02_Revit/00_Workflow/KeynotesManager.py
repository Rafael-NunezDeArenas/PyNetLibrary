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

from System.Windows.Forms import*
from System.Drawing import*

app = __revit__.Application #type:ignore

#endregion

# region Sync

# Sync Transfer Form
class KeynotesManagerForm(Form):
    # Update Legends Button
    def LoadData(self, sender, args):
        if self.Selection != None:
            if self.LoadTxtFile == True:
                TransactionManager.LoadKeyNotes(self.Application, self.Selection, self.NotesPath)
            if self.FillParameterData == False:
                TaskdialogResults.ShowCorrectTaskDialog()
            if self.FillParameterData == True:
                # Define Diferent Results
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
                elif dialogResult == dialogResult.Cancel:
                    TaskdialogResults.ShowCancelTaskDialog()
                else:
                    TaskdialogResults.ShowCancelTaskDialog()

            self.Close()
    # Generate Function for Cancel Button		
    def Cancel(self, sender, args):
        if sender.Click:
            self.DialogResult = DialogResult.Cancel
            self.Status = "Cancel"
            TaskdialogResults.ShowCancelTaskDialog()
            self.Close()    
    # Browse Notes Path
    def BrowserNotes(self, sender, args):
        if sender.Click:
            self.NotesPath = StandardDialogs.CreateOpenDialog()
    # Browse Dictionary
    def BrowserDiccionary(self, sender, args):
        if sender.Click:
            with OpenFileDialog() as openDialog:
                self.BrowseExcel()
    # Browse Method implementation
    def BrowseExcel(self):
        with OpenFileDialog() as openDialog:
                openDialog.InitialDirectory = os.path.join(os.path.expanduser('~'), 'Desktop')
                openDialog.Filter = "Txt files (*.xlsx)|*.xlsx|All files (*.*)|*.*"
                if openDialog.ShowDialog() == DialogResult.OK:
                    self.DataPath = openDialog.FileName
                    self.Data  = DataReader.ReadExcelData(openDialog.FileName)
                    self.DictionaryPath = openDialog.FileName
                    InputData.CreateJson({"path": openDialog.FileName})
    # Filter Button
    def ApplyFilter(self, sender, arg):
        listControl = [control for control in self.Controls if control.Name == "ModelsList"][0]
        listControl.DataSource = [model for model in self.DocumentNames if sender.Text in model] 
    # Able load Txt File
    def LoadTxt(self, sender, args):
        if sender.Checked:
            self.LoadTxtFile = True
        else:
            self.LoadTxtFile = False
    # Able Fill parameters Data
    def FillData(self, sender, args):
        if sender.Checked:
            self.FillParameterData = True
        else:
            self.FillParameterData = False 
    # Generate Function to include selected elements in Group Box
    def Include(self, sender, args):
        self.Selection = sender.SelectedItems
    # Windows Form Configuration
    def ConfigureForm(self, application):
    # Include Icon

    #Generate Tittle Value
        self.Text = "Keynotes manager"
    #Form Variables
        self.Application = application
        self.DocumentNames = None
        self.Selection = None
        self.NotesPath = None
        self.LoadTxtFile = True
        self.FillParameterData = False
        self.Data = None
        self.DictionaryPath = None
    #Window dimension
        self.WindowState = FormWindowState.Normal
    #Generate Window in Center
        self.CenterToScreen()
    #Window in front
        self.BringToFront()
        self.Topmost = True
    #Scale window with resolution
        self.screenSize = Screen.GetWorkingArea(self)
        self.Width = 600
        self.Height = 650
        self.MinimumSize = Size(600, 650)
    #Block Dimension of window
        self.FormBorderStyle = FormBorderStyle.Sizable
        self.MaximizeBox = True		
        screenSize = Screen.GetWorkingArea(self)
    # Windows Form Labels
    def GenerateFormLabels(self):
        # Description General
        labelGeneralDescription = Label(Text = "Select multiple models to load or reload the Keynotes file and fill the KeyNotes values using a dictionary file.")
        labelGeneralDescription.Parent = self
        labelGeneralDescription.Width = 400
        labelGeneralDescription.Height = 50
        labelGeneralDescription.Location = Point(20, 10)
        labelGeneralDescription.Anchor = AnchorStyles.Left | AnchorStyles.Top
        # Filter Label
        labelGeneralDescription = Label(Text = "Model name filter: ")
        labelGeneralDescription.Parent = self
        labelGeneralDescription.Width = 120
        labelGeneralDescription.Height = 25
        labelGeneralDescription.Location = Point(200, 93)
        labelGeneralDescription.Anchor = AnchorStyles.Right | AnchorStyles.Top
    # Windows Form Groups
    def GenerateFormGroups(self):
        # Generate Group Views	
        groupBoxViews = GroupBox()
        groupBoxViews.Text = "Documents to load data"
        groupBoxViews.Size = Size(550, 490)
        groupBoxViews.Location = Point(20, 60)
        groupBoxViews.Anchor = AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Bottom | AnchorStyles.Top
        groupBoxViews.Parent = self
    # Windows Form Selection List
    def GenerateFormSelectionList(self, documents):
        # Selection List
        listBox = ListBox()
        listBox.Name = "ModelsList"
        listBox.Location = Point(50, 140)
        listBox.Width = 500
        listBox.Height = 370
        listBox.SelectionMode = SelectionMode.MultiExtended
        listBox.HorizontalScrollbar = True
        listBox.DataSource = documents
        self.DocumentNames = documents
        listBox.Anchor = AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Bottom | AnchorStyles.Top
        listBox.SelectedIndexChanged += self.Include
        self.Controls.Add(listBox)
    # Windows Form Buttons
    def GenerateFormButtons(self):
    # Generate Browser Button
        buttonBrowserTxt = Button()
        buttonBrowserTxt.Width = 120
        buttonBrowserTxt.Text = "Browse txt"
        buttonBrowserTxt.Location = Point(20, 570)
        buttonBrowserTxt.Anchor = AnchorStyles.Left | AnchorStyles.Bottom
        buttonBrowserTxt.Click += self.BrowserNotes
        self.Controls.Add(buttonBrowserTxt)
    # Generate Browser Button
        buttonBrowserDiccionary = Button()
        buttonBrowserDiccionary.Width = 130
        buttonBrowserDiccionary.Text = "Browse diccionary"
        buttonBrowserDiccionary.Location = Point(150, 570)
        buttonBrowserDiccionary.Anchor = AnchorStyles.Left | AnchorStyles.Bottom
        buttonBrowserDiccionary.Click += self.BrowserDiccionary
        self.Controls.Add(buttonBrowserDiccionary)
    #Generate Load Button
        buttonSync = Button()
        buttonSync.Text = "Load"
        buttonSync.Width = 120
        buttonSync.Location = Point(450, 570)
        buttonSync.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
        buttonSync.Click += self.LoadData
        self.Controls.Add(buttonSync)
    # Generate Cancel Button
        buttonCancel = Button()
        buttonCancel.Width = 120
        buttonCancel.Text = "Cancel"
        buttonCancel.Location = Point(320, 570)
        buttonCancel.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
        buttonCancel.Click += self.Cancel
        self.Controls.Add(buttonCancel)
    # Windows Form Text Box
    def GenerateTextBox(self):
        textBox = TextBox()
        textBox.Location = Point(325, 90)
        textBox.Width = 225
        textBox.Anchor = AnchorStyles.Top | AnchorStyles.Right
        textBox.TextChanged += self.ApplyFilter
        self.Controls.Add(textBox)
    # Windows Form Check Boxes
    def GenerateFormCheckBoxes(self):
        # Generate CheckBox	Load Txt File
        checkBoxLoadTxt = CheckBox()
        checkBoxLoadTxt.Text = "Load Data from Txt"
        checkBoxLoadTxt.Location = Point(50, 510)
        checkBoxLoadTxt.Width = 150
        checkBoxLoadTxt.Font= Font("OpenSans", 8)
        checkBoxLoadTxt.CheckedChanged += self.LoadTxt
        checkBoxLoadTxt.Anchor = AnchorStyles.Left | AnchorStyles.Top
        self.Controls.Add(checkBoxLoadTxt)
        checkBoxLoadTxt.Checked = True
        # Generate CheckBox	Load Dictionary
        checkBoxDic = CheckBox()
        checkBoxDic.Text = "Fill keynote values"
        checkBoxDic.Location = Point(250, 510)
        checkBoxDic.Width = 150
        checkBoxDic.Font= Font("OpenSans", 8)
        checkBoxDic.Anchor = AnchorStyles.Left | AnchorStyles.Top
        checkBoxDic.CheckedChanged += self.FillData
        self.Controls.Add(checkBoxDic)
        checkBoxDic.Checked = False
    # Constructor Class
    def __init__(self, application):
        self.ConfigureForm(application)
        self.GenerateFormLabels()
        self.GenerateFormSelectionList(DocumentManager.GetDocumentNames(application))
        data = InputData.ReadJson()
        if data != None and os.path.isfile(data["path"]):
            self.Data = DataReader.ReadExcelData(data["path"])
            self.DictionaryPath = data["path"]
        self.GenerateFormCheckBoxes()
        self.GenerateTextBox()      
        self.GenerateFormButtons()
        self.GenerateFormGroups()

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
            if browsePath == None:          
                externalReference = KeynoteTable.GetKeynoteTable(document).GetExternalResourceReference(ExternalResourceTypes.BuiltInExternalResourceTypes.KeynoteTable)
                if "SymbolicLinks" not in externalReference.InSessionPath:
                    if filePath == None:
                        filePath = StandardDialogs.CreateOpenDialog()
                    externalReference = ExternalResourceReference.CreateLocalResource(document, ExternalResourceTypes.BuiltInExternalResourceTypes.KeynoteTable, FilePath(filePath), PathType.Absolute)
            else:
                externalReference = ExternalResourceReference.CreateLocalResource(document, ExternalResourceTypes.BuiltInExternalResourceTypes.KeynoteTable, FilePath(browsePath), PathType.Absolute)

            with Transaction(document) as tx:
                tx.Start("Load KeyNotes")

                KeynoteTable.GetKeynoteTable(document).LoadFrom(externalReference, results)

                tx.Commit()
    @staticmethod
    def FillKeyNotes(application, names, data):
        documents = DocumentManager.GetDocuments(application, names)
        for document in documents:
            with Transaction(document) as tx:
                tx.Start("Fill Keynotes Values")
                collectorMaterials = FilteredElementCollector(document).OfCategory(BuiltInCategory.OST_Materials).WhereElementIsNotElementType().ToElements()
                collectorElements = FilteredElementCollector(document).WhereElementIsElementType().ToElements()
                for keyNote in data:
                    if keyNote.Type.upper() == "ELEMENT KEYNOTE":
                        for element in collectorElements:
                            if Element.Name.__get__(element) == keyNote.Name:
                                if len(str(keyNote.Value).split(".")[1]) > 1 :
                                    element.LookupParameter("Keynote").Set(str(keyNote.Value))
                                else:
                                    element.LookupParameter("Keynote").Set(str(keyNote.Value)+"0")
                    if keyNote.Type.upper() == "MATERIAL KEYNOTE":
                        for material in collectorMaterials:
                            if material.Name == keyNote.Name:
                                if len(str(keyNote.Value).split(".")[1]) > 1 :
                                    material.LookupParameter("Keynote").Set(str(keyNote.Value))
                                else:
                                    material.LookupParameter("Keynote").Set(str(keyNote.Value)+"0")
                tx.Commit()
        
# Generate TaskDialog Options Class
class TaskdialogResults:
# Define Show Cancel TaskDialog Method
    @staticmethod
    def ShowCancelTaskDialog():
        dialog = TaskDialog("KeyNotes manager")
        dialog.MainInstruction = "Update keynotes process"
        dialog.MainContent = "Update keynotes in multiple documents process cancelled."
        dialog.TitleAutoPrefix = False
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconWarning
        dialog.Show()
# Define Show Process Finish TaskDialog Method
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
        # Include Command Links
        dialog.AddCommandLink(TaskDialogCommandLinkId.CommandLink1, "Load data from: {name}".format(name = os.path.basename(path)))
        dialog.AddCommandLink(TaskDialogCommandLinkId.CommandLink2, "Select new dictionary location", "Dictionary file contains de keynotes value of the different elements or materials.")
        return dialog

class StandardDialogs:
    @staticmethod
    def CreateOpenDialog():
        with OpenFileDialog() as openDialog:
            openDialog.InitialDirectory = os.path.join(os.path.expanduser('~'), 'Desktop')
            openDialog.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*"
            if openDialog.ShowDialog() == DialogResult.OK:
                return openDialog.FileName

class InputData():
    @staticmethod
    def CreateJson(dictionary):
        if not os.path.exists(os.path.join(app.CurrentUserAddinsLocation, "Balio\\Support")):
            os.makedirs(os.path.join(app.CurrentUserAddinsLocation, "Balio\\Support"))
        path = os.path.join(app.CurrentUserAddinsLocation, "Balio\\Support\\KeyNotes.json")
        with open(path, "w") as file:
            json.dump(dictionary, file)
    @staticmethod
    def ReadJson():
        try:
            path = os.path.join(app.CurrentUserAddinsLocation, "Balio\\Support\\KeyNotes.json")
            with open(path, "r") as file:
                return json.load(file)
        except:
            return None

class DataReader():
    @staticmethod
    def ReadExcelData(path):
        return None
class KeyNoteData():
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

KeynotesManagerForm(app).ShowDialog()

#endregion