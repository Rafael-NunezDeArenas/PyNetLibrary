# Auto-generated — Revit 2027 — Autodesk.Revit.DB.Plumbing

class FlexPipe(MEPCurve):
    """.NET: Autodesk.Revit.DB.Plumbing.FlexPipe"""
    def __init__(self, *args) -> None: ...
    EndTangent: XYZ
    StartTangent: XYZ
    Points: IList
    FlexPipeType: FlexPipeType
    FlowState: PipeFlowState
    MEPSystem: MEPSystem
    ReferenceLevel: Level
    LevelOffset: float
    Diameter: float
    Height: float
    Width: float
    ConnectorManager: ConnectorManager
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    @staticmethod
    def Create(document: Document, systemTypeId: ElementId, pipeTypeId: ElementId, levelId: ElementId, startTangent: XYZ, endTangent: XYZ, points: IList) -> FlexPipe: ...
    @staticmethod
    def IsFlexPipeTypeId(document: Document, pipeTypeId: ElementId) -> bool: ...
    @staticmethod
    def IsPipingSystemTypeId(document: Document, systemTypeId: ElementId) -> bool: ...

class FlexPipeType(MEPCurveType):
    """.NET: Autodesk.Revit.DB.Plumbing.FlexPipeType"""
    def __init__(self, *args) -> None: ...
    Shape: ConnectorProfileType
    RoutingPreferenceManager: RoutingPreferenceManager
    MultiShapeTransition: FamilySymbol
    Elbow: FamilySymbol
    Cross: FamilySymbol
    Union: FamilySymbol
    Transition: FamilySymbol
    Tap: FamilySymbol
    Tee: FamilySymbol
    PreferredJunctionType: JunctionType
    Roughness: float
    FamilyName: str
    CanBeDeleted: bool
    CanBeRenamed: bool
    CanBeCopied: bool
    Name: str
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category

class FlowConversionMode:
    """.NET: Autodesk.Revit.DB.Plumbing.FlowConversionMode"""
    def __init__(self, *args) -> None: ...
    ...

class FluidTemperature:
    """.NET: Autodesk.Revit.DB.Plumbing.FluidTemperature"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Density: float
    Viscosity: float
    Temperature: float
    def Dispose(self, ) -> None: ...

class FluidTemperatureSetIterator:
    """.NET: Autodesk.Revit.DB.Plumbing.FluidTemperatureSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: FluidTemperature
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetCurrent(self, ) -> FluidTemperature: ...
    def IsDone(self, ) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class FluidType(ElementType):
    """.NET: Autodesk.Revit.DB.Plumbing.FluidType"""
    def __init__(self, *args) -> None: ...
    FamilyName: str
    CanBeDeleted: bool
    CanBeRenamed: bool
    CanBeCopied: bool
    Name: str
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    def AddTemperature(self, fluidTemperature: FluidTemperature) -> None: ...
    def ClearAllTemperatures(self, ) -> None: ...
    @staticmethod
    def Create(document: Document, fluidTypeName: str, basedOnFluidType: FluidType) -> FluidType: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetFluidTemperatureSetIterator(self, ) -> FluidTemperatureSetIterator: ...
    @staticmethod
    def GetFluidType(document: Document, fluidTypeName: str) -> FluidType: ...
    def GetTemperature(self, temperature: float) -> FluidTemperature: ...
    @staticmethod
    def IsFluidInUse(document: Document, fluidId: ElementId) -> bool: ...
    def RemoveTemperature(self, temperature: float) -> None: ...

class IPipeFittingAndAccessoryPressureDropServer:
    """.NET: Autodesk.Revit.DB.Plumbing.IPipeFittingAndAccessoryPressureDropServer"""
    def __init__(self, *args) -> None: ...
    def Calculate(self, data: PipeFittingAndAccessoryPressureDropData) -> bool: ...
    def GetDataSchema(self, ) -> Schema: ...
    def IsApplicable(self, data: PipeFittingAndAccessoryPressureDropData) -> bool: ...

class IPipePlumbingFixtureFlowServer:
    """.NET: Autodesk.Revit.DB.Plumbing.IPipePlumbingFixtureFlowServer"""
    def __init__(self, *args) -> None: ...
    def Calculate(self, data: PipePlumbingFixtureFlowData) -> None: ...
    def GetHtmlDescription(self, ) -> str: ...
    def GetInformationLink(self, ) -> str: ...

class IPipePressureDropServer:
    """.NET: Autodesk.Revit.DB.Plumbing.IPipePressureDropServer"""
    def __init__(self, *args) -> None: ...
    def Calculate(self, data: PipePressureDropData) -> None: ...
    def GetHtmlDescription(self, ) -> str: ...
    def GetInformationLink(self, ) -> str: ...

class Pipe(MEPCurve):
    """.NET: Autodesk.Revit.DB.Plumbing.Pipe"""
    def __init__(self, *args) -> None: ...
    PipeSegment: PipeSegment
    IsPlaceholder: bool
    PipeType: PipeType
    FlowState: PipeFlowState
    MEPSystem: MEPSystem
    ReferenceLevel: Level
    LevelOffset: float
    Diameter: float
    Height: float
    Width: float
    ConnectorManager: ConnectorManager
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    @staticmethod
    def Create(document: Document, systemTypeId: ElementId, pipeTypeId: ElementId, levelId: ElementId, startPoint: XYZ, endPoint: XYZ) -> Pipe: ...
    @staticmethod
    def CreatePlaceholder(document: Document, systemTypeId: ElementId, pipeTypeId: ElementId, levelId: ElementId, startPoint: XYZ, endPoint: XYZ) -> Pipe: ...
    @staticmethod
    def IsPipeTypeId(document: Document, pipeTypeId: ElementId) -> bool: ...
    @staticmethod
    def IsPipingConnector(connector: Connector) -> bool: ...
    @staticmethod
    def IsPipingSystemTypeId(document: Document, systemTypeId: ElementId) -> bool: ...
    def SetSystemType(self, systemTypeId: ElementId) -> None: ...

class PipeFittingAndAccessoryConnectorData:
    """.NET: Autodesk.Revit.DB.Plumbing.PipeFittingAndAccessoryConnectorData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Profile: ConnectorProfileType
    VelocityPressure: float
    Flow: float
    FlowDirection: FlowDirectionType
    LinkIndex: int
    Index: int
    Angle: float
    Diameter: float
    Height: float
    Width: float
    def Dispose(self, ) -> None: ...
    def GetCoordination(self, ) -> Transform: ...

class PipeFittingAndAccessoryData:
    """.NET: Autodesk.Revit.DB.Plumbing.PipeFittingAndAccessoryData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    FluidDensity: float
    FluidViscosity: float
    Origin: XYZ
    SystemClassification: MEPSystemClassification
    BehaviorType: int
    PartType: PartType
    ServerGUID: Guid
    def Dispose(self, ) -> None: ...
    def GetAllConnectorData(self, ) -> IList: ...
    def GetEntity(self, ) -> Entity: ...
    def GetFamilyInstanceId(self, ) -> ElementId: ...

class PipeFittingAndAccessoryPressureDropData:
    """.NET: Autodesk.Revit.DB.Plumbing.PipeFittingAndAccessoryPressureDropData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsCurrentEntityValid: bool
    CalculationType: int
    def Dispose(self, ) -> None: ...
    def GetPipeFittingAndAccessoryData(self, ) -> PipeFittingAndAccessoryData: ...
    def GetPresureDropItems(self, ) -> IList: ...
    def SetDefaultEntity(self, defaultEntity: Entity) -> None: ...

class PipeFittingAndAccessoryPressureDropItem:
    """.NET: Autodesk.Revit.DB.Plumbing.PipeFittingAndAccessoryPressureDropItem"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Coefficient: float
    VelocityPressure: float
    EndConnectorIndex: int
    BeginConnectorIndex: int
    def Dispose(self, ) -> None: ...

class PipeFlowConfigurationType:
    """.NET: Autodesk.Revit.DB.Plumbing.PipeFlowConfigurationType"""
    def __init__(self, *args) -> None: ...
    ...

class PipeFlowState:
    """.NET: Autodesk.Revit.DB.Plumbing.PipeFlowState"""
    def __init__(self, *args) -> None: ...
    ...

class PipeInsulation(InsulationLiningBase):
    """.NET: Autodesk.Revit.DB.Plumbing.PipeInsulation"""
    def __init__(self, *args) -> None: ...
    HostElementId: ElementId
    Thickness: float
    MEPSystem: MEPSystem
    ReferenceLevel: Level
    LevelOffset: float
    Diameter: float
    Height: float
    Width: float
    ConnectorManager: ConnectorManager
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    @staticmethod
    def Create(document: Document, pipeOrContentElementId: ElementId, pipeInsulationTypeId: ElementId, Thickness: float) -> PipeInsulation: ...

class PipeInsulationType(ElementType):
    """.NET: Autodesk.Revit.DB.Plumbing.PipeInsulationType"""
    def __init__(self, *args) -> None: ...
    FamilyName: str
    CanBeDeleted: bool
    CanBeRenamed: bool
    CanBeCopied: bool
    Name: str
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category

class PipeLossMethodType:
    """.NET: Autodesk.Revit.DB.Plumbing.PipeLossMethodType"""
    def __init__(self, *args) -> None: ...
    ...

class PipePlumbingFixtureFlowData:
    """.NET: Autodesk.Revit.DB.Plumbing.PipePlumbingFixtureFlowData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    DimensionFlow: float
    FlowConversionMode: FlowConversionMode
    FixtureUnits: float
    FlowConfiguration: PipeFlowConfigurationType
    Flow: float
    def Dispose(self, ) -> None: ...

class PipePressureDropData:
    """.NET: Autodesk.Revit.DB.Plumbing.PipePressureDropData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    KLevel: SystemCalculationLevel
    CategoryId: ElementId
    Viscosity: float
    Density: float
    NominalDiameter: float
    OutsideDiameter: float
    InsideDiameter: float
    Flow: float
    Length: float
    Roughness: float
    PressureDrop: float
    Coefficient: float
    VelocityPressure: float
    Velocity: float
    FrictionFactor: float
    Friction: float
    FlowState: PipeFlowState
    ReynoldsNumber: float
    RelativeRoughness: float
    def Dispose(self, ) -> None: ...

class PipeScheduleType(ElementType):
    """.NET: Autodesk.Revit.DB.Plumbing.PipeScheduleType"""
    def __init__(self, *args) -> None: ...
    FamilyName: str
    CanBeDeleted: bool
    CanBeRenamed: bool
    CanBeCopied: bool
    Name: str
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    @staticmethod
    def Create(doc: Document, name: str) -> PipeScheduleType: ...
    @staticmethod
    def GetPipeScheduleId(doc: Document, name: str) -> ElementId: ...

class PipeSegment(Segment):
    """.NET: Autodesk.Revit.DB.Plumbing.PipeSegment"""
    def __init__(self, *args) -> None: ...
    ScheduleTypeId: ElementId
    SizeCount: int
    MaterialId: ElementId
    Roughness: float
    Description: str
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    @staticmethod
    def Create(ADocument: Document, MaterialId: ElementId, ScheduleId: ElementId, sizeSet: ICollection) -> PipeSegment: ...

class PipeSettings(Element):
    """.NET: Autodesk.Revit.DB.Plumbing.PipeSettings"""
    def __init__(self, *args) -> None: ...
    AnalysisForClosedLoopHydronicPipingNetworks: bool
    UseAnnotationScaleForSingleLineFittings: bool
    FittingAnnotationSize: float
    ConnectorTolerance: float
    ConnectorSeparator: str
    SizePrefix: str
    SizeSuffix: str
    FittingAngleUsage: FittingAngleUsage
    Centerline: str
    SetDownFromBottom: str
    SetUpFromBottom: str
    SetDown: str
    SetUp: str
    FlatOnBottom: str
    FlatOnTop: str
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    def AddPipeSlope(self, slope: float) -> None: ...
    def GetFlowConvertionServerInfo(self, ) -> MEPCalculationServerInfo: ...
    @staticmethod
    def GetPipeSettings(document: Document) -> PipeSettings: ...
    def GetPipeSlopes(self, ) -> IList: ...
    def GetSpecificFittingAngleStatus(self, angle: float) -> bool: ...
    def GetSpecificFittingAngles(self, ) -> IList: ...
    @staticmethod
    def IsAnalysisForClosedLoopHydronicPipingNetworksEnabled(ccda: Document) -> bool: ...
    def IsValidSpecificFittingAngle(self, angle: float) -> bool: ...
    def SetFlowConvertionServerInfo(self, serverInfo: MEPCalculationServerInfo) -> None: ...
    def SetPipeSlopes(self, slopes: IList) -> None: ...
    def SetSpecificFittingAngleStatus(self, angle: float, bStatus: bool) -> None: ...

class PipeSystemType:
    """.NET: Autodesk.Revit.DB.Plumbing.PipeSystemType"""
    def __init__(self, *args) -> None: ...
    ...

class PipeType(MEPCurveType):
    """.NET: Autodesk.Revit.DB.Plumbing.PipeType"""
    def __init__(self, *args) -> None: ...
    Shape: ConnectorProfileType
    RoutingPreferenceManager: RoutingPreferenceManager
    MultiShapeTransition: FamilySymbol
    Elbow: FamilySymbol
    Cross: FamilySymbol
    Union: FamilySymbol
    Transition: FamilySymbol
    Tap: FamilySymbol
    Tee: FamilySymbol
    PreferredJunctionType: JunctionType
    Roughness: float
    FamilyName: str
    CanBeDeleted: bool
    CanBeRenamed: bool
    CanBeCopied: bool
    Name: str
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category

class PipingSystem(MEPSystem):
    """.NET: Autodesk.Revit.DB.Plumbing.PipingSystem"""
    def __init__(self, *args) -> None: ...
    IsWellConnected: bool
    PipingNetwork: ElementSet
    BaseEquipmentConnector: Connector
    SystemType: PipeSystemType
    HasPlaceholders: bool
    HasDesignParts: bool
    HasFabricationParts: bool
    IsMultipleNetwork: bool
    PressureLossOfCriticalPath: float
    SectionsCount: int
    IsEmpty: bool
    IsValid: bool
    BaseEquipment: FamilyInstance
    Elements: ElementSet
    ConnectorManager: ConnectorManager
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    @staticmethod
    def CanBeHydraulicLoopBoundary(element: Element) -> bool: ...
    @staticmethod
    def Create(ADocument: Document, typeId: ElementId, name: str) -> PipingSystem: ...
    @staticmethod
    def CreateHydraulicSeparation(document: Document, pipeElementIds: ISet) -> ISet: ...
    @staticmethod
    def DeleteHydraulicSeparation(document: Document, pipeElementIds: ISet) -> None: ...
    def GetFixtureUnits(self, ) -> float: ...
    def GetFlow(self, ) -> float: ...
    def GetPumpSets(self, ) -> ISet: ...
    def GetStaticPressure(self, ) -> float: ...
    def GetVolume(self, ) -> float: ...
    def IsFlowServerMissing(self, ) -> bool: ...
    @staticmethod
    def IsHydraulicLoopBoundary(element: Element) -> bool: ...
    def IsPressureDropServerMissing(self, ) -> bool: ...

class PipingSystemType(MEPSystemType):
    """.NET: Autodesk.Revit.DB.Plumbing.PipingSystemType"""
    def __init__(self, *args) -> None: ...
    FluidType: ElementId
    FluidTemperature: float
    SingleLineJunctionDropType: RiseDropSymbol
    SingleLineJunctionRiseType: RiseDropSymbol
    SingleLineBendDropType: RiseDropSymbol
    SingleLineBendRiseType: RiseDropSymbol
    TwoLineDropType: RiseDropSymbol
    TwoLineRiseType: RiseDropSymbol
    FlowConversionMethod: FlowConversionMode
    CalculationLevel: SystemCalculationLevel
    MaterialId: ElementId
    FillVisible: bool
    FillPatternId: ElementId
    FillColor: Color
    LinePatternId: ElementId
    LineColor: Color
    LineWeight: int
    SystemClassification: MEPSystemClassification
    Abbreviation: str
    FamilyName: str
    CanBeDeleted: bool
    CanBeRenamed: bool
    CanBeCopied: bool
    Name: str
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    @staticmethod
    def Create(ADoc: Document, systemClassification: MEPSystemClassification, name: str) -> PipingSystemType: ...
    def ValidateRiseDropSymbolType(self, risedropType: RiseDropSymbol) -> bool: ...

class PlumbingUtils:
    """.NET: Autodesk.Revit.DB.Plumbing.PlumbingUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def BreakCurve(document: Document, pipeId: ElementId, ptBreak: XYZ) -> ElementId: ...
    @staticmethod
    def ConnectPipePlaceholdersAtCross(document: Document, connector1: Connector, connector2: Connector, connector3: Connector, connector4: Connector) -> bool: ...
    @staticmethod
    def ConnectPipePlaceholdersAtElbow(document: Document, connector1: Connector, connector2: Connector) -> bool: ...
    @staticmethod
    def ConnectPipePlaceholdersAtTee(document: Document, connector1: Connector, connector2: Connector, connector3: Connector) -> bool: ...
    @staticmethod
    def ConvertPipePlaceholders(document: Document, placeholderIds: ICollection) -> ICollection: ...
    @staticmethod
    def HasOpenConnector(document: Document, elemId: ElementId) -> bool: ...
    @staticmethod
    def PlaceCapOnOpenEnds(document: Document, elemId: ElementId, typeId: ElementId) -> None: ...
