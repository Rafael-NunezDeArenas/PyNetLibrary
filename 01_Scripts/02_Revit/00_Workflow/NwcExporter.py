import clr
from pathlib import Path
from datetime import date, datetime

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from Autodesk.Revit.DB import *
from System.Windows.Forms import *
from System.Drawing import *
from Autodesk.Revit.UI import TaskDialog, TaskDialogCommonButtons, TaskDialogIcon

uidoc = __revit__.ActiveUIDocument  #type:ignore
doc = uidoc.Document


class NWCExporterLog:
    def __init__(self, path):
        if path is not None:
            self.logPath = "{browser}/NWC_Exporter_{date}.txt".format(browser=path, date=str(date.today()))
            log = open(self.logPath, "w")
            log.write("Tracking\tDocument\tStatus\tExportation\tOutput Exportation")
            log.close()

    def OpenLog(self):
        return open(self.logPath, "a")

    def WriteLogModel(self, document, success=True):
        log = self.OpenLog()
        if success:
            log.write("\n{date}\t{doc}\tInfo\t{doc}: Model Exported\t{path}".format(date=str(datetime.now()), doc=document.Title, path=self.logPath))
        else:
            log.write("\n{date}\t{doc}\tError\t{doc}: Not Possible to Export the Model\tNull".format(date=str(datetime.now()), doc=document.Title))
        log.close()

    def WriteLogView(self, view, document, success=True):
        log = self.OpenLog()
        if success:
            log.write("\n{date}\t{doc}\tInfo\t{view}: View Exported\t{path}".format(date=str(datetime.now()), doc=document.Title, view=view.Name, path=self.logPath))
        else:
            log.write("\n{date}\t{doc}\tError\t{view}: Not Possible to Export the View. Empty View\tNull".format(date=str(datetime.now()), doc=document.Title, view=view.Name))
        log.close()


class WindowFilter(Form):
    def __init__(self, parameters):
        super().__init__()
        self.ConfigureForm(parameters)
        self.GenerateFormLabels()
        self.GenerateComboBoxes()
        self.GenerateTextBox()
        self.GenerateButtons()

    @staticmethod
    def GetParameterBindings(document):
        parameters = []
        iterador = document.ParameterBindings.ForwardIterator()
        while iterador.MoveNext():
            parameters.append(iterador.Key.Name)
        return parameters

    def GetParameter(self, sender, args):
        self.Param = sender.SelectedItem

    def GetValue(self, sender, args):
        self.Value = sender.Text

    def GetParameterProvider(self):
        iterator = doc.ParameterBindings.ForwardIterator()
        self.evaluator = FilterStringEquals()
        while iterator.MoveNext():
            if iterator.Key.Name == self.Param:
                self.provider = ParameterValueProvider(iterator.Key.Id)
                break

    def GetFilterViews(self):
        filterRule = FilterStringRule(self.provider, self.evaluator, self.Value, True)
        filterViews = ElementParameterFilter(filterRule)
        collector = FilteredElementCollector(doc).OfClass(View3D).WherePasses(filterViews).ToElements()
        self.Views = [view.Name for view in collector]

    def Next(self, sender, args):
        self.GetParameterProvider()
        if self.provider is None or self.Value is None:
            self.Status = "Missing"
        else:
            self.GetFilterViews()
            if len(self.Views) < 1:
                self.Status = "Empty"
        self.DialogResult = DialogResult.OK
        self.Close()

    def Cancel(self, sender, args):
        self.DialogResult = DialogResult.Cancel
        self.Status = "Cancel"
        self.Close()

    def ConfigureForm(self, parameters):
        self.Text = "NWC Exporter"
        if REVIT_ICON.exists():
            self.Icon = Icon(str(REVIT_ICON))
        self.Parameters = parameters
        self.Param = None
        self.Value = None
        self.Views = None
        self.provider = None
        self.evaluator = None
        self.Status = None
        self.WindowState = FormWindowState.Normal
        self.CenterToScreen()
        self.BringToFront()
        self.Topmost = True
        self.screenSize = Screen.GetWorkingArea(self)
        self.Width = 400
        self.Height = 240
        self.FormBorderStyle = FormBorderStyle.FixedDialog

    def GenerateFormLabels(self):
        label1 = Label()
        label1.Text = "Select Project Parameter to use in the 3D view Filter:"
        label1.Parent = self
        label1.Width = 350
        label1.Height = 20
        label1.Location = Point(20, 10)
        label2 = Label()
        label2.Text = "Add the Value of the Parameter to filter the 3D views: "
        label2.Parent = self
        label2.Width = 350
        label2.Height = 20
        label2.Location = Point(20, 80)

    def GenerateComboBoxes(self):
        cBox = ComboBox()
        cBox.Location = Point(20, 40)
        cBox.Width = self.screenSize.Width // 7
        for p in (self.Parameters or []):
            cBox.Items.Add(p)
        cBox.DropDownStyle = ComboBoxStyle.DropDownList
        cBox.SelectedIndexChanged += self.GetParameter
        self.Controls.Add(cBox)

    def GenerateTextBox(self):
        tBox = TextBox()
        tBox.Location = Point(20, 110)
        tBox.Width = self.screenSize.Width // 7
        tBox.TextChanged += self.GetValue
        self.Controls.Add(tBox)

    def GenerateButtons(self):
        bNext = Button()
        bNext.Text = "Next"
        bNext.Location = Point(290, 150)
        bNext.Click += self.Next
        self.Controls.Add(bNext)
        buttonCancel = Button()
        buttonCancel.Text = "Cancel"
        buttonCancel.Location = Point(200, 150)
        buttonCancel.Click += self.Cancel
        self.Controls.Add(buttonCancel)


class WindowExport(Form):
    def __init__(self, values):
        super().__init__()
        self.ConfigureForm(values)
        self.GenerateFormComboBoxes()
        self.GenerateFormLabels()
        self.GenerateFormSelectionList()
        self.GenerateFormCheckBoxes()
        self.GenerateFormButtons()
        self.GenerateFormGroups()

    @staticmethod
    def ExecuteExportation(result, obj):
        if obj.Options.ExportScope == NavisworksExportScope.View:
            result.Close()
            if obj.Output is None:
                obj.ShowNotViewsSelectedDialog()
            else:
                obj.Close()
                obj.ExportViews(obj, result)
        if obj.Options.ExportScope == NavisworksExportScope.Model:
            result.Close()
            if obj.Output is not None:
                obj.ExportModel(obj, result)

    def EmptyViewFilter(self, viewsToAnalyze, options):
        viewsResult = []
        for n in viewsToAnalyze:
            if not n.IsTemplate:
                collector = FilteredElementCollector(doc, n.Id)
                elementsInView = collector.WhereElementIsViewIndependent().ToElements()
                for m in elementsInView:
                    if n not in viewsResult:
                        if m.Category is not None and hasattr(m.Category, "CategoryType") and m.Category.CategoryType == CategoryType.Model and m.get_Geometry(options) is not None:
                            geometry = m.get_Geometry(options)
                            for geoElem in geometry:
                                if hasattr(geoElem, "Volume") and geoElem.Volume > 0:
                                    viewsResult.append(n)
        return viewsResult

    def ShowNotViewsSelectedDialog(self):
        dialog = TaskDialog("NWC Exporter")
        dialog.MainContent = "No Views Selected"
        dialog.CommonButtons = TaskDialogCommonButtons.Ok
        dialog.MainIcon = TaskDialogIcon.TaskDialogIconInformation
        dialog.Show()

    def ExportViews(self, obj, result):
        exporterLog = NWCExporterLog(obj.log)
        views = FilteredElementCollector(doc).OfClass(View3D).ToElements()
        filterViews = [n for n in views if n.Name in obj.Output]
        opts = Options()
        opts.DetailLevel = ViewDetailLevel.Fine
        viewsNotEmpty = obj.EmptyViewFilter(views, opts)
        for view in filterViews:
            if view in viewsNotEmpty:
                obj.Options.ViewId = view.Id
                doc.Export(obj.Path, view.Name, obj.Options)
                result.ElementsExported.append(view.Name + ": View Exported")
                if obj.log is not None:
                    exporterLog.WriteLogView(view, doc)
            else:
                result.Errors.append(view.Name + ": Not Possible to Export the View. Empty View")
                if obj.log is not None:
                    exporterLog.WriteLogView(view, doc, False)

    def ExportModel(self, obj, result):
        if obj.log is not None:
            log = NWCExporterLog(obj.log)
        try:
            doc.Export(obj.Path, str(doc.Title), obj.Options)
            result.ElementsExported.append(doc.Title + ": Model Exported")
            if obj.log is not None:
                log.WriteLogModel(doc)
        except:
            result.Errors.append(str(doc.Title) + ": Not Possible to Export the Model")
            if obj.log is not None:
                log.WriteLogModel(doc, False)

    def Export(self, sender, args):
        self.DialogResult = DialogResult.OK
        Resultform = WindowResult(self.Options.ExportScope)
        Resultform.ShowDialog()
        self.Resultform = Resultform

    def Cancel(self, sender, args):
        self.DialogResult = DialogResult.Cancel
        self.Close()

    def GetResultForm(self):
        return self.Resultform

    def CheckCoordinates(self, sender, args):
        if sender.SelectedItem == "Shared":
            self.Options.Coordinates = NavisworksCoordinates.Shared
        else:
            self.Options.Coordinates = NavisworksCoordinates.Internal

    def CheckExportScope(self, sender, args):
        if sender.SelectedItem == "View":
            self.Options.ExportScope = NavisworksExportScope.View
        else:
            self.Options.ExportScope = NavisworksExportScope.Model

    def CheckConvertElementProperties(self, sender, args):
        self.Options.ConvertElementProperties = sender.Checked

    def CheckConverLights(self, sender, args):
        self.Options.ConvertLights = sender.Checked

    def CheckConvertLinkedCadFormat(self, sender, args):
        self.Options.ConvertLinkedCADFormats = sender.Checked

    def CheckDivideFileIntoLevels(self, sender, args):
        self.Options.DivideFileIntoLevels = sender.Checked

    def CheckExportElementIds(self, sender, args):
        self.Options.ExportElementIds = sender.Checked

    def CheckExportLinks(self, sender, args):
        self.Options.ExportLinks = sender.Checked

    def CheckExportParts(self, sender, args):
        self.Options.ExportParts = sender.Checked

    def CheckExportRoomAsAttribute(self, sender, args):
        self.Options.ExportRoomAsAttribute = sender.Checked

    def CheckExportRoomGeometry(self, sender, args):
        self.Options.ExportRoomGeometry = sender.Checked

    def CheckExportUrl(self, sender, args):
        self.Options.ExportUrls = sender.Checked

    def CheckFindMissingMaterials(self, sender, args):
        self.Options.FindMissingMaterials = sender.Checked

    def Browser(self, sender, args):
        with FolderBrowserDialog() as dialog:
            if dialog.ShowDialog() == DialogResult.OK:
                self.Path = dialog.SelectedPath

    def LogBrowser(self, sender, args):
        with FolderBrowserDialog() as dialog:
            if dialog.ShowDialog() == DialogResult.OK:
                self.log = dialog.SelectedPath

    def Include(self, sender, args):
        self.Output = sender.SelectedItems

    def ConfigureForm(self, values):
        screenSize = Screen.GetWorkingArea(self)
        self.Width = 910
        self.Height = 620
        self.viewNames = values
        self.WindowResult = None
        self.Text = "NWC Exporter"
        if REVIT_ICON.exists():
            self.Icon = Icon(str(REVIT_ICON))
        self.Output = None
        self.Path = None
        self.log = None
        self.Options = NavisworksExportOptions()
        self.Resultform = None
        self.WindowState = FormWindowState.Normal
        self.CenterToScreen()
        self.BringToFront()
        self.Topmost = True
        self.FormBorderStyle = FormBorderStyle.FixedDialog

    def GenerateFormComboBoxes(self):
        comboBoxCoordinates = ComboBox()
        comboBoxCoordinates.Location = Point(650, 125)
        comboBoxCoordinates.Width = 100
        comboBoxCoordinates.Items.AddRange(("Shared", "Project Internal"))
        comboBoxCoordinates.DropDownStyle = ComboBoxStyle.DropDownList
        comboBoxCoordinates.SelectedIndexChanged += self.CheckCoordinates
        self.Controls.Add(comboBoxCoordinates)
        combBoxExportScope = ComboBox()
        combBoxExportScope.Location = Point(650, 395)
        combBoxExportScope.Width = 100
        combBoxExportScope.Items.AddRange(("View", "Model"))
        combBoxExportScope.DropDownStyle = ComboBoxStyle.DropDownList
        combBoxExportScope.SelectedIndexChanged += self.CheckExportScope
        self.Controls.Add(combBoxExportScope)

    def GenerateFormLabels(self):
        label1 = Label()
        label1.Text = "Select the 3D Views to Export to NWC and configure the Navisworks Settings: "
        label1.Parent = self
        label1.Width = 800
        label1.Height = 50
        label1.Location = Point(20, 10)
        label2 = Label()
        label2.Text = "Navisworks Coordinates"
        label2.Parent = self
        label2.Width = 250
        label2.Height = 30
        label2.Font = Font("OpenSans", 8)
        label2.Location = Point(470, 130)
        label3 = Label()
        label3.Text = "Export Scope"
        label3.Parent = self
        label3.Width = 250
        label3.Height = 30
        label3.Font = Font("OpenSans", 8)
        label3.Location = Point(470, 400)

    def GenerateFormSelectionList(self):
        listBox = ListBox()
        listBox.Location = Point(50, 90)
        listBox.Width = 300
        listBox.Height = 400
        listBox.SelectionMode = SelectionMode.MultiExtended
        for v in (self.viewNames or []):
            listBox.Items.Add(v)
        listBox.SelectedIndexChanged += self.Include
        self.Controls.Add(listBox)

    def GenerateFormGroups(self):
        groupBoxViews = GroupBox()
        groupBoxViews.Text = "3D Views in Current Model: "
        groupBoxViews.Size = Size(400, 450)
        groupBoxViews.Location = Point(20, 60)
        groupBoxViews.Parent = self
        groupBoxSettings = GroupBox()
        groupBoxSettings.Text = "Navisworks Settings:  "
        groupBoxSettings.Size = Size(400, 450)
        groupBoxSettings.Location = Point(450, 60)
        groupBoxSettings.Parent = self

    def GenerateFormCheckBoxes(self):
        checks = [
            ("Convert Element Properties", Point(470, 100), "CheckConvertElementProperties", True),
            ("Convert Lights", Point(470, 160), "CheckConverLights", False),
            ("Convert Linked CAD Formats", Point(470, 190), "CheckConvertLinkedCadFormat", False),
            ("Divide File Into Levels", Point(470, 220), "CheckDivideFileIntoLevels", True),
            ("Export Element IDs", Point(470, 250), "CheckExportElementIds", True),
            ("Export Links", Point(470, 280), "CheckExportLinks", False),
            ("Export Parts", Point(470, 310), "CheckExportParts", False),
            ("Export Rooms As Attribute", Point(470, 340), "CheckExportRoomAsAttribute", True),
            ("Export Rooms Geometry", Point(470, 370), "CheckExportRoomGeometry", False),
            ("Export URLs", Point(470, 430), "CheckExportUrl", False),
            ("Find Missing Materials", Point(470, 460), "CheckFindMissingMaterials", False),
        ]
        for text, location, handler_name, checked in checks:
            cb = CheckBox()
            cb.Text = text
            cb.Location = location
            cb.Width = 250
            cb.Font = Font("OpenSans", 8)
            cb.CheckedChanged += getattr(self, handler_name)
            cb.Checked = checked
            self.Controls.Add(cb)

    def GenerateFormButtons(self):
        buttonExport = Button()
        buttonExport.Text = "Export"
        buttonExport.Width = 120
        buttonExport.Location = Point(730, 530)
        buttonExport.Click += self.Export
        self.Controls.Add(buttonExport)
        buttonBrowser = Button()
        buttonBrowser.Width = 120
        buttonBrowser.Text = "Folder Browser"
        buttonBrowser.Location = Point(600, 530)
        buttonBrowser.Click += self.Browser
        self.Controls.Add(buttonBrowser)
        buttonCancel = Button()
        buttonCancel.Width = 120
        buttonCancel.Text = "Cancel"
        buttonCancel.Location = Point(470, 530)
        buttonCancel.Click += self.Cancel
        self.Controls.Add(buttonCancel)
        buttonLog = Button()
        buttonLog.Width = 120
        buttonLog.Text = "Log Output"
        buttonLog.Location = Point(20, 530)
        buttonLog.Click += self.LogBrowser
        self.Controls.Add(buttonLog)


class WindowResult(Form):
    def __init__(self, exportOptions):
        super().__init__()
        self.ConfigureForm(exportOptions)
        self.GenerateFormLabels()
        self.GenerateButtons()

    def Accept(self, sender, args):
        WindowExport.ExecuteExportation(self, Exporterform)
        self.DialogResult = DialogResult.OK

    def Cancel(self, sender, args):
        self.DialogResult = DialogResult.Cancel
        self.Close()

    def ConfigureForm(self, exportOptions):
        self.Text = "NWC Exporter"
        if REVIT_ICON.exists():
            self.Icon = Icon(str(REVIT_ICON))
        self.ElementsExported = []
        self.Errors = []
        self.ExportOption = exportOptions
        self.WindowState = FormWindowState.Normal
        self.CenterToScreen()
        self.BringToFront()
        self.Topmost = True
        self.Width = 510
        self.Height = 190
        self.FormBorderStyle = FormBorderStyle.FixedDialog

    def GenerateFormLabels(self):
        if self.ExportOption == NavisworksExportScope.View:
            text = "View Scope Option will generate a NWC export for each selected view. Are you sure you want to continue?"
        else:
            text = "Model Scope Option will generate one export with the entire model. Are you sure you want to continue?"
        label = Label()
        label.Text = text
        label.Parent = self
        label.Width = 400
        label.Height = 50
        label.Location = Point(20, 20)

    def GenerateButtons(self):
        bAccept = Button()
        bAccept.Text = "Accept"
        bAccept.Location = Point(320, 100)
        bAccept.Click += self.Accept
        self.Controls.Add(bAccept)
        buttonCancel = Button()
        buttonCancel.Text = "Cancel"
        buttonCancel.Location = Point(400, 100)
        buttonCancel.Click += self.Cancel
        self.Controls.Add(buttonCancel)


class TaskdialogResults:
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


print("Opening NWC Exporter filter...")
filterform = WindowFilter(WindowFilter.GetParameterBindings(doc))
filterform.ShowDialog()

if filterform.DialogResult == DialogResult.Cancel:
    TaskdialogResults().ShowCancelTaskDialog()
    print("Process Canceled")
else:
    resultMessages = {"Cancel": "No 3D Views collected", "Missing": "Missing input", "Empty": "No views found"}
    filterFormResult = resultMessages.get(filterform.Status)
    if filterFormResult is None:
        print("Parameter: {0}, Value: {1}, Views: {2}".format(filterform.Param, filterform.Value, filterform.Views))
        Exporterform = WindowExport(filterform.Views)
        Exporterform.ShowDialog()
        if Exporterform.DialogResult == DialogResult.OK:
            resultForm = Exporterform.GetResultForm()
            if resultForm.DialogResult == DialogResult.OK:
                if len(resultForm.Errors) == 0:
                    TaskdialogResults().ShowCorrectTaskDialog()
                    print("Export complete. Exported: {0}".format(resultForm.ElementsExported))
                else:
                    TaskdialogResults().ShowErrorsTaskDialog()
                    print("Exported: {0}, Errors: {1}".format(resultForm.ElementsExported, resultForm.Errors))
        elif Exporterform.DialogResult == DialogResult.Cancel:
            TaskdialogResults().ShowCancelTaskDialog()
            print("Process Canceled")
    else:
        print(filterFormResult)
