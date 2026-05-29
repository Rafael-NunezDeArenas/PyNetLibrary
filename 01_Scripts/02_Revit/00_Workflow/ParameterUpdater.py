import clr
from pathlib import Path

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from Autodesk.Revit.DB import *
from System.Windows.Forms import *
from System.Drawing import *
from Autodesk.Revit.UI import TaskDialog, TaskDialogCommonButtons, TaskDialogIcon, TaskDialogResult

uidoc = __revit__.ActiveUIDocument  #type:ignore
doc = uidoc.Document


class WindowParameterUpdater(Form):
    def __init__(self):
        super().__init__()
        self.ConfigureForm()
        self.GenerateFormLabels()
        self.GenerateComboBoxes()
        self.GenerateTextBox()
        self.GenerateButtons()

    def ShowDialogProcess(self, correctSet=True):
        processDialog = TaskDialog("Parameter Value Updater")
        processDialog.TitleAutoPrefix = False
        if correctSet:
            processDialog.MainInstruction = "Parameter Value Updated"
            processDialog.MainIcon = TaskDialogIcon.TaskDialogIconInformation
        else:
            processDialog.MainInstruction = "Parameter Value Not Updated"
            processDialog.MainIcon = TaskDialogIcon.TaskDialogIconError
        processDialog.Show()

    def ShowDialogExecute(self):
        mainDialog = TaskDialog("Parameter Value Updater")
        mainDialog.TitleAutoPrefix = False
        mainDialog.MainInstruction = "Update Parameter Value"
        mainDialog.MainContent = "Parameter Value Updater is going to update the Parameter Value of the Selected Type. Are you sure?"
        mainDialog.CommonButtons = TaskDialogCommonButtons.Cancel | TaskDialogCommonButtons.Ok
        mainDialog.DefaultButton = TaskDialogResult.Ok
        mainDialogResult = mainDialog.Show()
        if mainDialogResult == TaskDialogResult.Ok:
            self.SetParameterValue()

    def GetCategorySelected(self, sender, args):
        self.CategoryName = sender.SelectedItem
        for category in doc.Settings.Categories:
            if category.Name == self.CategoryName:
                filterCat = ElementCategoryFilter(category.Id)
                self.collector = FilteredElementCollector(doc).WherePasses(filterCat).WhereElementIsElementType().ToElements()
                self.TypeNames = [Element.Name.__get__(element) for element in self.collector]
                break
        self.typeBox.Items.Clear()
        for t in self.GetTypes():
            self.typeBox.Items.Add(t)

    def GetTypeSelected(self, sender, args):
        self.TypeName = sender.SelectedItem
        parameterNames = []
        for element in self.collector:
            if Element.Name.__get__(element) == self.TypeName:
                iterator = element.Parameters.ForwardIterator()
                while iterator.MoveNext():
                    if not iterator.Current.IsReadOnly:
                        parameterNames.append(iterator.Current.Definition.Name)
                break
        self.ParameterNames = parameterNames
        self.parameterBox.Items.Clear()
        for p in self.GetParameters():
            self.parameterBox.Items.Add(p)

    def GetParameterSelected(self, sender, args):
        self.ParameterName = sender.SelectedItem
        for element in self.collector:
            if Element.Name.__get__(element) == self.TypeName:
                iterator = element.Parameters.ForwardIterator()
                while iterator.MoveNext():
                    if iterator.Current.Definition.Name == self.ParameterName:
                        self.Parameter = iterator.Current
                        storage = iterator.Current.StorageType.ToString()
                        paramType = iterator.Current.Definition.ParameterType.ToString()
                        self.StorageLabel.Text = "Storage Type: " + storage
                        self.TypeParamLabel.Text = "Parameter Type: " + paramType
                        if paramType == "YesNo":
                            yesNoValues = {1: "Yes", 0: "No"}
                            self.textBox.Text = yesNoValues.get(iterator.Current.AsInteger(), "")
                        elif storage == "String":
                            self.textBox.Text = iterator.Current.AsString() or ""
                        else:
                            self.textBox.Text = iterator.Current.AsValueString() or ""
                        break
                break

    def UpdateParameter(self, sender, args):
        self.ShowDialogExecute()

    def Cancel(self, sender, args):
        self.DialogResult = DialogResult.Cancel
        self.Close()

    def GetValueBox(self, sender, args):
        self.Value = sender.Text

    def GetCategories(self):
        categories = [category.Name for category in doc.Settings.Categories if category.CategoryType == CategoryType.Model]
        categories.sort()
        return categories

    def GetTypes(self):
        self.TypeNames.sort()
        return self.TypeNames

    def GetParameters(self):
        self.ParameterNames.sort()
        return self.ParameterNames

    def SetParameterValue(self):
        conversionOptions = {"String": self.Value, "Double": self.ConvertValueFloat(), "Integer": self.ConvertValueInt()}
        setValue = conversionOptions.get(self.Parameter.StorageType.ToString())
        if self.Parameter.Definition.ParameterType.ToString() == "YesNo":
            setValue = self.ConvertValueYesNo()
        if setValue is not None:
            t = Transaction(doc, "Parameter Value Update")
            t.Start()
            try:
                self.Parameter.Set(setValue)
                t.Commit()
            except:
                t.RollBack()
                raise
            self.ShowDialogProcess()
            print("Parameter Value Updated: " + self.Parameter.Definition.Name + " = " + str(self.Value))
        else:
            self.ShowDialogProcess(False)
            print("Not Possible to set Parameter. Incorrect value format.")

    def ConvertValueInt(self):
        try:
            return int(self.Value)
        except:
            return None

    def ConvertValueFloat(self):
        try:
            return float(self.Value)
        except:
            return None

    def ConvertValueYesNo(self):
        try:
            if self.Value == "Yes":
                return 1
            if self.Value == "No":
                return 0
        except:
            return None

    def ConfigureForm(self):
        self.Text = "Parameter Value Updater"
        if REVIT_ICON.exists():
            self.Icon = Icon(str(REVIT_ICON))
        self.CategoryName = None
        self.TypeName = None
        self.ParameterName = None
        self.Parameter = None
        self.TypeNames = []
        self.ParameterNames = []
        self.Value = None
        self.Type = None
        self.collector = None
        self.WindowState = FormWindowState.Normal
        self.CenterToScreen()
        self.BringToFront()
        self.Topmost = True
        self.screenSize = Screen.GetWorkingArea(self)
        self.Width = 400
        self.Height = 350
        self.FormBorderStyle = FormBorderStyle.FixedDialog
        self.MaximizeBox = False

    def GenerateFormLabels(self):
        labels = [
            ("Select Category to Filter Family Type:", Point(20, 20)),
            ("Select Family Type to Filter Parameter Set:", Point(20, 80)),
            ("Select Parameter to Modify Value:", Point(20, 140)),
            ("Introduce Parameter value to Set:", Point(20, 200)),
        ]
        for text, location in labels:
            label = Label()
            label.Text = text
            label.Parent = self
            label.Width = 350
            label.Height = 20
            label.Location = location
        self.StorageLabel = Label()
        self.StorageLabel.Text = "Storage Type:"
        self.StorageLabel.Parent = self
        self.StorageLabel.Width = 170
        self.StorageLabel.Height = 20
        self.StorageLabel.Location = Point(20, 250)
        self.TypeParamLabel = Label()
        self.TypeParamLabel.Text = "Parameter Type:"
        self.TypeParamLabel.Parent = self
        self.TypeParamLabel.Width = 170
        self.TypeParamLabel.Height = 20
        self.TypeParamLabel.Location = Point(20, 270)

    def GenerateComboBoxes(self):
        categoryBox = ComboBox()
        categoryBox.Location = Point(20, 40)
        categoryBox.Width = self.screenSize.Width // 7
        for c in self.GetCategories():
            categoryBox.Items.Add(c)
        categoryBox.DropDownStyle = ComboBoxStyle.DropDownList
        categoryBox.SelectedIndexChanged += self.GetCategorySelected
        self.Controls.Add(categoryBox)
        self.typeBox = ComboBox()
        self.typeBox.Location = Point(20, 100)
        self.typeBox.Width = self.screenSize.Width // 7
        for t in self.GetTypes():
            self.typeBox.Items.Add(t)
        self.typeBox.DropDownStyle = ComboBoxStyle.DropDownList
        self.typeBox.SelectedIndexChanged += self.GetTypeSelected
        self.Controls.Add(self.typeBox)
        self.parameterBox = ComboBox()
        self.parameterBox.Location = Point(20, 160)
        self.parameterBox.Width = self.screenSize.Width // 7
        for p in self.GetParameters():
            self.parameterBox.Items.Add(p)
        self.parameterBox.DropDownStyle = ComboBoxStyle.DropDownList
        self.parameterBox.SelectedIndexChanged += self.GetParameterSelected
        self.Controls.Add(self.parameterBox)

    def GenerateTextBox(self):
        self.textBox = TextBox()
        self.textBox.Location = Point(20, 220)
        self.textBox.Width = self.screenSize.Width // 7
        self.textBox.TextChanged += self.GetValueBox
        self.Controls.Add(self.textBox)

    def GenerateButtons(self):
        bUpdate = Button()
        bUpdate.Text = "Update"
        bUpdate.Location = Point(290, 260)
        bUpdate.Click += self.UpdateParameter
        self.Controls.Add(bUpdate)
        bCancel = Button()
        bCancel.Text = "Cancel"
        bCancel.Location = Point(200, 260)
        bCancel.Click += self.Cancel
        self.Controls.Add(bCancel)


print("Opening Parameter Value Updater...")
updaterForm = WindowParameterUpdater()
updaterForm.ShowDialog()
