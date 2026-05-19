import plotly.graph_objects as go
import plotly.io as pio
import clr
import sys
from pathlib import Path

bundlePath = (Path.home()/ "AppData"/ "Roaming"/ "Autodesk"/ "ApplicationPlugins"/ "RAEN.Navisworks.PyNET.bundle"/ "Contents"/ "2024")
sys.path.append(str(bundlePath))
clr.AddReference("Raen.Core.Pynet.Resources")
from Raen.Core.Pynet.Resources import CastUtils  # type: ignore

clr.AddReference("Autodesk.Navisworks.Api")
clr.AddReference("Autodesk.Navisworks.Clash")
from Autodesk.Navisworks.Api import Application
from Autodesk.Navisworks.Api.Clash import DocumentClash, ClashResult


class DataManager:
    """
    Collects new clash result counts from each test in the active document.
    """

    @staticmethod
    def CollectNewClashes(document):
        clashDoc = CastUtils.CastTo[DocumentClash](document.Clash)
        data = []
        for test in clashDoc.TestsData.Tests:
            new_count = 0
            for child in test.Children:
                result = CastUtils.CastTo[ClashResult](child)
                if result is not None and str(result.Status) == "New":
                    new_count += 1
            if new_count > 0:
                data.append({"name": test.DisplayName, "new": new_count})
        return data


class ChartManager:
    """
    Renders a pie chart of new clash interferences per test using Plotly.
    """

    @staticmethod
    def ShowPieChart(data):
        labels = [d["name"] for d in data]
        values = [d["new"] for d in data]
        total = sum(values)

        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=0,
            textinfo='label+percent+value',
            pull=[0.05] * len(values)
        )])

        fig.update_layout(
            title=dict(
                text=f"Interferencias Nuevas por Test de Clash — Total: {total}",
                font=dict(size=16),
                x=0.5
            ),
            legend=dict(orientation="h", yanchor="bottom", y=-0.3)
        )

        pio.show(fig)
        return total


class FeatureManager:
    """
    Entry point for generating a pie chart of new clash interferences.
    """

    @staticmethod
    def Run(document):
        data = DataManager.CollectNewClashes(document)
        if data:
            total = ChartManager.ShowPieChart(data)
            return {"status": "Grafico mostrado", "total_new": total}
        return {"status": "No hay interferencias nuevas"}


# Entry point
doc = Application.ActiveDocument
ia_Result = FeatureManager.Run(doc)
