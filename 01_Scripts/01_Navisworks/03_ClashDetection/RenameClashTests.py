#region references

import clr
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

clr.AddReference("Autodesk.Navisworks.Api")
from Autodesk.Navisworks.Api import *

clr.AddReference("Autodesk.Navisworks.ComApi")
from Autodesk.Navisworks.Api.ComApi import *

clr.AddReference("Autodesk.Navisworks.Interop.ComApi")
from Autodesk.Navisworks.Api.Interop.ComApi import *

clr.AddReference("Autodesk.Navisworks.Clash")
from Autodesk.Navisworks.Api.Clash import *

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import*
from System.Drawing import*

bundlePath = (Path.home()/ "AppData"/ "Roaming"/ "Autodesk"/ "ApplicationPlugins"/ "RAEN.Navisworks.PyNET.bundle"/ "Contents"/ "2024")
NavisworksinconPath = (Path.home()/ "AppData"/ "Roaming"/ "Autodesk"/ "ApplicationPlugins"/ "RAEN.Navisworks.PyNET.bundle"/ "Contents"/ "2024" / "Images" / "manage.ico")

sys.path.append(str(bundlePath))

clr.AddReference("Raen.Core.Pynet.Resources")

from Raen.Core.Pynet.Resources import CastUtils  # type: ignore

from Autodesk.Navisworks.Api import Application 
doc = Application.ActiveDocument

#endregion

class DialogManager:
    """
    Handles user-facing dialogs for clash test rename operations.
    """

    @staticmethod
    def NameUpdateDialog():
        MessageBox.Show(
            "Clash names updated with the especified prefix",
            "Update Clash names",
            MessageBoxButtons.OK,
            MessageBoxIcon.Information
        )

class ClashManager:
    """
    Renames all clash tests in the active document by adding a prefix to their display names.
    """

    @staticmethod
    def RenameTests():
        documentClashTests = CastUtils.CastTo[DocumentClash](doc.Clash).TestsData
        tests = documentClashTests.Value.TestsRoot.Children

        for test in tests:
            documentClashTests.TestsEditDisplayName(test, "PrefixTest_" + test.DisplayName)

        DialogManager.NameUpdateDialog()

ClashManager.RenameTests()