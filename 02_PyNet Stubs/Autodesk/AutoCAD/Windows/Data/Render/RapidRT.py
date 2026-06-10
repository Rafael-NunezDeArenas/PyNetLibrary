# Auto-generated — Civil 26 — Autodesk.AutoCAD.Windows.Data.Render.RapidRT

class RenderData:
    """.NET: Autodesk.AutoCAD.Windows.Data.Render.RapidRT.RenderData"""
    def __init__(self, *args) -> None: ...
    IsViewportRender: bool
    IsRenderOK: bool
    IsRendering: bool
    IsIndeterminate: bool
    JobIndex: Nullable
    AbortFlag: bool
    OwningDocument: Document
    RenderStatistics: str
    RenderPreset: str
    OutputView: str
    OutputResolution: str
    OutputSize: str
    OutputFileName: str
    OutputImageFormat: str
    RenderTileImage: RenderImage
    RenderTime: int
    RenderLevel: int
    LevelProgress: float
    OverallProgress: float
    CurrentTileIndex: int
    def Dispose(self, ) -> None: ...
    def ReRender(self, ) -> None: ...

class RenderDataSet:
    """.NET: Autodesk.AutoCAD.Windows.Data.Render.RapidRT.RenderDataSet"""
    def __init__(self, *args) -> None: ...
    CurrentRenderData: RenderData
    RenderJobs: ObservableCollection
    Reactor: RenderDataReactorImp
    def Dispose(self, ) -> None: ...

class RenderEngine:
    """.NET: Autodesk.AutoCAD.Windows.Data.Render.RapidRT.RenderEngine"""
    def __init__(self, *args) -> None: ...
    CurrentRenderEnvironment: RenderEnvironment
    CurrentRenderExposure: RenderExposure
    IsViewportChanging: bool
    RenderDestination: int
    IsRendering: bool
    SkipGlobalUpdate: bool
    CurrentOutputFile: str
    OutputSaveEnabled: bool
    CurrentOutputSize: str
    CurrentRenderData: RenderData
    RenderDataMap: Dictionary
    def Dispose(self, ) -> None: ...
    def MakeRenderJobSettingsCurrent(self, doc: Document, jobIndex: int) -> None: ...
    def NotifyRenderEnd(self, doc: Document) -> None: ...
    def NotifyRenderStart(self, doc: Document, jobIndex: int) -> None: ...
    def RegisterDocument(self, doc: Document) -> None: ...
    def UnregisterDocument(self, doc: Document) -> None: ...

class RenderEnvironment:
    """.NET: Autodesk.AutoCAD.Windows.Data.Render.RapidRT.RenderEnvironment"""
    def __init__(self, *args) -> None: ...
    WhitePoint: Nullable
    Brightness: Nullable
    Exposure: Nullable
    DisplayImage: bool
    Rotation: float
    IBLImageName: str
    Enable: bool
    def Dispose(self, ) -> None: ...
    def SuppressDatabaseUpdate(self, newValue: bool) -> None: ...

class RenderExposure:
    """.NET: Autodesk.AutoCAD.Windows.Data.Render.RapidRT.RenderExposure"""
    def __init__(self, *args) -> None: ...
    IBLActive: bool
    WhitePoint: float
    Exposure: float
    Active: bool
    Type: ExposureType
    def Dispose(self, ) -> None: ...
    def InvalidateUI(self, ) -> None: ...
    def ResetDefault(self, ) -> None: ...

class RenderImage:
    """.NET: Autodesk.AutoCAD.Windows.Data.Render.RapidRT.RenderImage"""
    def __init__(self, *args) -> None: ...
    Image: Bitmap
    Height: int
    Width: int
    Left: int
    Top: int
    def Dispose(self, ) -> None: ...
