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
uidoc = __revit__.ActiveUIDocument  #type:ignore
doc = uidoc.Document


class WindowTransfer(Form):
    def __init__(self, application):
        super().__init__()
        self.ConfigureForm(application)
        self.GenerateTableLayout()
        self.GenerateFormGroups()
        self.GenerateFormSelectionList(ModelManager.GetModels(application))
        self.GenerateFormLabels()
        self.GenerateComboBoxes()
        self.GenerateButtons()

    def Transfer(self, sender, args):
        if self.BaseDocument is not None and self.Category is not None and len(self.GetTransferDocuments()) > 0 and len(self.GetSelectedParameters()) > 0:
            if self.Category.__class__ != ProjectInfo:
                DataCollector.TransferData(self.BaseDocument, self.GetTransferDocuments(), self.Category, self.GetSelectedParameters())
            else:
                DataCollector.TransferProjectInformation(self.BaseDocument, self.GetTransferDocuments(), self.GetSelectedParameters())
            TaskdialogResults.ShowCorrectTaskDialog()
            self.Close()

    def Cancel(self, sender, args):
        TaskdialogResults.ShowCancelTaskDialog()
        self.Close()

    def GetBaseDocument(self, sender, args):
        self.BaseDocument = ModelManager.GetModel(self.Application, sender.SelectedItem)
        categoriesComboBox = [control for control in self.GroupBoxDocuments.Controls if control.Name == "categoryComboBox"][0]
        categoriesComboBox.Items.Clear()
        [categoriesComboBox.Items.Add(category) for category in ModelManager.GetCategories(ModelManager.GetModel(self.Application, sender.SelectedItem))]
        listControl = [control for control in self.GroupBoxDocuments.Controls if control.Name == "ModelsList"][0]
        listControl.Items.Clear()
        [listControl.Items.Add(document, CheckState.Unchecked) for document in self.BaseDocuments if sender.SelectedItem != document]

    def GetTransferDocuments(self):
        result = []
        listControl = [control for control in self.GroupBoxDocuments.Controls if control.Name == "ModelsList"][0]
        for count in range(listControl.Items.Count):
            if listControl.GetItemCheckState(count) == CheckState.Checked:
                result.append(ModelManager.GetModel(self.Application, listControl.Items[count]))
        return result

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
            if not parameter.IsReadOnly and parameter.StorageType == StorageType.String:
                values.append(parameter.Definition.Name)
        values.sort()
        [listControl.Items.Add(value, CheckState.Unchecked) for value in values]

    def ParametersFilter(self, sender, args):
        listControl = [control for control in self.GroupBoxParameters.Controls if control.Name == "ParameterList"][0]
        listControl.Items.Clear()
        values = []
        if sender.SelectedItem == "All Parameters":
            for parameter in self.Parameters:
                if not parameter.IsReadOnly and parameter.StorageType == StorageType.String:
                    values.append(parameter.Definition.Name)
        elif sender.SelectedItem == "BuiltIn Parameters":
            for parameter in self.Parameters:
                if not parameter.IsReadOnly and parameter.StorageType == StorageType.String and parameter.Definition.BuiltInParameter != BuiltInParameter.INVALID:
                    values.append(parameter.Definition.Name)
        elif sender.SelectedItem == "Shared Parameters":
            for parameter in self.Parameters:
                if not parameter.IsReadOnly and parameter.StorageType == StorageType.String and parameter.Definition.BuiltInParameter == BuiltInParameter.INVALID:
                    values.append(parameter.Definition.Name)
        values.sort()
        [listControl.Items.Add(value, CheckState.Unchecked) for value in values]

    def CheckAll(self, sender, args):
        if [control for control in self.GroupBoxDocuments.Controls if control.Name == sender.Name.replace("Check", "") + "List"]:
            listControl = [control for control in self.GroupBoxDocuments.Controls if control.Name == sender.Name.replace("Check", "") + "List"][0]
        else:
            listControl = [control for control in self.GroupBoxParameters.Controls if control.Name == sender.Name.replace("Check", "") + "List"][0]
        for count in range(listControl.Items.Count):
            if listControl.GetItemCheckState(count) == CheckState.Unchecked:
                listControl.SetItemCheckState(count, CheckState.Checked)

    def UnCheckAll(self, sender, args):
        if [control for control in self.GroupBoxDocuments.Controls if control.Name == sender.Name.replace("UnCheck", "") + "List"]:
            listControl = [control for control in self.GroupBoxDocuments.Controls if control.Name == sender.Name.replace("UnCheck", "") + "List"][0]
        else:
            listControl = [control for control in self.GroupBoxParameters.Controls if control.Name == sender.Name.replace("UnCheck", "") + "List"][0]
        for count in range(listControl.Items.Count):
            if listControl.GetItemCheckState(count) == CheckState.Checked:
                listControl.SetItemCheckState(count, CheckState.Unchecked)

    def ConfigureForm(self, application):
        self.Text = "Transfer data"
        if REVIT_ICON.exists():
            self.Icon = Icon(str(REVIT_ICON))
        self.Application = application
        self.BaseDocuments = ModelManager.GetModels(application)
        self.TransferDocuments = ModelManager.GetModels(application)
        self.Categories = ModelManager.GetCategories([document for document in application.Documents if not document.IsLinked and document.IsWorkshared][0])
        self.BaseDocument = None
        self.Category = None
        self.Parameters = None
        self.WindowState = FormWindowState.Normal
        self.CenterToScreen()
        self.BringToFront()
        self.Topmost = True
        self.screenSize = Screen.GetWorkingArea(self)
        self.MaximizeBox = True
        self.Width = 880
        self.Height = 690
        self.MinimumSize = Size(880, 690)
        self.FormBorderStyle = FormBorderStyle.Sizable

    def GetSelectedParameters(self):
        result = []
        listControl = [control for control in self.GroupBoxParameters.Controls if control.Name == "ParameterList"][0]
        for count in range(listControl.Items.Count):
            if listControl.GetItemCheckState(count) == CheckState.Checked:
                result.append(listControl.Items[count])
        return result

    def GenerateFormLabels(self):
        label1 = Label()
        label1.Text = "Select the category to transfer the parameters data of all the common types between models."
        label1.Parent = self
        label1.Width = 800
        label1.Height = 40
        label1.Padding = Padding(10, 0, 0, 0)
        label1.Anchor = AnchorStyles.Left | AnchorStyles.Top
        self.TableLayout.Controls.Add(label1, 0, 0)
        for text, location, parent in [
            ("Select source model:", Point(15, 40), self.GroupBoxDocuments),
            ("Select category to collect types:", Point(15, 100), self.GroupBoxDocuments),
            ("Select destination model:", Point(15, 160), self.GroupBoxDocuments),
            ("Select parameters to transfer data:", Point(15, 40), self.GroupBoxParameters),
        ]:
            label = Label()
            label.Text = text
            label.Parent = self
            label.Width = 300
            label.Height = 20
            label.Location = location
            label.Anchor = AnchorStyles.Left | AnchorStyles.Top
            parent.Controls.Add(label)

    def GenerateComboBoxes(self):
        baseBox = ComboBox()
        baseBox.Name = "BaseDocumentComboBox"
        baseBox.Location = Point(15, 65)
        baseBox.Width = 370
        baseBox.Anchor = AnchorStyles.Left | AnchorStyles.Top | AnchorStyles.Right | AnchorStyles.Bottom
        if self.BaseDocuments:
            [baseBox.Items.Add(document) for document in self.BaseDocuments]
            self.BaseDocument = ModelManager.GetModel(self.Application, self.BaseDocuments[0])
        baseBox.DropDownStyle = ComboBoxStyle.DropDownList
        baseBox.SelectedIndexChanged += self.GetBaseDocument
        self.GroupBoxDocuments.Controls.Add(baseBox)
        categoryBox = ComboBox()
        categoryBox.Name = "categoryComboBox"
        categoryBox.Location = Point(15, 125)
        categoryBox.Width = 370
        categoryBox.Anchor = AnchorStyles.Left | AnchorStyles.Top | AnchorStyles.Right | AnchorStyles.Bottom
        [categoryBox.Items.Add(category) for category in self.Categories]
        if self.Categories:
            self.Category = ModelManager.GetCategory(self.Application, self.Categories[0])
        categoryBox.DropDownStyle = ComboBoxStyle.DropDownList
        categoryBox.SelectedIndexChanged += self.GetCategory
        self.GroupBoxDocuments.Controls.Add(categoryBox)
        parameterBox = ComboBox()
        parameterBox.Location = Point(15, 65)
        parameterBox.Width = 370
        parameterBox.Anchor = AnchorStyles.Left | AnchorStyles.Top | AnchorStyles.Right | AnchorStyles.Bottom
        for opt in ["All Parameters", "BuiltIn Parameters", "Shared Parameters"]:
            parameterBox.Items.Add(opt)
        parameterBox.DropDownStyle = ComboBoxStyle.DropDownList
        parameterBox.SelectedIndexChanged += self.ParametersFilter
        self.GroupBoxParameters.Controls.Add(parameterBox)

    def GenerateFormSelectionList(self, documents):
        checkedListBox = CheckedListBox()
        checkedListBox.Name = "ModelsList"
        checkedListBox.Location = Point(15, 180)
        checkedListBox.Width = 370
        checkedListBox.Height = 300
        checkedListBox.HorizontalScrollbar = True
        checkedListBox.CheckOnClick = True
        [checkedListBox.Items.Add(document, CheckState.Unchecked) for document in documents if self.BaseDocuments and self.BaseDocuments[0] != document]
        checkedListBox.Anchor = AnchorStyles.Right | AnchorStyles.Left | AnchorStyles.Bottom | AnchorStyles.Top
        self.GroupBoxDocuments.Controls.Add(checkedListBox)
        checkedListParametersBox = CheckedListBox()
        checkedListParametersBox.Name = "ParameterList"
        checkedListParametersBox.Location = Point(15, 100)
        checkedListParametersBox.Width = 370
        checkedListParametersBox.Height = 380
        checkedListParametersBox.HorizontalScrollbar = True
        checkedListParametersBox.CheckOnClick = True
        checkedListParametersBox.Anchor = AnchorStyles.Right | AnchorStyles.Left | AnchorStyles.Bottom | AnchorStyles.Top
        self.GroupBoxParameters.Controls.Add(checkedListParametersBox)

    def GenerateButtons(self):
        for text, name, location, parent, handler in [
            ("Check All", "ModelsCheck", Point(15, 485), self.GroupBoxDocuments, self.CheckAll),
            ("Check None", "ModelsUnCheck", Point(150, 485), self.GroupBoxDocuments, self.UnCheckAll),
            ("Check All", "ParameterCheck", Point(15, 485), self.GroupBoxParameters, self.CheckAll),
            ("Check None", "ParameterUnCheck", Point(150, 485), self.GroupBoxParameters, self.UnCheckAll),
        ]:
            btn = Button()
            btn.Text = text
            btn.Name = name
            btn.Width = 120
            btn.Location = location
            btn.Anchor = AnchorStyles.Left | AnchorStyles.Bottom
            btn.Click += handler
            parent.Controls.Add(btn)
        bNext = Button()
        bNext.Text = "Transfer"
        bNext.Width = 120
        bNext.Location = Point(130, 0)
        bNext.Click += self.Transfer
        buttonCancel = Button()
        buttonCancel.Text = "Cancel"
        buttonCancel.Width = 120
        buttonCancel.Location = Point(0, 0)
        buttonCancel.Click += self.Cancel
        panel = Panel()
        panel.Width = 250
        panel.Margin = Padding(10, 10, 10, 10)
        panel.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
        panel.Controls.Add(bNext)
        panel.Controls.Add(buttonCancel)
        self.TableLayout.Controls.Add(panel, 2, 2)

    def GenerateFormGroups(self):
        groupBoxDocuments = GroupBox()
        groupBoxDocuments.Text = "Documents configuration"
        groupBoxDocuments.Size = Size(400, 540)
        groupBoxDocuments.Location = Point(20, 50)
        groupBoxDocuments.Anchor = AnchorStyles.Right | AnchorStyles.Left | AnchorStyles.Bottom | AnchorStyles.Top
        groupBoxDocuments.Margin = Padding(10, 10, 10, 0)
        self.TableLayout.Controls.Add(groupBoxDocuments, 0, 1)
        self.GroupBoxDocuments = groupBoxDocuments
        groupBoxParameters = GroupBox()
        groupBoxParameters.Text = "Parameters configuration"
        groupBoxParameters.Size = Size(400, 540)
        groupBoxParameters.Location = Point(20, 50)
        groupBoxParameters.Anchor = AnchorStyles.Right | AnchorStyles.Left | AnchorStyles.Bottom | AnchorStyles.Top
        groupBoxParameters.Margin = Padding(10, 10, 10, 0)
        self.TableLayout.Controls.Add(groupBoxParameters, 1, 1)
        self.GroupBoxParameters = groupBoxParameters

    def GenerateTableLayout(self):
        tableLayout = TableLayoutPanel()
        tableLayout.Anchor = AnchorStyles.Right | AnchorStyles.Left | AnchorStyles.Bottom | AnchorStyles.Top
        tableLayout.ColumnCount = 2
        tableLayout.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 50))
        tableLayout.ColumnStyles.Add(ColumnStyle(SizeType.Percent, 50))
        tableLayout.Location = Point(0, 0)
        tableLayout.RowCount = 3
        tableLayout.RowStyles.Add(RowStyle(SizeType.Absolute, 50))
        tableLayout.RowStyles.Add(RowStyle(SizeType.Percent, 90))
        tableLayout.RowStyles.Add(RowStyle(SizeType.Absolute, 50))
        tableLayout.Size = Size(870, 690)
        tableLayout.Padding = Padding(10, 10, 20, 50)
        tableLayout.TabIndex = 0
        self.Controls.Add(tableLayout)
        self.TableLayout = tableLayout


class ModelManager:
    @staticmethod
    def GetModels(application):
        return [document.Title + ".rvt" for document in application.Documents if not document.IsLinked and document.IsWorkshared]

    @staticmethod
    def GetModel(application, name):
        return [document for document in application.Documents if document.IsWorkshared and not document.IsLinked and document.Title in name][0]

    @staticmethod
    def GetCategories(document):
        categories = [category.Name for category in document.Settings.Categories if category.CategoryType == CategoryType.Model and len(FilteredElementCollector(document).OfCategoryId(category.Id).WhereElementIsElementType().ToElements()) > 0 and "DWG" not in category.Name.upper()]
        categories.append("Project Information")
        categories.sort()
        return categories

    @staticmethod
    def GetCategory(application, name):
        document = [document for document in application.Documents if not document.IsLinked][0]
        return [category for category in document.Settings.Categories if category.Name == name][0]

    @staticmethod
    def GetProjectInformation(document):
        return document.ProjectInformation


class DataCollector:
    @staticmethod
    def GetTypes(document, category):
        return FilteredElementCollector(document).OfCategoryId(category.Id).WhereElementIsElementType().ToElements()

    @staticmethod
    def TransferData(baseDocument, transferDocuments, category, parameterNames):
        collectorBase = DataCollector.GetTypes(baseDocument, category)
        for transferDocument in transferDocuments:
            collectorTransfer = DataCollector.GetTypes(transferDocument, category)
            t = Transaction(transferDocument, "Set parameters")
            t.Start()
            try:
                for transferElement in collectorTransfer:
                    for baseElement in collectorBase:
                        if Element.Name.__get__(baseElement) == Element.Name.__get__(transferElement):
                            for parameterName in parameterNames:
                                if len(baseElement.GetParameters(parameterName)) == 1 and len(transferElement.GetParameters(parameterName)) == 1:
                                    baseParameter = baseElement.LookupParameter(parameterName)
                                    transferParameter = transferElement.LookupParameter(parameterName)
                                else:
                                    baseParamList = [p for p in baseElement.GetParameters(parameterName) if p.StorageType == StorageType.String]
                                    transferParamList = [p for p in transferElement.GetParameters(parameterName) if p.StorageType == StorageType.String]
                                    baseParameter = baseParamList[0] if baseParamList else None
                                    transferParameter = transferParamList[0] if transferParamList else None
                                if baseParameter is not None and transferParameter is not None:
                                    if baseParameter.AsString() != transferParameter.AsString():
                                        try:
                                            transferParameter.Set(baseParameter.AsString())
                                        except:
                                            pass
                t.Commit()
            except:
                t.RollBack()
                raise
            print(f"Data transferred to: {transferDocument.Title}")

    @staticmethod
    def TransferProjectInformation(baseDocument, transferDocuments, parameterNames):
        infoBase = ModelManager.GetProjectInformation(baseDocument)
        for transferDocument in transferDocuments:
            infoTransfer = ModelManager.GetProjectInformation(transferDocument)
            t = Transaction(transferDocument, "Set Project Information")
            t.Start()
            try:
                for baseParameter in infoBase.GetOrderedParameters():
                    for transferParameter in infoTransfer.GetOrderedParameters():
                        if baseParameter.Definition.Name == transferParameter.Definition.Name and baseParameter.Definition.Name in parameterNames:
                            try:
                                transferParameter.Set(baseParameter.AsString())
                            except:
                                pass
                t.Commit()
            except:
                t.RollBack()
                raise
            print(f"Project info transferred to: {transferDocument.Title}")


class TaskdialogResults:
    @staticmethod
    def ShowCancelTaskDialog():
        dialog = TaskDialog("Transfer data")
        dialog.MainInstruction = "Transfer process cancelled"
        dialog.MainContent = "Transfer data between models cancelled."
        dialog.TitleAutoPrefix = False
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconWarning
        dialog.Show()

    @staticmethod
    def ShowCorrectTaskDialog():
        dialog = TaskDialog("Transfer data")
        dialog.TitleAutoPrefix = False
        dialog.MainInstruction = "Transfer process finished"
        dialog.MainContent = "Transfer data between models process finished correctly."
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconInformation
        dialog.Show()


print("Opening Transfer Data dialog...")
WindowTransfer(app).ShowDialog()
