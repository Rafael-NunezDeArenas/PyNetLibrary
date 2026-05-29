# Auto-generated — Revit 2027 — Autodesk.Revit.DB.Mechanical

class AirCoolingCoilType:
    """.NET: Autodesk.Revit.DB.Mechanical.AirCoolingCoilType"""
    def __init__(self, *args) -> None: ...
    ...

class AirFanType:
    """.NET: Autodesk.Revit.DB.Mechanical.AirFanType"""
    def __init__(self, *args) -> None: ...
    ...

class AirHeatExchangerType:
    """.NET: Autodesk.Revit.DB.Mechanical.AirHeatExchangerType"""
    def __init__(self, *args) -> None: ...
    ...

class AirHeatingCoilType:
    """.NET: Autodesk.Revit.DB.Mechanical.AirHeatingCoilType"""
    def __init__(self, *args) -> None: ...
    ...

class AirSystemData:
    """.NET: Autodesk.Revit.DB.Mechanical.AirSystemData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    AirFanType: AirFanType
    ChilledWaterLoopId: ElementId
    CoolingCoilType: AirCoolingCoilType
    HeatingHotWaterLoopId: ElementId
    HeatingCoilType: AirHeatingCoilType
    PreheatHotWaterLoopId: ElementId
    PreheatCoilType: AirHeatingCoilType
    HeatExchangerType: AirHeatExchangerType
    def Dispose(self, ) -> None: ...

class AnalyticalSystemDomain:
    """.NET: Autodesk.Revit.DB.Mechanical.AnalyticalSystemDomain"""
    def __init__(self, *args) -> None: ...
    ...

class ComponentClassification:
    """.NET: Autodesk.Revit.DB.Mechanical.ComponentClassification"""
    def __init__(self, *args) -> None: ...
    ...

class ConditionType:
    """.NET: Autodesk.Revit.DB.Mechanical.ConditionType"""
    def __init__(self, *args) -> None: ...
    ...

class Duct(MEPCurve):
    """.NET: Autodesk.Revit.DB.Mechanical.Duct"""
    def __init__(self, *args) -> None: ...
    IsPlaceholder: bool
    DuctType: DuctType
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
    def Create(document: Document, systemTypeId: ElementId, ductTypeId: ElementId, levelId: ElementId, startPoint: XYZ, endPoint: XYZ) -> Duct: ...
    @staticmethod
    def CreatePlaceholder(document: Document, systemTypeId: ElementId, ductTypeId: ElementId, levelId: ElementId, startPoint: XYZ, endPoint: XYZ) -> Duct: ...
    @staticmethod
    def IsDuctTypeId(document: Document, ductTypeId: ElementId) -> bool: ...
    @staticmethod
    def IsHvacSystemTypeId(document: Document, systemTypeId: ElementId) -> bool: ...
    def SetSystemType(self, systemTypeId: ElementId) -> None: ...

class DuctFittingAndAccessoryConnectorData:
    """.NET: Autodesk.Revit.DB.Mechanical.DuctFittingAndAccessoryConnectorData"""
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

class DuctFittingAndAccessoryData:
    """.NET: Autodesk.Revit.DB.Mechanical.DuctFittingAndAccessoryData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Density: float
    DynamicViscosity: float
    Origin: XYZ
    SystemClassification: MEPSystemClassification
    PartType: PartType
    ServerGUID: Guid
    def Dispose(self, ) -> None: ...
    def GetAllConnectorData(self, ) -> IList: ...
    def GetEntity(self, ) -> Entity: ...
    def GetFamilyInstanceId(self, ) -> ElementId: ...

class DuctFittingAndAccessoryPressureDropData:
    """.NET: Autodesk.Revit.DB.Mechanical.DuctFittingAndAccessoryPressureDropData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsCurrentEntityValid: bool
    CalculationType: int
    def Dispose(self, ) -> None: ...
    def GetDuctFittingAndAccessoryData(self, ) -> DuctFittingAndAccessoryData: ...
    def GetPresureDropItems(self, ) -> IList: ...
    def SetDefaultEntity(self, defaultEntity: Entity) -> None: ...

class DuctFittingAndAccessoryPressureDropItem:
    """.NET: Autodesk.Revit.DB.Mechanical.DuctFittingAndAccessoryPressureDropItem"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Coefficient: float
    VelocityPressure: float
    EndConnectorIndex: int
    BeginConnectorIndex: int
    def Dispose(self, ) -> None: ...

class DuctFlowConfigurationType:
    """.NET: Autodesk.Revit.DB.Mechanical.DuctFlowConfigurationType"""
    def __init__(self, *args) -> None: ...
    ...

class DuctInsulation(InsulationLiningBase):
    """.NET: Autodesk.Revit.DB.Mechanical.DuctInsulation"""
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
    def Create(document: Document, ductOrContentElementId: ElementId, ductInsulationTypeId: ElementId, Thickness: float) -> DuctInsulation: ...

class DuctInsulationType(ElementType):
    """.NET: Autodesk.Revit.DB.Mechanical.DuctInsulationType"""
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

class DuctLining(InsulationLiningBase):
    """.NET: Autodesk.Revit.DB.Mechanical.DuctLining"""
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
    def Create(document: Document, ductOrContentElementId: ElementId, ductLiningTypeId: ElementId, Thickness: float) -> DuctLining: ...

class DuctLiningType(ElementType):
    """.NET: Autodesk.Revit.DB.Mechanical.DuctLiningType"""
    def __init__(self, *args) -> None: ...
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
    def IsValidRoughness(self, roughness: float) -> bool: ...

class DuctLossMethodType:
    """.NET: Autodesk.Revit.DB.Mechanical.DuctLossMethodType"""
    def __init__(self, *args) -> None: ...
    ...

class DuctPressureDropData:
    """.NET: Autodesk.Revit.DB.Mechanical.DuctPressureDropData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Coefficient: float
    PressureDrop: float
    Friction: float
    VelocityPressure: float
    Velocity: float
    ReynoldsNumber: float
    HydraulicDiameter: float
    Flow: float
    Roughness: float
    DynamicViscosity: float
    Density: float
    Length: float
    WidthOrDiameter: float
    Height: float
    CategoryId: ElementId
    Shape: ConnectorProfileType
    Level: SystemCalculationLevel
    def Dispose(self, ) -> None: ...

class DuctSettings(Element):
    """.NET: Autodesk.Revit.DB.Mechanical.DuctSettings"""
    def __init__(self, *args) -> None: ...
    NetworkBasedCalculations: bool
    UseAnnotationScaleForSingleLineFittings: bool
    FittingAngleUsage: FittingAngleUsage
    RiseDropAnnotationSize: float
    FittingAnnotationSize: float
    AirDynamicViscosity: float
    AirDensity: float
    Centerline: str
    SetDownFromBottom: str
    SetUpFromBottom: str
    SetDown: str
    SetUp: str
    FlatOnBottom: str
    FlatOnTop: str
    OvalDuctSizeSuffix: str
    OvalDuctSizeSeparator: str
    ConnectorSeparator: str
    RoundDuctSizePrefix: str
    RoundDuctSizeSuffix: str
    RectangularDuctSizeSuffix: str
    RectangularDuctSizeSeparator: str
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
    def GetDuctSettings(document: Document) -> DuctSettings: ...
    def GetPressLossCalculationServerInfo(self, ) -> MEPCalculationServerInfo: ...
    def GetSpecificFittingAngleStatus(self, angle: float) -> bool: ...
    def GetSpecificFittingAngles(self, ) -> IList: ...
    @staticmethod
    def IsNetworkBasedCalculationsEnabled(document: Document) -> bool: ...
    def IsValidSpecificFittingAngle(self, angle: float) -> bool: ...
    def SetPressLossCalculationServerInfo(self, serverInfo: MEPCalculationServerInfo) -> None: ...
    def SetSpecificFittingAngleStatus(self, angle: float, useInLayout: bool) -> None: ...

class DuctShape:
    """.NET: Autodesk.Revit.DB.Mechanical.DuctShape"""
    def __init__(self, *args) -> None: ...
    ...

class DuctSizeIterator:
    """.NET: Autodesk.Revit.DB.Mechanical.DuctSizeIterator"""
    def __init__(self, *args) -> None: ...
    Current: MEPSize
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetCurrent(self, ) -> MEPSize: ...
    def HasCurrent(self, ) -> bool: ...
    def IsDone(self, ) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class DuctSizeSettingIterator:
    """.NET: Autodesk.Revit.DB.Mechanical.DuctSizeSettingIterator"""
    def __init__(self, *args) -> None: ...
    Current: KeyValuePair
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def HasCurrent(self, ) -> bool: ...
    def IsDone(self, ) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class DuctSizeSettings(Element):
    """.NET: Autodesk.Revit.DB.Mechanical.DuctSizeSettings"""
    def __init__(self, *args) -> None: ...
    Item: DuctSizes
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
    def AddSize(self, shape: DuctShape, sizeInfo: MEPSize) -> None: ...
    def GetDuctSizeSettingIterator(self, ) -> DuctSizeSettingIterator: ...
    @staticmethod
    def GetDuctSizeSettings(aDoc: Document) -> DuctSizeSettings: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetSizeCount(self, shape: DuctShape) -> int: ...
    def RemoveSize(self, shape: DuctShape, nominalDiameter: float) -> None: ...

class DuctSizes:
    """.NET: Autodesk.Revit.DB.Mechanical.DuctSizes"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Count: int
    def Contains(self, nominalDiameter: float) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetDuctSizeIterator(self, ) -> DuctSizeIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...

class DuctSystemType:
    """.NET: Autodesk.Revit.DB.Mechanical.DuctSystemType"""
    def __init__(self, *args) -> None: ...
    ...

class DuctType(MEPCurveType):
    """.NET: Autodesk.Revit.DB.Mechanical.DuctType"""
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

class EquipmentClassification:
    """.NET: Autodesk.Revit.DB.Mechanical.EquipmentClassification"""
    def __init__(self, *args) -> None: ...
    ...

class FlexDuct(MEPCurve):
    """.NET: Autodesk.Revit.DB.Mechanical.FlexDuct"""
    def __init__(self, *args) -> None: ...
    EndTangent: XYZ
    StartTangent: XYZ
    FlexDuctType: FlexDuctType
    Points: IList
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
    def Create(document: Document, systemTypeId: ElementId, ductTypeId: ElementId, levelId: ElementId, startTangent: XYZ, endTangent: XYZ, points: IList) -> FlexDuct: ...
    @staticmethod
    def IsFlexDuctTypeId(document: Document, ductTypeId: ElementId) -> bool: ...
    @staticmethod
    def IsHVACSystemTypeId(document: Document, systemTypeId: ElementId) -> bool: ...

class FlexDuctType(MEPCurveType):
    """.NET: Autodesk.Revit.DB.Mechanical.FlexDuctType"""
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

class HVACZoneData(GenericZoneDomainData):
    """.NET: Autodesk.Revit.DB.Mechanical.HVACZoneData"""
    def __init__(self, *args) -> None: ...
    ZoneEquipmentId: ElementId
    IsValidObject: bool

class IDuctFittingAndAccessoryPressureDropServer:
    """.NET: Autodesk.Revit.DB.Mechanical.IDuctFittingAndAccessoryPressureDropServer"""
    def __init__(self, *args) -> None: ...
    def Calculate(self, data: DuctFittingAndAccessoryPressureDropData) -> bool: ...
    def GetDataSchema(self, ) -> Schema: ...
    def IsApplicable(self, data: DuctFittingAndAccessoryPressureDropData) -> bool: ...

class IDuctPressureDropServer:
    """.NET: Autodesk.Revit.DB.Mechanical.IDuctPressureDropServer"""
    def __init__(self, *args) -> None: ...
    def Calculate(self, data: DuctPressureDropData) -> None: ...
    def GetHtmlDescription(self, ) -> str: ...
    def GetInformationLink(self, ) -> str: ...

class MEPAnalyticalSystem(Element):
    """.NET: Autodesk.Revit.DB.Mechanical.MEPAnalyticalSystem"""
    def __init__(self, *args) -> None: ...
    AnalyticalSystemDomain: AnalyticalSystemDomain
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
    def Create(document: Document, domain: AnalyticalSystemDomain, name: str) -> MEPAnalyticalSystem: ...
    def GetAirSystemData(self, ) -> AirSystemData: ...
    def GetWaterLoopData(self, ) -> WaterLoopData: ...

class MEPBuildingConstruction(ElementType):
    """.NET: Autodesk.Revit.DB.Mechanical.MEPBuildingConstruction"""
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
    def GetBuildingConstruction(self, constructionType: ConstructionType) -> Construction: ...
    def GetBuildingConstructionOverride(self, constructionType: ConstructionType) -> bool: ...
    def GetConstructions(self, constructionType: ConstructionType) -> ICollection: ...
    def SetBuildingConstruction(self, constructionType: ConstructionType, buildingConstruction: Construction) -> None: ...
    def SetBuildingConstructionOverride(self, constructionType: ConstructionType, override: bool) -> None: ...

class MEPBuildingConstructionSet(APIObject):
    """.NET: Autodesk.Revit.DB.Mechanical.MEPBuildingConstructionSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: MEPBuildingConstruction) -> bool: ...
    def Erase(self, item: MEPBuildingConstruction) -> int: ...
    def ForwardIterator(self, ) -> MEPBuildingConstructionSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: MEPBuildingConstruction) -> bool: ...
    def ReverseIterator(self, ) -> MEPBuildingConstructionSetIterator: ...

class MEPBuildingConstructionSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.Mechanical.MEPBuildingConstructionSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class MEPHiddenLineSettings(Element):
    """.NET: Autodesk.Revit.DB.Mechanical.MEPHiddenLineSettings"""
    def __init__(self, *args) -> None: ...
    DrawHiddenLine: bool
    LineStyle: ElementId
    SingleLineGap: float
    OutsideGap: float
    InsideGap: float
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
    def GetMEPHiddenLineSettings(doc: Document) -> MEPHiddenLineSettings: ...

class MEPSection:
    """.NET: Autodesk.Revit.DB.Mechanical.MEPSection"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    FrictionFactor: float
    ReynoldsNumber: float
    TotalCurveLength: float
    TotalPressureLoss: float
    TotalCoefficient: float
    VelocityPressure: float
    Velocity: float
    Friction: float
    FixtureUnit: float
    Flow: float
    Roughness: float
    Number: int
    def Dispose(self, ) -> None: ...
    def GetCoefficient(self, elemId: ElementId) -> float: ...
    def GetElementIds(self, ) -> IList: ...
    def GetPressureDrop(self, elemId: ElementId) -> float: ...
    def GetSegmentLength(self, segmentId: ElementId) -> float: ...
    def IsMain(self, fittingId: ElementId) -> bool: ...

class MEPSpaceConstruction:
    """.NET: Autodesk.Revit.DB.Mechanical.MEPSpaceConstruction"""
    def __init__(self, *args) -> None: ...
    SpaceConstructions: MEPBuildingConstructionSet
    CurrentConstruction: MEPBuildingConstruction
    def DeleteConstruction(self, pCurrentConstruction: MEPBuildingConstruction) -> None: ...
    def DuplicateConstruction(self, pCurrentConstruction: MEPBuildingConstruction, pName: str) -> MEPBuildingConstruction: ...
    def NewConstruction(self, pName: str) -> MEPBuildingConstruction: ...

class MechanicalEquipment(MEPModel):
    """.NET: Autodesk.Revit.DB.Mechanical.MechanicalEquipment"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ConnectorManager: ConnectorManager
    IsReadOnly: bool

class MechanicalEquipmentSet(Element):
    """.NET: Autodesk.Revit.DB.Mechanical.MechanicalEquipmentSet"""
    def __init__(self, *args) -> None: ...
    OnStandby: int
    OnDuty: int
    Classification: EquipmentClassification
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
    def Add(self, elemIds: ISet) -> None: ...
    @staticmethod
    def AreElementsNotConnectedInSeries(document: Document, elemIds: ISet) -> bool: ...
    @staticmethod
    def AreValidMembers(document: Document, memberIds: ISet) -> bool: ...
    @staticmethod
    def Create(document: Document, typeId: ElementId, memberIds: ISet) -> MechanicalEquipmentSet: ...
    def GetMembers(self, ) -> ISet: ...
    def Remove(self, elemIds: ISet) -> None: ...

class MechanicalEquipmentSetType(ElementType):
    """.NET: Autodesk.Revit.DB.Mechanical.MechanicalEquipmentSetType"""
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
    def Create(document: Document, name: str) -> MechanicalEquipmentSetType: ...

class MechanicalFitting(MEPModel):
    """.NET: Autodesk.Revit.DB.Mechanical.MechanicalFitting"""
    def __init__(self, *args) -> None: ...
    PartType: PartType
    IsValidObject: bool
    ConnectorManager: ConnectorManager
    IsReadOnly: bool

class MechanicalSystem(MEPSystem):
    """.NET: Autodesk.Revit.DB.Mechanical.MechanicalSystem"""
    def __init__(self, *args) -> None: ...
    IsWellConnected: bool
    DuctNetwork: ElementSet
    BaseEquipmentConnector: Connector
    SystemType: DuctSystemType
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
    def Create(ADocument: Document, typeId: ElementId, name: str) -> MechanicalSystem: ...
    def GetFlow(self, ) -> float: ...
    def GetStaticPressure(self, ) -> float: ...
    def IsPressureDropServerMissing(self, ) -> bool: ...

class MechanicalSystemType(MEPSystemType):
    """.NET: Autodesk.Revit.DB.Mechanical.MechanicalSystemType"""
    def __init__(self, *args) -> None: ...
    RiseDropSettings: RiseDropSymbol
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
    def Create(ADoc: Document, systemClassification: MEPSystemClassification, name: str) -> MechanicalSystemType: ...
    def ValidateRiseDropSymbolType(self, risedropType: RiseDropSymbol) -> bool: ...

class MechanicalUtils:
    """.NET: Autodesk.Revit.DB.Mechanical.MechanicalUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def BreakCurve(document: Document, ductId: ElementId, ptBreak: XYZ) -> ElementId: ...
    @staticmethod
    def ConnectAirTerminalOnDuct(document: Document, airTerminalId: ElementId, ductCurveId: ElementId) -> bool: ...
    @staticmethod
    def ConnectDuctPlaceholdersAtCross(document: Document, connector1: Connector, connector2: Connector, connector3: Connector, connector4: Connector) -> bool: ...
    @staticmethod
    def ConnectDuctPlaceholdersAtElbow(document: Document, connector1: Connector, connector2: Connector) -> bool: ...
    @staticmethod
    def ConnectDuctPlaceholdersAtTee(document: Document, connector1: Connector, connector2: Connector, connector3: Connector) -> bool: ...
    @staticmethod
    def ConvertDuctPlaceholders(document: Document, placeholderIds: ICollection) -> ICollection: ...

class OccupancyUnit:
    """.NET: Autodesk.Revit.DB.Mechanical.OccupancyUnit"""
    def __init__(self, *args) -> None: ...
    ...

class ReturnAirflowType:
    """.NET: Autodesk.Revit.DB.Mechanical.ReturnAirflowType"""
    def __init__(self, *args) -> None: ...
    ...

class RiseDropSymbol:
    """.NET: Autodesk.Revit.DB.Mechanical.RiseDropSymbol"""
    def __init__(self, *args) -> None: ...
    ...

class Space(SpatialElement):
    """.NET: Autodesk.Revit.DB.Mechanical.Space"""
    def __init__(self, *args) -> None: ...
    Plenum: bool
    Occupiable: bool
    DesignPowerLoad: float
    ActualPowerLoad: float
    PowerLoadUnit: BaseLoadOn
    DesignLightingLoad: float
    ActualLightingLoad: float
    LightingLoadUnit: BaseLoadOn
    LatentHeatGainperPerson: float
    SensibleHeatGainperPerson: float
    AreaperPerson: float
    NumberofPeople: float
    BaseHeatLoadOn: BaseLoadOn
    OccupancyUnit: OccupancyUnit
    DesignCoolingLoad: float
    CalculatedCoolingLoad: float
    DesignHeatingLoad: float
    CalculatedHeatingLoad: float
    SpaceConstruction: MEPSpaceConstruction
    SpaceTypeId: ElementId
    SpaceType: SpaceType
    ConditionType: ConditionType
    Volume: float
    UnboundedHeight: float
    OutdoorAirFlowStandard: OutdoorAirFlowStandard
    OutdoorAirflow: float
    AirChangesPerHour: float
    OutdoorAirPerArea: float
    OutdoorAirPerPerson: float
    ActualExhaustAirflow: float
    DesignExhaustAirflow: float
    ActualReturnAirflow: float
    DesignReturnAirflow: float
    ReturnAirflow: ReturnAirflowType
    ActualSupplyAirflow: float
    CalculatedSupplyAirflow: float
    DesignSupplyAirflow: float
    ActualOtherLoad: float
    DesignOtherLoadperArea: float
    ActualHVACLoad: float
    DesignHVACLoadperArea: float
    FloorReflectance: float
    WallReflectance: float
    CeilingReflectance: float
    LightingCalculationWorkplane: float
    SpaceCavityRatio: float
    AverageEstimatedIllumination: float
    BaseOffset: float
    LimitOffset: float
    UpperLimit: Level
    Room: Room
    ClosedShell: GeometryElement
    Zone: Zone
    SpatialElementType: SpatialElementType
    Perimeter: float
    Area: float
    Location: Location
    Number: str
    Level: Level
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
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    def IsPointInSpace(self, point: XYZ) -> bool: ...

class SpaceFilter(ElementSlowFilter):
    """.NET: Autodesk.Revit.DB.Mechanical.SpaceFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool

class SpaceSet(APIObject):
    """.NET: Autodesk.Revit.DB.Mechanical.SpaceSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: Space) -> bool: ...
    def Erase(self, item: Space) -> int: ...
    def ForwardIterator(self, ) -> SpaceSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: Space) -> bool: ...
    def ReverseIterator(self, ) -> SpaceSetIterator: ...

class SpaceSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.Mechanical.SpaceSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class SpaceTag(SpatialElementTag):
    """.NET: Autodesk.Revit.DB.Mechanical.SpaceTag"""
    def __init__(self, *args) -> None: ...
    SpaceTagType: SpaceTagType
    Space: Space
    View: View
    LeaderStartCondition: LeaderStartCondition
    LeaderStart: XYZ
    LeaderElbow: XYZ
    LeaderEnd: XYZ
    TagHeadPosition: XYZ
    TagText: str
    RotationAngle: float
    TagOrientation: SpatialElementTagOrientation
    HasElbow: bool
    HasLeader: bool
    IsTaggingLink: bool
    IsOrphaned: bool
    Location: Location
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
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str

class SpaceTagFilter(ElementSlowFilter):
    """.NET: Autodesk.Revit.DB.Mechanical.SpaceTagFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool

class SpaceTagType(FamilySymbol):
    """.NET: Autodesk.Revit.DB.Mechanical.SpaceTagType"""
    def __init__(self, *args) -> None: ...
    Origin: XYZ
    IsActive: bool
    Family: Family
    StructuralMaterialType: StructuralMaterialType
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

class SpaceType:
    """.NET: Autodesk.Revit.DB.Mechanical.SpaceType"""
    def __init__(self, *args) -> None: ...
    ...

class SystemCalculationLevel:
    """.NET: Autodesk.Revit.DB.Mechanical.SystemCalculationLevel"""
    def __init__(self, *args) -> None: ...
    ...

class SystemZoneData(GenericZoneDomainData):
    """.NET: Autodesk.Revit.DB.Mechanical.SystemZoneData"""
    def __init__(self, *args) -> None: ...
    ZoneEquipmentId: ElementId
    IsValidObject: bool
    @staticmethod
    def Create() -> SystemZoneData: ...

class SystemZoneElementType(ElementType):
    """.NET: Autodesk.Revit.DB.Mechanical.SystemZoneElementType"""
    def __init__(self, *args) -> None: ...
    AirChangesPerHour: float
    OutdoorAirPerArea: float
    OutdoorAirPerPerson: float
    DehumidificationSetPoint: float
    HumidificationSetPoint: float
    UseDehumidificationSetPoint: bool
    UseHumidificationSetPoint: bool
    CoolingAirTemperature: float
    HeatingAirTemperature: float
    CoolingSetPoint: float
    HeatingSetPoint: float
    GeometricDefinition: ZoneGeometricDefinition
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
    def CreateSketchBased(doc: Document, name: str) -> SystemZoneElementType: ...
    @staticmethod
    def CreateSpaceBased(doc: Document, name: str) -> SystemZoneElementType: ...

class WaterChillerType:
    """.NET: Autodesk.Revit.DB.Mechanical.WaterChillerType"""
    def __init__(self, *args) -> None: ...
    ...

class WaterLoopData:
    """.NET: Autodesk.Revit.DB.Mechanical.WaterLoopData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    CondenserWaterLoopId: ElementId
    ChillerType: WaterChillerType
    WaterLoopType: WaterLoopType
    def Dispose(self, ) -> None: ...

class WaterLoopType:
    """.NET: Autodesk.Revit.DB.Mechanical.WaterLoopType"""
    def __init__(self, *args) -> None: ...
    ...

class Zone(Element):
    """.NET: Autodesk.Revit.DB.Mechanical.Zone"""
    def __init__(self, *args) -> None: ...
    Boundary: CurveArray
    Spaces: SpaceSet
    Area: float
    Phase: Phase
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
    def CreateAreaBasedLoad(doc: Document, name: str, levelId: ElementId, phaseId: ElementId) -> Zone: ...
    def GetDomainData(self, ) -> ZoneElementDomainData: ...

class ZoneElementDomainData:
    """.NET: Autodesk.Revit.DB.Mechanical.ZoneElementDomainData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class ZoneEquipment(Element):
    """.NET: Autodesk.Revit.DB.Mechanical.ZoneEquipment"""
    def __init__(self, *args) -> None: ...
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
    def Create(document: Document, name: str) -> ZoneEquipment: ...
    @staticmethod
    def GetAssociatedZoneEquipment(document: Document, spaces: ISet) -> ISet: ...
    def GetZoneEquipmentData(self, ) -> ZoneEquipmentData: ...
    @staticmethod
    def MoveSpaceToEquipment(document: Document, analyticalSpaceSet: ISet, originalZoneEquipmentId: ElementId, targetZoneEquipmentId: ElementId) -> None: ...

class ZoneEquipmentBehavior:
    """.NET: Autodesk.Revit.DB.Mechanical.ZoneEquipmentBehavior"""
    def __init__(self, *args) -> None: ...
    ...

class ZoneEquipmentData:
    """.NET: Autodesk.Revit.DB.Mechanical.ZoneEquipmentData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    AirSystemId: ElementId
    VRFLoopId: ElementId
    ChilledWaterLoopId: ElementId
    CondenserWaterLoopId: ElementId
    HotWaterLoopId: ElementId
    CoolingCoilType: AirCoolingCoilType
    HeatingCoilType: AirHeatingCoilType
    EquipmentBehavior: ZoneEquipmentBehavior
    EquipmentType: ZoneEquipmentHvacType
    def Dispose(self, ) -> None: ...
    def IsDataCompleted(self, ) -> bool: ...

class ZoneEquipmentHvacType:
    """.NET: Autodesk.Revit.DB.Mechanical.ZoneEquipmentHvacType"""
    def __init__(self, *args) -> None: ...
    ...
