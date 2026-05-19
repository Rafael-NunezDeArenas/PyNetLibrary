#region References

# Load the Python Standard and DesignScript Libraries
import clr
import sys

sys.path.append("C:\\Program Files (x86)\\IronPython 2.7\\Lib")
import os

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
from System.Collections.Generic import List
from datetime import date

app = __revit__.Application #type:ignore

#endregion

# region Sync

# Sync Transfer Form
class SyncForm(Form):
    # Update Legends Button
    def Sync(self, sender, args):
        if self.Selection != None:
            TransactionManager.SynchronizeDocuments(self.Application, self.Selection)  
            TaskdialogResults.ShowCorrectTaskDialog()
            self.Close()
    # Generate Function for Cancel Button		
    def Cancel(self, sender, args):
        if sender.Click:
            self.DialogResult = DialogResult.Cancel
            self.Status = "Cancel"
            TaskdialogResults.ShowCancelTaskDialog()
            self.Close()    
    # Filter Button
    def ApplyFilter(self, sender, arg):
        listControl = [control for control in self.Controls if control.Name == "ModelsList"][0]
        listControl.DataSource = [model for model in self.DocumentNames if sender.Text in model] 
    # Generate Function to include selected elements in Group Box
    def Include(self, sender, args):
        self.Selection = sender.SelectedItems
    # Windows Form Configuration
    def ConfigureForm(self, application):
    # Include Icon
    
    #Generate Tittle Value
        self.Text = "Sync models"
    #Form Variables
        self.Application = application
        self.DocumentNames = None
        self.Selection = None
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
        labelGeneralDescription = Label(Text = "Select multiple cloud models to sync with the central using relinquish all configuration.")
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
        groupBoxViews.Text = "Models to sync"
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
        listBox.Anchor = AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Bottom | AnchorStyles.Top
        listBox.Width = 500
        listBox.Height = 400
        listBox.SelectionMode = SelectionMode.MultiExtended
        listBox.HorizontalScrollbar = True
        listBox.DataSource = documents
        self.DocumentNames = documents
        listBox.SelectedIndexChanged += self.Include
        self.Controls.Add(listBox)
    # Windows Form Buttons
    def GenerateFormButtons(self):
    # Generate Export Button
        buttonSync = Button()
        buttonSync.Text = "Sync"
        buttonSync.Width = 120
        buttonSync.Location = Point(450, 570)
        buttonSync.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
        buttonSync.Click += self.Sync
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
        textBox.Anchor = AnchorStyles.Right | AnchorStyles.Top
        textBox.TextChanged += self.ApplyFilter
        self.Controls.Add(textBox)
    # Constructor Class
    def __init__(self, application):
        self.ConfigureForm(application)
        self.GenerateFormLabels()
        self.GenerateFormSelectionList(DocumentManager.GetSyncDocumentNames(application))
        self.GenerateTextBox()        
        self.GenerateFormButtons()
        self.GenerateFormGroups()

class SyncLockCallback(ICentralLockedCallback):
    def ShouldWaitForLockAvailability(self):
        return False

class DocumentManager:
    @staticmethod
    def GetSyncDocuments(application, names):
        return [document for document in application.Documents if document.Title in names and document.IsWorkshared and document.IsLinked == False]
    @staticmethod
    def GetSyncDocumentNames(application):
        return [document.Title for document in application.Documents if document.IsWorkshared and document.IsLinked == False]
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
            if document.IsWorkshared and document.IsLinked == False:
                DocumentManager.SyncDocument(document)

# Generate TaskDialog Options Class
class TaskdialogResults:
# Define Show Cancel TaskDialog Method
    @staticmethod
    def ShowCancelTaskDialog():
        dialog = TaskDialog("Synchronize models")
        dialog.MainInstruction = "Sync canceled"
        dialog.MainContent = "Sync multiple documents process cancelled."
        dialog.TitleAutoPrefix = False
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconWarning
        dialog.Show()
# Define Show Process Finish TaskDialog Method
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
        dialog.MainContent = "This tool Synchronize Documents relinquish all borrowed elements, family worksets and User-created worksets."
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconWarning
        dialog.Show()

TaskdialogResults.ShowDisclaimerTaskDialog()

SyncForm(app).ShowDialog()

#endregion