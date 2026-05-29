import clr
from pathlib import Path

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from Autodesk.Revit.DB import *
from System.Windows.Forms import *
from System.Drawing import *
from Autodesk.Revit.UI import TaskDialog, TaskDialogCommonButtons, TaskDialogIcon

app = __revit__.Application
REVIT_ICON = Path.home() / "AppData" / "Roaming" / "Autodesk" / "ApplicationPlugins" / "Raen.Revit.Pynet.bundle" / "Revit.ico"  #type:ignore


class SyncForm(Form):
    def __init__(self, application):
        super().__init__()
        self.ConfigureForm(application)
        self.GenerateFormLabels()
        self.GenerateFormSelectionList(DocumentManager.GetSyncDocumentNames(application))
        self.GenerateTextBox()
        self.GenerateFormButtons()
        self.GenerateFormGroups()

    def Sync(self, sender, args):
        if self.Selection is not None:
            TransactionManager.SynchronizeDocuments(self.Application, self.Selection)
            TaskdialogResults.ShowCorrectTaskDialog()
            self.Close()

    def Cancel(self, sender, args):
        self.DialogResult = DialogResult.Cancel
        self.Status = "Cancel"
        TaskdialogResults.ShowCancelTaskDialog()
        self.Close()

    def ApplyFilter(self, sender, arg):
        listControl = [control for control in self.Controls if control.Name == "ModelsList"][0]
        listControl.Items.Clear()
        for m in [model for model in self.DocumentNames if sender.Text in model]:
            listControl.Items.Add(m)

    def Include(self, sender, args):
        self.Selection = sender.SelectedItems

    def ConfigureForm(self, application):
        self.Text = "Sync models"
        if REVIT_ICON.exists():
            self.Icon = Icon(str(REVIT_ICON))
        self.Application = application
        self.DocumentNames = None
        self.Selection = None
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
        label1.Text = "Select multiple cloud models to sync with the central using relinquish all configuration."
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
        groupBoxViews.Text = "Models to sync"
        groupBoxViews.Size = Size(550, 490)
        groupBoxViews.Location = Point(20, 60)
        groupBoxViews.Anchor = AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Bottom | AnchorStyles.Top
        groupBoxViews.Parent = self

    def GenerateFormSelectionList(self, documents):
        listBox = ListBox()
        listBox.Name = "ModelsList"
        listBox.Location = Point(50, 140)
        listBox.Anchor = AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Bottom | AnchorStyles.Top
        listBox.Width = 500
        listBox.Height = 400
        listBox.SelectionMode = SelectionMode.MultiExtended
        listBox.HorizontalScrollbar = True
        for doc_name in (documents or []):
            listBox.Items.Add(doc_name)
        self.DocumentNames = documents
        listBox.SelectedIndexChanged += self.Include
        self.Controls.Add(listBox)

    def GenerateFormButtons(self):
        buttonSync = Button()
        buttonSync.Text = "Sync"
        buttonSync.Width = 120
        buttonSync.Location = Point(450, 570)
        buttonSync.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
        buttonSync.Click += self.Sync
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
        textBox.Anchor = AnchorStyles.Right | AnchorStyles.Top
        textBox.TextChanged += self.ApplyFilter
        self.Controls.Add(textBox)


class SyncLockCallback(ICentralLockedCallback):
    def ShouldWaitForLockAvailability(self):
        return False


class DocumentManager:
    @staticmethod
    def GetSyncDocuments(application, names):
        return [document for document in application.Documents if document.Title in names and document.IsWorkshared and not document.IsLinked]

    @staticmethod
    def GetSyncDocumentNames(application):
        return [document.Title for document in application.Documents if document.IsWorkshared and not document.IsLinked]

    @staticmethod
    def SyncDocument(document):
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


class TransactionManager:
    @staticmethod
    def SynchronizeDocuments(application, names):
        documents = DocumentManager.GetSyncDocuments(application, names)
        for document in documents:
            if document.IsWorkshared and not document.IsLinked:
                DocumentManager.SyncDocument(document)
                print(f"Synchronized: {document.Title}")


class TaskdialogResults:
    @staticmethod
    def ShowCancelTaskDialog():
        dialog = TaskDialog("Synchronize models")
        dialog.MainInstruction = "Sync canceled"
        dialog.MainContent = "Sync multiple documents process cancelled."
        dialog.TitleAutoPrefix = False
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconWarning
        dialog.Show()

    @staticmethod
    def ShowCorrectTaskDialog():
        dialog = TaskDialog("Synchronize models")
        dialog.TitleAutoPrefix = False
        dialog.MainInstruction = "Sync finished"
        dialog.MainContent = "Sync multiple documents process finished correctly."
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconInformation
        dialog.Show()

    @staticmethod
    def ShowDisclaimerTaskDialog():
        dialog = TaskDialog("Synchronize models")
        dialog.TitleAutoPrefix = False
        dialog.MainInstruction = "Automation information"
        dialog.MainContent = "This tool synchronizes documents and relinquishes all borrowed elements, family worksets, and user-created worksets."
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconWarning
        dialog.Show()


TaskdialogResults.ShowDisclaimerTaskDialog()
print("Opening Sync Models dialog...")
SyncForm(app).ShowDialog()
