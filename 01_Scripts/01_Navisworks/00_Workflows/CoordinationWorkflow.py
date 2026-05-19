#region references

import clr
import sys
from pathlib import Path
import json
import pandas as pd
from typing import Any, Dict, Optional
import threading

sys.path.append(str(Path.home() / "AppData" / "Roaming" / "Pynet" / "Library" / "01_Scripts" / "01_Navisworks" / "00_Workflows"))

from CoordinationDashboard import RunDashboard

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

from System.Windows.Forms import*
from System.Drawing import*
from System import DateTime

bundlePath = (Path.home()/ "AppData"/ "Roaming"/ "Autodesk"/ "ApplicationPlugins"/ "RAEN.Navisworks.PyNET.bundle"/ "Contents"/ "2027")
NavisworksinconPath = (Path.home()/ "AppData"/ "Roaming"/ "Autodesk"/ "ApplicationPlugins"/ "RAEN.Navisworks.PyNET.bundle"/ "Contents"/ "2027" / "Images" / "manage.ico")

sys.path.append(str(bundlePath))

clr.AddReference("Raen.Core.Pynet.Resources")

from Raen.Core.Pynet.Resources import CastUtils  # type: ignore

from Autodesk.Navisworks.Api import Application 
doc = Application.ActiveDocument

#endregion

#region: classes

class InputData:
    """
    Handles reading and writing a JSON file that stores update information
    for Navisworks models. Uses a fixed path inside the plugin bundle.
    """

    # Path to the JSON file
    JSON_PATH: Path = (
        bundlePath
        / "Configuration"
        / "updateModels.json"
    )

    @staticmethod
    def CreateJson(dictionary: Dict[str, Any]) -> None:
        """
        Saves the given dictionary to the JSON file.
        """
        # Ensure parent folder exists
        InputData.JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
        with InputData.JSON_PATH.open("w", encoding="utf-8") as file:
            json.dump(dictionary, file, ensure_ascii=False, indent=4)

    @staticmethod
    def ReadJson() -> Optional[Dict[str, Any]]:
        """
        Reads the JSON file and returns its contents as a dictionary.
        Returns None if the file doesn't exist or cannot be read.
        """
        try:
            with InputData.JSON_PATH.open("r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            return None

class WorkflowForm(Form):
    """
    WinForms dialog for executing the coordination workflow on selected models.
    Runs clash tests, exports results, creates backups, and publishes NWD files.
    """

    # Update Legends Button
    def Update(self, sender, args):
        if self.Selection != None and self.Version != "":
            
            dash_thread = threading.Thread(
                target=RunDashboard,
                daemon=False
            )
            dash_thread.start()

            for model in self.Documents:
                if model.Name in [element for element in self.Selection]:
                    ModelManager.OpenModel(doc, model.Path)
                    print("model opened: {modelName}".format(modelName = model.Name))

                    ModelManager.backUpModel(doc, model, self.Version)
                    print("Backup model created")

                    ModelManager.RunClashTests(doc)
                    print("Clash tests executed")

                    ModelManager.ExportResults(doc, model, self.Version)
                    print("Clash tests results exported")

                    ModelManager.PublishModel(doc, model, self.Version)
                    print("Model published")

                    ModelManager.SaveModel(doc, model.Path)
                    print("model saved: {modelName}".format(modelName = model.Name))
    
            DialogManager.ModelsUpdatedDialog()
        else:
            DialogManager.InputErrorDialog()

        self.Close()
    # Generate Function for Cancel Button		
    def Cancel(self, sender, args):
            self.DialogResult = DialogResult.Cancel
            self.Status = "Cancel"
            DialogManager.ProcessCancellDialog()
            self.Close()    
    # Filter Button
    def ApplyFilter(self, sender, arg):
        listControl = [control for control in self.Controls if control.Name == "ModelsList"][0]

        data = List[str]()
        for name in self.DocumentNames:
            if sender.Text in name:
                data.Add(name)      

        listControl.DataSource = data
    # Generate Function to include selected elements in Group Box
    def Include(self, sender, args):
        self.Selection = sender.SelectedItems
    def GetVersion(self, sender, args):
        self.Version = sender.Text
    # Windows Form Configuration
    def ConfigureForm(self):
    # Include Icon
        self.Icon = Icon(str(NavisworksinconPath))
    #Generate Tittle Value
        self.Text = "Coordination Workflow"
    #Form Variables
        self.Documents = None
        self.DocumentNames = None
        self.Selection = None
        self.Path = None
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
    def Browser(self, sender, args):
        path = DialogManager.ShowOpenFileDialog()
        if path != None:
            documents = DataReader.ReadModelsData(path)
            listControl = [control for control in self.Controls if control.Name == "ModelsList"][0]

            data = List[str]()
            for name in [document.Name for document in documents]:
                data.Add(name)      

            listControl.DataSource = data

            InputData.CreateJson({"path": path})
            self.Path = path
            self.Documents = documents
    # Windows Form Labels
    def GenerateFormLabels(self):
        # Description General
        labelGeneralDescription = Label()
        labelGeneralDescription.Text = "Select multiple models to execute the coordination Workflow."
        labelGeneralDescription.Parent = self
        labelGeneralDescription.Width = 400
        labelGeneralDescription.Height = 50
        labelGeneralDescription.Location = Point(20, 10)
        labelGeneralDescription.Anchor = AnchorStyles.Left | AnchorStyles.Top
        # Filter Label
        labelGeneralDescription = Label()
        labelGeneralDescription.Text = "Model name filter: "
        labelGeneralDescription.Parent = self
        labelGeneralDescription.Width = 120
        labelGeneralDescription.Height = 25
        labelGeneralDescription.Location = Point(200, 93)
        labelGeneralDescription.Anchor = AnchorStyles.Right | AnchorStyles.Top
    # Windows Form Groups
    def GenerateFormGroups(self):
        # Generate Group Views	
        groupBoxViews = GroupBox()
        groupBoxViews.Text = "Models to include in workflow"
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
        if documents != None:
            data = List[str]()
            for name in [document.Name for document in documents]:
                data.Add(name)      

            listBox.DataSource = data
            
            self.DocumentNames = [document.Name for document in documents]
        listBox.SelectedIndexChanged += self.Include
        self.Controls.Add(listBox)
    # Windows Form Buttons
    def GenerateFormButtons(self):
    # Generate Browser Button
        buttonBrowser = Button()
        buttonBrowser.Width = 120
        buttonBrowser.Text = "Browse data"
        buttonBrowser.Location = Point(20, 570)
        buttonBrowser.Anchor = AnchorStyles.Left | AnchorStyles.Bottom
        buttonBrowser.Click += self.Browser
        self.Controls.Add(buttonBrowser)
    # Generate Export Button
        buttonSync = Button()
        buttonSync.Text = "Execute"
        buttonSync.Width = 120
        buttonSync.Location = Point(450, 570)
        buttonSync.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
        buttonSync.Click += self.Update
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
        # Filter textBox
        textBox = TextBox()
        textBox.Location = Point(325, 90)
        textBox.Width = 225
        textBox.Anchor = AnchorStyles.Right | AnchorStyles.Top
        textBox.TextChanged += self.ApplyFilter
        self.Controls.Add(textBox)
        # Version textBox
        textBox = TextBox()
        textBox.Location = Point(150, 570)
        textBox.Width = 160
        textBox.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
        textBox.TextChanged += self.GetVersion
        self.Controls.Add(textBox)
    # Constructor Class
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
            self.Version = ""
        else:
            self.GenerateFormSelectionList(None)
        self.GenerateTextBox()        
        self.GenerateFormButtons()
        self.GenerateFormGroups()

class ClashDataResult:
    """
    Wrapper class to extract, normalize, and store information from
    a Navisworks Clash Test. Computes counts for each clash status
    (New, Active, Reviewed, Approved, Resolved) and exposes read-only
    properties for export or UI consumption.
    """

    def __init__(self, test: Any) -> None:
        self.testName: str = test.DisplayName
        self.tolerance: float = test.Tolerance
        self.status: str = test.Status
        self.lastRun: str = test.LastRun

        self.new: int = 0
        self.active: int = 0
        self.reviewed: int = 0
        self.approved: int = 0
        self.resolved: int = 0

        for child in test.Children:
            status = str(child.Status).upper()
            if status == str(ClashResultStatus.New).upper():
                self.new += 1
            elif status == str(ClashResultStatus.Active).upper():
                self.active += 1
            elif status == str(ClashResultStatus.Reviewed).upper():
                self.reviewed += 1
            elif status == str(ClashResultStatus.Approved).upper():
                self.approved += 1
            elif status == str(ClashResultStatus.Resolved).upper():
                self.resolved += 1

    @property
    def Name(self) -> str:
        """Returns the Clash Test display name."""
        return self.testName

    @property
    def Tolerance(self) -> float:
        """Returns the clash test tolerance."""
        return self.tolerance

    @property
    def Status(self) -> str:
        """Returns the overall status of the clash test."""
        return self.status

    @property
    def LastRun(self) -> str:
        """Returns the last execution date/time of the clash test."""
        return self.lastRun

    @property
    def NewCount(self) -> int:
        """Returns the number of NEW clash results."""
        return self.new

    @property
    def ActiveCount(self) -> int:
        """Returns the number of ACTIVE clash results."""
        return self.active

    @property
    def ReviewedCount(self) -> int:
        """Returns the number of REVIEWED clash results."""
        return self.reviewed

    @property
    def ApprovedCount(self) -> int:
        """Returns the number of APPROVED clash results."""
        return self.approved

    @property
    def ResolvedCount(self) -> int:
        """Returns the number of RESOLVED clash results."""
        return self.resolved

class ClashTotalsResult:
    """
    Wrapper class to extract, normalize, and store information from
    a Navisworks Clash Test. Computes Total counts for each clash status
    (New, Active, Reviewed, Approved, Resolved) and exposes read-only
    properties for export or UI consumption.
    """

    def __init__(self, tests: Any) -> None:
        self.new: int = 0
        self.active: int = 0
        self.reviewed: int = 0
        self.approved: int = 0
        self.resolved: int = 0

        for test in tests:
            self.new += test.NewCount
            self.active += test.ActiveCount
            self.reviewed += test.ReviewedCount
            self.approved += test.ApprovedCount
            self.resolved += test.ResolvedCount

    @property
    def NewCount(self) -> int:
        """Returns the number of NEW clash results."""
        return self.new

    @property
    def ActiveCount(self) -> int:
        """Returns the number of ACTIVE clash results."""
        return self.active

    @property
    def ReviewedCount(self) -> int:
        """Returns the number of REVIEWED clash results."""
        return self.reviewed

    @property
    def ApprovedCount(self) -> int:
        """Returns the number of APPROVED clash results."""
        return self.approved

    @property
    def ResolvedCount(self) -> int:
        """Returns the number of RESOLVED clash results."""
        return self.resolved

class DataManager:
    """
    High-level controller to manage the export of the data
    to CSV format using Pandas.
    """
        
    @staticmethod
    def ExportData(data, path):
        """
        Take the properties from the object to convert them to a dictionary.
        Export the dictionary to CSV.
        """
        df = pd.DataFrame([clash.__dict__ for clash in data])
        df.to_csv(path, index=False)
        DATA_ROOT = path
    @staticmethod
    def ExportClashData(data):
        results = ClashTotalsResult(data)
        CSV_PATH = Path.home() / "Desktop" / "clash_dashboard.csv"

        # Nuevo registro
        data = {
            "new": results.NewCount,
            "active": results.ActiveCount,
            "reviewed": results.ReviewedCount,
            "approved": results.ApprovedCount,
            "resolved": results.ResolvedCount
        }

        # Si existe CSV, leerlo y sumar
        if CSV_PATH.exists():
            try:
                dfExisting = pd.read_csv(CSV_PATH)
                # Asegurar que las columnas existen
                for col in ["new","active","reviewed","approved","resolved"]:
                    if col not in dfExisting.columns:
                        dfExisting[col] = 0
                # Sumar los valores nuevos a la primera fila (acumular totales)
                dfExisting.loc[0, "new"] += data["new"]
                dfExisting.loc[0, "active"] += data["active"]
                dfExisting.loc[0, "reviewed"] += data["reviewed"]
                dfExisting.loc[0, "approved"] += data["approved"]
                dfExisting.loc[0, "resolved"] += data["resolved"]
                dfUpdated = dfExisting
            except Exception:
                # Si hay error leyendo, crear nuevo DataFrame
                dfUpdated = pd.DataFrame([data])
        else:
            dfUpdated = pd.DataFrame([data])

        # Guardar CSV actualizado
        dfUpdated.to_csv(CSV_PATH, index=False, encoding="utf-8-sig")

class ModelData:
    """
    Represents a Navisworks model and its associated linked models.
    Stores the model's name, path, and a list of links to other models.
    """

    def __init__(self, name: str, path: str) -> None:
        self.modelName: str = name
        self.path: str = path
        self.links = []

    @property
    def Name(self) -> str:
        """Returns the model's display name."""
        return self.modelName

    @property
    def Path(self) -> str:
        """Returns the file path of the model."""
        return self.path

    @property
    def Links(self):
        """Returns the list of linked models."""
        return self.links

class Link:
    """
    Represents a linked Navisworks model.
    Stores the name and path of the linked model.
    """

    def __init__(self, name: str, path: str) -> None:
        self.modelName: str = name
        self.path: str = path

    @property
    def Name(self) -> str:
        """Returns the linked model's display name."""
        return self.modelName

    @property
    def Path(self) -> str:
        """Returns the file path of the linked model."""
        return self.path

class DataResult:
    """
    Represents a processed result for a model.
    Stores the model's name and its file path.
    Can be extended to store additional metadata.
    """

    def __init__(self, name: str, path: str) -> None:
        self.modelName: str = name
        self.path: str = path

    @property
    def Name(self) -> str:
        """Returns the model's display name."""
        return self.modelName

    @property
    def Path(self) -> str:
        """Returns the file path of the model."""
        return self.path

class DataReader:
    """
    Reads model data and their links from an Excel file using pandas.
    Replaces the legacy ExcelDataReader/DLL approach.
    """

    @staticmethod
    def ReadModelsData(path: str):
        """
        Reads the 'Federacion' sheet from the Excel file and builds a list
        of ModelData objects, with links to other models where indicated.

        Args:
            path (str): Path to the Excel file.

        Returns:
            List[ModelData]: List of model data objects with links.
        """
        df = pd.read_excel(path, sheet_name="Federacion")
        modelsData: List[ModelData] = []

        # Filter only models with Extension == "nwf"
        nwfRows = df[df["Extension"].str.lower() == "nwf"]

        # Filter only links with Extension == "ifc"
        ifcRows = df[df["Extension"].str.lower() == "ifc"]

        for _, nwfRow in nwfRows.iterrows():
            modelData = ModelData(nwfRow["Nombre"], nwfRow["Ruta"])

            # Iterate over ifc_rows to check links
            for _, ifcRow in ifcRows.iterrows():
                # Check if there's an "X" in the column corresponding to model name
                if modelData.Name in ifcRow and ifcRow[modelData.Name] == "X":
                    modelData.Links.append(Link(ifcRow["Nombre"], ifcRow["Ruta"]))

            modelsData.append(modelData)

        return modelsData
    
class ModelManager:
    """
    Provides high-level operations on Navisworks models,
    including opening, saving, backing up, running clash tests,
    exporting results, and publishing models.
    """

    @staticmethod
    def OpenModel(document: Any, path: str) -> None:
        """
        Opens a Navisworks model if it exists.
        """
        filePath = Path.home() / path
        if filePath.exists():
            document.OpenFile(str(filePath))

    @staticmethod
    def SaveModel(document: Any, path: str) -> None:
        """
        Saves the Navisworks model to the specified path,
        creating parent directories if necessary.
        """
        filePath = Path.home() / path
        filePath.parent.mkdir(parents=True, exist_ok=True)
        document.SaveFile(str(filePath))

    @staticmethod
    def backUpModel(document: Any, model: Any, version: str) -> None:
        """
        Creates a backup of the model in a versioned folder.
        """
        folder = Path.home() / Path(model.Path).parent
        backupFolder = folder / version
        backupFolder.mkdir(parents=True, exist_ok=True)

        backupFile = backupFolder / model.Name
        document.SaveFile(str(backupFile))

    @staticmethod
    def RunClashTests(document: Any) -> None:
        """
        Runs all clash tests in the document.
        """
        clashDocument = CastUtils.CastTo[DocumentClash](document.Clash)
        clashDocument.TestsData.TestsRunAllTests()

    @staticmethod
    def ExportResults(document: Any, model: Any, version: str) -> None:
        """
        Exports clash test results and model logs to a data folder.
        """
        folder = Path.home() / Path(model.Path).parent
        dataFolder = Path(str(folder).replace("01_nwf", "03_data")) / version
        dataFolder.mkdir(parents=True, exist_ok=True)

        clashDocument = CastUtils.CastTo[DocumentClash](document.Clash)
        tests = clashDocument.TestsData.Tests
        DataManager.ExportData([ClashDataResult(test) for test in tests], f"{dataFolder}/ClashData.csv")
        DataManager.ExportData([DataResult(Path(model.FileName).name, model.FileName) for model in document.Models.GetEnumerator()], f"{dataFolder}/ModelsData.csv")
        DataManager.ExportClashData([ClashDataResult(test) for test in tests])

    @staticmethod
    def PublishModel(document: Any, model: Any, version: str) -> None:
        """
        Publishes the model to a versioned folder with standard properties.
        """
        folder = Path.home() / Path(model.Path).parent
        publishFolder = Path(str(folder).replace("01_nwf", "02_nwd")) / version
        publishFolder.mkdir(parents=True, exist_ok=True)

        properties = PublishProperties()
        properties.AllowResave = True
        properties.Author = "PyNET"
        properties.Comments = "Weekly export"
        properties.Copyright = "PyNET"
        properties.DisplayAtPassword = True
        properties.DisplayOnOpen = True
        properties.EmbedDatabaseProperties = True
        properties.EmbedTextures = True
        properties.PreventObjectPropertyExport = False
        properties.PublishDate = DateTime.Now
        properties.PublishedFor = "PyNET"
        properties.Publisher = "PyNET"
        properties.Subject = "Coordination"
        properties.Title = model.Name.replace("nwf", "")

        publishPath = publishFolder / model.Name.replace(".nwf", ".nwd")
        document.PublishFile(str(publishPath), properties)

class DialogManager:
    """
    Handles user-facing dialogs for the coordination workflow.
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
        MessageBox.Show("Workflow process executed correctly", "Coordination workflow", MessageBoxButtons.OK, MessageBoxIcon.Information)
    @staticmethod
    def ProcessCancellDialog():
        MessageBox.Show("Workflow process cancelled", "Coordination workflow", MessageBoxButtons.OK, MessageBoxIcon.Warning)
    @staticmethod
    def InputErrorDialog():
        MessageBox.Show("Not possible to execute the workflow without a model selecion or version specified", "Coordination workflow", MessageBoxButtons.OK, MessageBoxIcon.Warning)

#endregion

#region: execution

WorkflowForm().ShowDialog()

#endregion