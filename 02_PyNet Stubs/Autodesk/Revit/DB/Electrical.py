# Auto-generated — Revit 2027 — Autodesk.Revit.DB.Electrical

class AnalyticalBusData(AnalyticalPowerDistributableNodeData):
    """.NET: Autodesk.Revit.DB.Electrical.AnalyticalBusData"""
    def __init__(self, *args) -> None: ...
    TotalConnectedCurrent: float
    CurrentRating: float
    AssignedPhasesNumber: int
    AssignedVoltage: float
    DistributionSystem: ElementId
    IsValidObject: bool
    ConnectedPhases: ElectricalConnectedPhases

class AnalyticalDistributionNodePropertyData:
    """.NET: Autodesk.Revit.DB.Electrical.AnalyticalDistributionNodePropertyData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ConnectedPhases: ElectricalConnectedPhases
    def Dispose(self, ) -> None: ...

class AnalyticalEquipmentLoadData(AnalyticalDistributionNodePropertyData):
    """.NET: Autodesk.Revit.DB.Electrical.AnalyticalEquipmentLoadData"""
    def __init__(self, *args) -> None: ...
    LoadType: ElectricalLoadType
    TrueLoad: float
    PowerFactor: float
    Current: float
    PhasesNumber: int
    Voltage: float
    ApparentLoad: float
    LoadSet: ElementId
    LoadClassification: ElementId
    PowerFactorState: PowerFactorStateType
    IsValidObject: bool
    ConnectedPhases: ElectricalConnectedPhases

class AnalyticalPowerDistributableNodeData(AnalyticalDistributionNodePropertyData):
    """.NET: Autodesk.Revit.DB.Electrical.AnalyticalPowerDistributableNodeData"""
    def __init__(self, *args) -> None: ...
    AssignedPhasesNumber: int
    AssignedVoltage: float
    DistributionSystem: ElementId
    IsValidObject: bool
    ConnectedPhases: ElectricalConnectedPhases
    def GetAllAvailableConnectedPhasesOnDownstream(self, id: ElementId) -> IList: ...
    def GetApparentPerPhaseResults(self, ) -> ElectricalPerPhaseData: ...
    def GetConnectedPhasesOnDownstream(self, id: ElementId) -> ElectricalConnectedPhases: ...
    def GetDemandPerPhaseResults(self, ) -> ElectricalPerPhaseData: ...
    def SetConnectedPhasesOnDownstream(self, id: ElementId, connectedPhases: ElectricalConnectedPhases) -> None: ...

class AnalyticalPowerSourceData(AnalyticalPowerDistributableNodeData):
    """.NET: Autodesk.Revit.DB.Electrical.AnalyticalPowerSourceData"""
    def __init__(self, *args) -> None: ...
    TotalConnectedCurrent: float
    ApparentPowerRating: float
    AssignedPhasesNumber: int
    AssignedVoltage: float
    DistributionSystem: ElementId
    IsValidObject: bool
    ConnectedPhases: ElectricalConnectedPhases

class AnalyticalTransferSwitchData(AnalyticalPowerDistributableNodeData):
    """.NET: Autodesk.Revit.DB.Electrical.AnalyticalTransferSwitchData"""
    def __init__(self, *args) -> None: ...
    TotalConnectedCurrent: float
    CurrentRating: float
    AssignedPhasesNumber: int
    AssignedVoltage: float
    DistributionSystem: ElementId
    IsValidObject: bool
    ConnectedPhases: ElectricalConnectedPhases

class AnalyticalTransformerData(AnalyticalPowerDistributableNodeData):
    """.NET: Autodesk.Revit.DB.Electrical.AnalyticalTransformerData"""
    def __init__(self, *args) -> None: ...
    ApparentPowerRating: float
    SecondaryDistributionSystem: ElementId
    AssignedPhasesNumber: int
    AssignedVoltage: float
    DistributionSystem: ElementId
    IsValidObject: bool
    ConnectedPhases: ElectricalConnectedPhases

class AreaBasedLoadBoundaryLineData:
    """.NET: Autodesk.Revit.DB.Electrical.AreaBasedLoadBoundaryLineData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    TopLevelId: ElementId
    BottomLevelId: ElementId
    def Dispose(self, ) -> None: ...
    def GetLevelIdsInRange(self, ) -> ISet: ...
    def IsElevationWithinRange(self, elev: float) -> bool: ...
    def IsLevelWithinRange(self, levelId: ElementId) -> bool: ...

class AreaBasedLoadData(ZoneElementDomainData):
    """.NET: Autodesk.Revit.DB.Electrical.AreaBasedLoadData"""
    def __init__(self, *args) -> None: ...
    Current: float
    Voltage: float
    ApparentPowerDensity: float
    LoadType: ElectricalLoadType
    ApparentLoad: float
    PowerFactorState: PowerFactorStateType
    PowerFactor: float
    TrueLoad: float
    LoadClassification: ElementId
    LoadDensity: float
    AreaBasedLoadType: ElementId
    PhasesNumber: int
    ConnectedPhases: ElectricalConnectedPhases
    IsValidObject: bool
    def AddElectricalLoadArea(self, electricalLoadAreaId: ElementId) -> None: ...
    def CanConnectToUpstreamNode(self, upstreamNodeId: ElementId) -> bool: ...
    def CanDisconnectFromUpstreamNode(self, ) -> bool: ...
    def ConnectToUpstreamNode(self, upstreamNodeId: ElementId) -> None: ...
    def DisconnectFromUpstreamNode(self, ) -> None: ...
    def GetElectricalLoadAreas(self, ) -> ISet: ...
    def GetUpstreamNodeId(self, ) -> ElementId: ...
    def RemoveElectricalLoadArea(self, electricalLoadAreaId: ElementId) -> None: ...

class AreaBasedLoadType(Element):
    """.NET: Autodesk.Revit.DB.Electrical.AreaBasedLoadType"""
    def __init__(self, *args) -> None: ...
    LoadClassification: ElementId
    LoadDensity: float
    ApparentPowerDensity: float
    PowerFactor: float
    PowerFactorState: PowerFactorStateType
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
    def Create(document: Document, name: str) -> AreaBasedLoadType: ...

class CableSize:
    """.NET: Autodesk.Revit.DB.Electrical.CableSize"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Name: str
    Id: ElementId
    Comments: str
    NumberOfOtherConductors: int
    OtherConductorSize: ElementId
    NumberOfGroundConductors: int
    GroundConductorSize: ElementId
    NumberOfNeutralConductors: int
    NeutralConductorSize: ElementId
    NumberOfHotConductors: int
    HotConductorSize: ElementId
    @staticmethod
    def Create(document: Document) -> CableSize: ...
    def Dispose(self, ) -> None: ...
    def Duplicate(self, ) -> CableSize: ...
    @staticmethod
    def GetCableSize(document: Document, cableSizeId: ElementId) -> CableSize: ...
    @staticmethod
    def GetCableSizeIdByName(document: Document, name: str) -> ElementId: ...
    @staticmethod
    def GetCableSizeIds(document: Document) -> IList: ...

class CableTray(CableTrayConduitBase):
    """.NET: Autodesk.Revit.DB.Electrical.CableTray"""
    def __init__(self, *args) -> None: ...
    CurveNormal: XYZ
    RungSpace: float
    RunId: ElementId
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
    def Create(document: Document, cabletrayType: ElementId, startPoint: XYZ, endPoint: XYZ, levelId: ElementId) -> CableTray: ...
    def GetShapeType(self, ) -> CableTrayShape: ...
    @staticmethod
    def IsValidCableTrayType(document: Document, cabletrayType: ElementId) -> bool: ...
    def IsValidRungSpace(self, rungSpace: float) -> bool: ...

class CableTrayConduitBase(MEPCurve):
    """.NET: Autodesk.Revit.DB.Electrical.CableTrayConduitBase"""
    def __init__(self, *args) -> None: ...
    RunId: ElementId
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
    def IsValidEndPoints(startPoint: XYZ, endPoint: XYZ) -> bool: ...
    @staticmethod
    def IsValidLevelId(document: Document, levelId: ElementId) -> bool: ...
    def IsWithFitting(self, ) -> bool: ...

class CableTrayConduitRunBase(Element):
    """.NET: Autodesk.Revit.DB.Electrical.CableTrayConduitRunBase"""
    def __init__(self, *args) -> None: ...
    Length: float
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

class CableTrayRun(CableTrayConduitRunBase):
    """.NET: Autodesk.Revit.DB.Electrical.CableTrayRun"""
    def __init__(self, *args) -> None: ...
    Length: float
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

class CableTraySettings(Element):
    """.NET: Autodesk.Revit.DB.Electrical.CableTraySettings"""
    def __init__(self, *args) -> None: ...
    UseAnnotationScaleForSingleLineFittings: bool
    RiseDropAnnotationSize: float
    FittingAnnotationSize: float
    ConnectorSeparator: str
    SizeSuffix: str
    SizeSeparator: str
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
    def GetCableTraySettings(document: Document) -> CableTraySettings: ...

class CableTrayShape:
    """.NET: Autodesk.Revit.DB.Electrical.CableTrayShape"""
    def __init__(self, *args) -> None: ...
    ...

class CableTraySizeIterator:
    """.NET: Autodesk.Revit.DB.Electrical.CableTraySizeIterator"""
    def __init__(self, *args) -> None: ...
    Current: MEPSize
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetCurrent(self, ) -> MEPSize: ...
    def HasCurrent(self, ) -> bool: ...
    def IsDone(self, ) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class CableTraySizes(Element):
    """.NET: Autodesk.Revit.DB.Electrical.CableTraySizes"""
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
    def AddSize(self, sizeInfo: MEPSize) -> None: ...
    def ClearAll(self, ) -> None: ...
    def Contains(self, nominalDiameter: float) -> bool: ...
    @staticmethod
    def GetCableTraySizes(aDoc: Document) -> CableTraySizes: ...
    def GetCableTraySizesIterator(self, ) -> CableTraySizeIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetSizeCount(self, ) -> int: ...
    def RemoveSize(self, sizeInfo: MEPSize) -> None: ...

class CableTrayType(MEPCurveType):
    """.NET: Autodesk.Revit.DB.Electrical.CableTrayType"""
    def __init__(self, *args) -> None: ...
    IsWithFitting: bool
    ShapeType: CableTrayShape
    BendMultiplier: float
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
    def IsValidBendMultiplier(self, bendMultiplier: float) -> bool: ...

class CableType(ElementType):
    """.NET: Autodesk.Revit.DB.Electrical.CableType"""
    def __init__(self, *args) -> None: ...
    CoreType: CoreType
    InsulationMaterial: ElementId
    ConductorMaterial: ElementId
    TemperatureRating: ElementId
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
    def Create(document: Document) -> CableType: ...
    def Duplicate(self, ) -> CableType: ...
    @staticmethod
    def GetCableTypeId(document: Document, name: str) -> ElementId: ...
    @staticmethod
    def GetCableTypeIds(document: Document) -> IList: ...
    def GetUsableCableSizeIds(self, ) -> IList: ...
    def IsCableSizeUsable(self, cableSizeId: ElementId) -> bool: ...
    def SetCableSizeUsable(self, cableSizeId: ElementId, usable: bool) -> None: ...

class CapitalizationForLoadNames:
    """.NET: Autodesk.Revit.DB.Electrical.CapitalizationForLoadNames"""
    def __init__(self, *args) -> None: ...
    ...

class CircuitConnectionType:
    """.NET: Autodesk.Revit.DB.Electrical.CircuitConnectionType"""
    def __init__(self, *args) -> None: ...
    ...

class CircuitLoadCalculationMethod:
    """.NET: Autodesk.Revit.DB.Electrical.CircuitLoadCalculationMethod"""
    def __init__(self, *args) -> None: ...
    ...

class CircuitNaming:
    """.NET: Autodesk.Revit.DB.Electrical.CircuitNaming"""
    def __init__(self, *args) -> None: ...
    ...

class CircuitNamingScheme(Element):
    """.NET: Autodesk.Revit.DB.Electrical.CircuitNamingScheme"""
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
    def Create(document: Document, name: str, data: IList) -> CircuitNamingScheme: ...
    def GetCombinedParameters(self, ) -> IList: ...
    @staticmethod
    def IsNameUnique(aDocument: Document, name: str) -> bool: ...
    @staticmethod
    def IsValidCombinedParameters(aDocument: Document, data: IList) -> bool: ...
    def SetCombinedParameters(self, data: IList) -> None: ...

class CircuitNamingSchemeSettings(Element):
    """.NET: Autodesk.Revit.DB.Electrical.CircuitNamingSchemeSettings"""
    def __init__(self, *args) -> None: ...
    CircuitNamingSchemeId: ElementId
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
    def GetCircuitNamingSchemeSettings(cda: Document) -> CircuitNamingSchemeSettings: ...
    @staticmethod
    def IsValidCircuitNamingSchemeId(aDocument: Document, circuitNamingSchemeId: ElementId) -> bool: ...

class CircuitNumberingOption:
    """.NET: Autodesk.Revit.DB.Electrical.CircuitNumberingOption"""
    def __init__(self, *args) -> None: ...
    ...

class CircuitSequence:
    """.NET: Autodesk.Revit.DB.Electrical.CircuitSequence"""
    def __init__(self, *args) -> None: ...
    ...

class CircuitType:
    """.NET: Autodesk.Revit.DB.Electrical.CircuitType"""
    def __init__(self, *args) -> None: ...
    ...

class ConductorMaterial:
    """.NET: Autodesk.Revit.DB.Electrical.ConductorMaterial"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Name: str
    Id: ElementId
    @staticmethod
    def Create(document: Document) -> ConductorMaterial: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetConductorMaterial(document: Document, conductorMaterialId: ElementId) -> ConductorMaterial: ...
    @staticmethod
    def GetConductorMaterialIdByName(document: Document, name: str) -> ElementId: ...
    @staticmethod
    def GetConductorMaterialIds(document: Document) -> IList: ...

class ConductorSize:
    """.NET: Autodesk.Revit.DB.Electrical.ConductorSize"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Name: str
    Id: ElementId
    Diameter: float
    @staticmethod
    def Create(document: Document) -> ConductorSize: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetConductorSize(document: Document, conductorSizeId: ElementId) -> ConductorSize: ...
    @staticmethod
    def GetConductorSizeIdByName(document: Document, name: str) -> ElementId: ...
    @staticmethod
    def GetConductorSizeIds(document: Document) -> IList: ...

class Conduit(CableTrayConduitBase):
    """.NET: Autodesk.Revit.DB.Electrical.Conduit"""
    def __init__(self, *args) -> None: ...
    RunId: ElementId
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
    def Create(document: Document, conduitType: ElementId, startPoint: XYZ, endPoint: XYZ, levelId: ElementId) -> Conduit: ...
    @staticmethod
    def IsValidConduitType(document: Document, conduitType: ElementId) -> bool: ...

class ConduitRun(CableTrayConduitRunBase):
    """.NET: Autodesk.Revit.DB.Electrical.ConduitRun"""
    def __init__(self, *args) -> None: ...
    Length: float
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

class ConduitSettings(Element):
    """.NET: Autodesk.Revit.DB.Electrical.ConduitSettings"""
    def __init__(self, *args) -> None: ...
    UseAnnotationScaleForSingleLineFittings: bool
    RiseDropAnnotationSize: float
    FittingAnnotationSize: float
    ConnectorSeparator: str
    SizePrefix: str
    SizeSuffix: str
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
    def GetConduitSettings(document: Document) -> ConduitSettings: ...

class ConduitSize:
    """.NET: Autodesk.Revit.DB.Electrical.ConduitSize"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    UsedInSizing: bool
    UsedInSizeLists: bool
    BendRadius: float
    OuterDiameter: float
    InnerDiameter: float
    NominalDiameter: float
    def Dispose(self, ) -> None: ...

class ConduitSizeIterator:
    """.NET: Autodesk.Revit.DB.Electrical.ConduitSizeIterator"""
    def __init__(self, *args) -> None: ...
    Current: ConduitSize
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetCurrent(self, ) -> ConduitSize: ...
    def HasCurrent(self, ) -> bool: ...
    def IsDone(self, ) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ConduitSizeSettingIterator:
    """.NET: Autodesk.Revit.DB.Electrical.ConduitSizeSettingIterator"""
    def __init__(self, *args) -> None: ...
    Current: KeyValuePair
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def HasCurrent(self, ) -> bool: ...
    def IsDone(self, ) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ConduitSizeSettings(Element):
    """.NET: Autodesk.Revit.DB.Electrical.ConduitSizeSettings"""
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
    def AddSize(self, standardName: str, sizeInfo: ConduitSize) -> None: ...
    def CreateConduitStandardTypeFromExisingStandardType(self, pADoc: Document, newStandardName: str, existingStandardName: str) -> bool: ...
    def DoesConduitStandardTypeExist(self, standardName: str) -> bool: ...
    @staticmethod
    def GetConduitSizeSettings(aDoc: Document) -> ConduitSizeSettings: ...
    def GetConduitSizeSettingsIterator(self, ) -> ConduitSizeSettingIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetSizeCount(self, standardName: str) -> int: ...
    def RemoveConduitStandardType(self, pADoc: Document, standardName: str) -> bool: ...
    def RemoveSize(self, standardName: str, nominalDiameter: float) -> None: ...

class ConduitSizes:
    """.NET: Autodesk.Revit.DB.Electrical.ConduitSizes"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Count: int
    def Contains(self, nominalDiameter: float) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetConduitSizesIterator(self, ) -> ConduitSizeIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...

class ConduitType(MEPCurveType):
    """.NET: Autodesk.Revit.DB.Electrical.ConduitType"""
    def __init__(self, *args) -> None: ...
    IsWithFitting: bool
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

class CoreType:
    """.NET: Autodesk.Revit.DB.Electrical.CoreType"""
    def __init__(self, *args) -> None: ...
    ...

class DistributionSysType(ElementType):
    """.NET: Autodesk.Revit.DB.Electrical.DistributionSysType"""
    def __init__(self, *args) -> None: ...
    HighLegPhase: ElectricalPhaseLine
    IsInUse: bool
    VoltageLineToGround: VoltageType
    VoltageLineToLine: VoltageType
    NumWires: int
    ElectricalPhase: ElectricalPhase
    ElectricalPhaseConfiguration: ElectricalPhaseConfiguration
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

class DistributionSysTypeSet(APIObject):
    """.NET: Autodesk.Revit.DB.Electrical.DistributionSysTypeSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: DistributionSysType) -> bool: ...
    def Erase(self, item: DistributionSysType) -> int: ...
    def ForwardIterator(self, ) -> DistributionSysTypeSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: DistributionSysType) -> bool: ...
    def ReverseIterator(self, ) -> DistributionSysTypeSetIterator: ...

class DistributionSysTypeSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.Electrical.DistributionSysTypeSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ElectricalAnalyticalLoadSet(Element):
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalAnalyticalLoadSet"""
    def __init__(self, *args) -> None: ...
    TotalQuantity: int
    QuantityOnStandBy: int
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
    def Create(document: Document, name: str) -> ElectricalAnalyticalLoadSet: ...
    def GetLoadIds(self, ) -> ISet: ...

class ElectricalAnalyticalNode(Element):
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalAnalyticalNode"""
    def __init__(self, *args) -> None: ...
    TotalLoad: float
    NodeType: ElectricalAnalyticalNodeType
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
    def CanConnectToUpstreamNode(self, upstreamNodeId: ElementId) -> bool: ...
    def CanDisconnectFromUpstreamNode(self, upstreamNodeId: ElementId) -> bool: ...
    def ConnectToUpstreamNode(self, upstreamNodeId: ElementId) -> None: ...
    @staticmethod
    def Create(document: Document, type: ElectricalAnalyticalNodeType, name: str) -> ElectricalAnalyticalNode: ...
    def DisconnectFromUpstreamNode(self, upstreamNodeId: ElementId) -> None: ...
    def GetAllDownstreamLoadIds(self, ) -> ISet: ...
    def GetAnalyticalPropertyData(self, ) -> AnalyticalDistributionNodePropertyData: ...
    def GetDownstreamNodeIds(self, ) -> IList: ...
    def GetUpstreamNodeIds(self, ) -> IList: ...

class ElectricalAnalyticalNodeType:
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalAnalyticalNodeType"""
    def __init__(self, *args) -> None: ...
    ...

class ElectricalCircuitPathMode:
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalCircuitPathMode"""
    def __init__(self, *args) -> None: ...
    ...

class ElectricalConnectedPhases:
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalConnectedPhases"""
    def __init__(self, *args) -> None: ...
    ...

class ElectricalDemandFactorDefinition(Element):
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalDemandFactorDefinition"""
    def __init__(self, *args) -> None: ...
    IncludeAdditionalLoad: bool
    RuleType: ElectricalDemandFactorRule
    AdditionalLoad: float
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
    def AddValue(self, dfValue: ElectricalDemandFactorValue) -> None: ...
    def ClearValues(self, ) -> None: ...
    @staticmethod
    def Create(ADoc: Document, strName: str) -> ElectricalDemandFactorDefinition: ...
    def GetApplicableDemandFactor(self, numberOrLoad: float) -> float: ...
    def GetValues(self, ) -> ICollection: ...
    def GetValuesCount(self, ) -> int: ...
    def RemoveValue(self, dfValue: ElectricalDemandFactorValue) -> None: ...
    def SetValues(self, values: ICollection) -> None: ...

class ElectricalDemandFactorRule:
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalDemandFactorRule"""
    def __init__(self, *args) -> None: ...
    ...

class ElectricalDemandFactorValue:
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalDemandFactorValue"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    MaxRange: float
    MinRange: float
    Factor: float
    def Dispose(self, ) -> None: ...
    def SetMaxRangeToUnlimited(self, ) -> None: ...

class ElectricalEquipment(MEPModel):
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalEquipment"""
    def __init__(self, *args) -> None: ...
    IsSwitchboard: bool
    MaxNumberOfCircuits: int
    CircuitNamingSchemeId: ElementId
    DistributionSystem: DistributionSysType
    IsValidObject: bool
    ConnectorManager: ConnectorManager
    IsReadOnly: bool
    def GetCircuitNamingSchemeType(self, ) -> CircuitNaming: ...
    @staticmethod
    def IsValidCircuitNamingSchemeId(aDocument: Document, circuitNamingSchemeId: ElementId) -> bool: ...
    def IsValidDistributionSystem(self, distributionSystem: DistributionSysType) -> bool: ...
    def SetCircuitNamingSchemeType(self, circuitNamingType: CircuitNaming) -> None: ...

class ElectricalLoadAreaData(SpatialElementDomainData):
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalLoadAreaData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    @staticmethod
    def CreateElectricalLoadAreas(doc: Document, levelId: ElementId, phaseId: ElementId) -> ISet: ...
    def GetAreaBasedLoadIds(self, ) -> ISet: ...
    @staticmethod
    def HasCircuitsWithoutElectricalLoadAreas(doc: Document, levelId: ElementId, phaseId: ElementId) -> bool: ...

class ElectricalLoadClassification(Element):
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalLoadClassification"""
    def __init__(self, *args) -> None: ...
    Spare: bool
    Other: bool
    Motor: bool
    Abbreviation: str
    ActualElectricalLoadLabel: str
    PanelEstimatedCurrentLabel: str
    PanelConnectedCurrentLabel: str
    PanelEstimatedLabel: str
    PanelConnectedLabel: str
    LoadSummaryDemandFactorLabel: str
    SpaceLoadClass: ElectricalLoadClassificationSpace
    DemandFactorId: ElementId
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
    def Create(ADoc: Document, strName: str) -> ElectricalLoadClassification: ...

class ElectricalLoadClassificationData:
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalLoadClassificationData"""
    def __init__(self, *args) -> None: ...
    ...

class ElectricalLoadClassificationSpace:
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalLoadClassificationSpace"""
    def __init__(self, *args) -> None: ...
    ...

class ElectricalLoadType:
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalLoadType"""
    def __init__(self, *args) -> None: ...
    ...

class ElectricalPerPhaseData:
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalPerPhaseData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    CurrentPhaseC: float
    CurrentPhaseB: float
    CurrentPhaseA: float
    def Dispose(self, ) -> None: ...

class ElectricalPhase:
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalPhase"""
    def __init__(self, *args) -> None: ...
    ...

class ElectricalPhaseConfiguration:
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalPhaseConfiguration"""
    def __init__(self, *args) -> None: ...
    ...

class ElectricalPhaseLine:
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalPhaseLine"""
    def __init__(self, *args) -> None: ...
    ...

class ElectricalSetting(Element):
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalSetting"""
    def __init__(self, *args) -> None: ...
    CircuitSequence: CircuitSequence
    CircuitLoadCalculationMethod: CircuitLoadCalculationMethod
    CircuitPathOffset: float
    CircuitRating: float
    CircuitNamePhaseC: str
    CircuitNamePhaseB: str
    CircuitNamePhaseA: str
    WireConduitTypes: WireConduitTypeSet
    DistributionSysTypes: DistributionSysTypeSet
    WireTypes: WireTypeSet
    VoltageTypes: VoltageTypeSet
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
    def AddDistributionSysType(self, name: str, phase: ElectricalPhase, phaseConfig: ElectricalPhaseConfiguration, numWire: int, volLineToLine: VoltageType, volLineToGround: VoltageType) -> DistributionSysType: ...
    def AddVoltageType(self, name: str, actualValue: float, minValue: float, maxValue: float) -> VoltageType: ...
    @staticmethod
    def GetCircuitNamingSchemeSettings(cda: Document) -> CircuitNamingSchemeSettings: ...
    @staticmethod
    def GetElectricalSettings(document: Document) -> ElectricalSetting: ...
    def GetSpecificFittingAngleStatus(self, angle: float) -> bool: ...
    def GetSpecificFittingAngles(self, ) -> IList: ...
    def IsValidSpecificFittingAngle(self, angle: float) -> bool: ...
    def RemoveDistributionSysType(self, distributionSysType: DistributionSysType) -> None: ...
    def RemoveVoltageType(self, voltageType: VoltageType) -> None: ...
    def RemoveWireType(self, wireType: WireType) -> None: ...
    def SetSpecificFittingAngleStatus(self, angle: float, bStatus: bool) -> None: ...

class ElectricalSystem(MEPSystem):
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalSystem"""
    def __init__(self, *args) -> None: ...
    CircuitConnectionType: CircuitConnectionType
    CircuitPathMode: ElectricalCircuitPathMode
    CableSize: ElementId
    CableType: ElementId
    HasCustomCircuitPath: bool
    IsBasePanelFeedThroughLugsOccupied: bool
    PanelName: str
    CircuitType: CircuitType
    OtherConductorsNumber: int
    GroundConductorsNumber: int
    NeutralConductorsNumber: int
    HotConductorsNumber: int
    RunsNumber: int
    BalancedLoad: bool
    PolesNumber: int
    Ways: int
    PhaseLabel: str
    LoadClassificationAbbreviations: str
    LoadClassifications: str
    PowerFactorState: PowerFactorStateType
    SystemType: ElectricalSystemType
    TrueCurrentPhaseC: float
    TrueCurrentPhaseB: float
    TrueCurrentPhaseA: float
    TrueCurrent: float
    ApparentCurrentPhaseC: float
    ApparentCurrentPhaseB: float
    ApparentCurrentPhaseA: float
    ApparentCurrent: float
    Length: float
    Frame: float
    HasPathOffset: bool
    PathOffset: float
    Rating: float
    TrueLoadPhaseC: float
    TrueLoadPhaseB: float
    TrueLoadPhaseA: float
    TrueLoad: float
    PowerFactor: float
    ApparentLoadPhaseC: float
    ApparentLoadPhaseB: float
    ApparentLoadPhaseA: float
    ApparentLoad: float
    Voltage: float
    OtherConductorSize: ElementId
    NeutralConductorSize: ElementId
    GroundConductorSize: ElementId
    HotConductorSize: ElementId
    LoadName: str
    SlotIndex: str
    StartSlot: int
    CircuitNamingIndex: int
    CircuitNumber: str
    HasPlaceholders: bool
    HasDesignParts: bool
    HasFabricationParts: bool
    IsMultipleNetwork: bool
    PressureLossOfCriticalPath: float
    SectionsCount: int
    IsEmpty: bool
    IsValid: bool
    BaseEquipmentConnector: Connector
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
    def AddToCircuit(self, components: ElementSet) -> bool: ...
    @staticmethod
    def Create(document: Document, electComponents: IList, elecSysType: ElectricalSystemType) -> ElectricalSystem: ...
    def DisconnectPanel(self, ) -> None: ...
    def GetCircuitPath(self, ) -> IList: ...
    def IsCircuitPathValid(self, nodes: IList) -> bool: ...
    def NewWires(self, view: View, wiringType: WiringType) -> WireSet: ...
    def RemoveFromCircuit(self, components: ElementSet) -> None: ...
    def SelectPanel(self, panel: FamilyInstance) -> None: ...
    def SetCircuitPath(self, nodes: IList) -> None: ...

class ElectricalSystemType:
    """.NET: Autodesk.Revit.DB.Electrical.ElectricalSystemType"""
    def __init__(self, *args) -> None: ...
    ...

class InsulationMaterial:
    """.NET: Autodesk.Revit.DB.Electrical.InsulationMaterial"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Name: str
    Id: ElementId
    @staticmethod
    def Create(document: Document) -> InsulationMaterial: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetInsulationMaterial(document: Document, insulationMaterialId: ElementId) -> InsulationMaterial: ...
    @staticmethod
    def GetInsulationMaterialIdByName(document: Document, name: str) -> ElementId: ...
    @staticmethod
    def GetInsulationMaterialIds(document: Document) -> IList: ...

class LightingDevice(MEPModel):
    """.NET: Autodesk.Revit.DB.Electrical.LightingDevice"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ConnectorManager: ConnectorManager
    IsReadOnly: bool

class LightingFixture(MEPModel):
    """.NET: Autodesk.Revit.DB.Electrical.LightingFixture"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ConnectorManager: ConnectorManager
    IsReadOnly: bool

class LoadClassification:
    """.NET: Autodesk.Revit.DB.Electrical.LoadClassification"""
    def __init__(self, *args) -> None: ...
    ...

class LoadClassificationType:
    """.NET: Autodesk.Revit.DB.Electrical.LoadClassificationType"""
    def __init__(self, *args) -> None: ...
    ...

class NeutralMode:
    """.NET: Autodesk.Revit.DB.Electrical.NeutralMode"""
    def __init__(self, *args) -> None: ...
    ...

class PanelConfiguration:
    """.NET: Autodesk.Revit.DB.Electrical.PanelConfiguration"""
    def __init__(self, *args) -> None: ...
    ...

class PanelScheduleData(TableData):
    """.NET: Autodesk.Revit.DB.Electrical.PanelScheduleData"""
    def __init__(self, *args) -> None: ...
    IsUnusedPhaseHidden: bool
    IsAutoShadingForLoadDisplay: bool
    PhasesAsCurrents: bool
    ShowSlotFromDeviceInsteadOfTemplate: bool
    ShowMultipleRowsForMultiphaseCircuits: bool
    ShowCircuitNumberOnOneRowForMultiphaseCircuits: bool
    IsPanelSinglePhase: bool
    BodyShowsVerticalHeaders: bool
    SummaryShowsVerticalHeaders: bool
    SummaryShowsGroups: bool
    SummaryShowsOnlyConnectedLoads: bool
    IsFooterSectionHidden: bool
    IsSummarySectionHidden: bool
    IsHeaderSectionHidden: bool
    NumberOfSlots: int
    PhaseLoadType: PanelSchedulePhaseLoadType
    PanelConfiguration: PanelConfiguration
    ScheduleType: PanelScheduleType
    BorderAroundSchedule: ElementId
    BorderAroundSections: ElementId
    IsValidObject: bool
    ZoomLevel: int
    Width: float
    WidthInPixels: int
    NumberOfSections: int
    FreezeColumnsAndRows: bool
    def AddLoadClassification(self, loadClassficationId: ElementId) -> bool: ...
    def GetLoadClassifications(self, ) -> IList: ...
    def GetNumberOfCircuitRows(self, ) -> int: ...
    def IsSymmetric(self, ) -> bool: ...
    def RemoveLoadClassification(self, nIndex: int) -> None: ...
    def SetBorderAroundSchedule(self, borderId: ElementId) -> None: ...
    def SetBorderAroundSections(self, borderId: ElementId) -> None: ...
    def SetLoadClassifications(self, loadClassificaions: IList) -> None: ...
    def UpdateCircuitTableForInstance(self, pPanel: FamilyInstance) -> None: ...
    def UpdateCircuitTableForTemplate(self, newType: PanelSchedulePhaseLoadType, nNumSlots: int, bPhasesAsCurrents: bool) -> None: ...
    def UpdateIsSectionHidden(self, sectionType: SectionType, bHide: bool) -> None: ...
    def UpdateLoadSummary(self, ) -> None: ...
    def UpdateVerticalHeadersInSection(self, sectionType: SectionType, bVertical: bool) -> None: ...

class PanelSchedulePhaseLoadType:
    """.NET: Autodesk.Revit.DB.Electrical.PanelSchedulePhaseLoadType"""
    def __init__(self, *args) -> None: ...
    ...

class PanelScheduleSheetInstance(Element):
    """.NET: Autodesk.Revit.DB.Electrical.PanelScheduleSheetInstance"""
    def __init__(self, *args) -> None: ...
    ScheduleId: ElementId
    Origin: XYZ
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
    def Create(ADoc: Document, scheduleId: ElementId, DBView: View) -> PanelScheduleSheetInstance: ...
    def GetSchedule(self, ) -> PanelScheduleView: ...
    def SplitSegment(self, iSeg: int) -> bool: ...

class PanelScheduleTemplate(Element):
    """.NET: Autodesk.Revit.DB.Electrical.PanelScheduleTemplate"""
    def __init__(self, *args) -> None: ...
    IsDefault: bool
    IsSwitchboardSchedule: bool
    IsDataPanelSchedule: bool
    IsBranchPanelSchedule: bool
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
    def CopyFrom(self, OtherADoc: Document, otherElem: PanelScheduleTemplate) -> None: ...
    @staticmethod
    def Create(document: Document, type: PanelScheduleType, config: PanelConfiguration, strName: str) -> PanelScheduleTemplate: ...
    def GetPanelScheduleType(self, ) -> PanelScheduleType: ...
    def GetSectionData(self, sectionType: SectionType) -> TableSectionData: ...
    def GetTableData(self, ) -> PanelScheduleData: ...
    def HasSameType(self, otherTemplate: PanelScheduleTemplate) -> bool: ...
    @staticmethod
    def IsValidPanelConfiguration(scheduleType: PanelScheduleType, configuration: PanelConfiguration) -> bool: ...
    @staticmethod
    def IsValidType(panelScheduleType: PanelScheduleType) -> bool: ...
    def SetTableData(self, Data: PanelScheduleData) -> None: ...

class PanelScheduleType:
    """.NET: Autodesk.Revit.DB.Electrical.PanelScheduleType"""
    def __init__(self, *args) -> None: ...
    ...

class PanelScheduleView(TableView):
    """.NET: Autodesk.Revit.DB.Electrical.PanelScheduleView"""
    def __init__(self, *args) -> None: ...
    MaximumRowHeight: int
    MaximumColumnWidth: int
    MinimumRowHeight: int
    MinimumColumnWidth: int
    MaximumGridWidth: int
    TargetId: ElementId
    ViewTemplateId: ElementId
    SunlightIntensity: int
    ShadowIntensity: int
    Discipline: ViewDiscipline
    DisplayStyle: DisplayStyle
    RevealConstraintsMode: bool
    TemporaryViewModes: TemporaryViewModes
    AnalysisDisplayStyleId: ElementId
    AreCoordinationModelHandlesHidden: bool
    ArePointCloudsHidden: bool
    AreImportCategoriesHidden: bool
    AreAnalyticalModelCategoriesHidden: bool
    AreAnnotationCategoriesHidden: bool
    AreModelCategoriesHidden: bool
    DetailLevel: ViewDetailLevel
    PartsVisibility: PartsVisibility
    Title: str
    IsAssemblyView: bool
    AssociatedAssemblyInstanceId: ElementId
    IsCallout: bool
    ViewPositionId: ElementId
    SunAndShadowSettings: SunAndShadowSettings
    SketchPlane: SketchPlane
    CropBoxVisible: bool
    CropBoxActive: bool
    GenLevel: Level
    IsTemplate: bool
    CanBePrinted: bool
    UpDirection: XYZ
    RightDirection: XYZ
    ViewDirection: XYZ
    Scale: int
    Origin: XYZ
    CropBox: BoundingBoxXYZ
    ViewType: ViewType
    Outline: BoundingBoxUV
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
    def AddSpace(self, nRow: int, nCol: int) -> None: ...
    def AddSpare(self, nRow: int, nCol: int) -> None: ...
    def CanMoveSlotTo(self, nMovingRow: int, nMovingCol: int, nToRow: int, nToCol: int) -> bool: ...
    @staticmethod
    def CreateInstanceView(ADoc: Document, templateId: ElementId, panelId: ElementId) -> PanelScheduleView: ...
    def GenerateInstanceFromTemplate(self, templateId: ElementId) -> None: ...
    def GetApparentPhaseValue(self, circuitId: ElementId, apparentLoadParam: ElementId) -> float: ...
    def GetCellsBySlotNumber(self, nSlotNumber: int, RowArr: IList, ColArr: IList) -> None: ...
    def GetCircuitByCell(self, nRow: int, nCol: int) -> ElectricalSystem: ...
    def GetCircuitIdByCell(self, nRow: int, nCol: int) -> ElementId: ...
    def GetCombinedParamValue(self, sectionType: SectionType, nRow: int, nCol: int) -> str: ...
    def GetLoadClassificationConnectedCurrent(self, nRow: int, nCol: int) -> str: ...
    def GetLoadClassificationConnectedLoad(self, nRow: int, nCol: int) -> str: ...
    def GetLoadClassificationDemandCurrent(self, nRow: int, nCol: int) -> str: ...
    def GetLoadClassificationDemandFactor(self, nRow: int, nCol: int) -> str: ...
    def GetLoadClassificationDemandLoad(self, nRow: int, nCol: int) -> str: ...
    def GetLoadClassificationId(self, nRow: int) -> ElementId: ...
    def GetLoadClassificationName(self, nRow: int, nCol: int) -> str: ...
    def GetLoadClassificationParamValue(self, parameterId: ElementId, nRow: int, nCol: int) -> str: ...
    def GetPanel(self, ) -> ElementId: ...
    def GetParamValue(self, sectionType: SectionType, nRow: int, nCol: int) -> str: ...
    def GetSectionData(self, sectionType: SectionType) -> TableSectionData: ...
    def GetSlotNumberByCell(self, nRow: int, nCol: int) -> int: ...
    def GetSpareCurrentValue(self, row: int, column: int, idCurrentParameter: ElementId) -> float: ...
    def GetSpareLoadValue(self, row: int, column: int, idLoadParameter: ElementId) -> float: ...
    def GetTableData(self, ) -> PanelScheduleData: ...
    def GetTemplate(self, ) -> ElementId: ...
    def IsCellInPhaseLoads(self, nRow: int, nCol: int) -> bool: ...
    def IsColumnInLoadSummary(self, nCol: int) -> bool: ...
    def IsPanelScheduleTemplate(self, ) -> bool: ...
    def IsRowInCircuitTable(self, nRow: int) -> bool: ...
    def IsSlotGrouped(self, nRow: int, nCol: int) -> int: ...
    def IsSlotLocked(self, nRow: int, nCol: int) -> bool: ...
    def IsSpace(self, nRow: int, nCol: int) -> bool: ...
    def IsSpare(self, nRow: int, nCol: int) -> bool: ...
    def MoveSlotTo(self, nMovingRow: int, nMovingCol: int, nToRow: int, nToCol: int) -> None: ...
    def RemoveSpace(self, nRow: int, nCol: int) -> None: ...
    def RemoveSpare(self, nRow: int, nCol: int) -> None: ...
    def RenumberIndexes(self, ) -> None: ...
    def SetLockSlot(self, nRow: int, nCol: int, bLock: bool) -> None: ...
    def SetParamValue(self, sectionType: SectionType, nRow: int, nCol: int, sValue: str) -> bool: ...
    def SetSpareCurrentValue(self, row: int, column: int, idCurrentParameter: ElementId, value: float) -> None: ...
    def SetSpareLoadValue(self, row: int, column: int, idLoadParameter: ElementId, value: float) -> None: ...
    def SwitchPhases(self, nRow: int, nCol: int) -> None: ...

class PowerFactorStateType:
    """.NET: Autodesk.Revit.DB.Electrical.PowerFactorStateType"""
    def __init__(self, *args) -> None: ...
    ...

class TemperatureRating:
    """.NET: Autodesk.Revit.DB.Electrical.TemperatureRating"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Name: str
    Id: ElementId
    @staticmethod
    def Create(document: Document) -> TemperatureRating: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetTemperatureRating(document: Document, temperatureRatingId: ElementId) -> TemperatureRating: ...
    @staticmethod
    def GetTemperatureRatingIdByName(document: Document, name: str) -> ElementId: ...
    @staticmethod
    def GetTemperatureRatingIds(document: Document) -> IList: ...

class VoltageType(ElementType):
    """.NET: Autodesk.Revit.DB.Electrical.VoltageType"""
    def __init__(self, *args) -> None: ...
    IsInUse: bool
    MinValue: float
    MaxValue: float
    ActualValue: float
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
    def SetVoltageValue(self, actualValue: float, minValue: float, maxValue: float) -> None: ...

class VoltageTypeSet(APIObject):
    """.NET: Autodesk.Revit.DB.Electrical.VoltageTypeSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: VoltageType) -> bool: ...
    def Erase(self, item: VoltageType) -> int: ...
    def ForwardIterator(self, ) -> VoltageTypeSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: VoltageType) -> bool: ...
    def ReverseIterator(self, ) -> VoltageTypeSetIterator: ...

class VoltageTypeSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.Electrical.VoltageTypeSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class Wire(MEPCurve):
    """.NET: Autodesk.Revit.DB.Electrical.Wire"""
    def __init__(self, *args) -> None: ...
    NumberOfVertices: int
    GroundConductorNum: int
    NeutralConductorNum: int
    HotConductorNum: int
    WiringType: WiringType
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
    def AppendVertex(self, vertexPoint: XYZ) -> None: ...
    @staticmethod
    def AreVertexPointsValid(vertexPoints: IList, startConnector: Connector, endConnector: Connector) -> bool: ...
    def ConnectTo(self, startConnectorTo: Connector, endConnectorTo: Connector) -> None: ...
    @staticmethod
    def Create(document: Document, wireTypeId: ElementId, viewId: ElementId, wiringType: WiringType, vertexPoints: IList, startConnectorTo: Connector, endConnectorTo: Connector) -> Wire: ...
    def GetMEPSystems(self, ) -> IList: ...
    def GetVertex(self, index: int) -> XYZ: ...
    def InsertVertex(self, index: int, vertexPoint: XYZ) -> None: ...
    def IsVertexPointValid(self, vertexPoint: XYZ) -> bool: ...
    def RemoveVertex(self, index: int) -> None: ...
    def SetVertex(self, index: int, vertexPoint: XYZ) -> None: ...

class WireConduitType(APIObject):
    """.NET: Autodesk.Revit.DB.Electrical.WireConduitType"""
    def __init__(self, *args) -> None: ...
    Name: str
    IsReadOnly: bool

class WireConduitTypeSet(APIObject):
    """.NET: Autodesk.Revit.DB.Electrical.WireConduitTypeSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: WireConduitType) -> bool: ...
    def Erase(self, item: WireConduitType) -> int: ...
    def ForwardIterator(self, ) -> WireConduitTypeSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: WireConduitType) -> bool: ...
    def ReverseIterator(self, ) -> WireConduitTypeSetIterator: ...

class WireConduitTypeSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.Electrical.WireConduitTypeSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class WireSet(APIObject):
    """.NET: Autodesk.Revit.DB.Electrical.WireSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: Wire) -> bool: ...
    def Erase(self, item: Wire) -> int: ...
    def ForwardIterator(self, ) -> WireSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: Wire) -> bool: ...
    def ReverseIterator(self, ) -> WireSetIterator: ...

class WireSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.Electrical.WireSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class WireType(ElementType):
    """.NET: Autodesk.Revit.DB.Electrical.WireType"""
    def __init__(self, *args) -> None: ...
    MaxSize: str
    Insulation: ElementId
    TemperatureRating: ElementId
    WireMaterial: ElementId
    IsInUse: bool
    Conduit: WireConduitType
    NeutralSize: NeutralMode
    NeutralRequired: bool
    NeutralMultiplier: float
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

class WireTypeSet(APIObject):
    """.NET: Autodesk.Revit.DB.Electrical.WireTypeSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: WireType) -> bool: ...
    def Erase(self, item: WireType) -> int: ...
    def ForwardIterator(self, ) -> WireTypeSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: WireType) -> bool: ...
    def ReverseIterator(self, ) -> WireTypeSetIterator: ...

class WireTypeSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.Electrical.WireTypeSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class WiringType:
    """.NET: Autodesk.Revit.DB.Electrical.WiringType"""
    def __init__(self, *args) -> None: ...
    ...
