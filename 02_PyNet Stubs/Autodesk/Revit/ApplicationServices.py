# Auto-generated — Revit 2027 — Autodesk.Revit.ApplicationServices

class Application:
    """.NET: Autodesk.Revit.ApplicationServices.Application"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    AllowNavigationDuringRedraw: bool
    LoginUserId: str
    IsLoggedIn: bool
    BackgroundColor: Color
    CurrentUsersAddinsDataFolderPath: str
    CurrentUsersDataFolderPath: str
    SharedComponentsLocation: str
    AllUsersAddinsLocation: str
    CurrentUserAddinsLocation: str
    MinimumThickness: float
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
    def CopyModel(self, sourceModelPath: ModelPath, destFilePath: str, overwrite: bool) -> None: ...
    def Dispose(self, ) -> None: ...
    def ExtractPartAtomFromFamilyFile(self, familyFilePath: str, xmlFilePath: str) -> None: ...
    def GetAssets(self, assetType: AssetType) -> IList: ...
    def GetExtendedApiService(self, ) -> TService: ...
    @staticmethod
    def GetFailureDefinitionRegistry() -> FailureDefinitionRegistry: ...
    def GetLibraryPaths(self, ) -> IDictionary: ...
    def GetRevitServerNetworkHosts(self, ) -> IList: ...
    def GetSystemsAnalysisWorkflowNames(self, ) -> IList: ...
    def GetSystemsAnalysisWorkflows(self, ) -> IDictionary: ...
    def GetWorksharingCentralGUID(self, serverModelPath: ServerPath) -> Guid: ...
    def IsJournalPlaying(self, ) -> bool: ...
    @staticmethod
    def IsValidThickness(thickness: float) -> bool: ...
    def NewFamilyDocument(self, templateFileName: str) -> Document: ...
    def NewProjectDocument(self, unitSystem: UnitSystem) -> Document: ...
    def NewProjectTemplateDocument(self, templateFilename: str) -> Document: ...
    def OpenDocumentFile(self, modelPath: ModelPath, openOptions: OpenOptions, openFromCloudCallback: IOpenFromCloudCallback) -> Document: ...
    def OpenIFCDocument(self, fileName: str, importOptions: IFCImportOptions) -> Document: ...
    def OpenSharedParameterFile(self, ) -> DefinitionFile: ...
    def PurgeReleasedAPIObjects(self, ) -> None: ...
    @staticmethod
    def RegisterFailuresProcessor(processor: IFailuresProcessor) -> None: ...
    def SetLibraryPaths(self, paths: IDictionary) -> None: ...
    def SetSystemsAnalysisWorkflows(self, paths: IDictionary) -> None: ...
    def UpdateRenderAppearanceLibrary(self, ) -> None: ...
    def WriteJournalComment(self, comment: str, timeStamp: bool) -> None: ...

class ControlledApplication:
    """.NET: Autodesk.Revit.ApplicationServices.ControlledApplication"""
    def __init__(self, *args) -> None: ...
    ActiveAddInId: AddInId
    SharedParametersFilename: str
    Product: ProductType
    Language: LanguageType
    Cities: CitySet
    VersionBuild: str
    VersionNumber: str
    VersionName: str
    Create: Application
    SubVersionNumber: str
    CurrentUsersAddinsDataFolderPath: str
    CurrentUsersDataFolderPath: str
    SharedComponentsLocation: str
    AllUsersAddinsLocation: str
    CurrentUserAddinsLocation: str
    RecordingJournalFilename: str
    IsLateAddinLoading: bool
    def GetExtendedApiService(self, ) -> TService: ...
    @staticmethod
    def GetFailureDefinitionRegistry() -> FailureDefinitionRegistry: ...
    def GetLibraryPaths(self, ) -> IDictionary: ...
    def IsJournalPlaying(self, ) -> bool: ...
    def OpenSharedParameterFile(self, ) -> DefinitionFile: ...
    @staticmethod
    def RegisterFailuresProcessor(processor: IFailuresProcessor) -> None: ...
    def SetLibraryPaths(self, paths: IDictionary) -> None: ...
    def WriteJournalComment(self, comment: str, timeStamp: bool) -> None: ...

class LanguageType:
    """.NET: Autodesk.Revit.ApplicationServices.LanguageType"""
    def __init__(self, *args) -> None: ...
    ...

class ProductType:
    """.NET: Autodesk.Revit.ApplicationServices.ProductType"""
    def __init__(self, *args) -> None: ...
    ...
