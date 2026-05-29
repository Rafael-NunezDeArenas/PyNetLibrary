# Auto-generated — Revit 2027 — Autodesk.Revit.DB.Macros

class AddInIdAttribute(Attribute):
    """.NET: Autodesk.Revit.DB.Macros.AddInIdAttribute"""
    def __init__(self, *args) -> None: ...
    Value: ValueType
    TypeId: object

class ApplicationEntryPoint(Application):
    """.NET: Autodesk.Revit.DB.Macros.ApplicationEntryPoint"""
    def __init__(self, *args) -> None: ...
    AddinFolder: str
    IsValidObject: bool
    AllowNavigationDuringRedraw: bool
    LoginUserId: str
    BackgroundColor: Color
    CurrentUsersAddinsDataFolderPath: str
    CurrentUsersDataFolderPath: str
    SharedComponentsLocation: str
    AllUsersAddinsLocation: str
    CurrentUserAddinsLocation: str
    ShortCurveTolerance: float
    CurrentRevitServerAccelerator: str
    IsInfrastructureEnabled: bool
    IsRouteAnalysisEnabled: bool
    IsPipingAnalysisEnabled: bool
    IsElectricalAnalysisEnabled: bool
    IsMechanicalAnalysisEnabled: bool
    IsPipingEnabled: bool
    IsElectricalEnabled: bool
    IsMechanicalEnabled: bool
    IsPrecastEnabled: bool
    IsStructuralAnalysisEnabled: bool
    IsEnergyAnalysisEnabled: bool
    IsMassingEnabled: bool
    IsSystemsEnabled: bool
    IsConcreteEnabled: bool
    IsStructureEnabled: bool
    IsArchitectureEnabled: bool
    AngleTolerance: float
    VertexTolerance: float
    DefaultViewDiscipline: ViewDiscipline
    ShowGraphicalWarningHangerDisconnects: bool
    ShowGraphicalOpenEndsAreaBasedLoadBoundaryDisconnects: bool
    ShowGraphicalWarningElectricalDisconnects: bool
    ShowGraphicalWarningCableTrayConduitDisconnects: bool
    ShowGraphicalWarningPipeDisconnects: bool
    ShowGraphicalWarningDuctDisconnects: bool
    ImportIFCCategoryTable: str
    ExportIFCCategoryTable: str
    DefaultIFCProjectTemplate: str
    DefaultProjectTemplate: str
    SystemsAnalysisWorkfilesRootPath: str
    PointCloudsRootPath: str
    FamilyTemplatePath: str
    SubVersionNumber: str
    Username: str
    ActiveAddInId: AddInId
    SharedParametersFilename: str
    Product: ProductType
    Language: LanguageType
    Cities: CitySet
    VersionBuild: str
    VersionNumber: str
    VersionName: str
    Create: Application
    RecordingJournalFilename: str
    Documents: DocumentSet
    def FinishInitializationEO(self, ) -> None: ...
    def Initialize(self, obj: object, addinFolder: str) -> None: ...
    def OnShutdownEO(self, ) -> None: ...

class IEntryPoint:
    """.NET: Autodesk.Revit.DB.Macros.IEntryPoint"""
    def __init__(self, *args) -> None: ...
    AddinFolder: str
    def FinishInitialization(self, ) -> None: ...
    def Initialize(self, obj: object, addinFolder: str) -> None: ...
    def OnShutdown(self, ) -> None: ...

class VendorIdAttribute(Attribute):
    """.NET: Autodesk.Revit.DB.Macros.VendorIdAttribute"""
    def __init__(self, *args) -> None: ...
    Value: str
    TypeId: object
