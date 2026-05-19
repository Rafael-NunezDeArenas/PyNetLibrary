#region references

import clr
import sys
from pathlib import Path
import json
import pandas as pd
from typing import Any, Dict, Optional

clr.AddReference("Autodesk.Navisworks.Api")
from Autodesk.Navisworks.Api import *

clr.AddReference("Autodesk.Navisworks.ComApi")
from Autodesk.Navisworks.Api.ComApi import *

clr.AddReference("Autodesk.Navisworks.Interop.ComApi")
from Autodesk.Navisworks.Api.Interop.ComApi import *

clr.AddReference("Autodesk.Navisworks.Clash")
from Autodesk.Navisworks.Api.Clash import *
from Autodesk.Navisworks.Api.Clash import DocumentClash

from System.Collections.Generic import List

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import *
from System.Drawing import *

bundlePath = (Path.home() / "AppData" / "Roaming" / "Autodesk" / "ApplicationPlugins" / "RAEN.Navisworks.PyNET.bundle" / "Contents" / "2024")
NavisworksinconPath = (Path.home() / "AppData" / "Roaming" / "Autodesk" / "ApplicationPlugins" / "RAEN.Navisworks.PyNET.bundle" / "Contents" / "2024" / "Images" / "manage.ico")

sys.path.append(str(bundlePath))

clr.AddReference("Raen.Core.Pynet.Resources")

from Raen.Core.Pynet.Resources import CastUtils  # type: ignore

from Autodesk.Navisworks.Api import Application
doc = Application.ActiveDocument

#endregion

#region classes

class InputData:
    """
    Handles reading and writing a JSON configuration file that persists
    the last used Excel path between sessions.
    """

    JSON_PATH = bundlePath / "Configuration" / "updateModels.json"

    @staticmethod
    def CreateJson(dictionary):
        InputData.JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
        with InputData.JSON_PATH.open("w", encoding="utf-8") as file:
            json.dump(dictionary, file, ensure_ascii=False, indent=4)

    @staticmethod
    def ReadJson():
        try:
            with InputData.JSON_PATH.open("r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            return None


class ModelData:
    """
    Represents a Navisworks federation model (NWF) and its associated IFC links.
    """

    def __init__(self, name, path):
        self.modelName = name
        self.path = path
        self.links = []

    @property
    def Name(self):
        return self.modelName

    @property
    def Path(self):
        return self.path

    @property
    def Links(self):
        return self.links


class Link:
    """
    Represents a linked IFC model to be appended into a federation.
    """

    def __init__(self, name, path):
        self.modelName = name
        self.path = path

    @property
    def Name(self):
        return self.modelName

    @property
    def Path(self):
        return self.path


class SearchSetData:
    """
    Data container for a Search Set definition read from the Excel matrix.
    """

    def __init__(self, name, value):
        self.searchSetName = name
        self.value = value

    @property
    def Name(self):
        return self.searchSetName

    @property
    def Value(self):
        return self.value


class ClashTestData:
    """
    Data container for a Clash Test definition read from the Excel matrix.
    Stores the test name, left/right selection set names, and tolerance level.
    """

    def __init__(self, name, right, left, tolerance):
        self.modelName = name
        self.right = right
        self.left = left
        self.tolerance = tolerance

    @property
    def Name(self):
        return self.modelName

    @property
    def Right(self):
        return self.right

    @property
    def Left(self):
        return self.left

    @property
    def Tolerance(self):
        return self.tolerance


class DataReader:
    """
    Reads federation, search set, and clash test definitions from an Excel file
    using pandas. Replaces the legacy Balio ExcelManager approach.
    """

    @staticmethod
    def ReadModelsData(path):
        df = pd.read_excel(path, sheet_name="Federacion")
        modelsData = []

        nwfRows = df[df["Extension"].str.lower() == "nwf"]
        ifcRows = df[df["Extension"].str.lower() == "ifc"]

        for _, nwfRow in nwfRows.iterrows():
            modelData = ModelData(nwfRow["Nombre"], nwfRow["Ruta"])

            for _, ifcRow in ifcRows.iterrows():
                if modelData.Name in ifcRow.index and ifcRow[modelData.Name] == "X":
                    modelData.Links.append(Link(ifcRow["Nombre"], ifcRow["Ruta"]))

            modelsData.append(modelData)

        return modelsData

    @staticmethod
    def ReadSearchSetsData(path):
        df = pd.read_excel(path, sheet_name="Matriz")
        setsData = []
        currentDiscipline = None

        for _, row in df.iterrows():
            if pd.notna(row.get("Disciplina")):
                currentDiscipline = str(row["Disciplina"])
            if pd.notna(row.get("Parametro_Clasificacion")):
                name = f"{currentDiscipline}_{row['Nombre']}_{row['Parametro_Clasificacion']}"
                setsData.append(SearchSetData(name, str(row["Parametro_Clasificacion"])))

        return setsData

    @staticmethod
    def ReadClashTestsData(path):
        clashTests = []
        setsData = DataReader.ReadSearchSetsData(path)
        df = pd.read_excel(path, sheet_name="Matriz")
        currentDiscipline = None

        for _, row in df.iterrows():
            if pd.notna(row.get("Disciplina")):
                currentDiscipline = str(row["Disciplina"])
            if pd.notna(row.get("Parametro_Clasificacion")):
                leftName = f"{currentDiscipline}_{row['Nombre']}_{row['Parametro_Clasificacion']}"
                for setData in setsData:
                    cellValue = row.get(setData.Value)
                    if pd.notna(cellValue) and str(cellValue) in ["A", "B", "C"]:
                        rightName = setData.Name
                        testName = f"{cellValue}_{leftName}_vs_{rightName}"
                        clashTests.append(ClashTestData(testName, rightName, leftName, str(cellValue)))

        return clashTests


class ModelManager:
    """
    Provides high-level operations on Navisworks models including opening,
    appending links, removing models, creating search sets and clash tests.
    """

    @staticmethod
    def OpenModel(document, path):
        filePath = Path.home() / path
        if filePath.exists():
            document.OpenFile(str(filePath))

    @staticmethod
    def AppendModels(document, model):
        pathValues = [file.FileName for file in document.Models]
        links = []
        for link in model.Links:
            linkPath = str(Path.home() / link.Path)
            if linkPath not in pathValues:
                links.append(linkPath)
        if links:
            document.AppendFiles(List[str](links))

    @staticmethod
    def SaveModel(document, path):
        filePath = Path.home() / path
        filePath.parent.mkdir(parents=True, exist_ok=True)
        document.SaveFile(str(filePath))

    @staticmethod
    def GetLinksToRemove(document, model):
        expectedPaths = [str(Path.home() / link.Path) for link in model.Links]
        result = ModelItemCollection()
        for file in document.Models:
            if file.FileName not in expectedPaths:
                result.Add(file.RootItem)
        return result

    @staticmethod
    def RemoveModels(document, models):
        document.CurrentSelection.CopyFrom(models)
        state = ComApiBridge.State
        state.DeleteSelectedFiles()

    @staticmethod
    def CreateSearchSets(searchSetData):
        selectionSets = doc.SelectionSets

        searchSet = Search()
        searchSet.Locations = SearchLocations.DescendantsAndSelf
        searchSet.Selection.SelectAll()

        condition = SearchCondition.HasPropertyByDisplayName("Parametro_01_Generales (Tipo de IFC)", "Parametro_Clasificacion")
        conditionValue = condition.EqualValue(VariantData.FromDisplayString(searchSetData.Value))
        conditionList = List[SearchCondition]([conditionValue])
        searchSet.SearchConditions.AddGroup(conditionList)

        conditionOr = SearchCondition.HasPropertyByDisplayName("Parametro_01_Generales (IFC Type)", "Parametro_Clasificacion")
        conditionValueOr = conditionOr.EqualValue(VariantData.FromDisplayString(searchSetData.Value))
        conditionListOr = List[SearchCondition]([conditionValueOr])
        searchSet.SearchConditions.AddGroup(conditionListOr)

        conditionOr2 = SearchCondition.HasPropertyByDisplayName("Parametro_01_Generales", "Parametro_Clasificacion")
        conditionValueOr2 = conditionOr2.EqualValue(VariantData.FromDisplayString(searchSetData.Value))
        conditionListOr2 = List[SearchCondition]([conditionValueOr2])
        searchSet.SearchConditions.AddGroup(conditionListOr2)

        instance = SelectionSet(searchSet)
        instance.DisplayName = searchSetData.Name

        selectionSets.AddCopy(instance)

    @staticmethod
    def CreateClashTests(name, selectionFirst, selectionSecond):
        setFirst = SelectionSourceCollection()
        setFirst.Add(doc.SelectionSets.CreateSelectionSource(selectionFirst))
        setSecond = SelectionSourceCollection()
        setSecond.Add(doc.SelectionSets.CreateSelectionSource(selectionSecond))

        test = ClashTest()
        test.DisplayName = name
        test.TestType = ClashTestType.Hard

        scale = UnitConversion.ScaleFactor(doc.Models.First.Units, Units.Meters)
        if "A_" in name:
            test.Tolerance = 0.01
        elif "B_" in name:
            test.Tolerance = 0.015 / scale
        elif "C_" in name:
            test.Tolerance = 0.02 / scale

        test.SelectionA.SelfIntersect = False
        test.SelectionA.PrimitiveTypes = PrimitiveTypes.Triangles
        test.SelectionB.SelfIntersect = False
        test.SelectionB.PrimitiveTypes = PrimitiveTypes.Triangles
        test.SelectionA.Selection.CopyFrom(setFirst)
        test.SelectionB.Selection.CopyFrom(setSecond)

        clashDocument = CastUtils.CastTo[DocumentClash](doc.Clash)
        clashDocument.TestsData.TestsAddCopy(test.CreateCopy())

    @staticmethod
    def GetSearchSet(name):
        selectionSets = doc.SelectionSets.Value
        for searchSet in selectionSets:
            if searchSet.DisplayName == name:
                return searchSet
        return None


class UpdateForm(Form):
    """
    WinForms dialog for selecting and updating Navisworks federation models.
    Opens each selected model, syncs IFC links, creates search sets, and generates clash tests.
    """

    def Update(self, sender, args):
        if self.Selection is not None:
            clashDoc = CastUtils.CastTo[DocumentClash](doc.Clash)
            existingTestNames = [test.DisplayName for test in clashDoc.TestsData.Tests]

            for model in self.Documents:
                if model.Name in [element for element in self.Selection]:
                    ModelManager.OpenModel(doc, model.Path)
                    print(f"model opened: {model.Name}")

                    if len(model.Links) > 0:
                        ModelManager.AppendModels(doc, model)
                        print("Links updated")

                    models = ModelManager.GetLinksToRemove(doc, model)
                    if models is not None and models.Count > 0:
                        ModelManager.RemoveModels(doc, models)
                        print("Links removed")

                    existingSetNames = [child.DisplayName for child in doc.SelectionSets.RootItem.Children]
                    for setData in DataReader.ReadSearchSetsData(self.Path):
                        if setData.Name not in existingSetNames:
                            ModelManager.CreateSearchSets(setData)
                    print("Search sets updated")

                    for data in DataReader.ReadClashTestsData(self.Path):
                        selectionFirst = ModelManager.GetSearchSet(data.Left)
                        selectionSecond = ModelManager.GetSearchSet(data.Right)
                        if selectionFirst is not None and selectionSecond is not None and data.Name not in existingTestNames:
                            ModelManager.CreateClashTests(data.Name, selectionFirst, selectionSecond)
                    print("Clash tests updated")

                    ModelManager.SaveModel(doc, model.Path)
                    print(f"model saved: {model.Name}")

            DialogManager.ModelsUpdatedDialog()
            self.Close()

    def Cancel(self, sender, args):
        self.DialogResult = DialogResult.Cancel
        self.Status = "Cancel"
        DialogManager.ProcessCancelDialog()
        self.Close()

    def ApplyFilter(self, sender, arg):
        listControl = [control for control in self.Controls if control.Name == "ModelsList"][0]

        data = List[str]()
        for name in self.DocumentNames:
            if sender.Text in name:
                data.Add(name)

        listControl.DataSource = data

    def Include(self, sender, args):
        self.Selection = sender.SelectedItems

    def ConfigureForm(self):
        self.Icon = Icon(str(NavisworksinconPath))
        self.Text = "Update models"
        self.Documents = None
        self.DocumentNames = None
        self.Selection = None
        self.Path = None
        self.WindowState = FormWindowState.Normal
        self.CenterToScreen()
        self.BringToFront()
        self.Topmost = True
        self.Width = 600
        self.Height = 650
        self.MinimumSize = Size(600, 650)
        self.FormBorderStyle = FormBorderStyle.Sizable
        self.MaximizeBox = True

    def Browser(self, sender, args):
        path = DialogManager.ShowOpenFileDialog()
        if path is not None:
            documents = DataReader.ReadModelsData(path)
            listControl = [control for control in self.Controls if control.Name == "ModelsList"][0]

            data = List[str]()
            for name in [document.Name for document in documents]:
                data.Add(name)

            listControl.DataSource = data

            InputData.CreateJson({"path": path})
            self.Path = path
            self.Documents = documents

    def GenerateFormLabels(self):
        labelDescription = Label()
        labelDescription.Text = "Select multiple models to update coordination data."
        labelDescription.Parent = self
        labelDescription.Width = 400
        labelDescription.Height = 50
        labelDescription.Location = Point(20, 10)
        labelDescription.Anchor = AnchorStyles.Left | AnchorStyles.Top

        labelFilter = Label()
        labelFilter.Text = "Model name filter: "
        labelFilter.Parent = self
        labelFilter.Width = 120
        labelFilter.Height = 25
        labelFilter.Location = Point(200, 93)
        labelFilter.Anchor = AnchorStyles.Right | AnchorStyles.Top

    def GenerateFormGroups(self):
        groupBoxViews = GroupBox()
        groupBoxViews.Text = "Models to update"
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
        if documents is not None:
            data = List[str]()
            for name in [document.Name for document in documents]:
                data.Add(name)
            listBox.DataSource = data
            self.DocumentNames = [document.Name for document in documents]
        listBox.SelectedIndexChanged += self.Include
        self.Controls.Add(listBox)

    def GenerateFormButtons(self):
        buttonBrowser = Button()
        buttonBrowser.Width = 120
        buttonBrowser.Text = "Browse data"
        buttonBrowser.Location = Point(20, 570)
        buttonBrowser.Anchor = AnchorStyles.Left | AnchorStyles.Bottom
        buttonBrowser.Click += self.Browser
        self.Controls.Add(buttonBrowser)

        buttonSync = Button()
        buttonSync.Text = "Update"
        buttonSync.Width = 120
        buttonSync.Location = Point(450, 570)
        buttonSync.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
        buttonSync.Click += self.Update
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

    def __init__(self):
        Form.__init__(self)
        self.ConfigureForm()
        self.GenerateFormLabels()
        data = InputData.ReadJson()
        if data is not None and Path(data["path"]).is_file():
            documents = DataReader.ReadModelsData(data["path"])
            self.GenerateFormSelectionList(documents)
            self.Documents = documents
            self.Path = data["path"]
        else:
            self.GenerateFormSelectionList(None)
        self.GenerateTextBox()
        self.GenerateFormButtons()
        self.GenerateFormGroups()


class DialogManager:
    """
    Handles user-facing dialogs for the model update workflow.
    Provides file browser and status message boxes.
    """

    @staticmethod
    def ShowOpenFileDialog():
        openDialog = OpenFileDialog()
        openDialog.Title = "Select Federation File"
        openDialog.InitialDirectory = str(Path.home() / "Desktop")
        openDialog.Filter = "xlsx files (*.xlsx)|*.xlsx|All files (*.*)|*.*"

        if openDialog.ShowDialog() == DialogResult.OK:
            return openDialog.FileName

        return None

    @staticmethod
    def ModelsUpdatedDialog():
        MessageBox.Show("Models updated correctly", "Update models", MessageBoxButtons.OK, MessageBoxIcon.Information)

    @staticmethod
    def ProcessCancelDialog():
        MessageBox.Show("Update models process cancelled", "Update models", MessageBoxButtons.OK, MessageBoxIcon.Warning)

#endregion

#region execution

UpdateForm().ShowDialog()

#endregion
