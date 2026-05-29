# Auto-generated — Revit 2027 — Autodesk.Revit.DB.Architecture

class BalusterInfo:
    """.NET: Autodesk.Revit.DB.Architecture.BalusterInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    TopReferenceName: str
    BaseReferenceName: str
    DistanceFromPreviousOrSpace: float
    Offset: float
    TopOffset: float
    BaseOffset: float
    Name: str
    BalusterFamilyId: ElementId
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetReferenceNameForHost() -> str: ...
    @staticmethod
    def GetReferenceNameForTopRail() -> str: ...

class BalusterPattern:
    """.NET: Autodesk.Revit.DB.Architecture.BalusterPattern"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Length: float
    DistributionJustification: PatternJustification
    BreakPattern: BreakPatternCondition
    ExcessLengthFillSpacing: float
    ExcessLengthFillBalusterId: ElementId
    PatternAngle: float
    EndSpace: float
    def Dispose(self, ) -> None: ...
    def DuplicateBaluster(self, index: int) -> BalusterInfo: ...
    def GetBaluster(self, index: int) -> BalusterInfo: ...
    def GetBalusterCount(self, ) -> int: ...
    def RemoveBaluster(self, index: int) -> None: ...

class BalusterPlacement:
    """.NET: Autodesk.Revit.DB.Architecture.BalusterPlacement"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    BalusterPerTreadFamilyId: ElementId
    BalusterPerTreadNumber: int
    UseBalusterPerTreadOnStairs: bool
    PostPattern: PostPattern
    BalusterPattern: BalusterPattern
    def Dispose(self, ) -> None: ...

class BreakCornerCondition:
    """.NET: Autodesk.Revit.DB.Architecture.BreakCornerCondition"""
    def __init__(self, *args) -> None: ...
    ...

class BreakPatternCondition:
    """.NET: Autodesk.Revit.DB.Architecture.BreakPatternCondition"""
    def __init__(self, *args) -> None: ...
    ...

class BuildingPad(CeilingAndFloor):
    """.NET: Autodesk.Revit.DB.Architecture.BuildingPad"""
    def __init__(self, *args) -> None: ...
    AssociatedTopographySurfaceId: ElementId
    HostId: ElementId
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
    def Create(document: Document, buildingPadTypeId: ElementId, levelId: ElementId, curveLoops: IList) -> BuildingPad: ...
    def GetBoundary(self, ) -> IList: ...
    def SetBoundary(self, curveLoops: IList) -> None: ...

class ContinuousRail(Element):
    """.NET: Autodesk.Revit.DB.Architecture.ContinuousRail"""
    def __init__(self, *args) -> None: ...
    HostRailingId: ElementId
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
    def GetEndExtensionPath(self, ) -> IList: ...
    def GetPath(self, ) -> IList: ...
    def GetStartExtensionPath(self, ) -> IList: ...
    def GetSupports(self, ) -> IList: ...

class ContinuousRailType(ElementType):
    """.NET: Autodesk.Revit.DB.Architecture.ContinuousRailType"""
    def __init__(self, *args) -> None: ...
    HandClearance: float
    Projection: float
    EndOrTopTermination: ElementId
    StartOrBottomTermination: ElementId
    FilletRadius: float
    DefaultJoinOption: RailTypeDefaultJoinOption
    Transition: RailTransitionOption
    EndOrTopExtensionStyle: RailExtensionStyle
    StartOrBottomExtensionStyle: RailExtensionStyle
    ProfileId: ElementId
    EndOrTopExtensionLength: float
    StartOrBottomExtensionLength: float
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

class CutLineType:
    """.NET: Autodesk.Revit.DB.Architecture.CutLineType"""
    def __init__(self, *args) -> None: ...
    ...

class CutMarkSymbol:
    """.NET: Autodesk.Revit.DB.Architecture.CutMarkSymbol"""
    def __init__(self, *args) -> None: ...
    ...

class CutMarkType(ElementType):
    """.NET: Autodesk.Revit.DB.Architecture.CutMarkType"""
    def __init__(self, *args) -> None: ...
    CutLineType: CutLineType
    CutMarkSymbol: CutMarkSymbol
    CutLineDistance: float
    CutLineExtension: float
    CutLineAngle: float
    CutMarkSymbolSize: float
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

class Fascia(HostedSweep):
    """.NET: Autodesk.Revit.DB.Architecture.Fascia"""
    def __init__(self, *args) -> None: ...
    FasciaType: FasciaType
    ReferenceCurve: Curve
    VerticalFlipped: bool
    HorizontalFlipped: bool
    Angle: float
    VerticalOffset: float
    HorizontalOffset: float
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
    def AddSegment(self, targetRef: Reference) -> None: ...

class FasciaType(HostedSweepType):
    """.NET: Autodesk.Revit.DB.Architecture.FasciaType"""
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

class Gutter(HostedSweep):
    """.NET: Autodesk.Revit.DB.Architecture.Gutter"""
    def __init__(self, *args) -> None: ...
    GutterType: GutterType
    ReferenceCurve: Curve
    VerticalFlipped: bool
    HorizontalFlipped: bool
    Angle: float
    VerticalOffset: float
    HorizontalOffset: float
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
    def AddSegment(self, targetRef: Reference) -> None: ...

class GutterType(HostedSweepType):
    """.NET: Autodesk.Revit.DB.Architecture.GutterType"""
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

class HandRail(ContinuousRail):
    """.NET: Autodesk.Revit.DB.Architecture.HandRail"""
    def __init__(self, *args) -> None: ...
    HostRailingId: ElementId
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

class HandRailPosition:
    """.NET: Autodesk.Revit.DB.Architecture.HandRailPosition"""
    def __init__(self, *args) -> None: ...
    ...

class HandRailType(ContinuousRailType):
    """.NET: Autodesk.Revit.DB.Architecture.HandRailType"""
    def __init__(self, *args) -> None: ...
    SupportLayout: RailSupportsLayout
    SupportJustification: RailSupportJustification
    SupportNumber: int
    SupportTypeId: ElementId
    SupportSpacing: float
    Height: float
    HandClearance: float
    Projection: float
    EndOrTopTermination: ElementId
    StartOrBottomTermination: ElementId
    FilletRadius: float
    DefaultJoinOption: RailTypeDefaultJoinOption
    Transition: RailTransitionOption
    EndOrTopExtensionStyle: RailExtensionStyle
    StartOrBottomExtensionStyle: RailExtensionStyle
    ProfileId: ElementId
    EndOrTopExtensionLength: float
    StartOrBottomExtensionLength: float
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

class MultistoryStairs(Element):
    """.NET: Autodesk.Revit.DB.Architecture.MultistoryStairs"""
    def __init__(self, *args) -> None: ...
    StandardStairsId: ElementId
    ActualTreadDepth: float
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
    def CanConnectLevel(self, levelId: ElementId) -> bool: ...
    def CanDisconnectLevel(self, levelId: ElementId) -> bool: ...
    def ConnectLevels(self, levelIds: ISet) -> None: ...
    @staticmethod
    def Create(stairs: Stairs) -> MultistoryStairs: ...
    def DisconnectLevels(self, levelIds: ISet) -> None: ...
    def GetAllConnectedLevels(self, ) -> ISet: ...
    def GetAllStairsIds(self, ) -> ISet: ...
    def GetStairsOnLevel(self, levelId: ElementId) -> Stairs: ...
    def GetStairsPlacementLevels(self, stairs: Stairs) -> ISet: ...
    @staticmethod
    def IsAcceptableForMultistoryStairs(stairs: Stairs) -> bool: ...
    def IsPinned(self, stairs: Stairs) -> bool: ...
    def Pin(self, levelId: ElementId) -> Stairs: ...
    def Unpin(self, levelId: ElementId) -> Stairs: ...

class NonContinuousRailInfo:
    """.NET: Autodesk.Revit.DB.Architecture.NonContinuousRailInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    MaterialId: ElementId
    ProfileId: ElementId
    Offset: float
    Height: float
    Name: str
    def Dispose(self, ) -> None: ...
    def IsValidNonContinuousRailHeight(self, height: float) -> bool: ...
    def IsValidNonContinuousRailMaterial(self, materialId: ElementId) -> bool: ...
    def IsValidNonContinuousRailName(self, name: str) -> bool: ...
    def IsValidNonContinuousRailProfile(self, profileId: ElementId) -> bool: ...

class NonContinuousRailStructure:
    """.NET: Autodesk.Revit.DB.Architecture.NonContinuousRailStructure"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def AddNonContinuousRail(self, name: str, height: float, offset: float) -> NonContinuousRailInfo: ...
    def Dispose(self, ) -> None: ...
    def GetNonContinuousRail(self, index: int) -> NonContinuousRailInfo: ...
    def GetNonContinuousRailCount(self, ) -> int: ...
    def IsValidNonContinuousRailProfile(self, profileId: ElementId) -> bool: ...
    def RemoveNonContinuousRail(self, index: int) -> None: ...

class NumberSystemType(ElementType):
    """.NET: Autodesk.Revit.DB.Architecture.NumberSystemType"""
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

class PatternJustification:
    """.NET: Autodesk.Revit.DB.Architecture.PatternJustification"""
    def __init__(self, *args) -> None: ...
    ...

class PostPattern:
    """.NET: Autodesk.Revit.DB.Architecture.PostPattern"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    CornerPostCondition: BreakCornerCondition
    CornerPostAngle: float
    CornerPost: BalusterInfo
    EndPost: BalusterInfo
    StartPost: BalusterInfo
    def Dispose(self, ) -> None: ...

class RailAngledJoinOption:
    """.NET: Autodesk.Revit.DB.Architecture.RailAngledJoinOption"""
    def __init__(self, *args) -> None: ...
    ...

class RailConnectionOption:
    """.NET: Autodesk.Revit.DB.Architecture.RailConnectionOption"""
    def __init__(self, *args) -> None: ...
    ...

class RailExtensionStyle:
    """.NET: Autodesk.Revit.DB.Architecture.RailExtensionStyle"""
    def __init__(self, *args) -> None: ...
    ...

class RailIndex:
    """.NET: Autodesk.Revit.DB.Architecture.RailIndex"""
    def __init__(self, *args) -> None: ...
    ...

class RailJoinOption:
    """.NET: Autodesk.Revit.DB.Architecture.RailJoinOption"""
    def __init__(self, *args) -> None: ...
    ...

class RailSupportJustification:
    """.NET: Autodesk.Revit.DB.Architecture.RailSupportJustification"""
    def __init__(self, *args) -> None: ...
    ...

class RailSupportsLayout:
    """.NET: Autodesk.Revit.DB.Architecture.RailSupportsLayout"""
    def __init__(self, *args) -> None: ...
    ...

class RailTagentJoinOption:
    """.NET: Autodesk.Revit.DB.Architecture.RailTagentJoinOption"""
    def __init__(self, *args) -> None: ...
    ...

class RailTransitionOption:
    """.NET: Autodesk.Revit.DB.Architecture.RailTransitionOption"""
    def __init__(self, *args) -> None: ...
    ...

class RailTypeDefaultJoinOption:
    """.NET: Autodesk.Revit.DB.Architecture.RailTypeDefaultJoinOption"""
    def __init__(self, *args) -> None: ...
    ...

class Railing(Element):
    """.NET: Autodesk.Revit.DB.Architecture.Railing"""
    def __init__(self, *args) -> None: ...
    CanReset: bool
    IsDefault: bool
    TopRail: ElementId
    Flipped: bool
    HasHost: bool
    HostId: ElementId
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
    def Create(document: Document, multistoryStairsId: ElementId, levelId: ElementId, railingTypeId: ElementId, placePosition: RailingPlacementPosition) -> ISet: ...
    def Flip(self, ) -> None: ...
    def GetHandRails(self, ) -> IList: ...
    def GetMultistoryStairsPlacementLevels(self, ) -> ISet: ...
    def GetPath(self, ) -> IList: ...
    def GetSubelementOnLevel(self, levelId: ElementId) -> Subelement: ...
    @staticmethod
    def IsValidHostForNewRailing(document: Document, elementId: ElementId) -> bool: ...
    @staticmethod
    def IsValidPathForRailing(curveLoop: CurveLoop) -> bool: ...
    def RailingCanBeHostedByElement(self, hostId: ElementId) -> bool: ...
    def RemoveHost(self, ) -> None: ...
    def Reset(self, ) -> None: ...
    def ResetSupportPosition(self, ) -> None: ...
    def SetMultistoryStairsPlacementLevels(self, levelIds: ISet) -> None: ...
    def SetPath(self, curveLoop: CurveLoop) -> None: ...

class RailingHeightCorrectionOption:
    """.NET: Autodesk.Revit.DB.Architecture.RailingHeightCorrectionOption"""
    def __init__(self, *args) -> None: ...
    ...

class RailingPathCurveJoinOption:
    """.NET: Autodesk.Revit.DB.Architecture.RailingPathCurveJoinOption"""
    def __init__(self, *args) -> None: ...
    ...

class RailingPlacementPosition:
    """.NET: Autodesk.Revit.DB.Architecture.RailingPlacementPosition"""
    def __init__(self, *args) -> None: ...
    ...

class RailingSlopeOption:
    """.NET: Autodesk.Revit.DB.Architecture.RailingSlopeOption"""
    def __init__(self, *args) -> None: ...
    ...

class RailingType(ElementType):
    """.NET: Autodesk.Revit.DB.Architecture.RailingType"""
    def __init__(self, *args) -> None: ...
    SecondaryHandrailHeight: float
    PrimaryHandrailHeight: float
    SecondaryHandrailLateralOffset: float
    PrimaryHandrailLateralOffset: float
    SecondaryHandrailType: ElementId
    PrimaryHandrailType: ElementId
    TopRailType: ElementId
    TopRailHeight: float
    SecondaryHandRailPosition: HandRailPosition
    PrimaryHandRailPosition: HandRailPosition
    RailStructure: NonContinuousRailStructure
    BalusterPlacement: BalusterPlacement
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

class RiserToTreadConnectionOption:
    """.NET: Autodesk.Revit.DB.Architecture.RiserToTreadConnectionOption"""
    def __init__(self, *args) -> None: ...
    ...

class Room(SpatialElement):
    """.NET: Autodesk.Revit.DB.Architecture.Room"""
    def __init__(self, *args) -> None: ...
    Volume: float
    UnboundedHeight: float
    BaseOffset: float
    LimitOffset: float
    UpperLimit: Level
    ClosedShell: GeometryElement
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
    def IsPointInRoom(self, point: XYZ) -> bool: ...
    def Unplace(self, ) -> None: ...

class RoomFilter(ElementSlowFilter):
    """.NET: Autodesk.Revit.DB.Architecture.RoomFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool

class RoomTag(SpatialElementTag):
    """.NET: Autodesk.Revit.DB.Architecture.RoomTag"""
    def __init__(self, *args) -> None: ...
    TaggedRoomId: LinkElementId
    TaggedLocalRoomId: ElementId
    IsInRoom: bool
    RoomTagType: RoomTagType
    Room: Room
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

class RoomTagFilter(ElementSlowFilter):
    """.NET: Autodesk.Revit.DB.Architecture.RoomTagFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool

class RoomTagType(FamilySymbol):
    """.NET: Autodesk.Revit.DB.Architecture.RoomTagType"""
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

class SiteSubRegion:
    """.NET: Autodesk.Revit.DB.Architecture.SiteSubRegion"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    HostId: ElementId
    TopographySurface: TopographySurface
    @staticmethod
    def Create(document: Document, curveLoops: IList, hostTopoSurfaceId: ElementId) -> SiteSubRegion: ...
    def Dispose(self, ) -> None: ...
    def GetBoundary(self, ) -> IList: ...
    @staticmethod
    def IsValidBoundary(curveLoops: IList) -> bool: ...
    def SetBoundary(self, curveLoops: IList) -> None: ...

class SketchedCurveSlopeOption:
    """.NET: Autodesk.Revit.DB.Architecture.SketchedCurveSlopeOption"""
    def __init__(self, *args) -> None: ...
    ...

class Stairs(Element):
    """.NET: Autodesk.Revit.DB.Architecture.Stairs"""
    def __init__(self, *args) -> None: ...
    MultistoryStairsId: ElementId
    NumberOfStories: int
    ActualTreadsNumber: int
    Height: float
    TopElevation: float
    BaseElevation: float
    DesiredRisersNumber: int
    ActualRisersNumber: int
    ActualTreadDepth: float
    ActualRiserHeight: float
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
    def GetAssociatedRailings(self, ) -> ICollection: ...
    def GetStairsLandings(self, ) -> ICollection: ...
    def GetStairsRuns(self, ) -> ICollection: ...
    def GetStairsSupports(self, ) -> ICollection: ...
    @staticmethod
    def IsByComponent(document: Document, stairsId: ElementId) -> bool: ...
    def IsInEditMode(self, ) -> bool: ...

class StairsComponentConnection:
    """.NET: Autodesk.Revit.DB.Architecture.StairsComponentConnection"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    PeerConnectionType: StairsComponentConnectionEndType
    ConnectionType: StairsComponentConnectionEndType
    PeerElementId: ElementId
    ElementId: ElementId
    def Dispose(self, ) -> None: ...

class StairsComponentConnectionEndType:
    """.NET: Autodesk.Revit.DB.Architecture.StairsComponentConnectionEndType"""
    def __init__(self, *args) -> None: ...
    ...

class StairsConstructionMethod:
    """.NET: Autodesk.Revit.DB.Architecture.StairsConstructionMethod"""
    def __init__(self, *args) -> None: ...
    ...

class StairsEndConnectionType:
    """.NET: Autodesk.Revit.DB.Architecture.StairsEndConnectionType"""
    def __init__(self, *args) -> None: ...
    ...

class StairsEndNotchOption:
    """.NET: Autodesk.Revit.DB.Architecture.StairsEndNotchOption"""
    def __init__(self, *args) -> None: ...
    ...

class StairsLanding(Element):
    """.NET: Autodesk.Revit.DB.Architecture.StairsLanding"""
    def __init__(self, *args) -> None: ...
    IsAutomaticLanding: bool
    BaseElevation: float
    Thickness: float
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
    def CanCreateAutomaticLanding(document: Document, firstRunId: ElementId, secondRunId: ElementId) -> bool: ...
    @staticmethod
    def CreateAutomaticLanding(document: Document, firstRunId: ElementId, secondRunId: ElementId) -> IList: ...
    @staticmethod
    def CreateSketchedLanding(document: Document, stairsId: ElementId, curveLoop: CurveLoop, baseElevation: float) -> StairsLanding: ...
    @staticmethod
    def CreateSketchedLandingWithSlopeData(document: Document, stairsId: ElementId, curveLoop: IList, baseElevation: float) -> StairsLanding: ...
    def GetAllSupports(self, ) -> IList: ...
    def GetConnections(self, ) -> IList: ...
    def GetFootprintBoundary(self, ) -> CurveLoop: ...
    def GetStairs(self, ) -> Stairs: ...
    def GetStairsPath(self, ) -> CurveLoop: ...
    def SetSketchedLandingBoundaryAndPath(self, document: Document, boundaryCurveLoop: CurveLoop, pathCurveLoop: CurveLoop) -> None: ...

class StairsLandingType(ElementType):
    """.NET: Autodesk.Revit.DB.Architecture.StairsLandingType"""
    def __init__(self, *args) -> None: ...
    Thickness: float
    IsMonolithic: bool
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

class StairsNumberSystemReferenceOption:
    """.NET: Autodesk.Revit.DB.Architecture.StairsNumberSystemReferenceOption"""
    def __init__(self, *args) -> None: ...
    ...

class StairsPath(Element):
    """.NET: Autodesk.Revit.DB.Architecture.StairsPath"""
    def __init__(self, *args) -> None: ...
    ShowDownText: bool
    ShowUpText: bool
    TextOrientation: StairsTextOrientation
    StairsId: LinkElementId
    StairsPathOffset: float
    UpTextOffset: XYZ
    DownTextOffset: XYZ
    DownText: str
    UpText: str
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
    def CanCreateOnMultistoryStairs(document: Document, multistoryStairsId: LinkElementId) -> bool: ...
    @staticmethod
    def Create(document: Document, stairsId: LinkElementId, typeId: ElementId, planViewId: ElementId) -> StairsPath: ...
    @staticmethod
    def CreateOnMultistoryStairs(document: Document, multistoryStairsId: LinkElementId, typeId: ElementId) -> IList: ...

class StairsPathDirection:
    """.NET: Autodesk.Revit.DB.Architecture.StairsPathDirection"""
    def __init__(self, *args) -> None: ...
    ...

class StairsPathLineShapeAtCorner:
    """.NET: Autodesk.Revit.DB.Architecture.StairsPathLineShapeAtCorner"""
    def __init__(self, *args) -> None: ...
    ...

class StairsPathType(ElementType):
    """.NET: Autodesk.Revit.DB.Architecture.StairsPathType"""
    def __init__(self, *args) -> None: ...
    FullStepArrow: bool
    StartFromRiser: bool
    ShowArrowheadToCutMark: bool
    DrawForEachRun: bool
    EndAtRiser: bool
    StairsPathDirection: StairsPathDirection
    LineShapeAtCorner: StairsPathLineShapeAtCorner
    StartSymbolTypeId: ElementId
    ArrowheadTypeId: ElementId
    StartExtension: float
    DistanceToCutMark: float
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

class StairsRun(Element):
    """.NET: Autodesk.Revit.DB.Architecture.StairsRun"""
    def __init__(self, *args) -> None: ...
    LocationLineJustification: StairsRunJustification
    EndsWithRiser: bool
    BeginsWithRiser: bool
    ExtensionBelowTreadBase: float
    ExtensionBelowRiserBase: float
    ActualTreadsNumber: int
    ActualRisersNumber: int
    ActualRunWidth: float
    TopElevation: float
    BaseElevation: float
    Height: float
    StairsRunStyle: StairsRunStyle
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
    def CreateSketchedRun(document: Document, stairsId: ElementId, baseElevation: float, boundaryCurves: IList, riserCurves: IList, stairsPath: IList) -> StairsRun: ...
    @staticmethod
    def CreateSketchedRunWithSlopeData(document: Document, stairsId: ElementId, baseElevation: float, boundaryCurves: IList, riserCurves: IList, stairsPath: IList) -> StairsRun: ...
    @staticmethod
    def CreateSpiralRun(document: Document, stairsId: ElementId, center: XYZ, radius: float, startAngle: float, includedAngle: float, clockwise: bool, justification: StairsRunJustification) -> StairsRun: ...
    @staticmethod
    def CreateStraightRun(document: Document, stairsId: ElementId, locationPath: Line, justification: StairsRunJustification) -> StairsRun: ...
    def GetAllSupports(self, ) -> IList: ...
    def GetConnections(self, ) -> IList: ...
    def GetFootprintBoundary(self, ) -> CurveLoop: ...
    def GetLeftSupports(self, ) -> IList: ...
    def GetNumberSystemReference(self, referenceOption: StairsNumberSystemReferenceOption) -> Reference: ...
    def GetRightSupports(self, ) -> IList: ...
    def GetStairs(self, ) -> Stairs: ...
    def GetStairsPath(self, ) -> CurveLoop: ...
    @staticmethod
    def SetLocationPathForSpiralRun(stairsRun: StairsRun, center: XYZ, radius: float, startAngle: float, includedAngle: float, clockwise: bool, justification: StairsRunJustification) -> bool: ...
    @staticmethod
    def SetLocationPathForStraightRun(stairsRun: StairsRun, locationPath: Line) -> bool: ...

class StairsRunJustification:
    """.NET: Autodesk.Revit.DB.Architecture.StairsRunJustification"""
    def __init__(self, *args) -> None: ...
    ...

class StairsRunStyle:
    """.NET: Autodesk.Revit.DB.Architecture.StairsRunStyle"""
    def __init__(self, *args) -> None: ...
    ...

class StairsRunType(ElementType):
    """.NET: Autodesk.Revit.DB.Architecture.StairsRunType"""
    def __init__(self, *args) -> None: ...
    RiserToTreadConnect: RiserToTreadConnectionOption
    RiserProfile: ElementId
    RiserThickness: float
    IsSlanted: bool
    TreadNosingPosition: TreadNosingPosition
    TreadProfile: ElementId
    NosingProfile: ElementId
    NosingLength: float
    TreadThickness: float
    MaterialId: ElementId
    UndersideSurfaceStyle: StairsUndersideSurfaceStyle
    TotalDepth: float
    StructuralDepth: float
    HasRisers: bool
    HasTreads: bool
    IsMonolithic: bool
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

class StairsSupportTopsideSurfaceType:
    """.NET: Autodesk.Revit.DB.Architecture.StairsSupportTopsideSurfaceType"""
    def __init__(self, *args) -> None: ...
    ...

class StairsTextOrientation:
    """.NET: Autodesk.Revit.DB.Architecture.StairsTextOrientation"""
    def __init__(self, *args) -> None: ...
    ...

class StairsType(ElementType):
    """.NET: Autodesk.Revit.DB.Architecture.StairsType"""
    def __init__(self, *args) -> None: ...
    HasMiddleSupports: bool
    MiddleSupportType: ElementId
    MiddleSupportsNumber: int
    RightLateralOffset: float
    LeftLateralOffset: float
    RightSideSupportType: ElementId
    LeftSideSupportType: ElementId
    ConstructionMethod: StairsConstructionMethod
    EndConnectionType: StairsEndConnectionType
    LandingType: ElementId
    RunType: ElementId
    NotchVerticalGap: float
    NotchHorizontalGap: float
    NotchThickness: float
    NotchExtension: float
    MinRunWidth: float
    MinTreadDepth: float
    MaxRiserHeight: float
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

class StairsUndersideSurfaceStyle:
    """.NET: Autodesk.Revit.DB.Architecture.StairsUndersideSurfaceStyle"""
    def __init__(self, *args) -> None: ...
    ...

class StairsWinderStyle:
    """.NET: Autodesk.Revit.DB.Architecture.StairsWinderStyle"""
    def __init__(self, *args) -> None: ...
    ...

class TopRail(ContinuousRail):
    """.NET: Autodesk.Revit.DB.Architecture.TopRail"""
    def __init__(self, *args) -> None: ...
    HostRailingId: ElementId
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

class TopRailType(ContinuousRailType):
    """.NET: Autodesk.Revit.DB.Architecture.TopRailType"""
    def __init__(self, *args) -> None: ...
    HandClearance: float
    Projection: float
    EndOrTopTermination: ElementId
    StartOrBottomTermination: ElementId
    FilletRadius: float
    DefaultJoinOption: RailTypeDefaultJoinOption
    Transition: RailTransitionOption
    EndOrTopExtensionStyle: RailExtensionStyle
    StartOrBottomExtensionStyle: RailExtensionStyle
    ProfileId: ElementId
    EndOrTopExtensionLength: float
    StartOrBottomExtensionLength: float
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

class TopographyEditScope(EditScope):
    """.NET: Autodesk.Revit.DB.Architecture.TopographyEditScope"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsPermitted: bool
    IsActive: bool
    def Start(self, topoSurfaceId: ElementId) -> ElementId: ...

class TopographyLinkType(ElementType):
    """.NET: Autodesk.Revit.DB.Architecture.TopographyLinkType"""
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
    def Reload(self, ) -> LinkLoadResult: ...

class TopographySurface(Element):
    """.NET: Autodesk.Revit.DB.Architecture.TopographySurface"""
    def __init__(self, *args) -> None: ...
    MaterialId: ElementId
    AssociatedBuildingPadId: ElementId
    IsAssociatedWithBuildingPad: bool
    IsSiteSubRegion: bool
    ArePointsEditable: bool
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
    def AddPoints(self, points: IList) -> None: ...
    @staticmethod
    def ArePointsDistinct(points: IList) -> bool: ...
    def AsSiteSubRegion(self, ) -> SiteSubRegion: ...
    def ChangePointElevation(self, point: XYZ, elevationValue: float) -> None: ...
    def ChangePointsElevation(self, points: IList, elevationValue: float) -> None: ...
    def ContainsPoint(self, point: XYZ) -> bool: ...
    @staticmethod
    def Create(document: Document, points: IList, facets: IList) -> TopographySurface: ...
    def DeletePoints(self, points: IList) -> None: ...
    def FindPoints(self, boundingBox: Outline) -> IList: ...
    def GetBoundaryPoints(self, ) -> IList: ...
    def GetHostedSubRegionIds(self, ) -> IList: ...
    def GetInteriorPoints(self, ) -> IList: ...
    def GetPoints(self, ) -> IList: ...
    def IsBoundaryPoint(self, point: XYZ) -> bool: ...
    @staticmethod
    def IsValidFaceSet(facets: IList, points: IList) -> bool: ...
    @staticmethod
    def IsValidRegion(points: IList) -> bool: ...
    def MovePoint(self, movedPoint: XYZ, targetPoint: XYZ) -> None: ...
    def MovePoints(self, movedPoints: IList, moveVector: XYZ) -> None: ...

class TreadNosingPosition:
    """.NET: Autodesk.Revit.DB.Architecture.TreadNosingPosition"""
    def __init__(self, *args) -> None: ...
    ...

class WinderPathResult:
    """.NET: Autodesk.Revit.DB.Architecture.WinderPathResult"""
    def __init__(self, *args) -> None: ...
    ...
