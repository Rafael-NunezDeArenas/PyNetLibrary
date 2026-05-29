# Auto-generated — Revit 2027 — Autodesk.Revit.DB

class ACADExportOptions(BaseExportOptions):
    """.NET: Autodesk.Revit.DB.ACADExportOptions"""
    def __init__(self, *args) -> None: ...
    HatchBackgroundColor: Color
    UseHatchBackgroundColor: bool
    FileVersion: ACADVersion
    NonplotSuffix: str
    MarkNonplotLayers: bool
    ExportingAreas: bool
    SharedCoords: bool
    TargetUnit: ExportUnit
    ACAPreference: ACAObjectPreference
    ExportOfSolids: SolidGeometry
    TextTreatment: TextTreatment
    LinetypesFileName: str
    LineScaling: LineScaling
    IsValidObject: bool
    PreserveCoincidentLines: bool
    HideUnreferenceViewTags: bool
    HideReferencePlane: bool
    HideScopeBox: bool
    Colors: ExportColorMode
    HatchPatternsFileName: str
    LayerMapping: str
    PropOverrides: PropOverrideMode

class ACADVersion:
    """.NET: Autodesk.Revit.DB.ACADVersion"""
    def __init__(self, *args) -> None: ...
    ...

class ACAObjectPreference:
    """.NET: Autodesk.Revit.DB.ACAObjectPreference"""
    def __init__(self, *args) -> None: ...
    ...

class APIObject:
    """.NET: Autodesk.Revit.DB.APIObject"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool
    def Dispose(self, ) -> None: ...

class AXMImportOptions(BaseImportOptions):
    """.NET: Autodesk.Revit.DB.AXMImportOptions"""
    def __init__(self, *args) -> None: ...
    ImportLevels: bool
    IsValidObject: bool
    ReferencePoint: XYZ
    AutoCorrectAlmostVHLines: bool
    VisibleLayersOnly: bool
    CustomScale: float
    OrientToView: bool
    ThisViewOnly: bool
    Placement: ImportPlacement
    ColorMode: ImportColorMode
    Unit: ImportUnit

class AdaptiveComponentFamilyUtils:
    """.NET: Autodesk.Revit.DB.AdaptiveComponentFamilyUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetNumberOfAdaptivePoints(family: Family) -> int: ...
    @staticmethod
    def GetNumberOfPlacementPoints(family: Family) -> int: ...
    @staticmethod
    def GetNumberOfShapeHandlePoints(family: Family) -> int: ...
    @staticmethod
    def GetPlacementNumber(doc: Document, refPointId: ElementId) -> int: ...
    @staticmethod
    def GetPointConstraintType(doc: Document, refPointId: ElementId) -> AdaptivePointConstraintType: ...
    @staticmethod
    def GetPointOrientationType(doc: Document, refPointId: ElementId) -> AdaptivePointOrientationType: ...
    @staticmethod
    def IsAdaptiveComponentFamily(family: Family) -> bool: ...
    @staticmethod
    def IsAdaptivePlacementPoint(doc: Document, refPointId: ElementId) -> bool: ...
    @staticmethod
    def IsAdaptivePoint(doc: Document, refPointId: ElementId) -> bool: ...
    @staticmethod
    def IsAdaptiveShapeHandlePoint(doc: Document, refPointId: ElementId) -> bool: ...
    @staticmethod
    def MakeAdaptivePoint(doc: Document, refPointId: ElementId, type: AdaptivePointType) -> None: ...
    @staticmethod
    def SetPlacementNumber(doc: Document, refPointId: ElementId, placementNumber: int) -> None: ...
    @staticmethod
    def SetPointConstraintType(doc: Document, refPointId: ElementId, constraintType: AdaptivePointConstraintType) -> None: ...
    @staticmethod
    def SetPointOrientationType(doc: Document, refPointId: ElementId, orientationType: AdaptivePointOrientationType) -> None: ...

class AdaptiveComponentInstanceUtils:
    """.NET: Autodesk.Revit.DB.AdaptiveComponentInstanceUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CreateAdaptiveComponentInstance(doc: Document, famSymb: FamilySymbol) -> FamilyInstance: ...
    @staticmethod
    def GetInstancePlacementPointElementRefIds(famInst: FamilyInstance) -> IList: ...
    @staticmethod
    def GetInstancePointElementRefIds(famInst: FamilyInstance) -> IList: ...
    @staticmethod
    def GetInstanceShapeHandlePointElementRefIds(famInst: FamilyInstance) -> IList: ...
    @staticmethod
    def HasAdaptiveFamilySymbol(famInst: FamilyInstance) -> bool: ...
    @staticmethod
    def IsAdaptiveComponentInstance(famInst: FamilyInstance) -> bool: ...
    @staticmethod
    def IsAdaptiveFamilySymbol(famSymb: FamilySymbol) -> bool: ...
    @staticmethod
    def IsInstanceFlipped(famInst: FamilyInstance) -> bool: ...
    @staticmethod
    def MoveAdaptiveComponentInstance(famInst: FamilyInstance, trf: Transform, unHost: bool) -> None: ...
    @staticmethod
    def SetInstanceFlipped(famInst: FamilyInstance, flip: bool) -> None: ...

class AdaptivePointConstraintType:
    """.NET: Autodesk.Revit.DB.AdaptivePointConstraintType"""
    def __init__(self, *args) -> None: ...
    ...

class AdaptivePointOrientationType:
    """.NET: Autodesk.Revit.DB.AdaptivePointOrientationType"""
    def __init__(self, *args) -> None: ...
    ...

class AdaptivePointType:
    """.NET: Autodesk.Revit.DB.AdaptivePointType"""
    def __init__(self, *args) -> None: ...
    ...

class AddInId:
    """.NET: Autodesk.Revit.DB.AddInId"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetAddInName(self, ) -> str: ...
    def GetAddInNameFromDocument(self, aDoc: Document) -> str: ...
    def GetGUID(self, ) -> Guid: ...

class AllowedValues:
    """.NET: Autodesk.Revit.DB.AllowedValues"""
    def __init__(self, *args) -> None: ...
    ...

class AlphanumericRevisionSettings:
    """.NET: Autodesk.Revit.DB.AlphanumericRevisionSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Suffix: str
    Prefix: str
    def Dispose(self, ) -> None: ...
    def GetSequence(self, ) -> IList: ...
    def IsEqual(self, other: AlphanumericRevisionSettings) -> bool: ...
    def IsValid(self, ) -> bool: ...
    def SetSequence(self, sequence: IList) -> None: ...

class AlternateUnits:
    """.NET: Autodesk.Revit.DB.AlternateUnits"""
    def __init__(self, *args) -> None: ...
    ...

class AnalyzesAsType:
    """.NET: Autodesk.Revit.DB.AnalyzesAsType"""
    def __init__(self, *args) -> None: ...
    ...

class AngularDimension(Dimension):
    """.NET: Autodesk.Revit.DB.AngularDimension"""
    def __init__(self, *args) -> None: ...
    IsValid: bool
    AreReferencesAvailable: bool
    TextPosition: XYZ
    Origin: XYZ
    LeaderEndPosition: XYZ
    HasLeader: bool
    ValueOverride: str
    Below: str
    Above: str
    Suffix: str
    Prefix: str
    IsLocked: bool
    ValueString: str
    Value: Nullable
    AreSegmentsEqual: bool
    Segments: DimensionSegmentArray
    NumberOfSegments: int
    DimensionShape: DimensionShape
    FamilyLabel: FamilyParameter
    Name: str
    DimensionType: DimensionType
    View: View
    Curve: Curve
    References: ReferenceArray
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
    def Create(document: Document, dbView: View, arc: Arc, references: IList, dimensionStyle: DimensionType) -> AngularDimension: ...
    def SetAngularRadius(self, radius: float) -> None: ...

class AnnotationFamilyUtils:
    """.NET: Autodesk.Revit.DB.AnnotationFamilyUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def HasExcludeFromLeaderOutline(element: Element) -> bool: ...
    @staticmethod
    def HasLeaderSnapReference(element: Element) -> bool: ...
    @staticmethod
    def IsExcludedFromLeaderOutline(element: Element) -> bool: ...
    @staticmethod
    def IsLeaderSnapReference(element: Element) -> bool: ...
    @staticmethod
    def SetIsExcludedFromLeaderOutline(element: Element, isExcluded: bool) -> None: ...
    @staticmethod
    def SetIsLeaderSnapReference(element: Element, isSnapReference: bool) -> None: ...

class AnnotationLabel(TextElement):
    """.NET: Autodesk.Revit.DB.AnnotationLabel"""
    def __init__(self, *args) -> None: ...
    UseNonBreakingSpaces: bool
    IsTextWrappingActive: bool
    KeepRotatedTextReadable: bool
    VerticalAlignment: VerticalTextAlignment
    HorizontalAlignment: HorizontalTextAlignment
    Text: str
    Coord: XYZ
    Width: float
    Height: float
    UpDirection: XYZ
    BaseDirection: XYZ
    Symbol: TextElementType
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
    def GetParameterFormatting(self, ) -> IList: ...

class AnnotationLabelParameterFormatting:
    """.NET: Autodesk.Revit.DB.AnnotationLabelParameterFormatting"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LeadingLineBreak: bool
    Suffix: str
    SampleText: str
    Prefix: str
    LeadingSpaces: int
    def Dispose(self, ) -> None: ...
    def GetParameterDefinition(self, document: Document) -> InternalDefinition: ...

class AnnotationMultipleAlignmentUtils:
    """.NET: Autodesk.Revit.DB.AnnotationMultipleAlignmentUtils"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    @staticmethod
    def ElementSupportsMultiAlign(element: Element) -> bool: ...
    @staticmethod
    def GetAnnotationCenter(element: Element) -> XYZ: ...
    @staticmethod
    def GetAnnotationOutlineWithoutLeaders(element: Element) -> IList: ...
    @staticmethod
    def MoveWithAnchoredLeaders(element: Element, moveVec: XYZ) -> None: ...

class AnnotationSymbol(FamilyInstance):
    """.NET: Autodesk.Revit.DB.AnnotationSymbol"""
    def __init__(self, *args) -> None: ...
    AnnotationSymbolType: AnnotationSymbolType
    HasSpatialElementFromToCalculationPoints: bool
    HasSpatialElementCalculationPoint: bool
    IsWorkPlaneFlipped: bool
    CanFlipWorkPlane: bool
    IsSlantedColumn: bool
    ExtensionUtility: IExtension
    SuperComponent: Element
    ToRoom: Room
    ToRoom: Room
    FromRoom: Room
    FromRoom: Room
    CanSplit: bool
    CanRotate: bool
    CanFlipFacing: bool
    CanFlipHand: bool
    Mirrored: bool
    Invisible: bool
    FacingFlipped: bool
    HandFlipped: bool
    FacingOrientation: XYZ
    HandOrientation: XYZ
    HostFace: Reference
    HostParameter: float
    Host: Element
    Location: Location
    Space: Space
    Space: Space
    Room: Room
    Room: Room
    StructuralType: StructuralType
    StructuralUsage: StructuralInstanceUsage
    StructuralMaterialId: ElementId
    StructuralMaterialType: StructuralMaterialType
    MEPModel: MEPModel
    Symbol: FamilySymbol
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
    def GetLeaders(self, ) -> IList: ...
    def addLeader(self, ) -> None: ...
    def duplicate(self, ) -> AnnotationSymbol: ...
    def removeLeader(self, ) -> None: ...

class AnnotationSymbolType(FamilySymbol):
    """.NET: Autodesk.Revit.DB.AnnotationSymbolType"""
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

class AppearanceAssetElement(Element):
    """.NET: Autodesk.Revit.DB.AppearanceAssetElement"""
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
    def Create(document: Document, name: str, asset: Asset) -> AppearanceAssetElement: ...
    def Duplicate(self, name: str) -> AppearanceAssetElement: ...
    @staticmethod
    def GetAppearanceAssetElementByName(doc: Document, name: str) -> AppearanceAssetElement: ...
    def GetRenderingAsset(self, ) -> Asset: ...
    def SetRenderingAsset(self, asset: Asset) -> None: ...

class Arc(Curve):
    """.NET: Autodesk.Revit.DB.Arc"""
    def __init__(self, *args) -> None: ...
    Radius: float
    YDirection: XYZ
    XDirection: XYZ
    Normal: XYZ
    Center: XYZ
    Period: float
    IsCyclic: bool
    Length: float
    ApproximateLength: float
    Reference: Reference
    IsClosed: bool
    IsBound: bool
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool
    @staticmethod
    def Create(center: XYZ, radius: float, startAngle: float, endAngle: float, xAxis: XYZ, yAxis: XYZ) -> Arc: ...

class ArcLengthDimension(AngularDimension):
    """.NET: Autodesk.Revit.DB.ArcLengthDimension"""
    def __init__(self, *args) -> None: ...
    IsValid: bool
    AreReferencesAvailable: bool
    TextPosition: XYZ
    Origin: XYZ
    LeaderEndPosition: XYZ
    HasLeader: bool
    ValueOverride: str
    Below: str
    Above: str
    Suffix: str
    Prefix: str
    IsLocked: bool
    ValueString: str
    Value: Nullable
    AreSegmentsEqual: bool
    Segments: DimensionSegmentArray
    NumberOfSegments: int
    DimensionShape: DimensionShape
    FamilyLabel: FamilyParameter
    Name: str
    DimensionType: DimensionType
    View: View
    Curve: Curve
    References: ReferenceArray
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
    def Create(document: Document, dbView: View, arc: Arc, ArcRef: Reference, references: IList) -> ArcLengthDimension: ...

class Area(SpatialElement):
    """.NET: Autodesk.Revit.DB.Area"""
    def __init__(self, *args) -> None: ...
    AreaScheme: AreaScheme
    IsGrossInterior: bool
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

class AreaElemType:
    """.NET: Autodesk.Revit.DB.AreaElemType"""
    def __init__(self, *args) -> None: ...
    ...

class AreaFilter(ElementSlowFilter):
    """.NET: Autodesk.Revit.DB.AreaFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool

class AreaScheme(Element):
    """.NET: Autodesk.Revit.DB.AreaScheme"""
    def __init__(self, *args) -> None: ...
    IsGrossBuildingArea: bool
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

class AreaTag(SpatialElementTag):
    """.NET: Autodesk.Revit.DB.AreaTag"""
    def __init__(self, *args) -> None: ...
    AreaTagType: AreaTagType
    Area: Area
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

class AreaTagFilter(ElementSlowFilter):
    """.NET: Autodesk.Revit.DB.AreaTagFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool

class AreaTagType(FamilySymbol):
    """.NET: Autodesk.Revit.DB.AreaTagType"""
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

class AreaVolumeSettings(Element):
    """.NET: Autodesk.Revit.DB.AreaVolumeSettings"""
    def __init__(self, *args) -> None: ...
    ComputeVolumes: bool
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
    def GetAreaVolumeSettings(aDoc: Document) -> AreaVolumeSettings: ...
    def GetSpatialElementBoundaryLocation(self, spType: SpatialElementType) -> SpatialElementBoundaryLocation: ...
    def SetSpatialElementBoundaryLocation(self, spatialElementBoundaryLocation: SpatialElementBoundaryLocation, spType: SpatialElementType) -> None: ...

class ArrayAnchorMember:
    """.NET: Autodesk.Revit.DB.ArrayAnchorMember"""
    def __init__(self, *args) -> None: ...
    ...

class AssemblyCodeTable(KeyBasedTreeEntryTable):
    """.NET: Autodesk.Revit.DB.AssemblyCodeTable"""
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
    def GetAssemblyCodeTable(doc: Document) -> AssemblyCodeTable: ...

class AssemblyDetailViewOrientation:
    """.NET: Autodesk.Revit.DB.AssemblyDetailViewOrientation"""
    def __init__(self, *args) -> None: ...
    ...

class AssemblyDifference:
    """.NET: Autodesk.Revit.DB.AssemblyDifference"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class AssemblyDifferenceConfiguration(AssemblyDifference):
    """.NET: Autodesk.Revit.DB.AssemblyDifferenceConfiguration"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class AssemblyDifferenceMemberCount(AssemblyDifference):
    """.NET: Autodesk.Revit.DB.AssemblyDifferenceMemberCount"""
    def __init__(self, *args) -> None: ...
    Count2: int
    Count1: int
    IsValidObject: bool

class AssemblyDifferenceMemberDifference(AssemblyDifference):
    """.NET: Autodesk.Revit.DB.AssemblyDifferenceMemberDifference"""
    def __init__(self, *args) -> None: ...
    MemberDifference: AssemblyMemberDifference
    MemberId2: ElementId
    MemberId1: ElementId
    IsValidObject: bool

class AssemblyDifferenceNamingCategory(AssemblyDifference):
    """.NET: Autodesk.Revit.DB.AssemblyDifferenceNamingCategory"""
    def __init__(self, *args) -> None: ...
    NamingCategoryId2: ElementId
    NamingCategoryId1: ElementId
    IsValidObject: bool

class AssemblyDifferenceNone(AssemblyDifference):
    """.NET: Autodesk.Revit.DB.AssemblyDifferenceNone"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class AssemblyInstance(Element):
    """.NET: Autodesk.Revit.DB.AssemblyInstance"""
    def __init__(self, *args) -> None: ...
    AssemblyTypeName: str
    NamingCategoryId: ElementId
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
    def AddMemberIds(self, memberIds: ICollection) -> None: ...
    def AllowsAssemblyViewCreation(self, ) -> bool: ...
    @staticmethod
    def AreElementsValidForAssembly(document: Document, assemblyMemberIds: ICollection, assemblyId: ElementId) -> bool: ...
    @staticmethod
    def CanRemoveElementsFromAssembly(assemblyInstance: AssemblyInstance, memberIds: ICollection) -> bool: ...
    @staticmethod
    def CompareAssemblyInstances(instance1: AssemblyInstance, instance2: AssemblyInstance) -> AssemblyDifference: ...
    @staticmethod
    def Create(document: Document, assemblyMemberIds: ICollection, namingCategoryId: ElementId) -> AssemblyInstance: ...
    def Disassemble(self, ) -> ICollection: ...
    def GetCenter(self, ) -> XYZ: ...
    def GetMemberIds(self, ) -> ICollection: ...
    def GetTransform(self, ) -> Transform: ...
    def IsMember(self, id: ElementId) -> bool: ...
    @staticmethod
    def IsValidNamingCategory(document: Document, namingCategoryId: ElementId, assemblyMemberIds: ICollection) -> bool: ...
    @staticmethod
    def PlaceInstance(document: Document, assemblyTypeId: ElementId, location: XYZ) -> AssemblyInstance: ...
    def RemoveMemberIds(self, memberIds: ICollection) -> None: ...
    def SetMemberIds(self, memberIds: ICollection) -> None: ...
    def SetTransform(self, trf: Transform) -> None: ...

class AssemblyMemberDifference:
    """.NET: Autodesk.Revit.DB.AssemblyMemberDifference"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class AssemblyMemberDifferentCategory(AssemblyMemberDifference):
    """.NET: Autodesk.Revit.DB.AssemblyMemberDifferentCategory"""
    def __init__(self, *args) -> None: ...
    CategoryId2: ElementId
    CategoryId1: ElementId
    IsValidObject: bool

class AssemblyMemberDifferentGeometry(AssemblyMemberDifference):
    """.NET: Autodesk.Revit.DB.AssemblyMemberDifferentGeometry"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class AssemblyMemberDifferentParameters(AssemblyMemberDifference):
    """.NET: Autodesk.Revit.DB.AssemblyMemberDifferentParameters"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class AssemblyMemberDifferentType(AssemblyMemberDifference):
    """.NET: Autodesk.Revit.DB.AssemblyMemberDifferentType"""
    def __init__(self, *args) -> None: ...
    TypeId2: ElementId
    TypeId1: ElementId
    IsValidObject: bool

class AssemblyType(ElementType):
    """.NET: Autodesk.Revit.DB.AssemblyType"""
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

class AssemblyViewUtils:
    """.NET: Autodesk.Revit.DB.AssemblyViewUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def AcquireAssemblyViews(document: Document, sourceAssemblyInstanceId: ElementId, targetAssemblyInstanceId: ElementId) -> None: ...
    @staticmethod
    def Create3DOrthographic(document: Document, assemblyInstanceId: ElementId, viewTemplateId: ElementId, isAssigned: bool) -> View3D: ...
    @staticmethod
    def CreateDetailSection(document: Document, assemblyInstanceId: ElementId, direction: AssemblyDetailViewOrientation, viewTemplateId: ElementId, isAssigned: bool) -> ViewSection: ...
    @staticmethod
    def CreateMaterialTakeoff(document: Document, assemblyInstanceId: ElementId, viewTemplateId: ElementId, isAssigned: bool) -> ViewSchedule: ...
    @staticmethod
    def CreatePartList(document: Document, assemblyInstanceId: ElementId, viewTemplateId: ElementId, isAssigned: bool) -> ViewSchedule: ...
    @staticmethod
    def CreateSheet(document: Document, assemblyInstanceId: ElementId, titleBlockId: ElementId) -> ViewSheet: ...
    @staticmethod
    def CreateSingleCategorySchedule(document: Document, assemblyInstanceId: ElementId, scheduleCategoryId: ElementId, viewTemplateId: ElementId, isAssigned: bool) -> ViewSchedule: ...

class AttachmentLocation:
    """.NET: Autodesk.Revit.DB.AttachmentLocation"""
    def __init__(self, *args) -> None: ...
    ...

class AttachmentType:
    """.NET: Autodesk.Revit.DB.AttachmentType"""
    def __init__(self, *args) -> None: ...
    ...

class AutomaticConnectionBehaviorType:
    """.NET: Autodesk.Revit.DB.AutomaticConnectionBehaviorType"""
    def __init__(self, *args) -> None: ...
    ...

class BIMExportOptions:
    """.NET: Autodesk.Revit.DB.BIMExportOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ViewId: ElementId
    def Dispose(self, ) -> None: ...

class BRepBuilder(ShapeBuilder):
    """.NET: Autodesk.Revit.DB.BRepBuilder"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def AddCoEdge(self, loopId: BRepBuilderGeometryId, edgeId: BRepBuilderGeometryId, bCoEdgeIsReversed: bool) -> BRepBuilderGeometryId: ...
    def AddEdge(self, edgeGeom: BRepBuilderEdgeGeometry) -> BRepBuilderGeometryId: ...
    def AddFace(self, surfaceGeom: BRepBuilderSurfaceGeometry, bFaceIsReversed: bool) -> BRepBuilderGeometryId: ...
    def AddLoop(self, faceId: BRepBuilderGeometryId) -> BRepBuilderGeometryId: ...
    def AllowRemovalOfProblematicFaces(self, ) -> None: ...
    def CanAddGeometry(self, ) -> bool: ...
    def Finish(self, ) -> BRepBuilderOutcome: ...
    def FinishFace(self, faceId: BRepBuilderGeometryId) -> None: ...
    def FinishLoop(self, loopId: BRepBuilderGeometryId) -> None: ...
    def GetResult(self, externalId: ExternalGeometryId, brepPersistentIds: BRepBuilderPersistentIds) -> ExternallyTaggedBRep: ...
    @staticmethod
    def IsPermittedSurfaceType(surface: Surface) -> bool: ...
    def IsResultAvailable(self, ) -> bool: ...
    def IsValidEdgeId(self, edgeId: BRepBuilderGeometryId) -> bool: ...
    def IsValidFaceId(self, faceId: BRepBuilderGeometryId) -> bool: ...
    def IsValidLoopId(self, loopId: BRepBuilderGeometryId) -> bool: ...
    def IsValidPersistentIdsMap(self, brepPersistentIds: BRepBuilderPersistentIds) -> bool: ...
    def RemovedSomeFaces(self, ) -> bool: ...
    def SetAllowShortEdges(self, ) -> None: ...
    def SetFaceMaterialId(self, faceId: BRepBuilderGeometryId, materialId: ElementId) -> None: ...

class BRepBuilderEdgeGeometry:
    """.NET: Autodesk.Revit.DB.BRepBuilderEdgeGeometry"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    @staticmethod
    def Create(startPoint: XYZ, endPoint: XYZ) -> BRepBuilderEdgeGeometry: ...
    def Dispose(self, ) -> None: ...

class BRepBuilderGeometryId:
    """.NET: Autodesk.Revit.DB.BRepBuilderGeometryId"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    @staticmethod
    def InvalidGeometryId() -> BRepBuilderGeometryId: ...

class BRepBuilderOutcome:
    """.NET: Autodesk.Revit.DB.BRepBuilderOutcome"""
    def __init__(self, *args) -> None: ...
    ...

class BRepBuilderPersistentIds:
    """.NET: Autodesk.Revit.DB.BRepBuilderPersistentIds"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def AddSubTag(self, externalGeometryId: ExternalGeometryId, brepBuilderGeometryId: BRepBuilderGeometryId) -> None: ...
    def Dispose(self, ) -> None: ...
    def IsAssociatedBRepBuilderValid(self, ) -> bool: ...
    def IsBRepBuilderGeometryIdFaceOrEdge(self, brepBuilderGeometryId: BRepBuilderGeometryId) -> bool: ...
    def IsValidBRepBuilderGeometryIdForNewCorrespondence(self, brepBuilderGeometryId: BRepBuilderGeometryId) -> bool: ...
    def IsValidExternalGeometryIdForNewCorrespondence(self, externalGeometryId: ExternalGeometryId) -> bool: ...

class BRepBuilderState:
    """.NET: Autodesk.Revit.DB.BRepBuilderState"""
    def __init__(self, *args) -> None: ...
    ...

class BRepBuilderSurfaceGeometry:
    """.NET: Autodesk.Revit.DB.BRepBuilderSurfaceGeometry"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    @staticmethod
    def Create(surface: Surface, surfaceEnvelope: BoundingBoxUV) -> BRepBuilderSurfaceGeometry: ...
    @staticmethod
    def CreateNURBSSurface(degreeU: int, degreeV: int, knotsU: IList, knotsV: IList, controlPoints: IList, weights: IList, bReverseOrientation: bool, surfaceEnvelope: BoundingBoxUV) -> BRepBuilderSurfaceGeometry: ...
    def Dispose(self, ) -> None: ...

class BRepType:
    """.NET: Autodesk.Revit.DB.BRepType"""
    def __init__(self, *args) -> None: ...
    ...

class BackClippingParam:
    """.NET: Autodesk.Revit.DB.BackClippingParam"""
    def __init__(self, *args) -> None: ...
    ...

class BackgroundImageFit:
    """.NET: Autodesk.Revit.DB.BackgroundImageFit"""
    def __init__(self, *args) -> None: ...
    ...

class BackgroundSettings:
    """.NET: Autodesk.Revit.DB.BackgroundSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class BackgroundStyle:
    """.NET: Autodesk.Revit.DB.BackgroundStyle"""
    def __init__(self, *args) -> None: ...
    ...

class BarTypeDiameterOptions:
    """.NET: Autodesk.Revit.DB.BarTypeDiameterOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    BarMassPerUnitLength: float
    StirrupTieBendDiameter: float
    StandardHookBendDiameter: float
    StandardBendDiameter: float
    BarNominalDiameter: float
    BarModelDiameter: float
    def Dispose(self, ) -> None: ...

class BaseArray(Element):
    """.NET: Autodesk.Revit.DB.BaseArray"""
    def __init__(self, *args) -> None: ...
    Label: FamilyParameter
    Name: str
    NumMembers: int
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
    def GetCopiedMemberIds(self, ) -> ICollection: ...
    def GetOriginalMemberIds(self, ) -> ICollection: ...

class BaseExportOptions:
    """.NET: Autodesk.Revit.DB.BaseExportOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    PreserveCoincidentLines: bool
    HideUnreferenceViewTags: bool
    HideReferencePlane: bool
    HideScopeBox: bool
    Colors: ExportColorMode
    HatchPatternsFileName: str
    LayerMapping: str
    PropOverrides: PropOverrideMode
    def Dispose(self, ) -> None: ...
    def GetExportFontTable(self, ) -> ExportFontTable: ...
    def GetExportLayerTable(self, ) -> ExportLayerTable: ...
    def GetExportLinetypeTable(self, ) -> ExportLinetypeTable: ...
    def GetExportPatternTable(self, ) -> ExportPatternTable: ...
    @staticmethod
    def GetPredefinedSetupNames(document: Document) -> IList: ...
    def SetExportFontTable(self, fontTable: ExportFontTable) -> None: ...
    def SetExportLayerTable(self, layerTable: ExportLayerTable) -> None: ...
    def SetExportLinetypeTable(self, linetypeTable: ExportLinetypeTable) -> None: ...
    def SetExportPatternTable(self, patternTable: ExportPatternTable) -> None: ...

class BaseImportOptions:
    """.NET: Autodesk.Revit.DB.BaseImportOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ReferencePoint: XYZ
    AutoCorrectAlmostVHLines: bool
    VisibleLayersOnly: bool
    CustomScale: float
    OrientToView: bool
    ThisViewOnly: bool
    Placement: ImportPlacement
    ColorMode: ImportColorMode
    Unit: ImportUnit
    def Dispose(self, ) -> None: ...
    def GetDefaultLengthUnit(self, ) -> ForgeTypeId: ...
    def GetLayerSelection(self, ) -> ICollection: ...
    def SetDefaultLengthUnit(self, specTypeId: ForgeTypeId) -> None: ...
    def SetLayerSelection(self, layerSelection: ICollection) -> None: ...

class BaseLoadOn:
    """.NET: Autodesk.Revit.DB.BaseLoadOn"""
    def __init__(self, *args) -> None: ...
    ...

class BasePoint(Element):
    """.NET: Autodesk.Revit.DB.BasePoint"""
    def __init__(self, *args) -> None: ...
    SharedPosition: XYZ
    Clipped: bool
    Position: XYZ
    IsShared: bool
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
    def GetProjectBasePoint(cda: Document) -> BasePoint: ...
    @staticmethod
    def GetSurveyPoint(cda: Document) -> BasePoint: ...

class BasicFileInfo:
    """.NET: Autodesk.Revit.DB.BasicFileInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LatestCentralEpisodeGUID: Guid
    LatestCentralVersion: int
    AllLocalChangesSavedToCentral: bool
    CentralPath: str
    Username: str
    LanguageWhenSaved: LanguageType
    Format: str
    IsSavedInLaterVersion: bool
    IsSavedInCurrentVersion: bool
    IsCreatedLocal: bool
    IsInProgress: bool
    IsCentral: bool
    IsLocal: bool
    IsWorkshared: bool
    def Dispose(self, ) -> None: ...
    @staticmethod
    def Extract(file: str) -> BasicFileInfo: ...
    def GetDocumentVersion(self, ) -> DocumentVersion: ...

class BeamSystem(Element):
    """.NET: Autodesk.Revit.DB.BeamSystem"""
    def __init__(self, *args) -> None: ...
    Direction: XYZ
    LayoutRule: LayoutRule
    Profile: CurveArray
    BeamSystemType: BeamSystemType
    BeamType: FamilySymbol
    Level: Level
    Elevation: float
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
    def BeamBelongsTo(beam: FamilyInstance) -> BeamSystem: ...
    @staticmethod
    def Create(document: Document, profile: IList, level: Level, curveIndexForDirection: int, is3d: bool) -> BeamSystem: ...
    @staticmethod
    def DropBeamSystem(beamSystem: BeamSystem) -> None: ...
    def GetBeamIds(self, ) -> ICollection: ...

class BeamSystemJustifyType:
    """.NET: Autodesk.Revit.DB.BeamSystemJustifyType"""
    def __init__(self, *args) -> None: ...
    ...

class BeamSystemType(ElementType):
    """.NET: Autodesk.Revit.DB.BeamSystemType"""
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

class BehaviorType:
    """.NET: Autodesk.Revit.DB.BehaviorType"""
    def __init__(self, *args) -> None: ...
    ...

class BendingDetailPositionOptions:
    """.NET: Autodesk.Revit.DB.BendingDetailPositionOptions"""
    def __init__(self, *args) -> None: ...
    ...

class Binding(APIObject):
    """.NET: Autodesk.Revit.DB.Binding"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool

class BindingMap(DefinitionBindingMap):
    """.NET: Autodesk.Revit.DB.BindingMap"""
    def __init__(self, *args) -> None: ...
    Item: Binding
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, key: Definition) -> bool: ...
    def Erase(self, key: Definition) -> int: ...
    def Insert(self, key: Definition, item: Binding, groupTypeId: ForgeTypeId) -> bool: ...
    def ReInsert(self, key: Definition, item: Binding, groupTypeId: ForgeTypeId) -> bool: ...
    def Remove(self, key: Definition) -> bool: ...

class Blend(GenericForm):
    """.NET: Autodesk.Revit.DB.Blend"""
    def __init__(self, *args) -> None: ...
    TopProfile: CurveArrArray
    BottomProfile: CurveArrArray
    TopOffset: float
    BottomOffset: float
    BottomSketch: Sketch
    TopSketch: Sketch
    Subcategory: Category
    Name: str
    IsSolid: bool
    Visible: bool
    Combinations: GeomCombinationSet
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
    def GetVertexConnectionMap(self, ) -> VertexIndexPairArray: ...
    def SetVertexConnectionMap(self, vertexMap: VertexIndexPairArray) -> None: ...

class BooleanOperationsType:
    """.NET: Autodesk.Revit.DB.BooleanOperationsType"""
    def __init__(self, *args) -> None: ...
    ...

class BooleanOperationsUtils:
    """.NET: Autodesk.Revit.DB.BooleanOperationsUtils"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    @staticmethod
    def CutWithHalfSpace(solid: Solid, plane: Plane) -> Solid: ...
    @staticmethod
    def CutWithHalfSpaceModifyingOriginalSolid(solid: Solid, plane: Plane) -> None: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def ExecuteBooleanOperation(solid0: Solid, solid1: Solid, booleanType: BooleanOperationsType) -> Solid: ...
    @staticmethod
    def ExecuteBooleanOperationModifyingOriginalSolid(solid0: Solid, solid1: Solid, booleanType: BooleanOperationsType) -> None: ...

class BorderTile:
    """.NET: Autodesk.Revit.DB.BorderTile"""
    def __init__(self, *args) -> None: ...
    ...

class BoundarySegment:
    """.NET: Autodesk.Revit.DB.BoundarySegment"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ElementId: ElementId
    LinkElementId: ElementId
    def Dispose(self, ) -> None: ...
    def GetCurve(self, ) -> Curve: ...

class BoundaryValidation:
    """.NET: Autodesk.Revit.DB.BoundaryValidation"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    @staticmethod
    def IsValidBoundaryOnSketchPlane(sketchPlane: SketchPlane, curveLoops: IList) -> bool: ...
    @staticmethod
    def IsValidBoundaryOnView(document: Document, viewId: ElementId, curveLoops: IList) -> bool: ...
    @staticmethod
    def IsValidHorizontalBoundary(curveLoops: IList) -> bool: ...

class BoundingBoxContainsPointFilter(ElementQuickFilter):
    """.NET: Autodesk.Revit.DB.BoundingBoxContainsPointFilter"""
    def __init__(self, *args) -> None: ...
    Tolerance: float
    Point: XYZ
    IsValidObject: bool
    Inverted: bool

class BoundingBoxIntersectsFilter(ElementQuickFilter):
    """.NET: Autodesk.Revit.DB.BoundingBoxIntersectsFilter"""
    def __init__(self, *args) -> None: ...
    Tolerance: float
    IsValidObject: bool
    Inverted: bool
    def GetBoundingBox(self, ) -> Outline: ...

class BoundingBoxIsInsideFilter(ElementQuickFilter):
    """.NET: Autodesk.Revit.DB.BoundingBoxIsInsideFilter"""
    def __init__(self, *args) -> None: ...
    Tolerance: float
    IsValidObject: bool
    Inverted: bool
    def GetBoundingBox(self, ) -> Outline: ...

class BoundingBoxUV:
    """.NET: Autodesk.Revit.DB.BoundingBoxUV"""
    def __init__(self, *args) -> None: ...
    Bounds: UV
    Max: UV
    Min: UV
    IsSet: bool
    def Dispose(self, ) -> None: ...

class BoundingBoxXYZ(APIObject):
    """.NET: Autodesk.Revit.DB.BoundingBoxXYZ"""
    def __init__(self, *args) -> None: ...
    IsSet: bool
    Enabled: bool
    BoundEnabled: bool
    MaxEnabled: bool
    MinEnabled: bool
    Bounds: XYZ
    Max: XYZ
    Min: XYZ
    Transform: Transform
    IsReadOnly: bool

class BoxPlacement:
    """.NET: Autodesk.Revit.DB.BoxPlacement"""
    def __init__(self, *args) -> None: ...
    ...

class BrowserOrganization(ElementType):
    """.NET: Autodesk.Revit.DB.BrowserOrganization"""
    def __init__(self, *args) -> None: ...
    SortingParameterId: ElementId
    SortingOrder: SortingOrder
    Type: BrowserOrganizationType
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
    def AreFiltersSatisfied(self, elementId: ElementId) -> bool: ...
    @staticmethod
    def GetCurrentBrowserOrganizationForPanelSchedules(document: Document) -> BrowserOrganization: ...
    @staticmethod
    def GetCurrentBrowserOrganizationForSchedules(document: Document) -> BrowserOrganization: ...
    @staticmethod
    def GetCurrentBrowserOrganizationForSheets(document: Document) -> BrowserOrganization: ...
    @staticmethod
    def GetCurrentBrowserOrganizationForViews(document: Document) -> BrowserOrganization: ...
    def GetFolderItems(self, elementId: ElementId) -> IList: ...
    def GetSortingParameterIdPath(self, ) -> IList: ...

class BrowserOrganizationType:
    """.NET: Autodesk.Revit.DB.BrowserOrganizationType"""
    def __init__(self, *args) -> None: ...
    ...

class BuildingPadType(HostObjAttributes):
    """.NET: Autodesk.Revit.DB.BuildingPadType"""
    def __init__(self, *args) -> None: ...
    ThermalProperties: ThermalProperties
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
    def CreateDefault(document: Document) -> BuildingPadType: ...

class BuildingType:
    """.NET: Autodesk.Revit.DB.BuildingType"""
    def __init__(self, *args) -> None: ...
    ...

class BuiltInCategory:
    """.NET: Autodesk.Revit.DB.BuiltInCategory"""
    def __init__(self, *args) -> None: ...
    ...

class BuiltInFailures:
    """.NET: Autodesk.Revit.DB.BuiltInFailures"""
    def __init__(self, *args) -> None: ...
    ...

class BuiltInParameter:
    """.NET: Autodesk.Revit.DB.BuiltInParameter"""
    def __init__(self, *args) -> None: ...
    ...

class CADExportOptions:
    """.NET: Autodesk.Revit.DB.CADExportOptions"""
    def __init__(self, *args) -> None: ...
    ...

class CADLinkOperations(LinkOperations):
    """.NET: Autodesk.Revit.DB.CADLinkOperations"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class CADLinkOptions:
    """.NET: Autodesk.Revit.DB.CADLinkOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ViewId: ElementId
    PreserveOverrides: bool
    def Dispose(self, ) -> None: ...

class CADLinkType(ElementType):
    """.NET: Autodesk.Revit.DB.CADLinkType"""
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
    def LoadFrom(self, resourceReference: ExternalResourceReference) -> LinkLoadResult: ...
    def Reload(self, options: CADLinkOptions) -> LinkLoadResult: ...

class CameraInfo:
    """.NET: Autodesk.Revit.DB.CameraInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    UpOffset: float
    RightOffset: float
    TargetDistance: float
    NearDistance: float
    FarDistance: float
    HorizontalExtent: float
    VerticalExtent: float
    IsPerspective: bool
    IsPespective: bool
    def Dispose(self, ) -> None: ...

class CancellationListener:
    """.NET: Autodesk.Revit.DB.CancellationListener"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def IsCancelled(self, ) -> bool: ...

class Categories(CategoryNameMap):
    """.NET: Autodesk.Revit.DB.Categories"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    Item: Category
    Item: Category
    IsReadOnly: bool
    def Contains(self, name: str) -> bool: ...
    def ForwardIterator(self, ) -> CategoryNameMapIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, key: str, item: Category) -> bool: ...
    def NewSubcategory(self, parentCategory: Category, name: str) -> Category: ...
    def ReverseIterator(self, ) -> CategoryNameMapIterator: ...

class Category(APIObject):
    """.NET: Autodesk.Revit.DB.Category"""
    def __init__(self, *args) -> None: ...
    IsVisibleInUI: bool
    BuiltInCategory: BuiltInCategory
    CategoryType: CategoryType
    IsTagCategory: bool
    HasMaterialQuantities: bool
    AllowsVisibilityControl: bool
    AllowsBoundParameters: bool
    Visible: bool
    Material: Material
    Id: ElementId
    Parent: Category
    SubCategories: CategoryNameMap
    CanAddSubcategory: bool
    IsCuttable: bool
    LineColor: Color
    Name: str
    IsValid: bool
    IsReadOnly: bool
    @staticmethod
    def GetBuiltInCategory(categoryTypeId: ForgeTypeId) -> BuiltInCategory: ...
    @staticmethod
    def GetBuiltInCategoryDisciplines(categoryId: BuiltInCategory) -> IList: ...
    @staticmethod
    def GetBuiltInCategoryTypeId(categoryId: BuiltInCategory) -> ForgeTypeId: ...
    @staticmethod
    def GetCategory(document: Document, categoryId: ElementId) -> Category: ...
    def GetGraphicsStyle(self, graphicsStyleType: GraphicsStyleType) -> GraphicsStyle: ...
    def GetHashCode(self, ) -> int: ...
    def GetLinePatternId(self, graphicsStyleType: GraphicsStyleType) -> ElementId: ...
    def GetLineWeight(self, graphicsStyleType: GraphicsStyleType) -> Nullable: ...
    @staticmethod
    def IsBuiltInCategory(categoryTypeId: ForgeTypeId) -> bool: ...
    @staticmethod
    def IsBuiltInCategoryValid(builtInCategory: BuiltInCategory) -> bool: ...
    def SetLinePatternId(self, linePatternId: ElementId, graphicsStyleType: GraphicsStyleType) -> None: ...
    def SetLineWeight(self, lineWeight: int, graphicsStyleType: GraphicsStyleType) -> None: ...

class CategoryNameMap(APIObject):
    """.NET: Autodesk.Revit.DB.CategoryNameMap"""
    def __init__(self, *args) -> None: ...
    Item: Category
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, key: str) -> bool: ...
    def Erase(self, key: str) -> int: ...
    def ForwardIterator(self, ) -> CategoryNameMapIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, key: str, item: Category) -> bool: ...
    def ReverseIterator(self, ) -> CategoryNameMapIterator: ...

class CategoryNameMapIterator(APIObject):
    """.NET: Autodesk.Revit.DB.CategoryNameMapIterator"""
    def __init__(self, *args) -> None: ...
    Key: str
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class CategorySet(APIObject):
    """.NET: Autodesk.Revit.DB.CategorySet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: Category) -> bool: ...
    def Erase(self, item: Category) -> int: ...
    def ForwardIterator(self, ) -> CategorySetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: Category) -> bool: ...
    def ReverseIterator(self, ) -> CategorySetIterator: ...

class CategorySetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.CategorySetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class CategoryType:
    """.NET: Autodesk.Revit.DB.CategoryType"""
    def __init__(self, *args) -> None: ...
    ...

class Ceiling(CeilingAndFloor):
    """.NET: Autodesk.Revit.DB.Ceiling"""
    def __init__(self, *args) -> None: ...
    SketchId: ElementId
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
    def Create(document: Document, curveLoops: IList, ceilingTypeId: ElementId, levelId: ElementId, slopeArrow: Line, slope: float) -> Ceiling: ...
    def GetCeilingGridLines(self, includeBoundary: bool) -> IList: ...

class CeilingAndFloor(HostObject):
    """.NET: Autodesk.Revit.DB.CeilingAndFloor"""
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

class CeilingType(HostObjAttributes):
    """.NET: Autodesk.Revit.DB.CeilingType"""
    def __init__(self, *args) -> None: ...
    ThermalProperties: ThermalProperties
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

class CellType:
    """.NET: Autodesk.Revit.DB.CellType"""
    def __init__(self, *args) -> None: ...
    ...

class ChangePriority:
    """.NET: Autodesk.Revit.DB.ChangePriority"""
    def __init__(self, *args) -> None: ...
    ...

class ChangeType:
    """.NET: Autodesk.Revit.DB.ChangeType"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    @staticmethod
    def ConcatenateChangeTypes(changeType1: ChangeType, changeType2: ChangeType) -> ChangeType: ...
    def Contains(self, changeType: ChangeType) -> bool: ...
    def Dispose(self, ) -> None: ...
    def IsIdentical(self, changeType: ChangeType) -> bool: ...

class CheckoutStatus:
    """.NET: Autodesk.Revit.DB.CheckoutStatus"""
    def __init__(self, *args) -> None: ...
    ...

class City(APIObject):
    """.NET: Autodesk.Revit.DB.City"""
    def __init__(self, *args) -> None: ...
    TimeZone: float
    Longitude: float
    Latitude: float
    WeatherStation: str
    Name: str
    IsReadOnly: bool

class CitySet(APIObject):
    """.NET: Autodesk.Revit.DB.CitySet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: City) -> bool: ...
    def Erase(self, item: City) -> int: ...
    def ForwardIterator(self, ) -> CitySetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: City) -> bool: ...
    def ReverseIterator(self, ) -> CitySetIterator: ...

class CitySetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.CitySetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ClassificationEntries(KeyBasedTreeEntries):
    """.NET: Autodesk.Revit.DB.ClassificationEntries"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    @staticmethod
    def LoadClassificationEntriesFromFile(filePath: str, loadContent: KeyBasedTreeEntriesLoadContent) -> bool: ...

class ClassificationEntry(KeyBasedTreeEntry):
    """.NET: Autodesk.Revit.DB.ClassificationEntry"""
    def __init__(self, *args) -> None: ...
    Description: str
    CategoryId: ElementId
    Level: int
    IsValidObject: bool
    ParentKey: str
    Key: str
    def HasBadCategoryId(self, ) -> bool: ...
    def HasBadLevel(self, ) -> bool: ...
    def HasInvalidKey(self, ) -> bool: ...

class ClosestPointsPairBetweenTwoCurves:
    """.NET: Autodesk.Revit.DB.ClosestPointsPairBetweenTwoCurves"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Distance: float
    ParameterOnSecondCurve: float
    ParameterOnFirstCurve: float
    XYZPointOnSecondCurve: XYZ
    XYZPointOnFirstCurve: XYZ
    def Dispose(self, ) -> None: ...

class Color(APIObject):
    """.NET: Autodesk.Revit.DB.Color"""
    def __init__(self, *args) -> None: ...
    InvalidColorValue: Color
    IsValid: bool
    Blue: int
    Green: int
    Red: int
    IsReadOnly: bool

class ColorBackgroundSettings(BackgroundSettings):
    """.NET: Autodesk.Revit.DB.ColorBackgroundSettings"""
    def __init__(self, *args) -> None: ...
    Color: Color
    IsValidObject: bool

class ColorDepthType:
    """.NET: Autodesk.Revit.DB.ColorDepthType"""
    def __init__(self, *args) -> None: ...
    ...

class ColorFillLegend(Element):
    """.NET: Autodesk.Revit.DB.ColorFillLegend"""
    def __init__(self, *args) -> None: ...
    Origin: XYZ
    Height: float
    ColorFillCategoryId: ElementId
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
    def Create(document: Document, viewId: ElementId, catetoryId: ElementId, origin: XYZ) -> ColorFillLegend: ...
    def GetColumnWidths(self, ) -> IList: ...
    def SetColumnWidths(self, widths: IList) -> None: ...

class ColorFillScheme(Element):
    """.NET: Autodesk.Revit.DB.ColorFillScheme"""
    def __init__(self, *args) -> None: ...
    ParameterDefinition: ElementId
    AreaSchemeId: ElementId
    IsLinkedFilesIncluded: bool
    IsByRange: bool
    StorageType: StorageType
    CategoryId: ElementId
    Title: str
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
    def AddEntry(self, entry: ColorFillSchemeEntry) -> None: ...
    def AreEntriesConsistentWithScheme(self, entries: IList) -> EntryAndSchemeConsistency: ...
    def CanDefineByRange(self, ) -> bool: ...
    def CanRemoveEntry(self, entry: ColorFillSchemeEntry) -> bool: ...
    def CanUpdateEntry(self, entry: ColorFillSchemeEntry) -> bool: ...
    def Duplicate(self, name: str) -> ElementId: ...
    def GetEntries(self, ) -> IList: ...
    def GetFormatOptions(self, ) -> FormatOptions: ...
    def GetSupportedParameterIds(self, ) -> IList: ...
    def IsEntryConsistentWithScheme(self, entry: ColorFillSchemeEntry) -> EntryAndSchemeConsistency: ...
    def IsValidParameterDefinitionId(self, parameterId: ElementId) -> bool: ...
    def IsValidSchemeName(self, name: str) -> bool: ...
    def RemoveEntry(self, entry: ColorFillSchemeEntry) -> None: ...
    def SetEntries(self, entries: IList) -> None: ...
    def SetFormatOptions(self, formatOptions: FormatOptions) -> None: ...
    def SortEntries(self, ) -> None: ...
    def UpdateEntry(self, entry: ColorFillSchemeEntry) -> None: ...

class ColorFillSchemeEntry:
    """.NET: Autodesk.Revit.DB.ColorFillSchemeEntry"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Caption: str
    StorageType: StorageType
    IsVisible: bool
    IsInUse: bool
    FillPatternId: ElementId
    Color: Color
    def CanSetValue(self, value: ElementId) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetDoubleValue(self, ) -> float: ...
    def GetElementIdValue(self, ) -> ElementId: ...
    def GetIntegerValue(self, ) -> int: ...
    def GetStringValue(self, ) -> str: ...
    def SetDoubleValue(self, value: float) -> None: ...
    def SetElementIdValue(self, value: ElementId) -> None: ...
    def SetIntegerValue(self, value: int) -> None: ...
    def SetStringValue(self, value: str) -> None: ...

class ColorOptions:
    """.NET: Autodesk.Revit.DB.ColorOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    EditingColor: Color
    CalculatingColor: Color
    AlertColor: Color
    PreselectionColor: Color
    SelectionSemitransparent: bool
    SelectionColor: Color
    BackgroundColor: Color
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetColorOptions() -> ColorOptions: ...

class ColorWithTransparency:
    """.NET: Autodesk.Revit.DB.ColorWithTransparency"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetBlue(self, ) -> int: ...
    def GetColor(self, ) -> Color: ...
    def GetGreen(self, ) -> int: ...
    def GetRed(self, ) -> int: ...
    def GetTransparency(self, ) -> int: ...
    def SetBlue(self, blue: int) -> None: ...
    def SetColor(self, color: Color) -> None: ...
    def SetGreen(self, green: int) -> None: ...
    def SetRed(self, red: int) -> None: ...
    def SetTransparency(self, transparency: int) -> None: ...

class ColumnAttachment:
    """.NET: Autodesk.Revit.DB.ColumnAttachment"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    CutStyle: ColumnAttachmentCutStyle
    Justification: ColumnAttachmentJustification
    BaseOrTop: int
    TargetId: ElementId
    AttachOffset: float
    @staticmethod
    def AddColumnAttachment(doc: Document, column: FamilyInstance, target: Element, baseOrTop: int, cutColumnStyle: ColumnAttachmentCutStyle, justification: ColumnAttachmentJustification, attachOffset: float) -> None: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetColumnAttachment(column: FamilyInstance, targetId: ElementId) -> ColumnAttachment: ...
    @staticmethod
    def IsValidColumn(familyInstance: FamilyInstance) -> bool: ...
    @staticmethod
    def IsValidTarget(forSlantedColumn: bool, target: Element) -> bool: ...
    @staticmethod
    def RemoveColumnAttachment(column: FamilyInstance, targetId: ElementId) -> None: ...
    def SetJustification(self, justification: ColumnAttachmentJustification) -> None: ...

class ColumnAttachmentCutStyle:
    """.NET: Autodesk.Revit.DB.ColumnAttachmentCutStyle"""
    def __init__(self, *args) -> None: ...
    ...

class ColumnAttachmentJustification:
    """.NET: Autodesk.Revit.DB.ColumnAttachmentJustification"""
    def __init__(self, *args) -> None: ...
    ...

class CombinableElement(Element):
    """.NET: Autodesk.Revit.DB.CombinableElement"""
    def __init__(self, *args) -> None: ...
    Combinations: GeomCombinationSet
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

class CombinableElementArray(APIObject):
    """.NET: Autodesk.Revit.DB.CombinableElementArray"""
    def __init__(self, *args) -> None: ...
    Item: CombinableElement
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: CombinableElement) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> CombinableElementArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: CombinableElement, index: int) -> None: ...
    def ReverseIterator(self, ) -> CombinableElementArrayIterator: ...

class CombinableElementArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.CombinableElementArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ComponentRepeater(Element):
    """.NET: Autodesk.Revit.DB.ComponentRepeater"""
    def __init__(self, *args) -> None: ...
    DimensionCount: int
    DefaultFamilyType: ElementId
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
    def CanElementBeRepeated(ADoc: Document, elementId: ElementId) -> bool: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IsTypeValidForRepeater(self, typeId: ElementId) -> bool: ...
    @staticmethod
    def RemoveRepeaters(document: Document, elementIds: ISet) -> ISet: ...
    @staticmethod
    def RepeatElements(document: Document, elementIds: ICollection) -> IList: ...

class ComponentRepeaterIterator:
    """.NET: Autodesk.Revit.DB.ComponentRepeaterIterator"""
    def __init__(self, *args) -> None: ...
    Current: ComponentRepeaterSlot
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetCurrent(self, ) -> ComponentRepeaterSlot: ...
    def IsDone(self, ) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ComponentRepeaterSlot(Element):
    """.NET: Autodesk.Revit.DB.ComponentRepeaterSlot"""
    def __init__(self, *args) -> None: ...
    FamilyType: ElementId
    IsDefault: bool
    IsEmpty: bool
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
    def IsTypeValidForSlot(self, typeId: ElementId) -> bool: ...
    def MakeDefault(self, ) -> None: ...
    def MakeEmpty(self, ) -> None: ...

class ComponentRotation:
    """.NET: Autodesk.Revit.DB.ComponentRotation"""
    def __init__(self, *args) -> None: ...
    ...

class CompoundStructure:
    """.NET: Autodesk.Revit.DB.CompoundStructure"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    MinimumSampleHeight: float
    CutoffHeight: float
    SampleHeight: float
    StructuralMaterialIndex: int
    VariableLayerIndex: int
    OpeningWrapping: OpeningWrappingCondition
    EndCap: EndCapCondition
    HasStructuralDeck: bool
    IsVerticallyCompound: bool
    LayerCount: int
    IsEmpty: bool
    def AddWallSweep(self, wallSweepInfo: WallSweepInfo) -> None: ...
    def AssociateRegionWithLayer(self, regionId: int, layerIdx: int) -> None: ...
    def CanLayerBeStructuralMaterial(self, layerIndex: int) -> bool: ...
    def CanLayerBeVariable(self, variableLayerIndex: int) -> bool: ...
    def CanLayerWidthBeNonZero(self, layerIdx: int) -> bool: ...
    def CanSplitAndMergeRegionsBeUsed(self, ) -> bool: ...
    def ChangeRegionWidth(self, regionId: int, newWidth: float) -> bool: ...
    def ClearWallSweeps(self, wallSweepType: WallSweepType) -> None: ...
    @staticmethod
    def CreateSimpleCompoundStructure(layers: IList) -> CompoundStructure: ...
    @staticmethod
    def CreateSingleLayerCompoundStructure(sampleHeight: float, layerFunction: MaterialFunctionAssignment, width: float, materialId: ElementId) -> CompoundStructure: ...
    def DeleteLayer(self, layerIdx: int) -> bool: ...
    def Dispose(self, ) -> None: ...
    def FindEnclosingRegionAndSegments(self, gridUV: UV, splitDirection: RectangularGridSegmentOrientation, segmentId1: int, segmentId2: int) -> int: ...
    def GetAdjacentRegions(self, segmentId: int) -> IList: ...
    def GetCoreBoundaryLayerIndex(self, shellLayerType: ShellLayerType) -> int: ...
    def GetDeckEmbeddingType(self, layerIdx: int) -> StructDeckEmbeddingType: ...
    def GetDeckProfileId(self, layerIdx: int) -> ElementId: ...
    def GetExtendableRegionIds(self, top: bool) -> IList: ...
    def GetFirstCoreLayerIndex(self, ) -> int: ...
    def GetLastCoreLayerIndex(self, ) -> int: ...
    def GetLayerAssociatedToRegion(self, regionId: int) -> int: ...
    def GetLayerFunction(self, layerIdx: int) -> MaterialFunctionAssignment: ...
    def GetLayerPriority(self, layerIdx: int) -> int: ...
    def GetLayerWidth(self, layerIdx: int) -> float: ...
    def GetLayers(self, ) -> IList: ...
    def GetMaterialId(self, layerIdx: int) -> ElementId: ...
    @staticmethod
    def GetMinimumLayerThickness() -> float: ...
    def GetNumberOfShellLayers(self, shellLayerType: ShellLayerType) -> int: ...
    def GetOffsetForLocationLine(self, wallLocationLine: WallLocationLine) -> float: ...
    def GetPreviousNonZeroLayerIndex(self, thisIdx: int) -> int: ...
    def GetRegionEnvelope(self, regionId: int) -> BoundingBoxUV: ...
    def GetRegionIds(self, ) -> IList: ...
    def GetRegionsAlongLevel(self, height: float) -> IList: ...
    def GetRegionsAssociatedToLayer(self, layerIdx: int) -> IList: ...
    def GetSegmentCoordinate(self, segmentId: int) -> float: ...
    def GetSegmentEndPoints(self, segmentId: int, regionId: int, end1: UV, end2: UV) -> None: ...
    def GetSegmentIds(self, ) -> IList: ...
    def GetSegmentOrientation(self, segmentId: int) -> RectangularGridSegmentOrientation: ...
    def GetSimpleCompoundStructure(self, wallHeight: float, distAboveBase: float) -> CompoundStructure: ...
    def GetWallSweepsInfo(self, wallSweepType: WallSweepType) -> IList: ...
    def GetWidth(self, regionId: int) -> float: ...
    def IsCoreLayer(self, layerIdx: int) -> bool: ...
    def IsEqual(self, otherStructure: CompoundStructure) -> bool: ...
    def IsLayerValid(self, layerIdx: int, layer: CompoundStructureLayer) -> bool: ...
    def IsRectangularRegion(self, regionId: int) -> bool: ...
    def IsSimpleRegion(self, regionId: int) -> bool: ...
    def IsStructuralDeck(self, layerIdx: int) -> bool: ...
    def IsValid(self, doc: Document, errMap: IDictionary, twoLayerErrorsMap: IDictionary) -> bool: ...
    def IsValidLayerPriority(self, layerIdx: int, priority: int) -> bool: ...
    def IsValidRegionId(self, regionId: int) -> bool: ...
    def IsValidSampleHeight(self, height: float) -> bool: ...
    def IsValidSegmentId(self, segmentId: int) -> bool: ...
    def IsVerticallyHomogeneous(self, ) -> bool: ...
    def MergeRegionsAdjacentToSegment(self, segmentId: int, layerIdxForMergedRegion: int) -> int: ...
    def ParticipatesInWrapping(self, layerIdx: int) -> bool: ...
    def RemoveWallSweep(self, wallSweepType: WallSweepType, id: int) -> None: ...
    def ResetAllLayersPriorities(self, ) -> None: ...
    def ResetLayerPriority(self, layerIdx: int) -> None: ...
    def SetDeckEmbeddingType(self, layerIdx: int, embedType: StructDeckEmbeddingType) -> None: ...
    def SetDeckProfileId(self, layerIdx: int, profileId: ElementId) -> None: ...
    def SetExtendableRegionIds(self, top: bool, regionIds: IList) -> None: ...
    def SetLayer(self, layerIdx: int, layer: CompoundStructureLayer) -> None: ...
    def SetLayerFunction(self, layerIdx: int, function: MaterialFunctionAssignment) -> None: ...
    def SetLayerPriority(self, layerIdx: int, priority: int) -> None: ...
    def SetLayerWidth(self, layerIdx: int, width: float) -> None: ...
    def SetLayers(self, layers: IList) -> None: ...
    def SetMaterialId(self, layerIdx: int, materialId: ElementId) -> None: ...
    def SetNumberOfShellLayers(self, shellLayerType: ShellLayerType, numLayers: int) -> None: ...
    def SetParticipatesInWrapping(self, layerIdx: int, participatesInWrapping: bool) -> None: ...
    def SplitRegion(self, gridUV: UV, splitDirection: RectangularGridSegmentOrientation, newSegmentId: int) -> int: ...

class CompoundStructureError:
    """.NET: Autodesk.Revit.DB.CompoundStructureError"""
    def __init__(self, *args) -> None: ...
    ...

class CompoundStructureLayer:
    """.NET: Autodesk.Revit.DB.CompoundStructureLayer"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LayerCapFlag: bool
    LayerId: int
    DeckEmbeddingType: StructDeckEmbeddingType
    LayerPriority: int
    Function: MaterialFunctionAssignment
    DeckProfileId: ElementId
    MaterialId: ElementId
    Width: float
    def Dispose(self, ) -> None: ...

class ConfigurationReloadInfo:
    """.NET: Autodesk.Revit.DB.ConfigurationReloadInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    OutOfDatePartCount: int
    ProfileNotAvailable: bool
    Disconnects: int
    def Dispose(self, ) -> None: ...
    def GetConnectivityValidation(self, ) -> ConnectionValidationInfo: ...
    def GetCustomDataChangedElements(self, ) -> ISet: ...
    def GetOutOfDatePartStatus(self, index: int) -> ReloadSwapOutInfo: ...

class ConicalFace(Face):
    """.NET: Autodesk.Revit.DB.ConicalFace"""
    def __init__(self, *args) -> None: ...
    HalfAngle: float
    Radius: XYZ
    Axis: XYZ
    Origin: XYZ
    Period: float
    IsCyclic: bool
    Area: float
    Reference: Reference
    IsTwoSided: bool
    MaterialElementId: ElementId
    EdgeLoops: EdgeArrayArray
    HasRegions: bool
    OrientationMatchesSurfaceOrientation: bool
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool

class ConicalSurface(Surface):
    """.NET: Autodesk.Revit.DB.ConicalSurface"""
    def __init__(self, *args) -> None: ...
    HalfAngle: float
    Origin: XYZ
    YDir: XYZ
    XDir: XYZ
    Axis: XYZ
    IsValidObject: bool
    OrientationMatchesParametricOrientation: bool
    @staticmethod
    def Create(frameOfReference: Frame, halfAngle: float) -> ConicalSurface: ...
    def GetFrameOfReference(self, ) -> Frame: ...
    @staticmethod
    def IsValidConeAngle(halfAngle: float) -> bool: ...

class ConnectionResolution:
    """.NET: Autodesk.Revit.DB.ConnectionResolution"""
    def __init__(self, *args) -> None: ...
    ...

class ConnectionValidationInfo:
    """.NET: Autodesk.Revit.DB.ConnectionValidationInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetWarning(self, index: int) -> ConnectionValidationWarning: ...
    def IsValidWarningIndex(self, index: int) -> bool: ...
    def ManyWarnings(self, ) -> int: ...

class ConnectionValidationWarning:
    """.NET: Autodesk.Revit.DB.ConnectionValidationWarning"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Reason: ConnectionWarning
    Resolution: ConnectionResolution
    def Dispose(self, ) -> None: ...
    def GetParts(self, ) -> ISet: ...

class ConnectionWarning:
    """.NET: Autodesk.Revit.DB.ConnectionWarning"""
    def __init__(self, *args) -> None: ...
    ...

class Connector:
    """.NET: Autodesk.Revit.DB.Connector"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    PressureDrop: float
    Coefficient: float
    VelocityPressure: float
    Direction: FlowDirectionType
    Flow: float
    Id: int
    Description: str
    Utility: bool
    AllowsSlopeAdjustments: bool
    GasketLength: float
    EngagementLength: float
    IsMovable: bool
    Angle: float
    AssignedKCoefficient: float
    AssignedFixtureUnits: float
    AssignedFlow: float
    AssignedPressureDrop: float
    AssignedPipeLossMethod: PipeLossMethodType
    AssignedDuctLossMethod: DuctLossMethodType
    AssignedDuctFlowConfiguration: DuctFlowConfigurationType
    AssignedPipeFlowConfiguration: PipeFlowConfigurationType
    AssignedLossCoefficient: float
    AssignedFlowFactor: float
    IsConnected: bool
    MEPSystem: MEPSystem
    ConnectorManager: ConnectorManager
    Demand: float
    PipeSystemType: PipeSystemType
    ElectricalSystemType: ElectricalSystemType
    DuctSystemType: DuctSystemType
    AssignedFlowDirection: FlowDirectionType
    Radius: float
    Height: float
    Width: float
    Shape: ConnectorProfileType
    ConnectorType: ConnectorType
    AllRefs: ConnectorSet
    Domain: Domain
    Owner: Element
    CoordinateSystem: Transform
    Origin: XYZ
    def ConnectTo(self, connector: Connector) -> None: ...
    def DisconnectFrom(self, connector: Connector) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetFabricationConnectorInfo(self, ) -> FabricationConnectorInfo: ...
    def GetMEPConnectorInfo(self, ) -> MEPConnectorInfo: ...
    def IsConnectedTo(self, connector: Connector) -> bool: ...

class ConnectorDomainType:
    """.NET: Autodesk.Revit.DB.ConnectorDomainType"""
    def __init__(self, *args) -> None: ...
    ...

class ConnectorElement(Element):
    """.NET: Autodesk.Revit.DB.ConnectorElement"""
    def __init__(self, *args) -> None: ...
    Direction: XYZ
    SystemClassification: MEPSystemClassification
    IsPrimary: bool
    Radius: float
    Height: float
    Width: float
    Shape: ConnectorProfileType
    Domain: Domain
    Origin: XYZ
    CoordinateSystem: Transform
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
    def AssignAsPrimary(self, ) -> None: ...
    def ChangeHostReference(self, planarFace: Reference, edge: Edge) -> None: ...
    @staticmethod
    def CreateCableTrayConnector(document: Document, planarFace: Reference, edge: Edge) -> ConnectorElement: ...
    @staticmethod
    def CreateConduitConnector(document: Document, planarFace: Reference, edge: Edge) -> ConnectorElement: ...
    @staticmethod
    def CreateDuctConnector(document: Document, ductSystemType: DuctSystemType, profileShape: ConnectorProfileType, planarFace: Reference, edge: Edge) -> ConnectorElement: ...
    @staticmethod
    def CreateElectricalConnector(document: Document, electricalSystemType: ElectricalSystemType, planarFace: Reference, edge: Edge) -> ConnectorElement: ...
    @staticmethod
    def CreatePipeConnector(document: Document, pipeSystemType: PipeSystemType, planarFace: Reference, edge: Edge) -> ConnectorElement: ...
    def FlipDirection(self, ) -> None: ...
    def GetLinkedConnectorElement(self, ) -> ConnectorElement: ...
    def IsSystemClassificationValid(self, systemClassification: MEPSystemClassification) -> bool: ...
    def SetLinkedConnectorElement(self, otherConnector: ConnectorElement) -> None: ...

class ConnectorGenderType:
    """.NET: Autodesk.Revit.DB.ConnectorGenderType"""
    def __init__(self, *args) -> None: ...
    ...

class ConnectorJointType:
    """.NET: Autodesk.Revit.DB.ConnectorJointType"""
    def __init__(self, *args) -> None: ...
    ...

class ConnectorManager:
    """.NET: Autodesk.Revit.DB.ConnectorManager"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Owner: Element
    UnusedConnectors: ConnectorSet
    Connectors: ConnectorSet
    def Dispose(self, ) -> None: ...
    def Lookup(self, index: int) -> Connector: ...

class ConnectorProfileType:
    """.NET: Autodesk.Revit.DB.ConnectorProfileType"""
    def __init__(self, *args) -> None: ...
    ...

class ConnectorSet(APIObject):
    """.NET: Autodesk.Revit.DB.ConnectorSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: Connector) -> bool: ...
    def Erase(self, item: Connector) -> int: ...
    def ForwardIterator(self, ) -> ConnectorSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: Connector) -> bool: ...
    def ReverseIterator(self, ) -> ConnectorSetIterator: ...

class ConnectorSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.ConnectorSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ConnectorType:
    """.NET: Autodesk.Revit.DB.ConnectorType"""
    def __init__(self, *args) -> None: ...
    ...

class Construction:
    """.NET: Autodesk.Revit.DB.Construction"""
    def __init__(self, *args) -> None: ...
    Name: str
    Id: str

class ContentNode(RenderNode):
    """.NET: Autodesk.Revit.DB.ContentNode"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    NodeName: str
    def GetAsset(self, ) -> Asset: ...
    def GetTransform(self, ) -> Transform: ...

class ContourSetting:
    """.NET: Autodesk.Revit.DB.ContourSetting"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def AddContourRange(self, start: float, stop: float, step: float, subcategoryId: ElementId) -> ContourSettingItem: ...
    def AddSingleContour(self, elevation: float, subcategoryId: ElementId) -> ContourSettingItem: ...
    def DisableItem(self, item: ContourSettingItem) -> None: ...
    def Dispose(self, ) -> None: ...
    def EnableItem(self, item: ContourSettingItem) -> None: ...
    def GetContourSettingItems(self, ) -> IList: ...
    def GetItemIndex(self, item: ContourSettingItem) -> int: ...
    def IsItemEnabled(self, item: ContourSettingItem) -> bool: ...
    def RemoveItem(self, item: ContourSettingItem) -> None: ...

class ContourSettingItem:
    """.NET: Autodesk.Revit.DB.ContourSettingItem"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Type: ContourSettingItemType
    SubCategoryId: ElementId
    Step: float
    Stop: float
    Start: float
    def Dispose(self, ) -> None: ...

class ContourSettingItemType:
    """.NET: Autodesk.Revit.DB.ContourSettingItemType"""
    def __init__(self, *args) -> None: ...
    ...

class Control(Element):
    """.NET: Autodesk.Revit.DB.Control"""
    def __init__(self, *args) -> None: ...
    View: View
    Origin: XYZ
    Shape: ControlShape
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

class ControlShape:
    """.NET: Autodesk.Revit.DB.ControlShape"""
    def __init__(self, *args) -> None: ...
    ...

class CoordinatePlaneVisibility:
    """.NET: Autodesk.Revit.DB.CoordinatePlaneVisibility"""
    def __init__(self, *args) -> None: ...
    ...

class CopyPasteOptions:
    """.NET: Autodesk.Revit.DB.CopyPasteOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetDuplicateTypeNamesHandler(self, ) -> IDuplicateTypeNamesHandler: ...
    def SetDuplicateTypeNamesHandler(self, handler: IDuplicateTypeNamesHandler) -> None: ...

class CurtainCell(APIObject):
    """.NET: Autodesk.Revit.DB.CurtainCell"""
    def __init__(self, *args) -> None: ...
    CurveLoops: CurveArrArray
    PlanarizedCurveLoops: CurveArrArray
    IsReadOnly: bool

class CurtainGrid(APIObject):
    """.NET: Autodesk.Revit.DB.CurtainGrid"""
    def __init__(self, *args) -> None: ...
    NumPanels: int
    NumVLines: int
    NumULines: int
    Grid2Offset: float
    Grid2Angle: float
    Grid2Justification: CurtainGridAlignType
    Grid1Offset: float
    Grid1Angle: float
    Grid1Justification: CurtainGridAlignType
    IsReadOnly: bool
    def AddGridLine(self, isUGridLine: bool, position: XYZ, oneSegmentOnly: bool) -> CurtainGridLine: ...
    def ChangePanelType(self, panel: Element, newSymbol: ElementType) -> Element: ...
    def GetCell(self, uGridLineId: ElementId, vGridLineId: ElementId) -> CurtainCell: ...
    def GetCurtainCells(self, ) -> ICollection: ...
    def GetMullionIds(self, ) -> ICollection: ...
    def GetPanel(self, uGridLineId: ElementId, vGridLineId: ElementId) -> Panel: ...
    def GetPanelIds(self, ) -> ICollection: ...
    def GetUGridLineIds(self, ) -> ICollection: ...
    def GetUnlockedMullionIds(self, ) -> ICollection: ...
    def GetUnlockedPanelIds(self, ) -> ICollection: ...
    def GetVGridLineIds(self, ) -> ICollection: ...

class CurtainGridAlignType:
    """.NET: Autodesk.Revit.DB.CurtainGridAlignType"""
    def __init__(self, *args) -> None: ...
    ...

class CurtainGridLine(HostObject):
    """.NET: Autodesk.Revit.DB.CurtainGridLine"""
    def __init__(self, *args) -> None: ...
    ExistingSegmentCurves: CurveArray
    SkippedSegmentCurves: CurveArray
    AllSegmentCurves: CurveArray
    FullCurve: Curve
    IsUGridLine: bool
    Lock: bool
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
    def AddAllSegments(self, ) -> None: ...
    def AddMullions(self, segment: Curve, mullionType: MullionType, oneSegmentOnly: bool) -> ElementSet: ...
    def AddSegment(self, curve: Curve) -> None: ...
    def RemoveSegment(self, curve: Curve) -> None: ...

class CurtainGridSet(APIObject):
    """.NET: Autodesk.Revit.DB.CurtainGridSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: CurtainGrid) -> bool: ...
    def Erase(self, item: CurtainGrid) -> int: ...
    def ForwardIterator(self, ) -> CurtainGridSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: CurtainGrid) -> bool: ...
    def ReverseIterator(self, ) -> CurtainGridSetIterator: ...

class CurtainGridSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.CurtainGridSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class CurtainSystem(CurtainSystemBase):
    """.NET: Autodesk.Revit.DB.CurtainSystem"""
    def __init__(self, *args) -> None: ...
    CurtainSystemType: CurtainSystemType
    CurtainGrids: CurtainGridSet
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
    def AddCurtainGrid(self, face: Reference) -> None: ...
    def RemoveCurtainGrid(self, face: Reference) -> None: ...

class CurtainSystemBase(HostObject):
    """.NET: Autodesk.Revit.DB.CurtainSystemBase"""
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

class CurtainSystemType(HostObjAttributes):
    """.NET: Autodesk.Revit.DB.CurtainSystemType"""
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

class Curve(GeometryObject):
    """.NET: Autodesk.Revit.DB.Curve"""
    def __init__(self, *args) -> None: ...
    Period: float
    IsCyclic: bool
    Length: float
    ApproximateLength: float
    Reference: Reference
    IsClosed: bool
    IsBound: bool
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool
    def Clone(self, ) -> Curve: ...
    def ComputeClosestPoints(self, otherCurve: Curve, withinThisCurveBounds: bool, withinOtherCurveBounds: bool, returnAllCriticalPnts: bool, resultList: IList) -> None: ...
    def ComputeDerivatives(self, parameter: float, normalized: bool) -> Transform: ...
    def ComputeNormalizedParameter(self, rawParameter: float) -> float: ...
    def ComputeRawParameter(self, normalizedParameter: float) -> float: ...
    def CreateOffset(self, offsetDist: float, referenceVector: XYZ) -> Curve: ...
    def CreateReversed(self, ) -> Curve: ...
    def CreateTransformed(self, transform: Transform) -> Curve: ...
    def Distance(self, point: XYZ) -> float: ...
    def Evaluate(self, parameter: float, normalized: bool) -> XYZ: ...
    def GetEndParameter(self, index: int) -> float: ...
    def GetEndPoint(self, index: int) -> XYZ: ...
    def GetEndPointReference(self, index: int) -> Reference: ...
    def Intersect(self, curve: Curve, option: CurveIntersectResultOption) -> CurveIntersectResult: ...
    def IsInside(self, parameter: float, end: int) -> bool: ...
    def MakeBound(self, startParameter: float, endParameter: float) -> None: ...
    def MakeUnbound(self, ) -> None: ...
    def Project(self, point: XYZ) -> IntersectionResult: ...
    def SetGraphicsStyleId(self, id: ElementId) -> None: ...
    def Tessellate(self, ) -> IList: ...

class CurveArrArray(APIObject):
    """.NET: Autodesk.Revit.DB.CurveArrArray"""
    def __init__(self, *args) -> None: ...
    Item: CurveArray
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: CurveArray) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> CurveArrArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: CurveArray, index: int) -> None: ...
    def ReverseIterator(self, ) -> CurveArrArrayIterator: ...

class CurveArrArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.CurveArrArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class CurveArray(APIObject):
    """.NET: Autodesk.Revit.DB.CurveArray"""
    def __init__(self, *args) -> None: ...
    Item: Curve
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: Curve) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> CurveArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: Curve, index: int) -> None: ...
    def ReverseIterator(self, ) -> CurveArrayIterator: ...

class CurveArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.CurveArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class CurveByPoints(CurveElement):
    """.NET: Autodesk.Revit.DB.CurveByPoints"""
    def __init__(self, *args) -> None: ...
    ReferenceType: ReferenceType
    Visible: bool
    Subcategory: GraphicsStyle
    IsReferenceLine: bool
    SketchPlane: SketchPlane
    SupportsTangentLocks: bool
    CurveElementType: CurveElementType
    LineStyle: Element
    CenterPointReference: Reference
    GeometryCurve: Curve
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
    def GetPoints(self, ) -> ReferencePointArray: ...
    def GetVisibility(self, ) -> FamilyElementVisibility: ...
    def SetPoints(self, points: ReferencePointArray) -> None: ...
    def SetVisibility(self, visibility: FamilyElementVisibility) -> None: ...
    @staticmethod
    def SortPoints(arr: ReferencePointArray) -> bool: ...

class CurveByPointsArray(APIObject):
    """.NET: Autodesk.Revit.DB.CurveByPointsArray"""
    def __init__(self, *args) -> None: ...
    Item: CurveByPoints
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: CurveByPoints) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> CurveByPointsArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: CurveByPoints, index: int) -> None: ...
    def ReverseIterator(self, ) -> CurveByPointsArrayIterator: ...

class CurveByPointsArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.CurveByPointsArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class CurveByPointsUtils:
    """.NET: Autodesk.Revit.DB.CurveByPointsUtils"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    @staticmethod
    def AddCurvesToFaceRegion(document: Document, curveElemIds: IList) -> None: ...
    @staticmethod
    def CreateArcThroughPoints(document: Document, startPoint: ReferencePoint, endPoint: ReferencePoint, interiorPoint: ReferencePoint) -> CurveElement: ...
    @staticmethod
    def CreateRectangle(document: Document, startPoint: ReferencePoint, endPoint: ReferencePoint, projectionType: CurveProjectionType, boundaryReferenceLines: bool, boundaryCurvesFollowSurface: bool, createdCurvesIds: IList, createdCornersIds: IList) -> None: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetFaceRegions(cda: Document, referenceOfFace: Reference) -> IList: ...
    @staticmethod
    def GetHostFace(curveElem: CurveElement) -> Reference: ...
    @staticmethod
    def GetProjectionType(curveElem: CurveElement) -> CurveProjectionType: ...
    @staticmethod
    def GetSketchOnSurface(curveElem: CurveElement) -> bool: ...
    @staticmethod
    def SetProjectionType(curveElem: CurveElement, value: CurveProjectionType) -> None: ...
    @staticmethod
    def SetSketchOnSurface(curveElem: CurveElement, sketchOnSurface: bool) -> None: ...
    @staticmethod
    def ValidateCurveElementIdArrayForFaceRegions(document: Document, curveElemIds: IList) -> bool: ...

class CurveElement(Element):
    """.NET: Autodesk.Revit.DB.CurveElement"""
    def __init__(self, *args) -> None: ...
    SupportsTangentLocks: bool
    CurveElementType: CurveElementType
    LineStyle: Element
    SketchPlane: SketchPlane
    CenterPointReference: Reference
    GeometryCurve: Curve
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
    def CreateAreaBasedLoadBoundaryLine(document: Document, curve: Curve, levelId: ElementId) -> CurveElement: ...
    @staticmethod
    def CreateAreaBasedLoadBoundaryLines(document: Document, curves: IList, levelId: ElementId) -> IList: ...
    def GetAdjoinedCurveElements(self, end: int) -> ISet: ...
    def GetAreaBasedLoadBoundaryLineData(self, ) -> AreaBasedLoadBoundaryLineData: ...
    def GetLineStyleIds(self, ) -> ICollection: ...
    def GetTangentLock(self, end: int, other: ElementId) -> bool: ...
    def HasTangentJoin(self, end: int, other: ElementId) -> bool: ...
    def HasTangentLocks(self, end: int) -> bool: ...
    def IsAdjoinedCurveElement(self, end: int, other: ElementId) -> bool: ...
    def SetGeometryCurve(self, curve: Curve, overrideJoins: bool) -> None: ...
    def SetSketchPlaneAndCurve(self, sketchPlane: SketchPlane, curve: Curve) -> None: ...
    def SetTangentLock(self, end: int, other: ElementId, state: bool) -> None: ...

class CurveElementFilter(ElementSlowFilter):
    """.NET: Autodesk.Revit.DB.CurveElementFilter"""
    def __init__(self, *args) -> None: ...
    CurveElementType: CurveElementType
    IsValidObject: bool
    Inverted: bool

class CurveElementType:
    """.NET: Autodesk.Revit.DB.CurveElementType"""
    def __init__(self, *args) -> None: ...
    ...

class CurveExtents:
    """.NET: Autodesk.Revit.DB.CurveExtents"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    EndParameter: float
    StartParameter: float
    def Dispose(self, ) -> None: ...

class CurveIntersectResult:
    """.NET: Autodesk.Revit.DB.CurveIntersectResult"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Result: SetComparisonResult
    def Dispose(self, ) -> None: ...
    def GetOverlaps(self, ) -> IList: ...

class CurveIntersectResultOption:
    """.NET: Autodesk.Revit.DB.CurveIntersectResultOption"""
    def __init__(self, *args) -> None: ...
    ...

class CurveLoop:
    """.NET: Autodesk.Revit.DB.CurveLoop"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Append(self, curve: Curve) -> None: ...
    @staticmethod
    def Create(curves: IList) -> CurveLoop: ...
    @staticmethod
    def CreateViaCopy(original: CurveLoop) -> CurveLoop: ...
    @staticmethod
    def CreateViaOffset(original: CurveLoop, offsetDists: IList, normal: XYZ) -> CurveLoop: ...
    @staticmethod
    def CreateViaThicken(curveLoop: CurveLoop, thickness: float, normal: XYZ) -> CurveLoop: ...
    @staticmethod
    def CreateViaTransform(curveLoop: CurveLoop, transform: Transform) -> CurveLoop: ...
    def Dispose(self, ) -> None: ...
    def Flip(self, ) -> None: ...
    def GetCurveLoopIterator(self, ) -> CurveLoopIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetExactLength(self, ) -> float: ...
    def GetPlane(self, ) -> Plane: ...
    def GetRectangularHeight(self, plane: Plane) -> float: ...
    def GetRectangularWidth(self, plane: Plane) -> float: ...
    def HasPlane(self, ) -> bool: ...
    def IsCounterclockwise(self, normal: XYZ) -> bool: ...
    def IsOpen(self, ) -> bool: ...
    def IsRectangular(self, plane: Plane) -> bool: ...
    def NumberOfCurves(self, ) -> int: ...
    def Transform(self, transform: Transform) -> None: ...

class CurveLoopIterator:
    """.NET: Autodesk.Revit.DB.CurveLoopIterator"""
    def __init__(self, *args) -> None: ...
    Current: Curve
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class CurveLoopsProfile(SweepProfile):
    """.NET: Autodesk.Revit.DB.CurveLoopsProfile"""
    def __init__(self, *args) -> None: ...
    Profile: CurveArrArray
    IsReadOnly: bool

class CurveNode(ModelCurveNode):
    """.NET: Autodesk.Revit.DB.CurveNode"""
    def __init__(self, *args) -> None: ...
    LineProperties: LineProperties
    IsValidObject: bool
    NodeName: str
    def GetCurve(self, ) -> Curve: ...

class CurveOverlapPoint:
    """.NET: Autodesk.Revit.DB.CurveOverlapPoint"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    SecondParameter: float
    FirstParameter: float
    Point: XYZ
    Type: CurveOverlapPointType
    def Dispose(self, ) -> None: ...

class CurveOverlapPointType:
    """.NET: Autodesk.Revit.DB.CurveOverlapPointType"""
    def __init__(self, *args) -> None: ...
    ...

class CurveProjectionType:
    """.NET: Autodesk.Revit.DB.CurveProjectionType"""
    def __init__(self, *args) -> None: ...
    ...

class CurveUV:
    """.NET: Autodesk.Revit.DB.CurveUV"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsBound: bool
    def As3DCurveInXYPlane(self, ) -> Curve: ...
    def ComputeDerivatives(self, parameter: float, normalized: bool) -> IList: ...
    @staticmethod
    def Create(curve3D: Curve) -> CurveUV: ...
    def Dispose(self, ) -> None: ...
    def Evaluate(self, parameter: float, normalized: bool) -> UV: ...
    def GetEndParameter(self, index: int) -> float: ...
    def Transform(self, trfUV: Transform2D) -> CurveUV: ...

class CurvedEdgeConditionParam:
    """.NET: Autodesk.Revit.DB.CurvedEdgeConditionParam"""
    def __init__(self, *args) -> None: ...
    ...

class CustomExporter:
    """.NET: Autodesk.Revit.DB.CustomExporter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Export2DForceDisplayStyle: DisplayStyle
    Export2DIncludingAnnotationObjects: bool
    Export2DGeometricObjectsIncludingPatternLines: bool
    IncludeGeometricObjects: bool
    ShouldStopOnError: bool
    def Dispose(self, ) -> None: ...
    def Export(self, viewIds: IList) -> None: ...
    @staticmethod
    def IsRenderingSupported() -> bool: ...

class CustomFieldData:
    """.NET: Autodesk.Revit.DB.CustomFieldData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    DefaultRowHeightOnSheet: float
    FieldName: str
    FieldTooltip: str
    def Dispose(self, ) -> None: ...
    def GetCustomFieldId(self, ) -> Guid: ...
    def GetCustomFieldProperties(self, ) -> ICustomFieldProperties: ...
    def SetCustomFieldProperties(self, customFieldProperties: ICustomFieldProperties) -> None: ...
    def ValidateCustomFieldProperties(self, customFieldProperties: ICustomFieldProperties) -> str: ...

class CustomSubCategoryId:
    """.NET: Autodesk.Revit.DB.CustomSubCategoryId"""
    def __init__(self, *args) -> None: ...
    ...

class CutFailureReason:
    """.NET: Autodesk.Revit.DB.CutFailureReason"""
    def __init__(self, *args) -> None: ...
    ...

class CylindricalFace(Face):
    """.NET: Autodesk.Revit.DB.CylindricalFace"""
    def __init__(self, *args) -> None: ...
    Radius: XYZ
    Axis: XYZ
    Origin: XYZ
    Period: float
    IsCyclic: bool
    Area: float
    Reference: Reference
    IsTwoSided: bool
    MaterialElementId: ElementId
    EdgeLoops: EdgeArrayArray
    HasRegions: bool
    OrientationMatchesSurfaceOrientation: bool
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool

class CylindricalHelix(Curve):
    """.NET: Autodesk.Revit.DB.CylindricalHelix"""
    def __init__(self, *args) -> None: ...
    Height: float
    IsRightHanded: bool
    Pitch: float
    ZVector: XYZ
    YVector: XYZ
    XVector: XYZ
    Radius: float
    BasePoint: XYZ
    Period: float
    IsCyclic: bool
    Length: float
    ApproximateLength: float
    Reference: Reference
    IsClosed: bool
    IsBound: bool
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool
    @staticmethod
    def Create(basePoint: XYZ, radius: float, xVector: XYZ, zVector: XYZ, pitch: float, startAngle: float, endAngle: float) -> CylindricalHelix: ...

class CylindricalSurface(Surface):
    """.NET: Autodesk.Revit.DB.CylindricalSurface"""
    def __init__(self, *args) -> None: ...
    Radius: float
    Origin: XYZ
    YDir: XYZ
    XDir: XYZ
    Axis: XYZ
    IsValidObject: bool
    OrientationMatchesParametricOrientation: bool
    @staticmethod
    def Create(frameOfReference: Frame, radius: float) -> CylindricalSurface: ...
    def GetFrameOfReference(self, ) -> Frame: ...

class DGNExportOptions(BaseExportOptions):
    """.NET: Autodesk.Revit.DB.DGNExportOptions"""
    def __init__(self, *args) -> None: ...
    FileVersion: DGNFileFormat
    WorkingUnits: bool
    SeedName: str
    MergedViews: bool
    IsValidObject: bool
    PreserveCoincidentLines: bool
    HideUnreferenceViewTags: bool
    HideReferencePlane: bool
    HideScopeBox: bool
    Colors: ExportColorMode
    HatchPatternsFileName: str
    LayerMapping: str
    PropOverrides: PropOverrideMode
    def GetExportLineweightTable(self, ) -> ExportLineweightTable: ...
    @staticmethod
    def GetPredefinedOptions(document: Document, setup: str) -> DGNExportOptions: ...
    @staticmethod
    def GetPredefinedSetupNames(document: Document) -> IList: ...
    def SetExportLineweightTable(self, lineweightTable: ExportLineweightTable) -> None: ...

class DGNFileFormat:
    """.NET: Autodesk.Revit.DB.DGNFileFormat"""
    def __init__(self, *args) -> None: ...
    ...

class DGNImportOptions(BaseImportOptions):
    """.NET: Autodesk.Revit.DB.DGNImportOptions"""
    def __init__(self, *args) -> None: ...
    DGNModelViewName: str
    IgnoreUnsupportedElementWarning: bool
    IsValidObject: bool
    ReferencePoint: XYZ
    AutoCorrectAlmostVHLines: bool
    VisibleLayersOnly: bool
    CustomScale: float
    OrientToView: bool
    ThisViewOnly: bool
    Placement: ImportPlacement
    ColorMode: ImportColorMode
    Unit: ImportUnit

class DWFExportOptions(CADExportOptions):
    """.NET: Autodesk.Revit.DB.DWFExportOptions"""
    def __init__(self, *args) -> None: ...
    ExportOnlyViewId: ElementId
    CropBoxVisible: bool
    ImageQuality: DWFImageQuality
    ImageFormat: DWFImageFormat
    PortraitLayout: bool
    PaperFormat: ExportPaperFormat
    StopOnError: bool
    ExportObjectData: bool
    MergedViews: bool
    ExportTexture: bool
    ExportingAreas: bool

class DWFImageFormat:
    """.NET: Autodesk.Revit.DB.DWFImageFormat"""
    def __init__(self, *args) -> None: ...
    ...

class DWFImageQuality:
    """.NET: Autodesk.Revit.DB.DWFImageQuality"""
    def __init__(self, *args) -> None: ...
    ...

class DWFImportOptions:
    """.NET: Autodesk.Revit.DB.DWFImportOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetSheetViews(self, ) -> IList: ...
    def SetSheetViews(self, sheetViews: IList) -> None: ...

class DWFXExportOptions(DWFExportOptions):
    """.NET: Autodesk.Revit.DB.DWFXExportOptions"""
    def __init__(self, *args) -> None: ...
    ExportOnlyViewId: ElementId
    CropBoxVisible: bool
    ImageQuality: DWFImageQuality
    ImageFormat: DWFImageFormat
    PortraitLayout: bool
    PaperFormat: ExportPaperFormat
    StopOnError: bool
    ExportObjectData: bool
    MergedViews: bool
    ExportTexture: bool
    ExportingAreas: bool

class DWGExportOptions(ACADExportOptions):
    """.NET: Autodesk.Revit.DB.DWGExportOptions"""
    def __init__(self, *args) -> None: ...
    MergedViews: bool
    HatchBackgroundColor: Color
    UseHatchBackgroundColor: bool
    FileVersion: ACADVersion
    NonplotSuffix: str
    MarkNonplotLayers: bool
    ExportingAreas: bool
    SharedCoords: bool
    TargetUnit: ExportUnit
    ACAPreference: ACAObjectPreference
    ExportOfSolids: SolidGeometry
    TextTreatment: TextTreatment
    LinetypesFileName: str
    LineScaling: LineScaling
    IsValidObject: bool
    PreserveCoincidentLines: bool
    HideUnreferenceViewTags: bool
    HideReferencePlane: bool
    HideScopeBox: bool
    Colors: ExportColorMode
    HatchPatternsFileName: str
    LayerMapping: str
    PropOverrides: PropOverrideMode
    @staticmethod
    def GetPredefinedOptions(document: Document, setup: str) -> DWGExportOptions: ...

class DWGImportOptions(BaseImportOptions):
    """.NET: Autodesk.Revit.DB.DWGImportOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ReferencePoint: XYZ
    AutoCorrectAlmostVHLines: bool
    VisibleLayersOnly: bool
    CustomScale: float
    OrientToView: bool
    ThisViewOnly: bool
    Placement: ImportPlacement
    ColorMode: ImportColorMode
    Unit: ImportUnit
    def GetLineWeights(self, ) -> IList: ...
    def SetLineWeights(self, lineWeight: IList) -> None: ...

class DXFExportOptions(ACADExportOptions):
    """.NET: Autodesk.Revit.DB.DXFExportOptions"""
    def __init__(self, *args) -> None: ...
    HatchBackgroundColor: Color
    UseHatchBackgroundColor: bool
    FileVersion: ACADVersion
    NonplotSuffix: str
    MarkNonplotLayers: bool
    ExportingAreas: bool
    SharedCoords: bool
    TargetUnit: ExportUnit
    ACAPreference: ACAObjectPreference
    ExportOfSolids: SolidGeometry
    TextTreatment: TextTreatment
    LinetypesFileName: str
    LineScaling: LineScaling
    IsValidObject: bool
    PreserveCoincidentLines: bool
    HideUnreferenceViewTags: bool
    HideReferencePlane: bool
    HideScopeBox: bool
    Colors: ExportColorMode
    HatchPatternsFileName: str
    LayerMapping: str
    PropOverrides: PropOverrideMode
    @staticmethod
    def GetPredefinedOptions(document: Document, setup: str) -> DXFExportOptions: ...

class DataConversionMonitorScope:
    """.NET: Autodesk.Revit.DB.DataConversionMonitorScope"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class DataExchangeMessageId:
    """.NET: Autodesk.Revit.DB.DataExchangeMessageId"""
    def __init__(self, *args) -> None: ...
    ...

class DataExchangeMessageSeverity:
    """.NET: Autodesk.Revit.DB.DataExchangeMessageSeverity"""
    def __init__(self, *args) -> None: ...
    ...

class DataExchangeMessageVerbosity:
    """.NET: Autodesk.Revit.DB.DataExchangeMessageVerbosity"""
    def __init__(self, *args) -> None: ...
    ...

class DatumEnds:
    """.NET: Autodesk.Revit.DB.DatumEnds"""
    def __init__(self, *args) -> None: ...
    ...

class DatumExtentType:
    """.NET: Autodesk.Revit.DB.DatumExtentType"""
    def __init__(self, *args) -> None: ...
    ...

class DatumPlane(Element):
    """.NET: Autodesk.Revit.DB.DatumPlane"""
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
    def AddLeader(self, datumEnd: DatumEnds, view: View) -> Leader: ...
    def CanBeVisibleInView(self, view: View) -> bool: ...
    def GetCurvesInView(self, extentMode: DatumExtentType, view: View) -> IList: ...
    def GetDatumExtentTypeInView(self, datumEnd: DatumEnds, view: View) -> DatumExtentType: ...
    def GetLeader(self, datumEnd: DatumEnds, view: View) -> Leader: ...
    def GetPropagationViews(self, view: View) -> ISet: ...
    def HasBubbleInView(self, datumEnd: DatumEnds, view: View) -> bool: ...
    def HideBubbleInView(self, datumEnd: DatumEnds, view: View) -> None: ...
    def IsBubbleVisibleInView(self, datumEnd: DatumEnds, view: View) -> bool: ...
    def IsCurveValidInView(self, extentMode: DatumExtentType, view: View, curve: Curve) -> bool: ...
    def IsLeaderValid(self, datumEnd: DatumEnds, view: View, leader: Leader) -> bool: ...
    def Maximize3DExtents(self, ) -> None: ...
    def PropagateToViews(self, view: View, parallelViews: ISet) -> None: ...
    def SetCurveInView(self, extentMode: DatumExtentType, view: View, curve: Curve) -> None: ...
    def SetDatumExtentType(self, datumEnd: DatumEnds, view: View, extentMode: DatumExtentType) -> None: ...
    def SetLeader(self, datumEnd: DatumEnds, view: View, pLeader: Leader) -> None: ...
    def ShowBubbleInView(self, datumEnd: DatumEnds, view: View) -> None: ...

class DecimalSymbol:
    """.NET: Autodesk.Revit.DB.DecimalSymbol"""
    def __init__(self, *args) -> None: ...
    ...

class DefaultDivideSettings(Element):
    """.NET: Autodesk.Revit.DB.DefaultDivideSettings"""
    def __init__(self, *args) -> None: ...
    PathMeasurementType: DividedPathMeasurementType
    PathDistance: float
    PathNumber: int
    PathLayout: SpacingRuleLayout
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
    def GetDefaultDivideSettings(cda: Document) -> DefaultDivideSettings: ...
    def GetSurfaceDistance(self, gridlines: UVGridlineType) -> float: ...
    def GetSurfaceLayout(self, gridlines: UVGridlineType) -> SpacingRuleLayout: ...
    def GetSurfaceNumber(self, gridlines: UVGridlineType) -> int: ...
    def SetSurfaceDistance(self, gridlines: UVGridlineType, distance: float) -> None: ...
    def SetSurfaceLayout(self, gridlines: UVGridlineType, layout: SpacingRuleLayout) -> None: ...
    def SetSurfaceNumber(self, gridlines: UVGridlineType, number: int) -> None: ...

class DefaultOpenFromCloudCallback:
    """.NET: Autodesk.Revit.DB.DefaultOpenFromCloudCallback"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def OnOpenConflict(self, scenario: OpenConflictScenario) -> OpenConflictResult: ...

class Definition:
    """.NET: Autodesk.Revit.DB.Definition"""
    def __init__(self, *args) -> None: ...
    Name: str
    def GetDataType(self, ) -> ForgeTypeId: ...
    def GetGroupTypeId(self, ) -> ForgeTypeId: ...

class DefinitionBindingMap(APIObject):
    """.NET: Autodesk.Revit.DB.DefinitionBindingMap"""
    def __init__(self, *args) -> None: ...
    Item: Binding
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, key: Definition) -> bool: ...
    def Erase(self, key: Definition) -> int: ...
    def ForwardIterator(self, ) -> DefinitionBindingMapIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, key: Definition, item: Binding) -> bool: ...
    def ReverseIterator(self, ) -> DefinitionBindingMapIterator: ...

class DefinitionBindingMapIterator(APIObject):
    """.NET: Autodesk.Revit.DB.DefinitionBindingMapIterator"""
    def __init__(self, *args) -> None: ...
    Key: Definition
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class DefinitionFile(APIObject):
    """.NET: Autodesk.Revit.DB.DefinitionFile"""
    def __init__(self, *args) -> None: ...
    Filename: str
    Groups: DefinitionGroups
    IsReadOnly: bool

class DefinitionGroup(APIObject):
    """.NET: Autodesk.Revit.DB.DefinitionGroup"""
    def __init__(self, *args) -> None: ...
    Definitions: Definitions
    Name: str
    IsReadOnly: bool

class DefinitionGroups:
    """.NET: Autodesk.Revit.DB.DefinitionGroups"""
    def __init__(self, *args) -> None: ...
    Size: int
    IsEmpty: bool
    Item: DefinitionGroup
    def Contains(self, definitionGroup: DefinitionGroup) -> bool: ...
    def Create(self, name: str) -> DefinitionGroup: ...
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...

class Definitions:
    """.NET: Autodesk.Revit.DB.Definitions"""
    def __init__(self, *args) -> None: ...
    Size: int
    IsEmpty: bool
    Item: Definition
    def Contains(self, definition: Definition) -> bool: ...
    def Create(self, option: ExternalDefinitionCreationOptions) -> Definition: ...
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...

class DeleteElements(FailureResolution):
    """.NET: Autodesk.Revit.DB.DeleteElements"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    @staticmethod
    def Create(document: Document, id: ElementId) -> FailureResolution: ...

class DeleteWorksetOption:
    """.NET: Autodesk.Revit.DB.DeleteWorksetOption"""
    def __init__(self, *args) -> None: ...
    ...

class DeleteWorksetSettings:
    """.NET: Autodesk.Revit.DB.DeleteWorksetSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    WorksetId: WorksetId
    DeleteWorksetOption: DeleteWorksetOption
    def Dispose(self, ) -> None: ...

class DesignOption(Element):
    """.NET: Autodesk.Revit.DB.DesignOption"""
    def __init__(self, *args) -> None: ...
    IsPrimary: bool
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
    def GetActiveDesignOptionId(document: Document) -> ElementId: ...

class DetachFromCentralOption:
    """.NET: Autodesk.Revit.DB.DetachFromCentralOption"""
    def __init__(self, *args) -> None: ...
    ...

class DetailArc(DetailCurve):
    """.NET: Autodesk.Revit.DB.DetailArc"""
    def __init__(self, *args) -> None: ...
    SupportsTangentLocks: bool
    CurveElementType: CurveElementType
    LineStyle: Element
    SketchPlane: SketchPlane
    CenterPointReference: Reference
    GeometryCurve: Curve
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

class DetailCurve(CurveElement):
    """.NET: Autodesk.Revit.DB.DetailCurve"""
    def __init__(self, *args) -> None: ...
    SupportsTangentLocks: bool
    CurveElementType: CurveElementType
    LineStyle: Element
    SketchPlane: SketchPlane
    CenterPointReference: Reference
    GeometryCurve: Curve
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

class DetailCurveArray(APIObject):
    """.NET: Autodesk.Revit.DB.DetailCurveArray"""
    def __init__(self, *args) -> None: ...
    Item: DetailCurve
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: DetailCurve) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> DetailCurveArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: DetailCurve, index: int) -> None: ...
    def ReverseIterator(self, ) -> DetailCurveArrayIterator: ...

class DetailCurveArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.DetailCurveArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class DetailElementOrderUtils:
    """.NET: Autodesk.Revit.DB.DetailElementOrderUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def AreDetailElements(document: Document, view: View, detailElementIds: ICollection) -> bool: ...
    @staticmethod
    def BringForward(document: Document, view: View, detailElementIds: ICollection) -> None: ...
    @staticmethod
    def BringToFront(document: Document, view: View, detailElementIds: ICollection) -> None: ...
    @staticmethod
    def GetDrawOrderForDetails(view: View, detailIdsToSort: ISet) -> IList: ...
    @staticmethod
    def IsDetailElement(document: Document, view: View, detailElementId: ElementId) -> bool: ...
    @staticmethod
    def SendBackward(document: Document, view: View, detailElementIds: ICollection) -> None: ...
    @staticmethod
    def SendToBack(document: Document, view: View, detailElementIds: ICollection) -> None: ...

class DetailEllipse(DetailCurve):
    """.NET: Autodesk.Revit.DB.DetailEllipse"""
    def __init__(self, *args) -> None: ...
    SupportsTangentLocks: bool
    CurveElementType: CurveElementType
    LineStyle: Element
    SketchPlane: SketchPlane
    CenterPointReference: Reference
    GeometryCurve: Curve
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

class DetailLine(DetailCurve):
    """.NET: Autodesk.Revit.DB.DetailLine"""
    def __init__(self, *args) -> None: ...
    SupportsTangentLocks: bool
    CurveElementType: CurveElementType
    LineStyle: Element
    SketchPlane: SketchPlane
    CenterPointReference: Reference
    GeometryCurve: Curve
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

class DetailNurbSpline(DetailCurve):
    """.NET: Autodesk.Revit.DB.DetailNurbSpline"""
    def __init__(self, *args) -> None: ...
    SupportsTangentLocks: bool
    CurveElementType: CurveElementType
    LineStyle: Element
    SketchPlane: SketchPlane
    CenterPointReference: Reference
    GeometryCurve: Curve
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

class DigitGroupingAmount:
    """.NET: Autodesk.Revit.DB.DigitGroupingAmount"""
    def __init__(self, *args) -> None: ...
    ...

class DigitGroupingSymbol:
    """.NET: Autodesk.Revit.DB.DigitGroupingSymbol"""
    def __init__(self, *args) -> None: ...
    ...

class Dimension(Element):
    """.NET: Autodesk.Revit.DB.Dimension"""
    def __init__(self, *args) -> None: ...
    IsValid: bool
    AreReferencesAvailable: bool
    TextPosition: XYZ
    Origin: XYZ
    LeaderEndPosition: XYZ
    HasLeader: bool
    ValueOverride: str
    Below: str
    Above: str
    Suffix: str
    Prefix: str
    IsLocked: bool
    ValueString: str
    Value: Nullable
    AreSegmentsEqual: bool
    Segments: DimensionSegmentArray
    NumberOfSegments: int
    DimensionShape: DimensionShape
    FamilyLabel: FamilyParameter
    Name: str
    DimensionType: DimensionType
    View: View
    Curve: Curve
    References: ReferenceArray
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
    def HasOneSegment(self, ) -> bool: ...
    def IsTextPositionAdjustable(self, ) -> bool: ...
    def ResetTextPosition(self, ) -> None: ...

class DimensionEqualityLabelFormatting:
    """.NET: Autodesk.Revit.DB.DimensionEqualityLabelFormatting"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Suffix: str
    Prefix: str
    LeadingSpaces: int
    LabelType: LabelType
    def Dispose(self, ) -> None: ...
    def GetFormatOptions(self, ) -> FormatOptions: ...
    def IsValidFormatOptions(self, ) -> bool: ...
    def SetFormatOptions(self, formatOptions: FormatOptions) -> None: ...

class DimensionSegment(APIObject):
    """.NET: Autodesk.Revit.DB.DimensionSegment"""
    def __init__(self, *args) -> None: ...
    TextPosition: XYZ
    LeaderEndPosition: XYZ
    ValueOverride: str
    Below: str
    Above: str
    Suffix: str
    Prefix: str
    IsLocked: bool
    ValueString: str
    Value: Nullable
    Origin: XYZ
    IsReadOnly: bool
    def IsTextPositionAdjustable(self, ) -> bool: ...
    def ResetTextPosition(self, ) -> None: ...

class DimensionSegmentArray(APIObject):
    """.NET: Autodesk.Revit.DB.DimensionSegmentArray"""
    def __init__(self, *args) -> None: ...
    Item: DimensionSegment
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: DimensionSegment) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> DimensionSegmentArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: DimensionSegment, index: int) -> None: ...
    def ReverseIterator(self, ) -> DimensionSegmentArrayIterator: ...

class DimensionSegmentArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.DimensionSegmentArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class DimensionShape:
    """.NET: Autodesk.Revit.DB.DimensionShape"""
    def __init__(self, *args) -> None: ...
    ...

class DimensionStyleType:
    """.NET: Autodesk.Revit.DB.DimensionStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class DimensionType(ElementType):
    """.NET: Autodesk.Revit.DB.DimensionType"""
    def __init__(self, *args) -> None: ...
    Suffix: str
    Prefix: str
    AlternateUnitsSuffix: str
    AlternateUnitsPrefix: str
    AlternateUnits: AlternateUnits
    StyleType: DimensionStyleType
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
    def CanHaveEqualityFormula(self, ) -> bool: ...
    def CanHaveOrdinateDimensionSetting(self, ) -> bool: ...
    def GetAlternateUnitsFormatOptions(self, ) -> FormatOptions: ...
    def GetEqualityFormula(self, ) -> IList: ...
    def GetOrdinateDimensionSetting(self, ) -> OrdinateDimensionSetting: ...
    def GetSpecTypeId(self, ) -> ForgeTypeId: ...
    def GetUnitsFormatOptions(self, ) -> FormatOptions: ...
    def SetAlternateUnitsFormatOptions(self, formatOptions: FormatOptions) -> None: ...
    def SetEqualityFormula(self, formattingArr: IList) -> None: ...
    def SetOrdinateDimensionSetting(self, ordinateDimSetting: OrdinateDimensionSetting) -> None: ...
    def SetUnitsFormatOptions(self, formatOptions: FormatOptions) -> None: ...

class DirectShape(Element):
    """.NET: Autodesk.Revit.DB.DirectShape"""
    def __init__(self, *args) -> None: ...
    ApplicationDataId: str
    ApplicationId: str
    TypeId: ElementId
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
    def AddExternallyTaggedGeometry(self, externallyTaggedGeometry: ExternallyTaggedGeometryObject) -> None: ...
    def AddReferenceCurve(self, refCurve: Curve, options: DirectShapeReferenceOptions) -> None: ...
    def AddReferencePlane(self, refPlane: Plane, boundingBoxUV: BoundingBoxUV, options: DirectShapeReferenceOptions) -> None: ...
    def AddReferencePoint(self, refPoint: XYZ, options: DirectShapeReferenceOptions) -> None: ...
    def AppendShape(self, pGeomArr: IList, viewType: DirectShapeTargetViewType) -> None: ...
    def AreOptionsValid(self, options: DirectShapeOptions) -> bool: ...
    def AreOptionsValidForTransientDirectShape(self, options: DirectShapeOptions) -> bool: ...
    def AreValidDirectShapeReferenceOptions(self, options: DirectShapeReferenceOptions) -> bool: ...
    def CanCreateParts(self, ) -> bool: ...
    @staticmethod
    def CreateElement(document: Document, categoryId: ElementId) -> DirectShape: ...
    @staticmethod
    def CreateElementInstance(document: Document, typeId: ElementId, categoryId: ElementId, definitionId: str, trf: Transform) -> DirectShape: ...
    @staticmethod
    def CreateGeometryInstance(document: Document, definition_id: str, trf: Transform) -> IList: ...
    def GetExternallyTaggedGeometry(self, externalId: ExternalGeometryId) -> ExternallyTaggedGeometryObject: ...
    def GetExternallyTaggedReference(self, externalId: ExternalGeometryId) -> Reference: ...
    def GetOptions(self, ) -> DirectShapeOptions: ...
    def HasExternalGeometry(self, externalId: ExternalGeometryId) -> bool: ...
    def HasExternallyTaggedReference(self, externalId: ExternalGeometryId) -> bool: ...
    @staticmethod
    def IsSupportedDocument(document: Document) -> bool: ...
    @staticmethod
    def IsValidCategoryId(categoryId: ElementId, doc: Document) -> bool: ...
    def IsValidGeometry(self, Geom: Solid) -> bool: ...
    @staticmethod
    def IsValidReferenceCurve(curve: Curve) -> bool: ...
    @staticmethod
    def IsValidReferencePlaneBoundingBoxUV(boundingBoxUV: BoundingBoxUV) -> bool: ...
    def IsValidShape(self, shape: IList, viewType: DirectShapeTargetViewType) -> bool: ...
    def IsValidTypeId(self, typeId: ElementId) -> bool: ...
    def IsValidUsage(self, externallyTaggedGeometry: ExternallyTaggedGeometryObject) -> bool: ...
    def RemoveAllReferenceObjects(self, ) -> None: ...
    def RemoveExternallyTaggedGeometry(self, externalId: ExternalGeometryId) -> None: ...
    def RemoveReferenceObject(self, externalId: ExternalGeometryId) -> None: ...
    def ResetExternallyTaggedGeometry(self, ) -> None: ...
    def SetName(self, name: str) -> None: ...
    def SetOptions(self, options: DirectShapeOptions) -> None: ...
    def SetShape(self, pGeomArr: IList, viewType: DirectShapeTargetViewType) -> None: ...
    def SetTypeId(self, typeId: ElementId) -> None: ...
    def UpdateExternallyTaggedGeometry(self, externallyTaggedGeometry: ExternallyTaggedGeometryObject) -> None: ...

class DirectShapeLibrary:
    """.NET: Autodesk.Revit.DB.DirectShapeLibrary"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def AddDefinition(self, id: str, GNodes: IList) -> None: ...
    def AddDefinitionType(self, id: str, typeId: ElementId) -> None: ...
    def Contains(self, id: str) -> bool: ...
    def ContainsType(self, name: str) -> bool: ...
    def Dispose(self, ) -> None: ...
    def FindDefinition(self, id: str) -> IList: ...
    def FindDefinitionType(self, id: str) -> ElementId: ...
    @staticmethod
    def GetDirectShapeLibrary(ADoc: Document) -> DirectShapeLibrary: ...
    def Reset(self, ) -> None: ...

class DirectShapeOptions:
    """.NET: Autodesk.Revit.DB.DirectShapeOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    RoomBoundingOption: DirectShapeRoomBoundingOption
    ReferencingOption: DirectShapeReferencingOption
    def Dispose(self, ) -> None: ...

class DirectShapeReferenceOptions:
    """.NET: Autodesk.Revit.DB.DirectShapeReferenceOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Name: str
    def Dispose(self, ) -> None: ...
    def GetExternalGeometryId(self, ) -> ExternalGeometryId: ...
    @staticmethod
    def IsValidExternalGeometryId(externalId: ExternalGeometryId) -> bool: ...
    @staticmethod
    def IsValidReferenceName(name: str) -> bool: ...
    def SetExternalGeometryId(self, externalId: ExternalGeometryId) -> DirectShapeReferenceOptions: ...

class DirectShapeReferencingOption:
    """.NET: Autodesk.Revit.DB.DirectShapeReferencingOption"""
    def __init__(self, *args) -> None: ...
    ...

class DirectShapeRoomBoundingOption:
    """.NET: Autodesk.Revit.DB.DirectShapeRoomBoundingOption"""
    def __init__(self, *args) -> None: ...
    ...

class DirectShapeTargetViewType:
    """.NET: Autodesk.Revit.DB.DirectShapeTargetViewType"""
    def __init__(self, *args) -> None: ...
    ...

class DirectShapeType(ElementType):
    """.NET: Autodesk.Revit.DB.DirectShapeType"""
    def __init__(self, *args) -> None: ...
    UserAssignability: DirectShapeTypeUserAssignability
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
    def AddExternallyTaggedGeometry(self, externallyTaggedGeometry: ExternallyTaggedGeometryObject) -> None: ...
    def AddReferenceCurve(self, refCurve: Curve, options: DirectShapeReferenceOptions) -> None: ...
    def AddReferencePlane(self, refPlane: Plane, boundingBoxUV: BoundingBoxUV, options: DirectShapeReferenceOptions) -> None: ...
    def AddReferencePoint(self, refPoint: XYZ, options: DirectShapeReferenceOptions) -> None: ...
    def AppendShape(self, pGeomArr: IList, viewType: DirectShapeTargetViewType) -> None: ...
    def AreOptionsValid(self, options: DirectShapeTypeOptions) -> bool: ...
    def AreValidDirectShapeReferenceOptions(self, options: DirectShapeReferenceOptions) -> bool: ...
    def CanChangeFamilyName(self, ) -> bool: ...
    def CanCreateParts(self, ) -> bool: ...
    @staticmethod
    def Create(document: Document, name: str, categoryId: ElementId, options: DirectShapeTypeOptions) -> DirectShapeType: ...
    def GetExternallyTaggedGeometry(self, externalId: ExternalGeometryId) -> ExternallyTaggedGeometryObject: ...
    def GetExternallyTaggedReference(self, externalId: ExternalGeometryId) -> Reference: ...
    def GetOptions(self, ) -> DirectShapeTypeOptions: ...
    def HasExternalGeometry(self, externalId: ExternalGeometryId) -> bool: ...
    def HasExternallyTaggedReference(self, externalId: ExternalGeometryId) -> bool: ...
    @staticmethod
    def IsValidReferenceCurve(curve: Curve) -> bool: ...
    @staticmethod
    def IsValidReferencePlaneBoundingBoxUV(boundingBoxUV: BoundingBoxUV) -> bool: ...
    def IsValidShape(self, shape: IList, viewType: DirectShapeTargetViewType) -> bool: ...
    def IsValidUsage(self, externallyTaggedGeometry: ExternallyTaggedGeometryObject) -> bool: ...
    def RemoveAllReferenceObjects(self, ) -> None: ...
    def RemoveExternallyTaggedGeometry(self, externalId: ExternalGeometryId) -> None: ...
    def RemoveReferenceObject(self, externalId: ExternalGeometryId) -> None: ...
    def ResetExternallyTaggedGeometry(self, ) -> None: ...
    def SetFamilyName(self, name: str) -> None: ...
    def SetOptions(self, options: DirectShapeTypeOptions) -> None: ...
    def SetShape(self, pGeomArr: IList, viewType: DirectShapeTargetViewType) -> None: ...
    def UpdateExternallyTaggedGeometry(self, externallyTaggedGeometry: ExternallyTaggedGeometryObject) -> None: ...

class DirectShapeTypeOptions:
    """.NET: Autodesk.Revit.DB.DirectShapeTypeOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    AllowDuplicateNames: bool
    def Dispose(self, ) -> None: ...
    def IsEqualTo(self, other: DirectShapeTypeOptions) -> bool: ...
    def IsValid(self, ) -> bool: ...

class DirectShapeTypeUserAssignability:
    """.NET: Autodesk.Revit.DB.DirectShapeTypeUserAssignability"""
    def __init__(self, *args) -> None: ...
    ...

class DisableAnalyticalModelCB(FailureResolution):
    """.NET: Autodesk.Revit.DB.DisableAnalyticalModelCB"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class DisciplineTypeId:
    """.NET: Autodesk.Revit.DB.DisciplineTypeId"""
    def __init__(self, *args) -> None: ...
    Structural: ForgeTypeId
    Piping: ForgeTypeId
    Infrastructure: ForgeTypeId
    Hvac: ForgeTypeId
    Energy: ForgeTypeId
    Electrical: ForgeTypeId
    Architecture: ForgeTypeId
    Common: ForgeTypeId

class DisplacementElement(Element):
    """.NET: Autodesk.Revit.DB.DisplacementElement"""
    def __init__(self, *args) -> None: ...
    ParentId: ElementId
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
    def CanCategoryBeDisplaced(categoryId: ElementId) -> bool: ...
    def CanElementsBeAddedToDisplacementSet(self, toDisplace: ICollection) -> bool: ...
    @staticmethod
    def CanElementsBeDisplaced(view: View, elementIds: ICollection, commonDisplacedElementId: ElementId) -> bool: ...
    @staticmethod
    def Create(document: Document, elementsToDisplace: ICollection, displacement: XYZ, ownerDBView: View, parentDisplacementElement: DisplacementElement) -> DisplacementElement: ...
    def GetAbsoluteDisplacement(self, ) -> XYZ: ...
    @staticmethod
    def GetAdditionalElementsToDisplace(document: Document, view: View, idToDisplace: ElementId) -> ICollection: ...
    def GetChildren(self, ) -> IList: ...
    @staticmethod
    def GetDisplacedElementIds(view: View) -> ICollection: ...
    def GetDisplacedElementIdsFromAllChildren(self, ) -> ICollection: ...
    @staticmethod
    def GetDisplacementElementId(view: View, id: ElementId) -> ElementId: ...
    @staticmethod
    def GetDisplacementElementIds(view: View) -> ICollection: ...
    def GetRelativeDisplacement(self, ) -> XYZ: ...
    @staticmethod
    def IsAllowedAsDisplacedElement(element: Element) -> bool: ...
    @staticmethod
    def IsElementDisplacedInView(view: View, id: ElementId) -> bool: ...
    @staticmethod
    def IsNotEmpty(elementIds: ICollection) -> bool: ...
    @staticmethod
    def IsValidAsParentInView(view: View, parent: DisplacementElement) -> bool: ...
    def RemoveDisplacedElement(self, ElemToRemove: Element) -> None: ...
    def ResetDisplacedElements(self, ) -> None: ...
    def SetDisplacedElementIds(self, displacedElemIds: ICollection) -> None: ...
    def SetRelativeDisplacement(self, displacement: XYZ) -> None: ...

class DisplacementPath(Element):
    """.NET: Autodesk.Revit.DB.DisplacementPath"""
    def __init__(self, *args) -> None: ...
    PathStyle: DisplacementPathStyle
    AncestorIdx: int
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
    def Create(aDoc: Document, displacementElement: DisplacementElement, reference: Reference, param: float) -> ElementId: ...
    @staticmethod
    def IsValidParam(param: float) -> bool: ...
    @staticmethod
    def IsValidReference(displacementElement: DisplacementElement, reference: Reference) -> bool: ...
    def SetAnchorPoint(self, displacementElement: DisplacementElement, reference: Reference, param: float) -> None: ...

class DisplacementPathStyle:
    """.NET: Autodesk.Revit.DB.DisplacementPathStyle"""
    def __init__(self, *args) -> None: ...
    ...

class DisplayStyle:
    """.NET: Autodesk.Revit.DB.DisplayStyle"""
    def __init__(self, *args) -> None: ...
    ...

class DisplayUnit:
    """.NET: Autodesk.Revit.DB.DisplayUnit"""
    def __init__(self, *args) -> None: ...
    ...

class DistanceMeasuredFrom:
    """.NET: Autodesk.Revit.DB.DistanceMeasuredFrom"""
    def __init__(self, *args) -> None: ...
    ...

class DistributionOfNormals:
    """.NET: Autodesk.Revit.DB.DistributionOfNormals"""
    def __init__(self, *args) -> None: ...
    ...

class DividedPath(Element):
    """.NET: Autodesk.Revit.DB.DividedPath"""
    def __init__(self, *args) -> None: ...
    DisplayReferenceCurves: bool
    Flipped: bool
    NumberOfPoints: int
    SpacingRuleJustification: SpacingRuleJustification
    SpacingRuleLayout: SpacingRuleLayout
    IsCyclical: bool
    IsClosedLoop: bool
    TotalPathLength: float
    DisplayNodeNumbers: bool
    DisplayNodes: bool
    EndIndent: float
    BeginningIndent: float
    MaximumDistance: float
    MinimumDistance: float
    Distance: float
    FixedNumberOfPoints: int
    MeasurementType: DividedPathMeasurementType
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
    def AreCurveReferencesConnected(document: Document, curveReferences: IList) -> bool: ...
    @staticmethod
    def Create(document: Document, curveReferences: IList, intersectors: ICollection) -> DividedPath: ...
    def Flip(self, ) -> None: ...
    def GetIntersectingElements(self, ) -> ICollection: ...
    @staticmethod
    def IsCurveReferenceValid(document: Document, curveReference: Reference) -> bool: ...
    @staticmethod
    def IsIntersectorValidForCreation(document: Document, intersector: ElementId) -> bool: ...
    def IsIntersectorValidForDividedPath(self, intersector: ElementId) -> bool: ...
    def IsValidBeginningIndent(self, beginningIndent: float) -> bool: ...
    def IsValidEndIndent(self, endIndent: float) -> bool: ...
    @staticmethod
    def IsValidFixedNumberOfPoints(fixedNumberOfPoints: int) -> bool: ...
    def IsValidMeasurementType(self, measurementType: DividedPathMeasurementType) -> bool: ...
    def IsValidSpacingRuleJustification(self, justification: SpacingRuleJustification) -> bool: ...
    def IsValidSpacingRuleLayout(self, layout: SpacingRuleLayout) -> bool: ...
    @staticmethod
    def SeparateReferencesIntoConnectedReferences(document: Document, curveReferences: IList) -> IList: ...
    def SetIntersectingElements(self, intersectors: ICollection) -> None: ...

class DividedPathMeasurementType:
    """.NET: Autodesk.Revit.DB.DividedPathMeasurementType"""
    def __init__(self, *args) -> None: ...
    ...

class DividedSurface(Element):
    """.NET: Autodesk.Revit.DB.DividedSurface"""
    def __init__(self, *args) -> None: ...
    NumberOfVGridlines: int
    NumberOfUGridlines: int
    IsComponentFlipped: bool
    IsComponentMirrored: bool
    ComponentRotation: ComponentRotation
    VPatternIndent: int
    UPatternIndent: int
    BorderTile: BorderTile
    AllGridRotation: float
    VSpacingRule: SpacingRule
    USpacingRule: SpacingRule
    HostReference: Reference
    Host: Element
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
    def AddIntersectionElement(self, newIntersectionElemId: ElementId) -> None: ...
    @staticmethod
    def CanBeDivided(document: Document, reference: Reference) -> bool: ...
    def CanBeIntersectionElement(self, id: ElementId) -> bool: ...
    @staticmethod
    def Create(document: Document, faceReference: Reference) -> DividedSurface: ...
    def GetAllIntersectionElements(self, ) -> ICollection: ...
    @staticmethod
    def GetDividedSurfaceForReference(document: Document, faceReference: Reference) -> DividedSurface: ...
    def GetGridNodeLocation(self, gridNode: GridNode) -> GridNodeLocation: ...
    def GetGridNodeReference(self, gridNode: GridNode) -> Reference: ...
    def GetGridNodeUV(self, gridNode: GridNode) -> UV: ...
    def GetGridSegmentReference(self, gridNode: GridNode, gridSegmentDirection: GridSegmentDirection) -> Reference: ...
    @staticmethod
    def GetReferencesWithDividedSurfaces(host: Element) -> IList: ...
    def GetTileFamilyInstance(self, gridNode: GridNode, tileIndex: int) -> FamilyInstance: ...
    def GetTileReference(self, gridNode: GridNode, tileIndex: int) -> Reference: ...
    def IsSeedNode(self, gridNode: GridNode) -> bool: ...
    def RemoveAllIntersectionElements(self, ) -> None: ...
    def RemoveIntersectionElement(self, referenceElemIdToRemove: ElementId) -> None: ...

class Document:
    """.NET: Autodesk.Revit.DB.Document"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    CreationGUID: Guid
    MassDisplayTemporaryOverride: MassDisplayTemporaryOverrideType
    WorksharingCentralGUID: Guid
    IsModelInCloud: bool
    IsDetached: bool
    IsWorkshared: bool
    IsLinked: bool
    IsReadOnlyFile: bool
    IsReadOnly: bool
    IsModified: bool
    IsModifiable: bool
    Title: str
    PathName: str
    Application: Application
    OwnerFamily: Family
    IsFamilyDocument: bool
    PrintManager: PrintManager
    SiteLocation: SiteLocation
    ActiveProjectLocation: ProjectLocation
    ProjectLocations: ProjectLocationSet
    ActiveView: View
    FamilyManager: FamilyManager
    FamilyCreate: FamilyItemFactory
    Create: Document
    PlanTopologies: PlanTopologySet
    PlanTopologies: PlanTopologySet
    PlanTopology: PlanTopology
    PlanTopology: PlanTopology
    ProjectInformation: ProjectInfo
    ReactionsAreUpToDate: bool
    Phases: PhaseArray
    PanelTypes: PanelTypeSet
    MullionTypes: MullionTypeSet
    ParameterBindings: BindingMap
    DisplayUnitSystem: DisplayUnit
    Settings: Settings
    TypeOfStorage: StorageType
    def AcquireCoordinates(self, linkInstanceId: ElementId) -> None: ...
    def AutoJoinElements(self, ) -> None: ...
    def CanEnableCloudWorksharing(self, ) -> bool: ...
    def CanEnableWorksharing(self, ) -> bool: ...
    def Close(self, saveModified: bool) -> bool: ...
    def CombineElements(self, members: CombinableElementArray) -> GeomCombination: ...
    def ConvertDetailToModelCurves(self, view: View, detailCurves: DetailCurveArray) -> ModelCurveArray: ...
    def ConvertModelToDetailCurves(self, view: View, modelCurves: ModelCurveArray) -> DetailCurveArray: ...
    def ConvertModelToSymbolicCurves(self, view: View, modelCurves: ModelCurveArray) -> SymbolicCurveArray: ...
    def ConvertSymbolicToModelCurves(self, view: View, symbolicCurve: SymbolicCurveArray) -> ModelCurveArray: ...
    def Delete(self, elementIds: ICollection) -> ICollection: ...
    def Dispose(self, ) -> None: ...
    def EditFamily(self, loadedFamily: Family) -> Document: ...
    def EnableCloudWorksharing(self, ) -> None: ...
    def EnableWorksharing(self, worksetNameGridLevel: str, worksetName: str) -> None: ...
    def Equals(self, obj: object) -> bool: ...
    def EraseSchemaAndAllEntities(self, schema: Schema) -> None: ...
    def Export(self, folder: str, name: str, views: ICollection, options: SATExportOptions) -> bool: ...
    def ExportImage(self, options: ImageExportOptions) -> None: ...
    def GetActiveEditMode(self, ) -> EditModeType: ...
    def GetAllUnusedElements(self, categories: ISet) -> ISet: ...
    def GetChangedElements(self, baseVersionGUID: Guid) -> DocumentDifference: ...
    def GetCloudFolderId(self, forceRefresh: bool) -> str: ...
    def GetCloudModelPath(self, ) -> ModelPath: ...
    def GetCloudModelUrn(self, ) -> str: ...
    def GetDefaultElementTypeId(self, defaultTypeId: ElementTypeGroup) -> ElementId: ...
    def GetDefaultFamilyTypeId(self, familyCategoryId: ElementId) -> ElementId: ...
    def GetDocumentPreviewSettings(self, ) -> DocumentPreviewSettings: ...
    @staticmethod
    def GetDocumentVersion(doc: Document) -> DocumentVersion: ...
    def GetElement(self, id: ElementId) -> Element: ...
    def GetHashCode(self, ) -> int: ...
    def GetHubId(self, ) -> str: ...
    def GetPaintedMaterial(self, elementId: ElementId, face: Face) -> ElementId: ...
    def GetPrintSettingIds(self, ) -> ICollection: ...
    def GetProjectId(self, ) -> str: ...
    def GetRoomAtPoint(self, point: XYZ, phase: Phase) -> Room: ...
    def GetSpaceAtPoint(self, point: XYZ, phase: Phase) -> Space: ...
    def GetSubelement(self, id: ElementId, subId: int) -> Subelement: ...
    def GetTypeOfStorage(self, parameterTypeId: ForgeTypeId) -> StorageType: ...
    def GetUnits(self, ) -> Units: ...
    def GetUnusedElements(self, categories: ISet) -> ISet: ...
    def GetWarnings(self, ) -> IList: ...
    def GetWorksetId(self, id: ElementId) -> WorksetId: ...
    def GetWorksetTable(self, ) -> WorksetTable: ...
    def GetWorksharingCentralModelPath(self, ) -> ModelPath: ...
    def HasAllChangesFromCentral(self, ) -> bool: ...
    def Import(self, file: str, options: DGNImportOptions, pDBView: View, elementId: ElementId) -> bool: ...
    def IsBackgroundCalculationInProgress(self, ) -> bool: ...
    def IsDefaultElementTypeIdValid(self, defaultTypeId: ElementTypeGroup, typeId: ElementId) -> bool: ...
    def IsDefaultFamilyTypeIdValid(self, familyCategoryId: ElementId, familyTypeId: ElementId) -> bool: ...
    def IsInEditMode(self, ) -> bool: ...
    def IsPainted(self, elementId: ElementId, face: Face) -> bool: ...
    @staticmethod
    def IsValidVersionGUID(document: Document, versionGUID: Guid) -> bool: ...
    def Link(self, file: str, options: DGNImportOptions, pDBView: View, elementId: ElementId) -> bool: ...
    def LoadFamily(self, filename: str, familyLoadOptions: IFamilyLoadOptions, family: Family) -> bool: ...
    def LoadFamilySymbol(self, filename: str, name: str, familyLoadOptions: IFamilyLoadOptions, symbol: FamilySymbol) -> bool: ...
    def MakeTransientElements(self, maker: ITransientElementMaker) -> None: ...
    def Paint(self, elementId: ElementId, face: Face, materialId: ElementId) -> None: ...
    def PostFailure(self, failure: FailureMessage) -> FailureMessageKey: ...
    def Print(self, views: ViewSet, viewTemplate: View, useCurrentPrintSettings: bool) -> None: ...
    def PublishCoordinates(self, locationId: LinkElementId) -> None: ...
    def Regenerate(self, ) -> None: ...
    def ReloadLatest(self, reloadOptions: ReloadLatestOptions) -> None: ...
    def RemovePaint(self, elementId: ElementId, face: Face) -> None: ...
    def ResetSharedCoordinates(self, ) -> None: ...
    def Save(self, options: SaveOptions) -> None: ...
    def SaveAs(self, path: ModelPath, options: SaveAsOptions) -> None: ...
    def SaveAsCloudModel(self, accountId: Guid, projectId: Guid, folderId: str, modelName: str) -> None: ...
    def SaveCloudModel(self, ) -> None: ...
    def SaveToProjectAsImage(self, options: ImageExportOptions) -> ElementId: ...
    def SeparateElements(self, members: CombinableElementArray) -> None: ...
    def SetDefaultElementTypeId(self, defaultTypeId: ElementTypeGroup, typeId: ElementId) -> None: ...
    def SetDefaultFamilyTypeId(self, familyCategoryId: ElementId, familyTypeId: ElementId) -> None: ...
    def SetUnits(self, units: Units) -> None: ...
    def SynchronizeWithCentral(self, transactOptions: TransactWithCentralOptions, syncOptions: SynchronizeWithCentralOptions) -> None: ...
    def UnpostFailure(self, messageKey: FailureMessageKey) -> None: ...

class DocumentDifference:
    """.NET: Autodesk.Revit.DB.DocumentDifference"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    AreDeletedElementIdsAvailable: bool
    def Dispose(self, ) -> None: ...
    def GetCreatedElementIds(self, ) -> ISet: ...
    def GetDeletedElementIds(self, ) -> ISet: ...
    def GetModifiedElementIds(self, ) -> ISet: ...

class DocumentPreviewSettings:
    """.NET: Autodesk.Revit.DB.DocumentPreviewSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    PreviewViewId: ElementId
    IsViewUpdateForced: bool
    def Dispose(self, ) -> None: ...
    def ForceViewUpdate(self, forceViewUpdate: bool) -> None: ...
    def IsViewIdValidForPreview(self, viewId: ElementId) -> bool: ...

class DocumentSet(APIObject):
    """.NET: Autodesk.Revit.DB.DocumentSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: Document) -> bool: ...
    def Erase(self, item: Document) -> int: ...
    def ForwardIterator(self, ) -> DocumentSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: Document) -> bool: ...
    def ReverseIterator(self, ) -> DocumentSetIterator: ...

class DocumentSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.DocumentSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class DocumentType:
    """.NET: Autodesk.Revit.DB.DocumentType"""
    def __init__(self, *args) -> None: ...
    ...

class DocumentValidation:
    """.NET: Autodesk.Revit.DB.DocumentValidation"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CanDeleteElement(document: Document, elementId: ElementId) -> bool: ...

class DocumentVersion:
    """.NET: Autodesk.Revit.DB.DocumentVersion"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    NumberOfSaves: int
    VersionGUID: Guid
    def Dispose(self, ) -> None: ...
    def IsEqual(self, other: DocumentVersion) -> bool: ...

class Domain:
    """.NET: Autodesk.Revit.DB.Domain"""
    def __init__(self, *args) -> None: ...
    ...

class DoorEvacuationExitType:
    """.NET: Autodesk.Revit.DB.DoorEvacuationExitType"""
    def __init__(self, *args) -> None: ...
    ...

class DoubleArray(APIObject):
    """.NET: Autodesk.Revit.DB.DoubleArray"""
    def __init__(self, *args) -> None: ...
    Item: float
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: float) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> DoubleArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: float, index: int) -> None: ...
    def ReverseIterator(self, ) -> DoubleArrayIterator: ...

class DoubleArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.DoubleArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class DoubleParameterValue(ParameterValue):
    """.NET: Autodesk.Revit.DB.DoubleParameterValue"""
    def __init__(self, *args) -> None: ...
    Value: float
    IsValidObject: bool

class DrawLayer:
    """.NET: Autodesk.Revit.DB.DrawLayer"""
    def __init__(self, *args) -> None: ...
    ...

class DuplicateTypeAction:
    """.NET: Autodesk.Revit.DB.DuplicateTypeAction"""
    def __init__(self, *args) -> None: ...
    ...

class DuplicateTypeNamesHandlerArgs:
    """.NET: Autodesk.Revit.DB.DuplicateTypeNamesHandlerArgs"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Document: Document
    def Dispose(self, ) -> None: ...
    def GetTypeIds(self, ) -> ICollection: ...

class EaveCutterType:
    """.NET: Autodesk.Revit.DB.EaveCutterType"""
    def __init__(self, *args) -> None: ...
    ...

class Edge(GeometryObject):
    """.NET: Autodesk.Revit.DB.Edge"""
    def __init__(self, *args) -> None: ...
    ApproximateLength: float
    Reference: Reference
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool
    def AsCurve(self, ) -> Curve: ...
    def AsCurveFollowingFace(self, faceForDir: Face) -> Curve: ...
    def ComputeDerivatives(self, parameter: float) -> Transform: ...
    def Evaluate(self, param: float) -> XYZ: ...
    def EvaluateOnFace(self, param: float, face: Face) -> UV: ...
    def GetCurveUV(self, index: int, transform: Transform2D) -> CurveUV: ...
    def GetEndPointReference(self, index: int) -> Reference: ...
    def GetFace(self, index: int) -> Face: ...
    def IsFlippedOnFace(self, face: Face) -> bool: ...
    def Tessellate(self, ) -> IList: ...
    def TessellateOnFace(self, face: Face) -> IList: ...

class EdgeArray(APIObject):
    """.NET: Autodesk.Revit.DB.EdgeArray"""
    def __init__(self, *args) -> None: ...
    Item: Edge
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: Edge) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> EdgeArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: Edge, index: int) -> None: ...
    def ReverseIterator(self, ) -> EdgeArrayIterator: ...

class EdgeArrayArray(APIObject):
    """.NET: Autodesk.Revit.DB.EdgeArrayArray"""
    def __init__(self, *args) -> None: ...
    Item: EdgeArray
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: EdgeArray) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> EdgeArrayArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: EdgeArray, index: int) -> None: ...
    def ReverseIterator(self, ) -> EdgeArrayArrayIterator: ...

class EdgeArrayArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.EdgeArrayArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class EdgeArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.EdgeArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class EdgeEndPoint:
    """.NET: Autodesk.Revit.DB.EdgeEndPoint"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Index: int
    Edge: Edge
    def Dispose(self, ) -> None: ...
    def Equals(self, other: EdgeEndPoint) -> bool: ...
    def Evaluate(self, ) -> XYZ: ...

class EditModeType:
    """.NET: Autodesk.Revit.DB.EditModeType"""
    def __init__(self, *args) -> None: ...
    ...

class EditScope:
    """.NET: Autodesk.Revit.DB.EditScope"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsPermitted: bool
    IsActive: bool
    def Cancel(self, ) -> None: ...
    def Commit(self, failurePreprocessor: IFailuresPreprocessor) -> None: ...
    def Dispose(self, ) -> None: ...

class Element:
    """.NET: Autodesk.Revit.DB.Element"""
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
    def ArePhasesModifiable(self, ) -> bool: ...
    def CanBeHidden(self, pView: View) -> bool: ...
    def CanBeLocked(self, ) -> bool: ...
    def CanDeleteSubelement(self, subelem: Subelement) -> bool: ...
    @staticmethod
    def CanHaveTypeAssigned(document: Document, elementIds: ICollection) -> bool: ...
    @staticmethod
    def ChangeTypeId(document: Document, elementIds: ICollection, typeId: ElementId) -> IDictionary: ...
    def DeleteEntity(self, schema: Schema) -> bool: ...
    def DeleteSubelement(self, subelem: Subelement) -> bool: ...
    def DeleteSubelements(self, subelems: IList) -> bool: ...
    def Dispose(self, ) -> None: ...
    def EvaluateAllParameterValues(self, ) -> IList: ...
    def EvaluateParameterValues(self, parameterIds: ISet) -> IList: ...
    @staticmethod
    def GetChangeTypeAny() -> ChangeType: ...
    @staticmethod
    def GetChangeTypeElementAddition() -> ChangeType: ...
    @staticmethod
    def GetChangeTypeElementDeletion() -> ChangeType: ...
    @staticmethod
    def GetChangeTypeGeometry() -> ChangeType: ...
    @staticmethod
    def GetChangeTypeParameter(parameterId: ElementId) -> ChangeType: ...
    def GetDependentElements(self, filter: ElementFilter) -> IList: ...
    def GetEntity(self, schema: Schema) -> Entity: ...
    def GetEntitySchemaGuids(self, ) -> IList: ...
    def GetExternalFileReference(self, ) -> ExternalFileReference: ...
    def GetExternalResourceReference(self, resourceType: ExternalResourceType) -> ExternalResourceReference: ...
    def GetExternalResourceReferenceExpanded(self, resourceType: ExternalResourceType) -> IList: ...
    def GetExternalResourceReferences(self, ) -> IDictionary: ...
    def GetExternalResourceReferencesExpanded(self, ) -> IDictionary: ...
    def GetGeneratingElementIds(self, geometryObject: GeometryObject) -> ICollection: ...
    def GetGeometryObjectFromReference(self, reference: Reference) -> GeometryObject: ...
    def GetMaterialArea(self, materialId: ElementId, usePaintMaterial: bool) -> float: ...
    def GetMaterialIds(self, returnPaintMaterials: bool) -> ICollection: ...
    def GetMaterialVolume(self, materialId: ElementId) -> float: ...
    def GetMonitoredLinkElementIds(self, ) -> IList: ...
    def GetMonitoredLocalElementIds(self, ) -> IList: ...
    def GetOrderedParameters(self, ) -> IList: ...
    def GetParameter(self, parameterTypeId: ForgeTypeId) -> Parameter: ...
    def GetParameterFormatOptions(self, parameterId: ElementId) -> FormatOptions: ...
    def GetParameters(self, name: str) -> IList: ...
    def GetPhaseStatus(self, phaseId: ElementId) -> ElementOnPhaseStatus: ...
    def GetSubelements(self, ) -> IList: ...
    def GetTypeId(self, ) -> ElementId: ...
    @staticmethod
    def GetValidTypes(document: Document, elementIds: ICollection) -> ICollection: ...
    def HasPhases(self, ) -> bool: ...
    def IsCreatedPhaseOrderValid(self, createdPhaseId: ElementId) -> bool: ...
    def IsDemolishedPhaseOrderValid(self, demolishedPhaseId: ElementId) -> bool: ...
    def IsExternalFileReference(self, ) -> bool: ...
    def IsHidden(self, pView: View) -> bool: ...
    def IsMonitoringLinkElement(self, ) -> bool: ...
    def IsMonitoringLocalElement(self, ) -> bool: ...
    def IsPhaseCreatedValid(self, createdPhaseId: ElementId) -> bool: ...
    def IsPhaseDemolishedValid(self, demolishedPhaseId: ElementId) -> bool: ...
    @staticmethod
    def IsValidType(document: Document, elementIds: ICollection, typeId: ElementId) -> bool: ...
    def LookupParameter(self, name: str) -> Parameter: ...
    def RefersToExternalResourceReference(self, resourceType: ExternalResourceType) -> bool: ...
    def RefersToExternalResourceReferences(self, ) -> bool: ...
    def SetEntity(self, entity: Entity) -> None: ...

class ElementArray(APIObject):
    """.NET: Autodesk.Revit.DB.ElementArray"""
    def __init__(self, *args) -> None: ...
    Item: Element
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: Element) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> ElementArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: Element, index: int) -> None: ...
    def ReverseIterator(self, ) -> ElementArrayIterator: ...

class ElementArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.ElementArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ElementBinding(Binding):
    """.NET: Autodesk.Revit.DB.ElementBinding"""
    def __init__(self, *args) -> None: ...
    Categories: CategorySet
    IsReadOnly: bool

class ElementCategoryFilter(ElementQuickFilter):
    """.NET: Autodesk.Revit.DB.ElementCategoryFilter"""
    def __init__(self, *args) -> None: ...
    CategoryId: ElementId
    IsValidObject: bool
    Inverted: bool

class ElementClassFilter(ElementQuickFilter):
    """.NET: Autodesk.Revit.DB.ElementClassFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool
    def GetElementClass(self, ) -> Type: ...

class ElementDesignOptionFilter(ElementQuickFilter):
    """.NET: Autodesk.Revit.DB.ElementDesignOptionFilter"""
    def __init__(self, *args) -> None: ...
    DesignOptionId: ElementId
    IsValidObject: bool
    Inverted: bool

class ElementFilter:
    """.NET: Autodesk.Revit.DB.ElementFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool
    def Dispose(self, ) -> None: ...
    def PassesFilter(self, document: Document, id: ElementId) -> bool: ...

class ElementId:
    """.NET: Autodesk.Revit.DB.ElementId"""
    def __init__(self, *args) -> None: ...
    InvalidElementId: ElementId
    Value: int
    def Compare(self, id: ElementId) -> int: ...
    def CompareTo(self, id: object) -> int: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    @staticmethod
    def Parse(idStr: str) -> ElementId: ...
    def ToString(self, ) -> str: ...
    @staticmethod
    def TryParse(idStr: str, id: ElementId) -> bool: ...

class ElementIdParameterValue(ParameterValue):
    """.NET: Autodesk.Revit.DB.ElementIdParameterValue"""
    def __init__(self, *args) -> None: ...
    Value: ElementId
    IsValidObject: bool

class ElementIdSetFilter(ElementQuickFilter):
    """.NET: Autodesk.Revit.DB.ElementIdSetFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool
    def GetIdsToInclude(self, ) -> ICollection: ...

class ElementIntersectsElementFilter(ElementIntersectsFilter):
    """.NET: Autodesk.Revit.DB.ElementIntersectsElementFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool
    def GetElement(self, ) -> Element: ...

class ElementIntersectsFilter(ElementSlowFilter):
    """.NET: Autodesk.Revit.DB.ElementIntersectsFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool
    @staticmethod
    def IsCategorySupported(element: Element) -> bool: ...
    @staticmethod
    def IsElementSupported(element: Element) -> bool: ...

class ElementIntersectsSolidFilter(ElementIntersectsFilter):
    """.NET: Autodesk.Revit.DB.ElementIntersectsSolidFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool
    def GetSolid(self, ) -> Solid: ...

class ElementIsCurveDrivenFilter(ElementQuickFilter):
    """.NET: Autodesk.Revit.DB.ElementIsCurveDrivenFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool

class ElementIsElementTypeFilter(ElementQuickFilter):
    """.NET: Autodesk.Revit.DB.ElementIsElementTypeFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool

class ElementLevelFilter(ElementSlowFilter):
    """.NET: Autodesk.Revit.DB.ElementLevelFilter"""
    def __init__(self, *args) -> None: ...
    LevelId: ElementId
    IsValidObject: bool
    Inverted: bool

class ElementLogicalFilter(ElementFilter):
    """.NET: Autodesk.Revit.DB.ElementLogicalFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool
    def GetFilters(self, ) -> IList: ...
    def SetFilters(self, filters: IList) -> None: ...

class ElementMulticategoryFilter(ElementQuickFilter):
    """.NET: Autodesk.Revit.DB.ElementMulticategoryFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool
    def GetCategoryIds(self, ) -> ICollection: ...

class ElementMulticlassFilter(ElementQuickFilter):
    """.NET: Autodesk.Revit.DB.ElementMulticlassFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool

class ElementNode(RenderNode):
    """.NET: Autodesk.Revit.DB.ElementNode"""
    def __init__(self, *args) -> None: ...
    LinkInstanceId: ElementId
    Document: Document
    ElementId: ElementId
    IsValidObject: bool
    NodeName: str

class ElementOnPhaseStatus:
    """.NET: Autodesk.Revit.DB.ElementOnPhaseStatus"""
    def __init__(self, *args) -> None: ...
    ...

class ElementOwnerViewFilter(ElementQuickFilter):
    """.NET: Autodesk.Revit.DB.ElementOwnerViewFilter"""
    def __init__(self, *args) -> None: ...
    ViewId: ElementId
    IsValidObject: bool
    Inverted: bool

class ElementParameterFilter(ElementSlowFilter):
    """.NET: Autodesk.Revit.DB.ElementParameterFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool
    def GetRules(self, ) -> IList: ...

class ElementPhaseStatusFilter(ElementSlowFilter):
    """.NET: Autodesk.Revit.DB.ElementPhaseStatusFilter"""
    def __init__(self, *args) -> None: ...
    PhaseId: ElementId
    IsValidObject: bool
    Inverted: bool
    def GetPhaseStatuses(self, ) -> ICollection: ...

class ElementQuickFilter(ElementFilter):
    """.NET: Autodesk.Revit.DB.ElementQuickFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool

class ElementRecord:
    """.NET: Autodesk.Revit.DB.ElementRecord"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    WorksetId: WorksetId
    def Dispose(self, ) -> None: ...
    def GetBoundingBox(self, ) -> Outline: ...
    def GetCategoryId(self, ) -> ElementId: ...
    def GetDesignOptionId(self, ) -> ElementId: ...
    def GetId(self, ) -> ElementId: ...
    def GetOwnerViewId(self, ) -> ElementId: ...
    def HasBoundingBox(self, ) -> bool: ...
    def IsAnElementType(self, ) -> bool: ...
    def IsCurveDriven(self, ) -> bool: ...

class ElementReferenceType:
    """.NET: Autodesk.Revit.DB.ElementReferenceType"""
    def __init__(self, *args) -> None: ...
    ...

class ElementSet(APIObject):
    """.NET: Autodesk.Revit.DB.ElementSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: Element) -> bool: ...
    def Erase(self, item: Element) -> int: ...
    def ForwardIterator(self, ) -> ElementSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: Element) -> bool: ...
    def ReverseIterator(self, ) -> ElementSetIterator: ...

class ElementSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.ElementSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ElementSlowFilter(ElementFilter):
    """.NET: Autodesk.Revit.DB.ElementSlowFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool

class ElementStructuralTypeFilter(ElementQuickFilter):
    """.NET: Autodesk.Revit.DB.ElementStructuralTypeFilter"""
    def __init__(self, *args) -> None: ...
    StructuralType: StructuralType
    IsValidObject: bool
    Inverted: bool

class ElementTransformUtils:
    """.NET: Autodesk.Revit.DB.ElementTransformUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CanMirrorElement(ADoc: Document, elemId: ElementId) -> bool: ...
    @staticmethod
    def CanMirrorElements(ADoc: Document, elemIds: ICollection) -> bool: ...
    @staticmethod
    def CopyElement(document: Document, elementToCopy: ElementId, translation: XYZ) -> ICollection: ...
    @staticmethod
    def CopyElements(sourceView: View, elementsToCopy: ICollection, destinationView: View, additionalTransform: Transform, options: CopyPasteOptions) -> ICollection: ...
    @staticmethod
    def GetTransformFromViewToView(sourceView: View, destinationView: View) -> Transform: ...
    @staticmethod
    def MirrorElement(document: Document, elementToMirror: ElementId, plane: Plane) -> None: ...
    @staticmethod
    def MirrorElements(document: Document, elementsToMirror: ICollection, plane: Plane, mirrorCopies: bool) -> IList: ...
    @staticmethod
    def MoveElement(document: Document, elementToMove: ElementId, translation: XYZ) -> None: ...
    @staticmethod
    def MoveElements(document: Document, elementsToMove: ICollection, translation: XYZ) -> None: ...
    @staticmethod
    def RotateElement(document: Document, elementToRotate: ElementId, axis: Line, angle: float) -> None: ...
    @staticmethod
    def RotateElements(document: Document, elementsToRotate: ICollection, axis: Line, angle: float) -> None: ...

class ElementType(Element):
    """.NET: Autodesk.Revit.DB.ElementType"""
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
    def Duplicate(self, name: str) -> ElementType: ...
    def GetPreviewImage(self, size: Size) -> Bitmap: ...
    def GetSimilarTypes(self, ) -> ICollection: ...
    def IsSimilarType(self, typeId: ElementId) -> bool: ...
    def IsValidDefaultFamilyType(self, familyCategoryId: ElementId) -> bool: ...

class ElementTypeGroup:
    """.NET: Autodesk.Revit.DB.ElementTypeGroup"""
    def __init__(self, *args) -> None: ...
    ...

class ElementWorksetFilter(ElementQuickFilter):
    """.NET: Autodesk.Revit.DB.ElementWorksetFilter"""
    def __init__(self, *args) -> None: ...
    WorksetId: WorksetId
    IsValidObject: bool
    Inverted: bool

class ElevationMarker(Element):
    """.NET: Autodesk.Revit.DB.ElevationMarker"""
    def __init__(self, *args) -> None: ...
    IsReference: bool
    MaximumViewCount: int
    CurrentViewCount: int
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
    def CreateElevation(self, document: Document, viewPlanId: ElementId, index: int) -> ViewSection: ...
    @staticmethod
    def CreateElevationMarker(document: Document, viewFamilyTypeId: ElementId, origin: XYZ, initialViewScale: int) -> ElevationMarker: ...
    def CreateReferenceElevation(self, document: Document, index: int, viewIdToReference: ElementId) -> None: ...
    @staticmethod
    def CreateReferenceElevationMarker(document: Document, viewFamilyTypeId: ElementId, origin: XYZ, viewPlanId: ElementId) -> ElevationMarker: ...
    def GetViewId(self, index: int) -> ElementId: ...
    def HasElevations(self, ) -> bool: ...
    def IsAvailableIndex(self, index: int) -> bool: ...

class Ellipse(Curve):
    """.NET: Autodesk.Revit.DB.Ellipse"""
    def __init__(self, *args) -> None: ...
    RadiusY: float
    RadiusX: float
    YDirection: XYZ
    XDirection: XYZ
    Normal: XYZ
    Center: XYZ
    Period: float
    IsCyclic: bool
    Length: float
    ApproximateLength: float
    Reference: Reference
    IsClosed: bool
    IsBound: bool
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool
    @staticmethod
    def CreateCurve(center: XYZ, xRadius: float, yRadius: float, xAxis: XYZ, yAxis: XYZ, startParameter: float, endParameter: float) -> Curve: ...

class EmbodiedCarbonAsset:
    """.NET: Autodesk.Revit.DB.EmbodiedCarbonAsset"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Name: str
    CarbonCoefficientUnitType: EmbodiedCarbonCoefficientUnitType
    CarbonCoefficient: float
    CategoryName: str
    CategoryId: str
    ProviderName: str
    ProviderId: str
    def Dispose(self, ) -> None: ...
    def EqualsEmbodiedCarbonOnly(self, other: EmbodiedCarbonAsset) -> bool: ...

class EmbodiedCarbonCoefficientUnitType:
    """.NET: Autodesk.Revit.DB.EmbodiedCarbonCoefficientUnitType"""
    def __init__(self, *args) -> None: ...
    ...

class EndCapCondition:
    """.NET: Autodesk.Revit.DB.EndCapCondition"""
    def __init__(self, *args) -> None: ...
    ...

class EntryAndSchemeConsistency:
    """.NET: Autodesk.Revit.DB.EntryAndSchemeConsistency"""
    def __init__(self, *args) -> None: ...
    ...

class EvaluatedParameter:
    """.NET: Autodesk.Revit.DB.EvaluatedParameter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    StorageType: StorageType
    HasValue: bool
    Value: ParameterValue
    Definition: InternalDefinition
    def AsValueString(self, doc: Document, options: FormatOptions) -> str: ...
    def Dispose(self, ) -> None: ...

class ExclusionFilter(ElementQuickFilter):
    """.NET: Autodesk.Revit.DB.ExclusionFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool
    def GetIdsToExclude(self, ) -> ICollection: ...

class ExportColorMode:
    """.NET: Autodesk.Revit.DB.ExportColorMode"""
    def __init__(self, *args) -> None: ...
    ...

class ExportColumnHeaders:
    """.NET: Autodesk.Revit.DB.ExportColumnHeaders"""
    def __init__(self, *args) -> None: ...
    ...

class ExportDGNSettings(Element):
    """.NET: Autodesk.Revit.DB.ExportDGNSettings"""
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
    def Create(document: Document, name: str, options: DGNExportOptions) -> ExportDGNSettings: ...
    @staticmethod
    def FindByName(aDoc: Document, name: str) -> ExportDGNSettings: ...
    @staticmethod
    def GetActivePredefinedSettings(aDoc: Document) -> ExportDGNSettings: ...
    def GetDGNExportOptions(self, ) -> DGNExportOptions: ...
    @staticmethod
    def ListNames(aDoc: Document) -> IList: ...
    def SetDGNExportOptions(self, options: DGNExportOptions) -> None: ...

class ExportDWGSettings(Element):
    """.NET: Autodesk.Revit.DB.ExportDWGSettings"""
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
    def Create(document: Document, name: str, options: DXFExportOptions) -> ExportDWGSettings: ...
    @staticmethod
    def FindByName(aDoc: Document, name: str) -> ExportDWGSettings: ...
    @staticmethod
    def GetActivePredefinedSettings(aDoc: Document) -> ExportDWGSettings: ...
    def GetDWGExportOptions(self, ) -> DWGExportOptions: ...
    def GetDXFExportOptions(self, ) -> DXFExportOptions: ...
    @staticmethod
    def ListNames(aDoc: Document) -> IList: ...
    def SetDWGExportOptions(self, options: DWGExportOptions) -> None: ...
    def SetDXFExportOptions(self, options: DXFExportOptions) -> None: ...

class ExportFontInfo:
    """.NET: Autodesk.Revit.DB.ExportFontInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    DestinationFontName: str
    def Dispose(self, ) -> None: ...

class ExportFontKey:
    """.NET: Autodesk.Revit.DB.ExportFontKey"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    OriginalFontName: str
    def Dispose(self, ) -> None: ...

class ExportFontTable:
    """.NET: Autodesk.Revit.DB.ExportFontTable"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Count: int
    Item: ExportFontInfo
    def Add(self, exportFontKey: ExportFontKey, exportFontInfo: ExportFontInfo) -> None: ...
    def Clear(self, ) -> None: ...
    def ContainsKey(self, exportfontKey: ExportFontKey) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetExportFontInfo(self, exportFontKey: ExportFontKey) -> ExportFontInfo: ...
    def GetFontTableIterator(self, ) -> ExportFontTableIterator: ...
    def GetKeys(self, ) -> IList: ...
    def GetValues(self, ) -> IList: ...
    def Remove(self, exportFontKey: ExportFontKey) -> None: ...

class ExportFontTableIterator:
    """.NET: Autodesk.Revit.DB.ExportFontTableIterator"""
    def __init__(self, *args) -> None: ...
    Current: KeyValuePair
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def IsDone(self, ) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ExportIFCCategoryInfo:
    """.NET: Autodesk.Revit.DB.ExportIFCCategoryInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IFCPresentationLayerName: str
    IFCUserDefinedType: str
    IFCPredefinedType: str
    IFCEntityName: str
    IFCExportFlag: bool
    def Dispose(self, ) -> None: ...
    def IsDefault(self, ) -> bool: ...

class ExportIFCCategoryKey:
    """.NET: Autodesk.Revit.DB.ExportIFCCategoryKey"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    CustomSubCategoryId: CustomSubCategoryId
    SubCategoryName: str
    CategoryName: str
    def Dispose(self, ) -> None: ...

class ExportLayerInfo:
    """.NET: Autodesk.Revit.DB.ExportLayerInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    CutColorNumber: int
    ColorNumber: int
    CutLayerName: str
    LayerName: str
    ColorName: str
    CategoryType: LayerCategoryType
    def AddCutLayerModifier(self, layerModifier: LayerModifier) -> None: ...
    def AddLayerModifier(self, layerModifier: LayerModifier) -> None: ...
    def ClearCutLayerModifiers(self, ) -> None: ...
    def ClearLayerModifiers(self, ) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetCutLayerModifiers(self, ) -> IList: ...
    def GetLayerModifiers(self, ) -> IList: ...
    def RemoveCutLayerModifier(self, layerModifier: LayerModifier) -> None: ...
    def RemoveLayerModifier(self, layerModifier: LayerModifier) -> None: ...
    def SetCutLayerModifiers(self, cutLayermodifiers: IList) -> None: ...
    def SetLayerModifiers(self, layermodifiers: IList) -> None: ...

class ExportLayerKey:
    """.NET: Autodesk.Revit.DB.ExportLayerKey"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    SpecialType: SpecialType
    SubCategoryName: str
    CategoryName: str
    def Dispose(self, ) -> None: ...

class ExportLayerTable:
    """.NET: Autodesk.Revit.DB.ExportLayerTable"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Count: int
    Item: ExportLayerInfo
    def Add(self, exportLayerKey: ExportLayerKey, exportLayerInfo: ExportLayerInfo) -> None: ...
    def Clear(self, ) -> None: ...
    def ContainsKey(self, exportlayerKey: ExportLayerKey) -> bool: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetAvaliableLayerModifierTypes(document: Document, exportLayerKey: ExportLayerKey) -> IList: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetExportLayerInfo(self, exportLayerKey: ExportLayerKey) -> ExportLayerInfo: ...
    def GetKeys(self, ) -> IList: ...
    def GetLayerTableIterator(self, ) -> ExportLayerTableIterator: ...
    def GetValues(self, ) -> IList: ...
    def Remove(self, exportLayerKey: ExportLayerKey) -> None: ...

class ExportLayerTableIterator:
    """.NET: Autodesk.Revit.DB.ExportLayerTableIterator"""
    def __init__(self, *args) -> None: ...
    Current: KeyValuePair
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def IsDone(self, ) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ExportLinetypeInfo:
    """.NET: Autodesk.Revit.DB.ExportLinetypeInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    DestinationLinetypeName: str
    def Dispose(self, ) -> None: ...

class ExportLinetypeKey:
    """.NET: Autodesk.Revit.DB.ExportLinetypeKey"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    OriginalLinetypeName: str
    def Dispose(self, ) -> None: ...

class ExportLinetypeTable:
    """.NET: Autodesk.Revit.DB.ExportLinetypeTable"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Count: int
    Item: ExportLinetypeInfo
    def Add(self, exportLinetypeKey: ExportLinetypeKey, exportLinetypeInfo: ExportLinetypeInfo) -> None: ...
    def Clear(self, ) -> None: ...
    def ContainsKey(self, exportLinetypeKey: ExportLinetypeKey) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetExportLinetypeInfo(self, exportLinetypeKey: ExportLinetypeKey) -> ExportLinetypeInfo: ...
    def GetKeys(self, ) -> IList: ...
    def GetLinetypeTableIterator(self, ) -> ExportLinetypeTableIterator: ...
    def GetValues(self, ) -> IList: ...
    def Remove(self, exportLinetypeKey: ExportLinetypeKey) -> None: ...

class ExportLinetypeTableIterator:
    """.NET: Autodesk.Revit.DB.ExportLinetypeTableIterator"""
    def __init__(self, *args) -> None: ...
    Current: KeyValuePair
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def IsDone(self, ) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ExportLineweightInfo:
    """.NET: Autodesk.Revit.DB.ExportLineweightInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    DestinationLineweightName: str
    def Dispose(self, ) -> None: ...

class ExportLineweightKey:
    """.NET: Autodesk.Revit.DB.ExportLineweightKey"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    OriginalLineweight: int
    def Dispose(self, ) -> None: ...

class ExportLineweightTable:
    """.NET: Autodesk.Revit.DB.ExportLineweightTable"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Count: int
    Item: ExportLineweightInfo
    def Add(self, exportLineweightKey: ExportLineweightKey, exportLineweightInfo: ExportLineweightInfo) -> None: ...
    def Clear(self, ) -> None: ...
    def ContainsKey(self, exportLineweightKey: ExportLineweightKey) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetExportLineweightInfo(self, exportLineweightKey: ExportLineweightKey) -> ExportLineweightInfo: ...
    def GetKeys(self, ) -> IList: ...
    def GetLineweightTableIterator(self, ) -> ExportLineweightTableIterator: ...
    def GetValues(self, ) -> IList: ...
    def Remove(self, exportLineweightKey: ExportLineweightKey) -> None: ...

class ExportLineweightTableIterator:
    """.NET: Autodesk.Revit.DB.ExportLineweightTableIterator"""
    def __init__(self, *args) -> None: ...
    Current: KeyValuePair
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def IsDone(self, ) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ExportPDFSettings(Element):
    """.NET: Autodesk.Revit.DB.ExportPDFSettings"""
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
    def Create(document: Document, name: str, options: PDFExportOptions) -> ExportPDFSettings: ...
    @staticmethod
    def FindByName(document: Document, name: str) -> ExportPDFSettings: ...
    @staticmethod
    def GetActivePredefinedSettings(document: Document) -> ExportPDFSettings: ...
    def GetOptions(self, ) -> PDFExportOptions: ...
    @staticmethod
    def IsValidName(document: Document, name: str) -> bool: ...
    @staticmethod
    def ListNames(document: Document) -> IList: ...
    def SetOptions(self, options: PDFExportOptions) -> None: ...

class ExportPaperFormat:
    """.NET: Autodesk.Revit.DB.ExportPaperFormat"""
    def __init__(self, *args) -> None: ...
    ...

class ExportPatternInfo:
    """.NET: Autodesk.Revit.DB.ExportPatternInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    DestinationPatternName: str
    def Dispose(self, ) -> None: ...

class ExportPatternKey:
    """.NET: Autodesk.Revit.DB.ExportPatternKey"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    OriginalFillPatternName: str
    OriginalFillPatternType: FillPatternTarget
    def Dispose(self, ) -> None: ...

class ExportPatternTable:
    """.NET: Autodesk.Revit.DB.ExportPatternTable"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Count: int
    Item: ExportPatternInfo
    def Add(self, exportPatternKey: ExportPatternKey, exportPatternInfo: ExportPatternInfo) -> None: ...
    def Clear(self, ) -> None: ...
    def ContainsKey(self, exportpatternKey: ExportPatternKey) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetExportPatternInfo(self, exportPatternKey: ExportPatternKey) -> ExportPatternInfo: ...
    def GetKeys(self, ) -> IList: ...
    def GetPatternTableIterator(self, ) -> ExportPatternTableIterator: ...
    def GetValues(self, ) -> IList: ...
    def Remove(self, exportPatternKey: ExportPatternKey) -> None: ...

class ExportPatternTableIterator:
    """.NET: Autodesk.Revit.DB.ExportPatternTableIterator"""
    def __init__(self, *args) -> None: ...
    Current: KeyValuePair
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def IsDone(self, ) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ExportRange:
    """.NET: Autodesk.Revit.DB.ExportRange"""
    def __init__(self, *args) -> None: ...
    ...

class ExportResolution:
    """.NET: Autodesk.Revit.DB.ExportResolution"""
    def __init__(self, *args) -> None: ...
    ...

class ExportSheetType:
    """.NET: Autodesk.Revit.DB.ExportSheetType"""
    def __init__(self, *args) -> None: ...
    ...

class ExportTextQualifier:
    """.NET: Autodesk.Revit.DB.ExportTextQualifier"""
    def __init__(self, *args) -> None: ...
    ...

class ExportUnit:
    """.NET: Autodesk.Revit.DB.ExportUnit"""
    def __init__(self, *args) -> None: ...
    ...

class ExportUtils:
    """.NET: Autodesk.Revit.DB.ExportUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetExportId(document: Document, elementId: ElementId) -> Guid: ...
    @staticmethod
    def GetGBXMLDocumentId(document: Document) -> Guid: ...
    @staticmethod
    def GetNurbsSurfaceDataForSurface(surface: Surface) -> NurbsSurfaceData: ...

class ExternalDBApplicationResult:
    """.NET: Autodesk.Revit.DB.ExternalDBApplicationResult"""
    def __init__(self, *args) -> None: ...
    ...

class ExternalDefinition(Definition):
    """.NET: Autodesk.Revit.DB.ExternalDefinition"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    HideWhenNoValue: bool
    UserModifiable: bool
    Description: str
    OwnerGroup: DefinitionGroup
    Visible: bool
    GUID: Guid
    Name: str
    def Dispose(self, ) -> None: ...
    def GetGroupTypeId(self, ) -> ForgeTypeId: ...

class ExternalDefinitionCreationOptions:
    """.NET: Autodesk.Revit.DB.ExternalDefinitionCreationOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    HideWhenNoValue: bool
    UserModifiable: bool
    Description: str
    GUID: Guid
    Visible: bool
    Name: str
    def Dispose(self, ) -> None: ...
    def GetDataType(self, ) -> ForgeTypeId: ...
    def SetDataType(self, dataType: ForgeTypeId) -> None: ...

class ExternalDefinitions(Definitions):
    """.NET: Autodesk.Revit.DB.ExternalDefinitions"""
    def __init__(self, *args) -> None: ...
    Size: int
    IsEmpty: bool
    Item: Definition

class ExternalFileReference:
    """.NET: Autodesk.Revit.DB.ExternalFileReference"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ExternalFileReferenceType: ExternalFileReferenceType
    PathType: PathType
    def Dispose(self, ) -> None: ...
    def GetAbsolutePath(self, ) -> ModelPath: ...
    def GetLinkedFileStatus(self, ) -> LinkedFileStatus: ...
    def GetPath(self, ) -> ModelPath: ...
    def GetReferencingId(self, ) -> ElementId: ...
    @staticmethod
    def IsValidExternalFileReference(data: ExternalFileReference) -> bool: ...
    def IsValidPathTypeForExternalFileReference(self, pathType: PathType) -> bool: ...

class ExternalFileReferenceType:
    """.NET: Autodesk.Revit.DB.ExternalFileReferenceType"""
    def __init__(self, *args) -> None: ...
    ...

class ExternalFileUtils:
    """.NET: Autodesk.Revit.DB.ExternalFileUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetAllExternalFileReferences(aDoc: Document) -> ICollection: ...
    @staticmethod
    def GetExternalFileReference(aDoc: Document, elemId: ElementId) -> ExternalFileReference: ...
    @staticmethod
    def GetFileBasedTempFolder(filename: str) -> str: ...
    @staticmethod
    def IsExternalFileReference(aDoc: Document, elemId: ElementId) -> bool: ...

class ExternalGeometryId:
    """.NET: Autodesk.Revit.DB.ExternalGeometryId"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Id: str
    def Dispose(self, ) -> None: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    @staticmethod
    def IsValidExternalGeometryId(externalGeometryId: str) -> bool: ...

class ExternalResourceBrowserData:
    """.NET: Autodesk.Revit.DB.ExternalResourceBrowserData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    FolderPath: str
    ServerId: Guid
    def AddResource(self, resourceName: str, version: str, referenceInformation: IDictionary) -> None: ...
    def AddSubFolder(self, folderName: str, iconPath: str) -> None: ...
    def CallingDocumentHasModelPath(self, ) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetCallingDocumentModelPath(self, ) -> ModelPath: ...
    def GetMatchOptions(self, ) -> ExternalResourceMatchOptions: ...
    def GetResources(self, ) -> IList: ...
    def GetSubFoldersData(self, ) -> IList: ...
    def IsValidFolderName(self, folderName: str) -> bool: ...
    def IsValidResourceName(self, resourceName: str) -> bool: ...

class ExternalResourceLoadContent:
    """.NET: Autodesk.Revit.DB.ExternalResourceLoadContent"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LoadStatus: ExternalResourceLoadStatus
    Version: str
    def Dispose(self, ) -> None: ...

class ExternalResourceLoadContext:
    """.NET: Autodesk.Revit.DB.ExternalResourceLoadContext"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LoadOperationType: LoadOperationType
    def CallingDocumentHasModelPath(self, ) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetCallingDocumentModelPath(self, ) -> ModelPath: ...
    def GetCurrentlyLoadedReference(self, ) -> ExternalResourceReference: ...

class ExternalResourceLoadData:
    """.NET: Autodesk.Revit.DB.ExternalResourceLoadData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LoadStatus: ExternalResourceLoadStatus
    ExternalResourceType: ExternalResourceType
    ErrorsReported: bool
    def Dispose(self, ) -> None: ...
    def GetExternalResourceReference(self, ) -> ExternalResourceReference: ...
    def GetLoadContent(self, ) -> ExternalResourceLoadContent: ...
    def GetLoadContext(self, ) -> ExternalResourceLoadContext: ...
    def GetLoadRequestId(self, ) -> Guid: ...

class ExternalResourceLoadStatus:
    """.NET: Autodesk.Revit.DB.ExternalResourceLoadStatus"""
    def __init__(self, *args) -> None: ...
    ...

class ExternalResourceMatchOptions:
    """.NET: Autodesk.Revit.DB.ExternalResourceMatchOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ResourceType: ExternalResourceType
    def Dispose(self, ) -> None: ...

class ExternalResourceReference:
    """.NET: Autodesk.Revit.DB.ExternalResourceReference"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    InSessionPath: str
    Version: str
    ServerId: Guid
    @staticmethod
    def CreateLocalResource(doc: Document, resourceType: ExternalResourceType, path: ModelPath, pathType: PathType) -> ExternalResourceReference: ...
    def Dispose(self, ) -> None: ...
    def GetReferenceInformation(self, ) -> IDictionary: ...
    def GetResourceShortDisplayName(self, ) -> str: ...
    def GetResourceVersionStatus(self, ) -> ResourceVersionStatus: ...
    def HasValidDisplayPath(self, ) -> bool: ...
    def IsValidReference(self, resourceType: ExternalResourceType) -> bool: ...

class ExternalResourceServerExtensions:
    """.NET: Autodesk.Revit.DB.ExternalResourceServerExtensions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetCADLinkOperations(self, ) -> CADLinkOperations: ...
    def GetRevitLinkOperations(self, ) -> RevitLinkOperations: ...

class ExternalResourceServerUtils:
    """.NET: Autodesk.Revit.DB.ExternalResourceServerUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def IsValidShortName(serverId: Guid, serverName: str) -> bool: ...
    @staticmethod
    def ServerSupportsAssemblyCodeData(extRef: ExternalResourceReference) -> bool: ...
    @staticmethod
    def ServerSupportsCADLinks(extRef: ExternalResourceReference) -> bool: ...
    @staticmethod
    def ServerSupportsIFCLinks(extRef: ExternalResourceReference) -> bool: ...
    @staticmethod
    def ServerSupportsKeynotes(extRef: ExternalResourceReference) -> bool: ...
    @staticmethod
    def ServerSupportsRevitLinks(extRef: ExternalResourceReference) -> bool: ...

class ExternalResourceServiceUtils:
    """.NET: Autodesk.Revit.DB.ExternalResourceServiceUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetServersByType(type: ExternalResourceType) -> IList: ...

class ExternalResourceSubFolder:
    """.NET: Autodesk.Revit.DB.ExternalResourceSubFolder"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IconPath: str
    FolderName: str
    def Dispose(self, ) -> None: ...

class ExternalResourceType(GuidEnum):
    """.NET: Autodesk.Revit.DB.ExternalResourceType"""
    def __init__(self, *args) -> None: ...
    Guid: Guid

class ExternalResourceTypes:
    """.NET: Autodesk.Revit.DB.ExternalResourceTypes"""
    def __init__(self, *args) -> None: ...
    ...

class ExternalResourceUIBrowseResultType:
    """.NET: Autodesk.Revit.DB.ExternalResourceUIBrowseResultType"""
    def __init__(self, *args) -> None: ...
    ...

class ExternalResourceUtils:
    """.NET: Autodesk.Revit.DB.ExternalResourceUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetAllExternalResourceReferences(document: Document, resourceType: ExternalResourceType) -> ISet: ...

class ExternallyTaggedBRep(ExternallyTaggedGeometryObject):
    """.NET: Autodesk.Revit.DB.ExternallyTaggedBRep"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ExternalId: ExternalGeometryId
    def GetTaggedGeometry(self, externalId: ExternalGeometryId) -> GeometryObject: ...

class ExternallyTaggedGeometryObject:
    """.NET: Autodesk.Revit.DB.ExternallyTaggedGeometryObject"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ExternalId: ExternalGeometryId
    def Dispose(self, ) -> None: ...

class ExternallyTaggedGeometryValidation:
    """.NET: Autodesk.Revit.DB.ExternallyTaggedGeometryValidation"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def IsNonSolid(geometry: GeometryObject) -> bool: ...
    @staticmethod
    def IsSolid(geometry: GeometryObject) -> bool: ...
    @staticmethod
    def LacksSubnodes(geometry: GeometryObject) -> bool: ...

class ExternallyTaggedNonBRep(ExternallyTaggedGeometryObject):
    """.NET: Autodesk.Revit.DB.ExternallyTaggedNonBRep"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ExternalId: ExternalGeometryId
    def SetUsage(self, usage: ExternallyTaggedNonBRepUsage) -> None: ...

class ExternallyTaggedNonBRepUsage:
    """.NET: Autodesk.Revit.DB.ExternallyTaggedNonBRepUsage"""
    def __init__(self, *args) -> None: ...
    ...

class ExternallyTaggedNonBReps:
    """.NET: Autodesk.Revit.DB.ExternallyTaggedNonBReps"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Add(self, geometry: ExternallyTaggedNonBRep) -> None: ...
    def CanAddExternallyTaggedNonBRep(self, geometry: ExternallyTaggedNonBRep) -> bool: ...
    def Dispose(self, ) -> None: ...

class Extrusion(GenericForm):
    """.NET: Autodesk.Revit.DB.Extrusion"""
    def __init__(self, *args) -> None: ...
    EndOffset: float
    StartOffset: float
    Sketch: Sketch
    Subcategory: Category
    Name: str
    IsSolid: bool
    Visible: bool
    Combinations: GeomCombinationSet
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

class ExtrusionAnalyzer:
    """.NET: Autodesk.Revit.DB.ExtrusionAnalyzer"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    EndParameter: float
    StartParameter: float
    ExtrusionDirection: XYZ
    def CalculateFaceAlignment(self, ) -> IDictionary: ...
    @staticmethod
    def Create(solidGeometry: Solid, plane: Plane, direction: XYZ) -> ExtrusionAnalyzer: ...
    def Dispose(self, ) -> None: ...
    def GetExtrusionBase(self, ) -> Face: ...

class ExtrusionAnalyzerFaceAlignment:
    """.NET: Autodesk.Revit.DB.ExtrusionAnalyzerFaceAlignment"""
    def __init__(self, *args) -> None: ...
    ...

class ExtrusionRoof(RoofBase):
    """.NET: Autodesk.Revit.DB.ExtrusionRoof"""
    def __init__(self, *args) -> None: ...
    CurtainGrids: CurtainGridSet
    FasciaDepth: float
    EaveCuts: EaveCutterType
    RoofType: RoofType
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
    def GetProfile(self, ) -> ModelCurveArray: ...

class FBXExportOptions:
    """.NET: Autodesk.Revit.DB.FBXExportOptions"""
    def __init__(self, *args) -> None: ...
    WithoutBoundaryEdges: bool
    LevelsOfDetailValue: int
    UseLevelsOfDetail: bool
    StopOnError: bool

class FabricationAncillaryUsage:
    """.NET: Autodesk.Revit.DB.FabricationAncillaryUsage"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ProductCode: str
    Length: float
    Quantity: float
    AncillaryDepth: float
    AncillaryWidthOrDiameter: float
    AncillaryId: int
    UsageType: FabricationAncillaryUsageType
    Type: FabricationAncillaryType
    def Dispose(self, ) -> None: ...

class FabricationConfiguration(Element):
    """.NET: Autodesk.Revit.DB.FabricationConfiguration"""
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
    def AirturnExists(self, airturnId: int) -> bool: ...
    def AncillaryExists(self, ancillaryId: int) -> bool: ...
    def AreItemFilesLoaded(self, itemFiles: IList) -> bool: ...
    def CanBeSwapped(self, ) -> bool: ...
    def CanUnloadItemFiles(self, itemFiles: IList) -> bool: ...
    def CheckConnectionsForAllFabricationParts(self, ) -> int: ...
    def CustomDataExists(self, customDataId: int) -> bool: ...
    def DamperExists(self, damperId: int) -> bool: ...
    def GetAirturnName(self, airturnId: int) -> str: ...
    def GetAllAirturnIds(self, ) -> IList: ...
    def GetAllDampers(self, ) -> IList: ...
    def GetAllFabricationConnectorDefinitions(self, domain: ConnectorDomainType, shape: ConnectorProfileType) -> IList: ...
    def GetAllInsulationSpecifications(self, pFabPart: FabricationPart) -> IList: ...
    def GetAllLoadedItemFiles(self, ) -> IList: ...
    def GetAllLoadedServices(self, ) -> IList: ...
    def GetAllMaterials(self, part: FabricationPart) -> IList: ...
    def GetAllPartCustomData(self, ) -> IList: ...
    def GetAllPartStatuses(self, ) -> IList: ...
    def GetAllSeamIds(self, ) -> IList: ...
    def GetAllServices(self, ) -> IList: ...
    def GetAllSpecifications(self, part: FabricationPart) -> IList: ...
    def GetAllStiffenerIds(self, ) -> IList: ...
    def GetAllUsedItemFiles(self, ) -> IList: ...
    def GetAllUsedServices(self, ) -> IList: ...
    def GetAncillaries(self, type: FabricationAncillaryType, includeKits: bool, filterKits: bool) -> IList: ...
    def GetAncillaryGroup(self, ancillaryId: int) -> str: ...
    def GetAncillaryGroupName(self, ancillaryId: int) -> str: ...
    def GetAncillaryName(self, ancillaryId: int) -> str: ...
    def GetDamperName(self, damperId: int) -> str: ...
    @staticmethod
    def GetFabricationConfiguration(document: Document) -> FabricationConfiguration: ...
    def GetFabricationConfigurationInfo(self, ) -> FabricationConfigurationInfo: ...
    def GetFabricationConnectorDomain(self, fabricationConnectorId: int) -> ConnectorDomainType: ...
    def GetFabricationConnectorGroup(self, fabricationConnectorId: int) -> str: ...
    def GetFabricationConnectorName(self, fabricationConnectorId: int) -> str: ...
    def GetFabricationConnectorShape(self, fabricationConnectorId: int) -> ConnectorProfileType: ...
    def GetInsulationSpecificationAbbreviation(self, insulationSpecificationId: int) -> str: ...
    def GetInsulationSpecificationGroup(self, specId: int) -> str: ...
    def GetInsulationSpecificationName(self, specId: int) -> str: ...
    def GetItemFolders(self, ) -> IList: ...
    def GetMaterialAbbreviation(self, materialId: int) -> str: ...
    def GetMaterialByGUID(self, materialGUID: Guid) -> int: ...
    def GetMaterialGUID(self, materialId: int) -> Guid: ...
    def GetMaterialGaugeByGUID(self, gaugeGUID: Guid, materialId: int) -> int: ...
    def GetMaterialGaugeGUID(self, materialId: int, gaugeId: int) -> Guid: ...
    def GetMaterialGroup(self, materialId: int) -> str: ...
    def GetMaterialName(self, materialId: int) -> str: ...
    def GetPartCustomDataName(self, customDataId: int) -> str: ...
    def GetPartCustomDataType(self, customDataId: int) -> FabricationCustomDataType: ...
    def GetPartStatusDescription(self, statusId: int) -> str: ...
    def GetProfile(self, ) -> str: ...
    def GetSeamName(self, seamId: int) -> str: ...
    def GetService(self, serviceId: int) -> FabricationService: ...
    def GetServiceByGUID(self, serviceGUID: Guid) -> int: ...
    def GetServiceGUID(self, serviceId: int) -> Guid: ...
    def GetServiceTypeName(self, serviceTypeId: int) -> str: ...
    def GetSpecificationAbbreviation(self, specificationId: int) -> str: ...
    def GetSpecificationByGUID(self, specificationGUID: Guid) -> int: ...
    def GetSpecificationGUID(self, specificationId: int) -> Guid: ...
    def GetSpecificationGroup(self, specId: int) -> str: ...
    def GetSpecificationName(self, specId: int) -> str: ...
    def GetStiffenerName(self, stiffenerId: int) -> str: ...
    def GetUpdatedStraightsFromValidateConnections(self, ) -> ISet: ...
    def HasValidConfiguration(self, ) -> bool: ...
    def IsAncillaryKit(self, ancillaryId: int) -> bool: ...
    def LoadItemFiles(self, itemFiles: IList) -> IList: ...
    def LoadServices(self, serviceIds: IList) -> IList: ...
    def LocateFabricationConnector(self, group: str, name: str, domain: ConnectorDomainType, shape: ConnectorProfileType) -> int: ...
    def LocateInsulationSpecification(self, group: str, name: str) -> int: ...
    def LocateMaterial(self, group: str, name: str) -> int: ...
    def LocateSpecification(self, group: str, name: str) -> int: ...
    def PostReviewableWarningsForBadConnections(self, info: ConnectionValidationInfo) -> None: ...
    def ReloadConfiguration(self, ) -> ConfigurationReloadInfo: ...
    def SeamExists(self, seamId: int) -> bool: ...
    def SetConfiguration(self, fabricationConfigurationInfo: FabricationConfigurationInfo, profile: str) -> None: ...
    def SetServicesToLoad(self, serviceIds: IList) -> bool: ...
    def StiffenerExists(self, stiffenerId: int) -> bool: ...
    def UnloadItemFiles(self, itemFiles: IList) -> None: ...
    def UnloadServices(self, serviceIds: IList) -> None: ...
    def ValidateConnectionsForAllFabricationParts(self, updateGapForStraights: bool) -> ConnectionValidationInfo: ...

class FabricationConfigurationInfo:
    """.NET: Autodesk.Revit.DB.FabricationConfigurationInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsCloudConfiguration: bool
    Path: str
    UnitSystem: UnitSystem
    Description: str
    Version: float
    GUID: Guid
    CloudId: str
    IsLocked: bool
    Name: str
    def Dispose(self, ) -> None: ...
    @staticmethod
    def FindSourceFabricationConfiguration(fabricationConfiguration: FabricationConfigurationInfo) -> FabricationConfigurationInfo: ...
    @staticmethod
    def GetAllFabricationConfigurations() -> IList: ...
    def GetProfiles(self, ) -> IList: ...
    def IsValid(self, ) -> bool: ...

class FabricationConnectorInfo:
    """.NET: Autodesk.Revit.DB.FabricationConnectorInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsDoubleWallConnectorLocked: bool
    DoubleWallConnectorId: int
    FabricationIndex: int
    IsBodyConnectorLocked: bool
    BodyConnectorId: int
    def Dispose(self, ) -> None: ...
    def HasDoubleWallConnector(self, ) -> bool: ...
    def IsValid(self, ) -> bool: ...

class FabricationDimensionDefinition:
    """.NET: Autodesk.Revit.DB.FabricationDimensionDefinition"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsModifiable: bool
    UnitType: FabricationDimensionUnitType
    Type: FabricationDimensionType
    Name: str
    def Dispose(self, ) -> None: ...

class FabricationDimensionType:
    """.NET: Autodesk.Revit.DB.FabricationDimensionType"""
    def __init__(self, *args) -> None: ...
    ...

class FabricationDimensionUnitType:
    """.NET: Autodesk.Revit.DB.FabricationDimensionUnitType"""
    def __init__(self, *args) -> None: ...
    ...

class FabricationHostedInfo:
    """.NET: Autodesk.Revit.DB.FabricationHostedInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    HostId: ElementId
    def DisconnectFromHost(self, ) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetBearerCenterline(self, ) -> Line: ...
    def PlaceOnHost(self, hostId: ElementId, hostConnector: Connector, distance: float, axisRotation: float) -> None: ...

class FabricationItemFile:
    """.NET: Autodesk.Revit.DB.FabricationItemFile"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsUsed: bool
    Identifier: str
    def Dispose(self, ) -> None: ...
    def GetImage(self, ) -> Bitmap: ...
    def IsLoaded(self, ) -> bool: ...
    def IsValid(self, ) -> bool: ...

class FabricationItemFolder:
    """.NET: Autodesk.Revit.DB.FabricationItemFolder"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Name: str
    def Dispose(self, ) -> None: ...
    def GetItemFiles(self, ) -> IList: ...
    def GetSubFolders(self, ) -> IList: ...

class FabricationMaterialType:
    """.NET: Autodesk.Revit.DB.FabricationMaterialType"""
    def __init__(self, *args) -> None: ...
    ...

class FabricationOptionDefinition:
    """.NET: Autodesk.Revit.DB.FabricationOptionDefinition"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsModifiable: bool
    Name: str
    def Dispose(self, ) -> None: ...

class FabricationPart(Element):
    """.NET: Autodesk.Revit.DB.FabricationPart"""
    def __init__(self, *args) -> None: ...
    InsulationLiningElementId: ElementId
    ServiceType: int
    GeometryChecksum: AssetPropertyUInt64
    SpoolName: str
    PartGuid: Guid
    PartStatus: int
    HangerRodKit: int
    ValidationStatus: ValidationStatus
    ConnectorManager: ConnectorManager
    DomainType: ConnectorDomainType
    ItemCustomId: int
    ItemNumber: str
    MaterialGauge: int
    Material: int
    InsulationSpecification: int
    Specification: int
    ServiceId: int
    ProductCode: str
    CenterlineLength: float
    Origin: XYZ
    LevelOffset: float
    ProductInstallType: str
    ProductOriginalEquipmentManufacture: str
    ProductDataRange: str
    ProductSizeDescription: str
    ProductMaterialDescription: str
    ProductSpecificationDescription: str
    ProductFinishDescription: str
    ProductLongDescription: str
    ProductShortDescription: str
    ProductName: str
    VendorCode: str
    Vendor: str
    Alias: str
    HandlePosition: FabricationHandlePosition
    HasHandle: bool
    Notes: str
    IsBoughtOut: bool
    ServiceName: str
    CutType: int
    DoubleWallMaterialArea: float
    DoubleWallMaterialThickness: float
    DoubleWallMaterial: int
    MaterialThickness: float
    SheetMetalArea: float
    LiningArea: float
    LiningThickness: float
    LiningType: str
    InsulationArea: float
    InsulationThickness: float
    InsulationType: str
    Weight: float
    FreeSize: str
    OverallSize: str
    Size: str
    Slope: float
    HasLining: bool
    HasInsulation: bool
    HasDoubleWall: bool
    ServiceAbbreviation: str
    BottomOfPartElevation: float
    TopOfPartElevation: float
    ProductListEntry: int
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
    def AddPartCustomData(self, customId: int) -> bool: ...
    def AdjustEndLength(self, connector: Connector, lengthToAdjust: float, totalLengthOnly: bool) -> float: ...
    @staticmethod
    def AlignPartByConnector(document: Document, connector: Connector, position: XYZ, rotation: float, rotationPerpendicular: float, slope: float, justification: FabricationPartJustification, trf: Transform) -> bool: ...
    @staticmethod
    def AlignPartByConnectorToConnector(document: Document, connector: Connector, fixedConnector: Connector, rotation: float, slope: float, justification: FabricationPartJustification) -> bool: ...
    @staticmethod
    def AlignPartByConnectors(document: Document, connector: Connector, toConnector: Connector, axisRotation: float) -> bool: ...
    @staticmethod
    def AlignPartByInsertionPoint(document: Document, partId: ElementId, position: XYZ, rotation: float, rotationPerpendicular: float, slope: float, justification: FabricationPartJustification, trf: Transform) -> bool: ...
    @staticmethod
    def AlignPartByInsertionPointAndCutInToStraight(document: Document, straightId: ElementId, partId: ElementId, position: XYZ, rotation: float, slope: float, flip: bool) -> bool: ...
    def CanASlopeBeApplied(self, ) -> bool: ...
    def CanAdjustEndLength(self, connector: Connector) -> bool: ...
    def CanFlipPart(self, ) -> bool: ...
    def CanSplitStraight(self, position: XYZ) -> bool: ...
    @staticmethod
    def ConnectAndCouple(document: Document, connector: Connector, toConnector: Connector) -> bool: ...
    @staticmethod
    def Create(document: Document, button: FabricationServiceButton, width: float, depth: float, levelId: ElementId) -> FabricationPart: ...
    @staticmethod
    def CreateHanger(document: Document, button: FabricationServiceButton, condition: int, hostId: ElementId, hostConnector: Connector, distance: float, attachToStructure: bool) -> FabricationPart: ...
    def Flip(self, ) -> bool: ...
    def GetAirturnCount(self, ) -> int: ...
    def GetAirturnInfo(self, index: int, locked: bool) -> int: ...
    def GetAllFabricationBodyConnectorDefinitions(self, connector: Connector) -> IList: ...
    def GetAllFabricationDoubleWallConnectorDefinitions(self, connector: Connector) -> IList: ...
    def GetCalculatedDimensionValue(self, dim: FabricationDimensionDefinition) -> str: ...
    def GetDimensionCalculatedOptions(self, dim: FabricationDimensionDefinition) -> IList: ...
    def GetDimensionDefinitions(self, ) -> IList: ...
    def GetDimensionValue(self, dim: FabricationDimensionDefinition) -> float: ...
    def GetDimensions(self, ) -> IList: ...
    def GetHostedInfo(self, ) -> FabricationHostedInfo: ...
    def GetInsulationLiningGeometry(self, ) -> GeometryElement: ...
    def GetOptionCount(self, ) -> int: ...
    def GetOptionDefinitions(self, ) -> IList: ...
    def GetOptionValue(self, option: FabricationOptionDefinition) -> float: ...
    def GetPartAncillaryUsage(self, ) -> IList: ...
    def GetPartCustomDataInteger(self, customId: int) -> int: ...
    def GetPartCustomDataReal(self, customId: int) -> float: ...
    def GetPartCustomDataText(self, customId: int) -> str: ...
    def GetProductListEntryCount(self, ) -> int: ...
    def GetProductListEntryName(self, index: int) -> str: ...
    def GetRodInfo(self, ) -> FabricationRodInfo: ...
    def GetSeamCount(self, ) -> int: ...
    def GetSeamInfo(self, seamIndex: int, locked: bool) -> int: ...
    def GetStiffenerCount(self, ) -> int: ...
    def GetStiffenerInfo(self, index: int, locked: bool) -> int: ...
    def GetTransform(self, ) -> Transform: ...
    def GetVersionHistory(self, ) -> IList: ...
    def HasCustomData(self, customId: int) -> bool: ...
    def HasNoConnections(self, ) -> bool: ...
    def IsAHanger(self, ) -> bool: ...
    def IsAStraight(self, ) -> bool: ...
    def IsATap(self, ) -> bool: ...
    def IsDimensionCalculated(self, dim: FabricationDimensionDefinition) -> bool: ...
    def IsProductList(self, ) -> bool: ...
    def IsProductListEntryCompatibleSize(self, productEntry: int) -> bool: ...
    def IsSameAs(self, part: FabricationPart, ignoreFields: IList) -> bool: ...
    @staticmethod
    def OptimizeLengths(document: Document, partIds: ISet) -> ISet: ...
    @staticmethod
    def PlaceAsTap(document: Document, tapPartConnector: Connector, hostPartConnector: Connector, distance: float, axisRotation: float, secondaryAxisRotation: float) -> None: ...
    @staticmethod
    def PlaceFittingAsCutIn(document: Document, straightId: ElementId, fittingId: ElementId, position: XYZ, fittingConnector: Connector, axisRotation: float) -> bool: ...
    def RemovePartCustomData(self, customId: int) -> bool: ...
    @staticmethod
    def Reposition(document: Document, partId: ElementId) -> None: ...
    @staticmethod
    def RotateConnectedPartByConnector(document: Document, connector: Connector, axisRotationBy: float) -> None: ...
    @staticmethod
    def RotateConnectedTap(document: Document, tap: FabricationPart, primaryAxisRotateBy: float, secondaryAxisRotateBy: float) -> None: ...
    @staticmethod
    def SaveAsFabricationJob(document: Document, ids: ISet, filename: str, saveOptions: FabricationSaveJobOptions) -> ISet: ...
    def SetAirturnInfo(self, index: int, airturnId: int, locked: bool) -> None: ...
    def SetCalculatedDimensionValue(self, dim: FabricationDimensionDefinition, value: str) -> None: ...
    def SetDimensionValue(self, dim: FabricationDimensionDefinition, newValue: float) -> None: ...
    def SetOptionValue(self, option: FabricationOptionDefinition, newValue: float) -> None: ...
    def SetPartCustomDataInteger(self, customId: int, value: int) -> None: ...
    def SetPartCustomDataReal(self, customId: int, value: float) -> None: ...
    def SetPartCustomDataText(self, customId: int, value: str) -> None: ...
    def SetPositionByEnd(self, connector: Connector, position: XYZ) -> None: ...
    def SetSeamInfo(self, seamIndex: int, seamId: int, locked: bool) -> None: ...
    def SetStiffenerInfo(self, index: int, stiffenerId: int, locked: bool) -> None: ...
    def SplitStraight(self, document: Document, partId: ElementId, position: XYZ) -> ElementId: ...
    @staticmethod
    def StretchAndFit(document: Document, stretchConnector: Connector, target: FabricationPartRouteEnd, newPartIds: ISet) -> FabricationPartFitResult: ...

class FabricationPartInsulationLining(Element):
    """.NET: Autodesk.Revit.DB.FabricationPartInsulationLining"""
    def __init__(self, *args) -> None: ...
    OwnerId: ElementId
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

class FabricationPartType(ElementType):
    """.NET: Autodesk.Revit.DB.FabricationPartType"""
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
    def Create(document: Document, button: FabricationServiceButton, condition: int) -> FabricationPartType: ...
    @staticmethod
    def Lookup(document: Document, button: FabricationServiceButton, condition: int) -> ElementId: ...
    @staticmethod
    def ResetAssemblyTypes(document: Document) -> None: ...

class FabricationRodInfo:
    """.NET: Autodesk.Revit.DB.FabricationRodInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsAttachedToStructure: bool
    RodCount: int
    CanRodsBeHosted: bool
    def AttachToHanger(self, hangerId: ElementId, rodIndex: int, position: XYZ) -> None: ...
    def AttachToStructure(self, ) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetBearerExtension(self, rodIndex: int) -> float: ...
    def GetRodAttachedElementId(self, rodIndex: int) -> LinkElementId: ...
    def GetRodEndPosition(self, rodIndex: int) -> XYZ: ...
    def GetRodLength(self, rodIndex: int) -> float: ...
    def GetRodStructureExtension(self, rodIndex: int) -> float: ...
    def IsRodLockedWithHost(self, rodIndex: int) -> bool: ...
    def SetBearerExtension(self, rodIndex: int, length: float) -> None: ...
    def SetRodEndPosition(self, rodIndex: int, position: XYZ) -> None: ...
    def SetRodLength(self, rodIndex: int, newLength: float) -> bool: ...
    def SetRodLockedWithHost(self, rodIndex: int, locked: bool) -> None: ...
    def SetRodStructureExtension(self, rodIndex: int, extension: float) -> bool: ...

class FabricationService:
    """.NET: Autodesk.Revit.DB.FabricationService"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ServiceId: int
    PaletteCount: int
    FabricationSystemName: str
    Abbreviation: str
    Name: str
    def Dispose(self, ) -> None: ...
    def GetButton(self, paletteIndex: int, buttonIndex: int) -> FabricationServiceButton: ...
    def GetButtonCount(self, palette: int) -> int: ...
    def GetPaletteName(self, palette: int) -> str: ...
    def IsCompatibleWith(self, otherService: FabricationService) -> bool: ...
    def IsPaletteExcluded(self, paletteIndex: int) -> bool: ...
    def IsValidButtonIndex(self, paletteIndex: int, buttonIndex: int) -> bool: ...
    def IsValidPaletteIndex(self, paletteIndex: int) -> bool: ...
    def OverrideServiceButtonExclusion(self, paletteIndex: int, buttonIndex: int, exclude: bool) -> None: ...
    def ResetServiceExclusionOverrides(self, ) -> None: ...
    def SetServicePaletteExclusions(self, excludedPalettes: IList) -> bool: ...

class FabricationServiceButton:
    """.NET: Autodesk.Revit.DB.FabricationServiceButton"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsStraight: bool
    IsAHanger: bool
    ButtonIndex: int
    PaletteIndex: int
    ServiceId: int
    ConditionCount: int
    Code: str
    Name: str
    def ContainsFabricationPartType(self, partType: FabricationPartType) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetConditionDescription(self, condition: int) -> str: ...
    def GetConditionImage(self, condition: int) -> Bitmap: ...
    def GetConditionLowerValue(self, condition: int) -> float: ...
    def GetConditionName(self, condition: int) -> str: ...
    def GetConditionUpperValue(self, condition: int) -> float: ...
    def GetImage(self, ) -> Bitmap: ...
    def IsExcluded(self, ) -> bool: ...
    def IsUnrestrictedCondition(self, condition: int) -> bool: ...
    def IsValid(self, ) -> bool: ...
    @staticmethod
    def IsValidConditionIndex(button: FabricationServiceButton, condition: int) -> bool: ...

class FabricationServiceSettings(Element):
    """.NET: Autodesk.Revit.DB.FabricationServiceSettings"""
    def __init__(self, *args) -> None: ...
    AirFluidType: ElementId
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
    def GetFabricationServiceSettings(doc: Document) -> FabricationServiceSettings: ...
    def GetFluidTemperature(self, service: FabricationService) -> float: ...
    def GetFluidType(self, service: FabricationService) -> ElementId: ...
    def HasValidFluidSetting(self, service: FabricationService) -> bool: ...
    def RemoveFluidSetting(self, service: FabricationService) -> None: ...
    def SetFluidTypeAndTemperature(self, service: FabricationService, fluidId: ElementId, temperature: float) -> None: ...

class FabricationVersionInfo:
    """.NET: Autodesk.Revit.DB.FabricationVersionInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Reason: str
    Version: int
    def Dispose(self, ) -> None: ...

class Face(GeometryObject):
    """.NET: Autodesk.Revit.DB.Face"""
    def __init__(self, *args) -> None: ...
    Period: float
    IsCyclic: bool
    Area: float
    Reference: Reference
    IsTwoSided: bool
    MaterialElementId: ElementId
    EdgeLoops: EdgeArrayArray
    HasRegions: bool
    OrientationMatchesSurfaceOrientation: bool
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool
    def ComputeDerivatives(self, point: UV) -> Transform: ...
    def ComputeNormal(self, point: UV) -> XYZ: ...
    def ComputeSecondDerivatives(self, point: UV) -> FaceSecondDerivatives: ...
    def Evaluate(self, params: UV) -> XYZ: ...
    def GetBoundingBox(self, ) -> BoundingBoxUV: ...
    def GetEdgesAsCurveLoops(self, ) -> IList: ...
    def GetRegions(self, ) -> IList: ...
    def GetSurface(self, ) -> Surface: ...
    def Intersect(self, face: Face, result: Curve) -> FaceIntersectionFaceResult: ...
    def IsInside(self, point: UV, result: IntersectionResult) -> bool: ...
    def Project(self, point: XYZ) -> IntersectionResult: ...
    def Triangulate(self, levelOfDetail: float) -> Mesh: ...

class FaceArray(APIObject):
    """.NET: Autodesk.Revit.DB.FaceArray"""
    def __init__(self, *args) -> None: ...
    Item: Face
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: Face) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> FaceArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: Face, index: int) -> None: ...
    def ReverseIterator(self, ) -> FaceArrayIterator: ...

class FaceArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.FaceArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class FaceDetailNode(RenderNode):
    """.NET: Autodesk.Revit.DB.FaceDetailNode"""
    def __init__(self, *args) -> None: ...
    LineProperties: LineProperties
    IsValidObject: bool
    NodeName: str
    def GetInstanceTransform(self, ) -> Transform: ...
    def GetLinkTransform(self, ) -> Transform: ...

class FaceEdgeNode(FaceDetailNode):
    """.NET: Autodesk.Revit.DB.FaceEdgeNode"""
    def __init__(self, *args) -> None: ...
    LineProperties: LineProperties
    IsValidObject: bool
    NodeName: str
    def GetFaceEdge(self, ) -> Edge: ...

class FaceIntersectionFaceResult:
    """.NET: Autodesk.Revit.DB.FaceIntersectionFaceResult"""
    def __init__(self, *args) -> None: ...
    ...

class FaceNode(RenderNode):
    """.NET: Autodesk.Revit.DB.FaceNode"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    NodeName: str
    def GetFace(self, ) -> Face: ...

class FaceSecondDerivatives:
    """.NET: Autodesk.Revit.DB.FaceSecondDerivatives"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    MixedDerivative: XYZ
    VVDerivative: XYZ
    UUDerivative: XYZ
    def Dispose(self, ) -> None: ...

class FaceSilhouetteNode(FaceDetailNode):
    """.NET: Autodesk.Revit.DB.FaceSilhouetteNode"""
    def __init__(self, *args) -> None: ...
    LineProperties: LineProperties
    IsValidObject: bool
    NodeName: str
    def GetFace(self, ) -> Face: ...

class FaceSplitter(Element):
    """.NET: Autodesk.Revit.DB.FaceSplitter"""
    def __init__(self, *args) -> None: ...
    SplitElementId: ElementId
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
    def GetBoundaries(self, ) -> IList: ...

class FaceToposolid(HostObject):
    """.NET: Autodesk.Revit.DB.FaceToposolid"""
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
    def Create(document: Document, toposolidTypeId: ElementId, levelId: ElementId, faceReferences: IList) -> FaceToposolid: ...
    def GetReferencedFaces(self, ) -> IList: ...
    def SetFaceReferences(self, faceReferences: IList) -> None: ...
    def UpdateToFace(self, ) -> None: ...

class FaceWall(HostObject):
    """.NET: Autodesk.Revit.DB.FaceWall"""
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
    def Create(document: Document, wallType: ElementId, locationLine: WallLocationLine, faceReference: Reference) -> FaceWall: ...
    @staticmethod
    def IsValidFaceReferenceForFaceWall(document: Document, faceReference: Reference) -> bool: ...
    @staticmethod
    def IsWallTypeValidForFaceWall(document: Document, wallType: ElementId) -> bool: ...

class FacetingUtils:
    """.NET: Autodesk.Revit.DB.FacetingUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def ConvertTrianglesToQuads(triangulation: TriangulationInterface) -> IList: ...

class FailureDefinition:
    """.NET: Autodesk.Revit.DB.FailureDefinition"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Severity: FailureSeverity
    def AddResolutionType(self, type: FailureResolutionType, caption: str, classOfResolution: Type) -> FailureDefinition: ...
    @staticmethod
    def CreateFailureDefinition(id: FailureDefinitionId, severity: FailureSeverity, messageString: str) -> FailureDefinition: ...
    def Dispose(self, ) -> None: ...
    def GetApplicableResolutionTypes(self, ) -> IList: ...
    def GetDefaultResolutionType(self, ) -> FailureResolutionType: ...
    def GetDescriptionText(self, ) -> str: ...
    def GetResolutionCaption(self, type: FailureResolutionType) -> str: ...
    def HasResolutions(self, ) -> bool: ...
    def IsResolutionApplicable(self, type: FailureResolutionType) -> bool: ...
    def SetDefaultResolutionType(self, type: FailureResolutionType) -> FailureDefinition: ...

class FailureDefinitionAccessor:
    """.NET: Autodesk.Revit.DB.FailureDefinitionAccessor"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetApplicableResolutionTypes(self, ) -> IList: ...
    def GetDefaultResolutionType(self, ) -> FailureResolutionType: ...
    def GetDescriptionText(self, ) -> str: ...
    def GetId(self, ) -> FailureDefinitionId: ...
    def GetResolutionCaption(self, type: FailureResolutionType) -> str: ...
    def GetSeverity(self, ) -> FailureSeverity: ...
    def HasResolutions(self, ) -> bool: ...
    def IsResolutionApplicable(self, type: FailureResolutionType) -> bool: ...
    def SetDefaultResolutionType(self, type: FailureResolutionType) -> None: ...

class FailureDefinitionId(GuidEnum):
    """.NET: Autodesk.Revit.DB.FailureDefinitionId"""
    def __init__(self, *args) -> None: ...
    Guid: Guid

class FailureDefinitionRegistry:
    """.NET: Autodesk.Revit.DB.FailureDefinitionRegistry"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def FindFailureDefinition(self, id: FailureDefinitionId) -> FailureDefinitionAccessor: ...
    def ListAllFailureDefinitions(self, ) -> IList: ...

class FailureHandlingOptions:
    """.NET: Autodesk.Revit.DB.FailureHandlingOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetClearAfterRollback(self, ) -> bool: ...
    def GetDelayedMiniWarnings(self, ) -> bool: ...
    def GetFailuresPreprocessor(self, ) -> IFailuresPreprocessor: ...
    def GetForcedModalHandling(self, ) -> bool: ...
    def GetTransactionFinalizer(self, ) -> ITransactionFinalizer: ...
    def SetClearAfterRollback(self, bFlag: bool) -> FailureHandlingOptions: ...
    def SetDelayedMiniWarnings(self, bFlag: bool) -> FailureHandlingOptions: ...
    def SetFailuresPreprocessor(self, preprocessor: IFailuresPreprocessor) -> FailureHandlingOptions: ...
    def SetForcedModalHandling(self, bFlag: bool) -> FailureHandlingOptions: ...
    def SetTransactionFinalizer(self, finalizer: ITransactionFinalizer) -> FailureHandlingOptions: ...

class FailureMessage:
    """.NET: Autodesk.Revit.DB.FailureMessage"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def AddResolution(self, type: FailureResolutionType, resolution: FailureResolution) -> FailureMessage: ...
    def Dispose(self, ) -> None: ...
    def GetAdditionalElements(self, ) -> ICollection: ...
    def GetDefaultResolutionCaption(self, ) -> str: ...
    def GetDescriptionText(self, ) -> str: ...
    def GetFailingElements(self, ) -> ICollection: ...
    def GetFailureDefinitionId(self, ) -> FailureDefinitionId: ...
    def GetSeverity(self, ) -> FailureSeverity: ...
    def HasResolutionOfType(self, type: FailureResolutionType) -> bool: ...
    def HasResolutions(self, ) -> bool: ...
    def SetAdditionalElement(self, additionalElement: ElementId) -> FailureMessage: ...
    def SetAdditionalElements(self, additionalElements: ICollection) -> FailureMessage: ...
    def SetFailingElement(self, id: ElementId) -> FailureMessage: ...
    def SetFailingElements(self, idsToShow: ICollection) -> FailureMessage: ...

class FailureMessageAccessor:
    """.NET: Autodesk.Revit.DB.FailureMessageAccessor"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def CloneFailureMessage(self, ) -> FailureMessage: ...
    def Dispose(self, ) -> None: ...
    def GetAdditionalElementIds(self, ) -> ICollection: ...
    def GetCurrentResolutionType(self, ) -> FailureResolutionType: ...
    def GetDefaultResolutionCaption(self, ) -> str: ...
    def GetDescriptionText(self, ) -> str: ...
    def GetFailingElementIds(self, ) -> ICollection: ...
    def GetFailureDefinitionId(self, ) -> FailureDefinitionId: ...
    def GetNumberOfResolutions(self, ) -> int: ...
    def GetSeverity(self, ) -> FailureSeverity: ...
    def HasResolutionOfType(self, type: FailureResolutionType) -> bool: ...
    def HasResolutions(self, ) -> bool: ...
    def SetCurrentResolutionType(self, resolutionType: FailureResolutionType) -> None: ...
    def ShouldMergeWithMessage(self, messageToMergeWith: FailureMessageAccessor) -> bool: ...

class FailureMessageKey:
    """.NET: Autodesk.Revit.DB.FailureMessageKey"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def IsEqual(self, other: FailureMessageKey) -> bool: ...
    def IsValid(self, ) -> bool: ...

class FailureProcessingResult:
    """.NET: Autodesk.Revit.DB.FailureProcessingResult"""
    def __init__(self, *args) -> None: ...
    ...

class FailureResolution:
    """.NET: Autodesk.Revit.DB.FailureResolution"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class FailureResolutionType:
    """.NET: Autodesk.Revit.DB.FailureResolutionType"""
    def __init__(self, *args) -> None: ...
    ...

class FailureSeverity:
    """.NET: Autodesk.Revit.DB.FailureSeverity"""
    def __init__(self, *args) -> None: ...
    ...

class FailuresAccessor:
    """.NET: Autodesk.Revit.DB.FailuresAccessor"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def CanCommitPendingTransaction(self, ) -> bool: ...
    def CanRollBackPendingTransaction(self, ) -> bool: ...
    def CommitPendingTransaction(self, ) -> TransactionStatus: ...
    def DeleteAllWarnings(self, ) -> None: ...
    def DeleteElements(self, idsToDelete: IList) -> None: ...
    def DeleteWarning(self, failure: FailureMessageAccessor) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetAttemptedResolutionTypes(self, failure: FailureMessageAccessor) -> IList: ...
    def GetDocument(self, ) -> Document: ...
    def GetFailureHandlingOptions(self, ) -> FailureHandlingOptions: ...
    def GetFailureMessages(self, severity: FailureSeverity) -> IList: ...
    def GetSeverity(self, ) -> FailureSeverity: ...
    def GetTransactionName(self, ) -> str: ...
    def IsActive(self, ) -> bool: ...
    def IsElementsDeletionPermitted(self, idsToDelete: IList, reason: str) -> bool: ...
    def IsFailureResolutionPermitted(self, failure: FailureMessageAccessor, resolutionType: FailureResolutionType) -> bool: ...
    def IsPending(self, ) -> bool: ...
    def IsTransactionBeingCommitted(self, ) -> bool: ...
    def JournalFailures(self, failures: IList) -> None: ...
    def PostFailure(self, failure: FailureMessage) -> None: ...
    def ReplaceFailures(self, failure: FailureMessage) -> None: ...
    def ResolveFailure(self, failure: FailureMessageAccessor) -> None: ...
    def ResolveFailures(self, failures: IList) -> None: ...
    def RollBackPendingTransaction(self, ) -> TransactionStatus: ...
    def SetFailureHandlingOptions(self, options: FailureHandlingOptions) -> None: ...
    def SetTransactionName(self, transactionName: str) -> None: ...

class Family(Element):
    """.NET: Autodesk.Revit.DB.Family"""
    def __init__(self, *args) -> None: ...
    IsParametric: bool
    IsUserCreated: bool
    FamilyPlacementType: FamilyPlacementType
    IsOwnerFamily: bool
    FamilyCategoryId: ElementId
    StructuralCodeName: str
    StructuralFamilyNameKey: str
    StructuralSectionShape: StructuralSectionShape
    StructuralMaterialType: StructuralMaterialType
    IsEditable: bool
    IsInPlace: bool
    FamilyCategory: Category
    ShowSpatialElementCalculationPoint: bool
    CurtainPanelVerticalSpacing: float
    CurtainPanelHorizontalSpacing: float
    CurtainPanelTilePattern: TilePatternsBuiltIn
    IsCurtainPanelFamily: bool
    IsConceptualMassFamily: bool
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
    def CanHaveStructuralSection(self, ) -> bool: ...
    @staticmethod
    def CanLoadFamilies(document: Document) -> bool: ...
    def ExtractPartAtom(self, xmlFilePath: str) -> None: ...
    def GetFamilySymbolIds(self, ) -> ISet: ...
    def GetFamilyTypeParameterValues(self, parameterId: ElementId) -> ISet: ...
    def HasLargeSketches(self, ) -> bool: ...
    def IsAppropriateCategoryId(self, categoryId: ElementId) -> bool: ...

class FamilyElementVisibility(APIObject):
    """.NET: Autodesk.Revit.DB.FamilyElementVisibility"""
    def __init__(self, *args) -> None: ...
    IsShownInFine: bool
    IsShownInMedium: bool
    IsShownInCoarse: bool
    IsShownInLeftRight: bool
    IsShownInFrontBack: bool
    IsShownInTopBottom: bool
    IsShownInPlanRCPCut: bool
    IsShownOnlyWhenCut: bool
    VisibilityType: FamilyElementVisibilityType
    IsReadOnly: bool

class FamilyElementVisibilityType:
    """.NET: Autodesk.Revit.DB.FamilyElementVisibilityType"""
    def __init__(self, *args) -> None: ...
    ...

class FamilyHostingBehavior:
    """.NET: Autodesk.Revit.DB.FamilyHostingBehavior"""
    def __init__(self, *args) -> None: ...
    ...

class FamilyInstance(Instance):
    """.NET: Autodesk.Revit.DB.FamilyInstance"""
    def __init__(self, *args) -> None: ...
    HasSpatialElementFromToCalculationPoints: bool
    HasSpatialElementCalculationPoint: bool
    IsWorkPlaneFlipped: bool
    CanFlipWorkPlane: bool
    IsSlantedColumn: bool
    ExtensionUtility: IExtension
    SuperComponent: Element
    ToRoom: Room
    ToRoom: Room
    FromRoom: Room
    FromRoom: Room
    CanSplit: bool
    CanRotate: bool
    CanFlipFacing: bool
    CanFlipHand: bool
    Mirrored: bool
    Invisible: bool
    FacingFlipped: bool
    HandFlipped: bool
    FacingOrientation: XYZ
    HandOrientation: XYZ
    HostFace: Reference
    HostParameter: float
    Host: Element
    Location: Location
    Space: Space
    Space: Space
    Room: Room
    Room: Room
    StructuralType: StructuralType
    StructuralUsage: StructuralInstanceUsage
    StructuralMaterialId: ElementId
    StructuralMaterialType: StructuralMaterialType
    MEPModel: MEPModel
    Symbol: FamilySymbol
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
    def AddCoping(self, cutter: FamilyInstance) -> bool: ...
    def FlipFromToRoom(self, ) -> None: ...
    def GetCopingIds(self, ) -> ICollection: ...
    def GetFamilyPointPlacementReferences(self, ) -> IList: ...
    def GetOriginalGeometry(self, options: Options) -> GeometryElement: ...
    def GetReferenceByName(self, name: str) -> Reference: ...
    def GetReferenceName(self, reference: Reference) -> str: ...
    def GetReferenceType(self, reference: Reference) -> FamilyInstanceReferenceType: ...
    def GetReferences(self, referenceType: FamilyInstanceReferenceType) -> IList: ...
    def GetSpatialElementCalculationPoint(self, ) -> XYZ: ...
    def GetSpatialElementFromToCalculationPoints(self, ) -> IList: ...
    def GetSubComponentIds(self, ) -> ICollection: ...
    def GetSweptProfile(self, ) -> SweptProfile: ...
    def HasModifiedGeometry(self, ) -> bool: ...
    def HasSweptProfile(self, ) -> bool: ...
    def RemoveCoping(self, cutter: FamilyInstance) -> bool: ...
    def SetCopingIds(self, cutters: ICollection) -> bool: ...
    def Split(self, param: float) -> ElementId: ...
    def flipFacing(self, ) -> bool: ...
    def flipHand(self, ) -> bool: ...
    def rotate(self, ) -> bool: ...

class FamilyInstanceFilter(ElementSlowFilter):
    """.NET: Autodesk.Revit.DB.FamilyInstanceFilter"""
    def __init__(self, *args) -> None: ...
    FamilySymbolId: ElementId
    IsValidObject: bool
    Inverted: bool

class FamilyInstanceReferenceType:
    """.NET: Autodesk.Revit.DB.FamilyInstanceReferenceType"""
    def __init__(self, *args) -> None: ...
    ...

class FamilyManager(APIObject):
    """.NET: Autodesk.Revit.DB.FamilyManager"""
    def __init__(self, *args) -> None: ...
    Parameter: FamilyParameter
    Parameter: FamilyParameter
    Parameter: FamilyParameter
    Parameter: FamilyParameter
    Parameters: FamilyParameterSet
    Types: FamilyTypeSet
    CurrentType: FamilyType
    IsReadOnly: bool
    def AddParameter(self, parameterName: str, groupTypeId: ForgeTypeId, familyCategory: Category, isInstance: bool) -> FamilyParameter: ...
    def AssociateElementParameterToFamilyParameter(self, elementParameter: Parameter, familyParameter: FamilyParameter) -> None: ...
    def CanElementParameterBeAssociated(self, elementParameter: Parameter) -> bool: ...
    def DeleteCurrentType(self, ) -> None: ...
    def GetAssociatedFamilyParameter(self, elementParameter: Parameter) -> FamilyParameter: ...
    def GetParameter(self, parameterTypeId: ForgeTypeId) -> FamilyParameter: ...
    def GetParameters(self, ) -> IList: ...
    def IsParameterLockable(self, familyParameter: FamilyParameter) -> bool: ...
    def IsParameterLocked(self, familyParameter: FamilyParameter) -> bool: ...
    def IsUserAssignableParameterGroup(self, groupTypeId: ForgeTypeId) -> bool: ...
    def MakeInstance(self, familyParameter: FamilyParameter) -> None: ...
    def MakeNonReporting(self, familyParameter: FamilyParameter) -> None: ...
    def MakeReporting(self, familyParameter: FamilyParameter) -> None: ...
    def MakeType(self, familyParameter: FamilyParameter) -> None: ...
    def NewType(self, typeName: str) -> FamilyType: ...
    def RemoveParameter(self, familyParameter: FamilyParameter) -> None: ...
    def RenameCurrentType(self, typeName: str) -> None: ...
    def RenameParameter(self, familyParameter: FamilyParameter, name: str) -> None: ...
    def ReorderParameters(self, parameters: IList) -> None: ...
    def ReplaceParameter(self, currentParameter: FamilyParameter, parameterName: str, groupTypeId: ForgeTypeId, isInstance: bool) -> FamilyParameter: ...
    def Set(self, familyParameter: FamilyParameter, value: ElementId) -> None: ...
    def SetDescription(self, familyParameter: FamilyParameter, description: str) -> None: ...
    def SetFormula(self, familyParameter: FamilyParameter, formula: str) -> None: ...
    def SetParameterLocked(self, familyParameter: FamilyParameter, locked: bool) -> None: ...
    def SetValueString(self, familyParameter: FamilyParameter, value: str) -> None: ...
    def SortParameters(self, order: ParametersOrder) -> None: ...

class FamilyNestingBehavior:
    """.NET: Autodesk.Revit.DB.FamilyNestingBehavior"""
    def __init__(self, *args) -> None: ...
    ...

class FamilyParameter(APIObject):
    """.NET: Autodesk.Revit.DB.FamilyParameter"""
    def __init__(self, *args) -> None: ...
    UserModifiable: bool
    IsReadOnly: bool
    IsShared: bool
    GUID: Guid
    Id: ElementId
    AssociatedParameters: ParameterSet
    Formula: str
    CanAssignFormula: bool
    IsDeterminedByFormula: bool
    IsReporting: bool
    IsInstance: bool
    StorageType: StorageType
    Definition: Definition
    def GetUnitTypeId(self, ) -> ForgeTypeId: ...

class FamilyParameterSet(APIObject):
    """.NET: Autodesk.Revit.DB.FamilyParameterSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: FamilyParameter) -> bool: ...
    def Erase(self, item: FamilyParameter) -> int: ...
    def ForwardIterator(self, ) -> FamilyParameterSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: FamilyParameter) -> bool: ...
    def ReverseIterator(self, ) -> FamilyParameterSetIterator: ...

class FamilyParameterSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.FamilyParameterSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class FamilyPlacementType:
    """.NET: Autodesk.Revit.DB.FamilyPlacementType"""
    def __init__(self, *args) -> None: ...
    ...

class FamilyPointLocation(APIObject):
    """.NET: Autodesk.Revit.DB.FamilyPointLocation"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Name: str
    IsReadOnly: bool
    def GetLocation(self, ) -> Transform: ...

class FamilyPointPlacementReference(APIObject):
    """.NET: Autodesk.Revit.DB.FamilyPointPlacementReference"""
    def __init__(self, *args) -> None: ...
    PointReference: Reference
    Location: Transform
    Name: str
    IsReadOnly: bool

class FamilySizeTable:
    """.NET: Autodesk.Revit.DB.FamilySizeTable"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    NumberOfColumns: int
    NumberOfRows: int
    def AsValueString(self, row: int, column: int) -> str: ...
    def Dispose(self, ) -> None: ...
    def GetColumnHeader(self, index: int) -> FamilySizeTableColumn: ...
    def IsValidColumnIndex(self, index: int) -> bool: ...

class FamilySizeTableColumn:
    """.NET: Autodesk.Revit.DB.FamilySizeTableColumn"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Name: str
    def Dispose(self, ) -> None: ...
    def GetSpecTypeId(self, ) -> ForgeTypeId: ...
    def GetUnitTypeId(self, ) -> ForgeTypeId: ...

class FamilySizeTableErrorInfo:
    """.NET: Autodesk.Revit.DB.FamilySizeTableErrorInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    InvalidRowIndex: int
    InvalidColumnIndex: int
    InvalidHeaderText: str
    FilePath: str
    FamilySizeTableErrorType: FamilySizeTableErrorType
    def Dispose(self, ) -> None: ...

class FamilySizeTableErrorType:
    """.NET: Autodesk.Revit.DB.FamilySizeTableErrorType"""
    def __init__(self, *args) -> None: ...
    ...

class FamilySizeTableManager:
    """.NET: Autodesk.Revit.DB.FamilySizeTableManager"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    NumberOfSizeTables: int
    @staticmethod
    def CreateFamilySizeTableManager(document: Document, familyId: ElementId) -> bool: ...
    def Dispose(self, ) -> None: ...
    def ExportSizeTable(self, tableName: str, filePath: str) -> bool: ...
    def GetAllSizeTableNames(self, ) -> IList: ...
    @staticmethod
    def GetFamilySizeTableManager(document: Document, familyId: ElementId) -> FamilySizeTableManager: ...
    def GetSizeTable(self, tableName: str) -> FamilySizeTable: ...
    def HasSizeTable(self, tableName: str) -> bool: ...
    def ImportSizeTable(self, document: Document, filePath: str, errorInfo: FamilySizeTableErrorInfo) -> bool: ...
    def RemoveSizeTable(self, tableName: str) -> bool: ...

class FamilySource:
    """.NET: Autodesk.Revit.DB.FamilySource"""
    def __init__(self, *args) -> None: ...
    ...

class FamilySymbol(InsertableObject):
    """.NET: Autodesk.Revit.DB.FamilySymbol"""
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
    def Activate(self, ) -> None: ...
    def CanHaveStructuralSection(self, ) -> bool: ...
    def GetFamilyPointLocations(self, ) -> IList: ...
    def GetStructuralSection(self, ) -> StructuralSection: ...
    def GetThermalProperties(self, ) -> FamilyThermalProperties: ...
    def HasThermalProperties(self, ) -> bool: ...
    def SetStructuralSection(self, structuralSection: StructuralSection) -> None: ...
    def SetThermalProperties(self, thermalProperties: FamilyThermalProperties) -> None: ...

class FamilySymbolFilter(ElementQuickFilter):
    """.NET: Autodesk.Revit.DB.FamilySymbolFilter"""
    def __init__(self, *args) -> None: ...
    FamilyId: ElementId
    IsValidObject: bool
    Inverted: bool

class FamilySymbolProfile(SweepProfile):
    """.NET: Autodesk.Revit.DB.FamilySymbolProfile"""
    def __init__(self, *args) -> None: ...
    IsFlipped: bool
    Angle: float
    YOffset: float
    XOffset: float
    Profile: FamilySymbol
    IsReadOnly: bool

class FamilyThermalProperties:
    """.NET: Autodesk.Revit.DB.FamilyThermalProperties"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    HeatTransferCoefficient: float
    ThermalResistance: float
    AnalyticConstructionName: str
    AnalyticConstructionTypeId: str
    VisualLightTransmittance: float
    SolarHeatGainCoefficient: float
    ThermalTransmittance: float
    def Dispose(self, ) -> None: ...
    @staticmethod
    def Find(pADoc: Document, constructionId: str) -> FamilyThermalProperties: ...
    def IsValid(self, ) -> bool: ...

class FamilyType(APIObject):
    """.NET: Autodesk.Revit.DB.FamilyType"""
    def __init__(self, *args) -> None: ...
    Name: str
    IsReadOnly: bool
    def AsDouble(self, familyParameter: FamilyParameter) -> Nullable: ...
    def AsElementId(self, familyParameter: FamilyParameter) -> ElementId: ...
    def AsInteger(self, familyParameter: FamilyParameter) -> Nullable: ...
    def AsString(self, familyParameter: FamilyParameter) -> str: ...
    def AsValueString(self, familyParameter: FamilyParameter) -> str: ...
    def HasValue(self, familyParameter: FamilyParameter) -> bool: ...

class FamilyTypeSet(APIObject):
    """.NET: Autodesk.Revit.DB.FamilyTypeSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: FamilyType) -> bool: ...
    def Erase(self, item: FamilyType) -> int: ...
    def ForwardIterator(self, ) -> FamilyTypeSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: FamilyType) -> bool: ...
    def ReverseIterator(self, ) -> FamilyTypeSetIterator: ...

class FamilyTypeSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.FamilyTypeSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class FamilyUtils:
    """.NET: Autodesk.Revit.DB.FamilyUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def ConvertFamilyToFaceHostBased(document: Document, familyId: ElementId) -> None: ...
    @staticmethod
    def FamilyCanConvertToFaceHostBased(document: Document, familyId: ElementId) -> bool: ...
    @staticmethod
    def GetProfileSymbols(document: Document, profileFamilyUsage: ProfileFamilyUsage, oneCurveLoopOnly: bool) -> ICollection: ...

class FilePath(ModelPath):
    """.NET: Autodesk.Revit.DB.FilePath"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Region: str
    CloudPath: bool
    ServerPath: bool
    Empty: bool
    CentralServerPath: str

class FillGrid:
    """.NET: Autodesk.Revit.DB.FillGrid"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Shift: float
    Offset: float
    Origin: UV
    Angle: float
    def CalculateLengthPerArea(self, ) -> float: ...
    def CalculateLinesPerLength(self, ) -> float: ...
    def CalculateStrokesPerArea(self, ) -> float: ...
    def Dispose(self, ) -> None: ...
    def GetHatchingDirection(self, ) -> UV: ...
    def GetPointLineZone(self, point: UV, nearestPoint: UV) -> int: ...
    def GetSegmentDirection(self, ) -> UV: ...
    def GetSegments(self, ) -> IList: ...
    def IsEqual(self, other: FillGrid) -> bool: ...
    def SetSegments(self, segArr: IList) -> None: ...

class FillPattern:
    """.NET: Autodesk.Revit.DB.FillPattern"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Name: str
    LinesPerLength: float
    StrokesPerArea: float
    LengthPerArea: float
    IsSolidFill: bool
    GridCount: int
    Target: FillPatternTarget
    HostOrientation: FillPatternHostOrientation
    def Dispose(self, ) -> None: ...
    def ExpandDots(self, ) -> bool: ...
    @staticmethod
    def ExportToPAT(fillPatterns: IList, filename: str) -> bool: ...
    def GetFillGrid(self, gridIdx: int) -> FillGrid: ...
    def GetFillGrids(self, ) -> IList: ...
    def IsEqual(self, other: FillPattern) -> bool: ...
    def SetFillGrid(self, gridIdx: int, fillGrid: FillGrid) -> None: ...
    def SetFillGrids(self, fillGrids: IList) -> None: ...

class FillPatternElement(Element):
    """.NET: Autodesk.Revit.DB.FillPatternElement"""
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
    def Create(document: Document, fillPattern: FillPattern) -> FillPatternElement: ...
    def GetFillPattern(self, ) -> FillPattern: ...
    @staticmethod
    def GetFillPatternElementByName(document: Document, target: FillPatternTarget, name: str) -> FillPatternElement: ...
    def SetFillPattern(self, newFillPattern: FillPattern) -> None: ...

class FillPatternHostOrientation:
    """.NET: Autodesk.Revit.DB.FillPatternHostOrientation"""
    def __init__(self, *args) -> None: ...
    ...

class FillPatternTarget:
    """.NET: Autodesk.Revit.DB.FillPatternTarget"""
    def __init__(self, *args) -> None: ...
    ...

class FilledRegion(Element):
    """.NET: Autodesk.Revit.DB.FilledRegion"""
    def __init__(self, *args) -> None: ...
    IsMasking: bool
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
    def Create(document: Document, typeId: ElementId, sketchPlane: SketchPlane, boundaries: IList) -> FilledRegion: ...
    @staticmethod
    def CreateMaskingRegion(document: Document, sketchPlane: SketchPlane, boundaries: IList) -> FilledRegion: ...
    def GetBoundaries(self, ) -> IList: ...
    @staticmethod
    def GetValidLineStyleIdsForFilledRegion(document: Document) -> IList: ...
    @staticmethod
    def IsValidFilledRegionTypeId(document: Document, typeId: ElementId) -> bool: ...
    @staticmethod
    def IsValidLineStyleIdForFilledRegion(document: Document, lineStyleId: ElementId) -> bool: ...
    def SetLineStyleId(self, lineStyleId: ElementId) -> None: ...

class FilledRegionType(LineAndTextAttrSymbol):
    """.NET: Autodesk.Revit.DB.FilledRegionType"""
    def __init__(self, *args) -> None: ...
    BackgroundPatternColor: Color
    ForegroundPatternColor: Color
    LineWeight: int
    IsMasking: bool
    BackgroundPatternId: ElementId
    ForegroundPatternId: ElementId
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
    def IsValidBackgroundPatternId(self, patternId: ElementId) -> bool: ...
    def IsValidFillPatternId(self, patternId: ElementId) -> bool: ...
    def IsValidForegroundPatternId(self, patternId: ElementId) -> bool: ...
    @staticmethod
    def IsValidLineWeight(lineWeight: int) -> bool: ...
    def IsValidMasking(self, isMasking: bool) -> bool: ...
    def IsValidSolidFillPatternId(self, patternId: ElementId) -> bool: ...

class FilterCategoryRule(FilterRule):
    """.NET: Autodesk.Revit.DB.FilterCategoryRule"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    @staticmethod
    def AllCategoriesFilterable(categories: ICollection) -> bool: ...
    def GetCategories(self, ) -> ICollection: ...
    def SetCategories(self, categories: ICollection) -> bool: ...

class FilterDoubleRule(FilterNumericValueRule):
    """.NET: Autodesk.Revit.DB.FilterDoubleRule"""
    def __init__(self, *args) -> None: ...
    Epsilon: float
    RuleValue: float
    IsValidObject: bool

class FilterElement(Element):
    """.NET: Autodesk.Revit.DB.FilterElement"""
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
    def IsNameUnique(aDocument: Document, name: str) -> bool: ...

class FilterElementIdRule(FilterNumericValueRule):
    """.NET: Autodesk.Revit.DB.FilterElementIdRule"""
    def __init__(self, *args) -> None: ...
    RuleValue: ElementId
    IsValidObject: bool
    @staticmethod
    def UsesLevelFiltering(doc: Document, parameterId: ElementId) -> bool: ...

class FilterGlobalParameterAssociationRule(FilterNumericValueRule):
    """.NET: Autodesk.Revit.DB.FilterGlobalParameterAssociationRule"""
    def __init__(self, *args) -> None: ...
    RuleValue: ElementId
    IsValidObject: bool

class FilterIntegerRule(FilterNumericValueRule):
    """.NET: Autodesk.Revit.DB.FilterIntegerRule"""
    def __init__(self, *args) -> None: ...
    RuleValue: int
    IsValidObject: bool

class FilterInverseRule(FilterRule):
    """.NET: Autodesk.Revit.DB.FilterInverseRule"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def GetInnerRule(self, ) -> FilterRule: ...
    def SetInnerRule(self, innerRule: FilterRule) -> None: ...

class FilterNumericEquals(FilterNumericRuleEvaluator):
    """.NET: Autodesk.Revit.DB.FilterNumericEquals"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class FilterNumericGreater(FilterNumericRuleEvaluator):
    """.NET: Autodesk.Revit.DB.FilterNumericGreater"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class FilterNumericGreaterOrEqual(FilterNumericRuleEvaluator):
    """.NET: Autodesk.Revit.DB.FilterNumericGreaterOrEqual"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class FilterNumericLess(FilterNumericRuleEvaluator):
    """.NET: Autodesk.Revit.DB.FilterNumericLess"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class FilterNumericLessOrEqual(FilterNumericRuleEvaluator):
    """.NET: Autodesk.Revit.DB.FilterNumericLessOrEqual"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class FilterNumericRuleEvaluator:
    """.NET: Autodesk.Revit.DB.FilterNumericRuleEvaluator"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def Evaluate(self, lhs: float, rhs: float, epsilon: float) -> bool: ...

class FilterNumericValueRule(FilterValueRule):
    """.NET: Autodesk.Revit.DB.FilterNumericValueRule"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def GetEvaluator(self, ) -> FilterNumericRuleEvaluator: ...
    def SetEvaluator(self, evaluator: FilterNumericRuleEvaluator) -> None: ...

class FilterOperatorAndTextString:
    """.NET: Autodesk.Revit.DB.FilterOperatorAndTextString"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    FilterOperatorStr: str
    OperatorType: ScheduleFilterType
    def Dispose(self, ) -> None: ...

class FilterRule:
    """.NET: Autodesk.Revit.DB.FilterRule"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def ElementPasses(self, element: Element) -> bool: ...
    def GetRuleParameter(self, ) -> ElementId: ...

class FilterStringBeginsWith(FilterStringRuleEvaluator):
    """.NET: Autodesk.Revit.DB.FilterStringBeginsWith"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class FilterStringContains(FilterStringRuleEvaluator):
    """.NET: Autodesk.Revit.DB.FilterStringContains"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class FilterStringEndsWith(FilterStringRuleEvaluator):
    """.NET: Autodesk.Revit.DB.FilterStringEndsWith"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class FilterStringEquals(FilterStringRuleEvaluator):
    """.NET: Autodesk.Revit.DB.FilterStringEquals"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class FilterStringGreater(FilterStringRuleEvaluator):
    """.NET: Autodesk.Revit.DB.FilterStringGreater"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class FilterStringGreaterOrEqual(FilterStringRuleEvaluator):
    """.NET: Autodesk.Revit.DB.FilterStringGreaterOrEqual"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class FilterStringLess(FilterStringRuleEvaluator):
    """.NET: Autodesk.Revit.DB.FilterStringLess"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class FilterStringLessOrEqual(FilterStringRuleEvaluator):
    """.NET: Autodesk.Revit.DB.FilterStringLessOrEqual"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class FilterStringRule(FilterValueRule):
    """.NET: Autodesk.Revit.DB.FilterStringRule"""
    def __init__(self, *args) -> None: ...
    RuleString: str
    IsValidObject: bool
    def GetEvaluator(self, ) -> FilterStringRuleEvaluator: ...
    def SetEvaluator(self, evaluator: FilterStringRuleEvaluator) -> None: ...

class FilterStringRuleEvaluator:
    """.NET: Autodesk.Revit.DB.FilterStringRuleEvaluator"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def Evaluate(self, lhs: str, rhs: str, caseSensitive: bool) -> bool: ...

class FilterValueRule(FilterRule):
    """.NET: Autodesk.Revit.DB.FilterValueRule"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class FilterableValueProvider:
    """.NET: Autodesk.Revit.DB.FilterableValueProvider"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetAssociatedGlobalParameterValue(self, element: Element) -> ElementId: ...
    def GetDoubleValue(self, element: Element) -> float: ...
    def GetElementIdValue(self, element: Element) -> ElementId: ...
    def GetIntegerValue(self, element: Element) -> int: ...
    def GetStringValue(self, element: Element) -> str: ...
    def IsDoubleValueSupported(self, element: Element) -> bool: ...
    def IsElementIdValueSupported(self, element: Element) -> bool: ...
    def IsIntegerValueSupported(self, element: Element) -> bool: ...
    def IsStringValueSupported(self, element: Element) -> bool: ...

class FilteredElementCollector:
    """.NET: Autodesk.Revit.DB.FilteredElementCollector"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def ContainedInDesignOption(self, designOptionId: ElementId) -> FilteredElementCollector: ...
    def Dispose(self, ) -> None: ...
    def Excluding(self, idsToExclude: ICollection) -> FilteredElementCollector: ...
    def FirstElement(self, ) -> Element: ...
    def FirstElementId(self, ) -> ElementId: ...
    def GetElementCount(self, ) -> int: ...
    def GetElementIdIterator(self, ) -> FilteredElementIdIterator: ...
    def GetElementIterator(self, ) -> FilteredElementIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IntersectWith(self, other: FilteredElementCollector) -> FilteredElementCollector: ...
    @staticmethod
    def IsViewValidForElementIteration(document: Document, viewId: ElementId) -> bool: ...
    def OfCategory(self, category: BuiltInCategory) -> FilteredElementCollector: ...
    def OfCategoryId(self, categoryId: ElementId) -> FilteredElementCollector: ...
    def OfClass(self, type: Type) -> FilteredElementCollector: ...
    def OwnedByView(self, viewId: ElementId) -> FilteredElementCollector: ...
    def ToElementIds(self, ) -> ICollection: ...
    def ToElements(self, ) -> IList: ...
    def UnionWith(self, other: FilteredElementCollector) -> FilteredElementCollector: ...
    def WhereElementIsCurveDriven(self, ) -> FilteredElementCollector: ...
    def WhereElementIsElementType(self, ) -> FilteredElementCollector: ...
    def WhereElementIsNotElementType(self, ) -> FilteredElementCollector: ...
    def WhereElementIsViewIndependent(self, ) -> FilteredElementCollector: ...
    def WherePasses(self, filter: ElementFilter) -> FilteredElementCollector: ...

class FilteredElementIdIterator:
    """.NET: Autodesk.Revit.DB.FilteredElementIdIterator"""
    def __init__(self, *args) -> None: ...
    Current: ElementId
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetCurrent(self, ) -> ElementId: ...
    def IsDone(self, ) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class FilteredElementIterator:
    """.NET: Autodesk.Revit.DB.FilteredElementIterator"""
    def __init__(self, *args) -> None: ...
    Current: Element
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetCurrent(self, ) -> Element: ...
    def IsDone(self, ) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class FilteredWorksetCollector:
    """.NET: Autodesk.Revit.DB.FilteredWorksetCollector"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def FirstWorkset(self, ) -> Workset: ...
    def FirstWorksetId(self, ) -> WorksetId: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetWorksetIdIterator(self, ) -> FilteredWorksetIdIterator: ...
    def GetWorksetIterator(self, ) -> FilteredWorksetIterator: ...
    def OfKind(self, worksetKind: WorksetKind) -> FilteredWorksetCollector: ...
    def ToWorksetIds(self, ) -> ICollection: ...
    def ToWorksets(self, ) -> IList: ...
    def WherePasses(self, filter: WorksetFilter) -> FilteredWorksetCollector: ...

class FilteredWorksetIdIterator:
    """.NET: Autodesk.Revit.DB.FilteredWorksetIdIterator"""
    def __init__(self, *args) -> None: ...
    Current: WorksetId
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetCurrent(self, ) -> WorksetId: ...
    def IsDone(self, ) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class FilteredWorksetIterator:
    """.NET: Autodesk.Revit.DB.FilteredWorksetIterator"""
    def __init__(self, *args) -> None: ...
    Current: Workset
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetCurrent(self, ) -> Workset: ...
    def IsDone(self, ) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class FindReferenceTarget:
    """.NET: Autodesk.Revit.DB.FindReferenceTarget"""
    def __init__(self, *args) -> None: ...
    ...

class FirstNumberFormattingOptions:
    """.NET: Autodesk.Revit.DB.FirstNumberFormattingOptions"""
    def __init__(self, *args) -> None: ...
    ...

class FitDirectionType:
    """.NET: Autodesk.Revit.DB.FitDirectionType"""
    def __init__(self, *args) -> None: ...
    ...

class FittingAndAccessoryCalculationType:
    """.NET: Autodesk.Revit.DB.FittingAndAccessoryCalculationType"""
    def __init__(self, *args) -> None: ...
    ...

class FittingAngleUsage:
    """.NET: Autodesk.Revit.DB.FittingAngleUsage"""
    def __init__(self, *args) -> None: ...
    ...

class Floor(CeilingAndFloor):
    """.NET: Autodesk.Revit.DB.Floor"""
    def __init__(self, *args) -> None: ...
    SketchId: ElementId
    SpanDirectionAngle: float
    FloorType: FloorType
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
    def Create(document: Document, profile: IList, floorTypeId: ElementId, levelId: ElementId, isStructural: bool, slopeArrow: Line, slope: float) -> Floor: ...
    @staticmethod
    def GetDefaultFloorType(document: Document, isFoundation: bool) -> ElementId: ...
    def GetNormalAtVerticalProjectionPoint(self, modelLocation: XYZ, floorFace: FloorFace) -> XYZ: ...
    def GetSlabShapeEditor(self, ) -> SlabShapeEditor: ...
    def GetSpanDirectionSymbolIds(self, ) -> ICollection: ...
    def GetVerticalProjectionPoint(self, modelLocation: XYZ, floorFace: FloorFace) -> XYZ: ...

class FloorFace:
    """.NET: Autodesk.Revit.DB.FloorFace"""
    def __init__(self, *args) -> None: ...
    ...

class FloorType(HostObjAttributes):
    """.NET: Autodesk.Revit.DB.FloorType"""
    def __init__(self, *args) -> None: ...
    ThermalProperties: ThermalProperties
    StructuralMaterialId: ElementId
    IsFoundationSlab: bool
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

class FlowDirectionType:
    """.NET: Autodesk.Revit.DB.FlowDirectionType"""
    def __init__(self, *args) -> None: ...
    ...

class FolderItemInfo:
    """.NET: Autodesk.Revit.DB.FolderItemInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ElementId: ElementId
    Name: str
    def Dispose(self, ) -> None: ...
    def GetGroupingParameterIdPath(self, ) -> IList: ...

class FootPrintRoof(RoofBase):
    """.NET: Autodesk.Revit.DB.FootPrintRoof"""
    def __init__(self, *args) -> None: ...
    CurtainGrids: CurtainGridSet
    Overhang: float
    ExtendIntoWall: bool
    Offset: float
    SlopeAngle: float
    DefinesSlope: bool
    FasciaDepth: float
    EaveCuts: EaveCutterType
    RoofType: RoofType
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
    def GetProfiles(self, ) -> ModelCurveArrArray: ...

class ForgeTypeId:
    """.NET: Autodesk.Revit.DB.ForgeTypeId"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    TypeId: str
    def Clear(self, ) -> ForgeTypeId: ...
    def Dispose(self, ) -> None: ...
    def Empty(self, ) -> bool: ...
    def Equals(self, other: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def NameEquals(self, other: ForgeTypeId) -> bool: ...
    def StrictlyEquals(self, other: ForgeTypeId) -> bool: ...

class Form(GenericForm):
    """.NET: Autodesk.Revit.DB.Form"""
    def __init__(self, *args) -> None: ...
    BaseOffset: float
    TopOffset: float
    HasOpenGeometry: bool
    AreProfilesConstrained: bool
    IsInXRayMode: bool
    HasOneOrMoreReferenceProfiles: bool
    PathCurveReference: Reference
    PathCurveCount: int
    CurveLoopReferencesOnProfile: ReferenceArray
    ProfileCurveLoopCount: int
    ProfileCount: int
    Subcategory: Category
    Name: str
    IsSolid: bool
    Visible: bool
    Combinations: GeomCombinationSet
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
    def AddEdge(self, startEdgeReference: Reference, startParam: float, endEdgeReference: Reference, endParam: float) -> None: ...
    def AddProfile(self, edgeReference: Reference, param: float) -> int: ...
    def CanManipulateProfile(self, profileIndex: int) -> bool: ...
    def CanManipulateSubElement(self, subElementReference: Reference) -> bool: ...
    def ConstrainProfiles(self, primaryProfileIndex: int) -> None: ...
    def DeleteProfile(self, profileIndex: int) -> None: ...
    def DeleteSubElement(self, subElementReference: Reference) -> None: ...
    def GetControlPoints(self, curveOrEdgeOrFaceReference: Reference) -> ReferenceArray: ...
    def GetCurvesAndEdgesReference(self, pointReference: Reference) -> ReferenceArray: ...
    def GetPathCurveIndexByCurveReference(self, curveReference: Reference) -> int: ...
    def GetProfileAndCurveLoopIndexFromReference(self, curveOrEdgeReference: Reference, profileIndex: int, curveLoopIndex: int) -> None: ...
    def IsAutoCreaseEdge(self, edgeReference: Reference) -> bool: ...
    def IsBeginningFace(self, faceReference: Reference) -> bool: ...
    def IsConnectingEdge(self, edgeReference: Reference) -> bool: ...
    def IsCurveReference(self, curveReference: Reference) -> bool: ...
    def IsEdgeReference(self, edgeReference: Reference) -> bool: ...
    def IsEndFace(self, faceReference: Reference) -> bool: ...
    def IsFaceReference(self, faceReference: Reference) -> bool: ...
    def IsProfileEdge(self, curveOrEdgeReference: Reference) -> bool: ...
    def IsReferenceOnlyProfile(self, profileIndex: int) -> bool: ...
    def IsSideFace(self, faceReference: Reference) -> bool: ...
    def IsVertexReference(self, vertexReference: Reference) -> bool: ...
    def MoveProfile(self, profileIndex: int, offset: XYZ) -> None: ...
    def MoveSubElement(self, subElementReference: Reference, offset: XYZ) -> None: ...
    def Rehost(self, sketchPlane: SketchPlane, location: XYZ) -> None: ...
    def RotateProfile(self, profileIndex: int, axis: Line, angle: float) -> None: ...
    def RotateSubElement(self, subElementReference: Reference, axis: Line, angle: float) -> None: ...
    def ScaleProfile(self, profileIndex: int, factor: float, origin: XYZ) -> None: ...
    def ScaleSubElement(self, subElementReference: Reference, factor: float, origin: XYZ) -> None: ...

class FormArray(APIObject):
    """.NET: Autodesk.Revit.DB.FormArray"""
    def __init__(self, *args) -> None: ...
    Item: Form
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: Form) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> FormArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: Form, index: int) -> None: ...
    def ReverseIterator(self, ) -> FormArrayIterator: ...

class FormArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.FormArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class FormUtils:
    """.NET: Autodesk.Revit.DB.FormUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CanBeDissolved(ADoc: Document, elements: ICollection) -> bool: ...
    @staticmethod
    def DissolveForms(ADoc: Document, elements: ICollection, ProfileOriginPointSet: ICollection) -> ICollection: ...

class FormatOptions:
    """.NET: Autodesk.Revit.DB.FormatOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    RoundingMethod: RoundingMethod
    UseDigitGrouping: bool
    UsePlusPrefix: bool
    SuppressSpaces: bool
    SuppressLeadingZeros: bool
    SuppressTrailingZeros: bool
    Accuracy: float
    UseDefault: bool
    @staticmethod
    def CanHaveSymbol(unitTypeId: ForgeTypeId) -> bool: ...
    @staticmethod
    def CanSuppressLeadingZeros(unitTypeId: ForgeTypeId) -> bool: ...
    @staticmethod
    def CanSuppressSpaces(unitTypeId: ForgeTypeId) -> bool: ...
    @staticmethod
    def CanSuppressTrailingZeros(unitTypeId: ForgeTypeId) -> bool: ...
    @staticmethod
    def CanUsePlusPrefix(unitTypeId: ForgeTypeId) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetSymbolTypeId(self, ) -> ForgeTypeId: ...
    def GetUnitTypeId(self, ) -> ForgeTypeId: ...
    @staticmethod
    def GetValidSymbols(unitTypeId: ForgeTypeId) -> IList: ...
    @staticmethod
    def IsValidAccuracy(unitTypeId: ForgeTypeId, accuracy: float) -> bool: ...
    def IsValidForSpec(self, specTypeId: ForgeTypeId) -> bool: ...
    @staticmethod
    def IsValidSymbol(unitTypeId: ForgeTypeId, symbolTypeId: ForgeTypeId) -> bool: ...
    def SetSymbolTypeId(self, symbolTypeId: ForgeTypeId) -> None: ...
    def SetUnitTypeId(self, unitTypeId: ForgeTypeId) -> FormatOptions: ...

class FormatStatus:
    """.NET: Autodesk.Revit.DB.FormatStatus"""
    def __init__(self, *args) -> None: ...
    ...

class FormatValueOptions:
    """.NET: Autodesk.Revit.DB.FormatValueOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    AppendUnitSymbol: bool
    def Dispose(self, ) -> None: ...
    def GetFormatOptions(self, ) -> FormatOptions: ...
    def SetFormatOptions(self, formatOptions: FormatOptions) -> None: ...

class FormattedText:
    """.NET: Autodesk.Revit.DB.FormattedText"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def AsTextRange(self, ) -> TextRange: ...
    def Dispose(self, ) -> None: ...
    def Find(self, searchString: str, startIndex: int, matchCase: bool, matchWholeWord: bool) -> TextRange: ...
    def GetAllCapsStatus(self, textRange: TextRange) -> FormatStatus: ...
    def GetBoldStatus(self, textRange: TextRange) -> FormatStatus: ...
    def GetIndentLevel(self, textRange: TextRange) -> int: ...
    def GetItalicStatus(self, textRange: TextRange) -> FormatStatus: ...
    def GetListStartNumber(self, textRange: TextRange) -> int: ...
    def GetListType(self, textRange: TextRange) -> ListType: ...
    def GetMaximumIndentLevel(self, ) -> int: ...
    def GetMaximumListStartNumber(self, ) -> int: ...
    def GetMinimumListStartNumber(self, ) -> int: ...
    def GetPlainText(self, textRange: TextRange) -> str: ...
    def GetSubscriptStatus(self, textRange: TextRange) -> FormatStatus: ...
    def GetSuperscriptStatus(self, textRange: TextRange) -> FormatStatus: ...
    def GetUnderlineStatus(self, textRange: TextRange) -> FormatStatus: ...
    def SetAllCapsStatus(self, textRange: TextRange, isAllCaps: bool) -> None: ...
    def SetBoldStatus(self, textRange: TextRange, isBold: bool) -> None: ...
    def SetIndentLevel(self, textRange: TextRange, level: int) -> None: ...
    def SetItalicStatus(self, textRange: TextRange, isItalic: bool) -> None: ...
    def SetListStartNumber(self, textRange: TextRange, value: int) -> None: ...
    def SetListType(self, textRange: TextRange, listType: ListType) -> None: ...
    def SetPlainText(self, textRange: TextRange, plainText: str) -> None: ...
    def SetSubscriptStatus(self, textRange: TextRange, isSubscript: bool) -> None: ...
    def SetSuperscriptStatus(self, textRange: TextRange, isSuperscript: bool) -> None: ...
    def SetUnderlineStatus(self, textRange: TextRange, isUnderlined: bool) -> None: ...

class FormulaManager:
    """.NET: Autodesk.Revit.DB.FormulaManager"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    @staticmethod
    def Evaluate(parameterId: ElementId, document: Document, formula: str) -> str: ...
    @staticmethod
    def GetFunctions() -> IList: ...
    @staticmethod
    def GetOperators() -> IList: ...
    @staticmethod
    def Validate(parameterId: ElementId, document: Document, formula: str) -> str: ...

class Frame:
    """.NET: Autodesk.Revit.DB.Frame"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    BasisZ: XYZ
    BasisY: XYZ
    BasisX: XYZ
    Origin: XYZ
    @staticmethod
    def CanDefineRevitGeometry(frameOfReference: Frame) -> bool: ...
    def Dispose(self, ) -> None: ...
    def IsOrthogonal(self, ) -> bool: ...
    def IsOrthonormal(self, ) -> bool: ...
    def IsRightHanded(self, ) -> bool: ...
    def Transform(self, trf: Transform) -> None: ...

class FramingShapeClassification:
    """.NET: Autodesk.Revit.DB.FramingShapeClassification"""
    def __init__(self, *args) -> None: ...
    ...

class FreeFormElement(GenericForm):
    """.NET: Autodesk.Revit.DB.FreeFormElement"""
    def __init__(self, *args) -> None: ...
    Subcategory: Category
    Name: str
    IsSolid: bool
    Visible: bool
    Combinations: GeomCombinationSet
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
    def CanOffsetFace(self, face: Face) -> bool: ...
    @staticmethod
    def Create(document: Document, geometry: Solid) -> FreeFormElement: ...
    def SetFaceOffset(self, face: Face, offset: float) -> None: ...
    def UpdateSolidGeometry(self, newGeometry: Solid) -> None: ...

class GBXMLExportOptions:
    """.NET: Autodesk.Revit.DB.GBXMLExportOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ExportAnalyticalSystems: bool
    def Dispose(self, ) -> None: ...

class GBXMLImportOptions:
    """.NET: Autodesk.Revit.DB.GBXMLImportOptions"""
    def __init__(self, *args) -> None: ...
    ...

class GenericForm(CombinableElement):
    """.NET: Autodesk.Revit.DB.GenericForm"""
    def __init__(self, *args) -> None: ...
    Subcategory: Category
    Name: str
    IsSolid: bool
    Visible: bool
    Combinations: GeomCombinationSet
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
    def GetVisibility(self, ) -> FamilyElementVisibility: ...
    def SetVisibility(self, visibility: FamilyElementVisibility) -> None: ...

class GenericImportOptions:
    """.NET: Autodesk.Revit.DB.GenericImportOptions"""
    def __init__(self, *args) -> None: ...
    RefPoint: XYZ

class GeomCombination(CombinableElement):
    """.NET: Autodesk.Revit.DB.GeomCombination"""
    def __init__(self, *args) -> None: ...
    AllMembers: CombinableElementArray
    Combinations: GeomCombinationSet
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

class GeomCombinationSet(APIObject):
    """.NET: Autodesk.Revit.DB.GeomCombinationSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: GeomCombination) -> bool: ...
    def Erase(self, item: GeomCombination) -> int: ...
    def ForwardIterator(self, ) -> GeomCombinationSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: GeomCombination) -> bool: ...
    def ReverseIterator(self, ) -> GeomCombinationSetIterator: ...

class GeomCombinationSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.GeomCombinationSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class GeometryCreationUtilities:
    """.NET: Autodesk.Revit.DB.GeometryCreationUtilities"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CreateBlendGeometry(firstLoop: CurveLoop, secondLoop: CurveLoop, vertexPairs: ICollection, solidOptions: SolidOptions) -> Solid: ...
    @staticmethod
    def CreateExtrusionGeometry(profileLoops: IList, extrusionDir: XYZ, extrusionDist: float, solidOptions: SolidOptions) -> Solid: ...
    @staticmethod
    def CreateFixedReferenceSweptGeometry(sweepPath: CurveLoop, pathAttachmentCrvIdx: int, pathAttachmentParam: float, profileLoops: IList, fixedReferenceDirection: XYZ, solidOptions: SolidOptions) -> Solid: ...
    @staticmethod
    def CreateLoftGeometry(profileLoops: IList, solidOptions: SolidOptions) -> Solid: ...
    @staticmethod
    def CreateRevolvedGeometry(coordinateFrame: Frame, profileLoops: IList, startAngle: float, endAngle: float, solidOptions: SolidOptions) -> Solid: ...
    @staticmethod
    def CreateSweptBlendGeometry(pathCurve: Curve, pathParams: IList, profileLoops: IList, vertexPairs: IList, solidOptions: SolidOptions) -> Solid: ...
    @staticmethod
    def CreateSweptGeometry(sweepPath: CurveLoop, pathAttachmentCrvIdx: int, pathAttachmentParam: float, profileLoops: IList, solidOptions: SolidOptions) -> Solid: ...

class GeometryElement(GeometryObject):
    """.NET: Autodesk.Revit.DB.GeometryElement"""
    def __init__(self, *args) -> None: ...
    MaterialElement: Material
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool
    def GetBoundingBox(self, ) -> BoundingBoxXYZ: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetTransformed(self, transform: Transform) -> GeometryElement: ...

class GeometryInstance(GeometryObject):
    """.NET: Autodesk.Revit.DB.GeometryInstance"""
    def __init__(self, *args) -> None: ...
    SymbolGeometry: GeometryElement
    Transform: Transform
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool
    def GetDocument(self, ) -> Document: ...
    def GetInstanceGeometry(self, transform: Transform) -> GeometryElement: ...
    def GetSymbolGeometry(self, transform: Transform) -> GeometryElement: ...
    def GetSymbolGeometryId(self, ) -> SymbolGeometryId: ...

class GeometryObject(APIObject):
    """.NET: Autodesk.Revit.DB.GeometryObject"""
    def __init__(self, *args) -> None: ...
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class GlobalParameter(ParameterElement):
    """.NET: Autodesk.Revit.DB.GlobalParameter"""
    def __init__(self, *args) -> None: ...
    IsDrivenByDimension: bool
    IsDrivenByFormula: bool
    IsReporting: bool
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
    def CanChangeReporting(self, ) -> bool: ...
    def CanLabelDimension(self, dimensionId: ElementId) -> bool: ...
    @staticmethod
    def Create(document: Document, name: str, specTypeId: ForgeTypeId) -> GlobalParameter: ...
    def GetAffectedElements(self, ) -> ISet: ...
    def GetAffectedGlobalParameters(self, ) -> ISet: ...
    def GetFormula(self, ) -> str: ...
    def GetLabelName(self, ) -> str: ...
    def GetLabeledDimensions(self, ) -> ISet: ...
    def GetValue(self, ) -> ParameterValue: ...
    def HasValidTypeForReporting(self, ) -> bool: ...
    def IsValidFormula(self, expression: str) -> bool: ...
    def LabelDimension(self, dimensionId: ElementId) -> None: ...
    def SetDrivingDimension(self, dimensionId: ElementId) -> None: ...
    def SetFormula(self, expression: str) -> None: ...
    def SetValue(self, value: ParameterValue) -> None: ...
    def UnlabelDimension(self, dimensionId: ElementId) -> None: ...

class GlobalParametersManager:
    """.NET: Autodesk.Revit.DB.GlobalParametersManager"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    @staticmethod
    def AreGlobalParametersAllowed(document: Document) -> bool: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def FindByName(document: Document, name: str) -> ElementId: ...
    @staticmethod
    def GetAllGlobalParameters(document: Document) -> ISet: ...
    @staticmethod
    def GetGlobalParametersOrdered(document: Document) -> IList: ...
    @staticmethod
    def IsUniqueName(document: Document, name: str) -> bool: ...
    @staticmethod
    def IsValidGlobalParameter(document: Document, parameterId: ElementId) -> bool: ...
    @staticmethod
    def MoveParameterDownOrder(document: Document, parameterId: ElementId) -> bool: ...
    @staticmethod
    def MoveParameterUpOrder(document: Document, parameterId: ElementId) -> bool: ...
    @staticmethod
    def SortParameters(document: Document, order: ParametersOrder) -> None: ...

class GradientBackgroundSettings(BackgroundSettings):
    """.NET: Autodesk.Revit.DB.GradientBackgroundSettings"""
    def __init__(self, *args) -> None: ...
    GroundColor: Color
    HorizonColor: Color
    SkyColor: Color
    IsValidObject: bool

class GraphicsStyle(Element):
    """.NET: Autodesk.Revit.DB.GraphicsStyle"""
    def __init__(self, *args) -> None: ...
    GraphicsStyleType: GraphicsStyleType
    GraphicsStyleCategory: Category
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

class GraphicsStyleType:
    """.NET: Autodesk.Revit.DB.GraphicsStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class Grid(DatumPlane):
    """.NET: Autodesk.Revit.DB.Grid"""
    def __init__(self, *args) -> None: ...
    IsCurved: bool
    Curve: Curve
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
    def Create(document: Document, arc: Arc) -> Grid: ...
    def GetExtents(self, ) -> Outline: ...
    def SetVerticalExtents(self, bottom: float, top: float) -> None: ...

class GridNode:
    """.NET: Autodesk.Revit.DB.GridNode"""
    def __init__(self, *args) -> None: ...
    VIndex: int
    UIndex: int

class GridNodeLocation:
    """.NET: Autodesk.Revit.DB.GridNodeLocation"""
    def __init__(self, *args) -> None: ...
    ...

class GridSegmentDirection:
    """.NET: Autodesk.Revit.DB.GridSegmentDirection"""
    def __init__(self, *args) -> None: ...
    ...

class GridType(LineAndTextAttrSymbol):
    """.NET: Autodesk.Revit.DB.GridType"""
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

class Group(Element):
    """.NET: Autodesk.Revit.DB.Group"""
    def __init__(self, *args) -> None: ...
    AttachedParentId: ElementId
    IsAttached: bool
    Location: Location
    GroupType: GroupType
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
    def GetAvailableAttachedDetailGroupTypeIds(self, ) -> ISet: ...
    def GetMemberIds(self, ) -> IList: ...
    def GetShownAttachedDetailGroupTypeIds(self, view: View) -> ISet: ...
    def HideAllAttachedDetailGroups(self, view: View) -> None: ...
    def HideAttachedDetailGroups(self, view: View, detailGroupTypeId: ElementId) -> None: ...
    def IsCompatibleAttachedDetailGroupType(self, view: View, detailGroupTypeId: ElementId) -> bool: ...
    def ShowAllAttachedDetailGroups(self, view: View) -> None: ...
    def ShowAttachedDetailGroups(self, view: View, detailGroupTypeId: ElementId) -> None: ...
    def UngroupMembers(self, ) -> ICollection: ...

class GroupLoadOptions:
    """.NET: Autodesk.Revit.DB.GroupLoadOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ReplaceDuplicatedGroups: bool
    IncludeGrids: bool
    IncludeLevels: bool
    IncludeAttachedDetails: bool
    def Dispose(self, ) -> None: ...
    def GetDuplicateTypeNamesHandler(self, ) -> IDuplicateTypeNamesHandler: ...
    def SetDuplicateTypeNamesHandler(self, handler: IDuplicateTypeNamesHandler) -> None: ...

class GroupNode(RenderNode):
    """.NET: Autodesk.Revit.DB.GroupNode"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    NodeName: str
    def GetTransform(self, ) -> Transform: ...

class GroupSet(APIObject):
    """.NET: Autodesk.Revit.DB.GroupSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: Group) -> bool: ...
    def Erase(self, item: Group) -> int: ...
    def ForwardIterator(self, ) -> GroupSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: Group) -> bool: ...
    def ReverseIterator(self, ) -> GroupSetIterator: ...

class GroupSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.GroupSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class GroupType(ElementType):
    """.NET: Autodesk.Revit.DB.GroupType"""
    def __init__(self, *args) -> None: ...
    Groups: GroupSet
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
    def GetAvailableAttachedDetailGroupTypeIds(self, ) -> ISet: ...
    def LoadFrom(self, fileName: str, options: GroupLoadOptions) -> None: ...

class GroupTypeId:
    """.NET: Autodesk.Revit.DB.GroupTypeId"""
    def __init__(self, *args) -> None: ...
    StairNumberSystemAboveCutMarkText: ForgeTypeId
    StairNumberSystemAboveCutMarkGraphics: ForgeTypeId
    Sustainability: ForgeTypeId
    WallCrossSectionDefinition: ForgeTypeId
    Visualization: ForgeTypeId
    Visibility: ForgeTypeId
    ViewExtents: ForgeTypeId
    ViewCamera: ForgeTypeId
    Underlay: ForgeTypeId
    TrussFamilyVertWeb: ForgeTypeId
    TrussFamilyTopChord: ForgeTypeId
    TrussFamilyDiagWeb: ForgeTypeId
    TrussFamilyBottomChord: ForgeTypeId
    TranslationIn: ForgeTypeId
    ToposolidSubdivision: ForgeTypeId
    Title: ForgeTypeId
    Text: ForgeTypeId
    Termination: ForgeTypeId
    SystemtypeRisedrop: ForgeTypeId
    Support: ForgeTypeId
    StructuralSectionGeometry: ForgeTypeId
    StructuralSectionDimensions: ForgeTypeId
    StructuralAnalysis: ForgeTypeId
    Structural: ForgeTypeId
    StairsWinders: ForgeTypeId
    StairsTreadsRisers: ForgeTypeId
    StairsSupports: ForgeTypeId
    StairsOpenEndConnection: ForgeTypeId
    StairsCalculatorRules: ForgeTypeId
    StairTreads: ForgeTypeId
    StairStringers: ForgeTypeId
    StairRisers: ForgeTypeId
    SplitProfileDimensions: ForgeTypeId
    SlabShapeEdit: ForgeTypeId
    SegmentsFittings: ForgeTypeId
    SecondaryEnd: ForgeTypeId
    RouteAnalysis: ForgeTypeId
    RotationAbout: ForgeTypeId
    ReleasesMemberForces: ForgeTypeId
    Reference: ForgeTypeId
    RebarSystemLayers: ForgeTypeId
    RebarArray: ForgeTypeId
    RailingSystemSegmentVGrid: ForgeTypeId
    RailingSystemSegmentUGrid: ForgeTypeId
    RailingSystemSegmentPosts: ForgeTypeId
    RailingSystemSegmentPatternRepeat: ForgeTypeId
    RailingSystemSegmentPatternRemainder: ForgeTypeId
    RailingSystemSecondaryFamilyHandrails: ForgeTypeId
    RailingSystemFamilyTopRail: ForgeTypeId
    RailingSystemFamilySegmentPattern: ForgeTypeId
    RailingSystemFamilyHandrails: ForgeTypeId
    Profilen2: ForgeTypeId
    Profilen1: ForgeTypeId
    Profile: ForgeTypeId
    PrimaryUnits: ForgeTypeId
    PrimaryEnd: ForgeTypeId
    Plumbing: ForgeTypeId
    ViewPositioning: ForgeTypeId
    Phasing: ForgeTypeId
    PatternApplication: ForgeTypeId
    Pattern: ForgeTypeId
    OverallLegend: ForgeTypeId
    Nodes: ForgeTypeId
    Moments: ForgeTypeId
    MechanicalLoads: ForgeTypeId
    MechanicalAirflow: ForgeTypeId
    Mechanical: ForgeTypeId
    Materials: ForgeTypeId
    Lining: ForgeTypeId
    LightPhotometrics: ForgeTypeId
    LifeSafety: ForgeTypeId
    Length: ForgeTypeId
    Insulation: ForgeTypeId
    Ifc: ForgeTypeId
    IdentityData: ForgeTypeId
    GreenBuilding: ForgeTypeId
    Graphics: ForgeTypeId
    GeometryPositioning: ForgeTypeId
    GeoLocation: ForgeTypeId
    General: ForgeTypeId
    Forces: ForgeTypeId
    Flexible: ForgeTypeId
    Fitting: ForgeTypeId
    FireProtection: ForgeTypeId
    FabricationProductData: ForgeTypeId
    EnergyAnalysisRoomSpaceData: ForgeTypeId
    EnergyAnalysisDetailedModel: ForgeTypeId
    EnergyAnalysisDetailedAndConceptualModels: ForgeTypeId
    EnergyAnalysisConceptualModel: ForgeTypeId
    EnergyAnalysisBuildingData: ForgeTypeId
    EnergyAnalysisBldgConsMtlThermalProps: ForgeTypeId
    EnergyAnalysisAdvanced: ForgeTypeId
    EnergyAnalysis: ForgeTypeId
    ElectricalLoads: ForgeTypeId
    ElectricalLighting: ForgeTypeId
    ElectricalEngineering: ForgeTypeId
    ElectricalCircuiting: ForgeTypeId
    ElectricalAnalysis: ForgeTypeId
    Electrical: ForgeTypeId
    DivisionGeometry: ForgeTypeId
    Display: ForgeTypeId
    Data: ForgeTypeId
    CurtainMullionn2: ForgeTypeId
    CurtainMullionn1: ForgeTypeId
    CurtainMullionVert: ForgeTypeId
    CurtainMullionHoriz: ForgeTypeId
    CurtainGridn2: ForgeTypeId
    CurtainGridn1: ForgeTypeId
    CurtainGridVert: ForgeTypeId
    CurtainGridV: ForgeTypeId
    CurtainGridU: ForgeTypeId
    CurtainGridHoriz: ForgeTypeId
    CurtainGrid: ForgeTypeId
    CouplerArray: ForgeTypeId
    ContinuousrailEndTopExtension: ForgeTypeId
    ContinuousrailBeginBottomExtension: ForgeTypeId
    Construction: ForgeTypeId
    Constraints: ForgeTypeId
    ConceptualEnergyDataBuildingServices: ForgeTypeId
    ConceptualEnergyData: ForgeTypeId
    Area: ForgeTypeId
    AnalyticalProperties: ForgeTypeId
    AnalyticalModel: ForgeTypeId
    AnalyticalAlignment: ForgeTypeId
    AnalysisResults: ForgeTypeId
    AlternateUnits: ForgeTypeId
    AdskModelProperties: ForgeTypeId
    Geometry: ForgeTypeId

class GuidEnum:
    """.NET: Autodesk.Revit.DB.GuidEnum"""
    def __init__(self, *args) -> None: ...
    Guid: Guid
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class HasNoValueFilterRule(ParameterValuePresenceRule):
    """.NET: Autodesk.Revit.DB.HasNoValueFilterRule"""
    def __init__(self, *args) -> None: ...
    Parameter: ElementId
    IsValidObject: bool

class HasValueFilterRule(ParameterValuePresenceRule):
    """.NET: Autodesk.Revit.DB.HasValueFilterRule"""
    def __init__(self, *args) -> None: ...
    Parameter: ElementId
    IsValidObject: bool

class HermiteFace(Face):
    """.NET: Autodesk.Revit.DB.HermiteFace"""
    def __init__(self, *args) -> None: ...
    MixedDerivs: IList
    Tangents: IList
    Points: IList
    Params: DoubleArray
    Period: float
    IsCyclic: bool
    Area: float
    Reference: Reference
    IsTwoSided: bool
    MaterialElementId: ElementId
    EdgeLoops: EdgeArrayArray
    HasRegions: bool
    OrientationMatchesSurfaceOrientation: bool
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool

class HermiteSpline(Curve):
    """.NET: Autodesk.Revit.DB.HermiteSpline"""
    def __init__(self, *args) -> None: ...
    Parameters: DoubleArray
    Tangents: IList
    ControlPoints: IList
    IsPeriodic: bool
    Period: float
    IsCyclic: bool
    Length: float
    ApproximateLength: float
    Reference: Reference
    IsClosed: bool
    IsBound: bool
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool
    @staticmethod
    def Create(controlPoints: IList, periodic: bool, tangents: HermiteSplineTangents) -> HermiteSpline: ...

class HermiteSplineTangents:
    """.NET: Autodesk.Revit.DB.HermiteSplineTangents"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    EndTangent: XYZ
    StartTangent: XYZ
    def Dispose(self, ) -> None: ...

class HermiteSurface(Surface):
    """.NET: Autodesk.Revit.DB.HermiteSurface"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    OrientationMatchesParametricOrientation: bool
    @staticmethod
    def Create(nU: int, nV: int, points: IList, periodicU: bool, periodicV: bool) -> HermiteSurface: ...
    def IsValid(self, ) -> bool: ...

class HiddenLineViewsType:
    """.NET: Autodesk.Revit.DB.HiddenLineViewsType"""
    def __init__(self, *args) -> None: ...
    ...

class HomeCamera:
    """.NET: Autodesk.Revit.DB.HomeCamera"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ViewId: ElementId
    OrthogonalProjectionHeight: float
    OrthogonalProjectionWidth: float
    BottomAngleOfFieldOfView: float
    TopAngleOfFieldOfView: float
    RightAngleOfFieldOfView: float
    LeftAngleOfFieldOfView: float
    Pivot: XYZ
    UpDirection: XYZ
    Center: XYZ
    EyePosition: XYZ
    def Dispose(self, ) -> None: ...

class HorizontalAlign:
    """.NET: Autodesk.Revit.DB.HorizontalAlign"""
    def __init__(self, *args) -> None: ...
    ...

class HorizontalAlignmentStyle:
    """.NET: Autodesk.Revit.DB.HorizontalAlignmentStyle"""
    def __init__(self, *args) -> None: ...
    ...

class HorizontalTextAlignment:
    """.NET: Autodesk.Revit.DB.HorizontalTextAlignment"""
    def __init__(self, *args) -> None: ...
    ...

class HostObjAttributes(ElementType):
    """.NET: Autodesk.Revit.DB.HostObjAttributes"""
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
    def GetCompoundStructure(self, ) -> CompoundStructure: ...
    def SetCompoundStructure(self, compoundStructure: CompoundStructure) -> None: ...

class HostObject(Element):
    """.NET: Autodesk.Revit.DB.HostObject"""
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
    def FindInserts(self, addRectOpenings: bool, includeShadows: bool, includeEmbeddedWalls: bool, includeSharedEmbeddedInserts: bool) -> IList: ...

class HostObjectUtils:
    """.NET: Autodesk.Revit.DB.HostObjectUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetBottomFaces(hostObject: HostObject) -> IList: ...
    @staticmethod
    def GetSideFaces(hostObject: HostObject, side: ShellLayerType) -> IList: ...
    @staticmethod
    def GetTopFaces(hostObject: HostObject) -> IList: ...

class HostedSweep(HostObject):
    """.NET: Autodesk.Revit.DB.HostedSweep"""
    def __init__(self, *args) -> None: ...
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
    def GetEndPointParameter(self, targetRef: Reference, endIdx: int) -> float: ...
    def HorizontalFlip(self, ) -> None: ...
    def RemoveSegment(self, targetRef: Reference) -> None: ...
    def SetEndPointParameter(self, targetRef: Reference, endIdx: int, param: float) -> bool: ...
    def VerticalFlip(self, ) -> None: ...

class HostedSweepType(HostObjAttributes):
    """.NET: Autodesk.Revit.DB.HostedSweepType"""
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

class ICentralLockedCallback:
    """.NET: Autodesk.Revit.DB.ICentralLockedCallback"""
    def __init__(self, *args) -> None: ...
    def ShouldWaitForLockAvailability(self, ) -> bool: ...

class IConnector:
    """.NET: Autodesk.Revit.DB.IConnector"""
    def __init__(self, *args) -> None: ...
    Radius: float
    Height: float
    Width: float
    Shape: ConnectorProfileType
    Domain: Domain
    Origin: XYZ
    CoordinateSystem: Transform

class ICustomFieldProperties:
    """.NET: Autodesk.Revit.DB.ICustomFieldProperties"""
    def __init__(self, *args) -> None: ...
    def AreEqualTo(self, otherProperties: ICustomFieldProperties) -> bool: ...

class IDataConversionMonitor:
    """.NET: Autodesk.Revit.DB.IDataConversionMonitor"""
    def __init__(self, *args) -> None: ...
    def GetVerbosity(self, ) -> DataExchangeMessageVerbosity: ...
    def ProcessMessage(self, messageId: DataExchangeMessageId, messageSeverity: DataExchangeMessageSeverity, entityIds: IList) -> bool: ...

class IDuplicateTypeNamesHandler:
    """.NET: Autodesk.Revit.DB.IDuplicateTypeNamesHandler"""
    def __init__(self, *args) -> None: ...
    def OnDuplicateTypeNamesFound(self, args: DuplicateTypeNamesHandlerArgs) -> DuplicateTypeAction: ...

class IExportContext:
    """.NET: Autodesk.Revit.DB.IExportContext"""
    def __init__(self, *args) -> None: ...
    def Finish(self, ) -> None: ...
    def IsCanceled(self, ) -> bool: ...
    def OnElementBegin(self, elementId: ElementId) -> RenderNodeAction: ...
    def OnElementEnd(self, elementId: ElementId) -> None: ...
    def OnFaceBegin(self, node: FaceNode) -> RenderNodeAction: ...
    def OnFaceEnd(self, node: FaceNode) -> None: ...
    def OnInstanceBegin(self, node: InstanceNode) -> RenderNodeAction: ...
    def OnInstanceEnd(self, node: InstanceNode) -> None: ...
    def OnLight(self, node: LightNode) -> None: ...
    def OnLinkBegin(self, node: LinkNode) -> RenderNodeAction: ...
    def OnLinkEnd(self, node: LinkNode) -> None: ...
    def OnMaterial(self, node: MaterialNode) -> None: ...
    def OnPolymesh(self, node: PolymeshTopology) -> None: ...
    def OnRPC(self, node: RPCNode) -> None: ...
    def OnViewBegin(self, node: ViewNode) -> RenderNodeAction: ...
    def OnViewEnd(self, elementId: ElementId) -> None: ...
    def Start(self, ) -> bool: ...

class IExportContext2D:
    """.NET: Autodesk.Revit.DB.IExportContext2D"""
    def __init__(self, *args) -> None: ...
    def OnElementBegin2D(self, node: ElementNode) -> RenderNodeAction: ...
    def OnElementEnd2D(self, node: ElementNode) -> None: ...
    def OnFaceEdge2D(self, node: FaceEdgeNode) -> RenderNodeAction: ...
    def OnFaceSilhouette2D(self, node: FaceSilhouetteNode) -> RenderNodeAction: ...

class IExportContextBase:
    """.NET: Autodesk.Revit.DB.IExportContextBase"""
    def __init__(self, *args) -> None: ...
    def OnCurve(self, node: CurveNode) -> RenderNodeAction: ...
    def OnLineSegment(self, segment: LineSegment) -> None: ...
    def OnPolyline(self, node: PolylineNode) -> RenderNodeAction: ...
    def OnPolylineSegments(self, segments: PolylineSegments) -> None: ...
    def OnText(self, node: TextNode) -> None: ...

class IExtension:
    """.NET: Autodesk.Revit.DB.IExtension"""
    def __init__(self, *args) -> None: ...
    IsMiterLocked: bool
    HasMiter: bool
    SymbolicExtended: bool
    Extended: bool

class IExternalDBApplication:
    """.NET: Autodesk.Revit.DB.IExternalDBApplication"""
    def __init__(self, *args) -> None: ...
    def OnShutdown(self, application: ControlledApplication) -> ExternalDBApplicationResult: ...
    def OnStartup(self, application: ControlledApplication) -> ExternalDBApplicationResult: ...

class IExternalResourceServer:
    """.NET: Autodesk.Revit.DB.IExternalResourceServer"""
    def __init__(self, *args) -> None: ...
    def AreSameResources(self, reference1: IDictionary, reference2: IDictionary) -> bool: ...
    def GetIconPath(self, ) -> str: ...
    def GetInSessionPath(self, reference: ExternalResourceReference, originalDisplayPath: str) -> str: ...
    def GetInformationLink(self, ) -> str: ...
    def GetResourceVersionStatus(self, reference: ExternalResourceReference) -> ResourceVersionStatus: ...
    def GetShortName(self, ) -> str: ...
    def GetTypeSpecificServerOperations(self, extensions: ExternalResourceServerExtensions) -> None: ...
    def IsResourceWellFormed(self, extRef: ExternalResourceReference) -> bool: ...
    def LoadResource(self, loadRequestId: Guid, resourceType: ExternalResourceType, desiredResource: ExternalResourceReference, loadContext: ExternalResourceLoadContext, loadResults: ExternalResourceLoadContent) -> None: ...
    def SetupBrowserData(self, browseData: ExternalResourceBrowserData) -> None: ...
    def SupportsExternalResourceType(self, type: ExternalResourceType) -> bool: ...

class IFCBuiltInCategoryKey:
    """.NET: Autodesk.Revit.DB.IFCBuiltInCategoryKey"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class IFCCategoryTemplate(Element):
    """.NET: Autodesk.Revit.DB.IFCCategoryTemplate"""
    def __init__(self, *args) -> None: ...
    IsValidCategoryMappingFile: bool
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
    def CopyTemplate(self, document: Document, copyTemplateName: str) -> IFCCategoryTemplate: ...
    @staticmethod
    def Create(document: Document, name: str) -> IFCCategoryTemplate: ...
    def ExportToFile(self, document: Document, fileName: str) -> None: ...
    @staticmethod
    def FindByName(document: Document, name: str) -> IFCCategoryTemplate: ...
    @staticmethod
    def GetActiveTemplate(document: Document) -> IFCCategoryTemplate: ...
    def GetCategoryMappingTable(self, document: Document) -> IDictionary: ...
    def GetMappingInfoById(self, document: Document, categoryId: ElementId, customSubCategoryId: CustomSubCategoryId) -> ExportIFCCategoryInfo: ...
    @staticmethod
    def GetOrCreateInSessionTemplate(document: Document) -> IFCCategoryTemplate: ...
    @staticmethod
    def ImportFromFile(document: Document, fileName: str, templateName: str) -> IFCCategoryTemplate: ...
    @staticmethod
    def IsValidName(document: Document, name: str) -> bool: ...
    @staticmethod
    def ListNames(document: Document) -> IList: ...
    @staticmethod
    def ResetActiveTemplate(document: Document) -> None: ...
    def ResetCategoryToDefault(self, categoryKey: ExportIFCCategoryKey) -> ExportIFCCategoryInfo: ...
    def SetActiveTemplate(self, ) -> None: ...
    def SetMappingInfo(self, key: ExportIFCCategoryKey, info: ExportIFCCategoryInfo) -> None: ...
    def UpdateCategoryList(self, document: Document) -> None: ...

class IFCExportElement:
    """.NET: Autodesk.Revit.DB.IFCExportElement"""
    def __init__(self, *args) -> None: ...
    ...

class IFCExportElementType:
    """.NET: Autodesk.Revit.DB.IFCExportElementType"""
    def __init__(self, *args) -> None: ...
    ...

class IFCExportOptions:
    """.NET: Autodesk.Revit.DB.IFCExportOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    FilterViewId: ElementId
    SpaceBoundaryLevel: int
    FamilyMappingFile: str
    ExportBaseQuantities: bool
    WallAndColumnSplitting: bool
    FileVersion: IFCVersion
    def AddOption(self, name: str, value: str) -> None: ...
    def Assign(self, sourceOptions: IFCExportOptions) -> None: ...
    def Dispose(self, ) -> None: ...

class IFCParameterTemplate(Element):
    """.NET: Autodesk.Revit.DB.IFCParameterTemplate"""
    def __init__(self, *args) -> None: ...
    ExportUserDefinedPropertySets: bool
    ExportRevitSchedules: bool
    ExportRevitMaterialParameters: bool
    ExportRevitElementParameters: bool
    ExportIFCBaseQuantities: bool
    ExportIFCCommonPropertySets: bool
    IsValidParameterMappingFile: bool
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
    def AddPropertyMappingInfo(self, propertySetupType: PropertySetupType, propertySetName: str, propertyMappingInfo: IFCPropertyMappingInfo) -> None: ...
    def AddPropertySet(self, propertySetupType: PropertySetupType, exportFlag: bool, propertySetName: str) -> None: ...
    def ClearPropertySets(self, propertySetupType: PropertySetupType) -> None: ...
    def CopyPropertySet(self, propertySetupType: PropertySetupType, propertySetName: str, propertySetCopyName: str) -> None: ...
    def CopyTemplate(self, document: Document, copyTemplateName: str) -> IFCParameterTemplate: ...
    @staticmethod
    def Create(document: Document, name: str) -> IFCParameterTemplate: ...
    def ExportPropertySetupToFile(self, propertySetupType: PropertySetupType, fileName: str) -> None: ...
    def ExportToFile(self, fileName: str) -> None: ...
    @staticmethod
    def FindByName(document: Document, name: str) -> IFCParameterTemplate: ...
    def FindPropertyMappingInfo(self, propertySetupType: PropertySetupType, propertySetName: str, revitPropertyId: ElementId) -> IFCPropertyMappingInfo: ...
    @staticmethod
    def GetActiveTemplate(document: Document) -> IFCParameterTemplate: ...
    @staticmethod
    def GetOrCreateInSessionTemplate(document: Document) -> IFCParameterTemplate: ...
    def GetPropertyMappingInfos(self, propertySetupType: PropertySetupType, propertySetName: str, propertySelectionType: PropertySelectionType) -> IList: ...
    def GetPropertySetApplicableEntities(self, propertySetupType: PropertySetupType, propertySetName: str) -> IList: ...
    def GetPropertySetNames(self, propertySetupType: PropertySetupType, propertySelectionType: PropertySelectionType) -> IList: ...
    @staticmethod
    def ImportFromFile(document: Document, fileName: str, templateName: str) -> IFCParameterTemplate: ...
    def ImportPropertySetupFromFile(self, fileName: str) -> None: ...
    def IsExportingPropertySet(self, propertySetupType: PropertySetupType, propertySetName: str) -> bool: ...
    def IsInSessionTemplate(self, ) -> bool: ...
    def IsPropertySetAMemberOfTemplate(self, propertySetupType: PropertySetupType, propertySetName: str) -> bool: ...
    @staticmethod
    def IsValidName(document: Document, name: str) -> bool: ...
    @staticmethod
    def ListNames(document: Document) -> IList: ...
    def RemovePropertyMappingInfo(self, propertySetupType: PropertySetupType, propertySetName: str, revitPropertyId: ElementId) -> None: ...
    def RemovePropertySet(self, propertySetupType: PropertySetupType, propertySetName: str) -> None: ...
    @staticmethod
    def ResetActiveTemplate(document: Document) -> None: ...
    def SetActiveTemplate(self, ) -> None: ...
    def SetInSessionTemplateDocument(self, document: Document) -> None: ...
    def SetPropertySetApplicableEntities(self, propertySetupType: PropertySetupType, propertySetName: str, applicableEntities: IList) -> None: ...
    def SetPropertySetExportingFlag(self, propertySetupType: PropertySetupType, propertySetName: str, exportFlag: bool) -> None: ...

class IFCPropertyMappingInfo:
    """.NET: Autodesk.Revit.DB.IFCPropertyMappingInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ExportFlag: bool
    RevitPropertyName: str
    RevitPropertyId: ElementId
    IFCPropertyName: str
    def Dispose(self, ) -> None: ...
    @staticmethod
    def IsValidMappingInfo(mappingInfo: IFCPropertyMappingInfo) -> bool: ...

class IFCPropertySetMappingInfo:
    """.NET: Autodesk.Revit.DB.IFCPropertySetMappingInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class IFCUserDefinedProperty:
    """.NET: Autodesk.Revit.DB.IFCUserDefinedProperty"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    DataTypeDefined: str
    PropertyType: IFCUserDefinedPropertyType
    DataType: str
    RevitPropertyName: str
    RevitPropertyId: ElementId
    IFCPropertyName: str
    def Dispose(self, ) -> None: ...

class IFCUserDefinedPropertySet(Element):
    """.NET: Autodesk.Revit.DB.IFCUserDefinedPropertySet"""
    def __init__(self, *args) -> None: ...
    PropertySetType: IFCUserDefinedPropertySetType
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
    def AddProperty(self, userDefinedProperty: IFCUserDefinedProperty) -> None: ...
    def ClearPropertySet(self, ) -> None: ...
    def CopyPropertySet(self, document: Document, copyPropertySetName: str) -> IFCUserDefinedPropertySet: ...
    @staticmethod
    def Create(document: Document, name: str) -> IFCUserDefinedPropertySet: ...
    @staticmethod
    def ExportToFile(document: Document, fileName: str) -> None: ...
    def FindPropertyByName(self, name: str) -> IFCUserDefinedProperty: ...
    @staticmethod
    def FindPropertySetByName(document: Document, name: str) -> IFCUserDefinedPropertySet: ...
    def GetApplicableEntities(self, ) -> IList: ...
    def GetProperties(self, ) -> IList: ...
    @staticmethod
    def ImportFromFile(document: Document, fileName: str, validUserDefinedPropertySetFile: bool) -> IList: ...
    def IsPropertyAMemberOfPropertySet(self, propertyName: str) -> bool: ...
    @staticmethod
    def IsValidName(document: Document, name: str) -> bool: ...
    @staticmethod
    def ListPropertySetNames(document: Document) -> IList: ...
    def RemoveProperty(self, propertyName: str) -> None: ...
    def SetApplicableEntities(self, applicableEntities: IList) -> None: ...

class IFCUserDefinedPropertySetType:
    """.NET: Autodesk.Revit.DB.IFCUserDefinedPropertySetType"""
    def __init__(self, *args) -> None: ...
    ...

class IFCUserDefinedPropertyType:
    """.NET: Autodesk.Revit.DB.IFCUserDefinedPropertyType"""
    def __init__(self, *args) -> None: ...
    ...

class IFCVersion:
    """.NET: Autodesk.Revit.DB.IFCVersion"""
    def __init__(self, *args) -> None: ...
    ...

class IFailuresPreprocessor:
    """.NET: Autodesk.Revit.DB.IFailuresPreprocessor"""
    def __init__(self, *args) -> None: ...
    def PreprocessFailures(self, failuresAccessor: FailuresAccessor) -> FailureProcessingResult: ...

class IFailuresProcessor:
    """.NET: Autodesk.Revit.DB.IFailuresProcessor"""
    def __init__(self, *args) -> None: ...
    def Dismiss(self, document: Document) -> None: ...
    def ProcessFailures(self, data: FailuresAccessor) -> FailureProcessingResult: ...

class IFamilyLoadOptions:
    """.NET: Autodesk.Revit.DB.IFamilyLoadOptions"""
    def __init__(self, *args) -> None: ...
    def OnFamilyFound(self, familyInUse: bool, overwriteParameterValues: bool) -> bool: ...
    def OnSharedFamilyFound(self, sharedFamily: Family, familyInUse: bool, source: FamilySource, overwriteParameterValues: bool) -> bool: ...

class IGetLocalPathForOpenCallback:
    """.NET: Autodesk.Revit.DB.IGetLocalPathForOpenCallback"""
    def __init__(self, *args) -> None: ...
    def GetLocalPathForOpen(self, desiredResource: ExternalResourceReference) -> str: ...

class IModelExportContext:
    """.NET: Autodesk.Revit.DB.IModelExportContext"""
    def __init__(self, *args) -> None: ...
    def OnPoint(self, node: PointNode) -> RenderNodeAction: ...

class INavisworksExporter:
    """.NET: Autodesk.Revit.DB.INavisworksExporter"""
    def __init__(self, *args) -> None: ...
    def Export(self, document: Document, folder: str, name: str, options: NavisworksExportOptions) -> None: ...
    def ValidateExportOptions(self, document: Document, folder: str, name: str, options: NavisworksExportOptions, exceptionMessage: str) -> bool: ...

class IOnLocalLinkSharedCoordinatesSavedCallback:
    """.NET: Autodesk.Revit.DB.IOnLocalLinkSharedCoordinatesSavedCallback"""
    def __init__(self, *args) -> None: ...
    def OnLocalLinkSharedCoordinatesSaved(self, changedResource: ExternalResourceReference) -> None: ...

class IOpenFromCloudCallback:
    """.NET: Autodesk.Revit.DB.IOpenFromCloudCallback"""
    def __init__(self, *args) -> None: ...
    def OnOpenConflict(self, scenario: OpenConflictScenario) -> OpenConflictResult: ...

class IPerformanceAdviserRule:
    """.NET: Autodesk.Revit.DB.IPerformanceAdviserRule"""
    def __init__(self, *args) -> None: ...
    def ExecuteElementCheck(self, document: Document, element: Element) -> None: ...
    def FinalizeCheck(self, document: Document) -> None: ...
    def GetDescription(self, ) -> str: ...
    def GetElementFilter(self, document: Document) -> ElementFilter: ...
    def GetName(self, ) -> str: ...
    def InitCheck(self, document: Document) -> None: ...
    def WillCheckElements(self, ) -> bool: ...

class IPhotoRenderContext:
    """.NET: Autodesk.Revit.DB.IPhotoRenderContext"""
    def __init__(self, *args) -> None: ...
    ...

class IPrintSetting:
    """.NET: Autodesk.Revit.DB.IPrintSetting"""
    def __init__(self, *args) -> None: ...
    PrintParameters: PrintParameters

class ISaveSharedCoordinatesCallback:
    """.NET: Autodesk.Revit.DB.ISaveSharedCoordinatesCallback"""
    def __init__(self, *args) -> None: ...
    def GetSaveModifiedLinksOption(self, link: RevitLinkType) -> SaveModifiedLinksOptions: ...

class ISaveSharedCoordinatesCallbackForUnloadLocally:
    """.NET: Autodesk.Revit.DB.ISaveSharedCoordinatesCallbackForUnloadLocally"""
    def __init__(self, *args) -> None: ...
    def GetSaveModifiedLinksOptionForUnloadLocally(self, link: RevitLinkType) -> SaveModifiedLinksOptionsForUnloadLocally: ...

class ITransactionFinalizer:
    """.NET: Autodesk.Revit.DB.ITransactionFinalizer"""
    def __init__(self, *args) -> None: ...
    def OnCommitted(self, document: Document, strTransactionName: str) -> None: ...
    def OnRolledBack(self, document: Document, strTransactionName: str) -> None: ...

class ITransientElementMaker:
    """.NET: Autodesk.Revit.DB.ITransientElementMaker"""
    def __init__(self, *args) -> None: ...
    def Execute(self, ) -> None: ...

class IUpdater:
    """.NET: Autodesk.Revit.DB.IUpdater"""
    def __init__(self, *args) -> None: ...
    def Execute(self, data: UpdaterData) -> None: ...
    def GetAdditionalInformation(self, ) -> str: ...
    def GetChangePriority(self, ) -> ChangePriority: ...
    def GetUpdaterId(self, ) -> UpdaterId: ...
    def GetUpdaterName(self, ) -> str: ...

class IViewSheetSet:
    """.NET: Autodesk.Revit.DB.IViewSheetSet"""
    def __init__(self, *args) -> None: ...
    IsAutomatic: bool
    ViewOrganizationId: ElementId
    SheetOrganizationId: ElementId
    OrderedViewList: IReadOnlyList
    Views: ViewSet

class ImageBackgroundSettings(BackgroundSettings):
    """.NET: Autodesk.Revit.DB.ImageBackgroundSettings"""
    def __init__(self, *args) -> None: ...
    OffsetHeight: float
    OffsetWidth: float
    BackgroundImageFit: BackgroundImageFit
    FilePath: str
    IsValidObject: bool

class ImageExportOptions:
    """.NET: Autodesk.Revit.DB.ImageExportOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ExportRange: ExportRange
    ShouldCreateWebSite: bool
    FilePath: str
    ViewName: str
    FitDirection: FitDirectionType
    HLRandWFViewsFileType: ImageFileType
    ShadowViewsFileType: ImageFileType
    ImageResolution: ImageResolution
    PixelSize: int
    Zoom: int
    ZoomType: ZoomFitType
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetFileName(aDoc: Document, dbViewId: ElementId) -> str: ...
    def GetViewsAndSheets(self, ) -> IList: ...
    @staticmethod
    def IsValidFileName(filePath: str) -> bool: ...
    @staticmethod
    def IsValidForSaveToProjectAsImage(options: ImageExportOptions, doc: Document) -> bool: ...
    def SetViewsAndSheets(self, viewsAndSheets: IList) -> None: ...

class ImageFileType:
    """.NET: Autodesk.Revit.DB.ImageFileType"""
    def __init__(self, *args) -> None: ...
    ...

class ImageInstance(Element):
    """.NET: Autodesk.Revit.DB.ImageInstance"""
    def __init__(self, *args) -> None: ...
    CanHaveSnaps: bool
    EnableSnaps: bool
    DrawLayer: DrawLayer
    LockProportions: bool
    HeightScale: float
    WidthScale: float
    Height: float
    Width: float
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
    def Create(document: Document, view: View, imageTypeId: ElementId, placementOptions: ImagePlacementOptions) -> ImageInstance: ...
    def GetLocation(self, placementPoint: BoxPlacement) -> XYZ: ...
    @staticmethod
    def IsValidView(view: View) -> bool: ...
    def SetLocation(self, newLocation: XYZ, placementPoint: BoxPlacement) -> None: ...

class ImagePlacementOptions:
    """.NET: Autodesk.Revit.DB.ImagePlacementOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    PlacementPoint: BoxPlacement
    Location: XYZ
    def Dispose(self, ) -> None: ...

class ImageResolution:
    """.NET: Autodesk.Revit.DB.ImageResolution"""
    def __init__(self, *args) -> None: ...
    ...

class ImageType(ElementType):
    """.NET: Autodesk.Revit.DB.ImageType"""
    def __init__(self, *args) -> None: ...
    Resolution: float
    Height: float
    Width: float
    Status: ImageTypeStatus
    Source: ImageTypeSource
    PathType: PathType
    Path: str
    ExternalResourceType: ExternalResourceType
    HeightInPixels: int
    WidthInPixels: int
    PageNumber: int
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
    def CanReload(self, ) -> bool: ...
    @staticmethod
    def Create(document: Document, options: ImageTypeOptions) -> ImageType: ...
    def GetImage(self, ) -> Bitmap: ...
    def Reload(self, ) -> None: ...
    def ReloadFrom(self, options: ImageTypeOptions) -> None: ...
    def Unload(self, ) -> None: ...

class ImageTypeOptions:
    """.NET: Autodesk.Revit.DB.ImageTypeOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    SourceType: ImageTypeSource
    Resolution: float
    PageNumber: int
    Path: str
    def Dispose(self, ) -> None: ...
    def IsValid(self, document: Document) -> bool: ...
    def SetExternalResourceReference(self, resourceReference: ExternalResourceReference) -> None: ...
    def SetPath(self, path: str, useRelativePath: bool) -> None: ...

class ImageTypeSource:
    """.NET: Autodesk.Revit.DB.ImageTypeSource"""
    def __init__(self, *args) -> None: ...
    ...

class ImageTypeStatus:
    """.NET: Autodesk.Revit.DB.ImageTypeStatus"""
    def __init__(self, *args) -> None: ...
    ...

class ImageView(ViewDrafting):
    """.NET: Autodesk.Revit.DB.ImageView"""
    def __init__(self, *args) -> None: ...
    ImageInstanceId: ElementId
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
    @staticmethod
    def Create(document: Document, options: ImageTypeOptions) -> ImageView: ...

class ImportColorMode:
    """.NET: Autodesk.Revit.DB.ImportColorMode"""
    def __init__(self, *args) -> None: ...
    ...

class ImportExportFileFormat:
    """.NET: Autodesk.Revit.DB.ImportExportFileFormat"""
    def __init__(self, *args) -> None: ...
    ...

class ImportIFCOptions:
    """.NET: Autodesk.Revit.DB.ImportIFCOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LinkProcessor: str
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetImportIFCOptions() -> ImportIFCOptions: ...

class ImportInstance(Instance):
    """.NET: Autodesk.Revit.DB.ImportInstance"""
    def __init__(self, *args) -> None: ...
    IsLinked: bool
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
    def Create(document: Document, DBView: View, resourceReference: ExternalResourceReference, options: STEPImportOptions, linkLoadResult: LinkLoadResult) -> ImportInstance: ...
    def GetVisibility(self, ) -> FamilyElementVisibility: ...
    def SetVisibility(self, visibility: FamilyElementVisibility) -> None: ...

class ImportOptions3DM(BaseImportOptions):
    """.NET: Autodesk.Revit.DB.ImportOptions3DM"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ReferencePoint: XYZ
    AutoCorrectAlmostVHLines: bool
    VisibleLayersOnly: bool
    CustomScale: float
    OrientToView: bool
    ThisViewOnly: bool
    Placement: ImportPlacement
    ColorMode: ImportColorMode
    Unit: ImportUnit

class ImportPlacement:
    """.NET: Autodesk.Revit.DB.ImportPlacement"""
    def __init__(self, *args) -> None: ...
    ...

class ImportUnit:
    """.NET: Autodesk.Revit.DB.ImportUnit"""
    def __init__(self, *args) -> None: ...
    ...

class InCanvasControlData:
    """.NET: Autodesk.Revit.DB.InCanvasControlData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ImagePath: str
    Position: XYZ
    def Dispose(self, ) -> None: ...

class InSessionPrintSetting:
    """.NET: Autodesk.Revit.DB.InSessionPrintSetting"""
    def __init__(self, *args) -> None: ...
    PrintParameters: PrintParameters
    def Dispose(self, ) -> None: ...

class InSessionViewSheetSet:
    """.NET: Autodesk.Revit.DB.InSessionViewSheetSet"""
    def __init__(self, *args) -> None: ...
    IsAutomatic: bool
    ViewOrganizationId: ElementId
    SheetOrganizationId: ElementId
    OrderedViewList: IReadOnlyList
    Views: ViewSet
    def Dispose(self, ) -> None: ...

class IndependentTag(Element):
    """.NET: Autodesk.Revit.DB.IndependentTag"""
    def __init__(self, *args) -> None: ...
    MergeElbows: bool
    LeadersPresentationMode: LeadersPresentationMode
    RotationAngle: float
    MultiLeader: bool
    LeaderStartCondition: LeaderStartCondition
    LeaderEndCondition: LeaderEndCondition
    HasLeader: bool
    TagHeadPosition: XYZ
    TagOrientation: TagOrientation
    IsOrphaned: bool
    IsMulticategoryTag: bool
    IsMaterialTag: bool
    TagText: str
    MultiReferenceAnnotationId: ElementId
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
    def AddReferences(self, referencesToTag: IList) -> None: ...
    def CanLeaderEndConditionBeAssigned(self, leaderEndCondition: LeaderEndCondition) -> bool: ...
    def CanLeaderStartConditionBeAssigned(self, leaderStartCondition: LeaderStartCondition) -> bool: ...
    @staticmethod
    def Create(document: Document, symId: ElementId, ownerDBViewId: ElementId, referenceToTag: Reference, addLeader: bool, tagOrientation: TagOrientation, pnt: XYZ) -> IndependentTag: ...
    def GetLeaderElbow(self, referenceTagged: Reference) -> XYZ: ...
    def GetLeaderEnd(self, referenceTagged: Reference) -> XYZ: ...
    def GetLeaderStart(self, referenceTagged: Reference) -> XYZ: ...
    def GetTaggedElementIds(self, ) -> ICollection: ...
    def GetTaggedLocalElementIds(self, ) -> ISet: ...
    def GetTaggedLocalElements(self, ) -> ICollection: ...
    def GetTaggedReferences(self, ) -> IList: ...
    def HasLeaderElbow(self, referenceTagged: Reference) -> bool: ...
    def HasTagBehavior(self, ) -> bool: ...
    def HasTagText(self, ) -> bool: ...
    def IsLeaderVisible(self, referenceTagged: Reference) -> bool: ...
    def IsTaggedOnSubelement(self, ) -> bool: ...
    def RemoveReferences(self, referencesToRemove: IList) -> None: ...
    def SetIsLeaderVisible(self, referenceTagged: Reference, visible: bool) -> None: ...
    def SetLeaderElbow(self, referenceTagged: Reference, elbowPosition: XYZ) -> None: ...
    def SetLeaderEnd(self, referenceTagged: Reference, freeLeaderEndPoint: XYZ) -> None: ...
    def SetLeaderStart(self, referenceTagged: Reference, freeLeaderStartPoint: XYZ) -> None: ...

class InsertOrientation:
    """.NET: Autodesk.Revit.DB.InsertOrientation"""
    def __init__(self, *args) -> None: ...
    ...

class InsertableObject(ElementType):
    """.NET: Autodesk.Revit.DB.InsertableObject"""
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

class Instance(Element):
    """.NET: Autodesk.Revit.DB.Instance"""
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
    def GetTotalTransform(self, ) -> Transform: ...
    def GetTransform(self, ) -> Transform: ...

class InstanceBinding(ElementBinding):
    """.NET: Autodesk.Revit.DB.InstanceBinding"""
    def __init__(self, *args) -> None: ...
    Categories: CategorySet
    IsReadOnly: bool

class InstanceNode(GroupNode):
    """.NET: Autodesk.Revit.DB.InstanceNode"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    NodeName: str
    def GetSymbolGeometryId(self, ) -> SymbolGeometryId: ...

class InstanceVoidCutUtils:
    """.NET: Autodesk.Revit.DB.InstanceVoidCutUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def AddInstanceVoidCut(document: Document, element: Element, cuttingInstance: Element) -> None: ...
    @staticmethod
    def CanBeCutWithVoid(element: Element) -> bool: ...
    @staticmethod
    def GetCuttingVoidInstances(element: Element) -> ICollection: ...
    @staticmethod
    def GetElementsBeingCut(cuttingInstance: Element) -> ICollection: ...
    @staticmethod
    def InstanceVoidCutExists(element: Element, cuttingInstance: Element) -> bool: ...
    @staticmethod
    def IsVoidInstanceCuttingElement(element: Element) -> bool: ...
    @staticmethod
    def RemoveInstanceVoidCut(document: Document, element: Element, cuttingInstance: Element) -> None: ...

class InsulationLiningBase(MEPCurve):
    """.NET: Autodesk.Revit.DB.InsulationLiningBase"""
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
    def GetInsulationIds(document: Document, elemId: ElementId) -> ICollection: ...
    @staticmethod
    def GetLiningIds(document: Document, elemId: ElementId) -> ICollection: ...
    @staticmethod
    def IsValidThickness(thickness: float) -> bool: ...

class IntegerParameterValue(ParameterValue):
    """.NET: Autodesk.Revit.DB.IntegerParameterValue"""
    def __init__(self, *args) -> None: ...
    Value: int
    IsValidObject: bool

class IntegerRange:
    """.NET: Autodesk.Revit.DB.IntegerRange"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    High: int
    Low: int
    def Dispose(self, ) -> None: ...

class InternalDefinition(Definition):
    """.NET: Autodesk.Revit.DB.InternalDefinition"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Id: ElementId
    VariesAcrossGroups: bool
    Visible: bool
    BuiltInParameter: BuiltInParameter
    Name: str
    def Dispose(self, ) -> None: ...
    def GetGroupTypeId(self, ) -> ForgeTypeId: ...
    def GetParameterTypeId(self, ) -> ForgeTypeId: ...
    def GetTypeId(self, ) -> ForgeTypeId: ...
    def SetAllowVaryBetweenGroups(self, document: Document, allowVaryBetweenGroups: bool) -> ICollection: ...
    def SetGroupTypeId(self, groupTypeId: ForgeTypeId) -> None: ...

class InternalDefinitions(Definitions):
    """.NET: Autodesk.Revit.DB.InternalDefinitions"""
    def __init__(self, *args) -> None: ...
    Size: int
    IsEmpty: bool
    Item: Definition

class InternalOrigin(Element):
    """.NET: Autodesk.Revit.DB.InternalOrigin"""
    def __init__(self, *args) -> None: ...
    SharedPosition: XYZ
    Position: XYZ
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
    def Get(document: Document) -> InternalOrigin: ...

class IntersectingElementData:
    """.NET: Autodesk.Revit.DB.IntersectingElementData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IntersectionVolume: float
    IntersectedElementId: ElementId
    IntersectingElementId: ElementId
    IntersectionType: IntersectionType
    def Dispose(self, ) -> None: ...

class IntersectionResult(APIObject):
    """.NET: Autodesk.Revit.DB.IntersectionResult"""
    def __init__(self, *args) -> None: ...
    EdgeParameter: float
    EdgeObject: Edge
    Distance: float
    Parameter: float
    UVPoint: UV
    XYZPoint: XYZ
    IsReadOnly: bool

class IntersectionResultArray(APIObject):
    """.NET: Autodesk.Revit.DB.IntersectionResultArray"""
    def __init__(self, *args) -> None: ...
    Item: IntersectionResult
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: IntersectionResult) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> IntersectionResultArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: IntersectionResult, index: int) -> None: ...
    def ReverseIterator(self, ) -> IntersectionResultArrayIterator: ...

class IntersectionResultArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.IntersectionResultArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class IntersectionType:
    """.NET: Autodesk.Revit.DB.IntersectionType"""
    def __init__(self, *args) -> None: ...
    ...

class JoinGeometryUtils:
    """.NET: Autodesk.Revit.DB.JoinGeometryUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def AreElementsJoined(document: Document, firstElement: Element, secondElement: Element) -> bool: ...
    @staticmethod
    def GetJoinedElements(document: Document, element: Element) -> ICollection: ...
    @staticmethod
    def IsCuttingElementInJoin(document: Document, firstElement: Element, secondElement: Element) -> bool: ...
    @staticmethod
    def JoinGeometry(document: Document, firstElement: Element, secondElement: Element) -> None: ...
    @staticmethod
    def SwitchJoinOrder(document: Document, firstElement: Element, secondElement: Element) -> None: ...
    @staticmethod
    def UnjoinGeometry(document: Document, firstElement: Element, secondElement: Element) -> None: ...

class JoinType:
    """.NET: Autodesk.Revit.DB.JoinType"""
    def __init__(self, *args) -> None: ...
    ...

class JunctionType:
    """.NET: Autodesk.Revit.DB.JunctionType"""
    def __init__(self, *args) -> None: ...
    ...

class KeyBasedTreeEntries:
    """.NET: Autodesk.Revit.DB.KeyBasedTreeEntries"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def FindEntry(self, key: str) -> KeyBasedTreeEntry: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetKeyBasedTreeEntriesIterator(self, ) -> KeyBasedTreeEntriesIterator: ...

class KeyBasedTreeEntriesIterator:
    """.NET: Autodesk.Revit.DB.KeyBasedTreeEntriesIterator"""
    def __init__(self, *args) -> None: ...
    Current: KeyBasedTreeEntry
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def IsDone(self, ) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class KeyBasedTreeEntriesLoadContent(ExternalResourceLoadContent):
    """.NET: Autodesk.Revit.DB.KeyBasedTreeEntriesLoadContent"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LoadStatus: ExternalResourceLoadStatus
    Version: str
    def AddEntry(self, entry: KeyBasedTreeEntry) -> bool: ...
    def BuildEntries(self, ) -> None: ...
    def CanAddEntry(self, entry: KeyBasedTreeEntry) -> bool: ...
    def GetEntries(self, ) -> KeyBasedTreeEntries: ...
    def GetLoadResults(self, ) -> KeyBasedTreeEntriesLoadResults: ...
    @staticmethod
    def IsEntriesBuilt(content: KeyBasedTreeEntriesLoadContent) -> bool: ...
    def Reset(self, ) -> None: ...

class KeyBasedTreeEntriesLoadResults:
    """.NET: Autodesk.Revit.DB.KeyBasedTreeEntriesLoadResults"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetFailureMessages(self, ) -> IList: ...
    def GetFileReadErrors(self, ) -> IList: ...
    def GetFileSyntaxErrors(self, ) -> IList: ...
    def GetKeyBasedTreeEntryErrors(self, type: KeyBasedTreeEntryErrorType) -> IList: ...

class KeyBasedTreeEntry:
    """.NET: Autodesk.Revit.DB.KeyBasedTreeEntry"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ParentKey: str
    Key: str
    def Dispose(self, ) -> None: ...
    def GetChildrenKeys(self, ) -> IList: ...

class KeyBasedTreeEntryError:
    """.NET: Autodesk.Revit.DB.KeyBasedTreeEntryError"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ErrorType: KeyBasedTreeEntryErrorType
    def Dispose(self, ) -> None: ...
    def GetEntry(self, ) -> KeyBasedTreeEntry: ...

class KeyBasedTreeEntryErrorType:
    """.NET: Autodesk.Revit.DB.KeyBasedTreeEntryErrorType"""
    def __init__(self, *args) -> None: ...
    ...

class KeyBasedTreeEntryTable(Element):
    """.NET: Autodesk.Revit.DB.KeyBasedTreeEntryTable"""
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
    def GetKeyBasedTreeEntries(self, ) -> KeyBasedTreeEntries: ...
    def LoadFrom(self, desiredResourceReference: ExternalResourceReference, loadResults: KeyBasedTreeEntriesLoadResults) -> ExternalResourceLoadStatus: ...
    def Reload(self, loadResults: KeyBasedTreeEntriesLoadResults) -> ExternalResourceLoadStatus: ...
    def ServerSupports(self, extRef: ExternalResourceReference) -> bool: ...

class KeynoteEntries(KeyBasedTreeEntries):
    """.NET: Autodesk.Revit.DB.KeynoteEntries"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    @staticmethod
    def LoadKeynoteEntriesFromFile(filePath: str, keynoteContent: KeyBasedTreeEntriesLoadContent) -> bool: ...

class KeynoteEntry(KeyBasedTreeEntry):
    """.NET: Autodesk.Revit.DB.KeynoteEntry"""
    def __init__(self, *args) -> None: ...
    KeynoteText: str
    IsValidObject: bool
    ParentKey: str
    Key: str

class KeynoteTable(KeyBasedTreeEntryTable):
    """.NET: Autodesk.Revit.DB.KeynoteTable"""
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
    def GetKeynoteTable(aDoc: Document) -> KeynoteTable: ...

class LabelType:
    """.NET: Autodesk.Revit.DB.LabelType"""
    def __init__(self, *args) -> None: ...
    ...

class LabelUtils:
    """.NET: Autodesk.Revit.DB.LabelUtils"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetFailureSeverityName(failureSeverity: FailureSeverity) -> str: ...
    @staticmethod
    def GetLabelFor(buildingType: gbXMLBuildingType, document: Document) -> str: ...
    @staticmethod
    def GetLabelForBuiltInParameter(parameterTypeId: ForgeTypeId, language: LanguageType) -> str: ...
    @staticmethod
    def GetLabelForDiscipline(disciplineTypeId: ForgeTypeId) -> str: ...
    @staticmethod
    def GetLabelForGroup(groupTypeId: ForgeTypeId) -> str: ...
    @staticmethod
    def GetLabelForSpec(specTypeId: ForgeTypeId) -> str: ...
    @staticmethod
    def GetLabelForSymbol(symbolTypeId: ForgeTypeId) -> str: ...
    @staticmethod
    def GetLabelForUnit(unitTypeId: ForgeTypeId) -> str: ...
    @staticmethod
    def GetStructuralSectionShapeName(shape: StructuralSectionShape) -> str: ...

class LayerCategoryType:
    """.NET: Autodesk.Revit.DB.LayerCategoryType"""
    def __init__(self, *args) -> None: ...
    ...

class LayerModifier:
    """.NET: Autodesk.Revit.DB.LayerModifier"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ModifierType: ModifierType
    Separator: str
    def Dispose(self, ) -> None: ...

class LayoutRule(APIObject):
    """.NET: Autodesk.Revit.DB.LayoutRule"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool

class LayoutRuleClearSpacing(LayoutRule):
    """.NET: Autodesk.Revit.DB.LayoutRuleClearSpacing"""
    def __init__(self, *args) -> None: ...
    JustifyType: BeamSystemJustifyType
    Spacing: float
    IsReadOnly: bool

class LayoutRuleFixedDistance(LayoutRule):
    """.NET: Autodesk.Revit.DB.LayoutRuleFixedDistance"""
    def __init__(self, *args) -> None: ...
    JustifyType: BeamSystemJustifyType
    Spacing: float
    IsReadOnly: bool

class LayoutRuleFixedNumber(LayoutRule):
    """.NET: Autodesk.Revit.DB.LayoutRuleFixedNumber"""
    def __init__(self, *args) -> None: ...
    NumberOfLines: int
    IsReadOnly: bool

class LayoutRuleMaximumSpacing(LayoutRule):
    """.NET: Autodesk.Revit.DB.LayoutRuleMaximumSpacing"""
    def __init__(self, *args) -> None: ...
    Spacing: float
    IsReadOnly: bool

class Leader(APIObject):
    """.NET: Autodesk.Revit.DB.Leader"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LeaderShape: LeaderShape
    Anchor: XYZ
    Elbow: XYZ
    End: XYZ
    IsReadOnly: bool

class LeaderArray(APIObject):
    """.NET: Autodesk.Revit.DB.LeaderArray"""
    def __init__(self, *args) -> None: ...
    Item: Leader
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: Leader) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> LeaderArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: Leader, index: int) -> None: ...
    def ReverseIterator(self, ) -> LeaderArrayIterator: ...

class LeaderArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.LeaderArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class LeaderAtachement:
    """.NET: Autodesk.Revit.DB.LeaderAtachement"""
    def __init__(self, *args) -> None: ...
    ...

class LeaderEndCondition:
    """.NET: Autodesk.Revit.DB.LeaderEndCondition"""
    def __init__(self, *args) -> None: ...
    ...

class LeaderShape:
    """.NET: Autodesk.Revit.DB.LeaderShape"""
    def __init__(self, *args) -> None: ...
    ...

class LeaderStartCondition:
    """.NET: Autodesk.Revit.DB.LeaderStartCondition"""
    def __init__(self, *args) -> None: ...
    ...

class LeadersPresentationMode:
    """.NET: Autodesk.Revit.DB.LeadersPresentationMode"""
    def __init__(self, *args) -> None: ...
    ...

class Level(DatumPlane):
    """.NET: Autodesk.Revit.DB.Level"""
    def __init__(self, *args) -> None: ...
    ProjectElevation: float
    Elevation: float
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
    def Create(document: Document, elevation: float) -> Level: ...
    def FindAssociatedPlanViewId(self, ) -> ElementId: ...
    @staticmethod
    def GetNearestLevelId(document: Document, elevation: float, offset: float) -> ElementId: ...
    def GetPlaneReference(self, ) -> Reference: ...

class LevelAssociationData:
    """.NET: Autodesk.Revit.DB.LevelAssociationData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetAssociatedLevel(self, ) -> ElementId: ...
    @staticmethod
    def GetLevelAssociationData(element: Element) -> LevelAssociationData: ...
    def GetLevelOffset(self, ) -> float: ...
    def SetAssociatedLevel(self, levelId: ElementId) -> None: ...

class LevelType(LineAndTextAttrSymbol):
    """.NET: Autodesk.Revit.DB.LevelType"""
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

class LightAndMaterialAccuracyMode:
    """.NET: Autodesk.Revit.DB.LightAndMaterialAccuracyMode"""
    def __init__(self, *args) -> None: ...
    ...

class LightNode(ContentNode):
    """.NET: Autodesk.Revit.DB.LightNode"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    NodeName: str

class LightingSource:
    """.NET: Autodesk.Revit.DB.LightingSource"""
    def __init__(self, *args) -> None: ...
    ...

class Line(Curve):
    """.NET: Autodesk.Revit.DB.Line"""
    def __init__(self, *args) -> None: ...
    Direction: XYZ
    Origin: XYZ
    Period: float
    IsCyclic: bool
    Length: float
    ApproximateLength: float
    Reference: Reference
    IsClosed: bool
    IsBound: bool
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool
    @staticmethod
    def CreateBound(endpoint1: XYZ, endpoint2: XYZ) -> Line: ...
    @staticmethod
    def CreateUnbound(origin: XYZ, direction: XYZ) -> Line: ...

class LineAndTextAttrSymbol(ElementType):
    """.NET: Autodesk.Revit.DB.LineAndTextAttrSymbol"""
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

class LinePattern:
    """.NET: Autodesk.Revit.DB.LinePattern"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Name: str
    def Dispose(self, ) -> None: ...
    def GetSegments(self, ) -> IList: ...
    def SetSegments(self, lineSegs: IList) -> None: ...

class LinePatternElement(Element):
    """.NET: Autodesk.Revit.DB.LinePatternElement"""
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
    def Create(document: Document, linePattern: LinePattern) -> LinePatternElement: ...
    @staticmethod
    def GetLinePattern(document: Document, elementId: ElementId) -> LinePattern: ...
    @staticmethod
    def GetLinePatternElementByName(document: Document, name: str) -> LinePatternElement: ...
    @staticmethod
    def GetSolidPatternId() -> ElementId: ...
    def SetLinePattern(self, newLinePattern: LinePattern) -> None: ...

class LinePatternSegment:
    """.NET: Autodesk.Revit.DB.LinePatternSegment"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Length: float
    Type: LinePatternSegmentType
    def Dispose(self, ) -> None: ...

class LinePatternSegmentType:
    """.NET: Autodesk.Revit.DB.LinePatternSegmentType"""
    def __init__(self, *args) -> None: ...
    ...

class LineProperties:
    """.NET: Autodesk.Revit.DB.LineProperties"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    PatternId: ElementId
    LineWidth: float
    Transparency: int
    Color: Color
    def Dispose(self, ) -> None: ...

class LineScaling:
    """.NET: Autodesk.Revit.DB.LineScaling"""
    def __init__(self, *args) -> None: ...
    ...

class LineSegment:
    """.NET: Autodesk.Revit.DB.LineSegment"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LineProperties: LineProperties
    EndParameter: float
    StartParameter: float
    EndPoint: XYZ
    StartPoint: XYZ
    def Dispose(self, ) -> None: ...

class LinearArray(BaseArray):
    """.NET: Autodesk.Revit.DB.LinearArray"""
    def __init__(self, *args) -> None: ...
    NumMembers: int
    Label: FamilyParameter
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
    def ArrayElementWithoutAssociation(aDoc: Document, dBView: View, id: ElementId, count: int, translationToAnchorMember: XYZ, anchorMember: ArrayAnchorMember) -> ICollection: ...
    @staticmethod
    def ArrayElementsWithoutAssociation(aDoc: Document, dBView: View, ids: ICollection, count: int, translationToAnchorMember: XYZ, anchorMember: ArrayAnchorMember) -> ICollection: ...
    @staticmethod
    def Create(aDoc: Document, dBView: View, id: ElementId, count: int, translationToAnchorMember: XYZ, anchorMember: ArrayAnchorMember) -> LinearArray: ...
    def GetCopiedMemberIds(self, ) -> ICollection: ...
    @staticmethod
    def GetMinimumSize(document: Document) -> int: ...
    def GetNumberOfMembersIncludingPlaceholders(self, ) -> int: ...
    def GetOriginalMemberIds(self, ) -> ICollection: ...
    @staticmethod
    def IsElementArrayable(aDoc: Document, id: ElementId) -> bool: ...
    @staticmethod
    def IsValidNumberOfMembers(count: int, pADoc: Document) -> bool: ...

class LinearDimension(Dimension):
    """.NET: Autodesk.Revit.DB.LinearDimension"""
    def __init__(self, *args) -> None: ...
    IsValid: bool
    AreReferencesAvailable: bool
    TextPosition: XYZ
    Origin: XYZ
    LeaderEndPosition: XYZ
    HasLeader: bool
    ValueOverride: str
    Below: str
    Above: str
    Suffix: str
    Prefix: str
    IsLocked: bool
    ValueString: str
    Value: Nullable
    AreSegmentsEqual: bool
    Segments: DimensionSegmentArray
    NumberOfSegments: int
    DimensionShape: DimensionShape
    FamilyLabel: FamilyParameter
    Name: str
    DimensionType: DimensionType
    View: View
    Curve: Curve
    References: ReferenceArray
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
    def Create(document: Document, dbView: View, line: Line, references: IList) -> LinearDimension: ...

class LinkConversionData:
    """.NET: Autodesk.Revit.DB.LinkConversionData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Path: str
    ServerId: Guid
    def Dispose(self, ) -> None: ...
    def GetOptions(self, ) -> IDictionary: ...

class LinkElementId:
    """.NET: Autodesk.Revit.DB.LinkElementId"""
    def __init__(self, *args) -> None: ...
    HostElementId: ElementId
    LinkedElementId: ElementId
    LinkInstanceId: ElementId
    def Equals(self, obj: object) -> bool: ...

class LinkLoadContent(ExternalResourceLoadContent):
    """.NET: Autodesk.Revit.DB.LinkLoadContent"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LoadStatus: ExternalResourceLoadStatus
    Version: str
    def GetLinkDataPath(self, ) -> ModelPath: ...
    def GetLinkLoadResult(self, ) -> LinkLoadResult: ...
    def SetLinkDataPath(self, linkPath: ModelPath) -> None: ...

class LinkLoadResult:
    """.NET: Autodesk.Revit.DB.LinkLoadResult"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LoadResult: LinkLoadResultType
    IsNested: bool
    IsCircularLink: bool
    ElementId: ElementId
    def Dispose(self, ) -> None: ...
    def GetCentralModelName(self, ) -> ModelPath: ...
    def GetExternalResourceReference(self, ) -> ExternalResourceReference: ...
    def GetExternalResourceReferencesFromFailedLoads(self, ) -> IList: ...
    def GetLinkLoadResult(self, matchExtResRef: ExternalResourceReference) -> LinkLoadResult: ...
    def GetModelName(self, ) -> ModelPath: ...
    def GetNestedLinkLoadResults(self, ) -> IDictionary: ...
    def GetParentModelName(self, ) -> ModelPath: ...
    @staticmethod
    def IsCodeSuccess(code: LinkLoadResultType) -> bool: ...

class LinkLoadResultType:
    """.NET: Autodesk.Revit.DB.LinkLoadResultType"""
    def __init__(self, *args) -> None: ...
    ...

class LinkNode(GroupNode):
    """.NET: Autodesk.Revit.DB.LinkNode"""
    def __init__(self, *args) -> None: ...
    SymbolId: ElementId
    IsValidObject: bool
    NodeName: str
    def GetDocument(self, ) -> Document: ...

class LinkOperations:
    """.NET: Autodesk.Revit.DB.LinkOperations"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def SetOnLocalLinkSharedCoordinatesSavedCallback(self, onLocalLinkSharedCoordinatesSaved: IOnLocalLinkSharedCoordinatesSavedCallback) -> None: ...

class LinkOriginFileType:
    """.NET: Autodesk.Revit.DB.LinkOriginFileType"""
    def __init__(self, *args) -> None: ...
    ...

class LinkVisibility:
    """.NET: Autodesk.Revit.DB.LinkVisibility"""
    def __init__(self, *args) -> None: ...
    ...

class LinkedFileStatus:
    """.NET: Autodesk.Revit.DB.LinkedFileStatus"""
    def __init__(self, *args) -> None: ...
    ...

class ListType:
    """.NET: Autodesk.Revit.DB.ListType"""
    def __init__(self, *args) -> None: ...
    ...

class LoadOperationType:
    """.NET: Autodesk.Revit.DB.LoadOperationType"""
    def __init__(self, *args) -> None: ...
    ...

class LoadedFamilyIntegrityCheck:
    """.NET: Autodesk.Revit.DB.LoadedFamilyIntegrityCheck"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CheckAllFamilies(ADoc: Document, corruptFamilyIds: ISet) -> bool: ...
    @staticmethod
    def CheckAllFamiliesSlow(ADoc: Document, corruptFamilyIds: ISet) -> bool: ...
    @staticmethod
    def CheckFamily(ADoc: Document, familyId: ElementId) -> bool: ...

class Location(APIObject):
    """.NET: Autodesk.Revit.DB.Location"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool
    def Move(self, translation: XYZ) -> bool: ...
    def Rotate(self, axis: Line, angle: float) -> bool: ...

class LocationCurve(Location):
    """.NET: Autodesk.Revit.DB.LocationCurve"""
    def __init__(self, *args) -> None: ...
    JoinType: JoinType
    ElementsAtJoin: ElementArray
    Curve: Curve
    IsReadOnly: bool

class LocationPoint(Location):
    """.NET: Autodesk.Revit.DB.LocationPoint"""
    def __init__(self, *args) -> None: ...
    Rotation: float
    Point: XYZ
    IsReadOnly: bool

class LogicalAndFilter(ElementLogicalFilter):
    """.NET: Autodesk.Revit.DB.LogicalAndFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool

class LogicalOrFilter(ElementLogicalFilter):
    """.NET: Autodesk.Revit.DB.LogicalOrFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool

class MEPAnalyticalConnection(MEPCurve):
    """.NET: Autodesk.Revit.DB.MEPAnalyticalConnection"""
    def __init__(self, *args) -> None: ...
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
    def CanSupportAnalyticalConnection(connector: Connector) -> bool: ...
    @staticmethod
    def Create(doc: Document, typeId: ElementId, startConnector: Connector, endConnector: Connector) -> MEPAnalyticalConnection: ...
    @staticmethod
    def CreateMultipleConnections(doc: Document, typeId: ElementId, equipmentOpenConnectors: IList, curveIdsToConnect: IList) -> ISet: ...
    def GetFlow(self, ) -> float: ...

class MEPAnalyticalConnectionType(ElementType):
    """.NET: Autodesk.Revit.DB.MEPAnalyticalConnectionType"""
    def __init__(self, *args) -> None: ...
    PressureLoss: float
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
    def Create(doc: Document, name: str) -> MEPAnalyticalConnectionType: ...
    @staticmethod
    def FindTypeByName(doc: Document, name: str) -> ElementId: ...
    @staticmethod
    def IsNameUnused(doc: Document, name: str) -> bool: ...

class MEPCalculationServerInfo:
    """.NET: Autodesk.Revit.DB.MEPCalculationServerInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    PipeUseDefinitionOnTypeGUID: Guid
    Description: str
    ServerName: str
    ServerId: Guid
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetMEPCalculationServerInfo(famInst: FamilyInstance) -> MEPCalculationServerInfo: ...

class MEPConnectorInfo:
    """.NET: Autodesk.Revit.DB.MEPConnectorInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LinkedConnector: Connector
    IsSecondary: bool
    IsPrimary: bool
    def Dispose(self, ) -> None: ...

class MEPCurve(HostObject):
    """.NET: Autodesk.Revit.DB.MEPCurve"""
    def __init__(self, *args) -> None: ...
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

class MEPCurveType(HostObjAttributes):
    """.NET: Autodesk.Revit.DB.MEPCurveType"""
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

class MEPFamilyConnectorInfo(MEPConnectorInfo):
    """.NET: Autodesk.Revit.DB.MEPFamilyConnectorInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LinkedConnector: Connector
    IsSecondary: bool
    IsPrimary: bool
    def GetAssociateFamilyParameterId(self, connectorParameterId: ElementId) -> ElementId: ...
    def GetConnectorParameterValue(self, connectorParameterId: ElementId) -> ParameterValue: ...

class MEPModel(APIObject):
    """.NET: Autodesk.Revit.DB.MEPModel"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ConnectorManager: ConnectorManager
    IsReadOnly: bool
    def GetAssignedElectricalSystems(self, ) -> ISet: ...
    def GetElectricalSystems(self, ) -> ISet: ...

class MEPSize:
    """.NET: Autodesk.Revit.DB.MEPSize"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    UsedInSizing: bool
    UsedInSizeLists: bool
    OuterDiameter: float
    InnerDiameter: float
    NominalDiameter: float
    def Dispose(self, ) -> None: ...

class MEPSupportUtils:
    """.NET: Autodesk.Revit.DB.MEPSupportUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CreateDuctworkStiffener(document: Document, familySymbolId: ElementId, hostId: ElementId, distanceFromHostEnd: float) -> FamilyInstance: ...

class MEPSystem(Element):
    """.NET: Autodesk.Revit.DB.MEPSystem"""
    def __init__(self, *args) -> None: ...
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
    def Add(self, connectors: ConnectorSet) -> None: ...
    def DivideSystem(self, ADoc: Document) -> ICollection: ...
    def GetCriticalPathSectionNumbers(self, ) -> IList: ...
    def GetPhysicalNetworksNumber(self, ) -> int: ...
    def GetSectionByIndex(self, index: int) -> MEPSection: ...
    def GetSectionByNumber(self, sectionNumber: int) -> MEPSection: ...
    def IsSystemDividable(self, ) -> bool: ...
    def Remove(self, elementIds: ICollection) -> None: ...

class MEPSystemClassification:
    """.NET: Autodesk.Revit.DB.MEPSystemClassification"""
    def __init__(self, *args) -> None: ...
    ...

class MEPSystemType(ElementType):
    """.NET: Autodesk.Revit.DB.MEPSystemType"""
    def __init__(self, *args) -> None: ...
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

class MarginType:
    """.NET: Autodesk.Revit.DB.MarginType"""
    def __init__(self, *args) -> None: ...
    ...

class MassDisplayTemporaryOverrideType:
    """.NET: Autodesk.Revit.DB.MassDisplayTemporaryOverrideType"""
    def __init__(self, *args) -> None: ...
    ...

class MassInstanceUtils:
    """.NET: Autodesk.Revit.DB.MassInstanceUtils"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    @staticmethod
    def AddMassLevelDataToMassInstance(document: Document, massInstanceId: ElementId, levelId: ElementId) -> ElementId: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetGrossFloorArea(document: Document, massInstanceId: ElementId) -> float: ...
    @staticmethod
    def GetGrossSurfaceArea(document: Document, massInstanceId: ElementId) -> float: ...
    @staticmethod
    def GetGrossVolume(document: Document, massInstanceId: ElementId) -> float: ...
    @staticmethod
    def GetJoinedElementIds(document: Document, massInstanceId: ElementId) -> IList: ...
    @staticmethod
    def GetMassLevelDataIds(document: Document, massInstanceId: ElementId) -> IList: ...
    @staticmethod
    def GetMassLevelIds(document: Document, massInstanceId: ElementId) -> IList: ...
    @staticmethod
    def RemoveMassLevelDataFromMassInstance(document: Document, massInstanceId: ElementId, levelId: ElementId) -> None: ...

class Material(Element):
    """.NET: Autodesk.Revit.DB.Material"""
    def __init__(self, *args) -> None: ...
    MaterialCategory: str
    MaterialClass: str
    EmbodiedCarbonAssetId: ElementId
    ThermalAssetId: ElementId
    StructuralAssetId: ElementId
    AppearanceAssetId: ElementId
    SurfaceBackgroundPatternId: ElementId
    CutBackgroundPatternId: ElementId
    SurfaceForegroundPatternId: ElementId
    CutForegroundPatternId: ElementId
    CutBackgroundPatternColor: Color
    SurfaceBackgroundPatternColor: Color
    CutForegroundPatternColor: Color
    SurfaceForegroundPatternColor: Color
    Color: Color
    Transparency: int
    Smoothness: int
    Shininess: int
    UseRenderAppearanceForShading: bool
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
    def ClearMaterialAspect(self, aspect: MaterialAspect) -> None: ...
    @staticmethod
    def Create(document: Document, name: str) -> ElementId: ...
    def Duplicate(self, name: str) -> Material: ...
    @staticmethod
    def GetIdentityParameterIds() -> IList: ...
    @staticmethod
    def IsMaterialOrValidDefault(pElem: Element, materialId: ElementId) -> bool: ...
    @staticmethod
    def IsNameUnique(aDocument: Document, name: str) -> bool: ...
    def SetMaterialAspectByPropertySet(self, aspect: MaterialAspect, propertySetId: ElementId) -> None: ...

class MaterialAspect:
    """.NET: Autodesk.Revit.DB.MaterialAspect"""
    def __init__(self, *args) -> None: ...
    ...

class MaterialFunctionAssignment:
    """.NET: Autodesk.Revit.DB.MaterialFunctionAssignment"""
    def __init__(self, *args) -> None: ...
    ...

class MaterialNode(RenderNode):
    """.NET: Autodesk.Revit.DB.MaterialNode"""
    def __init__(self, *args) -> None: ...
    ThumbnailFile: str
    Glossiness: int
    Smoothness: int
    Color: Color
    Transparency: float
    MaterialId: ElementId
    HasOverriddenAppearance: bool
    IsValidObject: bool
    NodeName: str
    def GetAppearance(self, ) -> Asset: ...
    def GetAppearanceOverride(self, ) -> Asset: ...

class MaterialPropertyPathType:
    """.NET: Autodesk.Revit.DB.MaterialPropertyPathType"""
    def __init__(self, *args) -> None: ...
    ...

class MathComparisonUtils:
    """.NET: Autodesk.Revit.DB.MathComparisonUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def IsAlmostEqual(value1: float, value2: float) -> bool: ...
    @staticmethod
    def IsAlmostZero(value: float) -> bool: ...
    @staticmethod
    def IsGreaterThan(value1: float, value2: float) -> bool: ...
    @staticmethod
    def IsGreaterThanOrAlmostEqual(value1: float, value2: float) -> bool: ...
    @staticmethod
    def IsLessThan(value1: float, value2: float) -> bool: ...
    @staticmethod
    def IsLessThanOrAlmostEqual(value1: float, value2: float) -> bool: ...

class Mesh(GeometryObject):
    """.NET: Autodesk.Revit.DB.Mesh"""
    def __init__(self, *args) -> None: ...
    IsClosed: bool
    DistributionOfNormals: DistributionOfNormals
    NumberOfNormals: int
    Transformed: Mesh
    MaterialElementId: ElementId
    Vertices: IList
    Triangle: MeshTriangle
    NumTriangles: int
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool
    def ComputeSurfaceArea(self, ) -> float: ...
    def GetNormal(self, idx: int) -> XYZ: ...
    def GetNormals(self, ) -> IList: ...

class MeshFromGeometryOperationIssue:
    """.NET: Autodesk.Revit.DB.MeshFromGeometryOperationIssue"""
    def __init__(self, *args) -> None: ...
    ...

class MeshFromGeometryOperationResult:
    """.NET: Autodesk.Revit.DB.MeshFromGeometryOperationResult"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsMeshAvailable: bool
    Tessellated: bool
    HasInvalidData: bool
    def Dispose(self, ) -> None: ...
    def GetIssues(self, ) -> IList: ...
    def GetMesh(self, ) -> Mesh: ...

class MeshTriangle:
    """.NET: Autodesk.Revit.DB.MeshTriangle"""
    def __init__(self, *args) -> None: ...
    Vertex: XYZ
    Index: int

class ModelArc(ModelCurve):
    """.NET: Autodesk.Revit.DB.ModelArc"""
    def __init__(self, *args) -> None: ...
    IsReferenceLine: bool
    TrussCurveType: TrussCurveType
    Subcategory: GraphicsStyle
    SupportsTangentLocks: bool
    CurveElementType: CurveElementType
    LineStyle: Element
    SketchPlane: SketchPlane
    CenterPointReference: Reference
    GeometryCurve: Curve
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

class ModelCurve(CurveElement):
    """.NET: Autodesk.Revit.DB.ModelCurve"""
    def __init__(self, *args) -> None: ...
    IsReferenceLine: bool
    TrussCurveType: TrussCurveType
    Subcategory: GraphicsStyle
    SupportsTangentLocks: bool
    CurveElementType: CurveElementType
    LineStyle: Element
    SketchPlane: SketchPlane
    CenterPointReference: Reference
    GeometryCurve: Curve
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
    def ChangeToReferenceLine(self, ) -> None: ...
    def GetVisibility(self, ) -> FamilyElementVisibility: ...
    def SetVisibility(self, visibility: FamilyElementVisibility) -> None: ...

class ModelCurveArrArray(APIObject):
    """.NET: Autodesk.Revit.DB.ModelCurveArrArray"""
    def __init__(self, *args) -> None: ...
    Item: ModelCurveArray
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: ModelCurveArray) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> ModelCurveArrArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: ModelCurveArray, index: int) -> None: ...
    def ReverseIterator(self, ) -> ModelCurveArrArrayIterator: ...

class ModelCurveArrArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.ModelCurveArrArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ModelCurveArray(APIObject):
    """.NET: Autodesk.Revit.DB.ModelCurveArray"""
    def __init__(self, *args) -> None: ...
    Item: ModelCurve
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: ModelCurve) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> ModelCurveArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: ModelCurve, index: int) -> None: ...
    def ReverseIterator(self, ) -> ModelCurveArrayIterator: ...

class ModelCurveArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.ModelCurveArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ModelCurveNode(RenderNode):
    """.NET: Autodesk.Revit.DB.ModelCurveNode"""
    def __init__(self, *args) -> None: ...
    LineProperties: LineProperties
    IsValidObject: bool
    NodeName: str

class ModelEllipse(ModelCurve):
    """.NET: Autodesk.Revit.DB.ModelEllipse"""
    def __init__(self, *args) -> None: ...
    IsReferenceLine: bool
    TrussCurveType: TrussCurveType
    Subcategory: GraphicsStyle
    SupportsTangentLocks: bool
    CurveElementType: CurveElementType
    LineStyle: Element
    SketchPlane: SketchPlane
    CenterPointReference: Reference
    GeometryCurve: Curve
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

class ModelHermiteSpline(ModelCurve):
    """.NET: Autodesk.Revit.DB.ModelHermiteSpline"""
    def __init__(self, *args) -> None: ...
    IsReferenceLine: bool
    TrussCurveType: TrussCurveType
    Subcategory: GraphicsStyle
    SupportsTangentLocks: bool
    CurveElementType: CurveElementType
    LineStyle: Element
    SketchPlane: SketchPlane
    CenterPointReference: Reference
    GeometryCurve: Curve
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

class ModelLine(ModelCurve):
    """.NET: Autodesk.Revit.DB.ModelLine"""
    def __init__(self, *args) -> None: ...
    IsReferenceLine: bool
    TrussCurveType: TrussCurveType
    Subcategory: GraphicsStyle
    SupportsTangentLocks: bool
    CurveElementType: CurveElementType
    LineStyle: Element
    SketchPlane: SketchPlane
    CenterPointReference: Reference
    GeometryCurve: Curve
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

class ModelNurbSpline(ModelCurve):
    """.NET: Autodesk.Revit.DB.ModelNurbSpline"""
    def __init__(self, *args) -> None: ...
    IsReferenceLine: bool
    TrussCurveType: TrussCurveType
    Subcategory: GraphicsStyle
    SupportsTangentLocks: bool
    CurveElementType: CurveElementType
    LineStyle: Element
    SketchPlane: SketchPlane
    CenterPointReference: Reference
    GeometryCurve: Curve
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

class ModelPath:
    """.NET: Autodesk.Revit.DB.ModelPath"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Region: str
    CloudPath: bool
    ServerPath: bool
    Empty: bool
    CentralServerPath: str
    def Compare(self, otherPath: ModelPath) -> int: ...
    def Dispose(self, ) -> None: ...
    def GetModelGUID(self, ) -> Guid: ...
    def GetProjectGUID(self, ) -> Guid: ...

class ModelPathUtils:
    """.NET: Autodesk.Revit.DB.ModelPathUtils"""
    def __init__(self, *args) -> None: ...
    CloudRegionEMEA: str
    CloudRegionUS: str
    @staticmethod
    def ConvertCloudGUIDsToCloudPath(region: str, projectGuid: Guid, modelGuid: Guid) -> ModelPath: ...
    @staticmethod
    def ConvertModelPathToUserVisiblePath(path: ModelPath) -> str: ...
    @staticmethod
    def ConvertUserVisiblePathToModelPath(strPath: str) -> ModelPath: ...
    @staticmethod
    def GetAllCloudRegions() -> IList: ...
    @staticmethod
    def IsValidUserVisibleFullServerPath(strPath: str) -> bool: ...

class ModelText(Element):
    """.NET: Autodesk.Revit.DB.ModelText"""
    def __init__(self, *args) -> None: ...
    Subcategory: Category
    ModelTextType: ModelTextType
    HorizontalAlignment: HorizontalAlign
    Depth: float
    Location: Location
    Text: str
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
    def GetVisibility(self, ) -> FamilyElementVisibility: ...
    def SetVisibility(self, visibility: FamilyElementVisibility) -> None: ...

class ModelTextType(ElementType):
    """.NET: Autodesk.Revit.DB.ModelTextType"""
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

class ModelUpdatesStatus:
    """.NET: Autodesk.Revit.DB.ModelUpdatesStatus"""
    def __init__(self, *args) -> None: ...
    ...

class ModifierType:
    """.NET: Autodesk.Revit.DB.ModifierType"""
    def __init__(self, *args) -> None: ...
    ...

class Mullion(FamilyInstance):
    """.NET: Autodesk.Revit.DB.Mullion"""
    def __init__(self, *args) -> None: ...
    LocationCurve: Curve
    MullionType: MullionType
    Lockable: bool
    Lock: bool
    HasSpatialElementFromToCalculationPoints: bool
    HasSpatialElementCalculationPoint: bool
    IsWorkPlaneFlipped: bool
    CanFlipWorkPlane: bool
    IsSlantedColumn: bool
    ExtensionUtility: IExtension
    SuperComponent: Element
    ToRoom: Room
    ToRoom: Room
    FromRoom: Room
    FromRoom: Room
    CanSplit: bool
    CanRotate: bool
    CanFlipFacing: bool
    CanFlipHand: bool
    Mirrored: bool
    Invisible: bool
    FacingFlipped: bool
    HandFlipped: bool
    FacingOrientation: XYZ
    HandOrientation: XYZ
    HostFace: Reference
    HostParameter: float
    Host: Element
    Location: Location
    Space: Space
    Space: Space
    Room: Room
    Room: Room
    StructuralType: StructuralType
    StructuralUsage: StructuralInstanceUsage
    StructuralMaterialId: ElementId
    StructuralMaterialType: StructuralMaterialType
    MEPModel: MEPModel
    Symbol: FamilySymbol
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
    def BreakMullion(self, ) -> None: ...
    def JoinMullion(self, ) -> None: ...

class MullionType(FamilySymbol):
    """.NET: Autodesk.Revit.DB.MullionType"""
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

class MullionTypeSet(APIObject):
    """.NET: Autodesk.Revit.DB.MullionTypeSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: MullionType) -> bool: ...
    def Erase(self, item: MullionType) -> int: ...
    def ForwardIterator(self, ) -> MullionTypeSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: MullionType) -> bool: ...
    def ReverseIterator(self, ) -> MullionTypeSetIterator: ...

class MullionTypeSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.MullionTypeSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class MultiReferenceAnnotation(Element):
    """.NET: Autodesk.Revit.DB.MultiReferenceAnnotation"""
    def __init__(self, *args) -> None: ...
    TagId: ElementId
    DimensionId: ElementId
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
    def AreElementsValidForMultiReferenceAnnotation(document: Document, options: MultiReferenceAnnotationOptions) -> bool: ...
    @staticmethod
    def AreReferencesValidForLinearDimension(document: Document, ownerViewId: ElementId, options: MultiReferenceAnnotationOptions) -> bool: ...
    @staticmethod
    def AreReferencesValidForLinearFixedDimension(document: Document, ownerViewId: ElementId, options: MultiReferenceAnnotationOptions) -> bool: ...
    @staticmethod
    def Create(document: Document, ownerViewId: ElementId, options: MultiReferenceAnnotationOptions) -> MultiReferenceAnnotation: ...
    @staticmethod
    def Is3DViewValidForDimension(document: Document, ownerViewId: ElementId, options: MultiReferenceAnnotationOptions) -> bool: ...
    @staticmethod
    def IsLinearFixedDimensionDirectionValid(document: Document, viewId: ElementId, options: MultiReferenceAnnotationOptions) -> bool: ...

class MultiReferenceAnnotationOptions:
    """.NET: Autodesk.Revit.DB.MultiReferenceAnnotationOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    TagHasLeader: bool
    TagHeadPosition: XYZ
    DimensionStyleType: DimensionStyleType
    DimensionLineOrigin: XYZ
    DimensionLineDirection: XYZ
    DimensionPlaneNormal: XYZ
    MultiReferenceAnnotationType: MultiReferenceAnnotationType
    def Dispose(self, ) -> None: ...
    def ElementsMatchReferenceCategory(self, elements: ICollection) -> bool: ...
    def GetAdditionalReferencesToDimension(self, ) -> IList: ...
    def GetElementsToDimension(self, ) -> ICollection: ...
    def IsAllowedDimensionStyleType(self, dimensionStyleType: DimensionStyleType) -> bool: ...
    def ReferencesDontMatchReferenceCategory(self, references: IList) -> bool: ...
    def SetAdditionalReferencesToDimension(self, referencesToDimension: IList) -> None: ...
    def SetElementsToDimension(self, elementsToDimension: ICollection) -> None: ...

class MultiReferenceAnnotationType(ElementType):
    """.NET: Autodesk.Revit.DB.MultiReferenceAnnotationType"""
    def __init__(self, *args) -> None: ...
    DimensionStyleId: ElementId
    ShowDimensionText: bool
    GroupTagHeads: bool
    TagTypeId: ElementId
    ReferenceCategoryId: ElementId
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
    def CreateDefault(document: Document) -> MultiReferenceAnnotationType: ...
    def GetAllowedTagCategory(self, ) -> ElementId: ...
    def IsAllowedDimensionStyle(self, dimensionStyleId: ElementId) -> bool: ...
    def IsAllowedReferenceCategory(self, referenceCategoryId: ElementId) -> bool: ...
    @staticmethod
    def IsAllowedTagCategory(tagCategoryId: ElementId) -> bool: ...
    def IsAllowedTagType(self, tagTypeId: ElementId) -> bool: ...

class MultiSegmentGrid(Element):
    """.NET: Autodesk.Revit.DB.MultiSegmentGrid"""
    def __init__(self, *args) -> None: ...
    Text: str
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
    def AreGridsInSameMultiSegmentGrid(grid1: Grid, grid2: Grid) -> bool: ...
    @staticmethod
    def Create(document: Document, typeId: ElementId, curveLoop: CurveLoop, sketchPlaneId: ElementId) -> ElementId: ...
    def GetGridIds(self, ) -> ICollection: ...
    @staticmethod
    def GetMultiSegementGridId(grid: Grid) -> ElementId: ...
    @staticmethod
    def IsValidCurveLoop(curveLoop: CurveLoop) -> bool: ...
    @staticmethod
    def IsValidSketchPlaneId(document: Document, elemId: ElementId) -> bool: ...

class MultipleValuesIndicationSettings(Element):
    """.NET: Autodesk.Revit.DB.MultipleValuesIndicationSettings"""
    def __init__(self, *args) -> None: ...
    Value: str
    CustomValue: str
    Custom: bool
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
    def GetMultipleValuesIndicationSettings(cda: Document) -> MultipleValuesIndicationSettings: ...

class NamingUtils:
    """.NET: Autodesk.Revit.DB.NamingUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CompareNames(nameA: str, nameB: str) -> int: ...
    @staticmethod
    def IsValidName(string: str) -> bool: ...

class NavisworksCoordinates:
    """.NET: Autodesk.Revit.DB.NavisworksCoordinates"""
    def __init__(self, *args) -> None: ...
    ...

class NavisworksExportOptions:
    """.NET: Autodesk.Revit.DB.NavisworksExportOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ConvertLinkedCADFormats: bool
    ConvertLights: bool
    FacetingFactor: float
    DivideFileIntoLevels: bool
    ConvertElementProperties: bool
    FindMissingMaterials: bool
    ExportRoomGeometry: bool
    ViewId: ElementId
    ExportScope: NavisworksExportScope
    Coordinates: NavisworksCoordinates
    ExportUrls: bool
    ExportRoomAsAttribute: bool
    ExportLinks: bool
    Parameters: NavisworksParameters
    ExportElementIds: bool
    ExportParts: bool
    def Dispose(self, ) -> None: ...
    def GetSelectedElementIds(self, ) -> ICollection: ...
    def SetSelectedElementIds(self, ids: ICollection) -> None: ...

class NavisworksExportScope:
    """.NET: Autodesk.Revit.DB.NavisworksExportScope"""
    def __init__(self, *args) -> None: ...
    ...

class NavisworksParameters:
    """.NET: Autodesk.Revit.DB.NavisworksParameters"""
    def __init__(self, *args) -> None: ...
    ...

class NestedFamilyTypeReference(Element):
    """.NET: Autodesk.Revit.DB.NestedFamilyTypeReference"""
    def __init__(self, *args) -> None: ...
    TypeName: str
    FamilyName: str
    CategoryId: ElementId
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

class NullParameterValue(ParameterValue):
    """.NET: Autodesk.Revit.DB.NullParameterValue"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class NumberSystem(Element):
    """.NET: Autodesk.Revit.DB.NumberSystem"""
    def __init__(self, *args) -> None: ...
    JustifyOption: NumberSystemJustifyOption
    NumberOrientation: TagOrientation
    NumberDisplayRule: NumberSystemDisplayRule
    NumberedElementId: LinkElementId
    PlacementLevelId: LinkElementId
    JustifyOffset: float
    ReferenceOffset: float
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
    def Create(document: Document, viewId: ElementId, hostElementId: LinkElementId, referenceOption: StairsNumberSystemReferenceOption, placementLevelId: LinkElementId) -> NumberSystem: ...
    def GetReferencePick(self, ) -> Reference: ...
    def SetReferencePick(self, referencePick: Reference) -> None: ...

class NumberSystemDisplayRule:
    """.NET: Autodesk.Revit.DB.NumberSystemDisplayRule"""
    def __init__(self, *args) -> None: ...
    ...

class NumberSystemJustifyOption:
    """.NET: Autodesk.Revit.DB.NumberSystemJustifyOption"""
    def __init__(self, *args) -> None: ...
    ...

class NumberedReferenceInfo:
    """.NET: Autodesk.Revit.DB.NumberedReferenceInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Value: int
    FormattedNumber: str
    NumberingParameterId: ElementId
    PartitionName: str
    NumberingSchemaId: ElementId
    NumberingSchemaName: str
    def Dispose(self, ) -> None: ...
    def GetReference(self, ) -> Reference: ...

class NumberingFormatSettings:
    """.NET: Autodesk.Revit.DB.NumberingFormatSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    NumberOfParameters: int
    FirstNumberFormattingOption: FirstNumberFormattingOptions
    UppercaseCharacters: bool
    AsCharacters: bool
    MinimumNumberOfDigits: int
    def Dispose(self, ) -> None: ...
    def GetParameter(self, index: int) -> NumberingFormattedParameter: ...
    def GetParameters(self, ) -> IList: ...
    def RemoveParameter(self, index: int) -> None: ...
    def SetParameter(self, formattingParameter: NumberingFormattedParameter, index: int) -> None: ...
    def SetParameters(self, formattingParameters: IList) -> None: ...

class NumberingFormattedParameter:
    """.NET: Autodesk.Revit.DB.NumberingFormattedParameter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Separator: str
    Suffix: str
    SampleValue: str
    Prefix: str
    def Dispose(self, ) -> None: ...
    def GetParameter(self, ) -> NumberingParameter: ...
    def SetParameter(self, parameter: NumberingParameter) -> None: ...

class NumberingParameter:
    """.NET: Autodesk.Revit.DB.NumberingParameter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    NumberingParameterType: NumberingParameterType
    ParameterId: ElementId
    def Dispose(self, ) -> None: ...

class NumberingParameterType:
    """.NET: Autodesk.Revit.DB.NumberingParameterType"""
    def __init__(self, *args) -> None: ...
    ...

class NumberingSchema(Element):
    """.NET: Autodesk.Revit.DB.NumberingSchema"""
    def __init__(self, *args) -> None: ...
    ScopeDefiningFilter: ElementId
    MaximumStartingNumber: int
    SchemaType: NumberingSchemaType
    NumberingParameterId: ElementId
    MatchGeometry: bool
    Priority: int
    Enabled: bool
    HasRoomRelatedParameters: bool
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
    def AddMatchingParameter(self, numberingParameter: NumberingParameter) -> None: ...
    def AddPartitioningParameter(self, partitioningParameter: NumberingParameter) -> None: ...
    def AppendSequence(self, fromPartition: str, toPartition: str) -> None: ...
    def ApplyExternalSorting(self, partition: str, sortedElements: IDictionary) -> None: ...
    def AssignElementsToSequence(self, elementIds: ISet, partitionName: str) -> None: ...
    def CanChangePartitioningValue(self, ) -> bool: ...
    def ChangeNumber(self, partition: str, fromNumber: int, toNumber: int) -> IList: ...
    def ChangePartitioningValue(self, fromPartition: str, newPartition: str) -> None: ...
    @staticmethod
    def Create(aDoc: Document, schemaName: str, numberingParameterId: ElementId, filterId: ElementId, priority: int) -> NumberingSchema: ...
    @staticmethod
    def FilterCompatibleOutputParameters(document: Document, parameters: ISet, categories: ISet, filterId: ElementId) -> ISet: ...
    @staticmethod
    def FilterToNumberableCategories(categories: ISet, document: Document) -> ISet: ...
    @staticmethod
    def GetAvailableParameters(category: ElementId, document: Document) -> ISet: ...
    @staticmethod
    def GetCategoriesWitheBuiltInMatching() -> ISet: ...
    def GetFormatting(self, ) -> NumberingFormatSettings: ...
    def GetMatchingParameters(self, ) -> ICollection: ...
    @staticmethod
    def GetMinimumNumberOfDigits(document: Document) -> int: ...
    def GetNumberOfPartitions(self, ) -> int: ...
    @staticmethod
    def GetNumberingInfoForReferences(document: Document, references: IList) -> IList: ...
    @staticmethod
    def GetNumberingSchema(document: Document, schemaName: str) -> NumberingSchema: ...
    def GetNumberingSequences(self, ) -> IList: ...
    def GetNumberingSequencesInfos(self, ) -> IList: ...
    def GetNumbers(self, partition: str) -> IList: ...
    def GetPartitioningParameters(self, ) -> ICollection: ...
    @staticmethod
    def GetSchemasInDocument(document: Document) -> ISet: ...
    def GetScopeDefiningCategories(self, ) -> ISet: ...
    def GetUseBuiltInMatchingForCategories(self, ) -> ISet: ...
    @staticmethod
    def GetValidCategoriesForNumbering(document: Document) -> ICollection: ...
    @staticmethod
    def IsValidPartitionName(name: str, message: str) -> bool: ...
    def MergeSequences(self, sourcePartitions: IList, newPartition: str) -> None: ...
    def MoveSequence(self, fromPartition: str, newPartition: str) -> None: ...
    def RemoveGaps(self, partition: str) -> None: ...
    def RemoveMatchingParameter(self, numberingParameter: NumberingParameter) -> None: ...
    def RemovePartitioningParameter(self, partitioningParameter: NumberingParameter) -> None: ...
    def SetFormatting(self, formattingSettings: NumberingFormatSettings) -> None: ...
    def SetMatchingParameters(self, matchingParameters: ISet) -> None: ...
    @staticmethod
    def SetMinimumNumberOfDigits(document: Document, value: int) -> None: ...
    def SetPartitioningParameters(self, partitioningParameters: ISet) -> None: ...
    def SetScopeDefiningFilterAndOutputParam(self, filterId: ElementId, numberingParameterId: ElementId) -> None: ...
    def SetUseBuiltInMatchingForCategories(self, categories: ISet) -> None: ...
    def ShiftNumbers(self, partition: str, firstNumber: int) -> None: ...
    def SwapNumber(self, partition: str, firstNumber: int, secondNumber: int) -> IList: ...

class NumberingSchemaType(GuidEnum):
    """.NET: Autodesk.Revit.DB.NumberingSchemaType"""
    def __init__(self, *args) -> None: ...
    Guid: Guid

class NumberingSchemaTypes:
    """.NET: Autodesk.Revit.DB.NumberingSchemaTypes"""
    def __init__(self, *args) -> None: ...
    ...

class NumberingSequenceInfo:
    """.NET: Autodesk.Revit.DB.NumberingSequenceInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class NumericRevisionSettings:
    """.NET: Autodesk.Revit.DB.NumericRevisionSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Suffix: str
    Prefix: str
    MinimumDigits: int
    StartNumber: int
    def Dispose(self, ) -> None: ...
    def IsEqual(self, other: NumericRevisionSettings) -> bool: ...
    def IsValid(self, ) -> bool: ...

class NurbSpline(Curve):
    """.NET: Autodesk.Revit.DB.NurbSpline"""
    def __init__(self, *args) -> None: ...
    Knots: DoubleArray
    Weights: DoubleArray
    CtrlPoints: IList
    Degree: int
    isRational: bool
    Period: float
    IsCyclic: bool
    Length: float
    ApproximateLength: float
    Reference: Reference
    IsClosed: bool
    IsBound: bool
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool
    @staticmethod
    def Create(hermiteSpline: HermiteSpline) -> NurbSpline: ...
    @staticmethod
    def CreateCurve(degree: int, knots: IList, controlPoints: IList, weights: IList) -> Curve: ...
    def SetControlPointsAndWeights(self, ctrlPoints: IList, weights: DoubleArray) -> None: ...

class NurbsSurfaceData:
    """.NET: Autodesk.Revit.DB.NurbsSurfaceData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ReverseOrientation: bool
    IsRational: bool
    DegreeV: int
    DegreeU: int
    @staticmethod
    def Create(degreeU: int, degreeV: int, knotsU: IList, knotsV: IList, controlPoints: IList, weights: IList, bReverseOrientation: bool) -> NurbsSurfaceData: ...
    def Dispose(self, ) -> None: ...
    def GetControlPoint(self, idx: int) -> XYZ: ...
    def GetControlPoints(self, ) -> IList: ...
    def GetKnotU(self, idx: int) -> float: ...
    def GetKnotV(self, idx: int) -> float: ...
    def GetKnotsU(self, ) -> IList: ...
    def GetKnotsV(self, ) -> IList: ...
    def GetNumberOfControlPoints(self, ) -> int: ...
    def GetNumberOfKnotsU(self, ) -> int: ...
    def GetNumberOfKnotsV(self, ) -> int: ...
    def GetNumberOfWeights(self, ) -> int: ...
    def GetWeight(self, idx: int) -> float: ...
    def GetWeights(self, ) -> IList: ...
    def IsValid(self, ) -> bool: ...

class OBJExportOptions(BIMExportOptions):
    """.NET: Autodesk.Revit.DB.OBJExportOptions"""
    def __init__(self, *args) -> None: ...
    GridAspectRatio: float
    MaxEdgeLength: float
    NormalTolerance: float
    SurfaceTolerance: float
    TargetUnit: ExportUnit
    IsValidObject: bool
    ViewId: ElementId
    def IsGridAspectRatioSet(self, ) -> bool: ...
    def IsMaxEdgeLengthSet(self, ) -> bool: ...
    def IsNormalToleranceSet(self, ) -> bool: ...
    def IsSurfaceToleranceSet(self, ) -> bool: ...
    @staticmethod
    def IsValidForGridAspectRatio(value: float) -> bool: ...
    @staticmethod
    def IsValidForMaxEdgeLength(value: float) -> bool: ...
    @staticmethod
    def IsValidForNormalTolerance(value: float) -> bool: ...
    @staticmethod
    def IsValidForSurfaceTolerance(value: float) -> bool: ...
    def SetTessellationSettings(self, resolutionType: ExportResolution) -> None: ...

class OBJImportOptions(BaseImportOptions):
    """.NET: Autodesk.Revit.DB.OBJImportOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ReferencePoint: XYZ
    AutoCorrectAlmostVHLines: bool
    VisibleLayersOnly: bool
    CustomScale: float
    OrientToView: bool
    ThisViewOnly: bool
    Placement: ImportPlacement
    ColorMode: ImportColorMode
    Unit: ImportUnit

class OffsetSurface(Surface):
    """.NET: Autodesk.Revit.DB.OffsetSurface"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    OrientationMatchesParametricOrientation: bool
    def GetBasisSurface(self, ) -> Surface: ...
    def GetOffsetDistance(self, ) -> float: ...
    def IsOrientationSameAsBasisSurface(self, ) -> bool: ...

class OpenConflictResult:
    """.NET: Autodesk.Revit.DB.OpenConflictResult"""
    def __init__(self, *args) -> None: ...
    ...

class OpenConflictScenario:
    """.NET: Autodesk.Revit.DB.OpenConflictScenario"""
    def __init__(self, *args) -> None: ...
    ...

class OpenForeignOption:
    """.NET: Autodesk.Revit.DB.OpenForeignOption"""
    def __init__(self, *args) -> None: ...
    ...

class OpenOptions:
    """.NET: Autodesk.Revit.DB.OpenOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    OpenForeignOption: OpenForeignOption
    AllowOpeningLocalByWrongUser: bool
    Audit: bool
    IgnoreExtensibleStorageSchemaConflict: bool
    DetachFromCentralOption: DetachFromCentralOption
    def Dispose(self, ) -> None: ...
    def GetOpenWorksetsConfiguration(self, ) -> WorksetConfiguration: ...
    def SetOpenWorksetsConfiguration(self, openConfiguration: WorksetConfiguration) -> None: ...

class Opening(Element):
    """.NET: Autodesk.Revit.DB.Opening"""
    def __init__(self, *args) -> None: ...
    SketchId: ElementId
    IsTransparentInElevation: bool
    IsTransparentIn3D: bool
    Host: Element
    BoundaryCurves: CurveArray
    BoundaryRect: IList
    IsRectBoundary: bool
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

class OpeningWrappingCondition:
    """.NET: Autodesk.Revit.DB.OpeningWrappingCondition"""
    def __init__(self, *args) -> None: ...
    ...

class OptionalFunctionalityUtils:
    """.NET: Autodesk.Revit.DB.OptionalFunctionalityUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def Is3DMImportLinkAvailable() -> bool: ...
    @staticmethod
    def IsAXMImportLinkAvailable() -> bool: ...
    @staticmethod
    def IsDGNExportAvailable() -> bool: ...
    @staticmethod
    def IsDGNImportLinkAvailable() -> bool: ...
    @staticmethod
    def IsDWFExportAvailable() -> bool: ...
    @staticmethod
    def IsDWGExportAvailable() -> bool: ...
    @staticmethod
    def IsDWGImportLinkAvailable() -> bool: ...
    @staticmethod
    def IsDXFExportAvailable() -> bool: ...
    @staticmethod
    def IsFBXExportAvailable() -> bool: ...
    @staticmethod
    def IsGraphicsAvailable() -> bool: ...
    @staticmethod
    def IsIFCAvailable() -> bool: ...
    @staticmethod
    def IsMaterialLibraryAvailable() -> bool: ...
    @staticmethod
    def IsNavisworksExporterAvailable() -> bool: ...
    @staticmethod
    def IsOBJImportLinkAvailable() -> bool: ...
    @staticmethod
    def IsSATImportLinkAvailable() -> bool: ...
    @staticmethod
    def IsSKPImportLinkAvailable() -> bool: ...
    @staticmethod
    def IsSTEPImportLinkAvailable() -> bool: ...
    @staticmethod
    def IsSTLImportLinkAvailable() -> bool: ...
    @staticmethod
    def IsShapeImporterAvailable() -> bool: ...

class Options(APIObject):
    """.NET: Autodesk.Revit.DB.Options"""
    def __init__(self, *args) -> None: ...
    IncludeNonVisibleObjects: bool
    View: View
    ComputeReferences: bool
    DetailLevel: ViewDetailLevel
    IsReadOnly: bool

class OrdinateDimensionLineStyle:
    """.NET: Autodesk.Revit.DB.OrdinateDimensionLineStyle"""
    def __init__(self, *args) -> None: ...
    ...

class OrdinateDimensionSetting:
    """.NET: Autodesk.Revit.DB.OrdinateDimensionSetting"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    OriginVisibility: OrdinateOriginVisibility
    TextPosition: OrdinateTextPosition
    TextOrientation: OrdinateTextOrientation
    DimensionLineStyle: OrdinateDimensionLineStyle
    OriginTickMarkId: ElementId
    DimensionLineLength: float
    def Dispose(self, ) -> None: ...

class OrdinateOriginVisibility:
    """.NET: Autodesk.Revit.DB.OrdinateOriginVisibility"""
    def __init__(self, *args) -> None: ...
    ...

class OrdinateTextOrientation:
    """.NET: Autodesk.Revit.DB.OrdinateTextOrientation"""
    def __init__(self, *args) -> None: ...
    ...

class OrdinateTextPosition:
    """.NET: Autodesk.Revit.DB.OrdinateTextPosition"""
    def __init__(self, *args) -> None: ...
    ...

class Outline:
    """.NET: Autodesk.Revit.DB.Outline"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsEmpty: bool
    MaximumPoint: XYZ
    MinimumPoint: XYZ
    def AddPoint(self, point: XYZ) -> None: ...
    def Contains(self, point: XYZ, tolerance: float) -> bool: ...
    def ContainsOtherOutline(self, otherOutline: Outline, tolerance: float) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetDiagonalLength(self, ) -> float: ...
    def Intersects(self, outline: Outline, tolerance: float) -> bool: ...
    def IsScaleValid(self, scale: float) -> bool: ...
    def Scale(self, scale: float) -> None: ...

class OverrideGraphicSettings:
    """.NET: Autodesk.Revit.DB.OverrideGraphicSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    InvalidPenNumber: int
    CutBackgroundPatternId: ElementId
    CutForegroundPatternId: ElementId
    SurfaceBackgroundPatternId: ElementId
    SurfaceForegroundPatternId: ElementId
    CutBackgroundPatternColor: Color
    CutForegroundPatternColor: Color
    SurfaceBackgroundPatternColor: Color
    SurfaceForegroundPatternColor: Color
    IsCutBackgroundPatternVisible: bool
    IsCutForegroundPatternVisible: bool
    IsSurfaceBackgroundPatternVisible: bool
    IsSurfaceForegroundPatternVisible: bool
    CutLinePatternId: ElementId
    CutLineColor: Color
    CutLineWeight: int
    Transparency: int
    ProjectionLinePatternId: ElementId
    ProjectionLineColor: Color
    ProjectionLineWeight: int
    DetailLevel: ViewDetailLevel
    Halftone: bool
    def Dispose(self, ) -> None: ...
    def SetCutBackgroundPatternColor(self, color: Color) -> OverrideGraphicSettings: ...
    def SetCutBackgroundPatternId(self, fillPatternId: ElementId) -> OverrideGraphicSettings: ...
    def SetCutBackgroundPatternVisible(self, fillPatternVisible: bool) -> OverrideGraphicSettings: ...
    def SetCutForegroundPatternColor(self, color: Color) -> OverrideGraphicSettings: ...
    def SetCutForegroundPatternId(self, fillPatternId: ElementId) -> OverrideGraphicSettings: ...
    def SetCutForegroundPatternVisible(self, fillPatternVisible: bool) -> OverrideGraphicSettings: ...
    def SetCutLineColor(self, color: Color) -> OverrideGraphicSettings: ...
    def SetCutLinePatternId(self, linePatternId: ElementId) -> OverrideGraphicSettings: ...
    def SetCutLineWeight(self, lineWeight: int) -> OverrideGraphicSettings: ...
    def SetDetailLevel(self, detailLevel: ViewDetailLevel) -> OverrideGraphicSettings: ...
    def SetHalftone(self, halftone: bool) -> OverrideGraphicSettings: ...
    def SetProjectionLineColor(self, color: Color) -> OverrideGraphicSettings: ...
    def SetProjectionLinePatternId(self, linePatternId: ElementId) -> OverrideGraphicSettings: ...
    def SetProjectionLineWeight(self, lineWeight: int) -> OverrideGraphicSettings: ...
    def SetSurfaceBackgroundPatternColor(self, color: Color) -> OverrideGraphicSettings: ...
    def SetSurfaceBackgroundPatternId(self, fillPatternId: ElementId) -> OverrideGraphicSettings: ...
    def SetSurfaceBackgroundPatternVisible(self, fillPatternVisible: bool) -> OverrideGraphicSettings: ...
    def SetSurfaceForegroundPatternColor(self, color: Color) -> OverrideGraphicSettings: ...
    def SetSurfaceForegroundPatternId(self, fillPatternId: ElementId) -> OverrideGraphicSettings: ...
    def SetSurfaceForegroundPatternVisible(self, fillPatternVisible: bool) -> OverrideGraphicSettings: ...
    def SetSurfaceTransparency(self, transparency: int) -> OverrideGraphicSettings: ...

class OverridePermissions:
    """.NET: Autodesk.Revit.DB.OverridePermissions"""
    def __init__(self, *args) -> None: ...
    ...

class PDFExportOptions:
    """.NET: Autodesk.Revit.DB.PDFExportOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Combine: bool
    StopOnError: bool
    ReplaceHalftoneWithThinLines: bool
    MaskCoincidentLines: bool
    HideScopeBoxes: bool
    HideUnreferencedViewTags: bool
    HideReferencePlane: bool
    HideCropBoundaries: bool
    ViewLinksInBlue: bool
    OriginOffsetY: float
    OriginOffsetX: float
    PaperPlacement: PaperPlacementType
    ColorDepth: ColorDepthType
    ExportQuality: PDFExportQualityType
    RasterQuality: RasterQualityType
    ZoomPercentage: int
    ZoomType: ZoomType
    AlwaysUseRaster: bool
    PaperFormat: ExportPaperFormat
    PaperOrientation: PageOrientationType
    FileName: str
    def Dispose(self, ) -> None: ...
    def GetExportInBackground(self, ) -> bool: ...
    def GetNamingRule(self, ) -> IList: ...
    @staticmethod
    def IsValidNamingRule(namingRule: IList) -> bool: ...
    def SetExportInBackground(self, exportInBackground: bool) -> None: ...
    def SetNamingRule(self, namingRule: IList) -> None: ...

class PDFExportQualityType:
    """.NET: Autodesk.Revit.DB.PDFExportQualityType"""
    def __init__(self, *args) -> None: ...
    ...

class PageOrientationType:
    """.NET: Autodesk.Revit.DB.PageOrientationType"""
    def __init__(self, *args) -> None: ...
    ...

class Panel(FamilyInstance):
    """.NET: Autodesk.Revit.DB.Panel"""
    def __init__(self, *args) -> None: ...
    Transform: Transform
    PanelType: PanelType
    Lockable: bool
    HasSpatialElementFromToCalculationPoints: bool
    HasSpatialElementCalculationPoint: bool
    IsWorkPlaneFlipped: bool
    CanFlipWorkPlane: bool
    IsSlantedColumn: bool
    ExtensionUtility: IExtension
    SuperComponent: Element
    ToRoom: Room
    ToRoom: Room
    FromRoom: Room
    FromRoom: Room
    CanSplit: bool
    CanRotate: bool
    CanFlipFacing: bool
    CanFlipHand: bool
    Mirrored: bool
    Invisible: bool
    FacingFlipped: bool
    HandFlipped: bool
    FacingOrientation: XYZ
    HandOrientation: XYZ
    HostFace: Reference
    HostParameter: float
    Host: Element
    Location: Location
    Space: Space
    Space: Space
    Room: Room
    Room: Room
    StructuralType: StructuralType
    StructuralUsage: StructuralInstanceUsage
    StructuralMaterialId: ElementId
    StructuralMaterialType: StructuralMaterialType
    MEPModel: MEPModel
    Symbol: FamilySymbol
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
    def FindHostPanel(self, ) -> ElementId: ...
    def GetRefGridLines(self, uGridLineId: ElementId, vGridLineId: ElementId) -> None: ...

class PanelType(FamilySymbol):
    """.NET: Autodesk.Revit.DB.PanelType"""
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

class PanelTypeSet(APIObject):
    """.NET: Autodesk.Revit.DB.PanelTypeSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: PanelType) -> bool: ...
    def Erase(self, item: PanelType) -> int: ...
    def ForwardIterator(self, ) -> PanelTypeSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: PanelType) -> bool: ...
    def ReverseIterator(self, ) -> PanelTypeSetIterator: ...

class PanelTypeSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.PanelTypeSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class PaperPlacementType:
    """.NET: Autodesk.Revit.DB.PaperPlacementType"""
    def __init__(self, *args) -> None: ...
    ...

class PaperSize(APIObject):
    """.NET: Autodesk.Revit.DB.PaperSize"""
    def __init__(self, *args) -> None: ...
    Name: str
    IsReadOnly: bool

class PaperSizeSet(APIObject):
    """.NET: Autodesk.Revit.DB.PaperSizeSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: PaperSize) -> bool: ...
    def Erase(self, item: PaperSize) -> int: ...
    def ForwardIterator(self, ) -> PaperSizeSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: PaperSize) -> bool: ...
    def ReverseIterator(self, ) -> PaperSizeSetIterator: ...

class PaperSizeSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.PaperSizeSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class PaperSource(APIObject):
    """.NET: Autodesk.Revit.DB.PaperSource"""
    def __init__(self, *args) -> None: ...
    Name: str
    IsReadOnly: bool

class PaperSourceSet(APIObject):
    """.NET: Autodesk.Revit.DB.PaperSourceSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: PaperSource) -> bool: ...
    def Erase(self, item: PaperSource) -> int: ...
    def ForwardIterator(self, ) -> PaperSourceSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: PaperSource) -> bool: ...
    def ReverseIterator(self, ) -> PaperSourceSetIterator: ...

class PaperSourceSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.PaperSourceSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class Parameter(APIObject):
    """.NET: Autodesk.Revit.DB.Parameter"""
    def __init__(self, *args) -> None: ...
    Id: ElementId
    GUID: Guid
    IsShared: bool
    Element: Element
    HasValue: bool
    UserModifiable: bool
    IsReadOnly: bool
    StorageType: StorageType
    Description: str
    Definition: Definition
    def AsDouble(self, ) -> float: ...
    def AsElementId(self, ) -> ElementId: ...
    def AsInteger(self, ) -> int: ...
    def AsString(self, ) -> str: ...
    def AsValueString(self, formatOptions: FormatOptions) -> str: ...
    def AssociateWithGlobalParameter(self, gpId: ElementId) -> None: ...
    def CanBeAssociatedWithGlobalParameter(self, gpId: ElementId) -> bool: ...
    def CanBeAssociatedWithGlobalParameters(self, ) -> bool: ...
    def ClearValue(self, ) -> bool: ...
    def DissociateFromGlobalParameter(self, ) -> None: ...
    def GetAssociatedGlobalParameter(self, ) -> ElementId: ...
    def GetTypeId(self, ) -> ForgeTypeId: ...
    def GetUnitTypeId(self, ) -> ForgeTypeId: ...
    def Set(self, value: ElementId) -> bool: ...
    @staticmethod
    def SetMultiple(values: IList) -> List: ...
    def SetValueString(self, valueString: str) -> bool: ...

class ParameterAccess:
    """.NET: Autodesk.Revit.DB.ParameterAccess"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetParameter(self, elementId: LinkElementId, parameterDoc: Document, parameterId: ElementId) -> EvaluatedParameter: ...
    def ListParameters(self, id: LinkElementId) -> IDictionary: ...

class ParameterDownloadOptions:
    """.NET: Autodesk.Revit.DB.ParameterDownloadOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Visible: bool
    IsInstance: bool
    def Dispose(self, ) -> None: ...
    def GetCategories(self, ) -> ISet: ...
    def GetGroupTypeId(self, ) -> ForgeTypeId: ...
    def SetCategories(self, categories: ISet) -> None: ...
    def SetGroupTypeId(self, groupTypeId: ForgeTypeId) -> None: ...

class ParameterElement(Element):
    """.NET: Autodesk.Revit.DB.ParameterElement"""
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
    def GetDefinition(self, ) -> InternalDefinition: ...

class ParameterFilterElement(FilterElement):
    """.NET: Autodesk.Revit.DB.ParameterFilterElement"""
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
    def AllRuleParametersApplicable(aDocument: Document, categories: ICollection, elementFilter: ElementFilter) -> bool: ...
    def ClearRules(self, ) -> None: ...
    @staticmethod
    def Create(aDocument: Document, name: str, categories: ICollection, elementFilter: ElementFilter) -> ParameterFilterElement: ...
    @staticmethod
    def ElementFilterIsAcceptableForParameterFilterElement(aDocument: Document, categories: ISet, elementFilter: ElementFilter) -> bool: ...
    def GetCategories(self, ) -> ICollection: ...
    def GetElementFilter(self, ) -> ElementFilter: ...
    def GetElementFilterParameters(self, ) -> ISet: ...
    def GetElementFilterParametersForCategory(self, categoryId: ElementId) -> ISet: ...
    def SetCategories(self, categories: ICollection) -> None: ...
    def SetElementFilter(self, elementFilter: ElementFilter) -> bool: ...

class ParameterFilterRuleFactory:
    """.NET: Autodesk.Revit.DB.ParameterFilterRuleFactory"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    @staticmethod
    def CreateBeginsWithRule(parameter: ElementId, value: str) -> FilterRule: ...
    @staticmethod
    def CreateContainsRule(parameter: ElementId, value: str) -> FilterRule: ...
    @staticmethod
    def CreateEndsWithRule(parameter: ElementId, value: str) -> FilterRule: ...
    @staticmethod
    def CreateEqualsRule(parameter: ElementId, value: float, epsilon: float) -> FilterRule: ...
    @staticmethod
    def CreateGreaterOrEqualRule(parameter: ElementId, value: float, epsilon: float) -> FilterRule: ...
    @staticmethod
    def CreateGreaterRule(parameter: ElementId, value: float, epsilon: float) -> FilterRule: ...
    @staticmethod
    def CreateHasNoValueParameterRule(parameter: ElementId) -> FilterRule: ...
    @staticmethod
    def CreateHasValueParameterRule(parameter: ElementId) -> FilterRule: ...
    @staticmethod
    def CreateIsAssociatedWithGlobalParameterRule(parameter: ElementId, value: ElementId) -> FilterRule: ...
    @staticmethod
    def CreateIsNotAssociatedWithGlobalParameterRule(parameter: ElementId, value: ElementId) -> FilterRule: ...
    @staticmethod
    def CreateLessOrEqualRule(parameter: ElementId, value: float, epsilon: float) -> FilterRule: ...
    @staticmethod
    def CreateLessRule(parameter: ElementId, value: float, epsilon: float) -> FilterRule: ...
    @staticmethod
    def CreateNotBeginsWithRule(parameter: ElementId, value: str) -> FilterRule: ...
    @staticmethod
    def CreateNotContainsRule(parameter: ElementId, value: str) -> FilterRule: ...
    @staticmethod
    def CreateNotEndsWithRule(parameter: ElementId, value: str) -> FilterRule: ...
    @staticmethod
    def CreateNotEqualsRule(parameter: ElementId, value: float, epsilon: float) -> FilterRule: ...
    @staticmethod
    def CreateSharedParameterApplicableRule(parameterName: str) -> FilterRule: ...
    def Dispose(self, ) -> None: ...

class ParameterFilterUtilities:
    """.NET: Autodesk.Revit.DB.ParameterFilterUtilities"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetAllFilterableCategories() -> ICollection: ...
    @staticmethod
    def GetFilterableParametersInCommon(aDoc: Document, categories: ICollection) -> ICollection: ...
    @staticmethod
    def GetInapplicableParameters(aDoc: Document, categories: ICollection, parameters: IList) -> IList: ...
    @staticmethod
    def IsParameterApplicable(element: Element, parameter: ElementId) -> bool: ...
    @staticmethod
    def RemoveUnfilterableCategories(categories: ICollection) -> ICollection: ...

class ParameterMap(APIObject):
    """.NET: Autodesk.Revit.DB.ParameterMap"""
    def __init__(self, *args) -> None: ...
    Item: Parameter
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, key: str) -> bool: ...
    def Erase(self, key: str) -> int: ...
    def ForwardIterator(self, ) -> ParameterMapIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, key: str, item: Parameter) -> bool: ...
    def ReverseIterator(self, ) -> ParameterMapIterator: ...

class ParameterMapIterator(APIObject):
    """.NET: Autodesk.Revit.DB.ParameterMapIterator"""
    def __init__(self, *args) -> None: ...
    Key: str
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ParameterSet(APIObject):
    """.NET: Autodesk.Revit.DB.ParameterSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: Parameter) -> bool: ...
    def Erase(self, item: Parameter) -> int: ...
    def ForwardIterator(self, ) -> ParameterSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: Parameter) -> bool: ...
    def ReverseIterator(self, ) -> ParameterSetIterator: ...

class ParameterSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.ParameterSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ParameterTypeId:
    """.NET: Autodesk.Revit.DB.ParameterTypeId"""
    def __init__(self, *args) -> None: ...
    StructuralSectionComputeAutomaticalyAnalysisProperties: ForgeTypeId
    ToggleParam: ForgeTypeId
    EllipseModificationKeepsRatio: ForgeTypeId
    ProjectionType: ForgeTypeId
    RoomCreationNumberUi: ForgeTypeId
    RoomTagLeaderUi: ForgeTypeId
    RoomTagOrientationUi: ForgeTypeId
    RoomTagOnPlacementUi: ForgeTypeId
    LeaderSnapReference: ForgeTypeId
    ExcludeFromLeaderOutline: ForgeTypeId
    RebarSpacingDetailedSummary: ForgeTypeId
    Rebar3dpathEndOffset: ForgeTypeId
    Rebar3dpathStartOffset: ForgeTypeId
    RebarElemDistributionLength: ForgeTypeId
    RebarLayoutFormulaUnformatted: ForgeTypeId
    SpacingSummary: ForgeTypeId
    RebarLayoutFormula: ForgeTypeId
    ToposurfacePointElevation: ForgeTypeId
    ToposurfacePointBasetypeEnum: ForgeTypeId
    RebarMorphedFreeFormOffset: ForgeTypeId
    BendingDetailTypeAngularDimensionsForCranksEnabled: ForgeTypeId
    RebarShapeName: ForgeTypeId
    RebarShapeCrankEndRatio: ForgeTypeId
    RebarShapeCrankStartRatio: ForgeTypeId
    RebarCrankLengthOverride: ForgeTypeId
    RebarTypeAtEnd: ForgeTypeId
    RebarTypeAtStart: ForgeTypeId
    RebarShapeTypeAtEnd: ForgeTypeId
    RebarShapeTypeAtStart: ForgeTypeId
    RebarCrankAtEndType: ForgeTypeId
    RebarCrankAtStartType: ForgeTypeId
    RebarShapeCrankEndLength: ForgeTypeId
    RebarShapeCrankEndAngledLength: ForgeTypeId
    RebarShapeCrankEndStraightLength: ForgeTypeId
    RebarShapeCrankEndOffset: ForgeTypeId
    RebarShapeCrankStartLength: ForgeTypeId
    RebarShapeCrankStartAngledLength: ForgeTypeId
    RebarShapeCrankStartStraightLength: ForgeTypeId
    RebarShapeCrankStartOffset: ForgeTypeId
    AnalyticalNodeCanBeHosted: ForgeTypeId
    AnalyticalNodeType: ForgeTypeId
    RebarCrankRatio: ForgeTypeId
    RebarCrankOffsetMultiplier: ForgeTypeId
    RebarCrankLengthMultiplier: ForgeTypeId
    RebarStaggeredSet: ForgeTypeId
    RebarMaximumNumber: ForgeTypeId
    RebarMinimumNumber: ForgeTypeId
    RebarSpliceShiftBars: ForgeTypeId
    RebarSpliceStaggerLengthMultiplier: ForgeTypeId
    RebarStaggerOffsetAtEnd: ForgeTypeId
    RebarStaggerOffsetAtStart: ForgeTypeId
    SpliceTypeAtEnd: ForgeTypeId
    SpliceTypeAtStart: ForgeTypeId
    SpliceLapLengthAtEnd: ForgeTypeId
    SpliceLapLengthAtStart: ForgeTypeId
    SpliceByRulesRunout: ForgeTypeId
    SpliceByRulesMinLength: ForgeTypeId
    SpliceByRulesMaxLength: ForgeTypeId
    RebarSpliceSpliceLinePosition: ForgeTypeId
    RebarSpliceLapLengthMultiplier: ForgeTypeId
    SteelElemSinglePartMark: ForgeTypeId
    SteelElemMark: ForgeTypeId
    BendingdetailPosition: ForgeTypeId
    TagHeadAlignment: ForgeTypeId
    RebarBarSpliceLengths: ForgeTypeId
    ExcavationVolumeOnToposolid: ForgeTypeId
    TotalExcavationVolume: ForgeTypeId
    ExcavationVolume: ForgeTypeId
    ExcavationElementFamilyAndType: ForgeTypeId
    ExcavationElementId: ForgeTypeId
    IndividualExcavationVolume: ForgeTypeId
    TagHeadPosition: ForgeTypeId
    RebarConstraintsStatus: ForgeTypeId
    ToposolidFacesLocation: ForgeTypeId
    PlacementTop: ForgeTypeId
    PlacementRight: ForgeTypeId
    PlacementBottom: ForgeTypeId
    PlacementLeft: ForgeTypeId
    PlacementCenterY: ForgeTypeId
    PlacementCenterX: ForgeTypeId
    PlacementParamsShow: ForgeTypeId
    FccAttributionUrl: ForgeTypeId
    FccAttributionLicense: ForgeTypeId
    FccAttributionSource: ForgeTypeId
    ExchangeEntityId: ForgeTypeId
    ExchangeId: ForgeTypeId
    CarbonMaterialParamCoefficientPerItem: ForgeTypeId
    CarbonMaterialParamCoefficientPerMass: ForgeTypeId
    CarbonMaterialParamCoefficientPerEnergy: ForgeTypeId
    CarbonMaterialParamCoefficientPerVolume: ForgeTypeId
    CarbonMaterialParamCoefficientPerArea: ForgeTypeId
    CarbonMaterialParamCoefficientPerLength: ForgeTypeId
    CarbonMaterialParamCategoryName: ForgeTypeId
    CarbonMaterialParamCategoryId: ForgeTypeId
    CarbonMaterialParamProviderName: ForgeTypeId
    CarbonMaterialParamProviderId: ForgeTypeId
    SheetScaleOverride: ForgeTypeId
    TagOrientationBehavior: ForgeTypeId
    FamilyNestingBehavior: ForgeTypeId
    BendingDetailTypeSchematicHeight: ForgeTypeId
    BendingDetailTypeSchematicWidth: ForgeTypeId
    BendingDetailTypeTagTypeId: ForgeTypeId
    BlendDepthParam: ForgeTypeId
    BendingDetailDetailLevel: ForgeTypeId
    BendingDetailAngularDimensionTextPosition: ForgeTypeId
    BendingDetailSegmentLengthDimensionTextPosition: ForgeTypeId
    BendingDetailSegmentRepresentation: ForgeTypeId
    BendingDetailVaryingRebarDimension: ForgeTypeId
    BendingDetailRepresentationFor3dBars: ForgeTypeId
    BendingDetailTypeAngularDimensionsMeasurement: ForgeTypeId
    BendingDetailTypeAngularDimensionsForHooksEnabled: ForgeTypeId
    BendingDetailTypeBendDiameterDimensionsForHooksEnabled: ForgeTypeId
    BendingDetailTypeBendDiameterDimensionsForSegmentsEnabled: ForgeTypeId
    BendingDetailTypeShowBarBendingUsing: ForgeTypeId
    BendingDetailTypeDiameterDimensionTypeId: ForgeTypeId
    BendingDetailTypeRadialDimensionTypeId: ForgeTypeId
    BendingDetailTypeBendDiameterDimensionsEnabled: ForgeTypeId
    BendingDetailTypeAngularDimensionOffset: ForgeTypeId
    BendingDetailTypeShowAngularDimensionsFor: ForgeTypeId
    BendingDetailTypeAngularDimensionTypeId: ForgeTypeId
    BendingDetailTypeAngularDimensionsEnabled: ForgeTypeId
    BendingDetailTypeOrthogonalAndOverallDimesionsEnabled: ForgeTypeId
    BendingDetailTypeSegmentLengthDimensionsForHooksEnabled: ForgeTypeId
    BendingDetailTypeSegmentLengthDimensionsOffset: ForgeTypeId
    BendingDetailTypeSegmentLengthsDisplayOption: ForgeTypeId
    BendingDetailTypeSegmentLengthsForArcsDisplayOption: ForgeTypeId
    BendingDetailTypeSegmentLengthDimensionTypeId: ForgeTypeId
    BendingDetailTypeSegmentLengthDimensionsEnabled: ForgeTypeId
    SsePointOffsetFromSnaps: ForgeTypeId
    LoadIsConstrainedOnHost: ForgeTypeId
    RebarAlignmentOptions: ForgeTypeId
    ScheduleRowHeightInput: ForgeTypeId
    ScheduleResizeRows: ForgeTypeId
    ScheduleRotationOnSheet: ForgeTypeId
    LayerElemScheduleFamily: ForgeTypeId
    LayerElemIsVariable: ForgeTypeId
    LayerElemIsStructuralMaterial: ForgeTypeId
    LayerElemIsCoreLayer: ForgeTypeId
    LayerElemCompoundElemType: ForgeTypeId
    LayerElemCompoundElemFamily: ForgeTypeId
    SsePointElevationBaseType: ForgeTypeId
    SsePointElevation: ForgeTypeId
    SsePointOffsetFromSurface: ForgeTypeId
    SsePointBasetypeEnum: ForgeTypeId
    ToposolidContourSubcategoryId: ForgeTypeId
    ToposolidContourDisplaySettingsIdParam: ForgeTypeId
    ToposolidSubdivideMaterial: ForgeTypeId
    ToposolidSubdivideHeight: ForgeTypeId
    ToposolidInheritContours: ForgeTypeId
    ToposolidFunctionParam: ForgeTypeId
    PreferPatternAlignUiFilter: ForgeTypeId
    ToposolidElevationAtTop: ForgeTypeId
    ToposolidElevationAtBottom: ForgeTypeId
    ToposolidStructureIdParam: ForgeTypeId
    AnalyticalModelHeightParam: ForgeTypeId
    LowestAssociatedLevel: ForgeTypeId
    HighestAssociatedLevel: ForgeTypeId
    ToposolidHeightabovelevelParam: ForgeTypeId
    ToposolidAttrThicknessParam: ForgeTypeId
    ToposolidTypeDefaultThicknessParam: ForgeTypeId
    OffsetFromReferenceBase: ForgeTypeId
    ReferenceBaseOnHost: ForgeTypeId
    OvalFramingHeight: ForgeTypeId
    OvalFramingWidth: ForgeTypeId
    CircularFramingDiameter: ForgeTypeId
    LinearFramingLength: ForgeTypeId
    FramingShapeClassification: ForgeTypeId
    StiffenerClassification: ForgeTypeId
    FamilySelfOrienting: ForgeTypeId
    CouplerRotationAngle: ForgeTypeId
    PreferDimSideUiFilter: ForgeTypeId
    MultipleAlignmentUiToggle: ForgeTypeId
    LockAlignmentUiToggle: ForgeTypeId
    LayerElemBaseExtensionDis: ForgeTypeId
    LayerElemTopExtensionDis: ForgeTypeId
    LayerElemFunction: ForgeTypeId
    LayerElemMaterials: ForgeTypeId
    LayerElemThickness: ForgeTypeId
    LayerElemAreaComputed: ForgeTypeId
    LayerElemOffsetFromHost: ForgeTypeId
    LayerElemVolumeComputed: ForgeTypeId
    LayerTypeMaterials: ForgeTypeId
    LayerTypeThickness: ForgeTypeId
    LayerElemBaseConstraint: ForgeTypeId
    LayerElemTopConstraint: ForgeTypeId
    RebarInstanceBarModelDiameter: ForgeTypeId
    RebarModelBarDiameter: ForgeTypeId
    ViewShowGrids: ForgeTypeId
    RebarModifiedSet: ForgeTypeId
    MovesWithGridParam: ForgeTypeId
    DpartLayerIndex: ForgeTypeId
    VoidCutsGeometry: ForgeTypeId
    RebarTerminationRotationAtEndSchedulesTagsFilters: ForgeTypeId
    RebarTerminationRotationAtStartSchedulesTagsFilters: ForgeTypeId
    RebarHookLengthOverride: ForgeTypeId
    InfrastructureAlignmentName: ForgeTypeId
    InfrastructureAlignmentDescription: ForgeTypeId
    InfrastructureAlignmentDisplayedStartStation: ForgeTypeId
    InfrastructureAlignmentDisplayedEndStation: ForgeTypeId
    AssemblyPrecastFreeze: ForgeTypeId
    RebarTerminationRotationAtEnd: ForgeTypeId
    RebarTerminationRotationAtStart: ForgeTypeId
    RebarShapeTerminationRotationAtEnd: ForgeTypeId
    RebarShapeTerminationRotationAtStart: ForgeTypeId
    PathOfTravelFromRoom: ForgeTypeId
    PathOfTravelToRoom: ForgeTypeId
    RbsElecMaxCircuitsDataPanel: ForgeTypeId
    RbsElecAnalyticalTotalCoincidentLoad: ForgeTypeId
    RbsElecNumberOfCircuits: ForgeTypeId
    SteelElemProfileVolume: ForgeTypeId
    SteelElemProfileLength: ForgeTypeId
    SteelElemProfileType: ForgeTypeId
    RbsElecEditCircuitNamingSettingsParam: ForgeTypeId
    SteelElemPlateJustification: ForgeTypeId
    SteelElemPlatePaintArea: ForgeTypeId
    SteelElemPlateExactWeight: ForgeTypeId
    SteelElemPlateWeight: ForgeTypeId
    SteelElemPlateVolume: ForgeTypeId
    SteelElemPlateArea: ForgeTypeId
    SteelElemPlateWidth: ForgeTypeId
    SteelElemPlateLength: ForgeTypeId
    SteelElemPlateType: ForgeTypeId
    SteelElemBoltTotalWeight: ForgeTypeId
    SteelElemShearstudTotalWeight: ForgeTypeId
    SteelElemAnchorTotalWeight: ForgeTypeId
    SteelElemAnchorOrientation: ForgeTypeId
    SteelElemCutLength: ForgeTypeId
    SteelElemExactWeight: ForgeTypeId
    SteelElemPaintArea: ForgeTypeId
    SteelElemWeight: ForgeTypeId
    PathOfTravelSpeed: ForgeTypeId
    SteelElemBoltLocation: ForgeTypeId
    SteelElemBoltFinishCalculationAtGap: ForgeTypeId
    SteelElemBoltInverted: ForgeTypeId
    SteelElemBoltGripLengthIncrease: ForgeTypeId
    SteelElemBoltGripLength: ForgeTypeId
    SteelElemBoltLength: ForgeTypeId
    GenericZoneName: ForgeTypeId
    RbsPipeBottomElevation: ForgeTypeId
    RbsPipeTopElevation: ForgeTypeId
    RbsElecPanelFeedThruLugsCurrentPhasec: ForgeTypeId
    RbsElecPanelFeedThruLugsCurrentPhaseb: ForgeTypeId
    RbsElecPanelFeedThruLugsCurrentPhasea: ForgeTypeId
    RbsElecPanelFeedThruLugsApparentLoadPhasec: ForgeTypeId
    RbsElecPanelFeedThruLugsApparentLoadPhaseb: ForgeTypeId
    RbsElecPanelFeedThruLugsApparentLoadPhasea: ForgeTypeId
    RbsElecPanelBranchCircuitCurrentPhasec: ForgeTypeId
    RbsElecPanelBranchCircuitCurrentPhaseb: ForgeTypeId
    RbsElecPanelBranchCircuitCurrentPhasea: ForgeTypeId
    RbsElecPanelBranchCircuitApparentLoadPhasec: ForgeTypeId
    RbsElecPanelBranchCircuitApparentLoadPhaseb: ForgeTypeId
    RbsElecPanelBranchCircuitApparentLoadPhasea: ForgeTypeId
    SteelElemHoleDefinition: ForgeTypeId
    RbsElecPanelFeedThruLugsParam: ForgeTypeId
    RbsElecCircuitNumberingType: ForgeTypeId
    TagOnPlacementUi: ForgeTypeId
    RouteAnalysisSettingsParam: ForgeTypeId
    PathOfTravelViewName: ForgeTypeId
    PathOfTravelLevelName: ForgeTypeId
    StructuralConnectionOverrideType: ForgeTypeId
    StructuralConnectionEditType: ForgeTypeId
    PathOfTravelTime: ForgeTypeId
    SteelElemZclipType: ForgeTypeId
    SteelElemCopeAroundAxis: ForgeTypeId
    SteelElemCopeAxisAngle: ForgeTypeId
    SteelElemCopeZAngle: ForgeTypeId
    SteelElemCopeXAngle: ForgeTypeId
    SteelElemCopeDistanceAxis: ForgeTypeId
    SteelElemCopeWidthx: ForgeTypeId
    SteelElemYDistance: ForgeTypeId
    SteelElemXDistance: ForgeTypeId
    SteelElemCutType: ForgeTypeId
    SteelElemPlateShortenCutstraight: ForgeTypeId
    SteelElemPlateShortenSuction: ForgeTypeId
    SteelElemPlateShortenAngle: ForgeTypeId
    SteelElemWeldPrefix: ForgeTypeId
    SteelElemWeldTextModule: ForgeTypeId
    SteelElemHoleDepthOfBoltHead: ForgeTypeId
    SteelElemHoleTapping: ForgeTypeId
    SteelElemHoleBackTaperThread: ForgeTypeId
    SteelElemHoleTappingHole: ForgeTypeId
    SteelElemHoleHeadDiameter: ForgeTypeId
    SteelElemHoleAngle: ForgeTypeId
    SteelElemHoleAlpha: ForgeTypeId
    SteelElemHoleDepth: ForgeTypeId
    SteelElemHoleSlotDirection: ForgeTypeId
    SteelElemHoleSlotLength: ForgeTypeId
    SteelElemHoleType: ForgeTypeId
    SteelElemHoleDiameter: ForgeTypeId
    SteelElemPatternNumber: ForgeTypeId
    SteelElemPatternRadius: ForgeTypeId
    SteelElemPatternEdgeDistanceY: ForgeTypeId
    SteelElemPatternEdgeDistanceX: ForgeTypeId
    SteelElemPatternIntermediateDistanceY: ForgeTypeId
    SteelElemPatternIntermediateDistanceX: ForgeTypeId
    SteelElemPatternTotalWidth: ForgeTypeId
    SteelElemPatternTotalLength: ForgeTypeId
    SteelElemPatternNumberY: ForgeTypeId
    SteelElemPatternNumberX: ForgeTypeId
    SteelElemWeldDoublePrepdepth: ForgeTypeId
    SteelElemWeldDoubleEffectivethroat: ForgeTypeId
    SteelElemWeldDoubleRootopening: ForgeTypeId
    SteelElemWeldDoubleWeldprep: ForgeTypeId
    SteelElemWeldDoubleSurfaceshape: ForgeTypeId
    SteelElemWeldDoubleText: ForgeTypeId
    SteelElemWeldDoubleThickness: ForgeTypeId
    SteelElemWeldDoubleType: ForgeTypeId
    SteelElemWeldMainPrepdepth: ForgeTypeId
    SteelElemWeldMainEffectivethroat: ForgeTypeId
    SteelElemWeldMainRootopening: ForgeTypeId
    SteelElemWeldMainWeldprep: ForgeTypeId
    SteelElemWeldMainSurfaceshape: ForgeTypeId
    SteelElemWeldMainText: ForgeTypeId
    SteelElemWeldPitch: ForgeTypeId
    SteelElemWeldContinuous: ForgeTypeId
    SteelElemWeldLocation: ForgeTypeId
    SteelElemWeldLength: ForgeTypeId
    SteelElemWeldMainThickness: ForgeTypeId
    SteelElemWeldMainType: ForgeTypeId
    SteelElemParamBoringout: ForgeTypeId
    SteelElemParamRadius: ForgeTypeId
    SteelElemContourSide2dist: ForgeTypeId
    SteelElemContourSide1dist: ForgeTypeId
    SteelElemContourGapWidth: ForgeTypeId
    SteelElemShortenAnglez: ForgeTypeId
    SteelElemShortenAngley: ForgeTypeId
    SteelElemShortenReflength: ForgeTypeId
    SteelElemShearstudLength: ForgeTypeId
    SteelElemBoltCoating: ForgeTypeId
    SteelElemAnchorLength: ForgeTypeId
    SteelElemShearstudDiameter: ForgeTypeId
    SteelElemShearstudGrade: ForgeTypeId
    SteelElemShearstudStandard: ForgeTypeId
    SteelElemAnchorDiameter: ForgeTypeId
    SteelElemAnchorAssembly: ForgeTypeId
    SteelElemAnchorGrade: ForgeTypeId
    SteelElemAnchorStandard: ForgeTypeId
    SteelElemCoating: ForgeTypeId
    SteelElemBoltDiameter: ForgeTypeId
    SteelElemBoltAssembly: ForgeTypeId
    SteelElemBoltGrade: ForgeTypeId
    SteelElemBoltStandard: ForgeTypeId
    SteelElemPlateThickness: ForgeTypeId
    SharedCoordElevation: ForgeTypeId
    SharedCoordNorthsouth: ForgeTypeId
    SharedCoordEastwest: ForgeTypeId
    RebarWorkshopInstructions: ForgeTypeId
    RebarGeometryType: ForgeTypeId
    BasepointLatitudeParam: ForgeTypeId
    BasepointLongitudeParam: ForgeTypeId
    RoomOutdoorAirflowParam: ForgeTypeId
    RoomOutdoorAirflowStandardParam: ForgeTypeId
    Directcontext3dSourceId: ForgeTypeId
    Directcontext3dApplicationId: ForgeTypeId
    Directcontext3dLoaded: ForgeTypeId
    Directcontext3dServerId: ForgeTypeId
    Directcontext3dName: ForgeTypeId
    RoomAirChangesPerHourParam: ForgeTypeId
    RoomOutdoorAirPerAreaParam: ForgeTypeId
    RoomOutdoorAirPerPersonParam: ForgeTypeId
    RoomOutdoorAirInfoParam: ForgeTypeId
    RebarInternalMultiplanarArcConnector: ForgeTypeId
    RebarElemEndtreatmentEnd: ForgeTypeId
    RebarElemEndtreatmentStart: ForgeTypeId
    EndTreatment: ForgeTypeId
    CouplerCoupledEndtreatment: ForgeTypeId
    CouplerMainEndtreatment: ForgeTypeId
    CouplerWidth: ForgeTypeId
    CouplerMark: ForgeTypeId
    FamilyFreeinstDefaultElevation: ForgeTypeId
    CouplerCoupledEngagement: ForgeTypeId
    CouplerMainEngagement: ForgeTypeId
    CouplerLength: ForgeTypeId
    CouplerWeight: ForgeTypeId
    CouplerNumber: ForgeTypeId
    CouplerQuantity: ForgeTypeId
    CouplerCoupledBarSize: ForgeTypeId
    CouplerMainBarSize: ForgeTypeId
    CouplerCode: ForgeTypeId
    MultistoryStairsActualTreadDepth: ForgeTypeId
    MultistoryStairsRefLevel: ForgeTypeId
    RebarElemHostMark: ForgeTypeId
    RebarShapeImage: ForgeTypeId
    FabricNumber: ForgeTypeId
    RebarNumber: ForgeTypeId
    GraphicDisplayOptionsSketchyLines: ForgeTypeId
    NumberPartitionParam: ForgeTypeId
    ViewShowHiddenLines: ForgeTypeId
    EnergyPeakloadDatetime: ForgeTypeId
    EnergyDesignFlow: ForgeTypeId
    EnergyCalculatedFlow: ForgeTypeId
    RbsElecAnalyticalDownstreamConnectedPhases: ForgeTypeId
    RbsElecAnalyticalSecondaryHighLegPhase: ForgeTypeId
    RbsElecAnalyticalHighLegPhase: ForgeTypeId
    RbsElecAnalyticalConnectedPhase: ForgeTypeId
    RbsElecAnalyticalNumphases: ForgeTypeId
    RbsElecAnalyticalArea: ForgeTypeId
    RbsElecAnalyticalLoadsInSetObsolete: ForgeTypeId
    RbsElecAnalyticalLoadSetOnStandby: ForgeTypeId
    RbsElecAnalyticalLoadSetOnDuty: ForgeTypeId
    RbsElecDistributionNodeLoadSet: ForgeTypeId
    RbsElecDistributionNodeSupplyTo: ForgeTypeId
    RbsElecAnalyticalFeederLength: ForgeTypeId
    RbsElecAnalyticalLevelId: ForgeTypeId
    RbsElecApparentPowerDensity: ForgeTypeId
    RbsElecDistributionNodeSupplyFrom2: ForgeTypeId
    RbsElecDistributionNodeSupplyFrom: ForgeTypeId
    RbsElecDistributionNodeSupplyFrom1: ForgeTypeId
    RbsElecAnalyticalLoadSetOnTotal: ForgeTypeId
    RbsElecAnalyticalLoadNameParam: ForgeTypeId
    RbsElecAnalyticalLoadTypeParam: ForgeTypeId
    RbsAreaBasedLoadType: ForgeTypeId
    RbsElecAnalyticalLoadDensity: ForgeTypeId
    MepElecZoneEquipmentType: ForgeTypeId
    MepZoneEquipmentDrawVentilation: ForgeTypeId
    MepVrfLoop: ForgeTypeId
    MepReheatHotwaterLoop: ForgeTypeId
    MepZoneEquipment: ForgeTypeId
    MepAnalyticalEquipmentName: ForgeTypeId
    MepZoneHotwaterLoop: ForgeTypeId
    MepZoneAirLoop: ForgeTypeId
    MepReheatCoilType: ForgeTypeId
    MepZoneEquipmentBehavior: ForgeTypeId
    MepZoneEquipmentType: ForgeTypeId
    MepAirloopFantype: ForgeTypeId
    MepChilledWaterLoop: ForgeTypeId
    MepCoolingCoilType: ForgeTypeId
    MepHeatingHotwaterLoop: ForgeTypeId
    MepHeatingCoilType: ForgeTypeId
    MepPreheatHotwaterLoop: ForgeTypeId
    MepAirloopPreheatCoiltype: ForgeTypeId
    MepAirloopHeatexchangerType: ForgeTypeId
    MepCondenserWaterLoop: ForgeTypeId
    MepWaterloopChillertype: ForgeTypeId
    MepWaterloopType: ForgeTypeId
    MepAnalyticalLoopName: ForgeTypeId
    MepSegmentFlowCharacteristic: ForgeTypeId
    MepSegmentOverride: ForgeTypeId
    MepSegmentElementTypename: ForgeTypeId
    MepSegmentFamilyname: ForgeTypeId
    MepSegmentSystemorservice: ForgeTypeId
    MepSegmentLength: ForgeTypeId
    MepAnalyticalElecApparentPowerRating: ForgeTypeId
    MepAnalyticalHydraulicloop: ForgeTypeId
    MepAnalyticalCriticalsequence: ForgeTypeId
    MepAnalyticalHeadersegment: ForgeTypeId
    MepAnalyticalNetwork: ForgeTypeId
    MepAnalyticalElecCurrent: ForgeTypeId
    MepAnalyticalElecVoltage: ForgeTypeId
    MepAnalyticalElecCurrentRating: ForgeTypeId
    SystemEquipmentSets: ForgeTypeId
    MepIgnoreFlowAnalysis: ForgeTypeId
    MepAnalyticalLoopBoundaryParam: ForgeTypeId
    MechanicalEquipmentSetIdParam: ForgeTypeId
    MechanicalEquipmentSetName: ForgeTypeId
    MechanicalEquipmentSetOnStandby: ForgeTypeId
    MechanicalEquipmentSetOnDuty: ForgeTypeId
    MepAnalyticalCriticalpathParam: ForgeTypeId
    MepAnalyticalPipeDesignflow: ForgeTypeId
    MepEquipmentCalcPipingpressuredropParam: ForgeTypeId
    MepEquipmentCalcPipingflowParam: ForgeTypeId
    MepEquipmentClassification: ForgeTypeId
    StructuralConnectionInputElements: ForgeTypeId
    StructuralConnectionNobleStatus: ForgeTypeId
    StructuralConnectionCodeCheckingStatus: ForgeTypeId
    StructuralConnectionApprovalStatus: ForgeTypeId
    StructuralConnectionModifyConnectionParameters: ForgeTypeId
    StructuralConnectionSymbol: ForgeTypeId
    AllModelImage: ForgeTypeId
    AllModelTypeImage: ForgeTypeId
    StructFramJoinStatus: ForgeTypeId
    ReferencedView: ForgeTypeId
    EnergyAnalysisAdvancedOptions: ForgeTypeId
    RbsEnergyAnalysisMode: ForgeTypeId
    RbsEnergyAnalysisBuildingEnvelopeAnalyticalSurfaceIdentificationResolution: ForgeTypeId
    RbsEnergyAnalysisBuildingEnvelopeAnalyticalSpaceIdentificationResolution: ForgeTypeId
    FamilyRoundconnectorDimensiontype: ForgeTypeId
    FamProfileDefinition: ForgeTypeId
    EndZOffsetValue: ForgeTypeId
    EndZJustification: ForgeTypeId
    EndYOffsetValue: ForgeTypeId
    EndYJustification: ForgeTypeId
    StartZOffsetValue: ForgeTypeId
    StartZJustification: ForgeTypeId
    StartYOffsetValue: ForgeTypeId
    StartYJustification: ForgeTypeId
    ZOffsetValue: ForgeTypeId
    ZJustification: ForgeTypeId
    YOffsetValue: ForgeTypeId
    YJustification: ForgeTypeId
    YzJustification: ForgeTypeId
    EndJoinCutback: ForgeTypeId
    StartJoinCutback: ForgeTypeId
    EndExtension: ForgeTypeId
    StartExtension: ForgeTypeId
    DivisionSketchCurveDivisionParamsOverrideParam: ForgeTypeId
    DivisionSketchCurveExtentdToSilhParam: ForgeTypeId
    DivisionRuleParam: ForgeTypeId
    PatternMirrorForDivisionRule: ForgeTypeId
    AllGridRotationForDivisionRule: ForgeTypeId
    PatternIndent2ForDivisionRule: ForgeTypeId
    PatternIndent1ForDivisionRule: ForgeTypeId
    DivisionPattern: ForgeTypeId
    DpartShapeModified: ForgeTypeId
    DpartExcluded: ForgeTypeId
    AnalyticalModelManuallyAdjusted: ForgeTypeId
    PropertySetKeywords: ForgeTypeId
    MaterialAssetParamSourceUrl: ForgeTypeId
    MaterialAssetParamSource: ForgeTypeId
    MaterialAssetParamExternalMaterialId: ForgeTypeId
    MaterialAssetParamCommonSharedAsset: ForgeTypeId
    MaterialAssetParamAssetLibId: ForgeTypeId
    DpartBaseLevelByOriginal: ForgeTypeId
    DpartBaseLevel: ForgeTypeId
    PointAdaptiveNumParam: ForgeTypeId
    PointAdaptiveShowNumber: ForgeTypeId
    PointAdaptiveConstrained: ForgeTypeId
    PointAdaptiveOrientationType: ForgeTypeId
    ThermalMaterialParamElectricalResistivity: ForgeTypeId
    ThermalMaterialParamReflectivity: ForgeTypeId
    ThermalMaterialParamPorosity: ForgeTypeId
    ThermalMaterialParamPermeability: ForgeTypeId
    ThermalMaterialParamTransmitsLight: ForgeTypeId
    ThermalMaterialParamVaporPressure: ForgeTypeId
    ThermalMaterialParamSpecificHeatOfVaporization: ForgeTypeId
    ThermalMaterialParamLiquidViscosity: ForgeTypeId
    ThermalMaterialParamCompressibility: ForgeTypeId
    ThermalMaterialParamGasViscosity: ForgeTypeId
    ThermalMaterialParamEmissivity: ForgeTypeId
    PhyMaterialParamWoodConstruction: ForgeTypeId
    PhyMaterialParamFivepercentModulusOfElacticity: ForgeTypeId
    PhyMaterialParamAverageModulus: ForgeTypeId
    PhyMaterialParamTensionPerpendicular: ForgeTypeId
    PhyMaterialParamTensionParallel: ForgeTypeId
    PhyMaterialParamStructuralThermalTreated: ForgeTypeId
    PhyMaterialParamStructuralDensity: ForgeTypeId
    PhyMaterialParamStructuralSpecificHeat: ForgeTypeId
    PhyMaterialParamThermalConductivityZ: ForgeTypeId
    PhyMaterialParamThermalConductivityY: ForgeTypeId
    PhyMaterialParamThermalConductivityX: ForgeTypeId
    PhyMaterialParamThermalConductivity: ForgeTypeId
    PhyMaterialParamExpCoeffn2: ForgeTypeId
    PhyMaterialParamExpCoeffn1: ForgeTypeId
    PhyMaterialParamShearMod12: ForgeTypeId
    PhyMaterialParamPoissonMod23: ForgeTypeId
    PhyMaterialParamPoissonMod12: ForgeTypeId
    PhyMaterialParamYoungModn2: ForgeTypeId
    PhyMaterialParamYoungModn1: ForgeTypeId
    StairsRailingPlacementOffset: ForgeTypeId
    StairsTrisertypeRiserIsSlanted: ForgeTypeId
    StairsTrisertypeRiser: ForgeTypeId
    StairsTrisertypeNosingPlacement: ForgeTypeId
    StairsTrisertypeRiserProfile: ForgeTypeId
    TerminationExtensionLength: ForgeTypeId
    SupportHeight: ForgeTypeId
    SupportHandClearance: ForgeTypeId
    StairsTrisertypeTreadProfile: ForgeTypeId
    StairsTrisertypeRiserMaterial: ForgeTypeId
    StairsTrisertypeTreadMaterial: ForgeTypeId
    StairsTrisertypeRiserTreadConnection: ForgeTypeId
    StairsTrisertypeRiserThickness: ForgeTypeId
    StairsTrisertypeRiserStyle: ForgeTypeId
    StairsTrisertypeBackNosing: ForgeTypeId
    StairsTrisertypeLeftNosing: ForgeTypeId
    StairsTrisertypeRightNosing: ForgeTypeId
    StairsTrisertypeFrontNosing: ForgeTypeId
    StairsTrisertypeNosingLength: ForgeTypeId
    StairsTrisertypeNosingProfile: ForgeTypeId
    StairsTrisertypeTreadThickness: ForgeTypeId
    StairsTrisertypeTread: ForgeTypeId
    StairsTriserRiserMark: ForgeTypeId
    StairsTriserTreadMark: ForgeTypeId
    StairsTriserRiserNumber: ForgeTypeId
    StairsTriserTreadNumber: ForgeTypeId
    StairsTriserIsTypeOverridden: ForgeTypeId
    StairsWinderpatternNumberOfStraightStepsAtEnd: ForgeTypeId
    StairsWinderpatternNumberOfStraightStepsAtBegin: ForgeTypeId
    StairsWinderpatternRadiusInterior: ForgeTypeId
    StairsWinderpatternFilletInsideCorner: ForgeTypeId
    StairsWinderpatternStairPathOffset: ForgeTypeId
    StairsWinderpatternMinimumWidthInsideWalkline: ForgeTypeId
    StairsWinderpatternMinimumWidthCorner: ForgeTypeId
    StairsWinderpatternWinderStyle: ForgeTypeId
    StairsSupporttypeFlipSectionProfile: ForgeTypeId
    StairsSupporttypeStructuralDepthOnLanding: ForgeTypeId
    StairsSupporttypeStructuralDepthOnRun: ForgeTypeId
    StairsSupporttypeMaterial: ForgeTypeId
    StairsSupporttypeWidth: ForgeTypeId
    StairsSupporttypeTotalDepth: ForgeTypeId
    StairsSupporttypeStructuralDepth: ForgeTypeId
    StairsSupporttypeUndersideSurface: ForgeTypeId
    StairsSupporttypeTopsideSurface: ForgeTypeId
    StairsSupporttypeSectionProfile: ForgeTypeId
    StairsSupportLandingsupportType: ForgeTypeId
    StairsSupportOverridden: ForgeTypeId
    StairsSupportTrimSupportUpper: ForgeTypeId
    StairsSupportUpperEndCut: ForgeTypeId
    StairsSupportLowerEndCut: ForgeTypeId
    StairsSupportVerticalOffset: ForgeTypeId
    StairsSupportHorizontalOffset: ForgeTypeId
    StairsLandingtypeLandingMaterial: ForgeTypeId
    StairsLandingtypeTreadriserType: ForgeTypeId
    StairsLandingtypeUseSameTriserAsRun: ForgeTypeId
    StairsLandingtypeThickness: ForgeTypeId
    StairsLandingtypeStructure: ForgeTypeId
    StairsLandingtypeHasMonolithicSupport: ForgeTypeId
    StairsLandingOverridden: ForgeTypeId
    StairsLandingThickness: ForgeTypeId
    StairsLandingStructural: ForgeTypeId
    StairsLandingBaseElevation: ForgeTypeId
    StairsRuntypeRunMaterial: ForgeTypeId
    StairsRuntypeTotalDepth: ForgeTypeId
    StairsRuntypeStructuralDepth: ForgeTypeId
    StairsRuntypeStructure: ForgeTypeId
    StairsRuntypeUndersideSurfaceType: ForgeTypeId
    StairsRuntypeHasMonolithicSupport: ForgeTypeId
    StairsRunCreationChainSpiral: ForgeTypeId
    StairsRunCreateOffset: ForgeTypeId
    StairsRunExtendBelowTreadBase: ForgeTypeId
    StairsRunCcw: ForgeTypeId
    StairsRunCreateAutoLanding: ForgeTypeId
    StairsRunWinderEndWithStraight: ForgeTypeId
    StairsRunWinderBeginWithStraight: ForgeTypeId
    StairsRunLocationpathJustfication: ForgeTypeId
    StairsRunEndWithRiser: ForgeTypeId
    StairsRunBeginWithRiser: ForgeTypeId
    StairsRunOverridden: ForgeTypeId
    StairsRunStructural: ForgeTypeId
    StairsRunCenterMarkVisible: ForgeTypeId
    StairsRunActualRunWidth: ForgeTypeId
    StairsRunActualTreadDepth: ForgeTypeId
    StairsRunActualRiserHeight: ForgeTypeId
    StairsRunActualNumberOfTreads: ForgeTypeId
    StairsRunActualNumberOfRisers: ForgeTypeId
    StairsRunExtendBelowRiserBase: ForgeTypeId
    StairsRunHeight: ForgeTypeId
    StairsRunTopElevation: ForgeTypeId
    StairsRunBottomElevation: ForgeTypeId
    StairstypeHasIntermediateSupport: ForgeTypeId
    StairstypeLeftSupportLateralOffset: ForgeTypeId
    StairstypeRightSupportLateralOffset: ForgeTypeId
    StairstypeCutmarkType: ForgeTypeId
    StairstypeConstructionMethod: ForgeTypeId
    StairstypeHasRightSupport: ForgeTypeId
    StairstypeHasLeftSupport: ForgeTypeId
    StairstypeNotchWidth: ForgeTypeId
    StairstypeNotchVerticalGap: ForgeTypeId
    StairstypeNotchHorizontalGap: ForgeTypeId
    StairstypeNotchCustomWidth: ForgeTypeId
    StairstypeNotchThickness: ForgeTypeId
    StairstypeNotchExtension: ForgeTypeId
    StairstypeGeomunjoinedEndCutStyle: ForgeTypeId
    StairstypeCalcRuleTargetResult: ForgeTypeId
    StairstypeCalcRuleMinResult: ForgeTypeId
    StairstypeCalcRuleMaxResult: ForgeTypeId
    StairstypeCalcRuleTreadMultiplier: ForgeTypeId
    StairstypeCalcRuleRiserMultiplier: ForgeTypeId
    StairstypeIsAssembledStairs: ForgeTypeId
    StairstypeNumberOfIntermediateSupports: ForgeTypeId
    StairstypeMinimumRunWidth: ForgeTypeId
    StairstypeWinderStepFrontMeasurement: ForgeTypeId
    StairstypeShowUpdown: ForgeTypeId
    StairstypeShowStairPath: ForgeTypeId
    StairstypeShowCutline: ForgeTypeId
    StairstypeIntermediateSupportType: ForgeTypeId
    StairstypeLeftSideSupportType: ForgeTypeId
    StairstypeRightSideSupportType: ForgeTypeId
    StairstypeLandingType: ForgeTypeId
    StairstypeRunType: ForgeTypeId
    StairstypeCalculationRules: ForgeTypeId
    StairstypeMinimumTreadWidthInsideBoundary: ForgeTypeId
    StairstypeMinimumTreadDepth: ForgeTypeId
    StairstypeMaximumRiserHeight: ForgeTypeId
    StairsTriserNumberBaseIndex: ForgeTypeId
    StairsDbgShowAnnotationCutMark: ForgeTypeId
    StairsDbgShowMonolithicSupportCorseGeom: ForgeTypeId
    StairsDbgShowTriserCorseGeom: ForgeTypeId
    StairsDbgShowRunCorseGeom: ForgeTypeId
    StairsDbgShowMonolithicSupportGeom: ForgeTypeId
    StairsDbgShowTriserGeom: ForgeTypeId
    StairsDbgShowRunGeom: ForgeTypeId
    StairsDbgShowSupportPath: ForgeTypeId
    StairsDbgShowBoundary3d: ForgeTypeId
    StairsDbgShowBoundary2d: ForgeTypeId
    StairsDbgShowLandingPath: ForgeTypeId
    StairsDbgShowLandingBoundary: ForgeTypeId
    StairsDbgShowRunOutlineForPlan: ForgeTypeId
    StairsDbgShowRunNosing: ForgeTypeId
    StairsDbgShowRunRiser: ForgeTypeId
    StairsDbgShowRunPath3d: ForgeTypeId
    StairsDbgShowRunPath2d: ForgeTypeId
    StairsDbgShowRightRunBoundary3d: ForgeTypeId
    StairsDbgShowLeftRunBoundary3d: ForgeTypeId
    StairsDbgShowRightRunBoundary2d: ForgeTypeId
    StairsDbgShowLeftRunBoundary2d: ForgeTypeId
    StairsDbgShowLandingFaces: ForgeTypeId
    StairsDbgShowTreadFaces: ForgeTypeId
    StairsEnableCalculationRuleChecking: ForgeTypeId
    StairsMinAutomaticLandingDepth: ForgeTypeId
    StairsRunWidthMeasurement: ForgeTypeId
    StairsTotalNumberOfTreads: ForgeTypeId
    StairsTotalNumberOfRisers: ForgeTypeId
    StairsActualNumberOfRisers: ForgeTypeId
    StairsDesiredNumberOfRisers: ForgeTypeId
    StairsMultistoryUpToLevel: ForgeTypeId
    StairsStairsHeight: ForgeTypeId
    StairsTopLevel: ForgeTypeId
    StairsBaseLevel: ForgeTypeId
    PartMakerDivisionProfileOffset: ForgeTypeId
    DivisionProfileWidth: ForgeTypeId
    PartMakerSplitterProfileEdgeMatch: ForgeTypeId
    PartMakerSplitterProfileFlipAlong: ForgeTypeId
    PartMakerSplitterProfileFlipAcross: ForgeTypeId
    PartMakerSplitterProfile: ForgeTypeId
    FamilyKeywordProtected: ForgeTypeId
    PartmakerParamDivisionGap: ForgeTypeId
    PointcloudinstanceName: ForgeTypeId
    AnalyticalModelRotation: ForgeTypeId
    PointcloudtypeScale: ForgeTypeId
    PropertySetDescription: ForgeTypeId
    PropertySetMaterialAspect: ForgeTypeId
    RbsDuctPipeSystemAbbreviationParam: ForgeTypeId
    PhyMaterialProperties: ForgeTypeId
    PropertySetName: ForgeTypeId
    PhyMaterialParamSubclass: ForgeTypeId
    PhyMaterialParamClass: ForgeTypeId
    AnalyticalModelPerimeter: ForgeTypeId
    AnalyticalModelArea: ForgeTypeId
    AnalyticalModelLength: ForgeTypeId
    SheetAssemblyKeynote: ForgeTypeId
    SheetAssemblyAssemblyDescription: ForgeTypeId
    SheetAssemblyCost: ForgeTypeId
    SheetAssemblyTypeMark: ForgeTypeId
    SheetAssemblyAssemblyCode: ForgeTypeId
    SheetAssemblyDescription: ForgeTypeId
    SheetAssemblyUrl: ForgeTypeId
    SheetAssemblyTypeComments: ForgeTypeId
    SheetAssemblyManufacturer: ForgeTypeId
    SheetAssemblyModel: ForgeTypeId
    SheetAssemblyName: ForgeTypeId
    PipeInsulationThickness: ForgeTypeId
    DuctInsulationThickness: ForgeTypeId
    RbsReferenceFreesize: ForgeTypeId
    RbsReferenceOverallsize: ForgeTypeId
    RbsReferenceLiningThickness: ForgeTypeId
    RbsReferenceLiningType: ForgeTypeId
    RbsReferenceInsulationThickness: ForgeTypeId
    RbsReferenceInsulationType: ForgeTypeId
    RbsPipeCalculatedSize: ForgeTypeId
    RbsDuctCalculatedSize: ForgeTypeId
    RbsInsulationLiningVolume: ForgeTypeId
    AssemblyName: ForgeTypeId
    RbsComponentClassificationParam: ForgeTypeId
    RbsSystemRisedropParam: ForgeTypeId
    RbsSystemRisedrop2linedropsymbolParam: ForgeTypeId
    RbsSystemRisedrop2linerisesymbolParam: ForgeTypeId
    RbsSystemRisedrop1linedropsymbolParam: ForgeTypeId
    RbsSystemRisedrop1linerisesymbolParam: ForgeTypeId
    RbsSystemRisedrop1lineteeupsymbolParam: ForgeTypeId
    RbsSystemRisedrop1lineteedownsymbolParam: ForgeTypeId
    AssemblyNamingCategory: ForgeTypeId
    RailingSystemHasTopRail: ForgeTypeId
    RailingPathCurvePropertiesSlopeOption: ForgeTypeId
    RailingPathCurvePropertiesHeightCorrectionOption: ForgeTypeId
    RailingPathCurvePropertiesHeight: ForgeTypeId
    RailingPathCurveJoinOption: ForgeTypeId
    ContinuousrailJoinTypeParam: ForgeTypeId
    ContinuousrailPlusTreadDepthParam: ForgeTypeId
    ContinuousrailLengthParam: ForgeTypeId
    HandrailSupportsJustificationParam: ForgeTypeId
    HandrailSupportsNumberParam: ForgeTypeId
    HandrailSupportsSpacingParam: ForgeTypeId
    HandrailSupportsLayoutParam: ForgeTypeId
    HandrailSupportsTypeParam: ForgeTypeId
    ContinuousrailEndExtensionLengthParam: ForgeTypeId
    ContinuousrailEndTerminationAttachmentParam: ForgeTypeId
    ContinuousrailExtensionLengthParam: ForgeTypeId
    ContinuousrailBeginningTerminationAttachmentParam: ForgeTypeId
    ContinuousrailEndTerminationTypeParam: ForgeTypeId
    ContinuousrailBeginningTerminationTypeParam: ForgeTypeId
    ContinuousrailMaterialsParam: ForgeTypeId
    ContinuousrailTransitionTypeParam: ForgeTypeId
    HandrailHandClearanceParam: ForgeTypeId
    HandrailProjectionParam: ForgeTypeId
    HandrailHeightParam: ForgeTypeId
    ContinuousrailProfileTypeParam: ForgeTypeId
    ContinuousrailFilletRadiusParam: ForgeTypeId
    ContinuousrailDefaultJoinTypeParam: ForgeTypeId
    RailingSystemSecondaryHandrailsLatteralOffset: ForgeTypeId
    RailingSystemSecondaryHandrailsHeightParam: ForgeTypeId
    RailingSystemSecondaryHandrailsPositionParam: ForgeTypeId
    RailingSystemSecondaryHandrailsTypesParam: ForgeTypeId
    RailingSystemHandrailsLatteralOffset: ForgeTypeId
    RailingSystemHandrailsHeightParam: ForgeTypeId
    RailingSystemHandrailsPositionParam: ForgeTypeId
    RailingSystemHandrailsTypesParam: ForgeTypeId
    RailingSystemTopRailHeightParam: ForgeTypeId
    RailingSystemTopRailTypesParam: ForgeTypeId
    PointElementRotationAngle: ForgeTypeId
    FlexibleInstanceFlip: ForgeTypeId
    PointFlexibleOrientationType: ForgeTypeId
    DefaultConstructionMassFloor: ForgeTypeId
    DefaultConstructionMassOpening: ForgeTypeId
    DefaultConstructionMassSkylight: ForgeTypeId
    DefaultConstructionMassGlazing: ForgeTypeId
    DefaultConstructionExtWallUnderground: ForgeTypeId
    DefaultConstructionMassSlab: ForgeTypeId
    DefaultConstructionMassShade: ForgeTypeId
    DefaultConstructionMassRoof: ForgeTypeId
    DefaultConstructionMassInteriorWall: ForgeTypeId
    DefaultConstructionMassExteriorWall: ForgeTypeId
    EnergyAnalysisSpaceBoundingParam: ForgeTypeId
    EnergyAnalysisHorizontalVoidThreshold: ForgeTypeId
    EnergyAnalysisVerticalVoidThreshold: ForgeTypeId
    RbsEnergyAnalysisBuildingEnvelopeAnalyticalGridCellSize: ForgeTypeId
    RbsEnergyAnalysisBuildingEnvelopeDeterminationParam: ForgeTypeId
    LeaderRightAttachment: ForgeTypeId
    LeaderLeftAttachment: ForgeTypeId
    PointElementMeasureFrom: ForgeTypeId
    PointElementAngle: ForgeTypeId
    PointElementChordLength: ForgeTypeId
    PointElementNormalizedSegmentLength: ForgeTypeId
    PointElementSegmentLength: ForgeTypeId
    PointElementNormalizedCurveParamater: ForgeTypeId
    PointElementNonNormalizedCurveParamater: ForgeTypeId
    PointElementMeasurementType: ForgeTypeId
    StructuralBeamEndAttachmentRefcolumnEnd: ForgeTypeId
    StructuralBeamStartAttachmentRefcolumnEnd: ForgeTypeId
    StructuralBeamEndAttachmentDistance: ForgeTypeId
    StructuralBeamStartAttachmentDistance: ForgeTypeId
    StructuralBeamEndAttachmentType: ForgeTypeId
    StructuralBeamStartAttachmentType: ForgeTypeId
    TextBoxVisibility: ForgeTypeId
    CurveByPointsProjectionType: ForgeTypeId
    FollowSurface: ForgeTypeId
    RbsEnergyAnalysisIncludeThermalProperties: ForgeTypeId
    PointFlexibleNumParam: ForgeTypeId
    FramingLengthRoundoff: ForgeTypeId
    SlantedColumnBaseExtension: ForgeTypeId
    SlantedColumnTopExtension: ForgeTypeId
    SlantedColumnBaseCutStyle: ForgeTypeId
    SlantedColumnTopCutStyle: ForgeTypeId
    RbsBuildingUseloadcredits: ForgeTypeId
    TilePatternFamrefComponentExtents: ForgeTypeId
    TilePatternGridCellsY: ForgeTypeId
    TilePatternGridCellsX: ForgeTypeId
    TilePatternGridUnitY: ForgeTypeId
    TilePatternGridUnitX: ForgeTypeId
    PointElementShowNormalPlaneOnly: ForgeTypeId
    LevelIsGroundPlane: ForgeTypeId
    BasepointAngletonParam: ForgeTypeId
    BasepointElevationParam: ForgeTypeId
    BasepointEastwestParam: ForgeTypeId
    BasepointNorthsouthParam: ForgeTypeId
    SlantedColumnGeometryTreatmentBase: ForgeTypeId
    SlantedColumnGeometryTreatmentTop: ForgeTypeId
    RoomPlenumLightingParam: ForgeTypeId
    StructuralAttachmentTopReferencedend: ForgeTypeId
    StructuralAttachmentTopRatio: ForgeTypeId
    StructuralAttachmentTopDistance: ForgeTypeId
    StructuralAttachmentTopType: ForgeTypeId
    StructuralAttachmentBaseReferencedend: ForgeTypeId
    StructuralAttachmentBaseRatio: ForgeTypeId
    StructuralAttachmentBaseDistance: ForgeTypeId
    StructuralAttachmentBaseType: ForgeTypeId
    InstanceMoveBaseWithGrids: ForgeTypeId
    InstanceMoveTopWithGrids: ForgeTypeId
    SlantedColumnTypeParam: ForgeTypeId
    ViewSlantedColumnSymbolOffset: ForgeTypeId
    PointElementMirrored: ForgeTypeId
    PointElementZflipped: ForgeTypeId
    PointElementHostedOnFaceVParam: ForgeTypeId
    PointElementHostedOnFaceUParam: ForgeTypeId
    LockedEndOffset: ForgeTypeId
    LockedStartOffset: ForgeTypeId
    LockedBaseOffset: ForgeTypeId
    LockedTopOffset: ForgeTypeId
    RbsProjectReporttypeParam: ForgeTypeId
    RbsBuildingConstructionclass: ForgeTypeId
    ConnectorUtilityParam: ForgeTypeId
    PointFlexibleShowNumber: ForgeTypeId
    PointFlexibleConstrained: ForgeTypeId
    PointNameParam: ForgeTypeId
    PointAdaptiveTypeParam: ForgeTypeId
    SpotDimStyleSlopeUnits: ForgeTypeId
    PointElementDriving: ForgeTypeId
    SpotSlopeLeaderLength: ForgeTypeId
    SpotSlopeSuffix: ForgeTypeId
    SpotSlopePrefix: ForgeTypeId
    PointVisibilityParam: ForgeTypeId
    PointElementShowPlanes: ForgeTypeId
    CurveIsReferenceLine: ForgeTypeId
    PointElementHostedParam: ForgeTypeId
    PointElementDriven: ForgeTypeId
    PointElementOffset: ForgeTypeId
    SpotDimStyleSlopeUnitsAlt: ForgeTypeId
    FbxLightPhotometricFileCache: ForgeTypeId
    FbxLightPhotometricsFam: ForgeTypeId
    FamilyCurveAttachmentProportion: ForgeTypeId
    FbxLightLossFactorCtrl: ForgeTypeId
    FbxLightInitialColorCtrl: ForgeTypeId
    FbxLightLossFactorMethod: ForgeTypeId
    FbxLightInitialColorName: ForgeTypeId
    FbxLightAtADistance: ForgeTypeId
    FbxLightInitialIntensityInputMethod: ForgeTypeId
    FbxLightSourceLength: ForgeTypeId
    FbxLightSourceDiameter: ForgeTypeId
    FbxLightEmitCircleDiameter: ForgeTypeId
    FbxLightEmitRectangleLength: ForgeTypeId
    FbxLightEmitRectangleWidth: ForgeTypeId
    FbxLightEmitLineLength: ForgeTypeId
    FbxLightEmitShapeVisible: ForgeTypeId
    FbxLightDimmingLightColor: ForgeTypeId
    FbxLightLumenaireDirt: ForgeTypeId
    FbxLightLampLumenDepr: ForgeTypeId
    FbxLightSurfaceLoss: ForgeTypeId
    FbxLightLampTiltLoss: ForgeTypeId
    FbxLightVoltageLoss: ForgeTypeId
    FbxLightTemperatureLoss: ForgeTypeId
    FbxLightColorFilter: ForgeTypeId
    FbxLightInitialColorTemperature: ForgeTypeId
    FbxLightIlluminance: ForgeTypeId
    FbxLightLimunousIntensity: ForgeTypeId
    FbxLightEfficacy: ForgeTypeId
    FbxLightWattage: ForgeTypeId
    FbxLightInitialIntensity: ForgeTypeId
    FbxLightPhotometrics: ForgeTypeId
    FbxAssetType: ForgeTypeId
    DividedSurfaceGridOptionParamn2: ForgeTypeId
    DividedSurfaceGridOptionParamn1: ForgeTypeId
    DividedSurfaceDisplayDiscardeddivisionlines: ForgeTypeId
    DividedSurfaceComponentTrimType: ForgeTypeId
    DividedSurfacePatternMirror: ForgeTypeId
    DividedSurfaceRule2Suspension: ForgeTypeId
    DividedSurfaceRule1Suspension: ForgeTypeId
    DividedSurfaceDisplayComponents: ForgeTypeId
    DividedSurfacePatternFillMaterial: ForgeTypeId
    DividedSurfaceDisplayPatternFill: ForgeTypeId
    DividedSurfacePatternLinesStyle: ForgeTypeId
    DividedSurfaceDisplayPatternLines: ForgeTypeId
    DividedSurfaceGridlinesStyle: ForgeTypeId
    DividedSurfaceDisplayGridlines: ForgeTypeId
    DividedSurfaceDisplayNodes: ForgeTypeId
    DividedSurfaceOriginalSurfaceMaterial: ForgeTypeId
    DividedSurfaceDisplayOriginalSurface: ForgeTypeId
    DividedSurfaceDisplaySurfaceOption: ForgeTypeId
    DividedSurfaceAllGridRotation: ForgeTypeId
    DividedSurfaceTileBorder: ForgeTypeId
    DividedSurfaceAllPoints: ForgeTypeId
    DividedSurfacePattern: ForgeTypeId
    DividedSurfacePatternFlip: ForgeTypeId
    DividedSurfacePatternRotationAngle: ForgeTypeId
    DividedSurfacePatternIndentn2: ForgeTypeId
    DividedSurfacePatternIndentn1: ForgeTypeId
    DividedSurfaceCoverFaceCompletely: ForgeTypeId
    DividedSurfaceOffsetFromSurface: ForgeTypeId
    DividedSurfaceTotalEdgeLength: ForgeTypeId
    DividedSurfaceEdgeNumber: ForgeTypeId
    DividedSurfacePointNumber: ForgeTypeId
    DividedSurfaceFacetNumber: ForgeTypeId
    DividedSurfaceSurfaceArea: ForgeTypeId
    RbsElecRoomLightingCalcLuminaireplane: ForgeTypeId
    LayoutnodeCurvetypeParam: ForgeTypeId
    RbsElecCircuitCoreTypeParam: ForgeTypeId
    RbsElecCircuitOtherConductorSizeParam: ForgeTypeId
    RbsElecCircuitGroundConductorSizeParam: ForgeTypeId
    RbsElecCircuitNeutralConductorSizeParam: ForgeTypeId
    RbsElecCircuitHotConductorSizeParam: ForgeTypeId
    RbsElecCircuitCableSizeParam: ForgeTypeId
    RbsElecCircuitCableTypeParam: ForgeTypeId
    RbsDistributionsysHlPhaseParam: ForgeTypeId
    FabricationHandlePosition: ForgeTypeId
    FabricationPartVolume: ForgeTypeId
    FabricationPartMaterialWeight: ForgeTypeId
    FabricationPartDuctWeight: ForgeTypeId
    RbsPipeWallThickness: ForgeTypeId
    MepFlexRibbonElevation: ForgeTypeId
    MepHorizontailOffset: ForgeTypeId
    MepPipeLowerInvertElevation: ForgeTypeId
    MepPipeUpperInvertElevation: ForgeTypeId
    MepPipeLowerObvertElevation: ForgeTypeId
    MepPipeUpperObvertElevation: ForgeTypeId
    MepLowerBottomElevationIncludeInsulation: ForgeTypeId
    MepLowerTopElevationIncludeInsulation: ForgeTypeId
    MepUpperBottomElevationIncludeInsulation: ForgeTypeId
    MepUpperTopElevationIncludeInsulation: ForgeTypeId
    MepLowerBottomElevation: ForgeTypeId
    MepLowerTopElevation: ForgeTypeId
    MepUpperBottomElevation: ForgeTypeId
    MepUpperTopElevation: ForgeTypeId
    MepLowerCenterlineElevation: ForgeTypeId
    MepUpperCenterlineElevation: ForgeTypeId
    FabricationMaterialGauge: ForgeTypeId
    FabricationDuctworkStiffenerSpec: ForgeTypeId
    FabricationPartPatNo: ForgeTypeId
    FabricationEndSize: ForgeTypeId
    FabricationBranchSize: ForgeTypeId
    FabricationSecondarySize: ForgeTypeId
    FabricationPrimarySize: ForgeTypeId
    FabricationChangeServiceParam: ForgeTypeId
    FabricationSetUpDownTagFromBottom: ForgeTypeId
    FabricationInsulationMaterialFinish: ForgeTypeId
    DisplacedElementDisplacementZ: ForgeTypeId
    DisplacedElementDisplacementY: ForgeTypeId
    DisplacedElementDisplacementX: ForgeTypeId
    DisplacementPathStyle: ForgeTypeId
    DisplacementPathDepth: ForgeTypeId
    ReferenceViewerUiTargetView: ForgeTypeId
    ReferenceViewerUiTargetFilter: ForgeTypeId
    FabricationFittingDescription: ForgeTypeId
    FabricationDoublewallMaterialAbbreviation: ForgeTypeId
    FabricationMaterialAbbreviation: ForgeTypeId
    FabricationInsulationSpecificationAbbreviation: ForgeTypeId
    FabricationInsulationAbbreviation: ForgeTypeId
    FabricationSpecificationAbbreviation: ForgeTypeId
    FabricationPipeInvertElevation: ForgeTypeId
    FabricationBottomElevationIncludeInsulationOfPart: ForgeTypeId
    FabricationBottomElevationOfPart: ForgeTypeId
    FabricationTopElevationIncludeInsulationOfPart: ForgeTypeId
    FabricationTopElevationOfPart: ForgeTypeId
    MepSpotCenterlineElevation: ForgeTypeId
    MepSpotBottomElevationIncludeInsulation: ForgeTypeId
    MepSpotBottomElevation: ForgeTypeId
    MepSpotTopElevationIncludeInsulation: ForgeTypeId
    MepSpotTopElevation: ForgeTypeId
    FabricationPartDoublewallMaterialArea: ForgeTypeId
    FabricationSetUpDownTag: ForgeTypeId
    FabricationPartSheetmetalArea: ForgeTypeId
    FabricationServiceAbbreviation: ForgeTypeId
    FabricationPartMaterialThickness: ForgeTypeId
    FabricationPartNotes: ForgeTypeId
    FabricationPartLiningArea: ForgeTypeId
    FabricationPartItemNumber: ForgeTypeId
    FabricationPartInsulationArea: ForgeTypeId
    FabricationServiceName: ForgeTypeId
    FabricationPartDoublewallMaterialThickness: ForgeTypeId
    FabricationPartDoublewallMaterial: ForgeTypeId
    FabricationPartCutType: ForgeTypeId
    FabricationPartBoughtOut: ForgeTypeId
    FabricationPartAlias: ForgeTypeId
    FabricationRoutingSolutionsUiParam: ForgeTypeId
    FabricationProductCode: ForgeTypeId
    FabricationPartTakeoffDialogParam: ForgeTypeId
    FabricationPartDepthOutOption: ForgeTypeId
    FabricationPartWidthOutOption: ForgeTypeId
    FabricationPartDiameterOutOption: ForgeTypeId
    FabricationPartDiameterInOption: ForgeTypeId
    FabricationPartDepthInOption: ForgeTypeId
    FabricationPartWidthInOption: ForgeTypeId
    FabricationPartAngleOption: ForgeTypeId
    FabricationPartLengthOption: ForgeTypeId
    FabricationInsulationSpec: ForgeTypeId
    FabricationPartLength: ForgeTypeId
    FabricationProductEntry: ForgeTypeId
    FabricationPartDepthOut: ForgeTypeId
    FabricationPartWidthOut: ForgeTypeId
    FabricationPartDiameterOut: ForgeTypeId
    FabricationPartDepthIn: ForgeTypeId
    FabricationPartWidthIn: ForgeTypeId
    FabricationEndOffsetParam: ForgeTypeId
    FabricationStartOffsetParam: ForgeTypeId
    FabricationSlopeParam: ForgeTypeId
    FabricationRelativeFilename: ForgeTypeId
    FabricationVendor: ForgeTypeId
    FabricationBottomOfPart: ForgeTypeId
    FabricationTopOfPart: ForgeTypeId
    FabricationOffsetParam: ForgeTypeId
    FabricationLevelParam: ForgeTypeId
    FabricationSpecification: ForgeTypeId
    FabricationVendorCode: ForgeTypeId
    FabricationPartWeight: ForgeTypeId
    FabricationPartDiameterIn: ForgeTypeId
    FabricationPartAngle: ForgeTypeId
    FabricationProductDataInstallType: ForgeTypeId
    FabricationPartMaterial: ForgeTypeId
    FabricationProductDataOem: ForgeTypeId
    FabricationProductDataProduct: ForgeTypeId
    FabricationProductDataItemDescription: ForgeTypeId
    FabricationProductDataSizeDescription: ForgeTypeId
    FabricationProductDataMaterialDescription: ForgeTypeId
    FabricationProductDataSpecification: ForgeTypeId
    FabricationProductDataLongDescription: ForgeTypeId
    FabricationProductDataRange: ForgeTypeId
    FabricationProductDataFinishDescription: ForgeTypeId
    TrussFamilyBottomChordStructuralTypesParam: ForgeTypeId
    TrussFamilyBottomChordAngleParam: ForgeTypeId
    TrussFamilyBottomChordVerticalProjectionParam: ForgeTypeId
    TrussFamilyBottomChordStartReleaseType: ForgeTypeId
    TrussFamilyBottomChordEndReleaseType: ForgeTypeId
    ReferenceOtherViewUiRefView: ForgeTypeId
    ReferenceOtherViewUiToggle: ForgeTypeId
    JoistSystemElemTagNewMembersView: ForgeTypeId
    ReferenceViewerAttrTag: ForgeTypeId
    ReferenceViewerTargetView: ForgeTypeId
    MatchlineBottomPlane: ForgeTypeId
    MatchlineTopPlane: ForgeTypeId
    MatchlineBottomOffset: ForgeTypeId
    MatchlineTopOffset: ForgeTypeId
    TrussFamilyTopChordStructuralTypesParam: ForgeTypeId
    TrussFamilyTopChordAngleParam: ForgeTypeId
    TrussFamilyTopChordVerticalProjectionParam: ForgeTypeId
    TrussFamilyTopChordStartReleaseType: ForgeTypeId
    TrussFamilyTopChordEndReleaseType: ForgeTypeId
    TrussFamilyDiagWebStructuralTypesParam: ForgeTypeId
    TrussFamilyDiagWebAngleParam: ForgeTypeId
    TrussFamilyDiagWebStartReleaseType: ForgeTypeId
    TrussFamilyDiagWebEndReleaseType: ForgeTypeId
    TrussFamilyVertWebStructuralTypesParam: ForgeTypeId
    TrussFamilyVertWebAngleParam: ForgeTypeId
    TrussFamilyVertWebStartReleaseType: ForgeTypeId
    TrussFamilyVertWebEndReleaseType: ForgeTypeId
    TrussElementTagNewMembersView: ForgeTypeId
    TrussNonBearingOffsetParam: ForgeTypeId
    TrussBearingChordTopBottomParam: ForgeTypeId
    TrussElementSpanParam: ForgeTypeId
    TrussElementStickJustParam: ForgeTypeId
    TrussFamilyWebsHaveSymbolicCutbackParam: ForgeTypeId
    TrussHeight: ForgeTypeId
    TrussFamilyTransformationParam: ForgeTypeId
    TrussElementRotateChordsWithTruss: ForgeTypeId
    TrussElementReferenceLevelParam: ForgeTypeId
    TrussElementEnd1Elevation: ForgeTypeId
    TrussElementEnd0Elevation: ForgeTypeId
    TrussElementBearingJustParam: ForgeTypeId
    TrussElementCreateBottomParam: ForgeTypeId
    TrussElementCreateTopParam: ForgeTypeId
    TrussElementAngleParam: ForgeTypeId
    TrussElementClassParam: ForgeTypeId
    TrussLength: ForgeTypeId
    BoundaryParamPresetArea: ForgeTypeId
    BoundaryParamPresetLinear: ForgeTypeId
    BoundaryParamPreset: ForgeTypeId
    BoundaryZTranslationSpring: ForgeTypeId
    BoundaryZTranslationFixed: ForgeTypeId
    BoundaryZRotationSpring: ForgeTypeId
    BoundaryZRotationFixed: ForgeTypeId
    BoundaryYTranslationSpring: ForgeTypeId
    BoundaryYTranslationFixed: ForgeTypeId
    BoundaryYRotationSpring: ForgeTypeId
    BoundaryYRotationFixed: ForgeTypeId
    BoundaryXTranslationSpring: ForgeTypeId
    BoundaryXTranslationFixed: ForgeTypeId
    BoundaryXRotationSpring: ForgeTypeId
    BoundaryXRotationFixed: ForgeTypeId
    BoundaryAreaRestraintZ: ForgeTypeId
    BoundaryAreaRestraintY: ForgeTypeId
    BoundaryAreaRestraintX: ForgeTypeId
    BoundaryLinearRestraintRotX: ForgeTypeId
    BoundaryLinearRestraintZ: ForgeTypeId
    BoundaryLinearRestraintY: ForgeTypeId
    BoundaryLinearRestraintX: ForgeTypeId
    BoundaryRestraintRotZ: ForgeTypeId
    BoundaryRestraintRotY: ForgeTypeId
    BoundaryRestraintRotX: ForgeTypeId
    BoundaryRestraintZ: ForgeTypeId
    BoundaryRestraintY: ForgeTypeId
    BoundaryRestraintX: ForgeTypeId
    BoundaryDirectionRotZ: ForgeTypeId
    BoundaryDirectionRotY: ForgeTypeId
    BoundaryDirectionRotX: ForgeTypeId
    BoundaryDirectionZ: ForgeTypeId
    BoundaryDirectionY: ForgeTypeId
    BoundaryDirectionX: ForgeTypeId
    BoundaryConditionsIsExt: ForgeTypeId
    BoundaryConditionsType: ForgeTypeId
    KeySourceParam: ForgeTypeId
    KeynoteParam: ForgeTypeId
    KeynoteNumber: ForgeTypeId
    SheetKeyNumber: ForgeTypeId
    KeynoteText: ForgeTypeId
    KeyValue: ForgeTypeId
    PhyMaterialParamGrade: ForgeTypeId
    PhyMaterialParamSpecies: ForgeTypeId
    PhyMaterialParamExpCoeff: ForgeTypeId
    PhyMaterialParamBending: ForgeTypeId
    PhyMaterialParamShearMod: ForgeTypeId
    PhyMaterialParamPoissonMod: ForgeTypeId
    PhyMaterialParamShearPerpendicular: ForgeTypeId
    PhyMaterialParamShearParallel: ForgeTypeId
    PhyMaterialParamCompressionPerpendicular: ForgeTypeId
    PhyMaterialParamCompressionParallel: ForgeTypeId
    PhyMaterialParamYoungMod: ForgeTypeId
    PhyMaterialParamType: ForgeTypeId
    ElemCategoryParamMt: ForgeTypeId
    ElemCategoryParam: ForgeTypeId
    MaterialVolume: ForgeTypeId
    MaterialArea: ForgeTypeId
    MaterialAspaint: ForgeTypeId
    MaterialName: ForgeTypeId
    RbsMepSizeHeightDefParam: ForgeTypeId
    RbsMepSizeDefParam: ForgeTypeId
    RbsPipeSlopeOptionsDefParam: ForgeTypeId
    FabricationServiceParam: ForgeTypeId
    ConnectorAngleOfDeflection: ForgeTypeId
    ConnectorLength: ForgeTypeId
    RbsDuctSystemCalculationParam: ForgeTypeId
    RbsPipeSystemCalculationParam: ForgeTypeId
    RbsPipingSystemTypeParam: ForgeTypeId
    RbsDuctSystemTypeParam: ForgeTypeId
    RbsSystemAbbreviationParam: ForgeTypeId
    MepSystemLineGraphicsOverridesParam: ForgeTypeId
    RbsPipeSlopeDefParam: ForgeTypeId
    ConnectorEngagementLength: ForgeTypeId
    RbsSystemFlowConversionMethodParam: ForgeTypeId
    RbsSystemNumElementsParam: ForgeTypeId
    RbsSystemBaseElementParam: ForgeTypeId
    RbsSystemClassificationParam: ForgeTypeId
    RbsSystemNameParam: ForgeTypeId
    PhyMaterialParamLightWeight: ForgeTypeId
    PhyMaterialParamBehavior: ForgeTypeId
    PhyMaterialParamResistanceCalcStrength: ForgeTypeId
    PhyMaterialParamReductionFactor: ForgeTypeId
    PhyMaterialParamMinimumTensileStrength: ForgeTypeId
    PhyMaterialParamMinimumYieldStress: ForgeTypeId
    PhyMaterialParamShearStrengthReduction: ForgeTypeId
    PhyMaterialParamShearReinforcement: ForgeTypeId
    PhyMaterialParamBendingReinforcement: ForgeTypeId
    PhyMaterialParamConcreteCompression: ForgeTypeId
    PhyMaterialParamExpCoeff3: ForgeTypeId
    PhyMaterialParamExpCoeff2: ForgeTypeId
    PhyMaterialParamExpCoeff1: ForgeTypeId
    PhyMaterialParamUnitWeight: ForgeTypeId
    PhyMaterialParamShearMod3: ForgeTypeId
    PhyMaterialParamShearMod2: ForgeTypeId
    PhyMaterialParamShearMod1: ForgeTypeId
    PhyMaterialParamPoissonMod3: ForgeTypeId
    PhyMaterialParamPoissonMod2: ForgeTypeId
    PhyMaterialParamPoissonMod1: ForgeTypeId
    PhyMaterialParamYoungMod3: ForgeTypeId
    PhyMaterialParamYoungMod2: ForgeTypeId
    PhyMaterialParamYoungMod1: ForgeTypeId
    PipeVelocityPressure: ForgeTypeId
    RbsPipeSizeMaximum: ForgeTypeId
    RbsPipeSizeMinimum: ForgeTypeId
    RbsDuctPressureDrop: ForgeTypeId
    RoutingPreferenceParam: ForgeTypeId
    RbsDuctRoutingPreferenceParam: ForgeTypeId
    RbsSegmentDescriptionParam: ForgeTypeId
    RbsPipeJointtypeParam: ForgeTypeId
    RbsPipeSegmentParam: ForgeTypeId
    RbsRoutingPreferenceParam: ForgeTypeId
    RbsParallelpipesVerticalOffsetValue: ForgeTypeId
    RbsParallelpipesHorizontalOffsetValue: ForgeTypeId
    RbsParallelpipesVerticalNumber: ForgeTypeId
    RbsParallelpipesHorizontalNumber: ForgeTypeId
    RbsParallelconduitsVerticalOffsetValue: ForgeTypeId
    RbsParallelconduitsHorizontalOffsetValue: ForgeTypeId
    RbsParallelconduitsVerticalNumber: ForgeTypeId
    RbsParallelconduitsHorizontalNumber: ForgeTypeId
    RbsConvertToFlexMaxLength: ForgeTypeId
    RbsFpSprinklerOrificeSizeParam: ForgeTypeId
    RbsFpSprinklerTemperatureRatingParam: ForgeTypeId
    RbsFpSprinklerKFactorParam: ForgeTypeId
    RbsFpSprinklerPressureClassParam: ForgeTypeId
    RbsFpSprinklerOrificeParam: ForgeTypeId
    RbsFpSprinklerCoverageParam: ForgeTypeId
    RbsFpSprinklerResponseParam: ForgeTypeId
    MepProfileTypeParam: ForgeTypeId
    RbsShowProfileType: ForgeTypeId
    RbsPipeSystemFixtureUnitParam: ForgeTypeId
    RbsPipeSlope: ForgeTypeId
    RbsDuctSlope: ForgeTypeId
    RbsCurveUtslope: ForgeTypeId
    RbsPipeVolumeParam: ForgeTypeId
    RbsPipeWfuParam: ForgeTypeId
    RbsPipeHwfuParam: ForgeTypeId
    RbsPipeCwfuParam: ForgeTypeId
    RbsPipeFlowConfigurationParam: ForgeTypeId
    RbsPipeFlowDirectionParam: ForgeTypeId
    RbsPipeFixtureUnitsParam: ForgeTypeId
    RbsPipeStaticPressure: ForgeTypeId
    RbsPipeInsulationThickness: ForgeTypeId
    RbsDuctBottomElevation: ForgeTypeId
    RbsDuctTopElevation: ForgeTypeId
    RbsPipeOuterDiameter: ForgeTypeId
    RbsPipeInvertElevation: ForgeTypeId
    RbsPipeTypeFittingLossMethodParam: ForgeTypeId
    RbsPipeTypeFittingLossTableParam: ForgeTypeId
    RbsPipeTypeFittingLossKfactorParam: ForgeTypeId
    RbsPipeTypeValveLossCvfactorParam: ForgeTypeId
    RbsPipeFittingLossMethodParam: ForgeTypeId
    RbsPipeFittingLossTableParam: ForgeTypeId
    RbsPipeFittingLossKfactorParam: ForgeTypeId
    RbsPipeValveLossCvfactorParam: ForgeTypeId
    RbsPipeAdditionalFlowParam: ForgeTypeId
    RbsPipeDiameterParam: ForgeTypeId
    RbsCurveSlope: ForgeTypeId
    RbsAdjustableConnector: ForgeTypeId
    RbsFlowFactorParam: ForgeTypeId
    RbsDuctFlowConfigurationParam: ForgeTypeId
    RbsDuctFlowDirectionParam: ForgeTypeId
    RbsPipeFluidTypeParam: ForgeTypeId
    RbsPipeFluidTemperatureParam: ForgeTypeId
    RbsPipeFluidViscosityParam: ForgeTypeId
    RbsPipeFluidDensityParam: ForgeTypeId
    RbsPipeFlowParam: ForgeTypeId
    RbsPipeInnerDiamParam: ForgeTypeId
    RbsPipeReynoldsNumberParam: ForgeTypeId
    RelativeRoughness: ForgeTypeId
    RbsPipeFlowStateParam: ForgeTypeId
    FrictionFactor: ForgeTypeId
    RbsPipeVelocityParam: ForgeTypeId
    RbsPipeFrictionParam: ForgeTypeId
    RbsPipePressuredropParam: ForgeTypeId
    PipeRoughness: ForgeTypeId
    RbsPipeMaterialParam: ForgeTypeId
    RbsPipeConnectiontypeParam: ForgeTypeId
    RbsPipeClassParam: ForgeTypeId
    RbsElecCircuitWireNumOthersParam: ForgeTypeId
    RbsElecCircuitState: ForgeTypeId
    PanelId: ForgeTypeId
    RbsElecDemandCurrentPhasec: ForgeTypeId
    RbsElecDemandCurrentPhaseb: ForgeTypeId
    RbsElecDemandCurrentPhasea: ForgeTypeId
    RbsElecDemandLoadPhasec: ForgeTypeId
    RbsElecDemandLoadPhaseb: ForgeTypeId
    RbsElecDemandLoadPhasea: ForgeTypeId
    RbsElecCircuitSlotIndex: ForgeTypeId
    CircuitWaysParam: ForgeTypeId
    CircuitLoadClassificationAbbreviationParam: ForgeTypeId
    CircuitPhaseParam: ForgeTypeId
    RbsElecCircuitNamingIndex: ForgeTypeId
    RbsElecCircuitConnectionTypeParam: ForgeTypeId
    RbsElecCircuitPathOffsetParam: ForgeTypeId
    RbsElecCircuitPathModeParam: ForgeTypeId
    RbsElecCircuitStartSlot: ForgeTypeId
    ConnectorGenderType: ForgeTypeId
    ConnectorJointType: ForgeTypeId
    RbsElecPanelConfigurationParam: ForgeTypeId
    RbsElecPanelLocationParam: ForgeTypeId
    PanelScheduleName: ForgeTypeId
    TemplateName: ForgeTypeId
    RbsElecPanelCurrentPhasecParam: ForgeTypeId
    RbsElecPanelCurrentPhasebParam: ForgeTypeId
    RbsElecPanelCurrentPhaseaParam: ForgeTypeId
    RbsElecLoadsummaryDemandFactorRuleParam: ForgeTypeId
    RbsElecLoadsummaryDemandCurrentParam: ForgeTypeId
    RbsElecLoadsummaryConnectedCurrentParam: ForgeTypeId
    RbsElecLoadsummaryDemandLoadParam: ForgeTypeId
    RbsElecLoadsummaryDemandFactorParam: ForgeTypeId
    RbsElecLoadsummaryConnectedLoadParam: ForgeTypeId
    RbsElecLoadsummaryLoadclassificationParam: ForgeTypeId
    RbsElecCircuitNotesParam: ForgeTypeId
    RbsElecCircuitNumberOfElementsParam: ForgeTypeId
    RbsElecCircuitFrameParam: ForgeTypeId
    RbsElecPanelTotalDemandCurrentParam: ForgeTypeId
    RbsElecPanelTotalConnectedCurrentParam: ForgeTypeId
    RbsElecPanelTotalDemandFactorParam: ForgeTypeId
    RbsElecPanelScheduleFooterNotesParam: ForgeTypeId
    RbsElecPanelScheduleHeaderNotesParam: ForgeTypeId
    RbsElecPanelNumwiresParam: ForgeTypeId
    RbsElecPanelNumphasesParam: ForgeTypeId
    RbsElecPanelNeutralRatingParam: ForgeTypeId
    RbsElecPanelNeutralBusParam: ForgeTypeId
    RbsElecPanelGroundBusParam: ForgeTypeId
    RbsElecPanelBussingParam: ForgeTypeId
    RbsElecPanelSubfeedLugsParam: ForgeTypeId
    RbsElecPanelSupplyFromParam: ForgeTypeId
    RbsElecPanelMcbRatingParam: ForgeTypeId
    RbsElecPanelMainstypeParam: ForgeTypeId
    RbsElecPanelFeedParam: ForgeTypeId
    RbsConduitrunOuterDiamParam: ForgeTypeId
    RbsConduitrunInnerDiamParam: ForgeTypeId
    RbsConduitrunDiameterParam: ForgeTypeId
    RbsCabletrayrunWidthParam: ForgeTypeId
    RbsCabletrayrunHeightParam: ForgeTypeId
    RbsCabletrayconduitrunLengthParam: ForgeTypeId
    RbsLoadSubClassificationMotor: ForgeTypeId
    RbsCabletrayShapetype: ForgeTypeId
    RbsCabletrayconduitBendorfitting: ForgeTypeId
    RbsCtcServiceType: ForgeTypeId
    RbsConduitOuterDiamParam: ForgeTypeId
    RbsConduitInnerDiamParam: ForgeTypeId
    RbsCtcBottomElevation: ForgeTypeId
    RbsCtcTopElevation: ForgeTypeId
    RbsConduitDiameterParam: ForgeTypeId
    RbsCabletrayWidthParam: ForgeTypeId
    RbsCabletrayHeightParam: ForgeTypeId
    CircuitLoadClassificationParam: ForgeTypeId
    CabletrayMinbendmultiplierParam: ForgeTypeId
    ConduitStandardTypeParam: ForgeTypeId
    RbsConduitTradesize: ForgeTypeId
    RbsConduitBendradius: ForgeTypeId
    RbsCabletrayBendradius: ForgeTypeId
    RbsCabletrayRungheight: ForgeTypeId
    RbsCabletrayRungwidth: ForgeTypeId
    RbsCabletrayRungspace: ForgeTypeId
    RbsCabletrayThickness: ForgeTypeId
    RbsElecSwitchIdParam: ForgeTypeId
    RbsWireCircuitDescription: ForgeTypeId
    RbsWireCircuitLoadName: ForgeTypeId
    RbsWireNumConductorsParam: ForgeTypeId
    RbsElecWireTickmarkState: ForgeTypeId
    RbsElecCircuitPanelParam: ForgeTypeId
    RbsElecCircuitNumber: ForgeTypeId
    RbsElecWireCircuits: ForgeTypeId
    RbsElecCircuitWireNumRunsParam: ForgeTypeId
    RbsElecCircuitWireNumHotsParam: ForgeTypeId
    RbsElecCircuitWireNumNeutralsParam: ForgeTypeId
    RbsElecCircuitWireNumGroundsParam: ForgeTypeId
    RbsElecWireType: ForgeTypeId
    RbsElecWireElevation: ForgeTypeId
    RbsElecWireHotAdjustment: ForgeTypeId
    RbsElecWireNeutralAdjustment: ForgeTypeId
    RbsElecWireGroundAdjustment: ForgeTypeId
    RbsElecWireShareNeutral: ForgeTypeId
    RbsElecWireShareGround: ForgeTypeId
    RbsElecCircuitName: ForgeTypeId
    RbsFamilyContentSecondaryDistribsys: ForgeTypeId
    RbsElecCircuitNaming: ForgeTypeId
    RbsElecCircuitPrefixSeparator: ForgeTypeId
    RbsElecCircuitPrefix: ForgeTypeId
    RbsElecModifications: ForgeTypeId
    RbsElecEnclosure: ForgeTypeId
    RbsElecMains: ForgeTypeId
    RbsElecMounting: ForgeTypeId
    RbsElecShortCircuitRating: ForgeTypeId
    RbsElecMaxPoleBreakers: ForgeTypeId
    RbsElecPanelName: ForgeTypeId
    RbsElecPanelTotalestloadHvacParam: ForgeTypeId
    RbsElecPanelTotalloadHvacParam: ForgeTypeId
    RbsElecPanelTotalestloadLightParam: ForgeTypeId
    RbsElecPanelTotalloadLightParam: ForgeTypeId
    RbsElecPanelTotalestloadPowerParam: ForgeTypeId
    RbsElecPanelTotalloadPowerParam: ForgeTypeId
    RbsElecPanelTotalestloadOtherParam: ForgeTypeId
    RbsElecPanelTotalloadOtherParam: ForgeTypeId
    RbsElecPanelTotalestloadParam: ForgeTypeId
    RbsElecPanelTotalloadParam: ForgeTypeId
    RbsElecDemandfactorLoadclassificationParam: ForgeTypeId
    RbsElecDemandfactorLoadParam: ForgeTypeId
    RbsElecDemandfactorDemandloadParam: ForgeTypeId
    RbsFamilyContentDistributionSystem: ForgeTypeId
    RbsDistributionsysVllParam: ForgeTypeId
    RbsDistributionsysVlgParam: ForgeTypeId
    RbsDistributionsysPhaseParam: ForgeTypeId
    RbsDistributionsysConfigParam: ForgeTypeId
    RbsDistributionsysNumwiresParam: ForgeTypeId
    RbsVoltagetypeVoltageParam: ForgeTypeId
    RbsVoltagetypeMinvoltageParam: ForgeTypeId
    RbsVoltagetypeMaxvoltageParam: ForgeTypeId
    RbsElecApparentLoadPhasec: ForgeTypeId
    RbsElecApparentLoadPhaseb: ForgeTypeId
    RbsElecApparentLoadPhasea: ForgeTypeId
    RbsElecTrueLoadPhasec: ForgeTypeId
    RbsElecTrueLoadPhaseb: ForgeTypeId
    RbsElecTrueLoadPhasea: ForgeTypeId
    RbsElecTrueCurrentParam: ForgeTypeId
    RbsElecTrueCurrentPhaseaParam: ForgeTypeId
    RbsElecTrueCurrentPhasebParam: ForgeTypeId
    RbsElecTrueCurrentPhasecParam: ForgeTypeId
    RbsElecApparentCurrentParam: ForgeTypeId
    RbsElecApparentCurrentPhaseaParam: ForgeTypeId
    RbsElecApparentCurrentPhasebParam: ForgeTypeId
    RbsElecApparentCurrentPhasecParam: ForgeTypeId
    RbsElecVoltageDropParam: ForgeTypeId
    RbsElecCalcCoefficientUtilization: ForgeTypeId
    RbsElecCircuitLengthParam: ForgeTypeId
    RbsElecCircuitRatingParam: ForgeTypeId
    RbsElecCircuitWireSizeParam: ForgeTypeId
    RbsElecCircuitWireTypeParam: ForgeTypeId
    RbsElecRoomCavityRatio: ForgeTypeId
    FbxLightPhotometricFile: ForgeTypeId
    RbsElecRoomAverageIllumination: ForgeTypeId
    RbsElecRoomReflectivityFloor: ForgeTypeId
    RbsElecRoomReflectivityWalls: ForgeTypeId
    RbsElecRoomReflectivityCeiling: ForgeTypeId
    RbsElecRoomLightingCalcWorkplane: ForgeTypeId
    RbsWireMaterialParam: ForgeTypeId
    RbsWireTemperatureRatingParam: ForgeTypeId
    RbsWireInsulationParam: ForgeTypeId
    RbsWireMaxConductorSizeParam: ForgeTypeId
    RbsWireNeutralMultiplierParam: ForgeTypeId
    RbsWireNeutralIncludedInBalancedLoadParam: ForgeTypeId
    RbsWireNeutralModeParam: ForgeTypeId
    RbsWireConduitTypeParam: ForgeTypeId
    RbsElecAmbientTemperature: ForgeTypeId
    RbsElecCircuitType: ForgeTypeId
    RbsElecLoadClassification: ForgeTypeId
    RbsElecTrueLoadPhase3: ForgeTypeId
    RbsElecTrueLoadPhase2: ForgeTypeId
    RbsElecTrueLoadPhase1: ForgeTypeId
    RbsElecTrueLoad: ForgeTypeId
    RbsElecPowerFactorState: ForgeTypeId
    RbsElecPowerFactor: ForgeTypeId
    RbsElecApparentLoadPhase3: ForgeTypeId
    RbsElecApparentLoadPhase2: ForgeTypeId
    RbsElecApparentLoadPhase1: ForgeTypeId
    RbsElecApparentLoad: ForgeTypeId
    RbsElecBalancedLoad: ForgeTypeId
    RbsElecVoltage: ForgeTypeId
    RbsElecNumberOfPoles: ForgeTypeId
    RbsConnectorDescription: ForgeTypeId
    ViewFamilySchedules: ForgeTypeId
    ViewFamilyAndTypeSchedules: ForgeTypeId
    ViewTypeSchedules: ForgeTypeId
    MarkupsPrivate: ForgeTypeId
    MarkupsNotes: ForgeTypeId
    MarkupsHistory: ForgeTypeId
    MarkupsStatus: ForgeTypeId
    MarkupsLabel: ForgeTypeId
    MarkupsCreator: ForgeTypeId
    MarkupsCreated: ForgeTypeId
    MarkupsModified: ForgeTypeId
    ViewSchemaSettingForSystemTemplate: ForgeTypeId
    LegendComponentDetailLevel: ForgeTypeId
    LegendComponentLength: ForgeTypeId
    LegendComponentView: ForgeTypeId
    LegendComponent: ForgeTypeId
    OptionSetId: ForgeTypeId
    OptionName: ForgeTypeId
    PrimaryOptionId: ForgeTypeId
    OptionSetName: ForgeTypeId
    GroupAttachedParentName: ForgeTypeId
    GroupAllowedViewTypes: ForgeTypeId
    GroupOffsetFromLevel: ForgeTypeId
    GroupLevel: ForgeTypeId
    MepSystemFillGraphicsOverridesParam: ForgeTypeId
    DuctTerminalEngagementLength: ForgeTypeId
    ConnectorInsideDiameter: ForgeTypeId
    ConnectorDiameter: ForgeTypeId
    RbsCabletrayconduitConnectorelemType: ForgeTypeId
    RbsCabletrayconduitSystemType: ForgeTypeId
    RbsConnectorIsprimary: ForgeTypeId
    ConnectorReferenceIndex: ForgeTypeId
    RbsPipeConnectorSystemClassificationParam: ForgeTypeId
    ConnectorAngle: ForgeTypeId
    RbsDuctConnectorSystemClassificationParam: ForgeTypeId
    ConnectorIndex: ForgeTypeId
    ConnectorVisibleSize: ForgeTypeId
    ConnectorHeight: ForgeTypeId
    ConnectorWidth: ForgeTypeId
    ConnectorRadius: ForgeTypeId
    ConnectorProfileType: ForgeTypeId
    TagOnFraming: ForgeTypeId
    TagOnSystem: ForgeTypeId
    TagOnPlacementStructural: ForgeTypeId
    CreateChain: ForgeTypeId
    WorkPlaneParam: ForgeTypeId
    MakeSurfaceFromClosedLoops: ForgeTypeId
    PlaneSelectionParam: ForgeTypeId
    PlaneShowParam: ForgeTypeId
    Use3dSnapping: ForgeTypeId
    ArcElemFixKeepConcentric: ForgeTypeId
    PipingGenderType: ForgeTypeId
    PipingConnectionType: ForgeTypeId
    RbsPartType: ForgeTypeId
    StructuralConnectionEditRangesOfApplicability: ForgeTypeId
    AnalyticalOpeningWidth: ForgeTypeId
    AnalyticalOpeningHeight: ForgeTypeId
    AnalyticalSurfaceWidth: ForgeTypeId
    AnalyticalSurfaceHeight: ForgeTypeId
    EnergyAnalysisZoneDataJson: ForgeTypeId
    EnergyAnalysisWindowTypeJson: ForgeTypeId
    EnergyAnalysisConstructionJson: ForgeTypeId
    EnergyAnalysisSpaceJson: ForgeTypeId
    WindowtypeIsSchematic: ForgeTypeId
    ThermalMaterialSpecificHeatCapacity: ForgeTypeId
    ThermalMaterialDensity: ForgeTypeId
    ThermalMaterialConductivity: ForgeTypeId
    ThermalMaterialThickness: ForgeTypeId
    ThermalMaterialDescription: ForgeTypeId
    ThermalMaterialName: ForgeTypeId
    SpaceComposednameParam: ForgeTypeId
    SpaceNumberParam: ForgeTypeId
    ConstructionIsSchematic: ForgeTypeId
    AnalyticalZoneName: ForgeTypeId
    ZoneDesignCoolTemperature: ForgeTypeId
    ZoneDesignHeatTemperature: ForgeTypeId
    ZoneOutsideAirFlowPerPerson: ForgeTypeId
    ZoneOutsideAirFlowPerArea: ForgeTypeId
    ZoneAirChangesPerHour: ForgeTypeId
    AnalyticalZone: ForgeTypeId
    SpaceNumberOfPeople: ForgeTypeId
    SpaceConditionType: ForgeTypeId
    SpaceTypeGbxml: ForgeTypeId
    AnalyticalSurface: ForgeTypeId
    SurfaceName: ForgeTypeId
    OriginatingElementName: ForgeTypeId
    WindowTypeName: ForgeTypeId
    ConstructionName: ForgeTypeId
    AnalyticConstruction: ForgeTypeId
    Tilt: ForgeTypeId
    Azimuth: ForgeTypeId
    AnalyticalAdjacentSpace: ForgeTypeId
    AnalyticalSpace: ForgeTypeId
    SpaceNameParam: ForgeTypeId
    SystemsAnalysisReportFolder: ForgeTypeId
    SystemsAnalysisReportStyle: ForgeTypeId
    EnergyAnalysisProjectPhase: ForgeTypeId
    SpaceVolume: ForgeTypeId
    SpaceArea: ForgeTypeId
    PeakLatentCoolingLoad: ForgeTypeId
    PeakAirflowParam: ForgeTypeId
    SpaceReferenceLevelParam: ForgeTypeId
    SpaceInfiltrationAirflow: ForgeTypeId
    SpaceInfiltrationAirflowPerArea: ForgeTypeId
    SpaceOutdoorAirflow: ForgeTypeId
    SpaceOutdoorAirflowPerPerson: ForgeTypeId
    SpaceOutdoorAirflowPerArea: ForgeTypeId
    SpaceAirChangesPerHour: ForgeTypeId
    SpacePowerLoadParam: ForgeTypeId
    SpaceLightingLoadParam: ForgeTypeId
    SpacePeopleLoadParam: ForgeTypeId
    SpacePowerLoadPerAreaParam: ForgeTypeId
    SpaceLightingLoadPerAreaParam: ForgeTypeId
    SpacePeopleLatentHeatGainPerPersonParam: ForgeTypeId
    SpacePeopleSensibleHeatGainPerPersonParam: ForgeTypeId
    SpaceAreaPerPersonParam: ForgeTypeId
    SpaceAirflowPerAreaParam: ForgeTypeId
    PeakCoolingLoadParam: ForgeTypeId
    PeakHeatingLoadParam: ForgeTypeId
    SystemZoneVolume: ForgeTypeId
    SystemZoneArea: ForgeTypeId
    SpaceDehumidificationSetPoint: ForgeTypeId
    SpaceHumidificationSetPoint: ForgeTypeId
    SpaceCoolingSetPoint: ForgeTypeId
    SpaceHeatingSetPoint: ForgeTypeId
    ZoneLevelOffsetTop: ForgeTypeId
    ZoneLevelOffset: ForgeTypeId
    SystemZoneLevelId: ForgeTypeId
    ZoneCalculatedHydronicCoolingflowParam: ForgeTypeId
    ZoneCalculatedHydronicHeatingflowParam: ForgeTypeId
    ZoneSpaceOutdoorAirOptionParam: ForgeTypeId
    RbsGbxmlOpeningType: ForgeTypeId
    RoomCalculationPoint: ForgeTypeId
    GridBankColWidth: ForgeTypeId
    GridBankRowHeight: ForgeTypeId
    GridBankColNum: ForgeTypeId
    GridBankRowNum: ForgeTypeId
    RbsCurvetypeDefaultBendParam: ForgeTypeId
    RbsCurvetypeDefaultHorizontalBendParam: ForgeTypeId
    RbsCurvetypeMultishapeTransitionOvalroundParam: ForgeTypeId
    RbsCurvetypeMultishapeTransitionRectovalParam: ForgeTypeId
    RbsCurvetypeDefaultTeedownParam: ForgeTypeId
    RbsCurvetypeDefaultTeeupParam: ForgeTypeId
    RbsCurvetypeDefaultElbowdownParam: ForgeTypeId
    RbsCurvetypeDefaultElbowupParam: ForgeTypeId
    RbsEnergyAnalysisExportCategoryParam: ForgeTypeId
    RbsEnergyAnalysisExportComplexityParam: ForgeTypeId
    SpaceZoneName: ForgeTypeId
    RbsEnergyAnalysisExportGbxmlDefaultsParam: ForgeTypeId
    RbsHvacloadPlenumCoolingLoadParam: ForgeTypeId
    RbsHvacloadSkylightCoolingLoadParam: ForgeTypeId
    RbsHvacloadPartitionCoolingLoadParam: ForgeTypeId
    RbsHvacloadDoorCoolingLoadParam: ForgeTypeId
    RbsHvacloadWindowCoolingLoadParam: ForgeTypeId
    RbsHvacloadWallCoolingLoadParam: ForgeTypeId
    RbsHvacloadRoofCoolingLoadParam: ForgeTypeId
    RbsHvacloadSkylightAreaParam: ForgeTypeId
    RbsHvacloadPartitionAreaParam: ForgeTypeId
    RbsHvacloadFloorAreaParam: ForgeTypeId
    RbsHvacloadDoorAreaParam: ForgeTypeId
    RbsHvacloadWindowAreaParam: ForgeTypeId
    RbsHvacloadWallAreaParam: ForgeTypeId
    RbsHvacloadRoofAreaParam: ForgeTypeId
    RbsLiningThicknessForDuct: ForgeTypeId
    RbsInsulationThicknessForPipe: ForgeTypeId
    RbsInsulationThicknessForDuct: ForgeTypeId
    BuildingUnoccupiedCoolingSetPointParam: ForgeTypeId
    BuildingClosingTimeParam: ForgeTypeId
    BuildingOpeningTimeParam: ForgeTypeId
    SpacePeopleActivityLevelParam: ForgeTypeId
    SpaceElecEquipmentRadiantPercentageParam: ForgeTypeId
    SpacePowerScheduleParam: ForgeTypeId
    SpaceLightingScheduleParam: ForgeTypeId
    SpaceOccupancyScheduleParam: ForgeTypeId
    SpaceInfiltrationParam: ForgeTypeId
    SpaceCarpetingParam: ForgeTypeId
    ZoneAirVolumeCalculationTypeParam: ForgeTypeId
    ZoneCoilBypassPercentageParam: ForgeTypeId
    ZoneCalculatedAreaPerCoolingLoadParam: ForgeTypeId
    ZoneCalculatedAreaPerHeatingLoadParam: ForgeTypeId
    ZoneUseAirChangesPerHourParam: ForgeTypeId
    ZoneUseOutsideAirPerAreaParam: ForgeTypeId
    ZoneUseOutsideAirPerPersonParam: ForgeTypeId
    ZoneUseDehumidificationSetpointParam: ForgeTypeId
    ZoneUseHumidificationSetpointParam: ForgeTypeId
    ZoneOutdoorAirInformationParam: ForgeTypeId
    ZoneCoolingInformationParam: ForgeTypeId
    ZoneHeatingInformationParam: ForgeTypeId
    RbsEnergyAnalysisSliverSpaceTolerance: ForgeTypeId
    ZoneAreaGross: ForgeTypeId
    ZoneVolumeGross: ForgeTypeId
    SpaceIsPlenum: ForgeTypeId
    SpaceIsOccupiable: ForgeTypeId
    SpaceAssocRoomNumber: ForgeTypeId
    SpaceAssocRoomName: ForgeTypeId
    ZonePhase: ForgeTypeId
    ZonePhaseId: ForgeTypeId
    RbsEnergyAnalysisProjectPhaseParam: ForgeTypeId
    RoomCalculatedSupplyAirflowPerAreaParam: ForgeTypeId
    RoomCalculatedCoolingLoadPerAreaParam: ForgeTypeId
    RoomCalculatedHeatingLoadPerAreaParam: ForgeTypeId
    ZoneCalculatedSupplyAirflowPerAreaParam: ForgeTypeId
    ZoneCalculatedCoolingLoadPerAreaParam: ForgeTypeId
    ZoneCalculatedHeatingLoadPerAreaParam: ForgeTypeId
    ZoneLevelId: ForgeTypeId
    ZoneOaRatePerAchParam: ForgeTypeId
    ZoneOutsideAirPerAreaParam: ForgeTypeId
    ZoneOutsideAirPerPersonParam: ForgeTypeId
    ZoneDehumidificationSetPointParam: ForgeTypeId
    ZoneHumidificationSetPointParam: ForgeTypeId
    ZoneCoolingAirTemperatureParam: ForgeTypeId
    ZoneHeatingAirTemperatureParam: ForgeTypeId
    ZoneCoolingSetPointParam: ForgeTypeId
    ZoneHeatingSetPointParam: ForgeTypeId
    ZoneCalculatedSupplyAirflowParam: ForgeTypeId
    ZoneCalculatedCoolingLoadParam: ForgeTypeId
    ZoneCalculatedHeatingLoadParam: ForgeTypeId
    ZoneServiceTypeParam: ForgeTypeId
    ZoneVolume: ForgeTypeId
    ZonePerimeter: ForgeTypeId
    ZoneArea: ForgeTypeId
    ZoneName: ForgeTypeId
    RbsProjectConstructionTypeShadingfactorParam: ForgeTypeId
    RbsConstructionTypeShadingfactorParam: ForgeTypeId
    RbsEnergyAnalysisGroundPlaneParam: ForgeTypeId
    RoomEditElectricalLoadsParam: ForgeTypeId
    RoomEditPeopleLoadsParam: ForgeTypeId
    RbsProjectLocationParam: ForgeTypeId
    RoomActualLightingLoadPerAreaParam: ForgeTypeId
    RoomActualPowerLoadPerAreaParam: ForgeTypeId
    RoomBaseHeatLoadOnParam: ForgeTypeId
    RoomLightingLoadUnitsParam: ForgeTypeId
    RoomPowerLoadUnitsParam: ForgeTypeId
    RoomDesignCoolingLoadParam: ForgeTypeId
    RoomCalculatedCoolingLoadParam: ForgeTypeId
    RoomDesignHeatingLoadParam: ForgeTypeId
    RoomCalculatedHeatingLoadParam: ForgeTypeId
    RoomBaseReturnAirflowOnParam: ForgeTypeId
    RoomConstructionSetParam: ForgeTypeId
    RbsConstructionSetParam: ForgeTypeId
    RbsServiceTypeParam: ForgeTypeId
    RbsGbxmlSurfaceArea: ForgeTypeId
    RbsGbxmlSurfaceType: ForgeTypeId
    FamilyElectricalMaintainAnnotationOrientation: ForgeTypeId
    RbsFamilyContentAnnotationDisplay: ForgeTypeId
    RbsElectricalData: ForgeTypeId
    RbsCalculatedSize: ForgeTypeId
    RoomPeopleSensibleHeatGainPerPersonParam: ForgeTypeId
    RbsIsCustomFitting: ForgeTypeId
    RbsConnectorOffsetObsolete: ForgeTypeId
    RbsLookupTableName: ForgeTypeId
    RoomDesignLightingLoadParam: ForgeTypeId
    RoomDesignPowerLoadParam: ForgeTypeId
    RoomActualLightingLoadParam: ForgeTypeId
    RoomActualPowerLoadParam: ForgeTypeId
    RoomBaseLightingLoadOnParam: ForgeTypeId
    RoomBasePowerLoadOnParam: ForgeTypeId
    RoomDesignOtherLoadPerAreaParam: ForgeTypeId
    RoomDesignMechanicalLoadPerAreaParam: ForgeTypeId
    RoomDesignLightingLoadPerAreaParam: ForgeTypeId
    RoomDesignPowerLoadPerAreaParam: ForgeTypeId
    FbxLightBallastLoss: ForgeTypeId
    FbxLightTotalLightLoss: ForgeTypeId
    RbsRoomCoefficientUtilization: ForgeTypeId
    RbsFamilyContentTakeoffFixedLength: ForgeTypeId
    RbsFamilyContentTakeoffProjlength: ForgeTypeId
    RbsFamilyContentTakeoffLength: ForgeTypeId
    RbsFamilyContentOffsetHeight: ForgeTypeId
    RbsFamilyContentOffsetWidth: ForgeTypeId
    FamilyContentPartType: ForgeTypeId
    GbxmlEditDataParam: ForgeTypeId
    RoomActualExhaustAirflowParam: ForgeTypeId
    RoomActualReturnAirflowParam: ForgeTypeId
    RoomActualSupplyAirflowParam: ForgeTypeId
    RoomPeopleLatentHeatGainPerPersonParam: ForgeTypeId
    RoomPeopleTotalHeatGainPerPersonParam: ForgeTypeId
    RoomCalculatedSupplyAirflowParam: ForgeTypeId
    RoomDesignExhaustAirflowParam: ForgeTypeId
    RoomDesignReturnAirflowParam: ForgeTypeId
    RoomDesignSupplyAirflowParam: ForgeTypeId
    RoomAreaPerPersonParam: ForgeTypeId
    RoomNumberOfPeopleParam: ForgeTypeId
    RoomOccupancyUnitParam: ForgeTypeId
    RoomSpaceTypeParam: ForgeTypeId
    RoomConditionTypeParam: ForgeTypeId
    ProjectPostalCode: ForgeTypeId
    ProjectBuildingType: ForgeTypeId
    RbsSizeLock: ForgeTypeId
    RbsAdditionalFlow: ForgeTypeId
    RbsCurvetypeMaxWidthParam: ForgeTypeId
    RbsPipeFittingLossMethodSettings: ForgeTypeId
    RbsDuctFittingLossMethodSettings: ForgeTypeId
    RbsCurvetypeDefaultCapParam: ForgeTypeId
    RbsPipeFittingLossMethodServerParam: ForgeTypeId
    RbsDuctFittingLossMethodServerParam: ForgeTypeId
    RbsCurvetypeDefaultMechjointParam: ForgeTypeId
    RbsPipeSizeFormattedParam: ForgeTypeId
    RbsDuctSizeFormattedParam: ForgeTypeId
    RbsDuctStaticPressure: ForgeTypeId
    RbsFlexPipeTypeParam: ForgeTypeId
    RbsPipeTypeParam: ForgeTypeId
    RbsFlexDuctTypeParam: ForgeTypeId
    RbsDuctTypeParam: ForgeTypeId
    RbsDuctFittingLossTableParam: ForgeTypeId
    RbsDuctFittingLossMethodParam: ForgeTypeId
    RbsFlexductRoundtypeParam: ForgeTypeId
    RbsCurvetypePreferredBranchParam: ForgeTypeId
    RbsCurvetypeDefaultTakeoffParam: ForgeTypeId
    RbsOffsetParam: ForgeTypeId
    RbsCurvetypeDefaultUnionParam: ForgeTypeId
    RbsHydraulicDiameterParam: ForgeTypeId
    RbsReynoldsnumberParam: ForgeTypeId
    RbsEqDiameterParam: ForgeTypeId
    RbsCurvetypeMultishapeTransitionParam: ForgeTypeId
    RbsSection: ForgeTypeId
    RbsLossCoefficient: ForgeTypeId
    RbsMaxFlow: ForgeTypeId
    RbsMinFlow: ForgeTypeId
    RbsVelocityPressure: ForgeTypeId
    RbsCurveSurfaceArea: ForgeTypeId
    RbsCurvetypeMaxHeightParam: ForgeTypeId
    RbsLiningThickness: ForgeTypeId
    RbsInsulationThickness: ForgeTypeId
    RbsFriction: ForgeTypeId
    DuctRoughness: ForgeTypeId
    RbsCurvetypeDefaultTransitionParam: ForgeTypeId
    RbsCurvetypeDefaultCrossParam: ForgeTypeId
    RbsCurvetypeDefaultTeeParam: ForgeTypeId
    RbsCurvetypeDefaultElbowParam: ForgeTypeId
    RbsPressureDrop: ForgeTypeId
    RbsVelocity: ForgeTypeId
    RbsCurveVertOffsetParam: ForgeTypeId
    RbsCurveHorOffsetParam: ForgeTypeId
    RbsFlowObsolete: ForgeTypeId
    RbsCurveDiameterParam: ForgeTypeId
    RbsCurveHeightParam: ForgeTypeId
    RbsCurveWidthParam: ForgeTypeId
    RbsFlexPatternParam: ForgeTypeId
    RbsEndOffsetParam: ForgeTypeId
    RbsStartOffsetParam: ForgeTypeId
    RbsEndLevelParam: ForgeTypeId
    RbsStartLevelParam: ForgeTypeId
    AnalyticalMemberUseOffsetInAnalysis: ForgeTypeId
    AnalyticalMemberOffsetEndZ: ForgeTypeId
    AnalyticalMemberOffsetEndY: ForgeTypeId
    AnalyticalMemberOffsetEndX: ForgeTypeId
    AnalyticalMemberOffsetStartZ: ForgeTypeId
    AnalyticalMemberOffsetStartY: ForgeTypeId
    AnalyticalMemberOffsetStartX: ForgeTypeId
    AnalyticalMemberForceEndAllNonZero: ForgeTypeId
    AnalyticalMemberForceStartAllNonZero: ForgeTypeId
    StructuralMemberForces: ForgeTypeId
    AnalyticalMemberForceEndMz: ForgeTypeId
    AnalyticalMemberForceEndMy: ForgeTypeId
    AnalyticalMemberForceEndMx: ForgeTypeId
    AnalyticalMemberForceEndFz: ForgeTypeId
    AnalyticalMemberForceEndFy: ForgeTypeId
    AnalyticalMemberForceEndFx: ForgeTypeId
    AnalyticalMemberForceStartMz: ForgeTypeId
    AnalyticalMemberForceStartMy: ForgeTypeId
    AnalyticalMemberForceStartMx: ForgeTypeId
    AnalyticalMemberForceStartFz: ForgeTypeId
    AnalyticalMemberForceStartFy: ForgeTypeId
    AnalyticalMemberForceStartFx: ForgeTypeId
    DividedpathTotalPathLength: ForgeTypeId
    DividedpathDisplayNodeNumbers: ForgeTypeId
    DividedpathMergedPointNum: ForgeTypeId
    DividedpathDisplayNodes: ForgeTypeId
    DividedpathDisplayReferenceCurves: ForgeTypeId
    DividedpathJustification: ForgeTypeId
    DividedpathLayoutFixedNumPoint: ForgeTypeId
    DividedpathFlipDirection: ForgeTypeId
    DividedpathMeasurementType: ForgeTypeId
    DividedpathMaxDistance: ForgeTypeId
    DividedpathMinDistance: ForgeTypeId
    DividedpathEndIndent: ForgeTypeId
    DividedpathBeginningIndent: ForgeTypeId
    DividedpathDistance: ForgeTypeId
    DividedpathLayout: ForgeTypeId
    NumberOfLeaders: ForgeTypeId
    DumpIdAction: ForgeTypeId
    DumpIdMode: ForgeTypeId
    DumpElementIds: ForgeTypeId
    SketchingOffsetTo: ForgeTypeId
    SketchingLockAlignment: ForgeTypeId
    SketchingSides: ForgeTypeId
    SketchingJoinStatus: ForgeTypeId
    SketchingRadius: ForgeTypeId
    SketchingRadiusToggle: ForgeTypeId
    SketchingOffset: ForgeTypeId
    SketchingChain: ForgeTypeId
    LineStyle: ForgeTypeId
    WallSweepPlacementVertical: ForgeTypeId
    WallSweepPlacementHorizontal: ForgeTypeId
    WallSweepReturnAngle: ForgeTypeId
    ArrayTypeParameter: ForgeTypeId
    ArrayInstanceParameter: ForgeTypeId
    ArrayLabel: ForgeTypeId
    ArrayTypeIndex: ForgeTypeId
    ArrayMoveTo: ForgeTypeId
    ArrayNumber: ForgeTypeId
    ArrayGroupAndAssociate: ForgeTypeId
    ArrayElementsAppendToEnd: ForgeTypeId
    RotateEastwest: ForgeTypeId
    RotateTruenorthAngle: ForgeTypeId
    RotateOriginplacement: ForgeTypeId
    RotateAngle: ForgeTypeId
    RotateCopy: ForgeTypeId
    RotateDisjoin: ForgeTypeId
    MirrorCopy: ForgeTypeId
    MoveMultiple: ForgeTypeId
    MoveDisjoin: ForgeTypeId
    MoveConstrain: ForgeTypeId
    AlignmentStationLabelSetEndStation: ForgeTypeId
    AlignmentStationLabelSetStartStation: ForgeTypeId
    AlignmentStationLabelSetInterval: ForgeTypeId
    AlignmentStationLabelSetOffset: ForgeTypeId
    WallTaperedWidthAtBottom: ForgeTypeId
    WallTaperedWidthAtTop: ForgeTypeId
    WallTaperedUseInstanceAngles: ForgeTypeId
    WallTypeWidthMeasuredAt: ForgeTypeId
    WallTypeDefaultTaperedInteriorInwardAngle: ForgeTypeId
    WallTypeDefaultTaperedExteriorInwardAngle: ForgeTypeId
    WallTaperedInteriorInwardAngle: ForgeTypeId
    WallTaperedExteriorInwardAngle: ForgeTypeId
    WallSingleSlantAngleFromVertical: ForgeTypeId
    WallCrossSection: ForgeTypeId
    IfcImportMaterialName: ForgeTypeId
    IfcExportPredefinedtypeType: ForgeTypeId
    IfcExportPredefinedtype: ForgeTypeId
    IfcExportElementTypeAs: ForgeTypeId
    IfcExportElementAs: ForgeTypeId
    IfcExportElementType: ForgeTypeId
    IfcExportElement: ForgeTypeId
    IfcOrganization: ForgeTypeId
    IfcApplicationVersion: ForgeTypeId
    IfcApplicationName: ForgeTypeId
    ProjectOrganizationName: ForgeTypeId
    ProjectOrganizationDescription: ForgeTypeId
    ProjectBuildingName: ForgeTypeId
    ProjectAuthor: ForgeTypeId
    IfcSiteGuid: ForgeTypeId
    IfcBuildingGuid: ForgeTypeId
    IfcProjectGuid: ForgeTypeId
    IfcTypeGuid: ForgeTypeId
    IfcGuid: ForgeTypeId
    StructConnectionTypeName: ForgeTypeId
    StructConnectionCutback: ForgeTypeId
    StructConnectionColumnBase: ForgeTypeId
    StructConnectionColumnTop: ForgeTypeId
    StructConnectionBeamEnd: ForgeTypeId
    StructConnectionBeamStart: ForgeTypeId
    StructConnectionApplyTo: ForgeTypeId
    LeaderOrientation: ForgeTypeId
    LeaderAngle: ForgeTypeId
    LeaderLength: ForgeTypeId
    RebarContainerBarType: ForgeTypeId
    ReinforcementMass: ForgeTypeId
    ReinforcementVolume: ForgeTypeId
    ReinEstBarVolume: ForgeTypeId
    ReinEstBarLength: ForgeTypeId
    ReinEstNumberOfBars: ForgeTypeId
    PathReinShapen2: ForgeTypeId
    PathReinShapen1: ForgeTypeId
    PathReinSpanlengthAltOffset: ForgeTypeId
    PathReinSpanlengthBarlengthAlt: ForgeTypeId
    PathReinSpanlengthBarlengthPrim: ForgeTypeId
    PathReinSpanlengthTopAlt: ForgeTypeId
    PathReinEndSpanhookAlt: ForgeTypeId
    PathReinEndSpanhookPrim: ForgeTypeId
    PathReinSummary: ForgeTypeId
    PathReinSpanlengthBottomAlt: ForgeTypeId
    PathReinSpanlengthBottomPrim: ForgeTypeId
    PathReinSpanhookAlt: ForgeTypeId
    PathReinSpanhookPrim: ForgeTypeId
    PathReinAddlOffset: ForgeTypeId
    PathReinAltOffset: ForgeTypeId
    PathReinEndHookOrient2Wall: ForgeTypeId
    PathReinEndHookOrient1Wall: ForgeTypeId
    PathReinEndHookOrient2Slab: ForgeTypeId
    PathReinEndHookOrient1Slab: ForgeTypeId
    PathReinEndHookTypen2: ForgeTypeId
    PathReinEndHookTypen1: ForgeTypeId
    PathReinHookOrient2Wall: ForgeTypeId
    PathReinHookOrient1Wall: ForgeTypeId
    PathReinHookOrient2Slab: ForgeTypeId
    PathReinHookOrient1Slab: ForgeTypeId
    PathReinHookTypen2: ForgeTypeId
    PathReinHookTypen1: ForgeTypeId
    PathReinLengthn2: ForgeTypeId
    PathReinLengthn1: ForgeTypeId
    PathReinTypen2: ForgeTypeId
    PathReinTypen1: ForgeTypeId
    PathReinAlternating: ForgeTypeId
    PathReinNumberOfBars: ForgeTypeId
    PathReinSpacing: ForgeTypeId
    PathReinFaceWall: ForgeTypeId
    PathReinFaceSlab: ForgeTypeId
    RebarBarMassPerUnitLength: ForgeTypeId
    RebarBarCrankLengths: ForgeTypeId
    RebarBarDeformationType: ForgeTypeId
    RebarSystemSpacingBottomDir2Generic: ForgeTypeId
    RebarSystemSpacingBottomDir1Generic: ForgeTypeId
    RebarSystemSpacingTopDir2Generic: ForgeTypeId
    RebarSystemSpacingTopDir1Generic: ForgeTypeId
    RebarSystemNumberOfLinesBottomDir2Generic: ForgeTypeId
    RebarSystemNumberOfLinesBottomDir1Generic: ForgeTypeId
    RebarSystemNumberOfLinesTopDir2Generic: ForgeTypeId
    RebarSystemNumberOfLinesTopDir1Generic: ForgeTypeId
    RebarSystemBarTypeBottomDir2Generic: ForgeTypeId
    RebarSystemBarTypeBottomDir1Generic: ForgeTypeId
    RebarSystemBarTypeTopDir2Generic: ForgeTypeId
    RebarSystemBarTypeTopDir1Generic: ForgeTypeId
    RebarSystemActiveBottomDir2Generic: ForgeTypeId
    RebarSystemActiveBottomDir1Generic: ForgeTypeId
    RebarSystemActiveTopDir2Generic: ForgeTypeId
    RebarSystemActiveTopDir1Generic: ForgeTypeId
    RebarSystemSpacingBackDirn2: ForgeTypeId
    RebarSystemSpacingBackDirn1: ForgeTypeId
    RebarSystemSpacingFrontDirn2: ForgeTypeId
    RebarSystemSpacingFrontDirn1: ForgeTypeId
    RebarSystemNumberOfLinesBackDirn2: ForgeTypeId
    RebarSystemNumberOfLinesBackDirn1: ForgeTypeId
    RebarSystemNumberOfLinesFrontDirn2: ForgeTypeId
    RebarSystemNumberOfLinesFrontDirn1: ForgeTypeId
    RebarSystemHookTypeBackDirn2: ForgeTypeId
    RebarSystemHookTypeBackDirn1: ForgeTypeId
    RebarSystemHookTypeFrontDirn2: ForgeTypeId
    RebarSystemHookTypeFrontDirn1: ForgeTypeId
    RebarSystemHookOrientBackDirn2: ForgeTypeId
    RebarSystemHookOrientBackDirn1: ForgeTypeId
    RebarSystemHookOrientFrontDirn2: ForgeTypeId
    RebarSystemHookOrientFrontDirn1: ForgeTypeId
    RebarSystemBarTypeBackDirn2: ForgeTypeId
    RebarSystemBarTypeBackDirn1: ForgeTypeId
    RebarSystemBarTypeFrontDirn2: ForgeTypeId
    RebarSystemBarTypeFrontDirn1: ForgeTypeId
    RebarSystemActiveBackDirn2: ForgeTypeId
    RebarSystemActiveBackDirn1: ForgeTypeId
    RebarSystemActiveFrontDirn2: ForgeTypeId
    RebarSystemActiveFrontDirn1: ForgeTypeId
    RebarSystemSpacingBottomDirn2: ForgeTypeId
    RebarSystemSpacingBottomDirn1: ForgeTypeId
    RebarSystemSpacingTopDirn2: ForgeTypeId
    RebarSystemSpacingTopDirn1: ForgeTypeId
    RebarSystemNumberOfLinesBottomDirn2: ForgeTypeId
    RebarSystemNumberOfLinesBottomDirn1: ForgeTypeId
    RebarSystemNumberOfLinesTopDirn2: ForgeTypeId
    RebarSystemNumberOfLinesTopDirn1: ForgeTypeId
    RebarSystemHookTypeBottomDirn2: ForgeTypeId
    RebarSystemHookTypeBottomDirn1: ForgeTypeId
    RebarSystemHookTypeTopDirn2: ForgeTypeId
    RebarSystemHookTypeTopDirn1: ForgeTypeId
    RebarSystemHookOrientBottomDirn2: ForgeTypeId
    RebarSystemHookOrientBottomDirn1: ForgeTypeId
    RebarSystemHookOrientTopDirn2: ForgeTypeId
    RebarSystemHookOrientTopDirn1: ForgeTypeId
    RebarSystemBarTypeBottomDirn2: ForgeTypeId
    RebarSystemBarTypeBottomDirn1: ForgeTypeId
    RebarSystemBarTypeTopDirn2: ForgeTypeId
    RebarSystemBarTypeTopDirn1: ForgeTypeId
    RebarSystemActiveBottomDirn2: ForgeTypeId
    RebarSystemActiveBottomDirn1: ForgeTypeId
    RebarSystemActiveTopDirn2: ForgeTypeId
    RebarSystemActiveTopDirn1: ForgeTypeId
    RebarSystemSpanhookTopDirn2: ForgeTypeId
    RebarSystemSpanhookBottomDirn2: ForgeTypeId
    RebarSystemSpanhookRightDirn1: ForgeTypeId
    RebarSystemSpanhookLeftDirn1: ForgeTypeId
    RebarSystemSpanactiveDirn2: ForgeTypeId
    RebarSystemSpanactiveDirn1: ForgeTypeId
    RebarSystemAddlInteriorOffset: ForgeTypeId
    RebarSystemAddlExteriorOffset: ForgeTypeId
    RebarSystemAddlBottomOffset: ForgeTypeId
    RebarSystemAddlTopOffset: ForgeTypeId
    RebarSystemTopMinorMatchesBottomMinor: ForgeTypeId
    RebarSystemTopMajorMatchesBottomMajor: ForgeTypeId
    RebarSystemBottomMajorMatchesBottomMinor: ForgeTypeId
    RebarSystemTopMajorMatchesTopMinor: ForgeTypeId
    RebarSystemLayerSummaryDir2NoSpacing: ForgeTypeId
    RebarSystemLayerSummaryDir2WithSpacing: ForgeTypeId
    RebarSystemLayerSummaryDir1NoSpacing: ForgeTypeId
    RebarSystemLayerSummaryDir1WithSpacing: ForgeTypeId
    RebarSystemLayerSummaryBottomDir2NoSpacing: ForgeTypeId
    RebarSystemLayerSummaryBottomDir2WithSpacing: ForgeTypeId
    RebarSystemLayerSummaryBottomDir1NoSpacing: ForgeTypeId
    RebarSystemLayerSummaryBottomDir1WithSpacing: ForgeTypeId
    RebarSystemLayerSummaryTopDir2NoSpacing: ForgeTypeId
    RebarSystemLayerSummaryTopDir2WithSpacing: ForgeTypeId
    RebarSystemLayerSummaryTopDir1NoSpacing: ForgeTypeId
    RebarSystemLayerSummaryTopDir1WithSpacing: ForgeTypeId
    RebarSystemCoverBottom: ForgeTypeId
    RebarSystemCoverTop: ForgeTypeId
    RebarSystemOverride: ForgeTypeId
    RebarSystemLayerSummaryNoSpacing: ForgeTypeId
    RebarSystemLayerSummaryWithSpacing: ForgeTypeId
    RebarSystemLayoutRule: ForgeTypeId
    RebarSystemCoverSide: ForgeTypeId
    EnergyAnalysisCurrentViewOnly: ForgeTypeId
    FabricParamWiresAtCover: ForgeTypeId
    FabricWireOffset: ForgeTypeId
    FabricWireDistance: ForgeTypeId
    FabricWireLength: ForgeTypeId
    FabricWireType: ForgeTypeId
    BentFabricParamLongitudinalCutLength: ForgeTypeId
    FabricParamSharedFamilyKey: ForgeTypeId
    FabricParamCutByHost: ForgeTypeId
    BentFabricParamStraightWiresLocation: ForgeTypeId
    BentFabricParamBendDirection: ForgeTypeId
    FabricParamSpanTagComponentReference: ForgeTypeId
    FabricParamSpanSymDRight: ForgeTypeId
    FabricParamSpanSymDLeft: ForgeTypeId
    FabricParamSpanSymDBottom: ForgeTypeId
    FabricParamSpanSymDTop: ForgeTypeId
    FabricParamSpanSymRight: ForgeTypeId
    FabricParamSpanSymLeft: ForgeTypeId
    FabricParamSpanSymBottom: ForgeTypeId
    FabricParamSpanSymTop: ForgeTypeId
    FabricParamTagView: ForgeTypeId
    FabricParamCutSheetMass: ForgeTypeId
    FabricParamTotalSheetMass: ForgeTypeId
    FabricParamCutOverallWidth: ForgeTypeId
    FabricParamCutOverallLength: ForgeTypeId
    FabricParamCoverOffset: ForgeTypeId
    FabricParamMinorLapspliceLength: ForgeTypeId
    FabricParamMajorLapspliceLength: ForgeTypeId
    FabricParamLocationGeneric: ForgeTypeId
    FabricParamLapsplicePosition: ForgeTypeId
    FabricParamLocationWall: ForgeTypeId
    FabricParamLocationSlab: ForgeTypeId
    FabricParamSheetType: ForgeTypeId
    FabricBendDiameter: ForgeTypeId
    FabricSheetMassunit: ForgeTypeId
    FabricSheetMinorReinforcementArea: ForgeTypeId
    FabricSheetMajorReinforcementArea: ForgeTypeId
    FabricSheetMass: ForgeTypeId
    FabricSheetMinorSpacing: ForgeTypeId
    FabricSheetMinorNumberOfWires: ForgeTypeId
    FabricSheetMinorLayoutPattern: ForgeTypeId
    FabricSheetMinorEndOverhang: ForgeTypeId
    FabricSheetMinorStartOverhang: ForgeTypeId
    FabricSheetWidth: ForgeTypeId
    FabricSheetOverallWidth: ForgeTypeId
    FabricSheetMajorSpacing: ForgeTypeId
    FabricSheetMajorNumberOfWires: ForgeTypeId
    FabricSheetMajorLayoutPattern: ForgeTypeId
    FabricSheetMajorEndOverhang: ForgeTypeId
    FabricSheetMajorStartOverhang: ForgeTypeId
    FabricSheetLength: ForgeTypeId
    FabricSheetOverallLength: ForgeTypeId
    FabricSheetDefaultMinorLapspliceLength: ForgeTypeId
    FabricSheetDefaultMajorLapspliceLength: ForgeTypeId
    FabricSheetMinorDirectionWireType: ForgeTypeId
    FabricSheetMajorDirectionWireType: ForgeTypeId
    FabricSheetPhysicalMaterialAsset: ForgeTypeId
    FabricWireDiameter: ForgeTypeId
    RebarInstanceBarMassPerUnitLength: ForgeTypeId
    RebarQuanityByDistrib: ForgeTypeId
    RebarMinLength: ForgeTypeId
    RebarMaxLength: ForgeTypeId
    RebarMaximSuffix: ForgeTypeId
    RebarMinimSuffix: ForgeTypeId
    RebarNumberSuffix: ForgeTypeId
    RebarDistributionType: ForgeTypeId
    DpartCanHostRebar: ForgeTypeId
    RebarHostCategory: ForgeTypeId
    RebarShapeParamEndHookTanLen: ForgeTypeId
    RebarShapeParamStartHookTanLen: ForgeTypeId
    RebarInternalMultiplanarEndConnector: ForgeTypeId
    RebarInternalMultiplanarStartConnector: ForgeTypeId
    RebarInternalMultiplanarDuplicate: ForgeTypeId
    RebarInternalMultiplanar: ForgeTypeId
    RebarShapeOutOfPlaneBendDiameter: ForgeTypeId
    RebarInstanceStirrupTieAttachment: ForgeTypeId
    RebarShapeStirrupTieAttachment: ForgeTypeId
    RebarShapeSpiralBaseFinishingTurns: ForgeTypeId
    RebarShapeSpiralTopFinishingTurns: ForgeTypeId
    RebarShapeSpiralHeight: ForgeTypeId
    RebarShapeSpiralPitch: ForgeTypeId
    RebarStandardHookBendDiameter: ForgeTypeId
    RebarIncludeLastBar: ForgeTypeId
    RebarIncludeFirstBar: ForgeTypeId
    RebarInstanceBendDiameter: ForgeTypeId
    RebarInstanceBarDiameter: ForgeTypeId
    RebarShapeEndHookOffset: ForgeTypeId
    RebarShapeEndHookLength: ForgeTypeId
    RebarShapeStartHookOffset: ForgeTypeId
    RebarShapeStartHookLength: ForgeTypeId
    RebarElemScheduleMark: ForgeTypeId
    FabricParamRounding: ForgeTypeId
    RebarElementRounding: ForgeTypeId
    RebarElemHookStyle: ForgeTypeId
    RebarShapeHookStyle: ForgeTypeId
    RebarShapeAllowedBarTypes: ForgeTypeId
    RebarBarMaximumBendRadius: ForgeTypeId
    RebarBarStirrupBendDiameter: ForgeTypeId
    RebarBarHookLengths: ForgeTypeId
    RebarHookStyle: ForgeTypeId
    RebarElemLength: ForgeTypeId
    RebarShape: ForgeTypeId
    RebarElementVisibility: ForgeTypeId
    RebarElemBarSpacing: ForgeTypeId
    RebarElemQuantityOfBars: ForgeTypeId
    RebarElemLayoutRule: ForgeTypeId
    RebarStandardBendDiameter: ForgeTypeId
    RebarElemTerminationEndOrient: ForgeTypeId
    RebarElemHookEndType: ForgeTypeId
    RebarElemTerminationStartOrient: ForgeTypeId
    RebarElemHookStartType: ForgeTypeId
    RebarElemTotalLength: ForgeTypeId
    RebarHookLineLenFactor: ForgeTypeId
    RebarHookAngle: ForgeTypeId
    RebarBarStyle: ForgeTypeId
    RebarBarDiameter: ForgeTypeId
    WallAlignKeyRefParam: ForgeTypeId
    CwpCopyRoofInserts: ForgeTypeId
    CwpCopyFloorInserts: ForgeTypeId
    CwpCopyWallInserts: ForgeTypeId
    CwpLinkedRoomParams: ForgeTypeId
    CwpLinkedRoomPhases: ForgeTypeId
    CwpReuseGridsSameName: ForgeTypeId
    CwpReuseLevelsSameName: ForgeTypeId
    CwpSplitColumnsAtLevels: ForgeTypeId
    CwpReuseExistingGrids: ForgeTypeId
    CwpReuseExistingLevels: ForgeTypeId
    CwpLevelOffset: ForgeTypeId
    CwpAddLevelSuffix: ForgeTypeId
    CwpAddLevelPrefix: ForgeTypeId
    CwpAddGridSuffix: ForgeTypeId
    CwpAddGridPrefix: ForgeTypeId
    LoadUsageName: ForgeTypeId
    LoadCombinationFactor: ForgeTypeId
    LoadCombinationName: ForgeTypeId
    LoadNatureName: ForgeTypeId
    LoadCaseSubcategory: ForgeTypeId
    LoadCaseNature: ForgeTypeId
    LoadCaseNumber: ForgeTypeId
    LoadCaseName: ForgeTypeId
    LoadAttrAreaForceScaleFactor: ForgeTypeId
    LoadAttrLinearForceScaleFactor: ForgeTypeId
    LoadArrowSeparation: ForgeTypeId
    LoadAttrMomentScaleFactor: ForgeTypeId
    LoadAttrMomentArrowLine: ForgeTypeId
    LoadAttrMomentArrowArc: ForgeTypeId
    LoadAttrForceScaleFactor: ForgeTypeId
    LoadAttrForceArrowType: ForgeTypeId
    LoadDescription: ForgeTypeId
    LoadComments: ForgeTypeId
    LoadCaseNatureText: ForgeTypeId
    LoadAllNon0Loads: ForgeTypeId
    LoadAreaIsProjected: ForgeTypeId
    LoadAreaArea: ForgeTypeId
    LoadAreaForceFz3: ForgeTypeId
    LoadAreaForceFy3: ForgeTypeId
    LoadAreaForceFx3: ForgeTypeId
    LoadAreaForceFz2: ForgeTypeId
    LoadAreaForceFy2: ForgeTypeId
    LoadAreaForceFx2: ForgeTypeId
    LoadAreaForceFz1: ForgeTypeId
    LoadAreaForceFy1: ForgeTypeId
    LoadAreaForceFx1: ForgeTypeId
    MeasureTotalLength: ForgeTypeId
    LoadLinearLength: ForgeTypeId
    LoadIsProjected: ForgeTypeId
    LoadMomentMz2: ForgeTypeId
    LoadMomentMy2: ForgeTypeId
    LoadMomentMx2: ForgeTypeId
    LoadMomentMz1: ForgeTypeId
    LoadMomentMy1: ForgeTypeId
    LoadMomentMx1: ForgeTypeId
    LoadLinearForceFz2: ForgeTypeId
    LoadLinearForceFy2: ForgeTypeId
    LoadLinearForceFx2: ForgeTypeId
    LoadLinearForceFz1: ForgeTypeId
    LoadLinearForceFy1: ForgeTypeId
    LoadLinearForceFx1: ForgeTypeId
    LoadMomentMz: ForgeTypeId
    LoadMomentMy: ForgeTypeId
    LoadMomentMx: ForgeTypeId
    LoadForceFz: ForgeTypeId
    LoadForceFy: ForgeTypeId
    LoadForceFx: ForgeTypeId
    LoadIsHosted: ForgeTypeId
    LoadIsReaction: ForgeTypeId
    LoadIsUniform: ForgeTypeId
    LoadUseLocalCoordinateSystem: ForgeTypeId
    LoadCaseId: ForgeTypeId
    SpanDirSymParamRight: ForgeTypeId
    SpanDirSymParamLeft: ForgeTypeId
    SpanDirSymParamBottom: ForgeTypeId
    SpanDirSymParamTop: ForgeTypeId
    SpanDirInstParamAngle: ForgeTypeId
    AnalyticalNodeConnectionStatus: ForgeTypeId
    AnalyticalMemberRotation: ForgeTypeId
    AnalyticalPanelThickness: ForgeTypeId
    AnalyticalElementStructuralRole: ForgeTypeId
    AnalyticalElementPhysicalAsset: ForgeTypeId
    AnalyticalGeometryIsValid: ForgeTypeId
    StructuralAssetParam: ForgeTypeId
    AnalyticalElementHasAssociation: ForgeTypeId
    GridNetLocationMark: ForgeTypeId
    AnalyticalModelCodeChecking: ForgeTypeId
    AnalyticalModelNodesMark: ForgeTypeId
    AnalyticalModelFoundationsMark: ForgeTypeId
    AnalyticalModelSurfaceElementsMark: ForgeTypeId
    AnalyticalModelStickElementsMark: ForgeTypeId
    FamilyEnableCuttingInViews: ForgeTypeId
    FamilyCanHostRebar: ForgeTypeId
    ClearCover: ForgeTypeId
    ClearCoverBottom: ForgeTypeId
    ClearCoverTop: ForgeTypeId
    ClearCoverOther: ForgeTypeId
    ClearCoverInterior: ForgeTypeId
    ClearCoverExterior: ForgeTypeId
    CoverTypeLength: ForgeTypeId
    CoverTypeName: ForgeTypeId
    JoistSystemClearSpacingParam: ForgeTypeId
    JoistSystemFixedSpacingParam: ForgeTypeId
    JoistSystemMaximumSpacingParam: ForgeTypeId
    CurveEdgeOffset: ForgeTypeId
    BeamSystem3dParam: ForgeTypeId
    JoistSystemNewBeamTypeNoFamNameParam: ForgeTypeId
    BeamSystemTagInstParamAngle: ForgeTypeId
    BeamSystemTagParamRight: ForgeTypeId
    BeamSystemTagParamLeft: ForgeTypeId
    JoistSystemNumBeamsSameType: ForgeTypeId
    BeamHJustification: ForgeTypeId
    BeamVJustification: ForgeTypeId
    CurveSupportOffset: ForgeTypeId
    JoistSystemNewBeamTypeParam: ForgeTypeId
    JoistSystemLayoutRuleParam: ForgeTypeId
    JoistSystemJustificationParam: ForgeTypeId
    JoistSystemSpacingParam: ForgeTypeId
    JoistSystemNumberOfLinesParam: ForgeTypeId
    RbsDuctFlowParam: ForgeTypeId
    CurtaingridBeltRatioV: ForgeTypeId
    CurtaingridBeltRatioU: ForgeTypeId
    CurtaingridUseCurveDistV: ForgeTypeId
    CurtaingridUseCurveDistU: ForgeTypeId
    CurtaingridAdjustBorderV: ForgeTypeId
    CurtaingridAdjustBorderU: ForgeTypeId
    CurtaingridBeltV: ForgeTypeId
    CurtaingridBeltU: ForgeTypeId
    CurtaingridOriginV: ForgeTypeId
    CurtaingridOriginU: ForgeTypeId
    CurtaingridAngleV: ForgeTypeId
    CurtaingridAngleU: ForgeTypeId
    SpacingNumDivisionsV: ForgeTypeId
    SpacingNumDivisionsU: ForgeTypeId
    SpacingJustificationV: ForgeTypeId
    SpacingJustificationU: ForgeTypeId
    SpacingLengthV: ForgeTypeId
    SpacingLengthU: ForgeTypeId
    SpacingLayoutV: ForgeTypeId
    SpacingLayoutU: ForgeTypeId
    CurtaingridBeltRation2: ForgeTypeId
    CurtaingridBeltRation1: ForgeTypeId
    CurtainVersionParam: ForgeTypeId
    PaddingLength: ForgeTypeId
    CurtaingridUseCurveDist: ForgeTypeId
    SpacingJustification: ForgeTypeId
    SpacingNumDivisions: ForgeTypeId
    SpacingLength: ForgeTypeId
    SpacingLayout: ForgeTypeId
    CurtaingridUseCurveDistn2: ForgeTypeId
    CurtaingridUseCurveDistn1: ForgeTypeId
    CurtaingridAdjustBordern2: ForgeTypeId
    CurtaingridAdjustBordern1: ForgeTypeId
    CurtaingridBeltn2: ForgeTypeId
    CurtaingridBeltn1: ForgeTypeId
    CurtaingridOriginn2: ForgeTypeId
    CurtaingridOriginn1: ForgeTypeId
    CurtaingridAnglen2: ForgeTypeId
    CurtaingridAnglen1: ForgeTypeId
    SpacingNumDivisionsn2: ForgeTypeId
    SpacingNumDivisionsn1: ForgeTypeId
    SpacingJustificationn2: ForgeTypeId
    SpacingJustificationn1: ForgeTypeId
    SpacingLengthn2: ForgeTypeId
    SpacingLengthn1: ForgeTypeId
    SpacingLayoutn2: ForgeTypeId
    SpacingLayoutn1: ForgeTypeId
    CurtaingridUseCurveDistHoriz: ForgeTypeId
    CurtaingridUseCurveDistVert: ForgeTypeId
    CurtaingridAdjustBorderHoriz: ForgeTypeId
    CurtaingridAdjustBorderVert: ForgeTypeId
    CurtaingridBeltHoriz: ForgeTypeId
    CurtaingridBeltVert: ForgeTypeId
    CurtaingridOriginHoriz: ForgeTypeId
    CurtaingridOriginVert: ForgeTypeId
    CurtaingridAngleHoriz: ForgeTypeId
    CurtaingridAngleVert: ForgeTypeId
    GridlineSpecStatus: ForgeTypeId
    SpacingNumDivisionsHoriz: ForgeTypeId
    SpacingNumDivisionsVert: ForgeTypeId
    SpacingJustificationHoriz: ForgeTypeId
    SpacingJustificationVert: ForgeTypeId
    SpacingLengthHoriz: ForgeTypeId
    SpacingLengthVert: ForgeTypeId
    SpacingLayoutHoriz: ForgeTypeId
    SpacingLayoutVert: ForgeTypeId
    ViewPositionName: ForgeTypeId
    ViewPositionY: ForgeTypeId
    ViewPositionX: ForgeTypeId
    ViewAnchor: ForgeTypeId
    ViewPosition: ForgeTypeId
    DesignOptionId: ForgeTypeId
    DesignOptionParam: ForgeTypeId
    PlanRegionViewRange: ForgeTypeId
    GuideGridNameParam: ForgeTypeId
    GuideGridSpacingParam: ForgeTypeId
    SketchGridSpacingParam: ForgeTypeId
    JoinStrengthOrder: ForgeTypeId
    FamilyHostingBehavior: ForgeTypeId
    FamilyIsElevationMarkBody: ForgeTypeId
    FamilyUsePrecutShape: ForgeTypeId
    WallSweepDefaultSetbackParam: ForgeTypeId
    WallSweepCutsWallParam: ForgeTypeId
    WallSweepCutByInsertsParam: ForgeTypeId
    SlabEdgeProfileParam: ForgeTypeId
    GutterProfileParam: ForgeTypeId
    RevealProfileParam: ForgeTypeId
    FamilyShared: ForgeTypeId
    FamilyWorkPlaneBased: ForgeTypeId
    FamilyAutojoin: ForgeTypeId
    FamilyIsParametric: ForgeTypeId
    FamilyKeepTextReadable: ForgeTypeId
    WallBottomExtensionDistParam: ForgeTypeId
    WallTopExtensionDistParam: ForgeTypeId
    SweepBaseVertOffset: ForgeTypeId
    SweepBaseOffset: ForgeTypeId
    SlabEdgeMaterialParam: ForgeTypeId
    GutterMaterialParam: ForgeTypeId
    FasciaMaterialParam: ForgeTypeId
    SweepBaseFloorSubcategoryId: ForgeTypeId
    SweepBaseRoofSubcategoryId: ForgeTypeId
    FasciaProfileParam: ForgeTypeId
    DecalSubcategoryId: ForgeTypeId
    DecalHeight: ForgeTypeId
    DecalWidth: ForgeTypeId
    DecalLockProportions: ForgeTypeId
    DecalAttributes: ForgeTypeId
    FamilyAllowCutWithVoids: ForgeTypeId
    FamilyKeyExtParam: ForgeTypeId
    WallSweepWallSubcategoryId: ForgeTypeId
    FamilyAlwaysVertical: ForgeTypeId
    FamilyRotateWithComponent: ForgeTypeId
    HostVolumeComputed: ForgeTypeId
    HostAreaComputed: ForgeTypeId
    WallSweepWallOffsetParam: ForgeTypeId
    WallSweepOffsetParam: ForgeTypeId
    WallSweepLevelParam: ForgeTypeId
    WallSweepProfileParam: ForgeTypeId
    FamilyRotateTextWithComponent: ForgeTypeId
    AreaSchemeName: ForgeTypeId
    AreaSchemeId: ForgeTypeId
    AreaTypeText: ForgeTypeId
    AreaType: ForgeTypeId
    ContourLabelsRelativeBase: ForgeTypeId
    ContourLabelsElevBaseType: ForgeTypeId
    PropertySegmentSubcategoryId: ForgeTypeId
    PropertySegmentLR: ForgeTypeId
    PropertySegmentRadius: ForgeTypeId
    PropertySegmentEW: ForgeTypeId
    PropertySegmentBearing: ForgeTypeId
    PropertySegmentNS: ForgeTypeId
    PropertySegmentDistance: ForgeTypeId
    PropertyLengthUnits: ForgeTypeId
    PropertyAreaUnits: ForgeTypeId
    VolumeNet: ForgeTypeId
    ProjectedSurfaceArea: ForgeTypeId
    ContourLabelsLinearUnits: ForgeTypeId
    ContourLabelsPrimaryOnly: ForgeTypeId
    PropertySubcategoryId: ForgeTypeId
    PropertyAreaOpen: ForgeTypeId
    VolumeFill: ForgeTypeId
    VolumeCut: ForgeTypeId
    SurfacePerimeter: ForgeTypeId
    SurfaceArea: ForgeTypeId
    PropertyArea: ForgeTypeId
    BuildingpadHeightabovelevelParam: ForgeTypeId
    BuildingpadThickness: ForgeTypeId
    TopographyLinkPath: ForgeTypeId
    TopographyLinkName: ForgeTypeId
    BoundaryRadius: ForgeTypeId
    ToposurfaceContourSubcategoryId: ForgeTypeId
    BoundaryBearing: ForgeTypeId
    BoundaryDistance: ForgeTypeId
    ContourElevationStep: ForgeTypeId
    ContourElevation: ForgeTypeId
    PointElevation: ForgeTypeId
    VolumeOfInterestName: ForgeTypeId
    VolumeOfInterestViewsVisible: ForgeTypeId
    ViewerVolumeOfInterestCrop: ForgeTypeId
    DatumVolumeOfInterest: ForgeTypeId
    OrientByView: ForgeTypeId
    VolumeOfInterestHeight: ForgeTypeId
    RoomPhase: ForgeTypeId
    RoomPhaseId: ForgeTypeId
    PhaseSequenceNumber: ForgeTypeId
    PhaseName: ForgeTypeId
    ViewFamily: ForgeTypeId
    ViewType: ForgeTypeId
    ViewPhaseFilter: ForgeTypeId
    ViewPhase: ForgeTypeId
    PhaseDemolished: ForgeTypeId
    PhaseCreated: ForgeTypeId
    MassDataSlab: ForgeTypeId
    EnergyAnalysisHvacSystem: ForgeTypeId
    EnergyAnalysisOutdoorAirInformationParam: ForgeTypeId
    EnergyAnalysisMasszoneUseenergydatasettings: ForgeTypeId
    EnergyAnalysisMasszoneDivideperimeter: ForgeTypeId
    EnergyAnalysisMasszoneCoreoffset: ForgeTypeId
    EnergyAnalysisShadeDepth: ForgeTypeId
    EnergyAnalysisConceptualConstruction: ForgeTypeId
    EnergyAnalysisSkylightWidth: ForgeTypeId
    EnergyAnalysisPercentageSkylights: ForgeTypeId
    EnergyAnalysisGlazingIsShaded: ForgeTypeId
    EnergyAnalysisSillHeight: ForgeTypeId
    EnergyAnalysisPercentageGlazing: ForgeTypeId
    EnergyAnalysisMassZoning: ForgeTypeId
    EnergyAnalysisBuildingOperatingSchedule: ForgeTypeId
    EnergyAnalysisCreateAnalyticalModel: ForgeTypeId
    MassDataSurfaceDataSource: ForgeTypeId
    MassDataSkylightWidth: ForgeTypeId
    MassDataPercentageSkylights: ForgeTypeId
    MassDataSillHeight: ForgeTypeId
    MassDataShadeDepth: ForgeTypeId
    MassDataGlazingIsShaded: ForgeTypeId
    MassDataPercentageGlazing: ForgeTypeId
    MassDataUnderground: ForgeTypeId
    MassDataMassOpeningArea: ForgeTypeId
    MassDataMassSkylightArea: ForgeTypeId
    MassDataMassWindowArea: ForgeTypeId
    MassDataMassRoofArea: ForgeTypeId
    MassDataMassInteriorWallArea: ForgeTypeId
    MassDataMassExteriorWallArea: ForgeTypeId
    MassDataSubcategory: ForgeTypeId
    MassDataConceptualConstruction: ForgeTypeId
    MassZoneConditionTypeParam: ForgeTypeId
    MassZoneSpaceTypeParam: ForgeTypeId
    MassZoneFloorArea: ForgeTypeId
    ConceptualConstructionMaterial: ForgeTypeId
    MassSurfacedataMaterial: ForgeTypeId
    MassZoneMaterial: ForgeTypeId
    MassZoneVolume: ForgeTypeId
    LevelDataMassTypeDescription: ForgeTypeId
    LevelDataMassInstanceComments: ForgeTypeId
    LevelDataMassTypeComments: ForgeTypeId
    LevelDataMassFamilyAndTypeParam: ForgeTypeId
    LevelDataMassFamilyParam: ForgeTypeId
    LevelDataSpaceUsage: ForgeTypeId
    LevelDataOwningLevel: ForgeTypeId
    LevelDataMassTypeParam: ForgeTypeId
    LevelDataVolume: ForgeTypeId
    LevelDataSurfaceArea: ForgeTypeId
    LevelDataFloorArea: ForgeTypeId
    LevelDataFloorPerimeter: ForgeTypeId
    MassGrossVolume: ForgeTypeId
    MassGrossSurfaceArea: ForgeTypeId
    MassFloorAreaLevels: ForgeTypeId
    MassGrossArea: ForgeTypeId
    MassingIntegrationLevel: ForgeTypeId
    ProjectRevisionRevisionIssued: ForgeTypeId
    ProjectRevisionEnumeration: ForgeTypeId
    ProjectRevisionRevisionIssuedBy: ForgeTypeId
    ProjectRevisionRevisionIssuedTo: ForgeTypeId
    ProjectRevisionRevisionDate: ForgeTypeId
    ProjectRevisionRevisionDescription: ForgeTypeId
    ProjectRevisionRevisionNum: ForgeTypeId
    ProjectRevisionSequenceNum: ForgeTypeId
    RevisionCloudRevisionIssuedBy: ForgeTypeId
    RevisionCloudRevisionIssuedTo: ForgeTypeId
    RevisionCloudRevisionDate: ForgeTypeId
    RevisionCloudRevisionDescription: ForgeTypeId
    RevisionCloudRevisionNum: ForgeTypeId
    RevisionCloudRevision: ForgeTypeId
    RepeatingDetailRotation: ForgeTypeId
    RepeatingDetailInside: ForgeTypeId
    RepeatingDetailElement: ForgeTypeId
    RepeatingDetailLayout: ForgeTypeId
    RepeatingDetailSpacing: ForgeTypeId
    RepeatingDetailNumber: ForgeTypeId
    InsulationScale: ForgeTypeId
    InsulationWidth: ForgeTypeId
    ViewPartsVisibility: ForgeTypeId
    ViewDetailLevel: ForgeTypeId
    PlumbingFixturesVentConnection: ForgeTypeId
    PlumbingFixturesWasteConnection: ForgeTypeId
    PlumbingFixturesCwConnection: ForgeTypeId
    PlumbingFixturesHwConnection: ForgeTypeId
    PlumbingFixturesTrap: ForgeTypeId
    PlumbingFixturesDrain: ForgeTypeId
    PlumbingFixturesSupplyPipe: ForgeTypeId
    PlumbingFixturesSupplyFitting: ForgeTypeId
    LightingFixtureLightEmitter: ForgeTypeId
    FbxLightSpotFieldAngle: ForgeTypeId
    FbxLightSpotBeamAngle: ForgeTypeId
    FbxLightSpotTiltAngle: ForgeTypeId
    FbxLightLimunousFlux: ForgeTypeId
    LightingFixtureLamp: ForgeTypeId
    LightingFixtureWattage: ForgeTypeId
    ElecticalEquipVoltage: ForgeTypeId
    ElecticalEquipWattage: ForgeTypeId
    CurtainWallSyspanelThickness: ForgeTypeId
    CurtainWallPanelHostId: ForgeTypeId
    CurtainWallSyspanelOffset: ForgeTypeId
    CurtainWallPanelsWidth: ForgeTypeId
    CurtainWallPanelsHeight: ForgeTypeId
    AllModelModel: ForgeTypeId
    AllModelManufacturer: ForgeTypeId
    AllModelInstanceComments: ForgeTypeId
    AllModelTypeComments: ForgeTypeId
    AllModelUrl: ForgeTypeId
    AllModelDescription: ForgeTypeId
    RgbBParam: ForgeTypeId
    RgbGParam: ForgeTypeId
    RgbRParam: ForgeTypeId
    EllipseYParam: ForgeTypeId
    EllipseXParam: ForgeTypeId
    GroupnameParam: ForgeTypeId
    IconIndexParam: ForgeTypeId
    ShowIconParam: ForgeTypeId
    GenericDepth: ForgeTypeId
    AnalyticalMemberSectionType: ForgeTypeId
    AnalyticalModelEndProjectionOrthogonal: ForgeTypeId
    AnalyticalModelStartProjectionOrthogonal: ForgeTypeId
    AnalyticalLinkReleaseRotationZ: ForgeTypeId
    AnalyticalLinkReleaseRotationY: ForgeTypeId
    AnalyticalLinkReleaseRotationX: ForgeTypeId
    AnalyticalLinkReleaseTranslationZ: ForgeTypeId
    AnalyticalLinkReleaseTranslationY: ForgeTypeId
    AnalyticalLinkReleaseTranslationX: ForgeTypeId
    AnalyticalModelPhysicalType: ForgeTypeId
    AnalyticalModelSketchProjection: ForgeTypeId
    AnalyticalModelSketchAlignmentMethod: ForgeTypeId
    AnalyticalModelWallBaseProjection: ForgeTypeId
    AnalyticalModelWallTopProjection: ForgeTypeId
    AnalyticalModelWallProjection: ForgeTypeId
    AnalyticalModelWallAlignmentMethod: ForgeTypeId
    AnalyticalModelFloorProjection: ForgeTypeId
    AnalyticalModelFloorAlignmentMethod: ForgeTypeId
    AnalyticalModelColumnBaseExtension: ForgeTypeId
    AnalyticalModelBaseExtensionMethod: ForgeTypeId
    AnalyticalModelColumnTopExtension: ForgeTypeId
    AnalyticalModelTopExtensionMethod: ForgeTypeId
    AnalyticalModelTopYProjection: ForgeTypeId
    AnalyticalModelTopZProjection: ForgeTypeId
    AnalyticalModelTopAlignmentMethod: ForgeTypeId
    AnalyticalModelBaseYProjection: ForgeTypeId
    AnalyticalModelBaseZProjection: ForgeTypeId
    AnalyticalModelBaseAlignmentMethod: ForgeTypeId
    AnalyticalModelEndZProjection: ForgeTypeId
    AnalyticalModelEndYProjection: ForgeTypeId
    AnalyticalModelEndAlignmentMethod: ForgeTypeId
    AnalyticalModelStartZProjection: ForgeTypeId
    AnalyticalModelStartYProjection: ForgeTypeId
    AnalyticalModelStartAlignmentMethod: ForgeTypeId
    ElementLockedParam: ForgeTypeId
    StairsRailingBalusterIsPost: ForgeTypeId
    StairsRailingConnection: ForgeTypeId
    StairsRailingAngledConnection: ForgeTypeId
    StairsRailingTangentConnection: ForgeTypeId
    StairsRailingHeightShiftVal: ForgeTypeId
    StairsRailingHeightShiftType: ForgeTypeId
    StairsRailingRailName: ForgeTypeId
    StairsRailingBalusterPlacement: ForgeTypeId
    StairsRailingBalusterSlopeAngle: ForgeTypeId
    StairsRailingBalusterBottomAngle: ForgeTypeId
    StairsRailingBalusterTopAngle: ForgeTypeId
    StairsRailingBalusterHeight: ForgeTypeId
    StairsRailingHeightOffset: ForgeTypeId
    StairsRailingBaseLevelParam: ForgeTypeId
    StairsRailingBalusterOffset: ForgeTypeId
    StairsRailingBalusterFamily: ForgeTypeId
    StairsRailingRailOffset: ForgeTypeId
    StairsRailingRailHeight: ForgeTypeId
    StairsRailingRailStructure: ForgeTypeId
    StairsRailingShape: ForgeTypeId
    StairsRailingBalusterLength: ForgeTypeId
    StairsRailingBalusterWidth: ForgeTypeId
    StairsRailingBalustersPerTread: ForgeTypeId
    StairsRailingBalusterSpacing: ForgeTypeId
    StairsRailingBalusterSpacingType: ForgeTypeId
    StairsRailingBalusterShape: ForgeTypeId
    StairsRailingThickness: ForgeTypeId
    StairsRailingWidth: ForgeTypeId
    StairsRailingHeight: ForgeTypeId
    RampAttrTextSize: ForgeTypeId
    RampAttrTextFont: ForgeTypeId
    RampAttrMaterial: ForgeTypeId
    RampAttrRightBalusterAttachPt: ForgeTypeId
    RampAttrLeftBalusterAttachPt: ForgeTypeId
    RampAttrShape: ForgeTypeId
    RampAttrThickness: ForgeTypeId
    RampMaxRunLength: ForgeTypeId
    RampAttrMinInvSlope: ForgeTypeId
    AssignTemplateOnViewCreation: ForgeTypeId
    DefaultViewTemplate: ForgeTypeId
    PlanViewViewDir: ForgeTypeId
    PocheMatId: ForgeTypeId
    ElevatnTag: ForgeTypeId
    CalloutTag: ForgeTypeId
    SectionTag: ForgeTypeId
    CalloutSyncronizeBoundOffsetFar: ForgeTypeId
    CalloutCornerSheetRadius: ForgeTypeId
    CalloutAttrHeadTag: ForgeTypeId
    GridBubbleEndn2: ForgeTypeId
    GridBubbleEndn1: ForgeTypeId
    DatumBubbleLocationInElev: ForgeTypeId
    DatumBubbleEndn1: ForgeTypeId
    DatumBubbleEndn2: ForgeTypeId
    DatumText: ForgeTypeId
    CurveIsMultilevel: ForgeTypeId
    CurveBottomLevel: ForgeTypeId
    CurveTopLevel: ForgeTypeId
    EllipseFocusMrkVisible: ForgeTypeId
    ArcWallCntrMrkVisible: ForgeTypeId
    RefTableParamName: ForgeTypeId
    RefTableElemName: ForgeTypeId
    RbsPanelScheduleSheetAppearanceInstParam: ForgeTypeId
    RbsPanelScheduleSheetAppearanceParam: ForgeTypeId
    ScheduleEmbeddedParam: ForgeTypeId
    ScheduleSheetAppearanceParam: ForgeTypeId
    ScheduleFormatParam: ForgeTypeId
    ScheduleGroupParam: ForgeTypeId
    ScheduleFilterParam: ForgeTypeId
    ScheduleFieldsParam: ForgeTypeId
    RasterSymbolLinkloadStatus: ForgeTypeId
    RasterEnableSnaps: ForgeTypeId
    RasterSymbolPagenumber: ForgeTypeId
    RasterHorizontalScale: ForgeTypeId
    RasterVerticalScale: ForgeTypeId
    RasterSymbolHeight: ForgeTypeId
    RasterSymbolWidth: ForgeTypeId
    RasterSymbolResolution: ForgeTypeId
    RasterSymbolFilename: ForgeTypeId
    RasterSymbolViewname: ForgeTypeId
    RasterSymbolPixelheight: ForgeTypeId
    RasterSymbolPixelwidth: ForgeTypeId
    RasterLockProportions: ForgeTypeId
    RasterSheetheight: ForgeTypeId
    RasterSheetwidth: ForgeTypeId
    ImportAdtEntityRoll: ForgeTypeId
    ImportAdtEntityThickness: ForgeTypeId
    ImportAdtEntityLength: ForgeTypeId
    ImportAdtEntityWidth: ForgeTypeId
    ImportAdtEntityHeight: ForgeTypeId
    ImportAdtComponentsDesc: ForgeTypeId
    ImportAdtEntityStyle: ForgeTypeId
    ImportAdtEntityStructType: ForgeTypeId
    ImportAdtEntityType: ForgeTypeId
    RvtLinkInstanceProjectInformation: ForgeTypeId
    RvtLinkPhaseMap: ForgeTypeId
    RvtLinkReferenceType: ForgeTypeId
    RvtLinkFileNameWithoutExt: ForgeTypeId
    RvtLevelOffset: ForgeTypeId
    RvtHostLevel: ForgeTypeId
    RvtSourceLevel: ForgeTypeId
    RvtLinkInstanceName: ForgeTypeId
    GeoLocation: ForgeTypeId
    ImportInstanceCuttingInView: ForgeTypeId
    ImportInstanceScale: ForgeTypeId
    ImportBackground: ForgeTypeId
    ImportDisplayUnits: ForgeTypeId
    ImportBaseLevelOffset: ForgeTypeId
    ImportBaseLevel: ForgeTypeId
    ImportScale: ForgeTypeId
    ImportSymbolName: ForgeTypeId
    ElevSymbolId: ForgeTypeId
    ElevReferenceLabelPos: ForgeTypeId
    ElevAssocDatum: ForgeTypeId
    ElevViewNamePos: ForgeTypeId
    ElevShowViewName: ForgeTypeId
    ElevTextPos: ForgeTypeId
    ElevArrowFilled: ForgeTypeId
    ElevArrowAngle: ForgeTypeId
    ElevShape: ForgeTypeId
    ElevWidth: ForgeTypeId
    ColorFillSwatchHeightParam: ForgeTypeId
    ColorFillSwatchWidthParam: ForgeTypeId
    ColorFillFilteredParam: ForgeTypeId
    SheetPrimaryTitleBlock: ForgeTypeId
    SheetCollection: ForgeTypeId
    SheetGuideGrid: ForgeTypeId
    SheetCurrentRevisionIssued: ForgeTypeId
    SheetCurrentRevisionIssuedBy: ForgeTypeId
    SheetCurrentRevisionIssuedTo: ForgeTypeId
    SheetCurrentRevisionDate: ForgeTypeId
    SheetCurrentRevisionDescription: ForgeTypeId
    SheetRevisionsOnSheet: ForgeTypeId
    SheetCurrentRevision: ForgeTypeId
    SheetHeight: ForgeTypeId
    SheetWidth: ForgeTypeId
    SheetFilePath: ForgeTypeId
    SheetApprovedBy: ForgeTypeId
    SheetDesignedBy: ForgeTypeId
    SheetScheduled: ForgeTypeId
    SheetCheckedBy: ForgeTypeId
    SheetDrawnBy: ForgeTypeId
    SheetDate: ForgeTypeId
    SheetScale: ForgeTypeId
    SheetNumber: ForgeTypeId
    SheetName: ForgeTypeId
    SpacingAppend: ForgeTypeId
    AutoJoinConditionWall: ForgeTypeId
    AutoMullionBorder2Horiz: ForgeTypeId
    AutoMullionBorder1Horiz: ForgeTypeId
    AutoMullionBorder2Vert: ForgeTypeId
    AutoMullionBorder1Vert: ForgeTypeId
    AutoMullionInteriorHoriz: ForgeTypeId
    AutoMullionInteriorVert: ForgeTypeId
    AutoPanelWall: ForgeTypeId
    AutoJoinCondition: ForgeTypeId
    AutoPanel: ForgeTypeId
    AutoMullionBorder2Grid2: ForgeTypeId
    AutoMullionBorder1Grid2: ForgeTypeId
    AutoMullionBorder2Grid1: ForgeTypeId
    AutoMullionBorder1Grid1: ForgeTypeId
    AutoMullionInteriorGrid2: ForgeTypeId
    AutoMullionInteriorGrid1: ForgeTypeId
    MullionAllGridLines: ForgeTypeId
    MullionGridLineSegment: ForgeTypeId
    MullionGridLine: ForgeTypeId
    CurtainGridBaseOrientation: ForgeTypeId
    MullionAngle: ForgeTypeId
    MullionPosition: ForgeTypeId
    MullionProfile: ForgeTypeId
    TrapMullWidth: ForgeTypeId
    MullionDepth2: ForgeTypeId
    MullionDepth1: ForgeTypeId
    MullionDepth: ForgeTypeId
    LvMullionLeg2: ForgeTypeId
    LvMullionLeg1: ForgeTypeId
    MullionCornerType: ForgeTypeId
    MullionFamType: ForgeTypeId
    MullionOffset: ForgeTypeId
    CircMullionRadius: ForgeTypeId
    CustMullionThick: ForgeTypeId
    CustMullionWidth2: ForgeTypeId
    CustMullionWidth1: ForgeTypeId
    RectMullionThick: ForgeTypeId
    RectMullionWidth2: ForgeTypeId
    RectMullionWidth1: ForgeTypeId
    StairsInstAlwaysUp: ForgeTypeId
    StairsAttrTrimTop: ForgeTypeId
    StairsInstDownArrowOn: ForgeTypeId
    StairsInstDownLabelText: ForgeTypeId
    StairsInstDownLabelOn: ForgeTypeId
    StairsInstUpArrowOn: ForgeTypeId
    StairsInstUpLabelText: ForgeTypeId
    StairsInstUpLabelOn: ForgeTypeId
    StairsAttrTextSize: ForgeTypeId
    StairsAttrTextFont: ForgeTypeId
    StairsAttrBodyMaterial: ForgeTypeId
    StairsAttrLandingCarriage: ForgeTypeId
    StairsAttrLandingsOverlapping: ForgeTypeId
    StairsAttrRightSideStringer: ForgeTypeId
    StairsAttrLeftSideStringer: ForgeTypeId
    StairsAttrNosingPlacement: ForgeTypeId
    StairsAttrRiserTreadConnect: ForgeTypeId
    StairsAttrRiserThickness: ForgeTypeId
    StairsAttrNumMidStringers: ForgeTypeId
    StairsAttrStairsCutOffset: ForgeTypeId
    StairsAttrLastRiser: ForgeTypeId
    StairsAttrFirstRiser: ForgeTypeId
    StairsAttrStairsBottom: ForgeTypeId
    StairsAttrMonolithicStairs: ForgeTypeId
    StairsAttrCalcEnabled: ForgeTypeId
    StairsAttrCalcMax: ForgeTypeId
    StairsAttrCalcMin: ForgeTypeId
    StairsAttrEqResult: ForgeTypeId
    StairsActualTreadDepth: ForgeTypeId
    StairsAttrTreadMult: ForgeTypeId
    StairsAttrRiserMult: ForgeTypeId
    StairsAttrStairCalculator: ForgeTypeId
    StairsActualNumRisers: ForgeTypeId
    StairsAttrBreakSymInCutline: ForgeTypeId
    StairsAttrRiserMaterial: ForgeTypeId
    StairsAttrRiserType: ForgeTypeId
    StairsAttrTreadMaterial: ForgeTypeId
    StairsAttrNosingLength: ForgeTypeId
    StairsAttrTreadFrontProfile: ForgeTypeId
    StairsAttrStringerMaterial: ForgeTypeId
    StairsAttrStringerOffset: ForgeTypeId
    StairsAttrStringerCarriage: ForgeTypeId
    StairsAttrSideStringerTypeParam: ForgeTypeId
    StairsMultistoryTopLevelParam: ForgeTypeId
    StairsStringersPresent: ForgeTypeId
    StairsTopOffset: ForgeTypeId
    StairsBaseOffset: ForgeTypeId
    StairsAttrRiserAngle: ForgeTypeId
    StairsAttrTreadThickness: ForgeTypeId
    StairsAttrStringerThickness: ForgeTypeId
    StairsAttrStringerHeight: ForgeTypeId
    StairsAttrRisersPresent: ForgeTypeId
    StairsActualRiserHeight: ForgeTypeId
    StairsDesiredNumRisers: ForgeTypeId
    StairsAttrTreadWidth: ForgeTypeId
    StairsAttrMinimumTreadDepth: ForgeTypeId
    StairsAttrMaxRiserHeight: ForgeTypeId
    StairsTopLevelParam: ForgeTypeId
    StairsBaseLevelParam: ForgeTypeId
    LevelIsStructural: ForgeTypeId
    LevelIsBuildingStory: ForgeTypeId
    LevelUpToLevel: ForgeTypeId
    LevelRelativeBaseType: ForgeTypeId
    LevelElev: ForgeTypeId
    LevelName: ForgeTypeId
    LevelHeadTag: ForgeTypeId
    SheetCollectionName: ForgeTypeId
    MultiReferenceAnnotationShowDimensionText: ForgeTypeId
    MultiReferenceAnnotationDimensionStyle: ForgeTypeId
    MultiReferenceAnnotationGroupTagHeads: ForgeTypeId
    MultiReferenceAnnotationTagType: ForgeTypeId
    MultiReferenceAnnotationReferenceCategory: ForgeTypeId
    TagLeaderStartType: ForgeTypeId
    TagLeaderEndType: ForgeTypeId
    TagElevationBase: ForgeTypeId
    TagElementCount: ForgeTypeId
    TagAngleParam: ForgeTypeId
    TagLeaderType: ForgeTypeId
    TagNoBreakParamStrings: ForgeTypeId
    RoomTagOrientationParam: ForgeTypeId
    TagOrientationParam: ForgeTypeId
    TagSampleText: ForgeTypeId
    TagTag: ForgeTypeId
    DiameterSymbolText: ForgeTypeId
    DiameterSymbolLocation: ForgeTypeId
    RadiusSymbolText: ForgeTypeId
    VisGraphicsCoordinationModel: ForgeTypeId
    VisGraphicsPointClouds: ForgeTypeId
    VisGraphicsWorksets: ForgeTypeId
    VisGraphicsAnalyticalModel: ForgeTypeId
    VisGraphicsDesignoptions: ForgeTypeId
    VisGraphicsRvtLinks: ForgeTypeId
    VisGraphicsFilters: ForgeTypeId
    VisGraphicsImport: ForgeTypeId
    VisGraphicsAnnotation: ForgeTypeId
    VisGraphicsModel: ForgeTypeId
    LevelAttrRoomComputationAutomatic: ForgeTypeId
    LevelAttrRoomComputationHeight: ForgeTypeId
    LevelRoomComputationHeight: ForgeTypeId
    RoomComputationHeight: ForgeTypeId
    AlwaysZeroLength: ForgeTypeId
    RoomComputationMethod: ForgeTypeId
    RoomLowerOffset: ForgeTypeId
    RoomUpperOffset: ForgeTypeId
    RoomUpperLevel: ForgeTypeId
    RoomVolume: ForgeTypeId
    RoomHeight: ForgeTypeId
    RoomPerimeter: ForgeTypeId
    RoomLevelId: ForgeTypeId
    RoomOccupancy: ForgeTypeId
    RoomDepartment: ForgeTypeId
    RoomFinishBase: ForgeTypeId
    RoomFinishCeiling: ForgeTypeId
    RoomFinishWall: ForgeTypeId
    RoomFinishFloor: ForgeTypeId
    RoomArea: ForgeTypeId
    RoomNumber: ForgeTypeId
    RoomName: ForgeTypeId
    SpatialFieldMgrLegendHorOriginGap: ForgeTypeId
    SpatialFieldMgrLegendVertOriginGap: ForgeTypeId
    SpatialFieldMgrLegendWidth: ForgeTypeId
    SpatialFieldMgrLegendHeight: ForgeTypeId
    ViewAnalysisResultsVisibility: ForgeTypeId
    SpatialFieldMgrLegendTextType: ForgeTypeId
    SpatialFieldMgrResultsVisibility: ForgeTypeId
    SpatialFieldMgrLegendShowDescription: ForgeTypeId
    SpatialFieldMgrLegendShowConfigName: ForgeTypeId
    SpatialFieldMgrDescription: ForgeTypeId
    SpatialFieldMgrCurrentName: ForgeTypeId
    SpatialFieldMgrRange: ForgeTypeId
    GridEndSegmentsLength: ForgeTypeId
    GridEndSegmentPattern: ForgeTypeId
    GridEndSegmentColor: ForgeTypeId
    GridEndSegmentWeight: ForgeTypeId
    GridCenterSegmentPattern: ForgeTypeId
    GridCenterSegmentColor: ForgeTypeId
    GridCenterSegmentWeight: ForgeTypeId
    GridCenterSegmentStyle: ForgeTypeId
    GridBubbleLinePen: ForgeTypeId
    GridHeadTag: ForgeTypeId
    StairsPathFullStepArrow: ForgeTypeId
    StairsPathStartExtension: ForgeTypeId
    TextWidthScaleAboveCutMark: ForgeTypeId
    TextStyleUnderlineAboveCutMark: ForgeTypeId
    TextStyleItalicAboveCutMark: ForgeTypeId
    TextStyleBoldAboveCutMark: ForgeTypeId
    TextSizeAboveCutMark: ForgeTypeId
    TextFontAboveCutMark: ForgeTypeId
    NumberSystemOverrideTextParams: ForgeTypeId
    LineColorAboveCutMark: ForgeTypeId
    TextBackgroundAboveCutMark: ForgeTypeId
    NumberSystemOverrideGraphicsParams: ForgeTypeId
    NumberSystemStartNumber: ForgeTypeId
    NumberSystemTagType: ForgeTypeId
    NumberSystemDisplayRule: ForgeTypeId
    NumberSystemReference: ForgeTypeId
    NumberSystemJustify: ForgeTypeId
    NumberSystemOrientation: ForgeTypeId
    NumberSystemReferenceOffset: ForgeTypeId
    NumberSystemJustifyOffset: ForgeTypeId
    StairsTextOrientation: ForgeTypeId
    StairsTextType: ForgeTypeId
    StairsDownText: ForgeTypeId
    StairsShowDownText: ForgeTypeId
    StairsUpText: ForgeTypeId
    StairsShowUpText: ForgeTypeId
    ShowArrowheadToCutMark: ForgeTypeId
    DrawForEachRun: ForgeTypeId
    ArrowheadEndAtRiser: ForgeTypeId
    StairsPathStartFromRiser: ForgeTypeId
    DistanceToCutMark: ForgeTypeId
    LineShapeAtCorner: ForgeTypeId
    ArrowheadType: ForgeTypeId
    StartSymbolType: ForgeTypeId
    CutMarkSymbolSize: ForgeTypeId
    CutLineType: ForgeTypeId
    CutLineAngle: ForgeTypeId
    CutLineExtension: ForgeTypeId
    CutLineDistance: ForgeTypeId
    CutMarkSymbol: ForgeTypeId
    SectionBrokenDisplayStyle: ForgeTypeId
    SectionCoarserScalePulldownImperial: ForgeTypeId
    SectionCoarserScalePulldownMetric: ForgeTypeId
    SectionParentViewName: ForgeTypeId
    SectionShowInOneViewOnly: ForgeTypeId
    SectionAttrTailTag: ForgeTypeId
    SectionAttrTailWidth: ForgeTypeId
    SectionAttrTailLength: ForgeTypeId
    ViewerDetailNumber: ForgeTypeId
    ViewerSheetNumber: ForgeTypeId
    SectionAttrHeadTag: ForgeTypeId
    AlignmentStationLabelStationValue: ForgeTypeId
    AlignmentStationLabelIndStation: ForgeTypeId
    AlignmentStationLabelIncludeStation: ForgeTypeId
    SpotDimLeaderLine: ForgeTypeId
    AlignmentStationLabelDistance: ForgeTypeId
    AlignmentStationSuffix: ForgeTypeId
    AlignmentStationPrefix: ForgeTypeId
    DimSuffix: ForgeTypeId
    DimPrefix: ForgeTypeId
    ArrowCentered: ForgeTypeId
    InteriorTickDisplay: ForgeTypeId
    WitnsLineTickMark: ForgeTypeId
    DimTotalLength: ForgeTypeId
    DimReferenceCount: ForgeTypeId
    AlternateUnitsSuffix: ForgeTypeId
    AlternateUnitsPrefix: ForgeTypeId
    EqualityWitnessDisplay: ForgeTypeId
    DimStyleSuppressSpaces: ForgeTypeId
    EqualityFormula: ForgeTypeId
    DimStyleLeaderTickMark: ForgeTypeId
    EqualityTextForAngularDim: ForgeTypeId
    EqualityTextForContinuousLinearDim: ForgeTypeId
    DimTextLocationForLeader: ForgeTypeId
    DimLeaderDisplayCondition: ForgeTypeId
    DimLeaderShoulderLength: ForgeTypeId
    DimLeaderType: ForgeTypeId
    DimToIntersectingGrids: ForgeTypeId
    DimToIntersectingWalls: ForgeTypeId
    DimToInsertType: ForgeTypeId
    FixedRotation: ForgeTypeId
    KeepReadable: ForgeTypeId
    LeaderLine: ForgeTypeId
    LeaderOffsetSheet: ForgeTypeId
    DimToInserts: ForgeTypeId
    SpotSlopeOffsetFromReference: ForgeTypeId
    SpotSlopeSlopeRepresentation: ForgeTypeId
    SpotSlopeSlopeDirection: ForgeTypeId
    SpotElevLowerValue: ForgeTypeId
    SpotElevSingleOrUpperValue: ForgeTypeId
    SpotElevIndTypeElevation: ForgeTypeId
    SpotCoordinateIncludeElevation: ForgeTypeId
    SpotCoordinateElevationSuffix: ForgeTypeId
    SpotCoordinateElevationPrefix: ForgeTypeId
    SpotCoordinateBottomSuffix: ForgeTypeId
    SpotCoordinateBottomPrefix: ForgeTypeId
    SpotCoordinateTopSuffix: ForgeTypeId
    SpotCoordinateTopPrefix: ForgeTypeId
    SpotElevLowerSuffix: ForgeTypeId
    SpotElevLowerPrefix: ForgeTypeId
    SpotElevSingleOrUpperSuffix: ForgeTypeId
    SpotElevSingleOrUpperPrefix: ForgeTypeId
    BaselineDimOffset: ForgeTypeId
    SpotElevBendLeader: ForgeTypeId
    SpotElevIndTypeBottom: ForgeTypeId
    SpotElevIndTypeTop: ForgeTypeId
    SpotElevIndBottom: ForgeTypeId
    SpotElevIndTop: ForgeTypeId
    SpotElevTextLocation: ForgeTypeId
    SpotElevRotateWithComponent: ForgeTypeId
    SpotElevDisplayElevations: ForgeTypeId
    OrdinateDimSetting: ForgeTypeId
    LinearDimType: ForgeTypeId
    SpotDimLeader: ForgeTypeId
    DimStyleFlippedDimLineExtension: ForgeTypeId
    DimStyleInteriorTickMark: ForgeTypeId
    SpotTextFromLeader: ForgeTypeId
    SpotCoordinateBase: ForgeTypeId
    DimStyleAngularUnitsAlt: ForgeTypeId
    SpotElevIndType: ForgeTypeId
    SpotElevBotValue: ForgeTypeId
    AlternateUnits: ForgeTypeId
    SpotElevTopValue: ForgeTypeId
    DimStyleLinearUnitsAlt: ForgeTypeId
    SpotElevTextOrientation: ForgeTypeId
    SpotElevIndElevation: ForgeTypeId
    SpotElevIndEw: ForgeTypeId
    SpotElevIndNs: ForgeTypeId
    ArrowClosed: ForgeTypeId
    DimStyleReadConvention: ForgeTypeId
    HeavyEndPen: ForgeTypeId
    DimStyleDimLineSnapDist: ForgeTypeId
    DimStyleCenterlineTickMark: ForgeTypeId
    SpotElevLinePen: ForgeTypeId
    SpotElevTickMarkPen: ForgeTypeId
    SpotElevLeaderArrowhead: ForgeTypeId
    SpotElevRelativeBase: ForgeTypeId
    SpotElevFlipTextVert: ForgeTypeId
    SpotElevTextHorizOffset: ForgeTypeId
    SpotElevBase: ForgeTypeId
    SpotElevSymbol: ForgeTypeId
    DimStyleShowOpeningHt: ForgeTypeId
    DimStyleCenterlinePattern: ForgeTypeId
    DimWitnsLineExtensionBelow: ForgeTypeId
    DimWitnsLineCntrl: ForgeTypeId
    DimLineExtension: ForgeTypeId
    DimStyleCenterlineSymbol: ForgeTypeId
    DimTextBackground: ForgeTypeId
    DimStyleAngularUnits: ForgeTypeId
    DimStyleLinearUnits: ForgeTypeId
    LeaderArrowWidth: ForgeTypeId
    ArrowFilled: ForgeTypeId
    HeavyTickMarkPen: ForgeTypeId
    ArrowSize: ForgeTypeId
    ArrowType: ForgeTypeId
    TickMarkPen: ForgeTypeId
    TextPosition: ForgeTypeId
    RadiusSymbolLocation: ForgeTypeId
    CenterMarkSize: ForgeTypeId
    ArcCenterMark: ForgeTypeId
    WitnsLineGapToElt: ForgeTypeId
    WitnsLineExtension: ForgeTypeId
    TextDistToLine: ForgeTypeId
    TextAlignment: ForgeTypeId
    ModelTextSize: ForgeTypeId
    TextStyleSize: ForgeTypeId
    TextStyleFont: ForgeTypeId
    ShowTitle: ForgeTypeId
    TitleStyleUnderline: ForgeTypeId
    TitleStyleItalic: ForgeTypeId
    TitleStyleBold: ForgeTypeId
    TitleSize: ForgeTypeId
    TitleFont: ForgeTypeId
    TextWidthScale: ForgeTypeId
    TextTabSize: ForgeTypeId
    ArcLeaderParam: ForgeTypeId
    DimLeaderArrowhead: ForgeTypeId
    SheetIssueDate: ForgeTypeId
    ProjectIssueDate: ForgeTypeId
    ProjectStatus: ForgeTypeId
    ClientName: ForgeTypeId
    ProjectAddress: ForgeTypeId
    ProjectName: ForgeTypeId
    ProjectNumber: ForgeTypeId
    LeaderArrowhead: ForgeTypeId
    TextBackground: ForgeTypeId
    TextStyleUnderline: ForgeTypeId
    TextStyleItalic: ForgeTypeId
    TextStyleBold: ForgeTypeId
    CurveIsFilled: ForgeTypeId
    TextAlignVert: ForgeTypeId
    TextAlignHorz: ForgeTypeId
    TextText: ForgeTypeId
    LinePattern: ForgeTypeId
    LineColor: ForgeTypeId
    LinePen: ForgeTypeId
    TextColor: ForgeTypeId
    TextSize: ForgeTypeId
    TextFont: ForgeTypeId
    ReferenceLineSubcategory: ForgeTypeId
    ClineSubcategory: ForgeTypeId
    EdgeLinework: ForgeTypeId
    BuildingCurveGstylePlusInvisible: ForgeTypeId
    BuildingCurveGstyle: ForgeTypeId
    FamilyCurveGstyleFor2010Mass: ForgeTypeId
    HeadOnPlacementMethod: ForgeTypeId
    IsVisibleParam: ForgeTypeId
    FamilyCurveGstylePlusInvisiblePlusStickSymMinusAnalytical: ForgeTypeId
    FamilyCurveGstylePlusInvisibleMinusAnalytical: ForgeTypeId
    FamilyCurveGstylePlusInvisiblePlusStickSym: ForgeTypeId
    FamilyCurveGstylePlusInvisible: ForgeTypeId
    FamilyElemSubcategory: ForgeTypeId
    RoofSlope: ForgeTypeId
    CurveParamSteelCantilever: ForgeTypeId
    CurveParamConcreteCantilever: ForgeTypeId
    CurveNumberOfSegments: ForgeTypeId
    SpecifySlopeOrOffset: ForgeTypeId
    SlopeArrowLevelEnd: ForgeTypeId
    SlopeArrowLevelStart: ForgeTypeId
    CurveLevel: ForgeTypeId
    CurveHeightOffset: ForgeTypeId
    CurveIsSlopeDefining: ForgeTypeId
    DefinesConstantHeight: ForgeTypeId
    RoofCurveHeightAtWall: ForgeTypeId
    RoofCurveHeightOffset: ForgeTypeId
    RoofCurveIsSlopeDefining: ForgeTypeId
    StructuralSectionPolygonDefinition: ForgeTypeId
    StructuralSectionPolygonSides: ForgeTypeId
    StructuralSectionCutHeight: ForgeTypeId
    StructuralSectionCutWidth: ForgeTypeId
    StructuralSectionIshapeWebthicknessLocation: ForgeTypeId
    StructuralSectionIshapeFlangethicknessLocation: ForgeTypeId
    StructuralSectionTopWebFillet: ForgeTypeId
    StructuralSectionSlopedWebAngle: ForgeTypeId
    StructuralSectionSlopedFlangeAngle: ForgeTypeId
    StructuralSectionCantileverHeight: ForgeTypeId
    StructuralSectionCantileverLength: ForgeTypeId
    StructuralSectionBottomCutHeight: ForgeTypeId
    StructuralSectionBottomCutWidth: ForgeTypeId
    StructuralSectionTopCutHeight: ForgeTypeId
    StructuralSectionTopCutWidth: ForgeTypeId
    StructuralFamilyCodeName: ForgeTypeId
    StructuralFamilyNameKey: ForgeTypeId
    StructuralSectionNameKey: ForgeTypeId
    StructuralSectionSigmaProfileTopBendWidth: ForgeTypeId
    StructuralSectionSigmaProfileMiddleBendWidth: ForgeTypeId
    StructuralSectionSigmaProfileBendWidth: ForgeTypeId
    StructuralSectionZprofileBottomFlangeLength: ForgeTypeId
    StructuralSectionCprofileFoldLength: ForgeTypeId
    StructuralSectionLprofileLipLength: ForgeTypeId
    StructuralSectionLangleBoltDiameterShorterFlange: ForgeTypeId
    StructuralSectionLangleBoltDiameterLongerFlange: ForgeTypeId
    StructuralSectionLangleBoltSpacingShorterFlange: ForgeTypeId
    StructuralSectionLangleBoltSpacing2LongerFlange: ForgeTypeId
    StructuralSectionLangleBoltSpacing1LongerFlange: ForgeTypeId
    StructuralSectionIshapeBoltSpacingWeb: ForgeTypeId
    StructuralSectionIshapeBoltSpacingBetweenRows: ForgeTypeId
    StructuralSectionIshapeBoltSpacingTwoRows: ForgeTypeId
    StructuralSectionIshapeBoltDiameter: ForgeTypeId
    StructuralSectionIshapeBoltSpacing: ForgeTypeId
    StructuralSectionIshapeWebToeOfFillet: ForgeTypeId
    StructuralSectionIshapeFlangeToeOfFillet: ForgeTypeId
    StructuralSectionIshapeClearWebHeight: ForgeTypeId
    StructuralSectionIweldedBottomflangewidth: ForgeTypeId
    StructuralSectionIweldedBottomflangethickness: ForgeTypeId
    StructuralSectionIweldedTopflangewidth: ForgeTypeId
    StructuralSectionIweldedTopflangethickness: ForgeTypeId
    StructuralSectionHssOuterfillet: ForgeTypeId
    StructuralSectionHssInnerfillet: ForgeTypeId
    StructuralSectionIshapeWebfillet: ForgeTypeId
    StructuralSectionIshapeFlangefillet: ForgeTypeId
    StructuralSectionIshapeWebheight: ForgeTypeId
    StructuralSectionIshapeWebthickness: ForgeTypeId
    StructuralSectionIshapeFlangethickness: ForgeTypeId
    StructuralSectionCommonShearAreaWeakAxis: ForgeTypeId
    StructuralSectionCommonShearAreaStrongAxis: ForgeTypeId
    StructuralSectionCommonWarpingConstant: ForgeTypeId
    StructuralSectionCommonTorsionalModulus: ForgeTypeId
    StructuralSectionCommonTorsionalMomentOfInertia: ForgeTypeId
    StructuralSectionCommonPlasticModulusWeakAxis: ForgeTypeId
    StructuralSectionCommonPlasticModulusStrongAxis: ForgeTypeId
    StructuralSectionCommonElasticModulusWeakAxis: ForgeTypeId
    StructuralSectionCommonElasticModulusStrongAxis: ForgeTypeId
    StructuralSectionCommonMomentOfInertiaWeakAxis: ForgeTypeId
    StructuralSectionCommonMomentOfInertiaStrongAxis: ForgeTypeId
    StructuralSectionCommonNominalWeight: ForgeTypeId
    StructuralSectionCommonPerimeter: ForgeTypeId
    StructuralSectionCommonAlpha: ForgeTypeId
    StructuralSectionCommonCentroidVertical: ForgeTypeId
    StructuralSectionCommonCentroidHoriz: ForgeTypeId
    StructuralSectionArea: ForgeTypeId
    StructuralSectionPipestandardWalldesignthickness: ForgeTypeId
    StructuralSectionPipestandardWallnominalthickness: ForgeTypeId
    StructuralSectionCommonDiameter: ForgeTypeId
    StructuralSectionCommonHeight: ForgeTypeId
    StructuralSectionCommonWidth: ForgeTypeId
    StructuralSectionShape: ForgeTypeId
    StructuralMaterialParam: ForgeTypeId
    AnalyticalDefineThermalPropertiesBy: ForgeTypeId
    AnalyticConstructionGbxmlTypeid: ForgeTypeId
    AnalyticConstructionLookupTable: ForgeTypeId
    AnalyticalRoughness: ForgeTypeId
    AnalyticalAbsorptance: ForgeTypeId
    AnalyticalThermalMass: ForgeTypeId
    AnalyticalVisualLightTransmittance: ForgeTypeId
    AnalyticalSolarHeatGainCoefficient: ForgeTypeId
    AnalyticalThermalResistance: ForgeTypeId
    AnalyticalHeatTransferCoefficient: ForgeTypeId
    CameraFromLevel: ForgeTypeId
    CameraOffset: ForgeTypeId
    WalkthroughFromLevel: ForgeTypeId
    WalkthroughOffset: ForgeTypeId
    WalkthroughActiveAndTotalFramesText: ForgeTypeId
    ViewSolarstudyLightingAltitudeText: ForgeTypeId
    ViewSolarstudyLightingAltitudeValue: ForgeTypeId
    ViewSolarstudyLightingAzimuthText: ForgeTypeId
    ViewSolarstudyLightingAzimuthValue: ForgeTypeId
    ViewSolarstudyMultidayDatetimeText: ForgeTypeId
    ViewSolarstudyMultidayFrameText: ForgeTypeId
    ViewSolarstudyMultidayFrameValue: ForgeTypeId
    ViewSolarstudySingledayDatetimeText: ForgeTypeId
    ViewSolarstudySingledayFrameText: ForgeTypeId
    ViewSolarstudySingledayFrameValue: ForgeTypeId
    ViewSolarstudyStillTimeText: ForgeTypeId
    ViewSolarstudyStillTimeValue: ForgeTypeId
    ViewSolarstudyStillDateText: ForgeTypeId
    ViewSolarstudyStillDateValue: ForgeTypeId
    ViewSolarstudyLightingPresetIndex: ForgeTypeId
    ViewSolarstudyMultidayPresetIndex: ForgeTypeId
    ViewSolarstudySingledayPresetIndex: ForgeTypeId
    ViewSolarstudyStillPresetIndex: ForgeTypeId
    ViewSolarstudyShadowsIntensityText: ForgeTypeId
    ViewSolarstudyShadowsIntensityValue: ForgeTypeId
    ViewSolarstudySunIntensityText: ForgeTypeId
    ViewSolarstudySunIntensityValue: ForgeTypeId
    ViewSolarstudyAnimationSpeedText: ForgeTypeId
    ViewSolarstudyAnimationSpeedValue: ForgeTypeId
    ViewSolarstudyIsLightingStudyType: ForgeTypeId
    ViewSolarstudyIsMultidayStudyType: ForgeTypeId
    ViewSolarstudyIsSingledayStudyType: ForgeTypeId
    ViewSolarstudyIsStillimageStudyType: ForgeTypeId
    ViewSolarstudyCurrentStudyTypeIndex: ForgeTypeId
    ViewUnderlayTopId: ForgeTypeId
    ViewGraphSunPathSize: ForgeTypeId
    ViewGraphSunPath: ForgeTypeId
    ViewAnalysisDisplayStyle: ForgeTypeId
    ViewGraphSchedLevelRelativeBaseType: ForgeTypeId
    ViewGraphSchedHiddenLevels: ForgeTypeId
    ViewGraphSchedTotalRows: ForgeTypeId
    ViewGraphSchedRowsCount: ForgeTypeId
    ViewGraphSchedGridAppearance: ForgeTypeId
    ViewGraphSchedTextAppearance: ForgeTypeId
    ViewGraphSchedTitle: ForgeTypeId
    ViewGraphSchedRowsFrom: ForgeTypeId
    ViewGraphSchedGroupSimilar: ForgeTypeId
    ViewGraphSchedMaterialTypes: ForgeTypeId
    ViewGraphSchedLocationsHigh: ForgeTypeId
    ViewGraphSchedLocationsLow: ForgeTypeId
    ViewGraphSchedBottomLevel: ForgeTypeId
    ViewGraphSchedTopLevel: ForgeTypeId
    ViewportAttrOrientationOnSheet: ForgeTypeId
    ViewportAttrShowBox: ForgeTypeId
    ViewportAttrShowExtensionLine: ForgeTypeId
    ViewportAttrShowLabel: ForgeTypeId
    ViewportAttrLabelTag: ForgeTypeId
    ViewScaleHavename: ForgeTypeId
    ViewScaleCustomname: ForgeTypeId
    ViewerSheetCollection: ForgeTypeId
    ViewerSheetName: ForgeTypeId
    ViewReferencingSheetCollection: ForgeTypeId
    ViewportSheetCollection: ForgeTypeId
    ViewportAttrPreserveTitlePosition: ForgeTypeId
    ViewportPositioning: ForgeTypeId
    ViewGraphSchedOffGrid: ForgeTypeId
    ViewGraphSchedUnitsFormat: ForgeTypeId
    ViewportSheetName: ForgeTypeId
    ViewportSheetNumber: ForgeTypeId
    ViewportScale: ForgeTypeId
    ViewportViewName: ForgeTypeId
    ViewportView: ForgeTypeId
    ViewportDetailNumber: ForgeTypeId
    ViewTemplateForSchedule: ForgeTypeId
    RenderRpcProperties: ForgeTypeId
    FamilySymbolicRep: ForgeTypeId
    FamilyRenderingType: ForgeTypeId
    RenderRpcFilename: ForgeTypeId
    RenderPlantTrimHeight: ForgeTypeId
    RenderPlantHeight: ForgeTypeId
    RenderPlantName: ForgeTypeId
    ViewCameraOrientation: ForgeTypeId
    ColorSchemeLocation: ForgeTypeId
    ViewDependency: ForgeTypeId
    ViewBackClipping: ForgeTypeId
    ViewAssociatedAssemblyInstanceId: ForgeTypeId
    ViewGraphSchedTotalColumns: ForgeTypeId
    ViewUnderlayOrientation: ForgeTypeId
    ViewTemplate: ForgeTypeId
    ViewGraphSchedNumberColumns: ForgeTypeId
    GraphicDisplayOptions: ForgeTypeId
    ModelGraphicsStyleAnonDraft: ForgeTypeId
    ViewReferencingDetail: ForgeTypeId
    ViewReferencingSheet: ForgeTypeId
    ViewCameraPosition: ForgeTypeId
    PlanViewNorth: ForgeTypeId
    WalkthroughFramesCount: ForgeTypeId
    PlanViewLevel: ForgeTypeId
    ModelGraphicsStyle: ForgeTypeId
    ViewVisibleCategories: ForgeTypeId
    ViewDiscipline: ForgeTypeId
    PlanViewRange: ForgeTypeId
    ViewModelDisplayMode: ForgeTypeId
    ViewShowMassing: ForgeTypeId
    PlanViewTopClipHeight: ForgeTypeId
    ViewCleanJoins: ForgeTypeId
    ViewSheetViewportInfo: ForgeTypeId
    PlanViewCutPlaneHeight: ForgeTypeId
    ViewDepth: ForgeTypeId
    ViewUnderlayBottomId: ForgeTypeId
    ViewScalePulldownImperial: ForgeTypeId
    ViewScalePulldownMetric: ForgeTypeId
    ViewScale: ForgeTypeId
    ViewSchemaSettingForSystem: ForgeTypeId
    ViewSchemaSettingForBuilding: ForgeTypeId
    ViewFixedSketchPlane: ForgeTypeId
    ViewScaleMetric: ForgeTypeId
    ViewScaleImperial: ForgeTypeId
    GraphicDisplayOptionsPhotoExposure: ForgeTypeId
    GraphicDisplayOptionsFog: ForgeTypeId
    GraphicDisplayOptionsBackground: ForgeTypeId
    GraphicDisplayOptionsSsIntensity: ForgeTypeId
    GraphicDisplayOptionsLighting: ForgeTypeId
    GraphicDisplayOptionsShadows: ForgeTypeId
    GraphicDisplayOptionsModel: ForgeTypeId
    Viewer3dRenderSettings: ForgeTypeId
    ViewerBoundFarClipping: ForgeTypeId
    ViewerReferenceLabelText: ForgeTypeId
    ViewerIsReference: ForgeTypeId
    ViewerReferenceLabel: ForgeTypeId
    ViewDescription: ForgeTypeId
    ViewerModelClipBoxActive: ForgeTypeId
    ViewName: ForgeTypeId
    ViewerBoundActiveNear: ForgeTypeId
    ViewerBoundActiveFar: ForgeTypeId
    ViewerBoundActiveBottom: ForgeTypeId
    ViewerBoundActiveTop: ForgeTypeId
    ViewerBoundActiveLeft: ForgeTypeId
    ViewerBoundActiveRight: ForgeTypeId
    ViewerBoundOffsetNear: ForgeTypeId
    ViewerBoundOffsetFar: ForgeTypeId
    ViewerBoundOffsetBottom: ForgeTypeId
    ViewerBoundOffsetTop: ForgeTypeId
    ViewerBoundOffsetLeft: ForgeTypeId
    ViewerBoundOffsetRight: ForgeTypeId
    ViewerAnnotationCropActive: ForgeTypeId
    ViewerShowUncropped: ForgeTypeId
    ViewerCropRegionDisabled: ForgeTypeId
    ViewerCropRegionVisible: ForgeTypeId
    ViewerCropRegion: ForgeTypeId
    ViewerPerspective: ForgeTypeId
    ViewerTargetElevation: ForgeTypeId
    ViewerOptionVisibility: ForgeTypeId
    ViewerEyeElevation: ForgeTypeId
    DimLabelIsType: ForgeTypeId
    DimLabelIsInstance: ForgeTypeId
    DimIsreporting: ForgeTypeId
    DimLeader: ForgeTypeId
    DimDisplayEq: ForgeTypeId
    DimNotModifiable: ForgeTypeId
    DimLabel: ForgeTypeId
    DimLabelGpShow: ForgeTypeId
    DimValueAngle: ForgeTypeId
    DimValueLength: ForgeTypeId
    StairRampStringerCurveHeightCorrection: ForgeTypeId
    StairRampStringerCurveSlope: ForgeTypeId
    ElemReferenceName2dXz: ForgeTypeId
    CurveElemDefinesSlope: ForgeTypeId
    RadialArrayArcRadius: ForgeTypeId
    CurveDeterminesOrientation: ForgeTypeId
    DatumPlaneDefinesWallClosure: ForgeTypeId
    CurveIsDetail: ForgeTypeId
    CurveElemArcRadius: ForgeTypeId
    CurveElemArcRange: ForgeTypeId
    CurveElemArcEndAngle: ForgeTypeId
    CurveElemArcStartAngle: ForgeTypeId
    CurveElemLineAngle: ForgeTypeId
    CurveElemLength: ForgeTypeId
    ElemDeletableInFamily: ForgeTypeId
    ElemReferenceName: ForgeTypeId
    DatumPlaneDefinesOrigin: ForgeTypeId
    ElemIsReference: ForgeTypeId
    EditCurveOffsetParam: ForgeTypeId
    ColAttachJustificationComboParam: ForgeTypeId
    AssociatedLevelOffset: ForgeTypeId
    AssociatedLevel: ForgeTypeId
    ColumnLocationMark: ForgeTypeId
    ColumnTopAttachCutParam: ForgeTypeId
    ColumnBaseAttachCutParam: ForgeTypeId
    ColumnBaseAttachedParam: ForgeTypeId
    ColumnTopAttachedParam: ForgeTypeId
    ColumnBaseAttachmentOffsetParam: ForgeTypeId
    ColumnTopAttachmentOffsetParam: ForgeTypeId
    ColumnBaseAttachJustificationParam: ForgeTypeId
    ColumnTopAttachJustificationParam: ForgeTypeId
    MaterialParamShininess: ForgeTypeId
    MaterialParamSmoothness: ForgeTypeId
    MaterialParamGlow: ForgeTypeId
    MaterialParamTransparency: ForgeTypeId
    MaterialParamColor: ForgeTypeId
    SeekItemId: ForgeTypeId
    ClassificationDescription: ForgeTypeId
    ClassificationCode: ForgeTypeId
    AssemblyDescription: ForgeTypeId
    AssemblyCode: ForgeTypeId
    SlopeEndHeight: ForgeTypeId
    SlopeStartHeight: ForgeTypeId
    ExcludeDesignOptions: ForgeTypeId
    CeilingHasThicknessParam: ForgeTypeId
    CeilingThicknessParam: ForgeTypeId
    CeilingHeightabovelevelParam: ForgeTypeId
    CeilingThickness: ForgeTypeId
    CeilingAttrSystemnameParam: ForgeTypeId
    CeilingAttrSpacing2Param: ForgeTypeId
    CeilingAttrSpacing1Param: ForgeTypeId
    CeilingAttrPatternParam: ForgeTypeId
    CeilingAttrDefaultHeightParam: ForgeTypeId
    FilledRegionMasking: ForgeTypeId
    BackgroundPatternColorParam: ForgeTypeId
    ForegroundPatternColorParam: ForgeTypeId
    BackgroundDraftPatternIdParam: ForgeTypeId
    ForegroundAnyPatternIdParam: ForgeTypeId
    ForegroundDraftPatternIdParam: ForgeTypeId
    BuilidingPadStructureIdParam: ForgeTypeId
    CeilingStructureIdParam: ForgeTypeId
    RoofStructureIdParam: ForgeTypeId
    FloorStructureIdParam: ForgeTypeId
    AnyPatternIdParamNoNo: ForgeTypeId
    FillPatternIdParamNoNo: ForgeTypeId
    ObjectStyleMaterialIdParam: ForgeTypeId
    WrappingAtInsertsParam: ForgeTypeId
    WrappingAtEndsParam: ForgeTypeId
    CoarseScaleFillPatternColor: ForgeTypeId
    ModelCategoryIdParam: ForgeTypeId
    HostIdParam: ForgeTypeId
    MaterialIdParam: ForgeTypeId
    CoarseScaleFillPatternIdParam: ForgeTypeId
    AnyPatternIdParam: ForgeTypeId
    WallStructureIdParam: ForgeTypeId
    SurfacePatternIdParam: ForgeTypeId
    FillPatternIdParam: ForgeTypeId
    IdParam: ForgeTypeId
    SelectionEditableOnly: ForgeTypeId
    EditedBy: ForgeTypeId
    ScheduleTopLevelOffsetParam: ForgeTypeId
    ScheduleBaseLevelOffsetParam: ForgeTypeId
    ScheduleTopLevelParam: ForgeTypeId
    ScheduleBaseLevelParam: ForgeTypeId
    ScheduleLevelParam: ForgeTypeId
    ElemRoomId: ForgeTypeId
    ElemRoomName: ForgeTypeId
    ElemRoomNumber: ForgeTypeId
    ElemPartitionParam: ForgeTypeId
    ElemFamilyAndTypeParam: ForgeTypeId
    ElemFamilyParam: ForgeTypeId
    ElemTypeParam: ForgeTypeId
    ElemTypeLabel: ForgeTypeId
    BrOrgFilter: ForgeTypeId
    BrOrgFolders: ForgeTypeId
    SymbolFamilyAndTypeNamesParam: ForgeTypeId
    SymbolFamilyNameParam: ForgeTypeId
    SymbolNameParam: ForgeTypeId
    SymbolIdParam: ForgeTypeId
    StructuralDisplayInHiddenViews: ForgeTypeId
    FloorParamSpanDirection: ForgeTypeId
    FloorParamIsStructural: ForgeTypeId
    HostPerimeterComputed: ForgeTypeId
    LevelParam: ForgeTypeId
    FloorHeightabovelevelParam: ForgeTypeId
    FloorAttrDefaultHeightParam: ForgeTypeId
    FloorAttrDefaultThicknessParam: ForgeTypeId
    FloorAttrThicknessParam: ForgeTypeId
    InsertOrientation: ForgeTypeId
    ProfileParamAlongPath: ForgeTypeId
    ProfileFamTypePlusNone: ForgeTypeId
    Profile2Angle: ForgeTypeId
    Profile2FamType: ForgeTypeId
    Profile2FlippedHor: ForgeTypeId
    Profile2OffsetY: ForgeTypeId
    Profile2OffsetX: ForgeTypeId
    Profile1Angle: ForgeTypeId
    Profile1FamType: ForgeTypeId
    Profile1FlippedHor: ForgeTypeId
    Profile1OffsetY: ForgeTypeId
    Profile1OffsetX: ForgeTypeId
    FamProfileUsage: ForgeTypeId
    SweepTrajSegmented: ForgeTypeId
    SweepMaxSegAngle: ForgeTypeId
    ModelOrSymbolic: ForgeTypeId
    ProfileAngle: ForgeTypeId
    ProfileFamType: ForgeTypeId
    ProfileFlippedHor: ForgeTypeId
    ProfileOffsetY: ForgeTypeId
    ProfileOffsetX: ForgeTypeId
    ExtrusionLength: ForgeTypeId
    CurveVisibilityParam: ForgeTypeId
    GeomVisibilityParam: ForgeTypeId
    ElementIsCutting: ForgeTypeId
    ExtrusionAutoParams: ForgeTypeId
    BlendEndParam: ForgeTypeId
    BlendStartParam: ForgeTypeId
    RevolutionEndAngle: ForgeTypeId
    RevolutionStartAngle: ForgeTypeId
    ExtrusionEndParam: ForgeTypeId
    ExtrusionStartParam: ForgeTypeId
    ExtrusionDepthParam: ForgeTypeId
    JointGapParam: ForgeTypeId
    FloorByFaceOffsetParam: ForgeTypeId
    ScheduleTypeForBrowser: ForgeTypeId
    ScheduleCategory: ForgeTypeId
    FaceroofOffsetParam: ForgeTypeId
    FaceroofLevelParam: ForgeTypeId
    RoofFacesLocation: ForgeTypeId
    RelatedToMass: ForgeTypeId
    FasciaDepthParam: ForgeTypeId
    RoofEaveCutParam: ForgeTypeId
    RoofRafterOrTrussParam: ForgeTypeId
    RoofBaseLevelParam: ForgeTypeId
    CurveWallOffsetRoofs: ForgeTypeId
    CurveWallOffset: ForgeTypeId
    ActualMaxRidgeHeightParam: ForgeTypeId
    RoofUptoLevelOffsetParam: ForgeTypeId
    RoofUptoLevelParam: ForgeTypeId
    RoofLevelOffsetParam: ForgeTypeId
    StructuralElevationAtBottomSurvey: ForgeTypeId
    StructuralElevationAtTopSurvey: ForgeTypeId
    StructuralFloorCoreThickness: ForgeTypeId
    StructuralElevationAtBottomCore: ForgeTypeId
    StructuralElevationAtTopCore: ForgeTypeId
    StructuralReferenceLevelElevation: ForgeTypeId
    RoofConstraintOffsetParam: ForgeTypeId
    RoofConstraintLevelParam: ForgeTypeId
    HostSseCurvedEdgeConditionParam: ForgeTypeId
    RoofAttrThicknessParam: ForgeTypeId
    RoofAttrDefaultThicknessParam: ForgeTypeId
    StructuralElevationAtTop: ForgeTypeId
    NodeConnectionStatus: ForgeTypeId
    WallStructuralSignificant: ForgeTypeId
    StructuralAnalyticalBeamRigidLink: ForgeTypeId
    StructuralAnalyticalColumnHorizontalProjectionPlane: ForgeTypeId
    StructuralAnalyticalBeamHorizontalProjectionPlane: ForgeTypeId
    ContinuousFootingBreakAtInsertsDisable: ForgeTypeId
    ContinuousFootingDefaultEndExtensionLength: ForgeTypeId
    StructuralAnalyticalTessellate: ForgeTypeId
    StructuralAnalyticalTessDeviation: ForgeTypeId
    StructuralAnalyticalHardPoints: ForgeTypeId
    StructuralBendDirAngle: ForgeTypeId
    StructuralDisplayInHiddenViewsColumn: ForgeTypeId
    StructuralDisplayInHiddenViewsFraming: ForgeTypeId
    StructuralFloorAnalyzesAs: ForgeTypeId
    StructuralAnalyzesAs: ForgeTypeId
    StructuralBeamCutbackForColumn: ForgeTypeId
    BeamVJustificationOtherValue: ForgeTypeId
    StructuralBeamOrientation: ForgeTypeId
    StructuralBeamEnd1Elevation: ForgeTypeId
    StructuralBeamEnd0Elevation: ForgeTypeId
    FamilyExportAsGeometry: ForgeTypeId
    StructuralFoundationLength: ForgeTypeId
    StructuralFoundationWidth: ForgeTypeId
    ContinuousFootingLength: ForgeTypeId
    ContinuousFootingEccentricity: ForgeTypeId
    ContinuousFootingStructuralUsage: ForgeTypeId
    ContinuousFootingBearingWidth: ForgeTypeId
    StructuralElevationAtBottom: ForgeTypeId
    FamilyStructFootingUseCapTop: ForgeTypeId
    StructuralCopingDistance: ForgeTypeId
    ContinuousFootingWidth: ForgeTypeId
    StructuralFoundationThickness: ForgeTypeId
    ContinuousFootingBottomHeel: ForgeTypeId
    ContinuousFootingTopHeel: ForgeTypeId
    ContinuousFootingBottomToe: ForgeTypeId
    ContinuousFootingTopToe: ForgeTypeId
    StructuralAnalyticalModel: ForgeTypeId
    StructuralAnalyticalColumnRigidLink: ForgeTypeId
    FamilyStructMaterialType: ForgeTypeId
    StructuralBottomReleaseMz: ForgeTypeId
    StructuralBottomReleaseMy: ForgeTypeId
    StructuralBottomReleaseMx: ForgeTypeId
    StructuralBottomReleaseFz: ForgeTypeId
    StructuralBottomReleaseFy: ForgeTypeId
    StructuralBottomReleaseFx: ForgeTypeId
    StructuralTopReleaseMz: ForgeTypeId
    StructuralTopReleaseMy: ForgeTypeId
    StructuralTopReleaseMx: ForgeTypeId
    StructuralTopReleaseFz: ForgeTypeId
    StructuralTopReleaseFy: ForgeTypeId
    StructuralTopReleaseFx: ForgeTypeId
    StructuralBottomReleaseType: ForgeTypeId
    StructuralTopReleaseType: ForgeTypeId
    StructuralAnalyticalProjectMemberPlaneColumnBottom: ForgeTypeId
    StructuralAnalyticalProjectMemberPlaneColumnTop: ForgeTypeId
    StructuralMaterialType: ForgeTypeId
    StructuralCamber: ForgeTypeId
    StructuralNumberOfStuds: ForgeTypeId
    StructuralEndReleaseMz: ForgeTypeId
    StructuralEndReleaseMy: ForgeTypeId
    StructuralEndReleaseMx: ForgeTypeId
    StructuralEndReleaseFz: ForgeTypeId
    StructuralEndReleaseFy: ForgeTypeId
    StructuralEndReleaseFx: ForgeTypeId
    StructuralStartReleaseMz: ForgeTypeId
    StructuralStartReleaseMy: ForgeTypeId
    StructuralStartReleaseMx: ForgeTypeId
    StructuralStartReleaseFz: ForgeTypeId
    StructuralStartReleaseFy: ForgeTypeId
    StructuralStartReleaseFx: ForgeTypeId
    StructuralEndReleaseType: ForgeTypeId
    StructuralStartReleaseType: ForgeTypeId
    StructuralWallBottomProjectionPlane: ForgeTypeId
    StructuralWallTopProjectionPlane: ForgeTypeId
    StructuralWallProjectionSurface: ForgeTypeId
    StructuralAnalyticalProjectFloorPlane: ForgeTypeId
    StructuralAnalyticalProjectMemberPlane: ForgeTypeId
    StructuralBraceRepresentation: ForgeTypeId
    StructuralStickSymbolLocation: ForgeTypeId
    StructuralBeamEndSupport: ForgeTypeId
    StructuralBeamStartSupport: ForgeTypeId
    CutTransparentInElevation: ForgeTypeId
    CutTransparentIn3d: ForgeTypeId
    WindowTypeId: ForgeTypeId
    WallSweepOrientation: ForgeTypeId
    StructuralAttachmentEndValueElevation: ForgeTypeId
    StructuralAttachmentStartValueElevation: ForgeTypeId
    StructuralAttachmentEndLevelReference: ForgeTypeId
    StructuralAttachmentStartLevelReference: ForgeTypeId
    StructuralAttachmentEndValueRatio: ForgeTypeId
    StructuralAttachmentStartValueRatio: ForgeTypeId
    StructuralAttachmentEndRefelementEnd: ForgeTypeId
    TypeWallClosure: ForgeTypeId
    StructuralAttachmentStartRefelementEnd: ForgeTypeId
    StructuralAttachmentEndValueDistance: ForgeTypeId
    StructuralAttachmentStartValueDistance: ForgeTypeId
    StructuralAttachmentEndType: ForgeTypeId
    StructuralAttachmentStartType: ForgeTypeId
    StructuralFrameCutLength: ForgeTypeId
    InstanceReferenceLevelParam: ForgeTypeId
    InstanceStructUsageParam: ForgeTypeId
    SketchPlaneParam: ForgeTypeId
    InstanceLengthParam: ForgeTypeId
    InstanceFreeHostId: ForgeTypeId
    InstanceMovesWithGridParam: ForgeTypeId
    InstanceOffsetPosParam: ForgeTypeId
    InstanceScheduleOnlyLevelParam: ForgeTypeId
    InstanceFreeHostOffsetParam: ForgeTypeId
    InstanceFreeHostParam: ForgeTypeId
    InstanceHeadHeightParam: ForgeTypeId
    InstanceSillHeightParam: ForgeTypeId
    InstanceElevationParam: ForgeTypeId
    FamilyTopLevelOffsetParam: ForgeTypeId
    FamilyBaseLevelOffsetParam: ForgeTypeId
    FamilyLevelParam: ForgeTypeId
    FamilyTopLevelParam: ForgeTypeId
    FamilyBaseLevelParam: ForgeTypeId
    FamilyRfaPathPseudoParam: ForgeTypeId
    FamilyCategoryPseudoParam: ForgeTypeId
    FamilyNamePseudoParam: ForgeTypeId
    FamilyUsagePseudoParam: ForgeTypeId
    FamilyWpbDefaultElevation: ForgeTypeId
    FamilyLineLengthParam: ForgeTypeId
    FamilyRoughWidthParam: ForgeTypeId
    FamilyRoughHeightParam: ForgeTypeId
    FamilyWindowInsetParam: ForgeTypeId
    FamilyThicknessParam: ForgeTypeId
    FamilyWidthParam: ForgeTypeId
    FamilyHeightParam: ForgeTypeId
    DoorEvacuationExitType: ForgeTypeId
    DoorOperationType: ForgeTypeId
    DoorFrameMaterial: ForgeTypeId
    DoorFrameType: ForgeTypeId
    DoorFinish: ForgeTypeId
    DoorConstructionType: ForgeTypeId
    FireRating: ForgeTypeId
    DoorCost: ForgeTypeId
    DoorNumber: ForgeTypeId
    UnconnectedHeightParam: ForgeTypeId
    UserTopConstraint: ForgeTypeId
    UserLevelConstraint: ForgeTypeId
    IsDepthParam: ForgeTypeId
    OffsetParam: ForgeTypeId
    WallOffsetFromHost: ForgeTypeId
    DpartOriginalCategoryId: ForgeTypeId
    DpartLayerConstruction: ForgeTypeId
    DpartPhaseDemolishedByOriginal: ForgeTypeId
    DpartPhaseCreatedByOriginal: ForgeTypeId
    DpartLengthComputed: ForgeTypeId
    DpartHeightComputed: ForgeTypeId
    DpartLayerWidth: ForgeTypeId
    DpartAreaComputed: ForgeTypeId
    DpartOriginalType: ForgeTypeId
    OffsetfacesShowShapeHandles: ForgeTypeId
    DpartLayerFunction: ForgeTypeId
    DpartVolumeComputed: ForgeTypeId
    DpartMaterialByOriginal: ForgeTypeId
    DpartMaterialIdParam: ForgeTypeId
    DpartOriginalFamily: ForgeTypeId
    DpartOriginalCategory: ForgeTypeId
    HostPanelScheduleAsPanelParam: ForgeTypeId
    WallLocationLineOffsetParam: ForgeTypeId
    WallKeyRefParam: ForgeTypeId
    Hosted: ForgeTypeId
    MeasureFromStructure: ForgeTypeId
    WallStructuralUsageParam: ForgeTypeId
    WallBottomIsAttached: ForgeTypeId
    WallTopIsAttached: ForgeTypeId
    WallTopOffset: ForgeTypeId
    WallBaseOffset: ForgeTypeId
    WallBaseConstraint: ForgeTypeId
    IsHeightParam: ForgeTypeId
    WallUserHeightParam: ForgeTypeId
    WallHeightType: ForgeTypeId
    WallBaseHeightParam: ForgeTypeId
    WallJoinVis: ForgeTypeId
    ScaleFactorParam: ForgeTypeId
    AllowAutoEmbed: ForgeTypeId
    WallAttrRoomBounding: ForgeTypeId
    FunctionParam: ForgeTypeId
    WallAttrDefheightParam: ForgeTypeId
    WallAttrHeightParam: ForgeTypeId
    WallAttrWidthParam: ForgeTypeId

class ParameterUtils:
    """.NET: Autodesk.Revit.DB.ParameterUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def DownloadCompanyName(document: Document, parameterTypeId: ForgeTypeId, region: str) -> str: ...
    @staticmethod
    def DownloadParameter(document: Document, options: ParameterDownloadOptions, parameterTypeId: ForgeTypeId, region: str) -> SharedParameterElement: ...
    @staticmethod
    def DownloadParameterOptions(parameterTypeId: ForgeTypeId, region: str) -> ParameterDownloadOptions: ...
    @staticmethod
    def GetAllBuiltInGroups() -> IList: ...
    @staticmethod
    def GetAllBuiltInParameters() -> IList: ...
    @staticmethod
    def GetBuiltInParameter(parameterTypeId: ForgeTypeId) -> BuiltInParameter: ...
    @staticmethod
    def GetBuiltInParameterGroupTypeId(parameterTypeId: ForgeTypeId) -> ForgeTypeId: ...
    @staticmethod
    def GetDefinition(parameterTypeId: ForgeTypeId) -> InternalDefinition: ...
    @staticmethod
    def GetParameterTypeId(builtInParam: BuiltInParameter) -> ForgeTypeId: ...
    @staticmethod
    def IsBuiltInGroup(groupTypeId: ForgeTypeId) -> bool: ...
    @staticmethod
    def IsBuiltInParameter(parameterId: ElementId) -> bool: ...
    @staticmethod
    def IsValidRegionCode(region: str) -> bool: ...
    @staticmethod
    def WriteSharedParametersToFile(doc: Document, fileName: str) -> None: ...

class ParameterValue:
    """.NET: Autodesk.Revit.DB.ParameterValue"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Copy(self, ) -> ParameterValue: ...
    def Dispose(self, ) -> None: ...
    def IsEqual(self, other: ParameterValue) -> bool: ...
    def IsSameType(self, other: ParameterValue) -> bool: ...

class ParameterValuePresenceRule(FilterRule):
    """.NET: Autodesk.Revit.DB.ParameterValuePresenceRule"""
    def __init__(self, *args) -> None: ...
    Parameter: ElementId
    IsValidObject: bool

class ParameterValueProvider(FilterableValueProvider):
    """.NET: Autodesk.Revit.DB.ParameterValueProvider"""
    def __init__(self, *args) -> None: ...
    Parameter: ElementId
    IsValidObject: bool

class ParametersOrder:
    """.NET: Autodesk.Revit.DB.ParametersOrder"""
    def __init__(self, *args) -> None: ...
    ...

class Part(Element):
    """.NET: Autodesk.Revit.DB.Part"""
    def __init__(self, *args) -> None: ...
    PartMaker: PartMaker
    Excluded: bool
    OriginalCategoryId: ElementId
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
    def CanOffsetFace(self, face: Face) -> bool: ...
    def GetFaceOffset(self, face: Face) -> float: ...
    def GetSourceElementIds(self, ) -> ICollection: ...
    def GetSourceElementOriginalCategoryIds(self, ) -> ICollection: ...
    def ResetFaceOffset(self, face: Face) -> None: ...
    def ResetPartShape(self, ) -> None: ...
    def SetFaceOffset(self, face: Face, offset: float) -> None: ...

class PartEdgeConditionOrientation:
    """.NET: Autodesk.Revit.DB.PartEdgeConditionOrientation"""
    def __init__(self, *args) -> None: ...
    ...

class PartMaker(Element):
    """.NET: Autodesk.Revit.DB.PartMaker"""
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
    def GetSourceElementIds(self, ) -> ICollection: ...
    def IsSourceElement(self, elemId: ElementId) -> bool: ...
    def SetSourceElementIds(self, sourceElementIds: ICollection) -> None: ...

class PartMakerMethodToDivideVolumes:
    """.NET: Autodesk.Revit.DB.PartMakerMethodToDivideVolumes"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    DivisionPatternMirror: bool
    DivisionRotationAngle: float
    VConstDivisionIndent: int
    UConstDivisionIndent: int
    DivisionRuleId: ElementId
    ProfileFlipAlong: bool
    ProfileFlipAcross: bool
    ProfileType: ElementId
    ProfileOffset: float
    DivisionGap: float
    ProfileMatch: PartEdgeConditionOrientation
    def AddIntersectingReference(self, intersectingReference: ElementId, offset: float) -> bool: ...
    @staticmethod
    def AreElementsValidIntersectingReferences(document: Document, elementIds: ICollection) -> bool: ...
    @staticmethod
    def CanBeDivisionProfile(familyId: ElementId, familyDocument: Document) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetOffsetForIntersectingReference(self, intersectingReference: ElementId) -> float: ...
    def GetPlaneOfSketch(self, ) -> Plane: ...
    def GetSketchCurves(self, curveArray: IList) -> None: ...
    def GetSplitRefsOffsets(self, ) -> IDictionary: ...
    @staticmethod
    def IsElementValidIntersectingReference(document: Document, elementId: ElementId) -> bool: ...
    @staticmethod
    def IsValidSketchPlane(document: Document, sketchPlaneId: ElementId) -> bool: ...
    def RemoveIntersectingReference(self, intersectingReference: ElementId) -> bool: ...
    def SetOffsetForIntersectingReference(self, intersectingReference: ElementId, offset: float) -> None: ...
    def UsesReference(self, intersectingReference: ElementId) -> bool: ...

class PartType:
    """.NET: Autodesk.Revit.DB.PartType"""
    def __init__(self, *args) -> None: ...
    ...

class PartUtils:
    """.NET: Autodesk.Revit.DB.PartUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def AreElementsValidForCreateParts(document: Document, elementIds: ICollection) -> bool: ...
    @staticmethod
    def ArePartsValidForDivide(document: Document, elementIdsToDivide: ICollection) -> bool: ...
    @staticmethod
    def ArePartsValidForMerge(document: Document, partIds: ICollection) -> bool: ...
    @staticmethod
    def CreateMergedPart(document: Document, partIds: ICollection) -> PartMaker: ...
    @staticmethod
    def CreateParts(document: Document, elementIds: ICollection) -> None: ...
    @staticmethod
    def DivideParts(document: Document, elementIdsToDivide: ICollection, intersectingReferenceIds: ICollection, curveArray: IList, sketchPlaneId: ElementId) -> PartMaker: ...
    @staticmethod
    def FindMergeableClusters(doc: Document, partIds: ICollection) -> IList: ...
    @staticmethod
    def GetAssociatedPartMaker(hostDocument: Document, elementId: ElementId) -> PartMaker: ...
    @staticmethod
    def GetAssociatedParts(hostDocument: Document, elementId: ElementId, includePartsWithAssociatedParts: bool, includeAllChildren: bool) -> ICollection: ...
    @staticmethod
    def GetChainLengthToOriginal(part: Part) -> int: ...
    @staticmethod
    def GetMergedParts(part: Part) -> ICollection: ...
    @staticmethod
    def GetPartMakerMethodToDivideVolumeFW(partMaker: PartMaker) -> PartMakerMethodToDivideVolumes: ...
    @staticmethod
    def GetSplittingCurves(document: Document, partId: ElementId, sketchPlane: Plane) -> IList: ...
    @staticmethod
    def GetSplittingElements(document: Document, partId: ElementId) -> ISet: ...
    @staticmethod
    def HasAssociatedParts(hostDocument: Document, elementId: ElementId) -> bool: ...
    @staticmethod
    def IsMergedPart(part: Part) -> bool: ...
    @staticmethod
    def IsPartDerivedFromLink(dPart: Part) -> bool: ...
    @staticmethod
    def IsValidForCreateParts(document: Document, hostOrLinkElementId: LinkElementId) -> bool: ...

class PartsVisibility:
    """.NET: Autodesk.Revit.DB.PartsVisibility"""
    def __init__(self, *args) -> None: ...
    ...

class Path3d(SketchBase):
    """.NET: Autodesk.Revit.DB.Path3d"""
    def __init__(self, *args) -> None: ...
    CurveLoop: CurveArray
    AllCurveLoops: CurveArrArray
    NumCurveLoops: int
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

class PathType:
    """.NET: Autodesk.Revit.DB.PathType"""
    def __init__(self, *args) -> None: ...
    ...

class PerformanceAdviser:
    """.NET: Autodesk.Revit.DB.PerformanceAdviser"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def AddRule(self, id: PerformanceAdviserRuleId, rule: IPerformanceAdviserRule) -> None: ...
    def DeleteRule(self, id: PerformanceAdviserRuleId) -> None: ...
    def Dispose(self, ) -> None: ...
    def ExecuteAllRules(self, document: Document) -> IList: ...
    def ExecuteRules(self, document: Document, rules: IList) -> IList: ...
    def GetAllRuleIds(self, ) -> IList: ...
    def GetElementFilterFromRule(self, index: int, document: Document) -> ElementFilter: ...
    def GetNumberOfRules(self, ) -> int: ...
    @staticmethod
    def GetPerformanceAdviser() -> PerformanceAdviser: ...
    def GetRuleDescription(self, index: int) -> str: ...
    def GetRuleId(self, index: int) -> PerformanceAdviserRuleId: ...
    def GetRuleName(self, index: int) -> str: ...
    def IsRuleEnabled(self, id: PerformanceAdviserRuleId) -> bool: ...
    def PostWarning(self, message: FailureMessage) -> None: ...
    def SetRuleEnabled(self, id: PerformanceAdviserRuleId, enabled: bool) -> None: ...
    def WillRuleCheckElements(self, index: int) -> bool: ...

class PerformanceAdviserRuleId(GuidEnum):
    """.NET: Autodesk.Revit.DB.PerformanceAdviserRuleId"""
    def __init__(self, *args) -> None: ...
    Guid: Guid

class PerformanceAdviserRules:
    """.NET: Autodesk.Revit.DB.PerformanceAdviserRules"""
    def __init__(self, *args) -> None: ...
    ...

class Phase(Element):
    """.NET: Autodesk.Revit.DB.Phase"""
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

class PhaseArray(APIObject):
    """.NET: Autodesk.Revit.DB.PhaseArray"""
    def __init__(self, *args) -> None: ...
    Item: Phase
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: Phase) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> PhaseArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: Phase, index: int) -> None: ...
    def ReverseIterator(self, ) -> PhaseArrayIterator: ...

class PhaseArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.PhaseArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class PhaseFilter(Element):
    """.NET: Autodesk.Revit.DB.PhaseFilter"""
    def __init__(self, *args) -> None: ...
    IsDefault: bool
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
    def Create(document: Document, name: str) -> PhaseFilter: ...
    def GetPhaseStatusPresentation(self, status: ElementOnPhaseStatus) -> PhaseStatusPresentation: ...
    def SetPhaseStatusPresentation(self, status: ElementOnPhaseStatus, presentation: PhaseStatusPresentation) -> None: ...

class PhaseStatusPresentation:
    """.NET: Autodesk.Revit.DB.PhaseStatusPresentation"""
    def __init__(self, *args) -> None: ...
    ...

class PlanCircuit(APIObject):
    """.NET: Autodesk.Revit.DB.PlanCircuit"""
    def __init__(self, *args) -> None: ...
    IsRoomLocated: bool
    Area: float
    SideNum: int
    IsReadOnly: bool
    def GetPointInside(self, ) -> UV: ...

class PlanCircuitSet(APIObject):
    """.NET: Autodesk.Revit.DB.PlanCircuitSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: PlanCircuit) -> bool: ...
    def Erase(self, item: PlanCircuit) -> int: ...
    def ForwardIterator(self, ) -> PlanCircuitSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: PlanCircuit) -> bool: ...
    def ReverseIterator(self, ) -> PlanCircuitSetIterator: ...

class PlanCircuitSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.PlanCircuitSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class PlanTopology(APIObject):
    """.NET: Autodesk.Revit.DB.PlanTopology"""
    def __init__(self, *args) -> None: ...
    Phase: Phase
    Circuits: PlanCircuitSet
    Level: Level
    IsReadOnly: bool
    def GetRoomIds(self, ) -> ICollection: ...

class PlanTopologySet(APIObject):
    """.NET: Autodesk.Revit.DB.PlanTopologySet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: PlanTopology) -> bool: ...
    def Erase(self, item: PlanTopology) -> int: ...
    def ForwardIterator(self, ) -> PlanTopologySetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: PlanTopology) -> bool: ...
    def ReverseIterator(self, ) -> PlanTopologySetIterator: ...

class PlanTopologySetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.PlanTopologySetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class PlanViewDirection:
    """.NET: Autodesk.Revit.DB.PlanViewDirection"""
    def __init__(self, *args) -> None: ...
    ...

class PlanViewPlane:
    """.NET: Autodesk.Revit.DB.PlanViewPlane"""
    def __init__(self, *args) -> None: ...
    ...

class PlanViewRange:
    """.NET: Autodesk.Revit.DB.PlanViewRange"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Current: ElementId
    LevelBelow: ElementId
    LevelAbove: ElementId
    Unlimited: ElementId
    def Dispose(self, ) -> None: ...
    def GetLevelId(self, planViewPlane: PlanViewPlane) -> ElementId: ...
    def GetOffset(self, planViewPlane: PlanViewPlane) -> float: ...
    def SetLevelId(self, planViewPlane: PlanViewPlane, id: ElementId) -> None: ...
    def SetOffset(self, planViewPlane: PlanViewPlane, offset: float) -> None: ...

class PlanViewRangeError:
    """.NET: Autodesk.Revit.DB.PlanViewRangeError"""
    def __init__(self, *args) -> None: ...
    ...

class PlanViewRangeLevel:
    """.NET: Autodesk.Revit.DB.PlanViewRangeLevel"""
    def __init__(self, *args) -> None: ...
    ...

class PlanarFace(Face):
    """.NET: Autodesk.Revit.DB.PlanarFace"""
    def __init__(self, *args) -> None: ...
    YVector: XYZ
    XVector: XYZ
    FaceNormal: XYZ
    Origin: XYZ
    Period: float
    IsCyclic: bool
    Area: float
    Reference: Reference
    IsTwoSided: bool
    MaterialElementId: ElementId
    EdgeLoops: EdgeArrayArray
    HasRegions: bool
    OrientationMatchesSurfaceOrientation: bool
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool

class Plane(Surface):
    """.NET: Autodesk.Revit.DB.Plane"""
    def __init__(self, *args) -> None: ...
    YVec: XYZ
    XVec: XYZ
    Origin: XYZ
    Normal: XYZ
    IsValidObject: bool
    OrientationMatchesParametricOrientation: bool
    @staticmethod
    def Create(frameOfReference: Frame) -> Plane: ...
    @staticmethod
    def CreateByNormalAndOrigin(normal: XYZ, origin: XYZ) -> Plane: ...
    @staticmethod
    def CreateByOriginAndBasis(origin: XYZ, basisX: XYZ, basisY: XYZ) -> Plane: ...
    @staticmethod
    def CreateByThreePoints(point1: XYZ, point2: XYZ, point3: XYZ) -> Plane: ...

class Point(GeometryObject):
    """.NET: Autodesk.Revit.DB.Point"""
    def __init__(self, *args) -> None: ...
    Reference: Reference
    Coord: XYZ
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool
    @staticmethod
    def Create(coord: XYZ, id: ElementId) -> Point: ...

class PointCloudColorMode:
    """.NET: Autodesk.Revit.DB.PointCloudColorMode"""
    def __init__(self, *args) -> None: ...
    ...

class PointCloudFoundStatus:
    """.NET: Autodesk.Revit.DB.PointCloudFoundStatus"""
    def __init__(self, *args) -> None: ...
    ...

class PointCloudInstance(Instance):
    """.NET: Autodesk.Revit.DB.PointCloudInstance"""
    def __init__(self, *args) -> None: ...
    SupportsOverrides: bool
    FilterAction: SelectionFilterAction
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
    def ContainsScan(self, scanName: str) -> bool: ...
    @staticmethod
    def Create(document: Document, typeId: ElementId, transform: Transform) -> PointCloudInstance: ...
    def GetPoints(self, filter: PointCloudFilter, averageDistance: float, numPoints: int) -> PointCollection: ...
    def GetRegions(self, ) -> IList: ...
    def GetScanOrigin(self, scanName: str) -> XYZ: ...
    def GetScans(self, ) -> IList: ...
    def GetSelectionFilter(self, ) -> PointCloudFilter: ...
    def HasColor(self, ) -> bool: ...
    def SetSelectionFilter(self, pFilter: PointCloudFilter) -> None: ...

class PointCloudType(ElementType):
    """.NET: Autodesk.Revit.DB.PointCloudType"""
    def __init__(self, *args) -> None: ...
    FoundStatus: PointCloudFoundStatus
    ColorEncoding: PointCloudColorEncoding
    Offset: XYZ
    Scale: float
    EngineIdentifier: str
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
    def Create(document: Document, engineIdentifier: str, typeIdentifier: str) -> PointCloudType: ...
    def GetPath(self, ) -> ModelPath: ...
    def GetReCapProject(self, ) -> RCProject: ...

class PointElementReference:
    """.NET: Autodesk.Revit.DB.PointElementReference"""
    def __init__(self, *args) -> None: ...
    ...

class PointLocationOnCurve:
    """.NET: Autodesk.Revit.DB.PointLocationOnCurve"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    MeasureFrom: PointOnCurveMeasureFrom
    MeasurementValue: float
    MeasurementType: PointOnCurveMeasurementType
    def Dispose(self, ) -> None: ...

class PointNode(ModelCurveNode):
    """.NET: Autodesk.Revit.DB.PointNode"""
    def __init__(self, *args) -> None: ...
    LineProperties: LineProperties
    IsValidObject: bool
    NodeName: str
    def GetPoint(self, ) -> Point: ...

class PointOnCurveMeasureFrom:
    """.NET: Autodesk.Revit.DB.PointOnCurveMeasureFrom"""
    def __init__(self, *args) -> None: ...
    ...

class PointOnCurveMeasurementType:
    """.NET: Autodesk.Revit.DB.PointOnCurveMeasurementType"""
    def __init__(self, *args) -> None: ...
    ...

class PointOnEdge(PointElementReference):
    """.NET: Autodesk.Revit.DB.PointOnEdge"""
    def __init__(self, *args) -> None: ...
    LocationOnCurve: PointLocationOnCurve
    def GetEdgeReference(self, ) -> Reference: ...
    def SetEdgeReference(self, reference: Reference) -> None: ...

class PointOnEdgeEdgeIntersection(PointElementReference):
    """.NET: Autodesk.Revit.DB.PointOnEdgeEdgeIntersection"""
    def __init__(self, *args) -> None: ...
    def GetEdgeReference1(self, ) -> Reference: ...
    def GetEdgeReference2(self, ) -> Reference: ...
    def SetEdgeReference1(self, edgeReference: Reference) -> None: ...
    def SetEdgeReference2(self, edgeReference: Reference) -> None: ...

class PointOnEdgeFaceIntersection(PointElementReference):
    """.NET: Autodesk.Revit.DB.PointOnEdgeFaceIntersection"""
    def __init__(self, *args) -> None: ...
    OrientWithEdge: bool
    def GetEdgeReference(self, ) -> Reference: ...
    def GetFaceReference(self, ) -> Reference: ...
    def SetEdgeReference(self, edgeReference: Reference) -> None: ...
    def SetFaceReference(self, reference: Reference) -> None: ...

class PointOnFace(PointElementReference):
    """.NET: Autodesk.Revit.DB.PointOnFace"""
    def __init__(self, *args) -> None: ...
    UV: UV
    def GetFaceReference(self, ) -> Reference: ...
    def SetFaceReference(self, reference: Reference) -> None: ...

class PointOnPlane(PointElementReference):
    """.NET: Autodesk.Revit.DB.PointOnPlane"""
    def __init__(self, *args) -> None: ...
    Offset: float
    XVec: UV
    Position: UV
    def GetPlaneReference(self, ) -> Reference: ...
    @staticmethod
    def IsValidPlaneReference(doc: Document, planeReference: Reference) -> bool: ...
    @staticmethod
    def NewPointOnPlane(doc: Document, planeReference: Reference, position: XYZ, xvec: XYZ) -> PointOnPlane: ...
    def SetPlaneReference(self, planeReference: Reference) -> None: ...

class PointRelativeToPoint(PointElementReference):
    """.NET: Autodesk.Revit.DB.PointRelativeToPoint"""
    def __init__(self, *args) -> None: ...
    def GetHostPointReference(self, ) -> Reference: ...
    def SetHostPointReference(self, hostPointReference: Reference) -> None: ...

class PolyLine(GeometryObject):
    """.NET: Autodesk.Revit.DB.PolyLine"""
    def __init__(self, *args) -> None: ...
    NumberOfCoordinates: int
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool
    def Clone(self, ) -> PolyLine: ...
    @staticmethod
    def Create(coordinates: IList) -> PolyLine: ...
    def Evaluate(self, param: float) -> XYZ: ...
    def GetCoordinate(self, index: int) -> XYZ: ...
    def GetCoordinates(self, ) -> IList: ...
    def GetOutline(self, ) -> Outline: ...
    def GetTransformed(self, transform: Transform) -> PolyLine: ...

class PolylineNode(ModelCurveNode):
    """.NET: Autodesk.Revit.DB.PolylineNode"""
    def __init__(self, *args) -> None: ...
    LineProperties: LineProperties
    IsValidObject: bool
    NodeName: str
    def GetPolyline(self, ) -> PolyLine: ...

class PolylineSegments:
    """.NET: Autodesk.Revit.DB.PolylineSegments"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LineProperties: LineProperties
    IsFilled: bool
    EndLocalParameter: float
    StartLocalParameter: float
    EndParameter: float
    StartParameter: float
    def Dispose(self, ) -> None: ...
    def GetVertices(self, ) -> IList: ...

class PolymeshFacet:
    """.NET: Autodesk.Revit.DB.PolymeshFacet"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    V3: int
    V2: int
    V1: int
    def GetVertices(self, ) -> IList: ...
    def ToString(self, ) -> str: ...

class PolymeshTopology:
    """.NET: Autodesk.Revit.DB.PolymeshTopology"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    NumberOfUVs: int
    NumberOfNormals: int
    NumberOfPoints: int
    NumberOfFacets: int
    DistributionOfNormals: DistributionOfNormals
    def Dispose(self, ) -> None: ...
    def GetFacet(self, idx: int) -> PolymeshFacet: ...
    def GetFacets(self, ) -> IList: ...
    def GetNormal(self, idx: int) -> XYZ: ...
    def GetNormals(self, ) -> IList: ...
    def GetPoint(self, idx: int) -> XYZ: ...
    def GetPoints(self, ) -> IList: ...
    def GetUV(self, idx: int) -> UV: ...
    def GetUVs(self, ) -> IList: ...

class PreferredJunctionType:
    """.NET: Autodesk.Revit.DB.PreferredJunctionType"""
    def __init__(self, *args) -> None: ...
    ...

class PreviewFamilyVisibilityMode:
    """.NET: Autodesk.Revit.DB.PreviewFamilyVisibilityMode"""
    def __init__(self, *args) -> None: ...
    ...

class PrimaryDesignOptionMemberFilter(ElementSlowFilter):
    """.NET: Autodesk.Revit.DB.PrimaryDesignOptionMemberFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool

class PrimarySizeCriterion(RoutingCriterionBase):
    """.NET: Autodesk.Revit.DB.PrimarySizeCriterion"""
    def __init__(self, *args) -> None: ...
    MaximumSize: float
    MinimumSize: float
    IsValidObject: bool
    @staticmethod
    def All() -> PrimarySizeCriterion: ...
    @staticmethod
    def None_() -> PrimarySizeCriterion: ...

class PrintManager(APIObject):
    """.NET: Autodesk.Revit.DB.PrintManager"""
    def __init__(self, *args) -> None: ...
    PaperSources: PaperSourceSet
    PaperSizes: PaperSizeSet
    IsVirtual: VirtualPrinterType
    Collate: bool
    PrintOrderReverse: bool
    CopyNumber: int
    PrintRange: PrintRange
    PrintToFileName: str
    CombinedFile: bool
    PrintToFile: bool
    ViewSheetSetting: ViewSheetSetting
    PrintSetup: PrintSetup
    PrinterName: str
    IsReadOnly: bool
    def Apply(self, ) -> None: ...
    def SelectNewPrintDriver(self, strPrinterName: str) -> None: ...
    def SubmitPrint(self, view: View) -> bool: ...

class PrintParameters(APIObject):
    """.NET: Autodesk.Revit.DB.PrintParameters"""
    def __init__(self, *args) -> None: ...
    MaskCoincidentLines: bool
    ReplaceHalftoneWithThinLines: bool
    HideCropBoundaries: bool
    HideScopeBoxes: bool
    HideUnreferencedViewTags: bool
    HideReforWorkPlanes: bool
    ViewLinksinBlue: bool
    ColorDepth: ColorDepthType
    RasterQuality: RasterQualityType
    HiddenLineViews: HiddenLineViewsType
    Zoom: int
    ZoomType: ZoomType
    OriginOffsetY: float
    OriginOffsetX: float
    UserDefinedMarginY: float
    UserDefinedMarginX: float
    MarginType: MarginType
    PaperPlacement: PaperPlacementType
    PaperSource: PaperSource
    PaperSize: PaperSize
    PageOrientation: PageOrientationType
    IsReadOnly: bool

class PrintRange:
    """.NET: Autodesk.Revit.DB.PrintRange"""
    def __init__(self, *args) -> None: ...
    ...

class PrintSetting(Element):
    """.NET: Autodesk.Revit.DB.PrintSetting"""
    def __init__(self, *args) -> None: ...
    PrintParameters: PrintParameters
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

class PrintSetup(APIObject):
    """.NET: Autodesk.Revit.DB.PrintSetup"""
    def __init__(self, *args) -> None: ...
    InSession: InSessionPrintSetting
    CurrentPrintSetting: IPrintSetting
    IsReadOnly: bool
    def Delete(self, ) -> bool: ...
    def Rename(self, newName: str) -> bool: ...
    def Revert(self, ) -> None: ...
    def Save(self, ) -> bool: ...
    def SaveAs(self, newName: str) -> bool: ...

class PrinterResolution:
    """.NET: Autodesk.Revit.DB.PrinterResolution"""
    def __init__(self, *args) -> None: ...
    ...

class Profile(GeometryObject):
    """.NET: Autodesk.Revit.DB.Profile"""
    def __init__(self, *args) -> None: ...
    Transformed: Profile
    Curves: CurveArray
    Filled: bool
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool
    def Clone(self, ) -> Profile: ...

class ProfileFamilyUsage:
    """.NET: Autodesk.Revit.DB.ProfileFamilyUsage"""
    def __init__(self, *args) -> None: ...
    ...

class ProfilePlaneLocation:
    """.NET: Autodesk.Revit.DB.ProfilePlaneLocation"""
    def __init__(self, *args) -> None: ...
    ...

class ProjectInfo(Element):
    """.NET: Autodesk.Revit.DB.ProjectInfo"""
    def __init__(self, *args) -> None: ...
    OrganizationDescription: str
    OrganizationName: str
    BuildingName: str
    Author: str
    Number: str
    Name: str
    Address: str
    ClientName: str
    Status: str
    IssueDate: str
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

class ProjectLocation(Instance):
    """.NET: Autodesk.Revit.DB.ProjectLocation"""
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
    def Create(document: Document, siteLocationId: ElementId, name: str) -> ProjectLocation: ...
    def Duplicate(self, name: str) -> ProjectLocation: ...
    def GetProjectPosition(self, point: XYZ) -> ProjectPosition: ...
    def GetSiteLocation(self, ) -> SiteLocation: ...
    @staticmethod
    def IsProjectLocationNameUnique(document: Document, name: str, siteLocationId: ElementId) -> bool: ...
    def SetProjectPosition(self, point: XYZ, position: ProjectPosition) -> None: ...

class ProjectLocationSet(APIObject):
    """.NET: Autodesk.Revit.DB.ProjectLocationSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: ProjectLocation) -> bool: ...
    def Erase(self, item: ProjectLocation) -> int: ...
    def ForwardIterator(self, ) -> ProjectLocationSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: ProjectLocation) -> bool: ...
    def ReverseIterator(self, ) -> ProjectLocationSetIterator: ...

class ProjectLocationSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.ProjectLocationSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ProjectPosition:
    """.NET: Autodesk.Revit.DB.ProjectPosition"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Angle: float
    Elevation: float
    NorthSouth: float
    EastWest: float
    def Dispose(self, ) -> None: ...

class PropOverrideMode:
    """.NET: Autodesk.Revit.DB.PropOverrideMode"""
    def __init__(self, *args) -> None: ...
    ...

class PropertyLine(Element):
    """.NET: Autodesk.Revit.DB.PropertyLine"""
    def __init__(self, *args) -> None: ...
    SketchId: ElementId
    Area: float
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
    def ConvertToTable(self, ) -> None: ...
    @staticmethod
    def Create(document: Document, pt: IList) -> PropertyLine: ...
    def GetBoundary(self, ) -> IList: ...
    def GetPropertyTable(self, ) -> IList: ...
    def GetStart(self, ) -> XYZ: ...
    def IsClosedLoop(self, ) -> bool: ...
    def IsSketchBased(self, ) -> bool: ...
    @staticmethod
    def IsValidBoundary(curveLoops: IList) -> bool: ...
    @staticmethod
    def IsValidPropertyTable(document: Document, pt: IList) -> bool: ...
    def IsValidToConvert(self, ) -> bool: ...
    def SetBoundary(self, curveLoops: IList) -> None: ...
    def SetPropertyTable(self, newTable: IList) -> None: ...
    def SetStart(self, start: XYZ) -> None: ...

class PropertySelectionType:
    """.NET: Autodesk.Revit.DB.PropertySelectionType"""
    def __init__(self, *args) -> None: ...
    ...

class PropertySetElement(Element):
    """.NET: Autodesk.Revit.DB.PropertySetElement"""
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
    def Create(document: Document, embodiedCarbonAsset: EmbodiedCarbonAsset) -> PropertySetElement: ...
    def Duplicate(self, document: Document, name: str) -> PropertySetElement: ...
    def GetEmbodiedCarbonAsset(self, ) -> EmbodiedCarbonAsset: ...
    def GetStructuralAsset(self, ) -> StructuralAsset: ...
    def GetThermalAsset(self, ) -> ThermalAsset: ...
    def SetEmbodiedCarbonAsset(self, embodiedCarbonAsset: EmbodiedCarbonAsset) -> None: ...
    def SetStructuralAsset(self, structuralAsset: StructuralAsset) -> None: ...
    def SetThermalAsset(self, thermalAsset: ThermalAsset) -> None: ...

class PropertySetupType:
    """.NET: Autodesk.Revit.DB.PropertySetupType"""
    def __init__(self, *args) -> None: ...
    ...

class PropertyTableEntry:
    """.NET: Autodesk.Revit.DB.PropertyTableEntry"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ArcDirection: PropertyTableEntryArcDirection
    CurveType: PropertyTableEntryCurveType
    Id: int
    Radius: float
    Bearing: float
    Distance: float
    @staticmethod
    def Create(distance: float, bearing: float, curveType: PropertyTableEntryCurveType, arcRadius: float, arcDir: PropertyTableEntryArcDirection, id: int) -> PropertyTableEntry: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def IsValidPropertyTableEntry(distance: float, bearing: float, curveType: PropertyTableEntryCurveType, arcRadius: float, arcDir: PropertyTableEntryArcDirection) -> bool: ...

class PropertyTableEntryArcDirection:
    """.NET: Autodesk.Revit.DB.PropertyTableEntryArcDirection"""
    def __init__(self, *args) -> None: ...
    ...

class PropertyTableEntryCurveType:
    """.NET: Autodesk.Revit.DB.PropertyTableEntryCurveType"""
    def __init__(self, *args) -> None: ...
    ...

class RPCNode(ContentNode):
    """.NET: Autodesk.Revit.DB.RPCNode"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    NodeName: str

class RadialArray(BaseArray):
    """.NET: Autodesk.Revit.DB.RadialArray"""
    def __init__(self, *args) -> None: ...
    NumMembers: int
    Label: FamilyParameter
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
    def ArrayElementWithoutAssociation(aDoc: Document, dBView: View, id: ElementId, count: int, axis: Line, angle: float, anchorMember: ArrayAnchorMember) -> ICollection: ...
    @staticmethod
    def ArrayElementsWithoutAssociation(aDoc: Document, dBView: View, ids: ICollection, count: int, axis: Line, angle: float, anchorMember: ArrayAnchorMember) -> ICollection: ...
    @staticmethod
    def Create(aDoc: Document, dBView: View, id: ElementId, count: int, axis: Line, angle: float, anchorMember: ArrayAnchorMember) -> RadialArray: ...
    def GetCopiedMemberIds(self, ) -> ICollection: ...
    @staticmethod
    def GetMinimumSize(document: Document) -> int: ...
    def GetNumberOfMembersIncludingPlaceholders(self, ) -> int: ...
    def GetOriginalMemberIds(self, ) -> ICollection: ...
    @staticmethod
    def IsRotationAngleValid(angle: float) -> bool: ...
    @staticmethod
    def IsValidNumberOfMembers(count: int, pADoc: Document) -> bool: ...

class RadialDimension(Dimension):
    """.NET: Autodesk.Revit.DB.RadialDimension"""
    def __init__(self, *args) -> None: ...
    IsValid: bool
    AreReferencesAvailable: bool
    TextPosition: XYZ
    Origin: XYZ
    LeaderEndPosition: XYZ
    HasLeader: bool
    ValueOverride: str
    Below: str
    Above: str
    Suffix: str
    Prefix: str
    IsLocked: bool
    ValueString: str
    Value: Nullable
    AreSegmentsEqual: bool
    Segments: DimensionSegmentArray
    NumberOfSegments: int
    DimensionShape: DimensionShape
    FamilyLabel: FamilyParameter
    Name: str
    DimensionType: DimensionType
    View: View
    Curve: Curve
    References: ReferenceArray
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
    def Create(document: Document, dbView: View, arcRef: Reference, isDiameter: bool) -> RadialDimension: ...

class RasterQualityType:
    """.NET: Autodesk.Revit.DB.RasterQualityType"""
    def __init__(self, *args) -> None: ...
    ...

class Rectangle:
    """.NET: Autodesk.Revit.DB.Rectangle"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Bottom: int
    Right: int
    Top: int
    Left: int
    def Dispose(self, ) -> None: ...
    def IsNormalized(self, ) -> bool: ...

class RectangularGridSegmentOrientation:
    """.NET: Autodesk.Revit.DB.RectangularGridSegmentOrientation"""
    def __init__(self, *args) -> None: ...
    ...

class Reference(APIObject):
    """.NET: Autodesk.Revit.DB.Reference"""
    def __init__(self, *args) -> None: ...
    UVPoint: UV
    GlobalPoint: XYZ
    ElementReferenceType: ElementReferenceType
    LinkedElementId: ElementId
    ElementId: ElementId
    IsReadOnly: bool
    def Contains(self, reference: Reference) -> bool: ...
    def ConvertToStableRepresentation(self, document: Document) -> str: ...
    def CreateLinkReference(self, revitLinkInstance: RevitLinkInstance) -> Reference: ...
    def CreateReferenceInLink(self, ) -> Reference: ...
    def EqualTo(self, reference: Reference) -> bool: ...
    @staticmethod
    def ParseFromStableRepresentation(document: Document, representation: str) -> Reference: ...

class ReferenceArray(APIObject):
    """.NET: Autodesk.Revit.DB.ReferenceArray"""
    def __init__(self, *args) -> None: ...
    Item: Reference
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: Reference) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> ReferenceArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: Reference, index: int) -> None: ...
    def ReverseIterator(self, ) -> ReferenceArrayIterator: ...

class ReferenceArrayArray(APIObject):
    """.NET: Autodesk.Revit.DB.ReferenceArrayArray"""
    def __init__(self, *args) -> None: ...
    Item: ReferenceArray
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: ReferenceArray) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> ReferenceArrayArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: ReferenceArray, index: int) -> None: ...
    def ReverseIterator(self, ) -> ReferenceArrayArrayIterator: ...

class ReferenceArrayArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.ReferenceArrayArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ReferenceArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.ReferenceArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ReferenceBaseOnHostType:
    """.NET: Autodesk.Revit.DB.ReferenceBaseOnHostType"""
    def __init__(self, *args) -> None: ...
    ...

class ReferenceIntersector:
    """.NET: Autodesk.Revit.DB.ReferenceIntersector"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    FindReferencesInRevitLinks: bool
    TargetType: FindReferenceTarget
    ViewId: ElementId
    def Dispose(self, ) -> None: ...
    def Find(self, origin: XYZ, direction: XYZ) -> IList: ...
    def FindNearest(self, origin: XYZ, direction: XYZ) -> ReferenceWithContext: ...
    def GetFilter(self, ) -> ElementFilter: ...
    def GetTargetElementIds(self, ) -> ICollection: ...
    def SetFilter(self, filter: ElementFilter) -> None: ...
    def SetTargetElementIds(self, elementIds: ICollection) -> None: ...

class ReferencePlane(DatumPlane):
    """.NET: Autodesk.Revit.DB.ReferencePlane"""
    def __init__(self, *args) -> None: ...
    Direction: XYZ
    Normal: XYZ
    FreeEnd: XYZ
    BubbleEnd: XYZ
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
    def Flip(self, ) -> None: ...
    def GetPlane(self, ) -> Plane: ...
    def GetReference(self, ) -> Reference: ...

class ReferencePoint(Element):
    """.NET: Autodesk.Revit.DB.ReferencePoint"""
    def __init__(self, *args) -> None: ...
    ShowNormalReferencePlaneOnly: bool
    CoordinatePlaneVisibility: CoordinatePlaneVisibility
    Visible: bool
    Position: XYZ
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
    def GetCoordinatePlaneReferenceXY(self, ) -> Reference: ...
    def GetCoordinatePlaneReferenceXZ(self, ) -> Reference: ...
    def GetCoordinatePlaneReferenceYZ(self, ) -> Reference: ...
    def GetCoordinateSystem(self, ) -> Transform: ...
    def GetHubId(self, ) -> ElementId: ...
    def GetInterpolatingCurves(self, ) -> CurveByPointsArray: ...
    def GetPointElementReference(self, ) -> PointElementReference: ...
    def GetVisibility(self, ) -> FamilyElementVisibility: ...
    def SetCoordinateSystem(self, coordinateSystem: Transform) -> None: ...
    def SetPointElementReference(self, pointElementReference: PointElementReference) -> None: ...
    def SetVisibility(self, visibility: FamilyElementVisibility) -> None: ...

class ReferencePointArray(APIObject):
    """.NET: Autodesk.Revit.DB.ReferencePointArray"""
    def __init__(self, *args) -> None: ...
    Item: ReferencePoint
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: ReferencePoint) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> ReferencePointArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: ReferencePoint, index: int) -> None: ...
    def ReverseIterator(self, ) -> ReferencePointArrayIterator: ...

class ReferencePointArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.ReferencePointArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ReferenceType:
    """.NET: Autodesk.Revit.DB.ReferenceType"""
    def __init__(self, *args) -> None: ...
    ...

class ReferenceUtils:
    """.NET: Autodesk.Revit.DB.ReferenceUtils"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class ReferenceWithContext:
    """.NET: Autodesk.Revit.DB.ReferenceWithContext"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Proximity: float
    def Dispose(self, ) -> None: ...
    def GetInstanceTransform(self, ) -> Transform: ...
    def GetReference(self, ) -> Reference: ...

class ReferenceableViewUtils:
    """.NET: Autodesk.Revit.DB.ReferenceableViewUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def ChangeReferencedView(document: Document, referenceId: ElementId, desiredViewId: ElementId) -> None: ...
    @staticmethod
    def GetReferencedViewId(document: Document, referenceId: ElementId) -> ElementId: ...

class RelinquishOptions:
    """.NET: Autodesk.Revit.DB.RelinquishOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    CheckedOutElements: bool
    UserWorksets: bool
    ViewWorksets: bool
    FamilyWorksets: bool
    StandardWorksets: bool
    def Dispose(self, ) -> None: ...

class RelinquishedItems:
    """.NET: Autodesk.Revit.DB.RelinquishedItems"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetRelinquishedElements(self, ) -> ICollection: ...
    def GetRelinquishedWorksets(self, ) -> ICollection: ...

class ReloadLatestOptions:
    """.NET: Autodesk.Revit.DB.ReloadLatestOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class ReloadSwapOutInfo:
    """.NET: Autodesk.Revit.DB.ReloadSwapOutInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    CurrentVersion: int
    PreviousVersion: int
    WasSwapped: bool
    Part: ElementId
    def Dispose(self, ) -> None: ...

class RenderDuration:
    """.NET: Autodesk.Revit.DB.RenderDuration"""
    def __init__(self, *args) -> None: ...
    ...

class RenderNode:
    """.NET: Autodesk.Revit.DB.RenderNode"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    NodeName: str
    def Dispose(self, ) -> None: ...

class RenderNodeAction:
    """.NET: Autodesk.Revit.DB.RenderNodeAction"""
    def __init__(self, *args) -> None: ...
    ...

class RenderingImageExposureSettings:
    """.NET: Autodesk.Revit.DB.RenderingImageExposureSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Saturation: float
    WhitePoint: float
    Shadows: float
    Highlights: float
    ExposureValue: float
    def Dispose(self, ) -> None: ...

class RenderingQuality:
    """.NET: Autodesk.Revit.DB.RenderingQuality"""
    def __init__(self, *args) -> None: ...
    ...

class RenderingQualitySettings:
    """.NET: Autodesk.Revit.DB.RenderingQualitySettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    RenderTime: int
    RenderLevel: int
    RenderDuration: RenderDuration
    LightAndMaterialAccuracyMode: LightAndMaterialAccuracyMode
    RenderingQuality: RenderingQuality
    def Dispose(self, ) -> None: ...
    def IsCustomQuality(self, ) -> bool: ...
    def IsValidRenderLevel(self, value: int) -> bool: ...
    def IsValidRenderTime(self, value: int) -> bool: ...

class RenderingSettings:
    """.NET: Autodesk.Revit.DB.RenderingSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ResolutionValue: int
    LightingSource: LightingSource
    PrinterResolution: PrinterResolution
    ResolutionTarget: ResolutionTarget
    BackgroundStyle: BackgroundStyle
    UsesRegionRendering: bool
    def Dispose(self, ) -> None: ...
    def GetBackgroundSettings(self, ) -> BackgroundSettings: ...
    def GetRenderingImageExposureSettings(self, ) -> RenderingImageExposureSettings: ...
    def GetRenderingQualitySettings(self, ) -> RenderingQualitySettings: ...
    def GetRenderingRegionOutline(self, ) -> Outline: ...
    def SetBackgroundSettings(self, background: BackgroundSettings) -> None: ...
    def SetRenderingImageExposureSettings(self, exposure: RenderingImageExposureSettings) -> None: ...
    def SetRenderingQualitySettings(self, settings: RenderingQualitySettings) -> None: ...

class RepeaterBounds:
    """.NET: Autodesk.Revit.DB.RepeaterBounds"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    DimensionCount: int
    def AdjustForCyclicalBounds(self, coordinates: RepeaterCoordinates) -> RepeaterCoordinates: ...
    def AreCoordinatesInBounds(self, coordinates: RepeaterCoordinates, treatCyclicalBoundsAsInfinite: bool) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetLowerBound(self, dimension: int) -> int: ...
    def GetUpperBound(self, dimension: int) -> int: ...
    def IsCyclical(self, dimension: int) -> bool: ...

class RepeaterCoordinates:
    """.NET: Autodesk.Revit.DB.RepeaterCoordinates"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    DimensionCount: int
    def Dispose(self, ) -> None: ...
    def GetCoordinate(self, dimension: int) -> int: ...

class RepeatingReferenceSource:
    """.NET: Autodesk.Revit.DB.RepeatingReferenceSource"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    DimensionCount: int
    def Dispose(self, ) -> None: ...
    def GetBounds(self, ) -> RepeaterBounds: ...
    @staticmethod
    def GetDefaultRepeatingReferenceSource(document: Document, elementId: ElementId) -> RepeatingReferenceSource: ...
    def GetReference(self, coordinates: RepeaterCoordinates) -> Reference: ...
    @staticmethod
    def HasRepeatingReferenceSource(document: Document, elementId: ElementId) -> bool: ...

class ResolutionTarget:
    """.NET: Autodesk.Revit.DB.ResolutionTarget"""
    def __init__(self, *args) -> None: ...
    ...

class ResourceVersionStatus:
    """.NET: Autodesk.Revit.DB.ResourceVersionStatus"""
    def __init__(self, *args) -> None: ...
    ...

class Revision(Element):
    """.NET: Autodesk.Revit.DB.Revision"""
    def __init__(self, *args) -> None: ...
    RevisionNumberingSequenceId: ElementId
    Visibility: RevisionVisibility
    RevisionDate: str
    IssuedBy: str
    IssuedTo: str
    Issued: bool
    Description: str
    RevisionNumber: str
    SequenceNumber: int
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
    def CombineWithNext(document: Document, revisionId: ElementId) -> ISet: ...
    @staticmethod
    def CombineWithPrevious(document: Document, revisionId: ElementId) -> ISet: ...
    @staticmethod
    def Create(document: Document) -> Revision: ...
    @staticmethod
    def GetAllRevisionIds(document: Document) -> IList: ...
    @staticmethod
    def ReorderRevisionSequence(document: Document, newSequence: IList) -> None: ...

class RevisionCloud(Element):
    """.NET: Autodesk.Revit.DB.RevisionCloud"""
    def __init__(self, *args) -> None: ...
    RevisionId: ElementId
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
    def Create(document: Document, view: View, revisionId: ElementId, curves: IList) -> RevisionCloud: ...
    def GetSheetIds(self, ) -> ISet: ...
    def GetSketchCurves(self, ) -> IList: ...
    def IsRevisionIssued(self, ) -> bool: ...

class RevisionNumberType:
    """.NET: Autodesk.Revit.DB.RevisionNumberType"""
    def __init__(self, *args) -> None: ...
    ...

class RevisionNumbering:
    """.NET: Autodesk.Revit.DB.RevisionNumbering"""
    def __init__(self, *args) -> None: ...
    ...

class RevisionNumberingSequence(Element):
    """.NET: Autodesk.Revit.DB.RevisionNumberingSequence"""
    def __init__(self, *args) -> None: ...
    NumberType: RevisionNumberType
    SequenceName: str
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
    def CreateAlphanumericSequence(document: Document, name: str, settings: AlphanumericRevisionSettings) -> RevisionNumberingSequence: ...
    @staticmethod
    def CreateNumericSequence(document: Document, name: str, settings: NumericRevisionSettings) -> RevisionNumberingSequence: ...
    @staticmethod
    def GetAllRevisionNumberingSequences(document: Document) -> ISet: ...
    def GetAlphanumericRevisionSettings(self, ) -> AlphanumericRevisionSettings: ...
    def GetNumericRevisionSettings(self, ) -> NumericRevisionSettings: ...
    def HasValidAlphanumericRevisionSettings(self, ) -> bool: ...
    def HasValidNumericRevisionSettings(self, ) -> bool: ...
    def HasValidRevisionSettingsForNumberType(self, ) -> bool: ...
    def SetAlphanumericRevisionSettings(self, settings: AlphanumericRevisionSettings) -> None: ...
    def SetNumericRevisionSettings(self, settings: NumericRevisionSettings) -> None: ...

class RevisionSettings(Element):
    """.NET: Autodesk.Revit.DB.RevisionSettings"""
    def __init__(self, *args) -> None: ...
    RevisionCloudSpacing: float
    RevisionNumbering: RevisionNumbering
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
    def GetRevisionSettings(ccda: Document) -> RevisionSettings: ...
    def IsAcceptableRevisionCloudSpacing(self, rawValue: float) -> bool: ...
    @staticmethod
    def RoundRevisionCloudSpacing(ccda: Document, rawValue: float) -> float: ...

class RevisionVisibility:
    """.NET: Autodesk.Revit.DB.RevisionVisibility"""
    def __init__(self, *args) -> None: ...
    ...

class RevitLinkGraphicsSettings:
    """.NET: Autodesk.Revit.DB.RevitLinkGraphicsSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LineWeights: LinkVisibility
    NestedLinks: LinkVisibility
    ObjectStyles: LinkVisibility
    ColorFill: LinkVisibility
    ViewRange: LinkVisibility
    ViewFilterType: LinkVisibility
    LinkVisibilityType: LinkVisibility
    LinkedViewId: ElementId
    def Dispose(self, ) -> None: ...
    def GetDiscipline(self, ) -> ViewDiscipline: ...
    def GetDisciplineType(self, ) -> LinkVisibility: ...
    def GetPhaseFilterId(self, ) -> ElementId: ...
    def GetPhaseFilterType(self, ) -> LinkVisibility: ...
    def GetPhaseId(self, ) -> ElementId: ...
    def GetPhaseType(self, ) -> LinkVisibility: ...
    def GetViewDetailLevel(self, ) -> ViewDetailLevel: ...
    def GetViewDetailLevelType(self, ) -> LinkVisibility: ...
    @staticmethod
    def IsViewRangeSupported(view: View) -> bool: ...
    def SetDiscipline(self, disciplineType: LinkVisibility, discipline: ViewDiscipline) -> None: ...
    def SetPhase(self, phaseType: LinkVisibility, phaseId: ElementId) -> None: ...
    def SetPhaseFilter(self, phaseFilterType: LinkVisibility, phaseFilterId: ElementId) -> None: ...
    def SetViewDetailLevel(self, viewDetailLevelType: LinkVisibility, viewDetailLevel: ViewDetailLevel) -> None: ...

class RevitLinkInstance(Instance):
    """.NET: Autodesk.Revit.DB.RevitLinkInstance"""
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
    def Create(document: Document, revitLinkTypeId: ElementId, placement: ImportPlacement) -> RevitLinkInstance: ...
    def GetLinkDocument(self, ) -> Document: ...
    def MoveBasePointToHostBasePoint(self, resetToOriginalRotation: bool) -> None: ...
    def MoveOriginToHostOrigin(self, resetToOriginalRotation: bool) -> None: ...

class RevitLinkOperations(LinkOperations):
    """.NET: Autodesk.Revit.DB.RevitLinkOperations"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def SetGetLocalPathForOpenCallback(self, makeLocalCopyForOpen: IGetLocalPathForOpenCallback) -> None: ...

class RevitLinkOptions:
    """.NET: Autodesk.Revit.DB.RevitLinkOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsRelative: bool
    def Dispose(self, ) -> None: ...
    def GetWorksetConfiguration(self, ) -> WorksetConfiguration: ...
    def SetWorksetConfiguration(self, config: WorksetConfiguration) -> None: ...

class RevitLinkType(ElementType):
    """.NET: Autodesk.Revit.DB.RevitLinkType"""
    def __init__(self, *args) -> None: ...
    LocallyUnloaded: bool
    AttachmentType: AttachmentType
    IsNestedLink: bool
    PathType: PathType
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
    def Create(document: Document, resourceReference: ExternalResourceReference, options: RevitLinkOptions) -> LinkLoadResult: ...
    @staticmethod
    def CreateFromIFC(document: Document, resourceReference: ExternalResourceReference, revitLinkedFilePath: str, recreateLink: bool, options: RevitLinkOptions) -> LinkLoadResult: ...
    def GetChildIds(self, ) -> ICollection: ...
    def GetConversionData(self, ) -> LinkConversionData: ...
    def GetLinkedFileStatus(self, ) -> LinkedFileStatus: ...
    def GetParentId(self, ) -> ElementId: ...
    def GetPhaseMap(self, ) -> IDictionary: ...
    def GetRootId(self, ) -> ElementId: ...
    @staticmethod
    def GetTopLevelLink(document: Document, reference: ExternalResourceReference) -> ElementId: ...
    def HasSaveablePositions(self, ) -> bool: ...
    def IsFromLocalPath(self, ) -> bool: ...
    def IsFromRevitServer(self, ) -> bool: ...
    @staticmethod
    def IsLoaded(document: Document, typeId: ElementId) -> bool: ...
    def IsNotLoadedIntoMultipleOpenDocuments(self, ) -> bool: ...
    def Load(self, ) -> LinkLoadResult: ...
    def LoadFrom(self, path: ModelPath, config: WorksetConfiguration) -> LinkLoadResult: ...
    def Reload(self, ) -> LinkLoadResult: ...
    def RevertLocalUnloadStatus(self, ) -> LinkedFileStatus: ...
    def SavePositions(self, callback: ISaveSharedCoordinatesCallback) -> bool: ...
    def Unload(self, callback: ISaveSharedCoordinatesCallback) -> None: ...
    def UnloadLocally(self, callback: ISaveSharedCoordinatesCallbackForUnloadLocally) -> bool: ...
    def UpdateFromIFC(self, document: Document, resourceReference: ExternalResourceReference, revitLinkedFilePath: str, recreateLink: bool) -> bool: ...

class Revolution(GenericForm):
    """.NET: Autodesk.Revit.DB.Revolution"""
    def __init__(self, *args) -> None: ...
    Axis: ModelLine
    EndAngle: float
    StartAngle: float
    Sketch: Sketch
    Subcategory: Category
    Name: str
    IsSolid: bool
    Visible: bool
    Combinations: GeomCombinationSet
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

class RevolvedFace(Face):
    """.NET: Autodesk.Revit.DB.RevolvedFace"""
    def __init__(self, *args) -> None: ...
    Curve: Curve
    Radius: XYZ
    Axis: XYZ
    Origin: XYZ
    Period: float
    IsCyclic: bool
    Area: float
    Reference: Reference
    IsTwoSided: bool
    MaterialElementId: ElementId
    EdgeLoops: EdgeArrayArray
    HasRegions: bool
    OrientationMatchesSurfaceOrientation: bool
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool

class RevolvedSurface(Surface):
    """.NET: Autodesk.Revit.DB.RevolvedSurface"""
    def __init__(self, *args) -> None: ...
    Origin: XYZ
    YDir: XYZ
    XDir: XYZ
    Axis: XYZ
    IsValidObject: bool
    OrientationMatchesParametricOrientation: bool
    @staticmethod
    def Create(axisBasePoint: XYZ, axisDirection: XYZ, profileCurve: Curve, startAngle: float, endAngle: float) -> Surface: ...
    def GetProfileCurve(self, ) -> Curve: ...
    def GetProfileCurveInWorldCoordinates(self, ) -> Curve: ...
    @staticmethod
    def IsValidProfileCurve(axisBasePoint: XYZ, axisDirection: XYZ, profileCurve: Curve) -> bool: ...

class RoofBase(HostObject):
    """.NET: Autodesk.Revit.DB.RoofBase"""
    def __init__(self, *args) -> None: ...
    FasciaDepth: float
    EaveCuts: EaveCutterType
    RoofType: RoofType
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
    def GetSlabShapeEditor(self, ) -> SlabShapeEditor: ...

class RoofType(HostObjAttributes):
    """.NET: Autodesk.Revit.DB.RoofType"""
    def __init__(self, *args) -> None: ...
    ThermalProperties: ThermalProperties
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

class RoundingMethod:
    """.NET: Autodesk.Revit.DB.RoundingMethod"""
    def __init__(self, *args) -> None: ...
    ...

class RoutingCondition:
    """.NET: Autodesk.Revit.DB.RoutingCondition"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Diameter: float
    def Dispose(self, ) -> None: ...

class RoutingConditions:
    """.NET: Autodesk.Revit.DB.RoutingConditions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    PreferredJunctionType: PreferredJunctionType
    ErrorLevel: RoutingPreferenceErrorLevel
    def AppendCondition(self, condition: RoutingCondition) -> None: ...
    def Clear(self, ) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetConditionAt(self, index: int) -> RoutingCondition: ...
    def GetNumberOfConditions(self, ) -> int: ...

class RoutingCriterionBase:
    """.NET: Autodesk.Revit.DB.RoutingCriterionBase"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def IsEqual(self, pOther: RoutingCriterionBase) -> bool: ...

class RoutingPreferenceErrorLevel:
    """.NET: Autodesk.Revit.DB.RoutingPreferenceErrorLevel"""
    def __init__(self, *args) -> None: ...
    ...

class RoutingPreferenceManager:
    """.NET: Autodesk.Revit.DB.RoutingPreferenceManager"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    OwnerId: ElementId
    PreferredJunctionType: PreferredJunctionType
    def AddRule(self, groupType: RoutingPreferenceRuleGroupType, rule: RoutingPreferenceRule, index: int) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetMEPPartId(self, groupType: RoutingPreferenceRuleGroupType, conditions: RoutingConditions) -> ElementId: ...
    def GetNumberOfRules(self, eGroupType: RoutingPreferenceRuleGroupType) -> int: ...
    def GetRule(self, groupType: RoutingPreferenceRuleGroupType, index: int) -> RoutingPreferenceRule: ...
    def GetSharedSizes(self, size: float, shape: ConnectorProfileType) -> IList: ...
    def RemoveRule(self, groupType: RoutingPreferenceRuleGroupType, index: int) -> None: ...

class RoutingPreferenceRule:
    """.NET: Autodesk.Revit.DB.RoutingPreferenceRule"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    RoutingPreferenceManager: RoutingPreferenceManager
    NumberOfCriteria: int
    MEPPartId: ElementId
    Description: str
    def AddCriterion(self, myCriterion: RoutingCriterionBase) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetCriterion(self, index: int) -> RoutingCriterionBase: ...
    def RemoveCriteron(self, index: int) -> None: ...

class RoutingPreferenceRuleGroupType:
    """.NET: Autodesk.Revit.DB.RoutingPreferenceRuleGroupType"""
    def __init__(self, *args) -> None: ...
    ...

class RowHeightOverrideOptions:
    """.NET: Autodesk.Revit.DB.RowHeightOverrideOptions"""
    def __init__(self, *args) -> None: ...
    ...

class RuledFace(Face):
    """.NET: Autodesk.Revit.DB.RuledFace"""
    def __init__(self, *args) -> None: ...
    IsExtruded: bool
    RulingsAreParallel: bool
    Point: XYZ
    Curve: Curve
    Period: float
    IsCyclic: bool
    Area: float
    Reference: Reference
    IsTwoSided: bool
    MaterialElementId: ElementId
    EdgeLoops: EdgeArrayArray
    HasRegions: bool
    OrientationMatchesSurfaceOrientation: bool
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool

class RuledSurface(Surface):
    """.NET: Autodesk.Revit.DB.RuledSurface"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    OrientationMatchesParametricOrientation: bool
    @staticmethod
    def Create(profileCurve: Curve, point: XYZ) -> Surface: ...
    def GetFirstProfileCurve(self, ) -> Curve: ...
    def GetFirstProfilePoint(self, ) -> XYZ: ...
    def GetSecondProfileCurve(self, ) -> Curve: ...
    def GetSecondProfilePoint(self, ) -> XYZ: ...
    def HasFirstProfilePoint(self, ) -> bool: ...
    def HasSecondProfilePoint(self, ) -> bool: ...

class SATExportOptions:
    """.NET: Autodesk.Revit.DB.SATExportOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class SATImportOptions(BaseImportOptions):
    """.NET: Autodesk.Revit.DB.SATImportOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ReferencePoint: XYZ
    AutoCorrectAlmostVHLines: bool
    VisibleLayersOnly: bool
    CustomScale: float
    OrientToView: bool
    ThisViewOnly: bool
    Placement: ImportPlacement
    ColorMode: ImportColorMode
    Unit: ImportUnit

class SKPImportOptions(BaseImportOptions):
    """.NET: Autodesk.Revit.DB.SKPImportOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ReferencePoint: XYZ
    AutoCorrectAlmostVHLines: bool
    VisibleLayersOnly: bool
    CustomScale: float
    OrientToView: bool
    ThisViewOnly: bool
    Placement: ImportPlacement
    ColorMode: ImportColorMode
    Unit: ImportUnit

class SSEPointVisibilitySettings(Element):
    """.NET: Autodesk.Revit.DB.SSEPointVisibilitySettings"""
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
    def GetVisibility(document: Document, categoryId: ElementId) -> bool: ...
    @staticmethod
    def SetVisibility(document: Document, categoryId: ElementId, isVisible: bool) -> None: ...

class STEPApplicationProtocol:
    """.NET: Autodesk.Revit.DB.STEPApplicationProtocol"""
    def __init__(self, *args) -> None: ...
    ...

class STEPExportOptions(BIMExportOptions):
    """.NET: Autodesk.Revit.DB.STEPExportOptions"""
    def __init__(self, *args) -> None: ...
    ApplicationProtocol: STEPApplicationProtocol
    TargetUnit: ExportUnit
    IsValidObject: bool
    ViewId: ElementId

class STEPImportOptions(BaseImportOptions):
    """.NET: Autodesk.Revit.DB.STEPImportOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ReferencePoint: XYZ
    AutoCorrectAlmostVHLines: bool
    VisibleLayersOnly: bool
    CustomScale: float
    OrientToView: bool
    ThisViewOnly: bool
    Placement: ImportPlacement
    ColorMode: ImportColorMode
    Unit: ImportUnit

class STLExportOptions(BIMExportOptions):
    """.NET: Autodesk.Revit.DB.STLExportOptions"""
    def __init__(self, *args) -> None: ...
    GridAspectRatio: float
    MaxEdgeLength: float
    NormalTolerance: float
    SurfaceTolerance: float
    ExportColor: bool
    TargetUnit: ExportUnit
    ExportBinary: bool
    IsValidObject: bool
    ViewId: ElementId
    def IsGridAspectRatioSet(self, ) -> bool: ...
    def IsMaxEdgeLengthSet(self, ) -> bool: ...
    def IsNormalToleranceSet(self, ) -> bool: ...
    def IsSurfaceToleranceSet(self, ) -> bool: ...
    @staticmethod
    def IsValidForGridAspectRatio(value: float) -> bool: ...
    @staticmethod
    def IsValidForMaxEdgeLength(value: float) -> bool: ...
    @staticmethod
    def IsValidForNormalTolerance(value: float) -> bool: ...
    @staticmethod
    def IsValidForSurfaceTolerance(value: float) -> bool: ...
    def SetTessellationSettings(self, resolutionType: ExportResolution) -> None: ...

class STLImportOptions(BaseImportOptions):
    """.NET: Autodesk.Revit.DB.STLImportOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ReferencePoint: XYZ
    AutoCorrectAlmostVHLines: bool
    VisibleLayersOnly: bool
    CustomScale: float
    OrientToView: bool
    ThisViewOnly: bool
    Placement: ImportPlacement
    ColorMode: ImportColorMode
    Unit: ImportUnit

class SaveAsOptions:
    """.NET: Autodesk.Revit.DB.SaveAsOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Compact: bool
    MaximumBackups: int
    PreviewViewId: ElementId
    OverwriteExistingFile: bool
    def Dispose(self, ) -> None: ...
    def GetWorksharingOptions(self, ) -> WorksharingSaveAsOptions: ...
    def SetWorksharingOptions(self, worksharingOptions: WorksharingSaveAsOptions) -> None: ...

class SaveModifiedLinksOptions:
    """.NET: Autodesk.Revit.DB.SaveModifiedLinksOptions"""
    def __init__(self, *args) -> None: ...
    ...

class SaveModifiedLinksOptionsForUnloadLocally:
    """.NET: Autodesk.Revit.DB.SaveModifiedLinksOptionsForUnloadLocally"""
    def __init__(self, *args) -> None: ...
    ...

class SaveOptions:
    """.NET: Autodesk.Revit.DB.SaveOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Compact: bool
    PreviewViewId: ElementId
    def Dispose(self, ) -> None: ...

class SchedulableField:
    """.NET: Autodesk.Revit.DB.SchedulableField"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ParameterId: ElementId
    FieldType: ScheduleFieldType
    def Dispose(self, ) -> None: ...
    def Equals(self, obj: object) -> bool: ...
    def GetCustomFieldData(self, ) -> CustomFieldData: ...
    def GetHashCode(self, ) -> int: ...
    def GetName(self, document: Document) -> str: ...

class ScheduleDefinition:
    """.NET: Autodesk.Revit.DB.ScheduleDefinition"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsFilteredBySheet: bool
    ShowGridLines: bool
    ShowHeaders: bool
    ShowTitle: bool
    GrandTotalTitle: str
    ShowGrandTotalCount: bool
    ShowGrandTotalTitle: bool
    ShowGrandTotal: bool
    IsEmbedded: bool
    HasEmbeddedSchedule: bool
    EmbeddedDefinition: ScheduleDefinition
    IsItemized: bool
    IncludeLinkedFiles: bool
    IsMaterialTakeoff: bool
    IsKeySchedule: bool
    FamilyId: ElementId
    AreaSchemeId: ElementId
    CategoryId: ElementId
    def AddEmbeddedSchedule(self, categoryId: ElementId) -> None: ...
    def AddField(self, fieldType: ScheduleFieldType, parameterId: ElementId) -> ScheduleField: ...
    def AddFilter(self, filter: ScheduleFilter) -> None: ...
    def AddSortGroupField(self, sortGroupField: ScheduleSortGroupField) -> None: ...
    def CanFilter(self, ) -> bool: ...
    def CanFilterByGlobalParameters(self, fieldId: ScheduleFieldId) -> bool: ...
    def CanFilterByParameterExistence(self, fieldId: ScheduleFieldId) -> bool: ...
    def CanFilterBySubstring(self, fieldId: ScheduleFieldId) -> bool: ...
    def CanFilterByValue(self, fieldId: ScheduleFieldId) -> bool: ...
    def CanFilterByValuePresence(self, fieldId: ScheduleFieldId) -> bool: ...
    def CanHaveEmbeddedSchedule(self, ) -> bool: ...
    def CanIncludeLinkedFiles(self, ) -> bool: ...
    def CanSortByField(self, fieldId: ScheduleFieldId) -> bool: ...
    def ClearFields(self, ) -> None: ...
    def ClearFilters(self, ) -> None: ...
    def ClearSortGroupFields(self, ) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetField(self, fieldId: ScheduleFieldId) -> ScheduleField: ...
    def GetFieldCount(self, ) -> int: ...
    def GetFieldId(self, index: int) -> ScheduleFieldId: ...
    def GetFieldIndex(self, fieldId: ScheduleFieldId) -> int: ...
    def GetFieldOrder(self, ) -> IList: ...
    def GetFilter(self, index: int) -> ScheduleFilter: ...
    def GetFilterCount(self, ) -> int: ...
    def GetFilters(self, ) -> IList: ...
    def GetSchedulableFields(self, ) -> IList: ...
    def GetSortGroupField(self, index: int) -> ScheduleSortGroupField: ...
    def GetSortGroupFieldCount(self, ) -> int: ...
    def GetSortGroupFields(self, ) -> IList: ...
    def GetValidCategoriesForEmbeddedSchedule(self, ) -> ICollection: ...
    def InsertCombinedParameterField(self, data: IList, fieldName: str, index: int) -> ScheduleField: ...
    def InsertField(self, fieldType: ScheduleFieldType, parameterId: ElementId, index: int) -> ScheduleField: ...
    def InsertFilter(self, filter: ScheduleFilter, index: int) -> None: ...
    def InsertSortGroupField(self, sortGroupField: ScheduleSortGroupField, index: int) -> None: ...
    def IsSchedulableField(self, schedulableField: SchedulableField) -> bool: ...
    def IsValidCategoryForEmbeddedSchedule(self, categoryId: ElementId) -> bool: ...
    def IsValidCategoryForFilterBySheet(self, ) -> bool: ...
    def IsValidCombinedParameters(self, data: IList) -> bool: ...
    def IsValidFieldId(self, fieldId: ScheduleFieldId) -> bool: ...
    def IsValidFieldIndex(self, index: int) -> bool: ...
    def RemoveEmbeddedSchedule(self, ) -> None: ...
    def RemoveField(self, fieldId: ScheduleFieldId) -> None: ...
    def RemoveFilter(self, index: int) -> None: ...
    def RemoveSortGroupField(self, index: int) -> None: ...
    def SetFieldOrder(self, fieldIds: IList) -> None: ...
    def SetFilter(self, index: int, filter: ScheduleFilter) -> None: ...
    def SetFilters(self, filters: IList) -> None: ...
    def SetSortGroupField(self, index: int, sortGroupField: ScheduleSortGroupField) -> None: ...
    def SetSortGroupFields(self, sortGroupFields: IList) -> None: ...

class ScheduleField:
    """.NET: Autodesk.Revit.DB.ScheduleField"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    FieldIndex: int
    FieldId: ScheduleFieldId
    Definition: ScheduleDefinition
    Schedule: ViewSchedule
    HasSchedulableField: bool
    IsCombinedParameterField: bool
    IsCalculatedField: bool
    MultipleValuesCustomText: str
    MultipleValuesText: str
    MultipleValuesDisplayType: ScheduleFieldMultipleValuesDisplayType
    GridColumnWidth: float
    SheetColumnWidth: float
    IsOverridden: bool
    HeadingOrientation: ScheduleHeadingOrientation
    VerticalAlignment: ScheduleVerticalAlignment
    HorizontalAlignment: ScheduleHorizontalAlignment
    DisplayType: ScheduleFieldDisplayType
    TotalByAssemblyType: bool
    ColumnHeading: str
    IsHidden: bool
    PercentageBy: ScheduleFieldId
    PercentageOf: ScheduleFieldId
    ParameterId: ElementId
    FieldType: ScheduleFieldType
    def CanDisplayMinMax(self, ) -> bool: ...
    def CanTotal(self, ) -> bool: ...
    def CanTotalByAssemblyType(self, ) -> bool: ...
    def CreatesCircularReferences(self, fieldId: ScheduleFieldId) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetCombinedParameters(self, ) -> IList: ...
    def GetCustomFieldData(self, ) -> CustomFieldData: ...
    def GetFormatOptions(self, ) -> FormatOptions: ...
    def GetName(self, ) -> str: ...
    def GetSchedulableField(self, ) -> SchedulableField: ...
    def GetSpecTypeId(self, ) -> ForgeTypeId: ...
    def GetStyle(self, ) -> TableCellStyle: ...
    def IsValidCombinedParameters(self, data: IList) -> bool: ...
    def ResetOverride(self, ) -> None: ...
    def SetCombinedParameters(self, data: IList) -> None: ...
    def SetFormatOptions(self, formatOptions: FormatOptions) -> None: ...
    def SetStyle(self, style: TableCellStyle) -> None: ...

class ScheduleFieldDisplayType:
    """.NET: Autodesk.Revit.DB.ScheduleFieldDisplayType"""
    def __init__(self, *args) -> None: ...
    ...

class ScheduleFieldId:
    """.NET: Autodesk.Revit.DB.ScheduleFieldId"""
    def __init__(self, *args) -> None: ...
    InvalidScheduleFieldId: ScheduleFieldId
    IntegerValue: int
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, ) -> str: ...

class ScheduleFieldMultipleValuesDisplayType:
    """.NET: Autodesk.Revit.DB.ScheduleFieldMultipleValuesDisplayType"""
    def __init__(self, *args) -> None: ...
    ...

class ScheduleFieldType:
    """.NET: Autodesk.Revit.DB.ScheduleFieldType"""
    def __init__(self, *args) -> None: ...
    ...

class ScheduleFilter:
    """.NET: Autodesk.Revit.DB.ScheduleFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsElementIdValue: bool
    IsDoubleValue: bool
    IsStringValue: bool
    IsIntegerValue: bool
    IsNullValue: bool
    FilterType: ScheduleFilterType
    FieldId: ScheduleFieldId
    def Dispose(self, ) -> None: ...
    def GetDoubleValue(self, ) -> float: ...
    def GetElementIdValue(self, ) -> ElementId: ...
    def GetIntegerValue(self, ) -> int: ...
    def GetStringValue(self, ) -> str: ...
    def SetNullValue(self, ) -> None: ...
    def SetValue(self, id: ElementId) -> None: ...

class ScheduleFilterType:
    """.NET: Autodesk.Revit.DB.ScheduleFilterType"""
    def __init__(self, *args) -> None: ...
    ...

class ScheduleHeadingOrientation:
    """.NET: Autodesk.Revit.DB.ScheduleHeadingOrientation"""
    def __init__(self, *args) -> None: ...
    ...

class ScheduleHeightsOnSheet:
    """.NET: Autodesk.Revit.DB.ScheduleHeightsOnSheet"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ColumnHeaderHeight: float
    TitleHeight: float
    def Dispose(self, ) -> None: ...
    def GetBodyRowHeights(self, ) -> IList: ...

class ScheduleHorizontalAlignment:
    """.NET: Autodesk.Revit.DB.ScheduleHorizontalAlignment"""
    def __init__(self, *args) -> None: ...
    ...

class ScheduleSheetInstance(Element):
    """.NET: Autodesk.Revit.DB.ScheduleSheetInstance"""
    def __init__(self, *args) -> None: ...
    IsTitleblockRevisionSchedule: bool
    SegmentIndex: int
    Rotation: ViewportRotation
    Point: XYZ
    ScheduleId: ElementId
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
    def Create(document: Document, viewSheetId: ElementId, scheduleId: ElementId, origin: XYZ, segmentIndex: int) -> ScheduleSheetInstance: ...

class ScheduleSortGroupField:
    """.NET: Autodesk.Revit.DB.ScheduleSortGroupField"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ShowFooterCount: bool
    ShowFooterTitle: bool
    ShowFooter: bool
    ShowBlankLine: bool
    ShowHeader: bool
    SortOrder: ScheduleSortOrder
    FieldId: ScheduleFieldId
    def Dispose(self, ) -> None: ...

class ScheduleSortOrder:
    """.NET: Autodesk.Revit.DB.ScheduleSortOrder"""
    def __init__(self, *args) -> None: ...
    ...

class ScheduleVerticalAlignment:
    """.NET: Autodesk.Revit.DB.ScheduleVerticalAlignment"""
    def __init__(self, *args) -> None: ...
    ...

class SectionType:
    """.NET: Autodesk.Revit.DB.SectionType"""
    def __init__(self, *args) -> None: ...
    ...

class Segment(Element):
    """.NET: Autodesk.Revit.DB.Segment"""
    def __init__(self, *args) -> None: ...
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
    def AddSize(self, size: MEPSize) -> None: ...
    def GetSizes(self, ) -> ICollection: ...
    def RemoveSize(self, nominalDiameter: float) -> None: ...

class SelectionFilterAction:
    """.NET: Autodesk.Revit.DB.SelectionFilterAction"""
    def __init__(self, *args) -> None: ...
    ...

class SelectionFilterElement(FilterElement):
    """.NET: Autodesk.Revit.DB.SelectionFilterElement"""
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
    def AddSet(self, ids: ICollection) -> None: ...
    def AddSingle(self, id: ElementId) -> None: ...
    def Clear(self, ) -> None: ...
    def Contains(self, id: ElementId) -> bool: ...
    @staticmethod
    def Create(document: Document, name: str) -> SelectionFilterElement: ...
    def GetElementIds(self, ) -> ICollection: ...
    def IsEmpty(self, ) -> bool: ...
    def RemoveSet(self, ids: ICollection) -> int: ...
    def RemoveSingle(self, id: ElementId) -> None: ...
    def SetElementIds(self, ids: ICollection) -> None: ...

class ServerPath(ModelPath):
    """.NET: Autodesk.Revit.DB.ServerPath"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Region: str
    CloudPath: bool
    ServerPath: bool
    Empty: bool
    CentralServerPath: str

class ServiceType:
    """.NET: Autodesk.Revit.DB.ServiceType"""
    def __init__(self, *args) -> None: ...
    ...

class SetComparisonResult:
    """.NET: Autodesk.Revit.DB.SetComparisonResult"""
    def __init__(self, *args) -> None: ...
    ...

class Settings(APIObject):
    """.NET: Autodesk.Revit.DB.Settings"""
    def __init__(self, *args) -> None: ...
    TilePatterns: TilePatterns
    ElectricalSetting: ElectricalSetting
    Categories: Categories
    IsReadOnly: bool

class ShapeBuilder:
    """.NET: Autodesk.Revit.DB.ShapeBuilder"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class ShapeImporter:
    """.NET: Autodesk.Revit.DB.ShapeImporter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    DefaultLengthUnit: ImportUnit
    InputFormat: ShapeImporterSourceFormat
    def Convert(self, document: Document, filename: str) -> IList: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def IsServiceAvailable() -> bool: ...
    def SetDefaultLengthUnit(self, defaultLengthUnit: ImportUnit) -> ShapeImporter: ...

class ShapeImporterSourceFormat:
    """.NET: Autodesk.Revit.DB.ShapeImporterSourceFormat"""
    def __init__(self, *args) -> None: ...
    ...

class SharedParameterApplicableRule(FilterRule):
    """.NET: Autodesk.Revit.DB.SharedParameterApplicableRule"""
    def __init__(self, *args) -> None: ...
    ParameterName: str
    IsValidObject: bool

class SharedParameterElement(ParameterElement):
    """.NET: Autodesk.Revit.DB.SharedParameterElement"""
    def __init__(self, *args) -> None: ...
    GuidValue: Guid
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
    def Create(document: Document, sharedParameterDefinition: ExternalDefinition) -> SharedParameterElement: ...
    @staticmethod
    def Lookup(document: Document, guidValue: Guid) -> SharedParameterElement: ...
    def ShouldHideWhenNoValue(self, ) -> bool: ...

class SheetCollection(Element):
    """.NET: Autodesk.Revit.DB.SheetCollection"""
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
    def Create(document: Document, name: str) -> SheetCollection: ...

class SheetDuplicateOption:
    """.NET: Autodesk.Revit.DB.SheetDuplicateOption"""
    def __init__(self, *args) -> None: ...
    ...

class ShellLayerType:
    """.NET: Autodesk.Revit.DB.ShellLayerType"""
    def __init__(self, *args) -> None: ...
    ...

class ShowHiddenLinesValues:
    """.NET: Autodesk.Revit.DB.ShowHiddenLinesValues"""
    def __init__(self, *args) -> None: ...
    ...

class SimpleWorksetConfiguration:
    """.NET: Autodesk.Revit.DB.SimpleWorksetConfiguration"""
    def __init__(self, *args) -> None: ...
    ...

class SiteLocation(ElementType):
    """.NET: Autodesk.Revit.DB.SiteLocation"""
    def __init__(self, *args) -> None: ...
    GeoCoordinateSystemDefinition: str
    GeoCoordinateSystemId: str
    Elevation: float
    WeatherStationName: str
    PlaceName: str
    TimeZone: float
    Longitude: float
    Latitude: float
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
    def ConvertFromProjectTime(self, projectTime: DateTime) -> DateTime: ...
    def ConvertToProjectTime(self, inputTime: DateTime) -> DateTime: ...
    def IsCompatibleWith(self, otherSiteLocation: SiteLocation) -> bool: ...
    def SetGeoCoordinateSystem(self, coordSystem: str) -> None: ...

class Sketch(SketchBase):
    """.NET: Autodesk.Revit.DB.Sketch"""
    def __init__(self, *args) -> None: ...
    OwnerId: ElementId
    SketchPlane: SketchPlane
    Profile: CurveArrArray
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
    def GetAllElements(self, ) -> IList: ...

class SketchBase(Element):
    """.NET: Autodesk.Revit.DB.SketchBase"""
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

class SketchEditScope(EditScope):
    """.NET: Autodesk.Revit.DB.SketchEditScope"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsPermitted: bool
    IsActive: bool
    def IsElementWithoutSketch(self, elementId: ElementId) -> bool: ...
    def IsSketchEditingSupported(self, sketchId: ElementId) -> bool: ...
    def IsSketchEditingSupportedForSketchBasedElement(self, elemId: ElementId) -> bool: ...
    def Start(self, sketchId: ElementId) -> None: ...
    def StartWithNewSketch(self, elementId: ElementId) -> None: ...

class SketchPlane(Element):
    """.NET: Autodesk.Revit.DB.SketchPlane"""
    def __init__(self, *args) -> None: ...
    IsSuitableForModelElements: bool
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
    def Create(document: Document, datumId: ElementId) -> SketchPlane: ...
    def GetPlane(self, ) -> Plane: ...
    def GetPlaneReference(self, ) -> Reference: ...

class SketchedStairsCurveData:
    """.NET: Autodesk.Revit.DB.SketchedStairsCurveData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetCurve(self, ) -> Curve: ...

class SkyBackgroundSettings(BackgroundSettings):
    """.NET: Autodesk.Revit.DB.SkyBackgroundSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class SlabEdge(HostedSweep):
    """.NET: Autodesk.Revit.DB.SlabEdge"""
    def __init__(self, *args) -> None: ...
    SlabEdgeType: SlabEdgeType
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

class SlabEdgeType(HostedSweepType):
    """.NET: Autodesk.Revit.DB.SlabEdgeType"""
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

class SlabShapeCrease:
    """.NET: Autodesk.Revit.DB.SlabShapeCrease"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    CreaseType: SlabShapeCreaseType
    EndPoints: SlabShapeVertexArray
    Curve: Curve
    def Dispose(self, ) -> None: ...

class SlabShapeCreaseArray(APIObject):
    """.NET: Autodesk.Revit.DB.SlabShapeCreaseArray"""
    def __init__(self, *args) -> None: ...
    Item: SlabShapeCrease
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: SlabShapeCrease) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> SlabShapeCreaseArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: SlabShapeCrease, index: int) -> None: ...
    def ReverseIterator(self, ) -> SlabShapeCreaseArrayIterator: ...

class SlabShapeCreaseArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.SlabShapeCreaseArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class SlabShapeCreaseType:
    """.NET: Autodesk.Revit.DB.SlabShapeCreaseType"""
    def __init__(self, *args) -> None: ...
    ...

class SlabShapeEditor:
    """.NET: Autodesk.Revit.DB.SlabShapeEditor"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    SlabShapeCreases: SlabShapeCreaseArray
    SlabShapeVertices: SlabShapeVertexArray
    IsEnabled: bool
    def AddPoint(self, point: XYZ) -> SlabShapeVertex: ...
    def AddPoints(self, points: IList) -> IList: ...
    def AddSplitLine(self, startVertex: SlabShapeVertex, endVertex: SlabShapeVertex) -> IList: ...
    def CreateCreasesFromFoldingLines(self, hostObj: Element, references: IList) -> None: ...
    def DeletePoint(self, vertex: SlabShapeVertex) -> bool: ...
    def Dispose(self, ) -> None: ...
    def Enable(self, ) -> None: ...
    def ModifySubElement(self, crease: SlabShapeCrease, offset: float) -> None: ...
    def PickSupport(self, gLine: Line) -> None: ...
    def ResetSlabShape(self, ) -> None: ...

class SlabShapeVertex:
    """.NET: Autodesk.Revit.DB.SlabShapeVertex"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Position: XYZ
    VertexType: SlabShapeVertexType
    def Dispose(self, ) -> None: ...

class SlabShapeVertexArray(APIObject):
    """.NET: Autodesk.Revit.DB.SlabShapeVertexArray"""
    def __init__(self, *args) -> None: ...
    Item: SlabShapeVertex
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: SlabShapeVertex) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> SlabShapeVertexArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: SlabShapeVertex, index: int) -> None: ...
    def ReverseIterator(self, ) -> SlabShapeVertexArrayIterator: ...

class SlabShapeVertexArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.SlabShapeVertexArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class SlabShapeVertexType:
    """.NET: Autodesk.Revit.DB.SlabShapeVertexType"""
    def __init__(self, *args) -> None: ...
    ...

class SlantedOrVerticalColumnType:
    """.NET: Autodesk.Revit.DB.SlantedOrVerticalColumnType"""
    def __init__(self, *args) -> None: ...
    ...

class Solid(GeometryObject):
    """.NET: Autodesk.Revit.DB.Solid"""
    def __init__(self, *args) -> None: ...
    Volume: float
    SurfaceArea: float
    Faces: FaceArray
    Edges: EdgeArray
    Id: int
    IsElementGeometry: bool
    GraphicsStyleId: ElementId
    Visibility: Visibility
    IsReadOnly: bool
    def ComputeCentroid(self, ) -> XYZ: ...
    def GetBoundingBox(self, ) -> BoundingBoxXYZ: ...
    def IntersectWithCurve(self, curve: Curve, options: SolidCurveIntersectionOptions) -> SolidCurveIntersection: ...

class SolidCurveIntersection:
    """.NET: Autodesk.Revit.DB.SolidCurveIntersection"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    SegmentCount: int
    ResultType: SolidCurveIntersectionMode
    def Dispose(self, ) -> None: ...
    def GetCurveSegment(self, index: int) -> Curve: ...
    def GetCurveSegmentExtents(self, index: int) -> CurveExtents: ...
    def GetEnumerator(self, ) -> IEnumerator: ...

class SolidCurveIntersectionMode:
    """.NET: Autodesk.Revit.DB.SolidCurveIntersectionMode"""
    def __init__(self, *args) -> None: ...
    ...

class SolidCurveIntersectionOptions:
    """.NET: Autodesk.Revit.DB.SolidCurveIntersectionOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ResultType: SolidCurveIntersectionMode
    def Dispose(self, ) -> None: ...

class SolidGeometry:
    """.NET: Autodesk.Revit.DB.SolidGeometry"""
    def __init__(self, *args) -> None: ...
    ...

class SolidGeometryOptions:
    """.NET: Autodesk.Revit.DB.SolidGeometryOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    SolidTag: int
    def Dispose(self, ) -> None: ...

class SolidOptions:
    """.NET: Autodesk.Revit.DB.SolidOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ExtraFaceAndEdgeHistoryKey: int
    GraphicsStyleId: ElementId
    MaterialId: ElementId
    def Dispose(self, ) -> None: ...

class SolidOrShellTessellationControls:
    """.NET: Autodesk.Revit.DB.SolidOrShellTessellationControls"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LevelOfDetail: float
    MinAngleInTriangle: float
    MinExternalAngleBetweenTriangles: float
    Accuracy: float
    def DisableLevelOfDetail(self, ) -> None: ...
    def Dispose(self, ) -> None: ...
    def UseLevelOfDetail(self, ) -> bool: ...

class SolidSolidCutUtils:
    """.NET: Autodesk.Revit.DB.SolidSolidCutUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def AddCutBetweenSolids(document: Document, solidToBeCut: Element, cuttingSolid: Element, splitFacesOfCuttingSolid: bool) -> None: ...
    @staticmethod
    def CanElementCutElement(cuttingElement: Element, cutElement: Element, reason: CutFailureReason) -> bool: ...
    @staticmethod
    def CutExistsBetweenElements(first: Element, second: Element, firstCutsSecond: bool) -> bool: ...
    @staticmethod
    def GetCuttingSolids(element: Element) -> ICollection: ...
    @staticmethod
    def GetSolidsBeingCut(element: Element) -> ICollection: ...
    @staticmethod
    def IsAllowedForSolidCut(element: Element) -> bool: ...
    @staticmethod
    def IsElementFromAppropriateContext(element: Element) -> bool: ...
    @staticmethod
    def RemoveCutBetweenSolids(document: Document, first: Element, second: Element) -> None: ...
    @staticmethod
    def SplitFacesOfCuttingSolid(first: Element, second: Element, split: bool) -> None: ...

class SolidUtils:
    """.NET: Autodesk.Revit.DB.SolidUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def Clone(solid: Solid) -> Solid: ...
    @staticmethod
    def ComputeIsGeometricallyClosed(geometry: Solid) -> bool: ...
    @staticmethod
    def ComputeIsTopologicallyClosed(geometry: Solid) -> bool: ...
    @staticmethod
    def CreateTransformed(solid: Solid, transform: Transform) -> Solid: ...
    @staticmethod
    def FindAllEdgeEndPointsAtVertex(edgeEndPoint: EdgeEndPoint) -> IList: ...
    @staticmethod
    def IsValidForTessellation(solidOrShell: Solid) -> bool: ...
    @staticmethod
    def SplitVolumes(solid: Solid) -> IList: ...
    @staticmethod
    def TessellateSolidOrShell(solidOrShell: Solid, tessellationControls: SolidOrShellTessellationControls) -> TriangulatedSolidOrShell: ...

class SortingOrder:
    """.NET: Autodesk.Revit.DB.SortingOrder"""
    def __init__(self, *args) -> None: ...
    ...

class SpacingRule(APIObject):
    """.NET: Autodesk.Revit.DB.SpacingRule"""
    def __init__(self, *args) -> None: ...
    BeltMeasurement: float
    HasBeltMeasurement: bool
    Offset: float
    GridlinesRotation: float
    Justification: SpacingRuleJustification
    Number: int
    Distance: float
    Layout: SpacingRuleLayout
    IsReadOnly: bool
    def SetLayoutFixedDistance(self, distance: float, just: SpacingRuleJustification, gridlinesRotation: float, offset: float) -> None: ...
    def SetLayoutFixedNumber(self, number: int, just: SpacingRuleJustification, gridlinesRotation: float, offset: float) -> None: ...
    def SetLayoutMaximumSpacing(self, distance: float, just: SpacingRuleJustification, gridlinesRotation: float, offset: float) -> None: ...
    def SetLayoutMinimumSpacing(self, distance: float, just: SpacingRuleJustification, gridlinesRotation: float, offset: float) -> None: ...
    def SetLayoutNone(self, ) -> None: ...

class SpacingRuleJustification:
    """.NET: Autodesk.Revit.DB.SpacingRuleJustification"""
    def __init__(self, *args) -> None: ...
    ...

class SpacingRuleLayout:
    """.NET: Autodesk.Revit.DB.SpacingRuleLayout"""
    def __init__(self, *args) -> None: ...
    ...

class SpanDirectionSymbol(IndependentTag):
    """.NET: Autodesk.Revit.DB.SpanDirectionSymbol"""
    def __init__(self, *args) -> None: ...
    MergeElbows: bool
    LeadersPresentationMode: LeadersPresentationMode
    RotationAngle: float
    MultiLeader: bool
    LeaderStartCondition: LeaderStartCondition
    LeaderEndCondition: LeaderEndCondition
    HasLeader: bool
    TagHeadPosition: XYZ
    TagOrientation: TagOrientation
    IsOrphaned: bool
    IsMulticategoryTag: bool
    IsMaterialTag: bool
    TagText: str
    MultiReferenceAnnotationId: ElementId
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
    def Create(document: Document, viewId: ElementId, elemIdToTag: LinkElementId, headPosistion: XYZ, symbolId: ElementId) -> SpanDirectionSymbol: ...
    @staticmethod
    def GetDefaultPlacementPoint(document: Document, elemIdToTag: LinkElementId) -> XYZ: ...

class SpatialElement(Element):
    """.NET: Autodesk.Revit.DB.SpatialElement"""
    def __init__(self, *args) -> None: ...
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
    def GetBoundarySegments(self, options: SpatialElementBoundaryOptions) -> IList: ...
    def GetDefaultLocation(self, ) -> XYZ: ...
    def GetSpatialElementDomainData(self, ) -> SpatialElementDomainData: ...
    def Recenter(self, ) -> None: ...

class SpatialElementBoundaryLocation:
    """.NET: Autodesk.Revit.DB.SpatialElementBoundaryLocation"""
    def __init__(self, *args) -> None: ...
    ...

class SpatialElementBoundaryOptions:
    """.NET: Autodesk.Revit.DB.SpatialElementBoundaryOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    SpatialElementBoundaryLocation: SpatialElementBoundaryLocation
    StoreFreeBoundaryFaces: bool
    def Dispose(self, ) -> None: ...

class SpatialElementBoundarySubface:
    """.NET: Autodesk.Revit.DB.SpatialElementBoundarySubface"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Valid: bool
    SubfaceType: SubfaceType
    SubfaceArisesFromElementFace: bool
    SpatialBoundaryElement: LinkElementId
    def Dispose(self, ) -> None: ...
    def GetBoundingElementFace(self, ) -> Face: ...
    def GetSpatialElementFace(self, ) -> Face: ...
    def GetSubface(self, ) -> Face: ...

class SpatialElementCalculationLocation(Element):
    """.NET: Autodesk.Revit.DB.SpatialElementCalculationLocation"""
    def __init__(self, *args) -> None: ...
    MarkerPosition: XYZ
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

class SpatialElementCalculationPoint(SpatialElementCalculationLocation):
    """.NET: Autodesk.Revit.DB.SpatialElementCalculationPoint"""
    def __init__(self, *args) -> None: ...
    Position: XYZ
    MarkerPosition: XYZ
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

class SpatialElementDomainData:
    """.NET: Autodesk.Revit.DB.SpatialElementDomainData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class SpatialElementFromToCalculationPoints(SpatialElementCalculationLocation):
    """.NET: Autodesk.Revit.DB.SpatialElementFromToCalculationPoints"""
    def __init__(self, *args) -> None: ...
    ToPosition: XYZ
    FromPosition: XYZ
    MarkerPosition: XYZ
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
    def Flip(self, ) -> None: ...
    def IsAcceptableFromPosition(self, fromPosition: XYZ) -> bool: ...
    def IsAcceptableToPosition(self, toPosition: XYZ) -> bool: ...
    def MakeFromPositionAcceptable(self, newFromLocation: XYZ) -> XYZ: ...
    def MakeToPositionAcceptable(self, newToLocation: XYZ) -> XYZ: ...

class SpatialElementGeometryCalculator:
    """.NET: Autodesk.Revit.DB.SpatialElementGeometryCalculator"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def CalculateSpatialElementGeometry(self, spatialElement: SpatialElement) -> SpatialElementGeometryResults: ...
    @staticmethod
    def CanCalculateGeometry(spatialElement: SpatialElement) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetOptions(self, ) -> SpatialElementBoundaryOptions: ...
    @staticmethod
    def IsRoomOrSpace(spatialElement: SpatialElement) -> bool: ...

class SpatialElementGeometryResults:
    """.NET: Autodesk.Revit.DB.SpatialElementGeometryResults"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetBoundaryFaceInfo(self, face: Face) -> IList: ...
    def GetGeometry(self, ) -> Solid: ...

class SpatialElementTag(Element):
    """.NET: Autodesk.Revit.DB.SpatialElementTag"""
    def __init__(self, *args) -> None: ...
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
    def MoveToReferenceLocation(self, ) -> None: ...

class SpatialElementTagOrientation:
    """.NET: Autodesk.Revit.DB.SpatialElementTagOrientation"""
    def __init__(self, *args) -> None: ...
    ...

class SpatialElementType:
    """.NET: Autodesk.Revit.DB.SpatialElementType"""
    def __init__(self, *args) -> None: ...
    ...

class SpecTypeId:
    """.NET: Autodesk.Revit.DB.SpecTypeId"""
    def __init__(self, *args) -> None: ...
    MassEquivalentPerItem: ForgeTypeId
    MassEquivalentPerUnitMass: ForgeTypeId
    MassEquivalentPerUnitEnergy: ForgeTypeId
    MassEquivalentPerUnitVolume: ForgeTypeId
    MassEquivalentPerUnitArea: ForgeTypeId
    MassEquivalentPerUnitLength: ForgeTypeId
    WireDiameter: ForgeTypeId
    WeightPerUnitLength: ForgeTypeId
    Weight: ForgeTypeId
    Wattage: ForgeTypeId
    WarpingConstant: ForgeTypeId
    Volume: ForgeTypeId
    UnitWeight: ForgeTypeId
    Time: ForgeTypeId
    ThermalResistance: ForgeTypeId
    ThermalMass: ForgeTypeId
    ThermalGradientCoefficientForMoistureCapacity: ForgeTypeId
    ThermalExpansionCoefficient: ForgeTypeId
    ThermalConductivity: ForgeTypeId
    SurfaceAreaPerUnitLength: ForgeTypeId
    StructuralVelocity: ForgeTypeId
    StructuralFrequency: ForgeTypeId
    Stress: ForgeTypeId
    StationingInterval: ForgeTypeId
    Stationing: ForgeTypeId
    Speed: ForgeTypeId
    SpecificHeatOfVaporization: ForgeTypeId
    SpecificHeat: ForgeTypeId
    Slope: ForgeTypeId
    SiteAngle: ForgeTypeId
    SheetLength: ForgeTypeId
    SectionProperty: ForgeTypeId
    SectionModulus: ForgeTypeId
    SectionDimension: ForgeTypeId
    SectionArea: ForgeTypeId
    RotationalPointSpringCoefficient: ForgeTypeId
    RotationalLineSpringCoefficient: ForgeTypeId
    RotationAngle: ForgeTypeId
    Rotation: ForgeTypeId
    ReinforcementVolume: ForgeTypeId
    ReinforcementSpacing: ForgeTypeId
    ReinforcementLength: ForgeTypeId
    ReinforcementCover: ForgeTypeId
    ReinforcementAreaPerUnitLength: ForgeTypeId
    ReinforcementArea: ForgeTypeId
    Pulsation: ForgeTypeId
    PowerPerLength: ForgeTypeId
    PowerPerFlow: ForgeTypeId
    PointSpringCoefficient: ForgeTypeId
    PipingVolume: ForgeTypeId
    PipingViscosity: ForgeTypeId
    PipingVelocity: ForgeTypeId
    PipingTemperatureDifference: ForgeTypeId
    PipingTemperature: ForgeTypeId
    PipingSlope: ForgeTypeId
    PipingRoughness: ForgeTypeId
    PipingPressure: ForgeTypeId
    PipingMassPerTime: ForgeTypeId
    PipingMass: ForgeTypeId
    PipingFriction: ForgeTypeId
    PipingDensity: ForgeTypeId
    PipeSize: ForgeTypeId
    PipeMassPerUnitLength: ForgeTypeId
    PipeInsulationThickness: ForgeTypeId
    PipeDimension: ForgeTypeId
    Permeability: ForgeTypeId
    Period: ForgeTypeId
    Number: ForgeTypeId
    MomentScale: ForgeTypeId
    MomentOfInertia: ForgeTypeId
    Moment: ForgeTypeId
    MassPerUnitLength: ForgeTypeId
    MassPerUnitArea: ForgeTypeId
    MassDensity: ForgeTypeId
    Mass: ForgeTypeId
    LuminousIntensity: ForgeTypeId
    LuminousFlux: ForgeTypeId
    Luminance: ForgeTypeId
    LinearMomentScale: ForgeTypeId
    LinearMoment: ForgeTypeId
    LinearForceScale: ForgeTypeId
    LinearForce: ForgeTypeId
    LineSpringCoefficient: ForgeTypeId
    Length: ForgeTypeId
    IsothermalMoistureCapacity: ForgeTypeId
    Illuminance: ForgeTypeId
    HvacViscosity: ForgeTypeId
    HvacVelocity: ForgeTypeId
    HvacTemperatureDifference: ForgeTypeId
    HvacTemperature: ForgeTypeId
    HvacSlope: ForgeTypeId
    HvacRoughness: ForgeTypeId
    HvacPressure: ForgeTypeId
    HvacPowerDensity: ForgeTypeId
    HvacPower: ForgeTypeId
    HvacMassPerTime: ForgeTypeId
    HvacFriction: ForgeTypeId
    HvacEnergy: ForgeTypeId
    HvacDensity: ForgeTypeId
    HeatingLoadDividedByVolume: ForgeTypeId
    HeatingLoadDividedByArea: ForgeTypeId
    HeatingLoad: ForgeTypeId
    HeatTransferCoefficient: ForgeTypeId
    HeatGain: ForgeTypeId
    HeatCapacityPerArea: ForgeTypeId
    ForceScale: ForgeTypeId
    Force: ForgeTypeId
    FlowPerPower: ForgeTypeId
    Flow: ForgeTypeId
    Factor: ForgeTypeId
    Energy: ForgeTypeId
    ElectricalTemperatureDifference: ForgeTypeId
    ElectricalTemperature: ForgeTypeId
    ElectricalResistivity: ForgeTypeId
    ElectricalPowerDensity: ForgeTypeId
    ElectricalPower: ForgeTypeId
    ElectricalPotential: ForgeTypeId
    ElectricalFrequency: ForgeTypeId
    Efficacy: ForgeTypeId
    DuctSize: ForgeTypeId
    DuctLiningThickness: ForgeTypeId
    DuctInsulationThickness: ForgeTypeId
    Distance: ForgeTypeId
    Displacement: ForgeTypeId
    Diffusivity: ForgeTypeId
    DemandFactor: ForgeTypeId
    DecimalSheetLength: ForgeTypeId
    Current: ForgeTypeId
    Currency: ForgeTypeId
    CrossSection: ForgeTypeId
    CrackWidth: ForgeTypeId
    CostRatePower: ForgeTypeId
    CostRateEnergy: ForgeTypeId
    CostPerArea: ForgeTypeId
    CoolingLoadDividedByVolume: ForgeTypeId
    CoolingLoadDividedByArea: ForgeTypeId
    CoolingLoad: ForgeTypeId
    ConduitSize: ForgeTypeId
    ColorTemperature: ForgeTypeId
    CableTraySize: ForgeTypeId
    BarDiameter: ForgeTypeId
    AreaSpringCoefficient: ForgeTypeId
    AreaForceScale: ForgeTypeId
    AreaForce: ForgeTypeId
    AreaDividedByHeatingLoad: ForgeTypeId
    AreaDividedByCoolingLoad: ForgeTypeId
    Area: ForgeTypeId
    ApparentPowerDensity: ForgeTypeId
    ApparentPower: ForgeTypeId
    AngularSpeed: ForgeTypeId
    Angle: ForgeTypeId
    AirFlowDividedByVolume: ForgeTypeId
    AirFlowDividedByCoolingLoad: ForgeTypeId
    AirFlowDensity: ForgeTypeId
    AirFlow: ForgeTypeId
    Acceleration: ForgeTypeId
    Custom: ForgeTypeId

class SpecUtils:
    """.NET: Autodesk.Revit.DB.SpecUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetAllSpecs() -> IList: ...
    @staticmethod
    def IsSpec(specTypeId: ForgeTypeId) -> bool: ...
    @staticmethod
    def IsValidDataType(dataType: ForgeTypeId) -> bool: ...

class SpecialType:
    """.NET: Autodesk.Revit.DB.SpecialType"""
    def __init__(self, *args) -> None: ...
    ...

class SpotDimension(Dimension):
    """.NET: Autodesk.Revit.DB.SpotDimension"""
    def __init__(self, *args) -> None: ...
    LeaderShoulderPosition: XYZ
    LeaderHasShoulder: bool
    SpotDimensionType: SpotDimensionType
    IsValid: bool
    AreReferencesAvailable: bool
    TextPosition: XYZ
    Origin: XYZ
    LeaderEndPosition: XYZ
    HasLeader: bool
    ValueOverride: str
    Below: str
    Above: str
    Suffix: str
    Prefix: str
    IsLocked: bool
    ValueString: str
    Value: Nullable
    AreSegmentsEqual: bool
    Segments: DimensionSegmentArray
    NumberOfSegments: int
    DimensionShape: DimensionShape
    FamilyLabel: FamilyParameter
    Name: str
    DimensionType: DimensionType
    View: View
    Curve: Curve
    References: ReferenceArray
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
    def CanFlip(self, ) -> bool: ...
    def Flip(self, ) -> None: ...

class SpotDimensionType(DimensionType):
    """.NET: Autodesk.Revit.DB.SpotDimensionType"""
    def __init__(self, *args) -> None: ...
    Suffix: str
    Prefix: str
    AlternateUnitsSuffix: str
    AlternateUnitsPrefix: str
    AlternateUnits: AlternateUnits
    StyleType: DimensionStyleType
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

class StairsEditScope(EditScope):
    """.NET: Autodesk.Revit.DB.StairsEditScope"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsPermitted: bool
    IsActive: bool
    def Start(self, baseLevelId: ElementId, topLevelId: ElementId) -> ElementId: ...

class StartingViewSettings(Element):
    """.NET: Autodesk.Revit.DB.StartingViewSettings"""
    def __init__(self, *args) -> None: ...
    ViewId: ElementId
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
    def GetStartingViewSettings(doc: Document) -> StartingViewSettings: ...
    def IsAcceptableStartingView(self, viewId: ElementId) -> bool: ...

class StdPostedWarning:
    """.NET: Autodesk.Revit.DB.StdPostedWarning"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class StickSymbolLocation:
    """.NET: Autodesk.Revit.DB.StickSymbolLocation"""
    def __init__(self, *args) -> None: ...
    ...

class StiffenerClassification:
    """.NET: Autodesk.Revit.DB.StiffenerClassification"""
    def __init__(self, *args) -> None: ...
    ...

class StorageType:
    """.NET: Autodesk.Revit.DB.StorageType"""
    def __init__(self, *args) -> None: ...
    ...

class StringParameterValue(ParameterValue):
    """.NET: Autodesk.Revit.DB.StringParameterValue"""
    def __init__(self, *args) -> None: ...
    Value: str
    IsValidObject: bool

class StripedRowPattern:
    """.NET: Autodesk.Revit.DB.StripedRowPattern"""
    def __init__(self, *args) -> None: ...
    ...

class StructDeckEmbeddingType:
    """.NET: Autodesk.Revit.DB.StructDeckEmbeddingType"""
    def __init__(self, *args) -> None: ...
    ...

class StructuralAsset:
    """.NET: Autodesk.Revit.DB.StructuralAsset"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Name: str
    Density: float
    SubClass: str
    WoodGrade: str
    WoodSpecies: str
    WoodPerpendicularShearStrength: float
    WoodParallelShearStrength: float
    WoodPerpendicularCompressionStrength: float
    WoodParallelCompressionStrength: float
    WoodBendingStrength: float
    MetalResistanceCalculationStrength: float
    MetalReductionFactor: float
    MetalThermallyTreated: bool
    MinimumTensileStrength: float
    MinimumYieldStress: float
    ConcreteShearStrengthReduction: float
    ConcreteShearReinforcement: float
    ConcreteBendingReinforcement: float
    ConcreteCompression: float
    Behavior: StructuralBehavior
    Lightweight: bool
    ThermalExpansionCoefficient: XYZ
    ShearModulus: XYZ
    PoissonRatio: XYZ
    YoungModulus: XYZ
    StructuralAssetClass: StructuralAssetClass
    def Copy(self, ) -> StructuralAsset: ...
    def Dispose(self, ) -> None: ...
    def Equals(self, other: StructuralAsset) -> bool: ...
    def SetPoissonRatio(self, poissonRatio: float) -> None: ...
    def SetShearModulus(self, shearModulus: float) -> None: ...
    def SetThermalExpansionCoefficient(self, thermalExpCoeff: float) -> None: ...
    def SetYoungModulus(self, youngModulus: float) -> None: ...

class StructuralAssetClass:
    """.NET: Autodesk.Revit.DB.StructuralAssetClass"""
    def __init__(self, *args) -> None: ...
    ...

class StructuralBehavior:
    """.NET: Autodesk.Revit.DB.StructuralBehavior"""
    def __init__(self, *args) -> None: ...
    ...

class StructuralReleaseType:
    """.NET: Autodesk.Revit.DB.StructuralReleaseType"""
    def __init__(self, *args) -> None: ...
    ...

class SubTransaction:
    """.NET: Autodesk.Revit.DB.SubTransaction"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Commit(self, ) -> TransactionStatus: ...
    def Dispose(self, ) -> None: ...
    def GetStatus(self, ) -> TransactionStatus: ...
    def HasEnded(self, ) -> bool: ...
    def HasStarted(self, ) -> bool: ...
    def RollBack(self, ) -> TransactionStatus: ...
    def Start(self, ) -> TransactionStatus: ...

class Subelement:
    """.NET: Autodesk.Revit.DB.Subelement"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    UniqueId: str
    Element: Element
    Document: Document
    TypeId: ElementId
    Category: Category
    def CanHaveTypeAssigned(self, ) -> bool: ...
    def ChangeTypeId(self, typeId: ElementId) -> None: ...
    @staticmethod
    def Create(aDoc: Document, reference: Reference) -> Subelement: ...
    def Dispose(self, ) -> None: ...
    def GetAllParameters(self, ) -> IList: ...
    def GetBoundingBox(self, dbView: View) -> BoundingBoxXYZ: ...
    def GetGeometryObject(self, dbView: View) -> GeometryObject: ...
    def GetParameterValue(self, parameterId: ElementId) -> ParameterValue: ...
    def GetReference(self, ) -> Reference: ...
    def GetValidTypes(self, ) -> ISet: ...
    def HasParameter(self, parameterId: ElementId) -> bool: ...
    def IsParameterModifiable(self, parameterId: ElementId) -> bool: ...
    @staticmethod
    def IsValidSubelementReference(aDoc: Document, reference: Reference) -> bool: ...
    def IsValidType(self, typeId: ElementId) -> bool: ...
    def SetParameterValue(self, parameterId: ElementId, pValue: ParameterValue) -> None: ...

class SubfaceType:
    """.NET: Autodesk.Revit.DB.SubfaceType"""
    def __init__(self, *args) -> None: ...
    ...

class SunAndShadowSettings(Element):
    """.NET: Autodesk.Revit.DB.SunAndShadowSettings"""
    def __init__(self, *args) -> None: ...
    SharesSettings: bool
    ProjectLocationId: ElementId
    ProjectLocationName: str
    UsesDST: bool
    TimeZone: float
    Longitude: float
    Latitude: float
    GroundPlaneHeight: float
    TimeInterval: SunStudyTimeInterval
    RelativeToView: bool
    UsesGroundPlane: bool
    SunriseToSunset: bool
    GroundPlaneLevelId: ElementId
    NumberOfFrames: float
    ActiveFrame: float
    EndDateAndTime: DateTime
    StartDateAndTime: DateTime
    ActiveFrameTime: DateTime
    SunAndShadowType: SunAndShadowType
    Altitude: float
    Azimuth: float
    Visible: bool
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
    def CalculateTimeZone(latitude: float, longitude: float) -> float: ...
    def FitToModel(self, ) -> None: ...
    @staticmethod
    def GetActiveSunAndShadowSettings(aDocument: Document) -> Element: ...
    def GetFrameAltitude(self, frame: float) -> float: ...
    def GetFrameAzimuth(self, frame: float) -> float: ...
    def GetFrameTime(self, frame: float) -> DateTime: ...
    def GetMatchingPreset(self, ) -> str: ...
    def GetSunrise(self, date: DateTime) -> DateTime: ...
    def GetSunset(self, date: DateTime) -> DateTime: ...
    def IsAfterStartDateAndTime(self, time: DateTime) -> bool: ...
    def IsBeforeEndDateAndTime(self, time: DateTime) -> bool: ...
    def IsFrameValid(self, frame: float) -> bool: ...
    def IsGroundPlaneLevelValid(self, levelId: ElementId) -> bool: ...
    def IsTimeIntervalValid(self, interval: SunStudyTimeInterval) -> bool: ...

class SunAndShadowType:
    """.NET: Autodesk.Revit.DB.SunAndShadowType"""
    def __init__(self, *args) -> None: ...
    ...

class SunStudyTimeInterval:
    """.NET: Autodesk.Revit.DB.SunStudyTimeInterval"""
    def __init__(self, *args) -> None: ...
    ...

class Surface:
    """.NET: Autodesk.Revit.DB.Surface"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    OrientationMatchesParametricOrientation: bool
    def Dispose(self, ) -> None: ...
    def GetBoundingBoxUV(self, ) -> BoundingBoxUV: ...
    def IsCoincidentWith(self, other: Surface) -> bool: ...
    def Project(self, point: XYZ, uv: UV, distance: float) -> None: ...
    def ProjectWithGuessPoint(self, point: XYZ, guessUV: UV, uv: UV, distance: float) -> None: ...

class Sweep(GenericForm):
    """.NET: Autodesk.Revit.DB.Sweep"""
    def __init__(self, *args) -> None: ...
    MaxSegmentAngle: float
    IsTrajectorySegmentationEnabled: bool
    Path3d: Path3d
    PathSketch: Sketch
    ProfileSymbol: FamilySymbolProfile
    ProfileSketch: Sketch
    Subcategory: Category
    Name: str
    IsSolid: bool
    Visible: bool
    Combinations: GeomCombinationSet
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

class SweepProfile(APIObject):
    """.NET: Autodesk.Revit.DB.SweepProfile"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool

class SweptBlend(GenericForm):
    """.NET: Autodesk.Revit.DB.SweptBlend"""
    def __init__(self, *args) -> None: ...
    TopProfile: CurveArrArray
    BottomProfile: CurveArrArray
    SelectedPath: Curve
    PathSketch: Sketch
    BottomProfileSymbol: FamilySymbolProfile
    BottomSketch: Sketch
    TopProfileSymbol: FamilySymbolProfile
    TopSketch: Sketch
    Subcategory: Category
    Name: str
    IsSolid: bool
    Visible: bool
    Combinations: GeomCombinationSet
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
    def GetVertexConnectionMap(self, ) -> VertexIndexPairArray: ...
    def SetVertexConnectionMap(self, vertexMap: VertexIndexPairArray) -> None: ...

class SweptProfile:
    """.NET: Autodesk.Revit.DB.SweptProfile"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    EndSetBack: float
    StartSetBack: float
    def Dispose(self, ) -> None: ...
    def GetDrivingCurve(self, ) -> Curve: ...
    def GetSweptProfile(self, ) -> Profile: ...

class SymbolGeometryId:
    """.NET: Autodesk.Revit.DB.SymbolGeometryId"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    SymbolId: ElementId
    def AsUniqueIdentifier(self, ) -> str: ...
    def Dispose(self, ) -> None: ...

class SymbolTypeId:
    """.NET: Autodesk.Revit.DB.SymbolTypeId"""
    def __init__(self, *args) -> None: ...
    TCO2ePerItem: ForgeTypeId
    TCO2ePerLb: ForgeTypeId
    TCO2ePerKg: ForgeTypeId
    TCO2ePerFt: ForgeTypeId
    TCO2ePerM: ForgeTypeId
    TCO2ePerFtSup2: ForgeTypeId
    TCO2ePerMSup2: ForgeTypeId
    TCO2ePerFtSup3: ForgeTypeId
    TCO2ePerMSup3: ForgeTypeId
    TCO2ePerMBtu: ForgeTypeId
    TCO2ePerKBtu: ForgeTypeId
    TCO2ePerBtu: ForgeTypeId
    TCO2ePerMWh: ForgeTypeId
    TCO2ePerKWh: ForgeTypeId
    KgCO2ePerItem: ForgeTypeId
    KgCO2ePerLb: ForgeTypeId
    KgCO2ePerKg: ForgeTypeId
    KgCO2ePerFt: ForgeTypeId
    KgCO2ePerM: ForgeTypeId
    KgCO2ePerFtSup2: ForgeTypeId
    KgCO2ePerMSup2: ForgeTypeId
    KgCO2ePerFtSup3: ForgeTypeId
    KgCO2ePerMSup3: ForgeTypeId
    KgCO2ePerMBtu: ForgeTypeId
    KgCO2ePerKBtu: ForgeTypeId
    KgCO2ePerBtu: ForgeTypeId
    KgCO2ePerMWh: ForgeTypeId
    KgCO2ePerKWh: ForgeTypeId
    Yen: ForgeTypeId
    YdSup3: ForgeTypeId
    YdCaret3: ForgeTypeId
    Won: ForgeTypeId
    Watt: ForgeTypeId
    WSPerMSup3: ForgeTypeId
    WPerMSup3: ForgeTypeId
    WPerMSup2K: ForgeTypeId
    WPerMSup2: ForgeTypeId
    WPerMK: ForgeTypeId
    WPerM: ForgeTypeId
    WPerFtSup3: ForgeTypeId
    WPerFtSup2: ForgeTypeId
    WPerFt: ForgeTypeId
    WMinPerFtSup3: ForgeTypeId
    Volt: ForgeTypeId
    VAPerMSup2: ForgeTypeId
    VAPerFtSup2: ForgeTypeId
    VA: ForgeTypeId
    Usgpm: ForgeTypeId
    Usgph: ForgeTypeId
    Usft: ForgeTypeId
    UsTonnesMassTons: ForgeTypeId
    UsTonnesMassT: ForgeTypeId
    UsTonnesMassSt: ForgeTypeId
    UsTonnesForceTons: ForgeTypeId
    UsTonnesForceT: ForgeTypeId
    UsTonnesForceSt: ForgeTypeId
    UsDollar: ForgeTypeId
    UmPerMDegreeC: ForgeTypeId
    UkPound: ForgeTypeId
    UinPerInDegreeF: ForgeTypeId
    Tonsf: ForgeTypeId
    Tonne: ForgeTypeId
    TonOfRefrigeration: ForgeTypeId
    Ton: ForgeTypeId
    Therm: ForgeTypeId
    TfPerMSup2: ForgeTypeId
    TfPerM: ForgeTypeId
    TfDashMPerM: ForgeTypeId
    TfDashM: ForgeTypeId
    Tf: ForgeTypeId
    Stf: ForgeTypeId
    Shekel: ForgeTypeId
    Shaku: ForgeTypeId
    SfPerTon: ForgeTypeId
    SfPerMbh: ForgeTypeId
    SfHPerKbtu: ForgeTypeId
    Sf: ForgeTypeId
    Second: ForgeTypeId
    Rps: ForgeTypeId
    Rpm: ForgeTypeId
    RadPerS: ForgeTypeId
    Rad: ForgeTypeId
    Psig: ForgeTypeId
    Psia: ForgeTypeId
    Psi: ForgeTypeId
    Psf: ForgeTypeId
    Pi: ForgeTypeId
    Percent: ForgeTypeId
    PerMille: ForgeTypeId
    PaPerM: ForgeTypeId
    PaDashS: ForgeTypeId
    Pa: ForgeTypeId
    OneColon: ForgeTypeId
    OhmM: ForgeTypeId
    NgPerPaSMSup2: ForgeTypeId
    Newton: ForgeTypeId
    NSPerMSup2: ForgeTypeId
    NPerMmSup2: ForgeTypeId
    NPerMSup2: ForgeTypeId
    NPerM: ForgeTypeId
    NDashMPerM: ForgeTypeId
    NDashM: ForgeTypeId
    Ms: ForgeTypeId
    Mph: ForgeTypeId
    MmSup6: ForgeTypeId
    MmSup4: ForgeTypeId
    MmSup3: ForgeTypeId
    MmSup2PerM: ForgeTypeId
    MmSup2: ForgeTypeId
    MmHg: ForgeTypeId
    MmH2OPerM: ForgeTypeId
    MmH2O: ForgeTypeId
    MmCaret3: ForgeTypeId
    MmCaret2: ForgeTypeId
    Mm: ForgeTypeId
    Min: ForgeTypeId
    MiPerSSup2: ForgeTypeId
    Meter: ForgeTypeId
    Mbh: ForgeTypeId
    MW: ForgeTypeId
    MV: ForgeTypeId
    MSup6: ForgeTypeId
    MSup4: ForgeTypeId
    MSup3PerWS: ForgeTypeId
    MSup3PerS: ForgeTypeId
    MSup3PerKg: ForgeTypeId
    MSup3PerKN: ForgeTypeId
    MSup3PerHMSup3: ForgeTypeId
    MSup3PerHMSup2: ForgeTypeId
    MSup3PerH: ForgeTypeId
    MSup3: ForgeTypeId
    MSup2PerS: ForgeTypeId
    MSup2PerM: ForgeTypeId
    MSup2PerKw: ForgeTypeId
    MSup2PerKN: ForgeTypeId
    MSup2KPerW: ForgeTypeId
    MSup2: ForgeTypeId
    MPerSSup2: ForgeTypeId
    MPerS: ForgeTypeId
    MPerKN: ForgeTypeId
    MPa: ForgeTypeId
    MNPerMSup2: ForgeTypeId
    MNPerM: ForgeTypeId
    MNDashMPerM: ForgeTypeId
    MNDashM: ForgeTypeId
    MN: ForgeTypeId
    MJ: ForgeTypeId
    MH2OPerM: ForgeTypeId
    MH2O: ForgeTypeId
    MCaret3: ForgeTypeId
    MCaret2: ForgeTypeId
    MBtu: ForgeTypeId
    MA: ForgeTypeId
    Lx: ForgeTypeId
    LpsPerMSup2: ForgeTypeId
    Lps: ForgeTypeId
    Lpm: ForgeTypeId
    LmPerW: ForgeTypeId
    Lm: ForgeTypeId
    Liter: ForgeTypeId
    Lf: ForgeTypeId
    LbmPerInSup3: ForgeTypeId
    LbmPerFtSup3: ForgeTypeId
    LbmPerFtDashS: ForgeTypeId
    LbmPerFtDashH: ForgeTypeId
    LbmPerFt: ForgeTypeId
    Lbm: ForgeTypeId
    LbfPerInSup2: ForgeTypeId
    LbfPerFtSup3: ForgeTypeId
    LbfPerFtSup2: ForgeTypeId
    LbfPerFt: ForgeTypeId
    LbfDashFtPerFt: ForgeTypeId
    LbfDashFt: ForgeTypeId
    Lbf: ForgeTypeId
    LbMassPerS: ForgeTypeId
    LbMassPerMin: ForgeTypeId
    LbMassPerLbDegreeF: ForgeTypeId
    LbMassPerInSup3: ForgeTypeId
    LbMassPerH: ForgeTypeId
    LbMassPerFtSup3: ForgeTypeId
    LbMassPerFtSup2: ForgeTypeId
    LbMassPerFtDashS: ForgeTypeId
    LbMassPerFtDashH: ForgeTypeId
    LbMassPerFt: ForgeTypeId
    LbMass: ForgeTypeId
    LbForceSPerFtSup2: ForgeTypeId
    LbForcePerInSup2: ForgeTypeId
    LbForcePerFtSup3: ForgeTypeId
    LbForcePerFtSup2: ForgeTypeId
    LbForcePerFt: ForgeTypeId
    LbForceDashFtPerFt: ForgeTypeId
    LbForceDashFt: ForgeTypeId
    LbForce: ForgeTypeId
    LPerSMSup3: ForgeTypeId
    LPerSMSup2: ForgeTypeId
    LPerSKw: ForgeTypeId
    LPerS: ForgeTypeId
    LPerMin: ForgeTypeId
    LPerH: ForgeTypeId
    Ksi: ForgeTypeId
    Ksf: ForgeTypeId
    Krone: ForgeTypeId
    KmPerSSup2: ForgeTypeId
    KmPerH: ForgeTypeId
    KipPerInSup3: ForgeTypeId
    KipPerInSup2: ForgeTypeId
    KipPerIn: ForgeTypeId
    KipPerFtSup3: ForgeTypeId
    KipPerFtSup2: ForgeTypeId
    KipPerFt: ForgeTypeId
    KipDashFtPerFt: ForgeTypeId
    KipDashFtPerDegreePerFt: ForgeTypeId
    KipDashFtPerDegree: ForgeTypeId
    KipDashFt: ForgeTypeId
    Kip: ForgeTypeId
    KgfPerMSup2: ForgeTypeId
    KgfPerM: ForgeTypeId
    KgfDashMPerM: ForgeTypeId
    KgfDashM: ForgeTypeId
    Kgf: ForgeTypeId
    KgPerS: ForgeTypeId
    KgPerMin: ForgeTypeId
    KgPerMSup3: ForgeTypeId
    KgPerMSup2: ForgeTypeId
    KgPerMS: ForgeTypeId
    KgPerMH: ForgeTypeId
    KgPerM: ForgeTypeId
    KgPerKgK: ForgeTypeId
    KgPerH: ForgeTypeId
    Kg: ForgeTypeId
    KelvinInterval: ForgeTypeId
    Kelvin: ForgeTypeId
    KcalPerS: ForgeTypeId
    Kcal: ForgeTypeId
    KWh: ForgeTypeId
    KW: ForgeTypeId
    KVA: ForgeTypeId
    KV: ForgeTypeId
    KPa: ForgeTypeId
    KNPerMmSup2: ForgeTypeId
    KNPerMSup3: ForgeTypeId
    KNPerMSup2: ForgeTypeId
    KNPerM: ForgeTypeId
    KNPerCmSup2: ForgeTypeId
    KNDashMPerM: ForgeTypeId
    KNDashMPerDegreePerM: ForgeTypeId
    KNDashMPerDegree: ForgeTypeId
    KNDashM: ForgeTypeId
    KN: ForgeTypeId
    KJPerMSup2K: ForgeTypeId
    KJPerK: ForgeTypeId
    KJ: ForgeTypeId
    KBtu: ForgeTypeId
    KA: ForgeTypeId
    Joule: ForgeTypeId
    JPerMSup2K: ForgeTypeId
    JPerKgDegreeC: ForgeTypeId
    JPerK: ForgeTypeId
    JPerGDegreeC: ForgeTypeId
    JPerG: ForgeTypeId
    InvKip: ForgeTypeId
    InvKN: ForgeTypeId
    InvDegreeF: ForgeTypeId
    InvDegreeC: ForgeTypeId
    InchDoubleQuote: ForgeTypeId
    InSup6: ForgeTypeId
    InSup4: ForgeTypeId
    InSup3: ForgeTypeId
    InSup2PerFt: ForgeTypeId
    InSup2: ForgeTypeId
    InPerSSup2: ForgeTypeId
    InHg: ForgeTypeId
    InDashWgPer100ft: ForgeTypeId
    InDashWg: ForgeTypeId
    InCaret3: ForgeTypeId
    InCaret2: ForgeTypeId
    In: ForgeTypeId
    Hz: ForgeTypeId
    Hp: ForgeTypeId
    Hour: ForgeTypeId
    Hectare: ForgeTypeId
    HFtSup2DegreeFPerBtu: ForgeTypeId
    Grad: ForgeTypeId
    GrPerHFtSup2InHg: ForgeTypeId
    Gpm: ForgeTypeId
    Gph: ForgeTypeId
    GalPerMin: ForgeTypeId
    GalPerH: ForgeTypeId
    Gal: ForgeTypeId
    GJ: ForgeTypeId
    Ftc: ForgeTypeId
    FtSup6: ForgeTypeId
    FtSup4: ForgeTypeId
    FtSup3PerMin: ForgeTypeId
    FtSup3PerLbMass: ForgeTypeId
    FtSup3PerKip: ForgeTypeId
    FtSup3PerH: ForgeTypeId
    FtSup3HPerMinBtu: ForgeTypeId
    FtSup3: ForgeTypeId
    FtSup2PerTon: ForgeTypeId
    FtSup2PerS: ForgeTypeId
    FtSup2PerMbh: ForgeTypeId
    FtSup2PerKip: ForgeTypeId
    FtSup2PerFt: ForgeTypeId
    FtSup2HPerKbtu: ForgeTypeId
    FtSup2: ForgeTypeId
    FtPerSSup2: ForgeTypeId
    FtPerS: ForgeTypeId
    FtPerMin: ForgeTypeId
    FtPerKip: ForgeTypeId
    FtOfWaterPer100ft: ForgeTypeId
    FtOfWater: ForgeTypeId
    FtL: ForgeTypeId
    FtH2OPer100ft: ForgeTypeId
    FtH2O: ForgeTypeId
    FtCaret3: ForgeTypeId
    FtCaret2: ForgeTypeId
    Ft: ForgeTypeId
    Fps: ForgeTypeId
    Fpm: ForgeTypeId
    FootSingleQuote: ForgeTypeId
    FlLowercase: ForgeTypeId
    FeetOfWaterPer100ft: ForgeTypeId
    FeetOfWater: ForgeTypeId
    Fc: ForgeTypeId
    EuroSuffix: ForgeTypeId
    EuroPrefix: ForgeTypeId
    Dong: ForgeTypeId
    DollarPerWH: ForgeTypeId
    DollarPerW: ForgeTypeId
    DollarPerMSup2: ForgeTypeId
    DollarPerFtSup2: ForgeTypeId
    DollarPerBtu: ForgeTypeId
    DollarHPerBtu: ForgeTypeId
    Dm: ForgeTypeId
    DeltaK: ForgeTypeId
    DeltaDegreeR: ForgeTypeId
    DeltaDegreeF: ForgeTypeId
    DeltaDegreeC: ForgeTypeId
    DegreeRInterval: ForgeTypeId
    DegreeR: ForgeTypeId
    DegreeFInterval: ForgeTypeId
    DegreeF: ForgeTypeId
    DegreeCInterval: ForgeTypeId
    DegreeC: ForgeTypeId
    Degree: ForgeTypeId
    DaNPerMSup2: ForgeTypeId
    DaNPerM: ForgeTypeId
    DaNDashMPerM: ForgeTypeId
    DaNDashM: ForgeTypeId
    DaN: ForgeTypeId
    Cy: ForgeTypeId
    Cps: ForgeTypeId
    Colon12: ForgeTypeId
    Colon10: ForgeTypeId
    Colon1: ForgeTypeId
    Cms: ForgeTypeId
    Cmh: ForgeTypeId
    CmSup6: ForgeTypeId
    CmSup4: ForgeTypeId
    CmSup3: ForgeTypeId
    CmSup2PerM: ForgeTypeId
    CmSup2: ForgeTypeId
    CmPerMin: ForgeTypeId
    CmCaret3: ForgeTypeId
    CmCaret2: ForgeTypeId
    Cm: ForgeTypeId
    ChineseHongKongDollar: ForgeTypeId
    CfmPerTon: ForgeTypeId
    CfmPerSf: ForgeTypeId
    CfmPerFtSup3: ForgeTypeId
    CfmPerFtSup2: ForgeTypeId
    CfmPerCf: ForgeTypeId
    Cfm: ForgeTypeId
    Cfh: ForgeTypeId
    Cf: ForgeTypeId
    CdPerMSup2: ForgeTypeId
    CdPerFtSup2: ForgeTypeId
    Cd: ForgeTypeId
    CalPerS: ForgeTypeId
    Cal: ForgeTypeId
    CP: ForgeTypeId
    BtuPerS: ForgeTypeId
    BtuPerLbDegreeF: ForgeTypeId
    BtuPerLb: ForgeTypeId
    BtuPerHFtSup3: ForgeTypeId
    BtuPerHFtSup2DegreeF: ForgeTypeId
    BtuPerHFtSup2: ForgeTypeId
    BtuPerHFtDegreeF: ForgeTypeId
    BtuPerH: ForgeTypeId
    BtuPerFtSup2DegreeF: ForgeTypeId
    BtuPerDegreeF: ForgeTypeId
    Btu: ForgeTypeId
    Bar: ForgeTypeId
    Baht: ForgeTypeId
    Atm: ForgeTypeId
    Ampere: ForgeTypeId
    Acres: ForgeTypeId
    SlopeDegree: ForgeTypeId
    Custom: ForgeTypeId
    FL: ForgeTypeId

class SymbolicCurve(CurveElement):
    """.NET: Autodesk.Revit.DB.SymbolicCurve"""
    def __init__(self, *args) -> None: ...
    Subcategory: GraphicsStyle
    ReferenceType: ReferenceType
    IsDrawnInForeground: bool
    SupportsTangentLocks: bool
    CurveElementType: CurveElementType
    LineStyle: Element
    SketchPlane: SketchPlane
    CenterPointReference: Reference
    GeometryCurve: Curve
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
    def GetVisibility(self, ) -> FamilyElementVisibility: ...
    def SetVisibility(self, visibility: FamilyElementVisibility) -> None: ...

class SymbolicCurveArray(APIObject):
    """.NET: Autodesk.Revit.DB.SymbolicCurveArray"""
    def __init__(self, *args) -> None: ...
    Item: SymbolicCurve
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: SymbolicCurve) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> SymbolicCurveArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: SymbolicCurve, index: int) -> None: ...
    def ReverseIterator(self, ) -> SymbolicCurveArrayIterator: ...

class SymbolicCurveArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.SymbolicCurveArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class SynchronizeWithCentralOptions:
    """.NET: Autodesk.Revit.DB.SynchronizeWithCentralOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    SaveLocalFile: bool
    RelinquishBorrowedElements: bool
    RelinquishUserCreatedWorksets: bool
    RelinquishViewWorksets: bool
    RelinquishFamilyWorksets: bool
    RelinquishProjectStandardWorksets: bool
    SaveLocalAfter: bool
    Compact: bool
    SaveLocalBefore: bool
    Comment: str
    def Dispose(self, ) -> None: ...
    def GetRelinquishOptions(self, ) -> RelinquishOptions: ...
    def SetRelinquishOptions(self, relinquishOptions: RelinquishOptions) -> None: ...

class TableCellCalculatedValueData:
    """.NET: Autodesk.Revit.DB.TableCellCalculatedValueData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetName(self, ) -> str: ...

class TableCellCombinedParameterData:
    """.NET: Autodesk.Revit.DB.TableCellCombinedParameterData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ParamId: ElementId
    CategoryId: ElementId
    Separator: str
    Suffix: str
    Prefix: str
    SampleValue: str
    @staticmethod
    def Create() -> TableCellCombinedParameterData: ...
    def Dispose(self, ) -> None: ...

class TableCellStyle:
    """.NET: Autodesk.Revit.DB.TableCellStyle"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    FontVerticalAlignment: VerticalAlignmentStyle
    FontHorizontalAlignment: HorizontalAlignmentStyle
    IsInactivePhaseload: bool
    IsFontUnderline: bool
    IsFontItalic: bool
    IsFontBold: bool
    IsReadOnly: bool
    IsEnabled: bool
    IsOverridden: bool
    BorderRightLineStyle: ElementId
    BorderLeftLineStyle: ElementId
    BorderBottomLineStyle: ElementId
    BorderTopLineStyle: ElementId
    TextOrientation: int
    SheetBackgroundColor: Color
    BackgroundColor: Color
    TextColor: Color
    TextSize: float
    FontName: str
    def Dispose(self, ) -> None: ...
    def GetCellStyleOverrideOptions(self, ) -> TableCellStyleOverrideOptions: ...
    def ResetOverride(self, ) -> None: ...
    def SetCellStyleOverrideOptions(self, helper: TableCellStyleOverrideOptions) -> None: ...

class TableCellStyleOverrideOptions:
    """.NET: Autodesk.Revit.DB.TableCellStyleOverrideOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    BorderLineStyle: bool
    TextOrientation: bool
    Underline: bool
    Italics: bool
    Bold: bool
    VerticalAlignment: bool
    HorizontalAlignment: bool
    BorderRightLineStyle: bool
    BorderLeftLineStyle: bool
    BorderBottomLineStyle: bool
    BorderTopLineStyle: bool
    BackgroundColor: bool
    FontColor: bool
    FontSize: bool
    Font: bool
    def Dispose(self, ) -> None: ...
    def SetAllOverrides(self, bOverride: bool) -> None: ...

class TableData:
    """.NET: Autodesk.Revit.DB.TableData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ZoomLevel: int
    Width: float
    WidthInPixels: int
    NumberOfSections: int
    FreezeColumnsAndRows: bool
    def Dispose(self, ) -> None: ...
    def GetSectionData(self, nIndex: int) -> TableSectionData: ...
    def IsEqual(self, OtherElem: TableData) -> bool: ...
    def IsValidZoomLevel(self, zoomLevel: int) -> bool: ...

class TableMergedCell:
    """.NET: Autodesk.Revit.DB.TableMergedCell"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Right: int
    Bottom: int
    Left: int
    Top: int
    def Dispose(self, ) -> None: ...

class TableSectionData:
    """.NET: Autodesk.Revit.DB.TableSectionData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    NeedsRefresh: bool
    NumberOfRows: int
    LastRowNumber: int
    FirstRowNumber: int
    LastColumnNumber: int
    FirstColumnNumber: int
    NumberOfColumns: int
    HideSection: bool
    def AllowOverrideCellStyle(self, nRow: int, nCol: int) -> bool: ...
    def CanInsertColumn(self, nIndex: int) -> bool: ...
    def CanInsertRow(self, nIndex: int) -> bool: ...
    def CanRemoveColumn(self, nIndex: int) -> bool: ...
    def CanRemoveRow(self, nIndex: int) -> bool: ...
    def ClearCell(self, nRow: int, nCol: int) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetCellCalculatedValue(self, nRow: int, nCol: int) -> TableCellCalculatedValueData: ...
    def GetCellCategoryId(self, nRow: int, nCol: int) -> ElementId: ...
    def GetCellCombinedParameters(self, nRow: int, nCol: int) -> IList: ...
    def GetCellFormatOptions(self, nRow: int, nCol: int, document: Document) -> FormatOptions: ...
    def GetCellParamId(self, nRow: int, nCol: int) -> ElementId: ...
    def GetCellSpec(self, nRow: int, nCol: int) -> ForgeTypeId: ...
    def GetCellText(self, nRow: int, nCol: int) -> str: ...
    def GetCellType(self, nRow: int, nCol: int) -> CellType: ...
    def GetColumnWidth(self, nCol: int) -> float: ...
    def GetColumnWidthInPixels(self, nCol: int) -> int: ...
    def GetCustomFieldId(self, row: int, col: int) -> Guid: ...
    def GetMergedCell(self, nRow: int, nCol: int) -> TableMergedCell: ...
    def GetRowHeight(self, nRow: int) -> float: ...
    def GetRowHeightInPixels(self, nRow: int) -> int: ...
    def GetTableCellStyle(self, nRow: int, nCol: int) -> TableCellStyle: ...
    def InsertColumn(self, index: int) -> None: ...
    def InsertImage(self, nRow: int, nColumn: int, imageSymbolId: ElementId) -> None: ...
    def InsertRow(self, nIndex: int) -> None: ...
    def IsAcceptableParamIdAndCategoryId(self, nRow: int, paramId: ElementId, categoryId: ElementId) -> bool: ...
    def IsCellFormattable(self, nRow: int, nCol: int) -> bool: ...
    def IsCellOverridden(self, nRow: int, nCol: int) -> bool: ...
    def IsDataOutOfDate(self, ) -> bool: ...
    def IsValidColumnNumber(self, nCol: int) -> bool: ...
    def IsValidImageSymbolId(self, imageSymbolId: ElementId) -> bool: ...
    def IsValidRowNumber(self, nRow: int) -> bool: ...
    def MergeCells(self, mergedCell: TableMergedCell) -> None: ...
    def RefreshData(self, ) -> bool: ...
    def RemoveColumn(self, nIndex: int) -> None: ...
    def RemoveRow(self, nIndex: int) -> None: ...
    def ResetCellOverride(self, nRow: int, nCol: int) -> None: ...
    def SetCellCalculatedValue(self, nRow: int, nCol: int, pCalcValue: TableCellCalculatedValueData) -> None: ...
    def SetCellCombinedParameters(self, nRow: int, nCol: int, paramData: IList) -> None: ...
    def SetCellFormatOptions(self, nRow: int, nCol: int, options: FormatOptions) -> None: ...
    def SetCellParamIdAndCategoryId(self, nRow: int, nCol: int, paramId: ElementId, categoryId: ElementId) -> None: ...
    def SetCellStyle(self, nRow: int, nCol: int, Style: TableCellStyle) -> None: ...
    def SetCellText(self, nRow: int, nCol: int, text: str) -> None: ...
    def SetCellType(self, nRow: int, nCol: int, type: CellType) -> None: ...
    def SetColumnWidth(self, nCol: int, width: float) -> None: ...
    def SetColumnWidthInPixels(self, nCol: int, width: int) -> None: ...
    def SetMergedCell(self, nRow: int, nCol: int, mergedCell: TableMergedCell) -> None: ...
    def SetRowHeight(self, nRow: int, height: float) -> None: ...
    def SetRowHeightInPixels(self, nRow: int, height: int) -> None: ...

class TableView(View):
    """.NET: Autodesk.Revit.DB.TableView"""
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
    def GetAvailableParameterCategories(self, sectionType: SectionType, row: int) -> IList: ...
    @staticmethod
    def GetAvailableParameters(cda: Document, categoryId: ElementId) -> IList: ...
    def GetCalculatedValueName(self, sectionType: SectionType, row: int, column: int) -> str: ...
    def GetCalculatedValueText(self, sectionType: SectionType, row: int, column: int) -> str: ...
    def GetCellText(self, sectionType: SectionType, row: int, column: int) -> str: ...
    def IsValidSectionType(self, sectionType: SectionType) -> bool: ...

class TagHeadAlignment:
    """.NET: Autodesk.Revit.DB.TagHeadAlignment"""
    def __init__(self, *args) -> None: ...
    ...

class TagHeadPositionOptions:
    """.NET: Autodesk.Revit.DB.TagHeadPositionOptions"""
    def __init__(self, *args) -> None: ...
    ...

class TagMode:
    """.NET: Autodesk.Revit.DB.TagMode"""
    def __init__(self, *args) -> None: ...
    ...

class TagOrientation:
    """.NET: Autodesk.Revit.DB.TagOrientation"""
    def __init__(self, *args) -> None: ...
    ...

class TagOrientationBehavior:
    """.NET: Autodesk.Revit.DB.TagOrientationBehavior"""
    def __init__(self, *args) -> None: ...
    ...

class TemporaryGraphicsManager:
    """.NET: Autodesk.Revit.DB.TemporaryGraphicsManager"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def AddControl(self, data: InCanvasControlData, ownerViewId: ElementId) -> int: ...
    def Clear(self, ) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetAll(self, ) -> ICollection: ...
    @staticmethod
    def GetTemporaryGraphicsManager(document: Document) -> TemporaryGraphicsManager: ...
    def RemoveControl(self, index: int) -> None: ...
    def SetTooltip(self, index: int, tooltip: str) -> None: ...
    def SetVisibility(self, index: int, visible: bool) -> None: ...
    def UpdateControl(self, index: int, data: InCanvasControlData) -> None: ...

class TemporaryViewMode:
    """.NET: Autodesk.Revit.DB.TemporaryViewMode"""
    def __init__(self, *args) -> None: ...
    ...

class TemporaryViewModes(APIObject):
    """.NET: Autodesk.Revit.DB.TemporaryViewModes"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    CustomColor: Color
    CustomTitle: str
    AcceleratedGraphicsMode: bool
    RevealHiddenElements: bool
    WorksharingDisplay: WorksharingDisplayMode
    RevealConstraints: bool
    PreviewFamilyVisibilityDefaultUncutState: bool
    PreviewFamilyVisibilityDefaultOnState: bool
    PreviewFamilyVisibility: PreviewFamilyVisibilityMode
    IsReadOnly: bool
    def DeactivateAllModes(self, ) -> None: ...
    def DeactivateMode(self, mode: TemporaryViewMode) -> None: ...
    def GetCaption(self, mode: TemporaryViewMode) -> str: ...
    def IsCustomized(self, ) -> bool: ...
    def IsModeActive(self, mode: TemporaryViewMode) -> bool: ...
    def IsModeAvailable(self, mode: TemporaryViewMode) -> bool: ...
    def IsModeEnabled(self, mode: TemporaryViewMode) -> bool: ...
    def IsValidState(self, state: PreviewFamilyVisibilityMode) -> bool: ...
    def RemoveCustomization(self, ) -> None: ...

class TessellatedBuildIssue:
    """.NET: Autodesk.Revit.DB.TessellatedBuildIssue"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    NumberEncountered: int
    def Dispose(self, ) -> None: ...
    def GetIssueDescription(self, ) -> str: ...
    def IsValidIssue(self, ) -> bool: ...
    def MakesDataUnusable(self, ) -> bool: ...
    def ReportIssueToDataSource(self, ) -> bool: ...

class TessellatedBuildIssueType:
    """.NET: Autodesk.Revit.DB.TessellatedBuildIssueType"""
    def __init__(self, *args) -> None: ...
    ...

class TessellatedFace:
    """.NET: Autodesk.Revit.DB.TessellatedFace"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    MaterialId: ElementId
    def Dispose(self, ) -> None: ...
    def GetBoundaryLoops(self, ) -> IList: ...

class TessellatedShapeBuilder(ShapeBuilder):
    """.NET: Autodesk.Revit.DB.TessellatedShapeBuilder"""
    def __init__(self, *args) -> None: ...
    NumberOfCompletedFaceSets: int
    OwnerInfo: str
    LogInteger: int
    LogString: str
    GraphicsStyleId: ElementId
    Fallback: TessellatedShapeBuilderFallback
    Target: TessellatedShapeBuilderTarget
    IsFaceSetOpen: bool
    IsValidObject: bool
    def AddFace(self, face: TessellatedFace) -> None: ...
    def AreTargetAndFallbackCompatible(self, target: TessellatedShapeBuilderTarget, fallback: TessellatedShapeBuilderFallback) -> bool: ...
    def Build(self, ) -> None: ...
    def CancelConnectedFaceSet(self, ) -> None: ...
    def Clear(self, ) -> None: ...
    def CloseConnectedFaceSet(self, ) -> None: ...
    @staticmethod
    def CreateMeshByExtrusion(profileLoops: IList, extrusionDirection: XYZ, extrusionDistance: float, materialId: ElementId) -> MeshFromGeometryOperationResult: ...
    def DoesFaceHaveEnoughLoopsAndVertices(self, face: TessellatedFace) -> bool: ...
    def GetBuildResult(self, ) -> TessellatedShapeBuilderResult: ...
    def OpenConnectedFaceSet(self, isSolid: bool) -> None: ...

class TessellatedShapeBuilderFallback:
    """.NET: Autodesk.Revit.DB.TessellatedShapeBuilderFallback"""
    def __init__(self, *args) -> None: ...
    ...

class TessellatedShapeBuilderOutcome:
    """.NET: Autodesk.Revit.DB.TessellatedShapeBuilderOutcome"""
    def __init__(self, *args) -> None: ...
    ...

class TessellatedShapeBuilderResult:
    """.NET: Autodesk.Revit.DB.TessellatedShapeBuilderResult"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    AreObjectsAvailable: bool
    Outcome: TessellatedShapeBuilderOutcome
    HasInvalidData: bool
    def Dispose(self, ) -> None: ...
    def GetGeometricalObjects(self, ) -> IList: ...
    def GetIssuesForFaceSet(self, setIndex: int) -> IList: ...
    def GetNumberOfFaceSets(self, ) -> int: ...

class TessellatedShapeBuilderTarget:
    """.NET: Autodesk.Revit.DB.TessellatedShapeBuilderTarget"""
    def __init__(self, *args) -> None: ...
    ...

class TextAlignFlags:
    """.NET: Autodesk.Revit.DB.TextAlignFlags"""
    def __init__(self, *args) -> None: ...
    ...

class TextAlignMask:
    """.NET: Autodesk.Revit.DB.TextAlignMask"""
    def __init__(self, *args) -> None: ...
    ...

class TextBaselineStyle:
    """.NET: Autodesk.Revit.DB.TextBaselineStyle"""
    def __init__(self, *args) -> None: ...
    ...

class TextElement(Element):
    """.NET: Autodesk.Revit.DB.TextElement"""
    def __init__(self, *args) -> None: ...
    IsTextWrappingActive: bool
    KeepRotatedTextReadable: bool
    VerticalAlignment: VerticalTextAlignment
    HorizontalAlignment: HorizontalTextAlignment
    Text: str
    Coord: XYZ
    Width: float
    Height: float
    UpDirection: XYZ
    BaseDirection: XYZ
    Symbol: TextElementType
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
    def GetMaximumAllowedWidth(cdda: Document, typeId: ElementId) -> float: ...
    @staticmethod
    def GetMinimumAllowedWidth(cdda: Document, typeId: ElementId) -> float: ...

class TextElementBackground:
    """.NET: Autodesk.Revit.DB.TextElementBackground"""
    def __init__(self, *args) -> None: ...
    ...

class TextElementType(LineAndTextAttrSymbol):
    """.NET: Autodesk.Revit.DB.TextElementType"""
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

class TextListStyle:
    """.NET: Autodesk.Revit.DB.TextListStyle"""
    def __init__(self, *args) -> None: ...
    ...

class TextNode(RenderNode):
    """.NET: Autodesk.Revit.DB.TextNode"""
    def __init__(self, *args) -> None: ...
    VerticalAlignment: VerticalTextAlignment
    HorizontalAlignment: HorizontalTextAlignment
    IsKeptReadable: bool
    IsTransparent: bool
    IsUnderlined: bool
    IsItalic: bool
    IsBold: bool
    TabSize: float
    FontHeight: float
    Height: float
    WidthScale: float
    Width: float
    UpDirection: XYZ
    BaseDirection: XYZ
    Position: XYZ
    Text: str
    FontName: str
    Color: Color
    IsValidObject: bool
    NodeName: str
    def GetFormattedText(self, ) -> FormattedText: ...

class TextNote(TextElement):
    """.NET: Autodesk.Revit.DB.TextNote"""
    def __init__(self, *args) -> None: ...
    LeaderRightAttachment: LeaderAtachement
    LeaderLeftAttachment: LeaderAtachement
    LeaderCount: int
    TextNoteType: TextNoteType
    IsTextWrappingActive: bool
    KeepRotatedTextReadable: bool
    VerticalAlignment: VerticalTextAlignment
    HorizontalAlignment: HorizontalTextAlignment
    Text: str
    Coord: XYZ
    Width: float
    Height: float
    UpDirection: XYZ
    BaseDirection: XYZ
    Symbol: TextElementType
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
    def AddLeader(self, leaderType: TextNoteLeaderTypes) -> Leader: ...
    @staticmethod
    def Create(document: Document, viewId: ElementId, position: XYZ, width: float, text: str, options: TextNoteOptions) -> TextNote: ...
    def GetFormattedText(self, ) -> FormattedText: ...
    def GetLeaders(self, ) -> IList: ...
    def RemoveLeaders(self, ) -> None: ...
    def SetFormattedText(self, formattedText: FormattedText) -> None: ...

class TextNoteLeaderStyles:
    """.NET: Autodesk.Revit.DB.TextNoteLeaderStyles"""
    def __init__(self, *args) -> None: ...
    ...

class TextNoteLeaderTypes:
    """.NET: Autodesk.Revit.DB.TextNoteLeaderTypes"""
    def __init__(self, *args) -> None: ...
    ...

class TextNoteOptions:
    """.NET: Autodesk.Revit.DB.TextNoteOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    KeepRotatedTextReadable: bool
    VerticalAlignment: VerticalTextAlignment
    HorizontalAlignment: HorizontalTextAlignment
    Rotation: float
    TypeId: ElementId
    def Dispose(self, ) -> None: ...

class TextNoteType(TextElementType):
    """.NET: Autodesk.Revit.DB.TextNoteType"""
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

class TextRange:
    """.NET: Autodesk.Revit.DB.TextRange"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    End: int
    Length: int
    Start: int
    def Dispose(self, ) -> None: ...

class TextTreatment:
    """.NET: Autodesk.Revit.DB.TextTreatment"""
    def __init__(self, *args) -> None: ...
    ...

class ThermalAsset:
    """.NET: Autodesk.Revit.DB.ThermalAsset"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Name: str
    Behavior: StructuralBehavior
    ThermalConductivity: float
    Density: float
    ElectricalResistivity: float
    Reflectivity: float
    Porosity: float
    Permeability: float
    TransmitsLight: bool
    VaporPressure: float
    SpecificHeat: float
    SpecificHeatOfVaporization: float
    LiquidViscosity: float
    Compressibility: float
    GasViscosity: float
    Emissivity: float
    ThermalMaterialType: ThermalMaterialType
    def Copy(self, ) -> ThermalAsset: ...
    def Dispose(self, ) -> None: ...
    def Equals(self, other: ThermalAsset) -> bool: ...
    def EqualsThermalOnly(self, other: ThermalAsset) -> bool: ...

class ThermalMaterialType:
    """.NET: Autodesk.Revit.DB.ThermalMaterialType"""
    def __init__(self, *args) -> None: ...
    ...

class ThermalProperties(APIObject):
    """.NET: Autodesk.Revit.DB.ThermalProperties"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ThermalMass: float
    ThermalResistance: float
    ThermalTransmittance: float
    HeatTransferCoefficient: float
    Roughness: int
    Absorptance: float
    IsReadOnly: bool

class TilePattern(ElementType):
    """.NET: Autodesk.Revit.DB.TilePattern"""
    def __init__(self, *args) -> None: ...
    TilesPerSeedNode: int
    TilePatternType: TilePatternsBuiltIn
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

class TilePatterns(APIObject):
    """.NET: Autodesk.Revit.DB.TilePatterns"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool
    def GetTilePattern(self, tilePatternBuiltIn: TilePatternsBuiltIn) -> TilePattern: ...

class TilePatternsBuiltIn:
    """.NET: Autodesk.Revit.DB.TilePatternsBuiltIn"""
    def __init__(self, *args) -> None: ...
    ...

class Toposolid(CeilingAndFloor):
    """.NET: Autodesk.Revit.DB.Toposolid"""
    def __init__(self, *args) -> None: ...
    SketchId: ElementId
    HostTopoId: ElementId
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
    def CanBeExcavatedBy(self, elementId: ElementId) -> bool: ...
    @staticmethod
    def Create(document: Document, profiles: IList, points: IList, topoTypeId: ElementId, levelId: ElementId) -> Toposolid: ...
    @staticmethod
    def CreateFromTopographySurface(document: Document, hostSurfaceId: ElementId, topoTypeId: ElementId, levelId: ElementId) -> Toposolid: ...
    def CreateSubDivision(self, document: Document, topoTypeId: ElementId, profiles: IList) -> Toposolid: ...
    def ExcavateBy(self, elementId: ElementId) -> None: ...
    def GetIntersectingElementData(self, ) -> IList: ...
    def GetSlabShapeEditor(self, ) -> SlabShapeEditor: ...
    def GetSubDivisionIds(self, ) -> IList: ...
    @staticmethod
    def IsCutVoidStabilityEnabled(document: Document) -> bool: ...
    @staticmethod
    def IsSmoothedSurfaceEnabled(document: Document) -> bool: ...
    def RemoveExcavationBy(self, elementId: ElementId) -> None: ...
    @staticmethod
    def SetCutVoidStability(document: Document, enable: bool) -> None: ...
    @staticmethod
    def SetSmoothedSurface(document: Document, enable: bool) -> None: ...
    def Simplify(self, percentage: float) -> None: ...
    def Split(self, splitCurveLoops: IList) -> IList: ...

class ToposolidType(HostObjAttributes):
    """.NET: Autodesk.Revit.DB.ToposolidType"""
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
    def GetContourSetting(self, ) -> ContourSetting: ...
    def SetContourSettting(self, setting: ContourSetting) -> None: ...

class TransactWithCentralOptions:
    """.NET: Autodesk.Revit.DB.TransactWithCentralOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetLockCallback(self, ) -> ICentralLockedCallback: ...
    def SetLockCallback(self, lockCallback: ICentralLockedCallback) -> None: ...

class Transaction:
    """.NET: Autodesk.Revit.DB.Transaction"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Commit(self, options: FailureHandlingOptions) -> TransactionStatus: ...
    def Dispose(self, ) -> None: ...
    def GetFailureHandlingOptions(self, ) -> FailureHandlingOptions: ...
    def GetName(self, ) -> str: ...
    def GetStatus(self, ) -> TransactionStatus: ...
    def HasEnded(self, ) -> bool: ...
    def HasStarted(self, ) -> bool: ...
    def RollBack(self, options: FailureHandlingOptions) -> TransactionStatus: ...
    def SetFailureHandlingOptions(self, options: FailureHandlingOptions) -> None: ...
    def SetName(self, name: str) -> None: ...
    def Start(self, name: str) -> TransactionStatus: ...

class TransactionGroup:
    """.NET: Autodesk.Revit.DB.TransactionGroup"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsFailureHandlingForcedModal: bool
    def Assimilate(self, ) -> TransactionStatus: ...
    def Commit(self, ) -> TransactionStatus: ...
    def Dispose(self, ) -> None: ...
    def GetName(self, ) -> str: ...
    def GetStatus(self, ) -> TransactionStatus: ...
    def HasEnded(self, ) -> bool: ...
    def HasStarted(self, ) -> bool: ...
    def RollBack(self, ) -> TransactionStatus: ...
    def SetName(self, name: str) -> None: ...
    def Start(self, transGroupName: str) -> TransactionStatus: ...

class TransactionStatus:
    """.NET: Autodesk.Revit.DB.TransactionStatus"""
    def __init__(self, *args) -> None: ...
    ...

class Transform(APIObject):
    """.NET: Autodesk.Revit.DB.Transform"""
    def __init__(self, *args) -> None: ...
    Inverse: Transform
    Determinant: float
    IsConformal: bool
    HasReflection: bool
    Scale: float
    IsTranslation: bool
    IsIdentity: bool
    Identity: Transform
    Origin: XYZ
    Basis: XYZ
    BasisZ: XYZ
    BasisY: XYZ
    BasisX: XYZ
    IsReadOnly: bool
    def AlmostEqual(self, right: Transform) -> bool: ...
    @staticmethod
    def CreateReflection(plane: Plane) -> Transform: ...
    @staticmethod
    def CreateRotation(axis: XYZ, angle: float) -> Transform: ...
    @staticmethod
    def CreateRotationAtPoint(axis: XYZ, angle: float, origin: XYZ) -> Transform: ...
    @staticmethod
    def CreateTranslation(vector: XYZ) -> Transform: ...
    def Multiply(self, right: Transform) -> Transform: ...
    def OfPoint(self, point: XYZ) -> XYZ: ...
    def OfVector(self, vec: XYZ) -> XYZ: ...
    def ScaleBasis(self, scale: float) -> Transform: ...
    def ScaleBasisAndOrigin(self, scale: float) -> Transform: ...

class Transform1D:
    """.NET: Autodesk.Revit.DB.Transform1D"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Determinant: float
    IsIdentity: bool
    Translation: float
    Scale: float
    def AlmostEqual(self, right: Transform1D) -> bool: ...
    def Assign(self, from_: Transform1D) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetInverse(self, ) -> Transform1D: ...
    def Multiply(self, right: Transform1D) -> Transform1D: ...
    def OfPoint(self, point: float) -> float: ...
    def OfVector(self, vector: float) -> float: ...
    def SetToIdentity(self, ) -> Transform1D: ...
    def TransformParameterDomain(self, domainStart: float, domainEnd: float) -> IList: ...

class Transform2D:
    """.NET: Autodesk.Revit.DB.Transform2D"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Scale: float
    HasReflection: bool
    BasisV: UV
    BasisU: UV
    Determinant: float
    IsConformal: bool
    IsTranslation: bool
    IsIdentity: bool
    Origin: UV
    def AlmostEqual(self, right: Transform2D) -> bool: ...
    def Assign(self, from_: Transform2D) -> None: ...
    @staticmethod
    def CreateIdentity() -> Transform2D: ...
    def Dispose(self, ) -> None: ...
    def GetInverse(self, ) -> Transform2D: ...
    def Multiply(self, right: Transform2D) -> Transform2D: ...
    def OfPoint(self, point: UV) -> UV: ...
    def OfVector(self, vector: UV) -> UV: ...
    def PostScale(self, scale: float) -> Transform2D: ...
    def PreScale(self, scale: float) -> Transform2D: ...
    def SetToIdentity(self, ) -> Transform2D: ...
    def TransformUVDomainIfPossible(self, uvDomain: BoundingBoxUV) -> BoundingBoxUV: ...

class TransformWithBoundary:
    """.NET: Autodesk.Revit.DB.TransformWithBoundary"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetBoundary(self, ) -> CurveLoop: ...
    def GetModelToProjectionTransform(self, ) -> Transform: ...

class TransmissionData:
    """.NET: Autodesk.Revit.DB.TransmissionData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Version: int
    UserData: str
    IsTransmitted: bool
    def Dispose(self, ) -> None: ...
    @staticmethod
    def DocumentIsNotTransmitted(filePath: ModelPath) -> bool: ...
    def GetAllExternalFileReferenceIds(self, ) -> ICollection: ...
    def GetDesiredReferenceData(self, elemId: ElementId) -> ExternalFileReference: ...
    def GetLastSavedReferenceData(self, elemId: ElementId) -> ExternalFileReference: ...
    @staticmethod
    def IsDocumentTransmitted(filePath: ModelPath) -> bool: ...
    @staticmethod
    def ReadTransmissionData(path: ModelPath) -> TransmissionData: ...
    def SetDesiredReferenceData(self, elemId: ElementId, path: ModelPath, pathType: PathType, shouldLoad: bool) -> None: ...
    @staticmethod
    def WriteTransmissionData(path: ModelPath, data: TransmissionData) -> None: ...

class TransmittedModelOptions:
    """.NET: Autodesk.Revit.DB.TransmittedModelOptions"""
    def __init__(self, *args) -> None: ...
    ...

class TriOrQuadFacet:
    """.NET: Autodesk.Revit.DB.TriOrQuadFacet"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Normal: XYZ
    NumberOfVertices: int
    def Dispose(self, ) -> None: ...
    def GetVertexIndex(self, index: int) -> int: ...

class TriangleInShellComponent:
    """.NET: Autodesk.Revit.DB.TriangleInShellComponent"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    VertexIndex2: int
    VertexIndex1: int
    VertexIndex0: int
    def Dispose(self, ) -> None: ...

class TriangulatedShellComponent:
    """.NET: Autodesk.Revit.DB.TriangulatedShellComponent"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    TriangleCount: int
    VertexCount: int
    IsClosed: bool
    def Clear(self, ) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetTriangle(self, triangleIndex: int) -> TriangleInShellComponent: ...
    def GetVertex(self, vertexIndex: int) -> XYZ: ...
    def GetVertices(self, ) -> IList: ...

class TriangulatedSolidOrShell:
    """.NET: Autodesk.Revit.DB.TriangulatedSolidOrShell"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ShellComponentCount: int
    def Dispose(self, ) -> None: ...
    def GetShellComponent(self, componentIndex: int) -> TriangulatedShellComponent: ...

class TriangulationInterface:
    """.NET: Autodesk.Revit.DB.TriangulationInterface"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class TriangulationInterfaceForTriangulatedShellComponent(TriangulationInterface):
    """.NET: Autodesk.Revit.DB.TriangulationInterfaceForTriangulatedShellComponent"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class TriangulationInterfaceForTriangulatedSolidOrShell(TriangulationInterface):
    """.NET: Autodesk.Revit.DB.TriangulationInterfaceForTriangulatedSolidOrShell"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class TypeBinding(ElementBinding):
    """.NET: Autodesk.Revit.DB.TypeBinding"""
    def __init__(self, *args) -> None: ...
    Categories: CategorySet
    IsReadOnly: bool

class UV:
    """.NET: Autodesk.Revit.DB.UV"""
    def __init__(self, *args) -> None: ...
    BasisV: UV
    BasisU: UV
    Zero: UV
    Item: float
    V: float
    U: float
    def Add(self, source: UV) -> UV: ...
    def AngleTo(self, source: UV) -> float: ...
    def CrossProduct(self, source: UV) -> float: ...
    def DistanceTo(self, source: UV) -> float: ...
    def Divide(self, value: float) -> UV: ...
    def DotProduct(self, source: UV) -> float: ...
    def GetLength(self, ) -> float: ...
    def IsAlmostEqualTo(self, source: UV, tolerance: float) -> bool: ...
    def IsUnitLength(self, ) -> bool: ...
    def IsZeroLength(self, ) -> bool: ...
    def Multiply(self, value: float) -> UV: ...
    def Negate(self, ) -> UV: ...
    def Normalize(self, ) -> UV: ...
    def Subtract(self, source: UV) -> UV: ...
    def ToString(self, ) -> str: ...

class UVGridlineType:
    """.NET: Autodesk.Revit.DB.UVGridlineType"""
    def __init__(self, *args) -> None: ...
    ...

class UnderlayOrientation:
    """.NET: Autodesk.Revit.DB.UnderlayOrientation"""
    def __init__(self, *args) -> None: ...
    ...

class UnitFormatUtils:
    """.NET: Autodesk.Revit.DB.UnitFormatUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def Format(units: Units, specTypeId: ForgeTypeId, value: float, forEditing: bool, formatValueOptions: FormatValueOptions) -> str: ...
    @staticmethod
    def TryParse(units: Units, specTypeId: ForgeTypeId, stringToParse: str, valueParsingOptions: ValueParsingOptions, value: float, message: str) -> bool: ...

class UnitSystem:
    """.NET: Autodesk.Revit.DB.UnitSystem"""
    def __init__(self, *args) -> None: ...
    ...

class UnitTypeId:
    """.NET: Autodesk.Revit.DB.UnitTypeId"""
    def __init__(self, *args) -> None: ...
    TonnesCarbonDioxidePerItem: ForgeTypeId
    TonnesCarbonDioxidePerPoundMass: ForgeTypeId
    TonnesCarbonDioxidePerKilogram: ForgeTypeId
    TonnesCarbonDioxidePerFoot: ForgeTypeId
    TonnesCarbonDioxidePerMeter: ForgeTypeId
    TonnesCarbonDioxidePerSquareFoot: ForgeTypeId
    TonnesCarbonDioxidePerSquareMeter: ForgeTypeId
    TonnesCarbonDioxidePerCubicFoot: ForgeTypeId
    TonnesCarbonDioxidePerCubicMeter: ForgeTypeId
    TonnesCarbonDioxidePerMillionBritishThermalUnits: ForgeTypeId
    TonnesCarbonDioxidePerThousandBritishThermalUnits: ForgeTypeId
    TonnesCarbonDioxidePerBritishThermalUnit: ForgeTypeId
    TonnesCarbonDioxidePerMegawattHour: ForgeTypeId
    TonnesCarbonDioxidePerKilowattHour: ForgeTypeId
    KilogramsCarbonDioxidePerItem: ForgeTypeId
    KilogramsCarbonDioxidePerPound: ForgeTypeId
    KilogramsCarbonDioxidePerKilogram: ForgeTypeId
    KilogramsCarbonDioxidePerFoot: ForgeTypeId
    KilogramsCarbonDioxidePerMeter: ForgeTypeId
    KilogramsCarbonDioxidePerSquareFoot: ForgeTypeId
    KilogramsCarbonDioxidePerSquareMeter: ForgeTypeId
    KilogramsCarbonDioxidePerCubicFoot: ForgeTypeId
    KilogramsCarbonDioxidePerCubicMeter: ForgeTypeId
    KilogramsCarbonDioxidePerMillionBritishThermalUnits: ForgeTypeId
    KilogramsCarbonDioxidePerThousandBritishThermalUnits: ForgeTypeId
    KilogramsCarbonDioxidePerBritishThermalUnit: ForgeTypeId
    KilogramsCarbonDioxidePerMegawattHour: ForgeTypeId
    KilogramsCarbonDioxidePerKilowattHour: ForgeTypeId
    WattsPerSquareMeterKelvin: ForgeTypeId
    WattsPerSquareMeter: ForgeTypeId
    WattsPerSquareFoot: ForgeTypeId
    WattsPerMeterKelvin: ForgeTypeId
    WattsPerMeter: ForgeTypeId
    WattsPerFoot: ForgeTypeId
    WattsPerCubicMeterPerSecond: ForgeTypeId
    WattsPerCubicMeter: ForgeTypeId
    WattsPerCubicFootPerMinute: ForgeTypeId
    WattsPerCubicFoot: ForgeTypeId
    Watts: ForgeTypeId
    Volts: ForgeTypeId
    VoltAmperesPerSquareMeter: ForgeTypeId
    VoltAmperesPerSquareFoot: ForgeTypeId
    VoltAmperes: ForgeTypeId
    UsTonnesMass: ForgeTypeId
    UsTonnesForce: ForgeTypeId
    UsSurveyFeet: ForgeTypeId
    UsGallonsPerMinute: ForgeTypeId
    UsGallonsPerHour: ForgeTypeId
    UsGallons: ForgeTypeId
    TonsOfRefrigeration: ForgeTypeId
    TonnesForcePerSquareMeter: ForgeTypeId
    TonnesForcePerMeter: ForgeTypeId
    TonnesForce: ForgeTypeId
    Tonnes: ForgeTypeId
    TonneForceMetersPerMeter: ForgeTypeId
    TonneForceMeters: ForgeTypeId
    ThousandBritishThermalUnitsPerHour: ForgeTypeId
    ThousandBritishThermalUnits: ForgeTypeId
    Therms: ForgeTypeId
    SquareMillimetersPerMeter: ForgeTypeId
    SquareMillimeters: ForgeTypeId
    SquareMetersPerSecond: ForgeTypeId
    SquareMetersPerMeter: ForgeTypeId
    SquareMetersPerKilowatt: ForgeTypeId
    SquareMetersPerKilonewton: ForgeTypeId
    SquareMeters: ForgeTypeId
    SquareMeterKelvinsPerWatt: ForgeTypeId
    SquareInchesPerFoot: ForgeTypeId
    SquareInches: ForgeTypeId
    SquareFeetPerTonOfRefrigeration: ForgeTypeId
    SquareFeetPerSecond: ForgeTypeId
    SquareFeetPerKip: ForgeTypeId
    SquareFeetPerFoot: ForgeTypeId
    SquareFeetPer1000BritishThermalUnitsPerHour: ForgeTypeId
    SquareFeet: ForgeTypeId
    SquareCentimetersPerMeter: ForgeTypeId
    SquareCentimeters: ForgeTypeId
    Shaku: ForgeTypeId
    Seconds: ForgeTypeId
    RiseDividedBy1Foot: ForgeTypeId
    RiseDividedBy12Inches: ForgeTypeId
    RiseDividedBy120Inches: ForgeTypeId
    RiseDividedBy10Feet: ForgeTypeId
    RiseDividedBy1000Millimeters: ForgeTypeId
    RevolutionsPerSecond: ForgeTypeId
    RevolutionsPerMinute: ForgeTypeId
    RatioTo12: ForgeTypeId
    RatioTo10: ForgeTypeId
    RatioTo1: ForgeTypeId
    RankineInterval: ForgeTypeId
    Rankine: ForgeTypeId
    RadiansPerSecond: ForgeTypeId
    Radians: ForgeTypeId
    PoundsMassPerSquareFoot: ForgeTypeId
    PoundsMassPerSecond: ForgeTypeId
    PoundsMassPerPoundDegreeFahrenheit: ForgeTypeId
    PoundsMassPerMinute: ForgeTypeId
    PoundsMassPerHour: ForgeTypeId
    PoundsMassPerFootSecond: ForgeTypeId
    PoundsMassPerFootHour: ForgeTypeId
    PoundsMassPerFoot: ForgeTypeId
    PoundsMassPerCubicInch: ForgeTypeId
    PoundsMassPerCubicFoot: ForgeTypeId
    PoundsMass: ForgeTypeId
    PoundsForcePerSquareInch: ForgeTypeId
    PoundsForcePerSquareFoot: ForgeTypeId
    PoundsForcePerFoot: ForgeTypeId
    PoundsForcePerCubicFoot: ForgeTypeId
    PoundsForce: ForgeTypeId
    PoundForceSecondsPerSquareFoot: ForgeTypeId
    PoundForceFeetPerFoot: ForgeTypeId
    PoundForceFeet: ForgeTypeId
    Pi: ForgeTypeId
    Percentage: ForgeTypeId
    PerMille: ForgeTypeId
    PascalsPerMeter: ForgeTypeId
    Pascals: ForgeTypeId
    PascalSeconds: ForgeTypeId
    OneToRatio: ForgeTypeId
    OhmMeters: ForgeTypeId
    NewtonsPerSquareMillimeter: ForgeTypeId
    NewtonsPerSquareMeter: ForgeTypeId
    NewtonsPerMeter: ForgeTypeId
    Newtons: ForgeTypeId
    NewtonSecondsPerSquareMeter: ForgeTypeId
    NewtonMetersPerMeter: ForgeTypeId
    NewtonMeters: ForgeTypeId
    NanogramsPerPascalSecondSquareMeter: ForgeTypeId
    Minutes: ForgeTypeId
    Millivolts: ForgeTypeId
    Milliseconds: ForgeTypeId
    MillionBritishThermalUnits: ForgeTypeId
    MillimetersToTheSixthPower: ForgeTypeId
    MillimetersToTheFourthPower: ForgeTypeId
    MillimetersOfWaterColumnPerMeter: ForgeTypeId
    MillimetersOfWaterColumn: ForgeTypeId
    MillimetersOfMercury: ForgeTypeId
    Millimeters: ForgeTypeId
    Milliamperes: ForgeTypeId
    MilesPerSecondSquared: ForgeTypeId
    MilesPerHour: ForgeTypeId
    MicrometersPerMeterDegreeCelsius: ForgeTypeId
    MicroinchesPerInchDegreeFahrenheit: ForgeTypeId
    MetersToTheSixthPower: ForgeTypeId
    MetersToTheFourthPower: ForgeTypeId
    MetersPerSecondSquared: ForgeTypeId
    MetersPerSecond: ForgeTypeId
    MetersPerKilonewton: ForgeTypeId
    MetersOfWaterColumnPerMeter: ForgeTypeId
    MetersOfWaterColumn: ForgeTypeId
    Meters: ForgeTypeId
    Megawatts: ForgeTypeId
    Megapascals: ForgeTypeId
    MeganewtonsPerSquareMeter: ForgeTypeId
    MeganewtonsPerMeter: ForgeTypeId
    Meganewtons: ForgeTypeId
    MeganewtonMetersPerMeter: ForgeTypeId
    MeganewtonMeters: ForgeTypeId
    Megajoules: ForgeTypeId
    Lux: ForgeTypeId
    LumensPerWatt: ForgeTypeId
    Lumens: ForgeTypeId
    LitersPerSecondSquareMeter: ForgeTypeId
    LitersPerSecondKilowatt: ForgeTypeId
    LitersPerSecondCubicMeter: ForgeTypeId
    LitersPerSecond: ForgeTypeId
    LitersPerMinute: ForgeTypeId
    LitersPerHour: ForgeTypeId
    Liters: ForgeTypeId
    KipsPerSquareInch: ForgeTypeId
    KipsPerSquareFoot: ForgeTypeId
    KipsPerInch: ForgeTypeId
    KipsPerFoot: ForgeTypeId
    KipsPerCubicInch: ForgeTypeId
    KipsPerCubicFoot: ForgeTypeId
    Kips: ForgeTypeId
    KipFeetPerFoot: ForgeTypeId
    KipFeetPerDegreePerFoot: ForgeTypeId
    KipFeetPerDegree: ForgeTypeId
    KipFeet: ForgeTypeId
    Kilowatts: ForgeTypeId
    KilowattHours: ForgeTypeId
    Kilovolts: ForgeTypeId
    KilovoltAmperes: ForgeTypeId
    Kilopascals: ForgeTypeId
    KilonewtonsPerSquareMillimeter: ForgeTypeId
    KilonewtonsPerSquareMeter: ForgeTypeId
    KilonewtonsPerSquareCentimeter: ForgeTypeId
    KilonewtonsPerMeter: ForgeTypeId
    KilonewtonsPerCubicMeter: ForgeTypeId
    Kilonewtons: ForgeTypeId
    KilonewtonMetersPerMeter: ForgeTypeId
    KilonewtonMetersPerDegreePerMeter: ForgeTypeId
    KilonewtonMetersPerDegree: ForgeTypeId
    KilonewtonMeters: ForgeTypeId
    KilometersPerSecondSquared: ForgeTypeId
    KilometersPerHour: ForgeTypeId
    KilojoulesPerSquareMeterKelvin: ForgeTypeId
    KilojoulesPerKelvin: ForgeTypeId
    Kilojoules: ForgeTypeId
    KilogramsPerSquareMeter: ForgeTypeId
    KilogramsPerSecond: ForgeTypeId
    KilogramsPerMinute: ForgeTypeId
    KilogramsPerMeterSecond: ForgeTypeId
    KilogramsPerMeterHour: ForgeTypeId
    KilogramsPerMeter: ForgeTypeId
    KilogramsPerKilogramKelvin: ForgeTypeId
    KilogramsPerHour: ForgeTypeId
    KilogramsPerCubicMeter: ForgeTypeId
    KilogramsForcePerSquareMeter: ForgeTypeId
    KilogramsForcePerMeter: ForgeTypeId
    KilogramsForce: ForgeTypeId
    Kilograms: ForgeTypeId
    KilogramForceMetersPerMeter: ForgeTypeId
    KilogramForceMeters: ForgeTypeId
    KilocaloriesPerSecond: ForgeTypeId
    Kilocalories: ForgeTypeId
    Kiloamperes: ForgeTypeId
    KelvinInterval: ForgeTypeId
    Kelvin: ForgeTypeId
    JoulesPerSquareMeterKelvin: ForgeTypeId
    JoulesPerKilogramDegreeCelsius: ForgeTypeId
    JoulesPerKelvin: ForgeTypeId
    JoulesPerGramDegreeCelsius: ForgeTypeId
    JoulesPerGram: ForgeTypeId
    Joules: ForgeTypeId
    InverseKips: ForgeTypeId
    InverseKilonewtons: ForgeTypeId
    InverseDegreesFahrenheit: ForgeTypeId
    InverseDegreesCelsius: ForgeTypeId
    InchesToTheSixthPower: ForgeTypeId
    InchesToTheFourthPower: ForgeTypeId
    InchesPerSecondSquared: ForgeTypeId
    InchesOfWater60DegreesFahrenheitPer100Feet: ForgeTypeId
    InchesOfWater60DegreesFahrenheit: ForgeTypeId
    InchesOfMercury32DegreesFahrenheit: ForgeTypeId
    Inches: ForgeTypeId
    Hours: ForgeTypeId
    HourSquareFootDegreesFahrenheitPerBritishThermalUnit: ForgeTypeId
    Horsepower: ForgeTypeId
    Hertz: ForgeTypeId
    Hectares: ForgeTypeId
    GrainsPerHourSquareFootInchMercury: ForgeTypeId
    Gradians: ForgeTypeId
    Gigajoules: ForgeTypeId
    General: ForgeTypeId
    Footlamberts: ForgeTypeId
    Footcandles: ForgeTypeId
    Fixed: ForgeTypeId
    FeetToTheSixthPower: ForgeTypeId
    FeetToTheFourthPower: ForgeTypeId
    FeetPerSecondSquared: ForgeTypeId
    FeetPerSecond: ForgeTypeId
    FeetPerMinute: ForgeTypeId
    FeetPerKip: ForgeTypeId
    FeetOfWater39_2DegreesFahrenheitPer100Feet: ForgeTypeId
    FeetOfWater39_2DegreesFahrenheit: ForgeTypeId
    Feet: ForgeTypeId
    FahrenheitInterval: ForgeTypeId
    Fahrenheit: ForgeTypeId
    DekanewtonsPerSquareMeter: ForgeTypeId
    DekanewtonsPerMeter: ForgeTypeId
    Dekanewtons: ForgeTypeId
    DekanewtonMetersPerMeter: ForgeTypeId
    DekanewtonMeters: ForgeTypeId
    Degrees: ForgeTypeId
    Decimeters: ForgeTypeId
    CyclesPerSecond: ForgeTypeId
    CurrencyPerWattHour: ForgeTypeId
    CurrencyPerWatt: ForgeTypeId
    CurrencyPerSquareMeter: ForgeTypeId
    CurrencyPerSquareFoot: ForgeTypeId
    CurrencyPerBritishThermalUnitPerHour: ForgeTypeId
    CurrencyPerBritishThermalUnit: ForgeTypeId
    Currency: ForgeTypeId
    CubicYards: ForgeTypeId
    CubicMillimeters: ForgeTypeId
    CubicMetersPerWattSecond: ForgeTypeId
    CubicMetersPerSecond: ForgeTypeId
    CubicMetersPerKilonewton: ForgeTypeId
    CubicMetersPerKilogram: ForgeTypeId
    CubicMetersPerHourSquareMeter: ForgeTypeId
    CubicMetersPerHourCubicMeter: ForgeTypeId
    CubicMetersPerHour: ForgeTypeId
    CubicMeters: ForgeTypeId
    CubicInches: ForgeTypeId
    CubicFeetPerPoundMass: ForgeTypeId
    CubicFeetPerMinuteTonOfRefrigeration: ForgeTypeId
    CubicFeetPerMinuteSquareFoot: ForgeTypeId
    CubicFeetPerMinutePerBritishThermalUnitPerHour: ForgeTypeId
    CubicFeetPerMinuteCubicFoot: ForgeTypeId
    CubicFeetPerMinute: ForgeTypeId
    CubicFeetPerKip: ForgeTypeId
    CubicFeetPerHour: ForgeTypeId
    CubicFeet: ForgeTypeId
    CubicCentimeters: ForgeTypeId
    Centipoises: ForgeTypeId
    CentimetersToTheSixthPower: ForgeTypeId
    CentimetersToTheFourthPower: ForgeTypeId
    CentimetersPerMinute: ForgeTypeId
    Centimeters: ForgeTypeId
    CelsiusInterval: ForgeTypeId
    Celsius: ForgeTypeId
    CandelasPerSquareMeter: ForgeTypeId
    CandelasPerSquareFoot: ForgeTypeId
    Candelas: ForgeTypeId
    CaloriesPerSecond: ForgeTypeId
    Calories: ForgeTypeId
    BritishThermalUnitsPerSquareFootDegreeFahrenheit: ForgeTypeId
    BritishThermalUnitsPerSecond: ForgeTypeId
    BritishThermalUnitsPerPoundDegreeFahrenheit: ForgeTypeId
    BritishThermalUnitsPerPound: ForgeTypeId
    BritishThermalUnitsPerHourSquareFootDegreeFahrenheit: ForgeTypeId
    BritishThermalUnitsPerHourSquareFoot: ForgeTypeId
    BritishThermalUnitsPerHourFootDegreeFahrenheit: ForgeTypeId
    BritishThermalUnitsPerHourCubicFoot: ForgeTypeId
    BritishThermalUnitsPerHour: ForgeTypeId
    BritishThermalUnitsPerDegreeFahrenheit: ForgeTypeId
    BritishThermalUnits: ForgeTypeId
    Bars: ForgeTypeId
    Atmospheres: ForgeTypeId
    Amperes: ForgeTypeId
    Acres: ForgeTypeId
    Steradians: ForgeTypeId
    StationingSurveyFeet: ForgeTypeId
    StationingMeters: ForgeTypeId
    StationingFeet: ForgeTypeId
    SlopeDegrees: ForgeTypeId
    MetersCentimeters: ForgeTypeId
    FractionalInches: ForgeTypeId
    FeetFractionalInches: ForgeTypeId
    DegreesMinutes: ForgeTypeId
    Custom: ForgeTypeId

class UnitUtils:
    """.NET: Autodesk.Revit.DB.UnitUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def Convert(value: float, currentUnitTypeId: ForgeTypeId, desiredUnitTypeId: ForgeTypeId) -> float: ...
    @staticmethod
    def ConvertFromInternalUnits(value: float, unitTypeId: ForgeTypeId) -> float: ...
    @staticmethod
    def ConvertToInternalUnits(value: float, unitTypeId: ForgeTypeId) -> float: ...
    @staticmethod
    def GetAllDisciplines() -> IList: ...
    @staticmethod
    def GetAllMeasurableSpecs() -> IList: ...
    @staticmethod
    def GetAllUnits() -> IList: ...
    @staticmethod
    def GetDiscipline(specTypeId: ForgeTypeId) -> ForgeTypeId: ...
    @staticmethod
    def GetTypeCatalogStringForSpec(specTypeId: ForgeTypeId) -> str: ...
    @staticmethod
    def GetTypeCatalogStringForUnit(unitTypeId: ForgeTypeId) -> str: ...
    @staticmethod
    def GetValidUnits(specTypeId: ForgeTypeId) -> IList: ...
    @staticmethod
    def IsMeasurableSpec(specTypeId: ForgeTypeId) -> bool: ...
    @staticmethod
    def IsSymbol(symbolTypeId: ForgeTypeId) -> bool: ...
    @staticmethod
    def IsUnit(unitTypeId: ForgeTypeId) -> bool: ...
    @staticmethod
    def IsValidUnit(specTypeId: ForgeTypeId, unitTypeId: ForgeTypeId) -> bool: ...

class Units:
    """.NET: Autodesk.Revit.DB.Units"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    DigitGroupingAmount: DigitGroupingAmount
    DigitGroupingSymbol: DigitGroupingSymbol
    DecimalSymbol: DecimalSymbol
    def Dispose(self, ) -> None: ...
    def GetFormatOptions(self, specTypeId: ForgeTypeId) -> FormatOptions: ...
    @staticmethod
    def GetModifiableSpecs() -> IList: ...
    @staticmethod
    def IsModifiableSpec(specTypeId: ForgeTypeId) -> bool: ...
    def SetFormatOptions(self, specTypeId: ForgeTypeId, options: FormatOptions) -> None: ...

class UpdaterData:
    """.NET: Autodesk.Revit.DB.UpdaterData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetAddedElementIds(self, ) -> ICollection: ...
    def GetDeletedElementIds(self, ) -> ICollection: ...
    def GetDocument(self, ) -> Document: ...
    def GetModifiedElementIds(self, ) -> ICollection: ...
    def IsChangeTriggered(self, id: ElementId, type: ChangeType) -> bool: ...

class UpdaterId:
    """.NET: Autodesk.Revit.DB.UpdaterId"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetAddInId(self, ) -> AddInId: ...
    def GetGUID(self, ) -> Guid: ...

class UpdaterInfo:
    """.NET: Autodesk.Revit.DB.UpdaterInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsOptional: bool
    ApplicationName: str
    AdditionalInformation: str
    UpdaterName: str
    def Dispose(self, ) -> None: ...

class UpdaterRegistry:
    """.NET: Autodesk.Revit.DB.UpdaterRegistry"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    @staticmethod
    def AddTrigger(id: UpdaterId, document: Document, filter: ElementFilter, change: ChangeType) -> None: ...
    @staticmethod
    def DisableUpdater(id: UpdaterId) -> None: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def EnableUpdater(id: UpdaterId) -> None: ...
    @staticmethod
    def GetIsUpdaterOptional(id: UpdaterId) -> bool: ...
    @staticmethod
    def GetRegisteredUpdaterInfos(document: Document) -> IList: ...
    @staticmethod
    def IsUpdaterEnabled(id: UpdaterId) -> bool: ...
    @staticmethod
    def IsUpdaterRegistered(id: UpdaterId, document: Document) -> bool: ...
    @staticmethod
    def RegisterUpdater(updater: IUpdater, document: Document, isOptional: bool) -> None: ...
    @staticmethod
    def RemoveAllTriggers(id: UpdaterId) -> None: ...
    @staticmethod
    def RemoveDocumentTriggers(id: UpdaterId, document: Document) -> None: ...
    @staticmethod
    def SetExecutionOrder(first: UpdaterId, second: UpdaterId) -> None: ...
    @staticmethod
    def SetIsUpdaterOptional(id: UpdaterId, isOptional: bool) -> None: ...
    @staticmethod
    def UnregisterUpdater(id: UpdaterId, document: Document) -> None: ...

class ValidateCurveLoopsOptions:
    """.NET: Autodesk.Revit.DB.ValidateCurveLoopsOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class ValueAtPointBase:
    """.NET: Autodesk.Revit.DB.ValueAtPointBase"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def ClearAllFlags(self, ) -> None: ...
    def ClearFlagsAt(self, measurement: int) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetFlags(self, measurement: int) -> int: ...
    def SetFlags(self, flags: int, measurement: int) -> None: ...

class ValueAtPointFlags:
    """.NET: Autodesk.Revit.DB.ValueAtPointFlags"""
    def __init__(self, *args) -> None: ...
    ...

class ValueParsingOptions:
    """.NET: Autodesk.Revit.DB.ValueParsingOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    AllowedValues: AllowedValues
    def Dispose(self, ) -> None: ...
    def GetFormatOptions(self, ) -> FormatOptions: ...
    def SetFormatOptions(self, formatOptions: FormatOptions) -> None: ...

class VertexIndexPair:
    """.NET: Autodesk.Revit.DB.VertexIndexPair"""
    def __init__(self, *args) -> None: ...
    Bottom: int
    Top: int

class VertexIndexPairArray(APIObject):
    """.NET: Autodesk.Revit.DB.VertexIndexPairArray"""
    def __init__(self, *args) -> None: ...
    Item: VertexIndexPair
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: VertexIndexPair) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> VertexIndexPairArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: VertexIndexPair, index: int) -> None: ...
    def ReverseIterator(self, ) -> VertexIndexPairArrayIterator: ...

class VertexIndexPairArrayIterator(APIObject):
    """.NET: Autodesk.Revit.DB.VertexIndexPairArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class VertexPair:
    """.NET: Autodesk.Revit.DB.VertexPair"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Second: int
    First: int
    def Dispose(self, ) -> None: ...

class VerticalAlignmentStyle:
    """.NET: Autodesk.Revit.DB.VerticalAlignmentStyle"""
    def __init__(self, *args) -> None: ...
    ...

class VerticalTextAlignment:
    """.NET: Autodesk.Revit.DB.VerticalTextAlignment"""
    def __init__(self, *args) -> None: ...
    ...

class View(Element):
    """.NET: Autodesk.Revit.DB.View"""
    def __init__(self, *args) -> None: ...
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
    def AddFilter(self, filterElementId: ElementId) -> None: ...
    def AllowsAnalysisDisplay(self, ) -> bool: ...
    def ApplyViewTemplateParameters(self, otherView: View) -> None: ...
    def AreGraphicsOverridesAllowed(self, ) -> bool: ...
    def CanApplyColorFillScheme(self, categoryId: ElementId, schemeId: ElementId) -> bool: ...
    def CanCategoryBeHidden(self, elementId: ElementId) -> bool: ...
    def CanCategoryBeHiddenTemporary(self, elementId: ElementId) -> bool: ...
    def CanEnableTemporaryViewPropertiesMode(self, ) -> bool: ...
    def CanModifyDetailLevel(self, ) -> bool: ...
    def CanModifyDisplayStyle(self, ) -> bool: ...
    def CanModifyViewDiscipline(self, ) -> bool: ...
    def CanUseDepthCueing(self, ) -> bool: ...
    def CanUseTemporaryVisibilityModes(self, ) -> bool: ...
    def CanViewBeDuplicated(self, duplicateOption: ViewDuplicateOption) -> bool: ...
    def ConvertTemporaryHideIsolateToPermanent(self, ) -> None: ...
    def ConvertToIndependent(self, ) -> None: ...
    def CreateViewTemplate(self, ) -> View: ...
    def DisableTemporaryViewMode(self, mode: TemporaryViewMode) -> None: ...
    def Duplicate(self, duplicateOption: ViewDuplicateOption) -> ElementId: ...
    def EnableRevealHiddenMode(self, ) -> None: ...
    def EnableTemporaryViewPropertiesMode(self, viewTemplateId: ElementId) -> bool: ...
    def GetBackground(self, ) -> ViewDisplayBackground: ...
    def GetCalloutParentId(self, ) -> ElementId: ...
    def GetCategoryHidden(self, categoryId: ElementId) -> bool: ...
    def GetCategoryOverrides(self, categoryId: ElementId) -> OverrideGraphicSettings: ...
    def GetColorFillSchemeId(self, categoryId: ElementId) -> ElementId: ...
    def GetCropRegionShapeManager(self, ) -> ViewCropRegionShapeManager: ...
    @staticmethod
    def GetCropRegionShapeManagerForReferenceCallout(doc: Document, callout: ElementId) -> ViewCropRegionShapeManager: ...
    def GetDependentViewIds(self, ) -> ICollection: ...
    def GetDepthCueing(self, ) -> ViewDisplayDepthCueing: ...
    def GetDirectContext3DHandleOverrides(self, ) -> DirectContext3DHandleOverrides: ...
    def GetElementOverrides(self, elementId: ElementId) -> OverrideGraphicSettings: ...
    def GetFilterOverrides(self, filterElementId: ElementId) -> OverrideGraphicSettings: ...
    def GetFilterVisibility(self, filterElementId: ElementId) -> bool: ...
    def GetFilters(self, ) -> ICollection: ...
    def GetIsFilterEnabled(self, filterElementId: ElementId) -> bool: ...
    def GetLinkOverrides(self, linkId: ElementId) -> RevitLinkGraphicsSettings: ...
    def GetModelToProjectionTransforms(self, ) -> IList: ...
    def GetNonControlledTemplateParameterIds(self, ) -> ICollection: ...
    def GetOrderedFilters(self, ) -> IList: ...
    def GetPlacementOnSheetStatus(self, ) -> ViewPlacementOnSheetStatus: ...
    def GetPointCloudOverrides(self, ) -> PointCloudOverrides: ...
    def GetPrimaryViewId(self, ) -> ElementId: ...
    def GetReferenceCallouts(self, ) -> ICollection: ...
    def GetReferenceElevations(self, ) -> ICollection: ...
    def GetReferenceSections(self, ) -> ICollection: ...
    def GetSketchyLines(self, ) -> ViewDisplaySketchyLines: ...
    def GetTemplateParameterIds(self, ) -> IList: ...
    def GetTemporaryViewPropertiesId(self, ) -> ElementId: ...
    def GetTemporaryViewPropertiesName(self, ) -> str: ...
    def GetViewDisplayModel(self, ) -> ViewDisplayModel: ...
    def GetWorksetVisibility(self, worksetId: WorksetId) -> WorksetVisibility: ...
    def GetWorksharingDisplayMode(self, ) -> WorksharingDisplayMode: ...
    def HasDetailLevel(self, ) -> bool: ...
    def HasDisplayStyle(self, ) -> bool: ...
    def HasViewDiscipline(self, ) -> bool: ...
    def HasViewTransforms(self, ) -> bool: ...
    def HideActiveWorkPlane(self, ) -> None: ...
    def HideCategoriesTemporary(self, elementIds: ICollection) -> None: ...
    def HideCategoryTemporary(self, elementId: ElementId) -> None: ...
    def HideElementTemporary(self, elementId: ElementId) -> None: ...
    def HideElements(self, elementIdSet: ICollection) -> None: ...
    def HideElementsTemporary(self, elementIdSet: ICollection) -> None: ...
    def IsCategoryOverridable(self, categoryId: ElementId) -> bool: ...
    def IsElementVisibleInTemporaryViewMode(self, mode: TemporaryViewMode, id: ElementId) -> bool: ...
    def IsFilterApplied(self, filterElementId: ElementId) -> bool: ...
    def IsInTemporaryViewMode(self, mode: TemporaryViewMode) -> bool: ...
    def IsTemporaryHideIsolateActive(self, ) -> bool: ...
    def IsTemporaryViewPropertiesModeEnabled(self, ) -> bool: ...
    @staticmethod
    def IsValidViewScale(viewScale: int) -> bool: ...
    def IsValidViewTemplate(self, templateId: ElementId) -> bool: ...
    def IsViewValidForTemplateCreation(self, ) -> bool: ...
    def IsWorksetVisible(self, worksetId: WorksetId) -> bool: ...
    def IsolateCategoriesTemporary(self, elementIds: ICollection) -> None: ...
    def IsolateCategoryTemporary(self, elementId: ElementId) -> None: ...
    def IsolateElementTemporary(self, elementId: ElementId) -> None: ...
    def IsolateElementsTemporary(self, elementIds: ICollection) -> None: ...
    def Print(self, viewTemplate: View, useCurrentPrintSettings: bool) -> None: ...
    def RemoveCalloutParent(self, ) -> None: ...
    def RemoveFilter(self, filterElementId: ElementId) -> None: ...
    def RemoveLinkOverrides(self, linkId: ElementId) -> None: ...
    def RestoreCalloutParent(self, ) -> None: ...
    def SetBackground(self, background: ViewDisplayBackground) -> None: ...
    def SetCategoryHidden(self, categoryId: ElementId, hide: bool) -> None: ...
    def SetCategoryOverrides(self, categoryId: ElementId, overrideGraphicSettings: OverrideGraphicSettings) -> None: ...
    def SetColorFillSchemeId(self, categoryId: ElementId, schemeId: ElementId) -> None: ...
    def SetDepthCueing(self, depthCueing: ViewDisplayDepthCueing) -> None: ...
    def SetElementOverrides(self, elementId: ElementId, overrideGraphicSettings: OverrideGraphicSettings) -> None: ...
    def SetFilterOverrides(self, filterElementId: ElementId, overrideGraphicSettings: OverrideGraphicSettings) -> None: ...
    def SetFilterVisibility(self, filterElementId: ElementId, visibility: bool) -> None: ...
    def SetIsFilterEnabled(self, filterElementId: ElementId, enable: bool) -> None: ...
    def SetLinkOverrides(self, linkId: ElementId, linkDisplaySettings: RevitLinkGraphicsSettings) -> None: ...
    def SetNonControlledTemplateParameterIds(self, newSet: ICollection) -> None: ...
    def SetSketchyLines(self, sketchyLines: ViewDisplaySketchyLines) -> None: ...
    def SetViewDisplayModel(self, viewDisplayModel: ViewDisplayModel) -> None: ...
    def SetWorksetVisibility(self, worksetId: WorksetId, visible: WorksetVisibility) -> None: ...
    def SetWorksharingDisplayMode(self, displayMode: WorksharingDisplayMode) -> None: ...
    def ShowActiveWorkPlane(self, ) -> None: ...
    def SupportedColorFillCategoryIds(self, ) -> ICollection: ...
    def SupportsRevealConstraints(self, ) -> bool: ...
    def SupportsWorksharingDisplayMode(self, mode: WorksharingDisplayMode) -> bool: ...
    def UnhideElements(self, elementIdSet: ICollection) -> None: ...

class View3D(View):
    """.NET: Autodesk.Revit.DB.View3D"""
    def __init__(self, *args) -> None: ...
    ProjectGridsOnSectionBox: bool
    IsSectionBoxActive: bool
    IsPerspective: bool
    IsLocked: bool
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
    def CanResetCameraTarget(self, ) -> bool: ...
    def CanSaveOrientation(self, ) -> bool: ...
    def CanToggleBetweenPerspectiveAndIsometric(self, ) -> bool: ...
    @staticmethod
    def CreateIsometric(document: Document, viewFamilyTypeId: ElementId) -> View3D: ...
    @staticmethod
    def CreatePerspective(document: Document, viewFamilyTypeId: ElementId) -> View3D: ...
    def GetLevelsThatShowGrids(self, ) -> ISet: ...
    def GetOrientation(self, ) -> ViewOrientation3D: ...
    def GetRenderingSettings(self, ) -> RenderingSettings: ...
    def GetSavedOrientation(self, ) -> ViewOrientation3D: ...
    def GetSectionBox(self, ) -> BoundingBoxXYZ: ...
    def HasBeenLocked(self, ) -> bool: ...
    def HideGridsOnLevel(self, levelId: ElementId) -> None: ...
    def OrientTo(self, forwardDirection: XYZ) -> None: ...
    def ResetCameraTarget(self, ) -> None: ...
    def RestoreOrientationAndLock(self, ) -> None: ...
    def SaveOrientation(self, ) -> None: ...
    def SaveOrientationAndLock(self, ) -> None: ...
    def ScalePerspectiveCropBox(self, multiplier: float) -> None: ...
    def SetOrientation(self, newViewOrientation3D: ViewOrientation3D) -> None: ...
    def SetRenderingSettings(self, settings: RenderingSettings) -> None: ...
    def SetSectionBox(self, boundingBoxXYZ: BoundingBoxXYZ) -> None: ...
    def ShowGridsOnLevel(self, levelId: ElementId) -> None: ...
    def ShowGridsOnLevels(self, levelsIds: ISet) -> None: ...
    def ToggleToIsometric(self, ) -> None: ...
    def ToggleToPerspective(self, ) -> None: ...
    def Unlock(self, ) -> None: ...

class ViewAnchor:
    """.NET: Autodesk.Revit.DB.ViewAnchor"""
    def __init__(self, *args) -> None: ...
    ...

class ViewCropRegionShapeManager:
    """.NET: Autodesk.Revit.DB.ViewCropRegionShapeManager"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    RightAnnotationCropOffset: float
    LeftAnnotationCropOffset: float
    BottomAnnotationCropOffset: float
    TopAnnotationCropOffset: float
    CanHaveAnnotationCrop: bool
    IsSplitVertically: bool
    IsSplitHorizontally: bool
    NumberOfSplitRegions: int
    ShapeSet: bool
    Split: bool
    CanBeSplit: bool
    CanHaveShape: bool
    def Dispose(self, ) -> None: ...
    def GetAnnotationCropShape(self, ) -> CurveLoop: ...
    def GetCropShape(self, ) -> IList: ...
    def GetSplitRegionMaximum(self, regionIndex: int) -> float: ...
    def GetSplitRegionMinimum(self, regionIndex: int) -> float: ...
    def GetSplitRegionOffset(self, regionIndex: int) -> XYZ: ...
    def IsCropRegionShapeValid(self, boundary: CurveLoop) -> bool: ...
    def RemoveCropRegionShape(self, ) -> None: ...
    def RemoveSplit(self, ) -> None: ...
    def RemoveSplitRegion(self, regionIndex: int) -> None: ...
    def SetCropShape(self, boundary: CurveLoop) -> None: ...
    def SplitRegionHorizontally(self, regionIndex: int, leftPart: float, rightPart: float) -> None: ...
    def SplitRegionVertically(self, regionIndex: int, topPart: float, bottomPart: float) -> None: ...

class ViewDetailLevel:
    """.NET: Autodesk.Revit.DB.ViewDetailLevel"""
    def __init__(self, *args) -> None: ...
    ...

class ViewDiscipline:
    """.NET: Autodesk.Revit.DB.ViewDiscipline"""
    def __init__(self, *args) -> None: ...
    ...

class ViewDisplayBackground:
    """.NET: Autodesk.Revit.DB.ViewDisplayBackground"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    VerticalImageScale: float
    HorizontalImageScale: float
    VerticalImageOffset: float
    HorizontalImageOffset: float
    ImageFlags: ViewDisplayBackgroundImageFlags
    ImagePath: str
    SkyColor: Color
    BackgroundColor: Color
    GroundColor: Color
    Type: ViewDisplayBackgroundType
    @staticmethod
    def CreateGradient(skyColor: Color, horizonColor: Color, groundColor: Color) -> ViewDisplayBackground: ...
    @staticmethod
    def CreateImage(imagePath: str, flags: ViewDisplayBackgroundImageFlags, imageOffsets: UV, imageScales: UV) -> ViewDisplayBackground: ...
    @staticmethod
    def CreateSky() -> ViewDisplayBackground: ...
    def Dispose(self, ) -> None: ...

class ViewDisplayBackgroundImageFlags:
    """.NET: Autodesk.Revit.DB.ViewDisplayBackgroundImageFlags"""
    def __init__(self, *args) -> None: ...
    ...

class ViewDisplayBackgroundType:
    """.NET: Autodesk.Revit.DB.ViewDisplayBackgroundType"""
    def __init__(self, *args) -> None: ...
    ...

class ViewDisplayDepthCueing:
    """.NET: Autodesk.Revit.DB.ViewDisplayDepthCueing"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    FadeTo: int
    EndPercentage: int
    StartPercentage: int
    EnableDepthCueing: bool
    def Dispose(self, ) -> None: ...
    def SetStartEndPercentages(self, startPercentage: int, endPercentage: int) -> None: ...

class ViewDisplayEdges:
    """.NET: Autodesk.Revit.DB.ViewDisplayEdges"""
    def __init__(self, *args) -> None: ...
    ...

class ViewDisplayModel:
    """.NET: Autodesk.Revit.DB.ViewDisplayModel"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    SmoothEdges: bool
    ShowHiddenLines: ShowHiddenLinesValues
    SilhouetteEdgesGStyleId: ElementId
    EnableSilhouettes: bool
    Transparency: int
    def Dispose(self, ) -> None: ...

class ViewDisplaySketchyLines:
    """.NET: Autodesk.Revit.DB.ViewDisplaySketchyLines"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Extension: int
    EnableSketchyLines: bool
    Jitter: int
    def Dispose(self, ) -> None: ...

class ViewDrafting(View):
    """.NET: Autodesk.Revit.DB.ViewDrafting"""
    def __init__(self, *args) -> None: ...
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
    @staticmethod
    def Create(document: Document, viewFamilyTypeId: ElementId) -> ViewDrafting: ...

class ViewDuplicateOption:
    """.NET: Autodesk.Revit.DB.ViewDuplicateOption"""
    def __init__(self, *args) -> None: ...
    ...

class ViewFamily:
    """.NET: Autodesk.Revit.DB.ViewFamily"""
    def __init__(self, *args) -> None: ...
    ...

class ViewFamilyType(ElementType):
    """.NET: Autodesk.Revit.DB.ViewFamilyType"""
    def __init__(self, *args) -> None: ...
    ViewFamily: ViewFamily
    DefaultTemplateId: ElementId
    PlanViewDirection: PlanViewDirection
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
    def IsValidDefaultTemplate(self, templateId: ElementId) -> bool: ...

class ViewNavigationToolSettings(Element):
    """.NET: Autodesk.Revit.DB.ViewNavigationToolSettings"""
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
    def GetHomeCamera(self, ) -> HomeCamera: ...
    @staticmethod
    def GetViewNavigationToolSettings(pADoc: Document) -> ViewNavigationToolSettings: ...
    def IsHomeCameraSet(self, ) -> bool: ...

class ViewNode(RenderNode):
    """.NET: Autodesk.Revit.DB.ViewNode"""
    def __init__(self, *args) -> None: ...
    ViewId: ElementId
    LevelOfDetail: int
    IsValidObject: bool
    NodeName: str
    def GetCameraInfo(self, ) -> CameraInfo: ...

class ViewOrientation3D:
    """.NET: Autodesk.Revit.DB.ViewOrientation3D"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ForwardDirection: XYZ
    UpDirection: XYZ
    EyePosition: XYZ
    def Dispose(self, ) -> None: ...

class ViewPlacementOnSheetStatus:
    """.NET: Autodesk.Revit.DB.ViewPlacementOnSheetStatus"""
    def __init__(self, *args) -> None: ...
    ...

class ViewPlan(View):
    """.NET: Autodesk.Revit.DB.ViewPlan"""
    def __init__(self, *args) -> None: ...
    AreaScheme: AreaScheme
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
    def CheckPlanViewRangeValidity(self, planViewRange: PlanViewRange) -> IList: ...
    @staticmethod
    def Create(document: Document, viewFamilyTypeId: ElementId, levelId: ElementId) -> ViewPlan: ...
    @staticmethod
    def CreateAreaPlan(document: Document, areaSchemeId: ElementId, levelId: ElementId) -> ViewPlan: ...
    def GetUnderlayBaseLevel(self, ) -> ElementId: ...
    def GetUnderlayOrientation(self, ) -> UnderlayOrientation: ...
    def GetUnderlayTopLevel(self, ) -> ElementId: ...
    def GetViewRange(self, ) -> PlanViewRange: ...
    def SetUnderlayBaseLevel(self, levelId: ElementId) -> None: ...
    def SetUnderlayOrientation(self, uo: UnderlayOrientation) -> None: ...
    def SetUnderlayRange(self, baseLevelId: ElementId, topLevelId: ElementId) -> None: ...
    def SetViewRange(self, planViewRange: PlanViewRange) -> None: ...

class ViewPlanType:
    """.NET: Autodesk.Revit.DB.ViewPlanType"""
    def __init__(self, *args) -> None: ...
    ...

class ViewPosition(Element):
    """.NET: Autodesk.Revit.DB.ViewPosition"""
    def __init__(self, *args) -> None: ...
    ViewAnchor: ViewAnchor
    Position: XYZ
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
    def Create(document: Document, name: str, position: XYZ, viewAnchor: ViewAnchor) -> ViewPosition: ...
    def GetPlacedViewportIdsForViewPosition(self, ) -> IList: ...

class ViewSchedule(TableView):
    """.NET: Autodesk.Revit.DB.ViewSchedule"""
    def __init__(self, *args) -> None: ...
    IsInternalKeynoteSchedule: bool
    IsTitleblockRevisionSchedule: bool
    IsHeaderFrozen: bool
    UseStripedRowsOnSheets: bool
    HasStripedRows: bool
    RowHeightOverride: RowHeightOverrideOptions
    RowHeight: float
    KeyScheduleParameterName: str
    EmbeddedDefinition: ScheduleDefinition
    Definition: ScheduleDefinition
    BodyTextTypeId: ElementId
    HeaderTextTypeId: ElementId
    TitleTextTypeId: ElementId
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
    def CanGroupHeaders(self, top: int, left: int, bottom: int, right: int) -> bool: ...
    def CanUngroupHeaders(self, top: int, left: int, bottom: int, right: int) -> bool: ...
    @staticmethod
    def CreateKeySchedule(document: Document, categoryId: ElementId) -> ViewSchedule: ...
    @staticmethod
    def CreateKeynoteLegend(document: Document) -> ViewSchedule: ...
    @staticmethod
    def CreateMaterialTakeoff(document: Document, categoryId: ElementId) -> ViewSchedule: ...
    @staticmethod
    def CreateNoteBlock(document: Document, familyId: ElementId) -> ViewSchedule: ...
    @staticmethod
    def CreateRevisionSchedule(document: Document) -> ViewSchedule: ...
    @staticmethod
    def CreateSchedule(document: Document, categoryId: ElementId, areaSchemeId: ElementId) -> ViewSchedule: ...
    @staticmethod
    def CreateSheetList(document: Document) -> ViewSchedule: ...
    @staticmethod
    def CreateViewList(document: Document) -> ViewSchedule: ...
    def DeleteSegment(self, segmentIndex: int) -> None: ...
    def Export(self, folder: str, name: str, options: ViewScheduleExportOptions) -> None: ...
    @staticmethod
    def GetDefaultNameForKeySchedule(document: Document, categoryId: ElementId) -> str: ...
    @staticmethod
    def GetDefaultNameForKeynoteLegend(document: Document) -> str: ...
    @staticmethod
    def GetDefaultNameForMaterialTakeoff(document: Document, categoryId: ElementId) -> str: ...
    @staticmethod
    def GetDefaultNameForNoteBlock(document: Document) -> str: ...
    @staticmethod
    def GetDefaultNameForRevisionSchedule(document: Document) -> str: ...
    @staticmethod
    def GetDefaultNameForSchedule(document: Document, categoryId: ElementId, areaSchemeId: ElementId) -> str: ...
    @staticmethod
    def GetDefaultNameForSheetList(document: Document) -> str: ...
    @staticmethod
    def GetDefaultNameForViewList(document: Document) -> str: ...
    @staticmethod
    def GetDefaultParameterNameForKeySchedule(document: Document, categoryId: ElementId) -> str: ...
    def GetScheduleHeightsOnSheet(self, ) -> ScheduleHeightsOnSheet: ...
    def GetScheduleInstances(self, segmentIndex: int) -> IList: ...
    def GetSegmentCount(self, ) -> int: ...
    def GetSegmentHeight(self, segmentIndex: int) -> float: ...
    def GetStripedRowsColor(self, index: StripedRowPattern) -> Color: ...
    def GetTableData(self, ) -> TableData: ...
    @staticmethod
    def GetValidCategoriesForKeySchedule() -> ICollection: ...
    @staticmethod
    def GetValidCategoriesForMaterialTakeoff() -> ICollection: ...
    @staticmethod
    def GetValidCategoriesForSchedule() -> ICollection: ...
    @staticmethod
    def GetValidFamiliesForNoteBlock(document: Document) -> ICollection: ...
    def GroupHeaders(self, top: int, left: int, bottom: int, right: int, caption: str) -> None: ...
    def HasImageField(self, ) -> bool: ...
    def IsDataOutOfDate(self, ) -> bool: ...
    def IsSplit(self, ) -> bool: ...
    @staticmethod
    def IsValidCategoryForKeySchedule(categoryId: ElementId) -> bool: ...
    @staticmethod
    def IsValidCategoryForMaterialTakeoff(categoryId: ElementId) -> bool: ...
    @staticmethod
    def IsValidCategoryForSchedule(categoryId: ElementId) -> bool: ...
    @staticmethod
    def IsValidFamilyForNoteBlock(document: Document, familyId: ElementId) -> bool: ...
    def IsValidTextTypeId(self, textTypeId: ElementId) -> bool: ...
    def MergeSegments(self, movedSegmentIndex: int, targetSegmentIndex: int) -> None: ...
    def RefreshData(self, ) -> bool: ...
    def RestoreImageSize(self, ) -> None: ...
    def SetSegmentHeight(self, segmentIndex: int, height: float) -> None: ...
    def SetStripedRowsColor(self, index: StripedRowPattern, color: Color) -> None: ...
    def Split(self, segmentHeights: IList) -> None: ...
    def SplitSegment(self, segmentIndex: int, segmentHeights: IList) -> None: ...
    def UngroupHeaders(self, top: int, left: int, bottom: int, right: int) -> None: ...

class ViewScheduleExportOptions:
    """.NET: Autodesk.Revit.DB.ViewScheduleExportOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Title: bool
    HeadersFootersBlanks: bool
    FieldDelimiter: str
    ColumnHeaders: ExportColumnHeaders
    TextQualifier: ExportTextQualifier
    def Dispose(self, ) -> None: ...

class ViewSection(View):
    """.NET: Autodesk.Revit.DB.ViewSection"""
    def __init__(self, *args) -> None: ...
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
    @staticmethod
    def CreateCallout(document: Document, parentViewId: ElementId, viewFamilyTypeId: ElementId, point1: XYZ, point2: XYZ) -> View: ...
    @staticmethod
    def CreateDetail(document: Document, viewFamilyTypeId: ElementId, sectionBox: BoundingBoxXYZ) -> ViewSection: ...
    @staticmethod
    def CreateReferenceCallout(document: Document, parentViewId: ElementId, viewIdToReference: ElementId, point1: XYZ, point2: XYZ) -> None: ...
    @staticmethod
    def CreateReferenceSection(document: Document, parentViewId: ElementId, viewIdToReference: ElementId, headPoint: XYZ, tailPoint: XYZ) -> None: ...
    @staticmethod
    def CreateSection(document: Document, viewFamilyTypeId: ElementId, sectionBox: BoundingBoxXYZ) -> ViewSection: ...
    @staticmethod
    def IsParentViewValidForCallout(document: Document, parentViewId: ElementId) -> bool: ...
    def IsSplitSection(self, ) -> bool: ...
    @staticmethod
    def IsViewFamilyTypeValidForCallout(document: Document, viewFamilyTypeId: ElementId, parentViewId: ElementId) -> bool: ...

class ViewSet(APIObject):
    """.NET: Autodesk.Revit.DB.ViewSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: View) -> bool: ...
    def Erase(self, item: View) -> int: ...
    def ForwardIterator(self, ) -> ViewSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: View) -> bool: ...
    def ReverseIterator(self, ) -> ViewSetIterator: ...

class ViewSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.ViewSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ViewShapeBuilder(ShapeBuilder):
    """.NET: Autodesk.Revit.DB.ViewShapeBuilder"""
    def __init__(self, *args) -> None: ...
    ViewType: DirectShapeTargetViewType
    ViewNormal: XYZ
    IsValidObject: bool
    def AddCurve(self, GCurve: Curve) -> None: ...
    def Reset(self, ) -> None: ...
    @staticmethod
    def ValidateCurve(GCurve: Curve, targetViewType: DirectShapeTargetViewType) -> bool: ...
    @staticmethod
    def ValidateShape(shape: IList, targetViewType: DirectShapeTargetViewType) -> bool: ...
    @staticmethod
    def ValidateViewType(targetViewType: DirectShapeTargetViewType) -> bool: ...

class ViewSheet(View):
    """.NET: Autodesk.Revit.DB.ViewSheet"""
    def __init__(self, *args) -> None: ...
    SheetTitleBlockId: ElementId
    SheetCollectionId: ElementId
    IsPlaceholder: bool
    SheetNumber: str
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
    def CanBeDuplicated(self, duplicateOption: SheetDuplicateOption) -> bool: ...
    def ConvertToRealSheet(self, titleBlockTypeId: ElementId) -> None: ...
    @staticmethod
    def Create(document: Document, titleBlockTypeId: ElementId) -> ViewSheet: ...
    @staticmethod
    def CreatePlaceholder(aDoc: Document) -> ViewSheet: ...
    def DeleteViewport(self, viewport: Viewport) -> None: ...
    def Duplicate(self, duplicateOption: SheetDuplicateOption) -> ElementId: ...
    def GetAdditionalRevisionIds(self, ) -> ICollection: ...
    def GetAllPlacedViews(self, ) -> ISet: ...
    def GetAllRevisionCloudIds(self, ) -> ISet: ...
    def GetAllRevisionIds(self, ) -> IList: ...
    def GetAllViewports(self, ) -> ICollection: ...
    def GetCurrentRevision(self, ) -> ElementId: ...
    def GetRevisionCloudNumberOnSheet(self, revisionCloudId: ElementId) -> str: ...
    def GetRevisionNumberOnSheet(self, revisionId: ElementId) -> str: ...
    def SetAdditionalRevisionIds(self, projectRevisionIds: ICollection) -> None: ...

class ViewSheetSet(Element):
    """.NET: Autodesk.Revit.DB.ViewSheetSet"""
    def __init__(self, *args) -> None: ...
    IsAutomatic: bool
    ViewOrganizationId: ElementId
    SheetOrganizationId: ElementId
    OrderedViewList: IReadOnlyList
    Views: ViewSet
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

class ViewSheetSetting(APIObject):
    """.NET: Autodesk.Revit.DB.ViewSheetSetting"""
    def __init__(self, *args) -> None: ...
    InSession: InSessionViewSheetSet
    AvailableViews: ViewSet
    CurrentViewSheetSet: IViewSheetSet
    IsReadOnly: bool
    def Delete(self, ) -> bool: ...
    def Rename(self, newName: str) -> bool: ...
    def Revert(self, ) -> None: ...
    def Save(self, ) -> bool: ...
    def SaveAs(self, newName: str) -> bool: ...

class ViewTemplateApplicationOption:
    """.NET: Autodesk.Revit.DB.ViewTemplateApplicationOption"""
    def __init__(self, *args) -> None: ...
    ...

class ViewType:
    """.NET: Autodesk.Revit.DB.ViewType"""
    def __init__(self, *args) -> None: ...
    ...

class Viewport(Element):
    """.NET: Autodesk.Revit.DB.Viewport"""
    def __init__(self, *args) -> None: ...
    LabelOffset: XYZ
    LabelLineLength: float
    Rotation: ViewportRotation
    SheetId: ElementId
    ViewId: ElementId
    ViewAnchor: ViewAnchor
    ViewPosition: XYZ
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
    def CanAddViewToSheet(document: Document, viewSheetId: ElementId, viewId: ElementId) -> bool: ...
    @staticmethod
    def Create(document: Document, viewSheetId: ElementId, viewId: ElementId, point: XYZ) -> Viewport: ...
    def GetBoxCenter(self, ) -> XYZ: ...
    def GetBoxOutline(self, ) -> Outline: ...
    def GetLabelOutline(self, ) -> Outline: ...
    def GetPositionAtViewAnchor(self, viewAnchor: ViewAnchor) -> XYZ: ...
    def GetProjectionToSheetTransform(self, ) -> Transform: ...
    def HasViewportTransforms(self, ) -> bool: ...
    def IsViewIdValidForViewport(self, viewId: ElementId) -> bool: ...
    def SetBoxCenter(self, newCenterPoint: XYZ) -> None: ...
    def SetViewAnchorAndPosition(self, viewAnchor: ViewAnchor, position: XYZ) -> None: ...

class ViewportRotation:
    """.NET: Autodesk.Revit.DB.ViewportRotation"""
    def __init__(self, *args) -> None: ...
    ...

class VirtualPrinterType:
    """.NET: Autodesk.Revit.DB.VirtualPrinterType"""
    def __init__(self, *args) -> None: ...
    ...

class Visibility:
    """.NET: Autodesk.Revit.DB.Visibility"""
    def __init__(self, *args) -> None: ...
    ...

class VisibleInViewFilter(ElementQuickFilter):
    """.NET: Autodesk.Revit.DB.VisibleInViewFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Inverted: bool

class Wall(HostObject):
    """.NET: Autodesk.Revit.DB.Wall"""
    def __init__(self, *args) -> None: ...
    Orientation: XYZ
    CrossSection: WallCrossSection
    StackedWallOwnerId: ElementId
    IsStackedWallMember: bool
    IsStackedWall: bool
    Flipped: bool
    StructuralUsage: StructuralWallUsage
    Width: float
    WallType: WallType
    SketchId: ElementId
    CurtainGrid: CurtainGrid
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
    def AddAttachment(self, targetId: ElementId, attachmentLocation: AttachmentLocation) -> None: ...
    def AllowWrappingAtLocation(self, locationIndex: int) -> None: ...
    def CanHaveProfileSketch(self, ) -> bool: ...
    def CanSetHostWall(self, hostWallId: ElementId) -> bool: ...
    @staticmethod
    def Create(document: Document, curve: Curve, wallTypeId: ElementId, levelId: ElementId, height: float, offset: float, flip: bool, structural: bool) -> Wall: ...
    def CreateProfileSketch(self, ) -> Sketch: ...
    def DisallowWrappingAtLocation(self, locationIndex: int) -> None: ...
    def Flip(self, ) -> None: ...
    def GetAttachmentIds(self, attachmentLocation: AttachmentLocation) -> IList: ...
    def GetHostWallId(self, ) -> ElementId: ...
    def GetStackedWallMemberIds(self, ) -> IList: ...
    def GetValidWrappingLocationIndices(self, ) -> IList: ...
    def GetWrappingLocationAsCurveParameter(self, locationIndex: int) -> float: ...
    def GetWrappingLocationAsReferences(self, locationIndex: int) -> IList: ...
    @staticmethod
    def IsValidTargetAttachment(doc: Document, targetId: ElementId) -> bool: ...
    def IsWallCrossSectionValid(self, wallCrossSection: WallCrossSection) -> bool: ...
    def IsWrappingAtLocationAllowed(self, locationIndex: int) -> bool: ...
    def RemoveAttachment(self, targetId: ElementId, attachmentLocation: AttachmentLocation) -> None: ...
    def RemoveProfileSketch(self, ) -> None: ...
    def SetHostWallId(self, hostWallId: ElementId) -> None: ...

class WallCrossSection:
    """.NET: Autodesk.Revit.DB.WallCrossSection"""
    def __init__(self, *args) -> None: ...
    ...

class WallFoundation(HostObject):
    """.NET: Autodesk.Revit.DB.WallFoundation"""
    def __init__(self, *args) -> None: ...
    WallId: ElementId
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
    def Create(document: Document, typeId: ElementId, wallId: ElementId) -> WallFoundation: ...

class WallFoundationType(HostObjAttributes):
    """.NET: Autodesk.Revit.DB.WallFoundationType"""
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

class WallFunction:
    """.NET: Autodesk.Revit.DB.WallFunction"""
    def __init__(self, *args) -> None: ...
    ...

class WallKind:
    """.NET: Autodesk.Revit.DB.WallKind"""
    def __init__(self, *args) -> None: ...
    ...

class WallLocationLine:
    """.NET: Autodesk.Revit.DB.WallLocationLine"""
    def __init__(self, *args) -> None: ...
    ...

class WallSide:
    """.NET: Autodesk.Revit.DB.WallSide"""
    def __init__(self, *args) -> None: ...
    ...

class WallSweep(HostObject):
    """.NET: Autodesk.Revit.DB.WallSweep"""
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
    def Create(wall: Wall, wallSweepType: ElementId, wallSweepInfo: WallSweepInfo) -> WallSweep: ...
    def GetHostIds(self, ) -> IList: ...
    def GetWallSweepInfo(self, ) -> WallSweepInfo: ...
    @staticmethod
    def WallAllowsWallSweep(wall: Wall) -> bool: ...

class WallSweepInfo:
    """.NET: Autodesk.Revit.DB.WallSweepInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsFixed: bool
    IsVertical: bool
    CutsWall: bool
    IsCutByInserts: bool
    IsProfileFlipped: bool
    WallSweepOrientation: WallSweepOrientation
    DistanceMeasuredFrom: DistanceMeasuredFrom
    WallSweepType: WallSweepType
    WallSide: WallSide
    Id: int
    MaterialId: ElementId
    ProfileId: ElementId
    DefaultSetback: float
    WallOffset: float
    Distance: float
    def Dispose(self, ) -> None: ...
    def IsEqual(self, toCompare: WallSweepInfo) -> bool: ...

class WallSweepOrientation:
    """.NET: Autodesk.Revit.DB.WallSweepOrientation"""
    def __init__(self, *args) -> None: ...
    ...

class WallSweepType:
    """.NET: Autodesk.Revit.DB.WallSweepType"""
    def __init__(self, *args) -> None: ...
    ...

class WallType(HostObjAttributes):
    """.NET: Autodesk.Revit.DB.WallType"""
    def __init__(self, *args) -> None: ...
    Width: float
    Kind: WallKind
    ThermalProperties: ThermalProperties
    Function: WallFunction
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

class WallUtils:
    """.NET: Autodesk.Revit.DB.WallUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def AllowWallJoinAtEnd(wall: Wall, end: int) -> None: ...
    @staticmethod
    def DisallowWallJoinAtEnd(wall: Wall, end: int) -> None: ...
    @staticmethod
    def IsWallJoinAllowedAtEnd(wall: Wall, end: int) -> bool: ...

class WidthMeasuredAt:
    """.NET: Autodesk.Revit.DB.WidthMeasuredAt"""
    def __init__(self, *args) -> None: ...
    ...

class WireframeBuilder(ShapeBuilder):
    """.NET: Autodesk.Revit.DB.WireframeBuilder"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def AddCurve(self, GCurve: Curve) -> None: ...
    def AddPoint(self, GPoint: Point) -> None: ...
    def Reset(self, ) -> None: ...
    @staticmethod
    def ValidateCurve(GCurve: Curve) -> bool: ...
    @staticmethod
    def ValidatePoint(GPoint: Point) -> bool: ...

class Workset(WorksetPreview):
    """.NET: Autodesk.Revit.DB.Workset"""
    def __init__(self, *args) -> None: ...
    IsVisibleByDefault: bool
    IsEditable: bool
    IsOpen: bool
    Kind: WorksetKind
    IsValidObject: bool
    IsDefaultWorkset: bool
    Owner: str
    Name: str
    UniqueId: Guid
    Id: WorksetId
    @staticmethod
    def Create(document: Document, name: str) -> Workset: ...

class WorksetConfiguration:
    """.NET: Autodesk.Revit.DB.WorksetConfiguration"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Close(self, worksetsToClose: IList) -> None: ...
    def Dispose(self, ) -> None: ...
    def Open(self, worksetsToOpen: IList) -> None: ...

class WorksetConfigurationOption:
    """.NET: Autodesk.Revit.DB.WorksetConfigurationOption"""
    def __init__(self, *args) -> None: ...
    ...

class WorksetDefaultVisibilitySettings(Element):
    """.NET: Autodesk.Revit.DB.WorksetDefaultVisibilitySettings"""
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
    def GetWorksetDefaultVisibilitySettings(aDoc: Document) -> WorksetDefaultVisibilitySettings: ...
    def IsWorksetVisible(self, worksetId: WorksetId) -> bool: ...
    def SetWorksetVisibility(self, worksetId: WorksetId, visible: bool) -> None: ...

class WorksetFilter:
    """.NET: Autodesk.Revit.DB.WorksetFilter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IncludeStandaloneWorksetsOnly: bool
    Inverted: bool
    def Dispose(self, ) -> None: ...

class WorksetId:
    """.NET: Autodesk.Revit.DB.WorksetId"""
    def __init__(self, *args) -> None: ...
    InvalidWorksetId: WorksetId
    IntegerValue: int
    def Compare(self, id: WorksetId) -> int: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, ) -> str: ...

class WorksetKind:
    """.NET: Autodesk.Revit.DB.WorksetKind"""
    def __init__(self, *args) -> None: ...
    ...

class WorksetKindFilter(WorksetFilter):
    """.NET: Autodesk.Revit.DB.WorksetKindFilter"""
    def __init__(self, *args) -> None: ...
    WorksetKind: WorksetKind
    IsValidObject: bool
    IncludeStandaloneWorksetsOnly: bool
    Inverted: bool

class WorksetPreview:
    """.NET: Autodesk.Revit.DB.WorksetPreview"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsDefaultWorkset: bool
    Owner: str
    Name: str
    UniqueId: Guid
    Id: WorksetId
    def Dispose(self, ) -> None: ...

class WorksetTable:
    """.NET: Autodesk.Revit.DB.WorksetTable"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    @staticmethod
    def CanDeleteWorkset(document: Document, worksetId: WorksetId, deleteWorksetSettings: DeleteWorksetSettings) -> bool: ...
    @staticmethod
    def DeleteWorkset(document: Document, worksetId: WorksetId, deleteWorksetSettings: DeleteWorksetSettings) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetActiveWorksetId(self, ) -> WorksetId: ...
    def GetWorkset(self, guid: Guid) -> Workset: ...
    @staticmethod
    def IsWorksetNameUnique(aDoc: Document, name: str) -> bool: ...
    @staticmethod
    def RenameWorkset(aDoc: Document, worksetId: WorksetId, name: str) -> None: ...
    def SetActiveWorksetId(self, worksetId: WorksetId) -> None: ...

class WorksetVisibility:
    """.NET: Autodesk.Revit.DB.WorksetVisibility"""
    def __init__(self, *args) -> None: ...
    ...

class WorksharingDisplayGraphicSettings:
    """.NET: Autodesk.Revit.DB.WorksharingDisplayGraphicSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    FillColor: Color
    LineColor: Color
    IsApplied: bool
    def Dispose(self, ) -> None: ...

class WorksharingDisplayMode:
    """.NET: Autodesk.Revit.DB.WorksharingDisplayMode"""
    def __init__(self, *args) -> None: ...
    ...

class WorksharingDisplaySettings(Element):
    """.NET: Autodesk.Revit.DB.WorksharingDisplaySettings"""
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
    def CanUserHaveOverrides(self, username: str) -> bool: ...
    def GetAllUsersWithGraphicOverrides(self, ) -> ICollection: ...
    def GetGraphicOverrides(self, worksetId: WorksetId) -> WorksharingDisplayGraphicSettings: ...
    @staticmethod
    def GetOrCreateWorksharingDisplaySettings(doc: Document) -> WorksharingDisplaySettings: ...
    def GetRemovedUsers(self, ) -> ICollection: ...
    def RemoveUsers(self, document: Document, usersToRemove: ICollection, usersActuallyRemoved: ICollection) -> None: ...
    def RestoreUsers(self, usersToRestore: ICollection) -> int: ...
    def SetGraphicOverrides(self, worksetId: WorksetId, overrides: WorksharingDisplayGraphicSettings) -> None: ...
    def UserHasGraphicOverrides(self, username: str) -> bool: ...

class WorksharingSaveAsOptions:
    """.NET: Autodesk.Revit.DB.WorksharingSaveAsOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ClearTransmitted: bool
    OpenWorksetsDefault: SimpleWorksetConfiguration
    SaveAsCentral: bool
    def Dispose(self, ) -> None: ...

class WorksharingTooltipInfo:
    """.NET: Autodesk.Revit.DB.WorksharingTooltipInfo"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LastChangedBy: str
    Creator: str
    Owner: str
    def Dispose(self, ) -> None: ...
    def GetRequesters(self, ) -> IList: ...

class WorksharingUtils:
    """.NET: Autodesk.Revit.DB.WorksharingUtils"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    @staticmethod
    def CheckoutElements(document: Document, elementsToCheckout: ISet, options: TransactWithCentralOptions) -> ISet: ...
    @staticmethod
    def CheckoutWorksets(document: Document, worksetsToCheckout: ISet, options: TransactWithCentralOptions) -> ISet: ...
    @staticmethod
    def CreateNewLocal(sourcePath: ModelPath, targetPath: ModelPath) -> None: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetCheckoutStatus(document: Document, elementId: ElementId, owner: str) -> CheckoutStatus: ...
    @staticmethod
    def GetModelUpdatesStatus(document: Document, elementId: ElementId) -> ModelUpdatesStatus: ...
    @staticmethod
    def GetUserWorksetInfo(path: ModelPath) -> IList: ...
    @staticmethod
    def GetWorksharingTooltipInfo(document: Document, elementId: ElementId) -> WorksharingTooltipInfo: ...
    @staticmethod
    def RelinquishOwnership(document: Document, generalCategories: RelinquishOptions, options: TransactWithCentralOptions) -> RelinquishedItems: ...

class XYZ:
    """.NET: Autodesk.Revit.DB.XYZ"""
    def __init__(self, *args) -> None: ...
    BasisZ: XYZ
    BasisY: XYZ
    BasisX: XYZ
    Zero: XYZ
    Item: float
    Z: float
    Y: float
    X: float
    def Add(self, source: XYZ) -> XYZ: ...
    def AngleOnPlaneTo(self, right: XYZ, normal: XYZ) -> float: ...
    def AngleTo(self, source: XYZ) -> float: ...
    def CrossProduct(self, source: XYZ) -> XYZ: ...
    def DistanceTo(self, source: XYZ) -> float: ...
    def Divide(self, value: float) -> XYZ: ...
    def DotProduct(self, source: XYZ) -> float: ...
    def GetLength(self, ) -> float: ...
    def IsAlmostEqualTo(self, source: XYZ, tolerance: float) -> bool: ...
    def IsUnitLength(self, ) -> bool: ...
    @staticmethod
    def IsWithinLengthLimits(point: XYZ) -> bool: ...
    def IsZeroLength(self, ) -> bool: ...
    def Multiply(self, value: float) -> XYZ: ...
    def Negate(self, ) -> XYZ: ...
    def Normalize(self, ) -> XYZ: ...
    def Subtract(self, source: XYZ) -> XYZ: ...
    def ToString(self, ) -> str: ...
    def TripleProduct(self, middle: XYZ, right: XYZ) -> float: ...

class ZoomFitType:
    """.NET: Autodesk.Revit.DB.ZoomFitType"""
    def __init__(self, *args) -> None: ...
    ...

class ZoomType:
    """.NET: Autodesk.Revit.DB.ZoomType"""
    def __init__(self, *args) -> None: ...
    ...
