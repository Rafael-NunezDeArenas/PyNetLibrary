# Auto-generated — Civil 26 — Autodesk.Civil.DatabaseServices

class AdditionalAppliedAssemblyInfo:
    """.NET: Autodesk.Civil.DatabaseServices.AdditionalAppliedAssemblyInfo"""
    def __init__(self, *args) -> None: ...
    Description: str
    Station: float

class Alignment(Feature):
    """.NET: Autodesk.Civil.DatabaseServices.Alignment"""
    def __init__(self, *args) -> None: ...
    CANTCriticalStaitons: CANTCriticalStationCollection
    CANTCurves: CANTCurveCollection
    SuperelevationCriticalStations: SuperelevationCriticalStationCollection
    SuperelevationCurves: SuperelevationCurveCollection
    ConnectedAlignmentInfo: ConnectedAlignmentInfo
    IsConnectedAlignment: bool
    HasRoundabout: bool
    IsOffsetAlignment: bool
    OffsetAlignmentInfo: OffsetAlignmentInfo
    RailAlignmentInfo: RailAlignmentInfo
    CreationMode: AlignmentCreationType
    SuperelevationType: SuperelevationType
    AlignmentType: AlignmentType
    UpdateMode: AlignmentUpdateType
    StyleId: ObjectId
    StyleName: str
    StationIndexIncrement: float
    ReferencePointStation: float
    ReferencePoint: Point2d
    SiteName: str
    SiteId: ObjectId
    IsSiteless: bool
    Length: float
    UseDesignSpeed: bool
    CriteriaFileName: str
    UseDesignCriteriaFile: bool
    DesignCheckSetName: str
    DesignCheckSetId: ObjectId
    UseDesignCheckSet: bool
    EndingStationWithEquations: float
    EndingStation: float
    StartingStation: float
    StationEquations: StationEquationCollection
    DesignSpeeds: DesignSpeedCollection
    Entities: AlignmentEntityCollection
    IsEditable: bool
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CopyToSameSite(self, ) -> None: ...
    def CopyToSite(self, siteName: str) -> None: ...
    @staticmethod
    def Create(document: CivilDocument, alignmentName: str, siteId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId, type: AlignmentType) -> ObjectId: ...
    @staticmethod
    def CreateConnectedAlignment(alignmentName: str, siteId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId, connectedAlignmentParams: ConnectedAlignmentParams) -> ObjectId: ...
    @staticmethod
    def CreateOffsetAlignment(database: Database, alignmentName: str, parentAlignmentName: str, offset: float, styleName: str, startStation: float, endStation: float) -> ObjectId: ...
    def DistanceToAlignment(self, stationOnThisAlignment: float, otherAlignment: Alignment, enumSide: AlignmentSide, distanceToOtherAlignment: float, stationOnOtherAlignment: float) -> None: ...
    def GetAlignmentLabelGroupIds(self, ) -> ObjectIdCollection: ...
    def GetAlignmentLabelIds(self, ) -> ObjectIdCollection: ...
    def GetChildOffsetAlignmentIds(self, onlyDynamicUpdate: bool) -> ObjectIdCollection: ...
    def GetCrossSlopeAtStation(self, station: float, crossSegmentType: SuperelevationCrossSegmentType, applySmoothing: bool) -> float: ...
    def GetInstantaneousRadius(self, rawStation: float) -> float: ...
    def GetLabelGroupIds(self, ) -> ObjectIdCollection: ...
    def GetLabelIds(self, ) -> ObjectIdCollection: ...
    @staticmethod
    def GetNextUniqueName(alignmentName: str) -> str: ...
    def GetPolyline(self, ) -> ObjectId: ...
    def GetProfileIds(self, ) -> ObjectIdCollection: ...
    def GetProfileViewIds(self, ) -> ObjectIdCollection: ...
    def GetRegions(self, ) -> AlignmentRegionCollection: ...
    def GetSampleLineGroupIds(self, ) -> ObjectIdCollection: ...
    def GetStationSet(self, stationType: StationTypes, majorInterval: float, minorInterval: float, startStation: float, endStation: float) -> list: ...
    def GetStationStringWithEquations(self, rawStation: float) -> str: ...
    def GetSuperelevationViewIds(self, ) -> ObjectIdCollection: ...
    def ImportLabelSet(self, labelSetStyleName: str) -> None: ...
    def PointLocation(self, station: float, offset: float, tolerance: float, easting: float, northing: float, Bearing: float) -> None: ...
    def RenumerateTags(self, ) -> None: ...
    def Reverse(self, ) -> None: ...
    def StationOffset(self, easting: float, northing: float, tolerance: float, station: float, offset: float) -> None: ...
    def StationOffsetAcceptOutOfRange(self, easting: float, northing: float, tolerance: float, station: float, offset: float, outofrange: bool) -> None: ...
    def TrackDistanceToAlignment(self, startStationOnThisAlignment: float, endStationOnThisAlignment: float, gaugeForThisAlignment: Nullable, otherAlignmentId: ObjectId, gaugeForOtherAlignment: Nullable, trackDistanceCalculationMode: TrackDistanceCalculationMode) -> AlignmentTrackDistanceData: ...
    def Update(self, ) -> None: ...

class AlignmentArc(AlignmentCurve):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentArc"""
    def __init__(self, *args) -> None: ...
    MinimumRadius: float
    CurveGroupSubEntityIndex: str
    CurveGroupIndex: str
    Clockwise: bool
    ReverseCurve: bool
    DeflectedAngle: float
    GreaterThan180: bool
    PIStation: float
    DirectionAtPoint2: float
    DirectionAtPoint1: float
    PassThroughPoint3: Point2d
    PassThroughPoint2: Point2d
    PassThroughPoint1: Point2d
    MidOrdinate: float
    ExternalTangent: float
    ExternalSecant: float
    ChordDirection: float
    ChordLength: float
    Delta: float
    EndDirection: float
    StartDirection: float
    Radius: float
    CenterPoint: Point2d
    Length: float
    Constraint2: AlignmentArcConstraintType
    Item: AlignmentSubEntity
    HighestDesignSpeed: float
    EndStation: float
    StartStation: float
    EndPoint: Point2d
    StartPoint: Point2d
    EntityId: int
    Constraint1: AlignmentEntityConstraintType
    EntityType: AlignmentEntityType
    SubEntityCount: int
    EntityAfter: int
    EntityBefore: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AlignmentArcConstraintType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentArcConstraintType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentCCRC(AlignmentCurve):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentCCRC"""
    def __init__(self, *args) -> None: ...
    Arc3: AlignmentSubEntityArc
    Arc2: AlignmentSubEntityArc
    Arc1: AlignmentSubEntityArc
    Constraint2: AlignmentCCRCConstraintType
    HighestDesignSpeed: float
    EndStation: float
    StartStation: float
    EndPoint: Point2d
    StartPoint: Point2d
    Length: float
    EntityId: int
    Constraint1: AlignmentEntityConstraintType
    EntityType: AlignmentEntityType
    Item: AlignmentSubEntity
    SubEntityCount: int
    EntityAfter: int
    EntityBefore: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AlignmentCCRCConstraintType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentCCRCConstraintType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentCRC(AlignmentCurve):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentCRC"""
    def __init__(self, *args) -> None: ...
    Arc2: AlignmentSubEntityArc
    Arc1: AlignmentSubEntityArc
    Constraint2: AlignmentCRCConstraintType
    HighestDesignSpeed: float
    EndStation: float
    StartStation: float
    EndPoint: Point2d
    StartPoint: Point2d
    Length: float
    EntityId: int
    Constraint1: AlignmentEntityConstraintType
    EntityType: AlignmentEntityType
    Item: AlignmentSubEntity
    SubEntityCount: int
    EntityAfter: int
    EntityBefore: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AlignmentCRCConstraintType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentCRCConstraintType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentCTC(AlignmentCurve):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentCTC"""
    def __init__(self, *args) -> None: ...
    Arc2: AlignmentSubEntityArc
    Tangent: AlignmentSubEntityLine
    Arc1: AlignmentSubEntityArc
    Constraint2: AlignmentCTCConstraintType
    HighestDesignSpeed: float
    EndStation: float
    StartStation: float
    EndPoint: Point2d
    StartPoint: Point2d
    Length: float
    EntityId: int
    Constraint1: AlignmentEntityConstraintType
    EntityType: AlignmentEntityType
    Item: AlignmentSubEntity
    SubEntityCount: int
    EntityAfter: int
    EntityBefore: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AlignmentCTCConstraintType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentCTCConstraintType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentCantLabelGroup(AlignmentLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentCantLabelGroup"""
    def __init__(self, *args) -> None: ...
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(alignmentId: ObjectId, styleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection: ...
    def GetGeometryPointsOptions(self, ) -> GeometryPointSelector: ...
    def SetGeometryPointsOptions(self, transitionPointsOptions: GeometryPointSelector) -> None: ...

class AlignmentCreationType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentCreationType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentCurve(AlignmentEntity):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentCurve"""
    def __init__(self, *args) -> None: ...
    HighestDesignSpeed: float
    EndStation: float
    StartStation: float
    EndPoint: Point2d
    StartPoint: Point2d
    Length: float
    EntityId: int
    Constraint1: AlignmentEntityConstraintType
    EntityType: AlignmentEntityType
    Item: AlignmentSubEntity
    SubEntityCount: int
    EntityAfter: int
    EntityBefore: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AlignmentCurveLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentCurveLabel"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(subEntityArc: AlignmentSubEntityArc, labelStyleId: ObjectId) -> ObjectId: ...

class AlignmentDesignSpeedLabelGroup(AlignmentLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentDesignSpeedLabelGroup"""
    def __init__(self, *args) -> None: ...
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(styleId: ObjectId, alignmentId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class AlignmentEntity(DisposableWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentEntity"""
    def __init__(self, *args) -> None: ...
    EntityId: int
    Constraint1: AlignmentEntityConstraintType
    EntityType: AlignmentEntityType
    Item: AlignmentSubEntity
    SubEntityCount: int
    EntityAfter: int
    EntityBefore: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DesignChecks(self, ) -> Collection: ...
    def Equals(self, obj: object) -> bool: ...
    def ValidateDesignCheck(self, designCheck: AlignmentDesignCheck) -> bool: ...

class AlignmentEntityCollection(CivilWrapper<AeccDbAlignment>):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentEntityCollection"""
    def __init__(self, *args) -> None: ...
    LastEntity: int
    FirstEntity: int
    Count: int
    Item: AlignmentEntity
    def AddFixedCurve(self, previousEntityId: int, passThroughPoint1: Point3d, passThroughPoint2: Point3d, radius: float, isClockwise: bool, isGreaterThan180: bool) -> AlignmentArc: ...
    def AddFixedLine(self, previousEntityId: int, startPoint: Point3d, endPoint: Point3d) -> AlignmentLine: ...
    def AddFixedSpiral(self, previousEntityId: int, startPoint: Point3d, spiralPI: Point3d, startRadius: float, endRadius: float, length: float, isClockwise: bool, spiralDefinition: SpiralType) -> AlignmentSpiral: ...
    def AddFloatSpiral(self, radius: float, length: float, nextEntityId: int, isClockwise: bool, spiralDefinition: SpiralType) -> AlignmentSpiral: ...
    def AddFloatingArcWithSpiral(self, attachEntityId: int, attachType: EntityAttachType, spParam: float, spType: SpiralParamType, radius: float, arcLength: float, isClockwise: bool, spiralDefinition: SpiralType) -> AlignmentSCS: ...
    def AddFloatingCSS(self, nextEntityId: int, passThroughPoint1: Point3d, passThroughPoint2: Point3d, sp3Param: float, sp4Param: float, spType: SpiralParamType, spiralDefinition: SpiralType) -> AlignmentSSCSS: ...
    def AddFloatingCurve(self, radius: float, paramValue: float, paramType: CurveParamType, isClockwise: bool, nextEntityId: int) -> AlignmentArc: ...
    def AddFloatingLine(self, length: float, nextEntityId: int) -> AlignmentLine: ...
    def AddFloatingLineWithSpiral(self, attachEntityId: int, attachType: EntityAttachType, spParam: float, spType: SpiralParamType, tanLength: float, spiralDefinition: SpiralType) -> AlignmentSTS: ...
    def AddFloatingSSC(self, previousEntityId: int, sp1Param: float, sp2Param: float, spType: SpiralParamType, passThroughPoint1: Point3d, passThroughPoint2: Point3d, spiralDefinition: SpiralType) -> AlignmentSSCSS: ...
    def AddFreeCurve(self, previousEntityId: int, nextEntityId: int, paramValue: float, paramType: CurveParamType, isGreaterThan180: bool, curveType: CurveType) -> AlignmentArc: ...
    def AddFreeLine(self, previousEntityId: int, nextEntityId: int) -> AlignmentLine: ...
    def AddFreeSCS(self, previousEntityId: int, nextEntityId: int, spiral1Param: float, spiral2Param: float, spType: SpiralParamType, radius: float, isGreaterThan180: bool, spiralDefinition: SpiralType) -> AlignmentSCS: ...
    def AddFreeSCSCS(self, previousEntityId: int, nextEntityId: int, constraintValue: SCSCSConstraints, spiralDefinition: SpiralType) -> AlignmentSCSCS: ...
    def AddFreeSCSS(self, previousEntityId: int, nextEntityId: int, sp1Param: float, radius: float, sp3Param: float, sp4Param: float, isGreaterThan180: bool, spiralDefinition: SpiralType) -> AlignmentSSCSS: ...
    def AddFreeSCSSCS(self, previousEntityId: int, nextEntityId: int, constraintValue: SCSSCSConstraints, spiralDefinition: SpiralType) -> AlignmentSCSSCS: ...
    def AddFreeSSBetweenCurves(self, previousEntityId: int, nextEntityId: int, spRatio: float, spType: SpiralParamType, spiralDefinition: SpiralType) -> AlignmentSTS: ...
    def AddFreeSSBetweenTangents(self, previousEntityId: int, nextEntityId: int, spiral1Param: float, spiral2Param: float, spType: SpiralParamType, isGreaterThan180: bool, spiralDefinition: SpiralType) -> AlignmentSCS: ...
    def AddFreeSSCS(self, previousEntityId: int, nextEntityId: int, sp1Param: float, sp2Param: float, radius: float, sp3Param: float, isGreaterThan180: bool, spiralDefinition: SpiralType) -> AlignmentSSCSS: ...
    def AddFreeSSCSS(self, previousEntityId: int, nextEntityId: int, sp1Param: float, sp2Param: float, radius: float, sp3Param: float, sp4Param: float, isGreaterThan180: bool, spiralDefinition: SpiralType) -> AlignmentSSCSS: ...
    def AddFreeSTS(self, previousEntityId: int, nextEntityId: int, sp1Param: float, sp2Param: float, spType: SpiralParamType, spiralDefinition: SpiralType) -> AlignmentSTS: ...
    def AddFreeSpiral(self, previousEntityId: int, nextEntityId: int, spParam: float, spType: SpiralParamType, spiralCurveType: SpiralCurveType, spiralDefinition: SpiralType) -> AlignmentSCS: ...
    def Clear(self, ) -> None: ...
    def EntityAtId(self, id: int) -> AlignmentEntity: ...
    def EntityAtStation(self, rawStation: float) -> AlignmentEntity: ...
    def GetEntityByOrder(self, index: int) -> AlignmentEntity: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, entity: AlignmentEntity) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class AlignmentEntityConstraintType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentEntityConstraintType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentEntityType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentEntityType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentGeometryPointLabelGroup(AlignmentLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentGeometryPointLabelGroup"""
    def __init__(self, *args) -> None: ...
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(styleId: ObjectId, alignmentId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...
    def GetGeometryPointsOptions(self, ) -> GeometryPointSelector: ...
    def SetGeometryPointsOptions(self, alignmentGeometryPoints: GeometryPointSelector) -> None: ...

class AlignmentGeometryPointStationType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentGeometryPointStationType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentIndexedPILabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentIndexedPILabel"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(scs: AlignmentSCS, labelStyleId: ObjectId) -> ObjectId: ...

class AlignmentLabelGroup(AutoFeatureLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentLabelGroup"""
    def __init__(self, *args) -> None: ...
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetAvailableLabelGroupIds(rxClass: RXClass, alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(rxClass: RXClass, alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class AlignmentLine(AlignmentCurve):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentLine"""
    def __init__(self, *args) -> None: ...
    CurveGroupSubEntityIndex: str
    CurveGroupIndex: str
    PassThroughPoint2: Point2d
    PassThroughPoint1: Point2d
    MidPoint: Point2d
    Direction: float
    Constraint2: AlignmentLineConstraintType
    Length: float
    Item: AlignmentSubEntity
    HighestDesignSpeed: float
    EndStation: float
    StartStation: float
    EndPoint: Point2d
    StartPoint: Point2d
    EntityId: int
    Constraint1: AlignmentEntityConstraintType
    EntityType: AlignmentEntityType
    SubEntityCount: int
    EntityAfter: int
    EntityBefore: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AlignmentLineConstraintType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentLineConstraintType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentMinorStationLabelGroup(AlignmentStationLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentMinorStationLabelGroup"""
    def __init__(self, *args) -> None: ...
    RangeEndFromFeature: bool
    RangeEnd: float
    RangeStartFromFeature: bool
    RangeStart: float
    MajorStationLabelGroup: ObjectId
    Increment: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(styleId: ObjectId, majorStationId: ObjectId, increment: float) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...
    def SetRange(self, rangeStart: float, rangeEnd: float) -> None: ...

class AlignmentMultipleSegments(AlignmentCurve):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentMultipleSegments"""
    def __init__(self, *args) -> None: ...
    Constraint2: AlignmentMultipleSegmentsConstraintType
    Item: AlignmentSubEntity
    SubEntityCount: int
    HighestDesignSpeed: float
    EndStation: float
    StartStation: float
    EndPoint: Point2d
    StartPoint: Point2d
    Length: float
    EntityId: int
    Constraint1: AlignmentEntityConstraintType
    EntityType: AlignmentEntityType
    EntityAfter: int
    EntityBefore: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AlignmentMultipleSegmentsConstraintType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentMultipleSegmentsConstraintType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentPILabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentPILabel"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(scs: AlignmentSCS, labelStyleId: ObjectId) -> ObjectId: ...

class AlignmentRegion(CivilWrapper<AeccDbAlignment>):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentRegion"""
    def __init__(self, *args) -> None: ...
    WideningCriteria: OffsetAlignmentWideningCriteria
    RegionType: AlignmentRegionType
    OffsetDist: float
    IncreasedWidth: float
    Offset: float
    Length: float
    EndStation: float
    StartStation: float
    ExitTransition: AlignmentTransition
    EntryTransition: AlignmentTransition
    def Split(self, ) -> None: ...

class AlignmentRegionCollection(CivilWrapper<AeccDbAlignment>):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentRegionCollection"""
    def __init__(self, *args) -> None: ...
    Item: AlignmentRegion
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def MergeToNeighborRegion(self, index: int, preRegion: bool) -> bool: ...
    def Remove(self, index: int) -> None: ...

class AlignmentRegionType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentRegionType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentSCS(AlignmentCurve):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSCS"""
    def __init__(self, *args) -> None: ...
    SpiralOut: AlignmentSubEntitySpiral
    Arc: AlignmentSubEntityArc
    SpiralIn: AlignmentSubEntitySpiral
    GreaterThan180: bool
    Constraint2: AlignmentSCSConstraintType
    HighestDesignSpeed: float
    EndStation: float
    StartStation: float
    EndPoint: Point2d
    StartPoint: Point2d
    Length: float
    EntityId: int
    Constraint1: AlignmentEntityConstraintType
    EntityType: AlignmentEntityType
    Item: AlignmentSubEntity
    SubEntityCount: int
    EntityAfter: int
    EntityBefore: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AlignmentSCSCS(AlignmentCurve):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSCSCS"""
    def __init__(self, *args) -> None: ...
    Spiral3: AlignmentSubEntitySpiral
    Arc2: AlignmentSubEntityArc
    Spiral2: AlignmentSubEntitySpiral
    Arc1: AlignmentSubEntityArc
    Spiral1: AlignmentSubEntitySpiral
    Constraint2: AlignmentSCSCSConstraintType
    HighestDesignSpeed: float
    EndStation: float
    StartStation: float
    EndPoint: Point2d
    StartPoint: Point2d
    Length: float
    EntityId: int
    Constraint1: AlignmentEntityConstraintType
    EntityType: AlignmentEntityType
    Item: AlignmentSubEntity
    SubEntityCount: int
    EntityAfter: int
    EntityBefore: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AlignmentSCSCSConstraintType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSCSCSConstraintType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentSCSConstraintType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSCSConstraintType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentSCSSCS(AlignmentCurve):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSCSSCS"""
    def __init__(self, *args) -> None: ...
    Spiral4: AlignmentSubEntitySpiral
    Arc2: AlignmentSubEntityArc
    Spiral3: AlignmentSubEntitySpiral
    Spiral2: AlignmentSubEntitySpiral
    Arc1: AlignmentSubEntityArc
    Spiral1: AlignmentSubEntitySpiral
    Constraint2: AlignmentSCSSCSConstraintType
    HighestDesignSpeed: float
    EndStation: float
    StartStation: float
    EndPoint: Point2d
    StartPoint: Point2d
    Length: float
    EntityId: int
    Constraint1: AlignmentEntityConstraintType
    EntityType: AlignmentEntityType
    Item: AlignmentSubEntity
    SubEntityCount: int
    EntityAfter: int
    EntityBefore: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AlignmentSCSSCSConstraintType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSCSSCSConstraintType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentSSCSS(AlignmentCurve):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSSCSS"""
    def __init__(self, *args) -> None: ...
    Spiral4: AlignmentSubEntitySpiral
    Spiral3: AlignmentSubEntitySpiral
    Arc: AlignmentSubEntityArc
    Spiral2: AlignmentSubEntitySpiral
    Spiral1: AlignmentSubEntitySpiral
    GreaterThan180: bool
    Constraint2: AlignmentSSCSSConstraintType
    HighestDesignSpeed: float
    EndStation: float
    StartStation: float
    EndPoint: Point2d
    StartPoint: Point2d
    Length: float
    EntityId: int
    Constraint1: AlignmentEntityConstraintType
    EntityType: AlignmentEntityType
    Item: AlignmentSubEntity
    SubEntityCount: int
    EntityAfter: int
    EntityBefore: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AlignmentSSCSSConstraintType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSSCSSConstraintType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentSTS(AlignmentCurve):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSTS"""
    def __init__(self, *args) -> None: ...
    SpiralOut: AlignmentSubEntitySpiral
    Tangent: AlignmentSubEntityLine
    SpiralIn: AlignmentSubEntitySpiral
    Constraint2: AlignmentSTSConstraintType
    HighestDesignSpeed: float
    EndStation: float
    StartStation: float
    EndPoint: Point2d
    StartPoint: Point2d
    Length: float
    EntityId: int
    Constraint1: AlignmentEntityConstraintType
    EntityType: AlignmentEntityType
    Item: AlignmentSubEntity
    SubEntityCount: int
    EntityAfter: int
    EntityBefore: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AlignmentSTSConstraintType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSTSConstraintType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentSide:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSide"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentSpiral(AlignmentCurve):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSpiral"""
    def __init__(self, *args) -> None: ...
    TotalY: float
    TotalX: float
    Direction: SpiralDirectionType
    SPIStation: float
    SpiralDefinition: SpiralType
    Constraint2: AlignmentSpiralConstraintType
    SPIPoint: Point2d
    SPIAngle: float
    ShortTangent: float
    RadiusOut: float
    RadiusIn: float
    RadialPoint: Point2d
    P: float
    MinimumTransitionLength: float
    LongTangent: float
    Length: float
    K: float
    EndDirection: float
    StartDirection: float
    Delta: float
    CurveGroupSubEntityIndex: str
    CurveGroupIndex: str
    CurveType: SpiralCurveType
    Compound: bool
    A: float
    Item: AlignmentSubEntity
    HighestDesignSpeed: float
    EndStation: float
    StartStation: float
    EndPoint: Point2d
    StartPoint: Point2d
    EntityId: int
    Constraint1: AlignmentEntityConstraintType
    EntityType: AlignmentEntityType
    SubEntityCount: int
    EntityAfter: int
    EntityBefore: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AlignmentSpiralConstraintType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSpiralConstraintType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentSpiralLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSpiralLabel"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(subEntitySpiral: AlignmentSubEntitySpiral, labelStyleId: ObjectId) -> ObjectId: ...

class AlignmentStationEquationLabelGroup(AlignmentLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentStationEquationLabelGroup"""
    def __init__(self, *args) -> None: ...
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(styleId: ObjectId, alignmentId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class AlignmentStationLabelGroup(AlignmentLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentStationLabelGroup"""
    def __init__(self, *args) -> None: ...
    RangeEnd: float
    RangeStart: float
    Increment: float
    RangeStartFromFeature: bool
    RangeEndFromFeature: bool
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(styleId: ObjectId, alignmentId: ObjectId, increment: float) -> ObjectId: ...
    @staticmethod
    def CreateMajor(styleId: ObjectId, alignmentId: ObjectId, increment: float) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class AlignmentSubEntity(DisposableWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSubEntity"""
    def __init__(self, *args) -> None: ...
    CurveGroupSubEntityIndex: str
    CurveGroupIndex: str
    EndStation: float
    StartStation: float
    EndPoint: Point2d
    StartPoint: Point2d
    Length: float
    SubEntityType: AlignmentSubEntityType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DesignChecks(self, ) -> Collection: ...
    def Equals(self, obj: object) -> bool: ...
    def ValidateDesignCheck(self, designCheck: AlignmentDesignCheck) -> bool: ...

class AlignmentSubEntityArc(AlignmentSubEntity):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSubEntityArc"""
    def __init__(self, *args) -> None: ...
    MinimumRadius: float
    Clockwise: bool
    ReverseCurve: bool
    DeflectedAngle: float
    GreaterThan180: bool
    PIPoint: Point2d
    PIStation: float
    DirectionAtPoint2: float
    DirectionAtPoint1: float
    PassThroughPoint3: Point2d
    PassThroughPoint2: Point2d
    PassThroughPoint1: Point2d
    MidOrdinate: float
    ExternalTangent: float
    ExternalSecant: float
    ChordDirection: float
    ChordLength: float
    Delta: float
    EndDirection: float
    StartDirection: float
    Radius: float
    CenterPoint: Point2d
    SubEntityType: AlignmentSubEntityType
    CurveGroupSubEntityIndex: str
    CurveGroupIndex: str
    EndStation: float
    StartStation: float
    EndPoint: Point2d
    StartPoint: Point2d
    Length: float
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AlignmentSubEntityLine(AlignmentSubEntity):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSubEntityLine"""
    def __init__(self, *args) -> None: ...
    PassThroughPoint2: Point2d
    PassThroughPoint1: Point2d
    MidPoint: Point2d
    Direction: float
    SubEntityType: AlignmentSubEntityType
    CurveGroupSubEntityIndex: str
    CurveGroupIndex: str
    EndStation: float
    StartStation: float
    EndPoint: Point2d
    StartPoint: Point2d
    Length: float
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AlignmentSubEntitySpiral(AlignmentSubEntity):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSubEntitySpiral"""
    def __init__(self, *args) -> None: ...
    TotalY: float
    TotalX: float
    Direction: SpiralDirectionType
    SPIStation: float
    SpiralDefinition: SpiralType
    SPIPoint: Point2d
    SPIAngle: float
    ShortTangent: float
    RadiusOut: float
    RadiusIn: float
    RadialPoint: Point2d
    P: float
    MinimumTransitionLength: float
    LongTangent: float
    K: float
    EndDirection: float
    StartDirection: float
    Delta: float
    CurveType: SpiralCurveType
    Compound: bool
    A: float
    SubEntityType: AlignmentSubEntityType
    CurveGroupSubEntityIndex: str
    CurveGroupIndex: str
    EndStation: float
    StartStation: float
    EndPoint: Point2d
    StartPoint: Point2d
    Length: float
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AlignmentSubEntityType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSubEntityType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentSuperelevationLabelGroup(AlignmentLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentSuperelevationLabelGroup"""
    def __init__(self, *args) -> None: ...
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(styleId: ObjectId, alignmentId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...
    def GetGeometryPointsOptions(self, ) -> GeometryPointSelector: ...
    def SetGeometryPointsOptions(self, transitionPoints: GeometryPointSelector) -> None: ...

class AlignmentTable(Table):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentTable"""
    def __init__(self, *args) -> None: ...
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AlignmentTangentLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentTangentLabel"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(subEntityLine: AlignmentSubEntityLine, labelStyleId: ObjectId) -> ObjectId: ...

class AlignmentTrackDistanceData:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentTrackDistanceData"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentTransition(CivilWrapper<AeccDbAlignment>):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentTransition"""
    def __init__(self, *args) -> None: ...
    TransitionDescription: TransitionDescriptionBase
    TransitionType: TransitionType
    PreviousRegion: AlignmentRegion
    NextRegion: AlignmentRegion
    def Slim(self, ) -> None: ...

class AlignmentTransitionCollection(CivilWrapper<AeccDbAlignment>):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentTransitionCollection"""
    def __init__(self, *args) -> None: ...
    Item: AlignmentTransition
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class AlignmentType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentUpdateType:
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentUpdateType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentVerticalGeometryPointLabelGroup(AlignmentLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.AlignmentVerticalGeometryPointLabelGroup"""
    def __init__(self, *args) -> None: ...
    VerticalAlignment: ObjectId
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(styleId: ObjectId, alignmentId: ObjectId, verticalAlignmentId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...
    def GetGeometryPointsOptions(self, ) -> GeometryPointSelector: ...
    def SetGeometryPointsOptions(self, alignmentVerticalGeometryPoints: GeometryPointSelector) -> None: ...

class AnchorInfo:
    """.NET: Autodesk.Civil.DatabaseServices.AnchorInfo"""
    def __init__(self, *args) -> None: ...
    ...

class AppliedAssembly(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.AppliedAssembly"""
    def __init__(self, *args) -> None: ...
    AdjustedElevation: float
    AssemblyId: ObjectId
    ShapesByCode: CalculatedShapeCollection
    Shapes: CalculatedShapeCollection
    LinksByCode: CalculatedLinkCollection
    Links: CalculatedLinkCollection
    PointsByCode: CalculatedPointCollection
    Points: CalculatedPointCollection
    CorridorId: ObjectId
    def GetAppliedSubassemblies(self, ) -> AppliedSubassemblyCollection: ...
    def GetLinksByCode(self, code: str) -> CalculatedLinkCollection: ...
    def GetPointsByCode(self, code: str) -> CalculatedPointCollection: ...
    def GetShapesByCode(self, code: str) -> CalculatedShapeCollection: ...

class AppliedAssemblyCollection(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.AppliedAssemblyCollection"""
    def __init__(self, *args) -> None: ...
    Item: AppliedAssembly
    Count: int
    CorridorId: ObjectId
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetItemAt(self, station: float) -> AppliedAssembly: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Stations(self, ) -> list: ...

class AppliedAssemblySetting:
    """.NET: Autodesk.Civil.DatabaseServices.AppliedAssemblySetting"""
    def __init__(self, *args) -> None: ...
    AdditionalAppliedAssemblies: List
    FrequencyAlongTargetCurves: float
    MODAlongTargetCurves: float
    TargetCurveOption: CorridorAlongOffsetTargetCurveOption
    AppliedAdjacentToOffsetTargetStartEnd: bool
    AppliedAtOffsetTargetGeometryPoints: bool
    AppliedAtProfileHighLowPoints: bool
    AppliedAtProfileGeometryPoints: bool
    AppliedAtSuperelevationCriticalPoints: bool
    AppliedAtHorizontalGeometryPoints: bool
    FrequencyAlongProfileCurves: float
    FrequencyAlongSpirals: float
    FrequencyAlongCurves: float
    MODAlongCurves: float
    CorridorAlongCurvesOption: CorridorAlongCurveOption
    FrequencyAlongTangents: float

class AppliedSubassembly(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.AppliedSubassembly"""
    def __init__(self, *args) -> None: ...
    Parameters: list
    SubassemblyId: ObjectId
    BaselineHookedTo: BaseBaseline
    OriginStationOffsetElevationToBaseline: Point3d
    Shapes: CalculatedShapeCollection
    Links: CalculatedLinkCollection
    Points: CalculatedPointCollection
    CorridorId: ObjectId
    def Contains(self, paramKeyName: str) -> bool: ...
    def GetParameter(self, paramKeyName: str) -> AppliedSubassemblyParam: ...

class AppliedSubassemblyCollection(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.AppliedSubassemblyCollection"""
    def __init__(self, *args) -> None: ...
    Item: AppliedSubassembly
    Count: int
    CorridorId: ObjectId
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def ObjectIds(self, ) -> list: ...

class AppliedSubassemblyParam:
    """.NET: Autodesk.Civil.DatabaseServices.AppliedSubassemblyParam`1"""
    def __init__(self, *args) -> None: ...
    Value: T
    DesignValue: T
    ValueAsObject: object
    DesignValueAsObject: object
    ValueType: Type
    IsOverriden: bool
    Comment: str
    DisplayName: str
    KeyName: str
    def ClearOverride(self, ) -> bool: ...

class Assembly(GeoEntity):
    """.NET: Autodesk.Civil.DatabaseServices.Assembly"""
    def __init__(self, *args) -> None: ...
    Groups: AssemblyGroupCollection
    OffsetAssemblies: OffsetAssemblyCollection
    Location: Point3d
    Type: AssemblyType
    StyleId: ObjectId
    StyleName: str
    CodeSetStyleId: ObjectId
    CodeSetStyleName: str
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddSubassembly(self, subassemblyId: ObjectId, pointHookTo: Point) -> None: ...
    def CopySubassembly(self, subassemblyIdFrom: ObjectId, pointHookTo: Point) -> ObjectId: ...
    def GetOffsetBaselineNames(self, ) -> list: ...
    def InsertSubassemblyAfter(self, subassemblyId: ObjectId, pointHookTo: Point) -> None: ...
    def InsertSubassemblyBefore(self, subassemblyId: ObjectId, targetSubassemblyId: ObjectId) -> None: ...
    def MirrorSubassembly(self, subassemblyIdFrom: ObjectId, pointHookTo: Point) -> ObjectId: ...
    def ReplaceSubassembly(self, subassemblyId: ObjectId, targetSubassemblyId: ObjectId) -> None: ...

class AssemblyCollection(CivilWrapper<AcDbDatabase>):
    """.NET: Autodesk.Civil.DatabaseServices.AssemblyCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    def Add(self, assemblyName: str, type: AssemblyType, location: Point3d, styleId: ObjectId, codeSetStyleId: ObjectId) -> ObjectId: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def ImportAssembly(self, assemblyName: str, sourceDatabase: Database, sourceAssemblyName: str, location: Point3d) -> ObjectId: ...

class AssemblyGroup:
    """.NET: Autodesk.Civil.DatabaseServices.AssemblyGroup"""
    def __init__(self, *args) -> None: ...
    Name: str
    def GetSubassemblyIds(self, ) -> ObjectIdCollection: ...

class AssemblyGroupCollection:
    """.NET: Autodesk.Civil.DatabaseServices.AssemblyGroupCollection"""
    def __init__(self, *args) -> None: ...
    Item: AssemblyGroup
    Item: AssemblyGroup
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, group: AssemblyGroup) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class AssemblyType:
    """.NET: Autodesk.Civil.DatabaseServices.AssemblyType"""
    def __init__(self, *args) -> None: ...
    ...

class AttributeTypeInfo(DisposableWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.AttributeTypeInfo"""
    def __init__(self, *args) -> None: ...
    UseDefaultValue: bool
    DefaultValue: object
    Description: str
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AttributeTypeInfoBool(AttributeTypeInfo):
    """.NET: Autodesk.Civil.DatabaseServices.AttributeTypeInfoBool"""
    def __init__(self, *args) -> None: ...
    DefaultValue: bool
    UseDefaultValue: bool
    DefaultValue: object
    Description: str
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AttributeTypeInfoDouble(AttributeTypeInfo):
    """.NET: Autodesk.Civil.DatabaseServices.AttributeTypeInfoDouble"""
    def __init__(self, *args) -> None: ...
    LowerBoundValue: float
    UpperBoundValue: float
    LowerBoundInclusive: bool
    UpperBoundInclusive: bool
    DefaultValue: float
    DataType: AttributeTypeInfoDoubleDataType
    UseDefaultValue: bool
    DefaultValue: object
    Description: str
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AttributeTypeInfoDoubleDataType:
    """.NET: Autodesk.Civil.DatabaseServices.AttributeTypeInfoDoubleDataType"""
    def __init__(self, *args) -> None: ...
    ...

class AttributeTypeInfoEnum(AttributeTypeInfo):
    """.NET: Autodesk.Civil.DatabaseServices.AttributeTypeInfoEnum"""
    def __init__(self, *args) -> None: ...
    DefaultValue: str
    UseDefaultValue: bool
    DefaultValue: object
    Description: str
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetEnumValues(self, ) -> list: ...

class AttributeTypeInfoInt(AttributeTypeInfo):
    """.NET: Autodesk.Civil.DatabaseServices.AttributeTypeInfoInt"""
    def __init__(self, *args) -> None: ...
    LowerBoundValue: int
    UpperBoundValue: int
    LowerBoundInclusive: bool
    UpperBoundInclusive: bool
    DefaultValue: int
    UseDefaultValue: bool
    DefaultValue: object
    Description: str
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AttributeTypeInfoString(AttributeTypeInfo):
    """.NET: Autodesk.Civil.DatabaseServices.AttributeTypeInfoString"""
    def __init__(self, *args) -> None: ...
    DefaultValue: str
    UseDefaultValue: bool
    DefaultValue: object
    Description: str
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AutoCorridorFeatureLine(FeatureLine):
    """.NET: Autodesk.Civil.DatabaseServices.AutoCorridorFeatureLine"""
    def __init__(self, *args) -> None: ...
    CorridorFeaturelineSide: str
    CorridorFeaturelineRegionName: str
    FeatureLineEndCriteriaBeadStation: float
    FeatureLineStartCriteriaBeadStation: float
    CreateFeatureLineDynamicLink: bool
    CorridorName: str
    CorridorFeaturelineBaselineName: str
    CorridorFeaturelineCode: str
    CurvesCount: int
    ElevationPointsCount: int
    PIPointsCount: int
    PointsCount: int
    RelativeSurfaceId: ObjectId
    Length3D: float
    Length2D: float
    MaxGrade: float
    MinGrade: float
    MaxElevation: float
    MinElevation: float
    SiteId: ObjectId
    StyleName: str
    StyleId: ObjectId
    IsEditable: bool
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DetachCorridor(self, ) -> None: ...
    def ReAttachCorridor(self, ) -> None: ...
    def SourceObjectName(self, ) -> str: ...

class AutoFeatureLabelGroup(LabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.AutoFeatureLabelGroup"""
    def __init__(self, *args) -> None: ...
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetRange(self, rangeStart: float, rangeEnd: float) -> None: ...

class AutoFeatureLine(FeatureLine):
    """.NET: Autodesk.Civil.DatabaseServices.AutoFeatureLine"""
    def __init__(self, *args) -> None: ...
    AutomaticUpdate: bool
    SpiralTessellation: float
    VerticalDeviation: float
    SourceObjectName: str
    SourceObjectId: ObjectId
    AlignmentId: ObjectId
    ProfileId: ObjectId
    CurvesCount: int
    ElevationPointsCount: int
    PIPointsCount: int
    PointsCount: int
    RelativeSurfaceId: ObjectId
    Length3D: float
    Length2D: float
    MaxGrade: float
    MinGrade: float
    MaxElevation: float
    MinElevation: float
    SiteId: ObjectId
    StyleName: str
    StyleId: ObjectId
    IsEditable: bool
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DetachAlignment(self, ) -> None: ...
    def ReAttachAlignment(self, ) -> None: ...

class AutoWideningCriteriaInfo:
    """.NET: Autodesk.Civil.DatabaseServices.AutoWideningCriteriaInfo"""
    def __init__(self, *args) -> None: ...
    WideningSide: WideningSide
    WheelbaseLength: float
    RightLanesCount: int
    LeftLanesCount: int
    LaneWidth: float
    TangentPercentForTC: float
    SpiralPercentForSC: float
    AttainmentMethod: str
    TransitionLengthTableName: str
    MinimumRadiusTableName: str
    WideningMethod: str
    CriteriaFileName: str

class AutoWideningInfo:
    """.NET: Autodesk.Civil.DatabaseServices.AutoWideningInfo"""
    def __init__(self, *args) -> None: ...
    Side: WideningSide
    TransitionLength: float
    IncreasedWidth: float

class BaseBaseline(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.BaseBaseline"""
    def __init__(self, *args) -> None: ...
    DirectionAtStation: Vector3d
    EndStation: float
    StartStation: float
    baselineGUID: Guid
    BaselineGuid: Guid
    ProfileId: ObjectId
    FeatureLineId: ObjectId
    AlignmentId: ObjectId
    BaselineType: CorridorBaselineType
    CorridorId: ObjectId
    def GetDirectionAtStation(self, station: float) -> Vector3d: ...
    def IsFeatureLineBased(self, ) -> bool: ...
    def SetAlignmentAndProfile(self, alignmentId: ObjectId, profileId: ObjectId) -> None: ...
    def SortedStations(self, ) -> list: ...
    def StationOffsetElevationToXYZ(self, soe: Point3d) -> Point3d: ...

class BaseLineRange:
    """.NET: Autodesk.Civil.DatabaseServices.BaseLineRange"""
    def __init__(self, *args) -> None: ...
    BaseLineId: ObjectId
    EndStation: float
    StartStation: float
    def CheckStationRange(self, ) -> None: ...

class Baseline(BaseBaseline):
    """.NET: Autodesk.Civil.DatabaseServices.Baseline"""
    def __init__(self, *args) -> None: ...
    MainBaselineFeatureLines: BaselineFeatureLines
    OffsetBaselineFeatureLinesCol: BaselineFeatureLinesCollection
    AppliedAssembly: AppliedAssembly
    AppliedAssembly: AppliedAssembly
    BaselineRegions: BaselineRegionCollection
    NeedsProcessing: bool
    IsProcessed: bool
    Name: str
    ProfileId: ObjectId
    baselineGUID: Guid
    BaselineGuid: Guid
    AlignmentId: ObjectId
    BaselineType: CorridorBaselineType
    DirectionAtStation: Vector3d
    EndStation: float
    StartStation: float
    FeatureLineId: ObjectId
    CorridorId: ObjectId
    def ExportSolids(self, params: ExportCorridorSolidsParams, targetDatabase: Database) -> ObjectIdCollection: ...
    def ExportTransitions(self, csvFileName: str) -> None: ...
    def GetAppliedAssemblyAtIndex(self, index: int) -> AppliedAssembly: ...
    def GetAppliedAssemblyAtStation(self, station: float) -> AppliedAssembly: ...
    def GetTargets(self, ) -> SubassemblyTargetInfoCollection: ...
    def ImportTransitions(self, csvFileName: str) -> int: ...
    def IsFeatureLineBased(self, ) -> bool: ...
    def SetFeatureLine(self, featureLineId: ObjectId) -> None: ...
    def SetTargets(self, updatedTargets: SubassemblyTargetInfoCollection) -> None: ...
    def SetTransitions(self, transitionSets: IEnumerable) -> None: ...
    def SortedStations(self, ) -> list: ...
    def UpdateStation(self, station: float) -> None: ...
    def getTransitions(self, ) -> List: ...

class BaselineCollection(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.BaselineCollection"""
    def __init__(self, *args) -> None: ...
    Item: Baseline
    Item: Baseline
    Item: Baseline
    Count: int
    CorridorId: ObjectId
    def Add(self, baselineName: str, alignmentId: ObjectId, profileId: ObjectId) -> Baseline: ...
    def AddGUIDBaseline(self, baselineName: str, alignmentId: ObjectId, profileId: ObjectId) -> Baseline: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, baseline: Baseline) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class BaselineFeatureLines(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.BaselineFeatureLines"""
    def __init__(self, *args) -> None: ...
    HardcodedOffsetBaselineName: str
    OffsetAlignmentId: ObjectId
    IsMainBaseline: bool
    FeatureLineCollectionMap: FeatureLineCollectionMap
    CorridorId: ObjectId
    def CodeNames(self, ) -> list: ...

class BaselineFeatureLinesCollection(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.BaselineFeatureLinesCollection"""
    def __init__(self, *args) -> None: ...
    Item: BaselineFeatureLines
    Count: int
    CorridorId: ObjectId
    def CodeNames(self, ) -> list: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class BaselineRegion(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.BaselineRegion"""
    def __init__(self, *args) -> None: ...
    AppliedAssemblySetting: AppliedAssemblySetting
    RegionGUID: Guid
    AssemblyId: ObjectId
    EndStation: float
    StartStation: float
    AppliedAssemblies: AppliedAssemblyCollection
    OffsetBaselines: OffsetBaselineCollection
    NeedsProcessing: bool
    IsProcessed: bool
    CorridorId: ObjectId
    Name: str
    def AddStation(self, rawStation: float, description: str) -> None: ...
    def AdditionalStations(self, ) -> list: ...
    def ClearAdditionalStations(self, ) -> None: ...
    def DeleteStation(self, rawStation: float) -> None: ...
    def ExportSolids(self, params: ExportCorridorSolidsParams, startStation: float, endStation: float, targetDatabase: Database) -> ObjectIdCollection: ...
    def GetOverriddenStations(self, ) -> list: ...
    def GetTargets(self, ) -> SubassemblyTargetInfoCollection: ...
    def Match(self, sourceRegion: BaselineRegion, matchOption: RegionMatchType) -> None: ...
    def Merge(self, firstRegion: BaselineRegion, lastRegion: BaselineRegion) -> None: ...
    def RemoveOverriddenStation(self, station: float) -> bool: ...
    def SetTargets(self, updatedTargets: SubassemblyTargetInfoCollection) -> None: ...
    def SortedStations(self, ) -> list: ...
    def Split(self, splitStation: float) -> BaselineRegion: ...

class BaselineRegionCollection(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.BaselineRegionCollection"""
    def __init__(self, *args) -> None: ...
    Item: BaselineRegion
    Item: BaselineRegion
    Item: BaselineRegion
    Count: int
    CorridorId: ObjectId
    def Add(self, regionName: str, assemblyId: ObjectId, startStation: float, endStation: float) -> BaselineRegion: ...
    def AddRegion(self, regionName: str, assemblyId: ObjectId) -> BaselineRegion: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, region: BaselineRegion) -> int: ...
    def Remove(self, region: BaselineRegion) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class BoundingShapeType:
    """.NET: Autodesk.Civil.DatabaseServices.BoundingShapeType"""
    def __init__(self, *args) -> None: ...
    ...

class Bridge(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.Bridge"""
    def __init__(self, *args) -> None: ...
    DeckId: ObjectId
    BridgeGuid: str
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetAbutmentIds(self, ) -> ObjectIdCollection: ...
    def GetAllContentIds(self, ) -> ObjectIdCollection: ...
    def GetAllStructureIds(self, ) -> ObjectIdCollection: ...
    def GetFoundationIds(self, ) -> ObjectIdCollection: ...
    def GetGenericObjectIds(self, ) -> ObjectIdCollection: ...
    def GetGirderGroupIds(self, ) -> ObjectIdCollection: ...
    def GetGirderIds(self, ) -> ObjectIdCollection: ...
    def GetPierIds(self, ) -> ObjectIdCollection: ...

class BridgeAbutment(BridgeStructure):
    """.NET: Autodesk.Civil.DatabaseServices.BridgeAbutment"""
    def __init__(self, *args) -> None: ...
    FoundationId: ObjectId
    BridgeStructureType: BridgeStructureType
    BridgeId: ObjectId
    BridgeStructureGuid: str
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class BridgeDeck(BridgeStructure):
    """.NET: Autodesk.Civil.DatabaseServices.BridgeDeck"""
    def __init__(self, *args) -> None: ...
    BridgeStructureType: BridgeStructureType
    BridgeId: ObjectId
    BridgeStructureGuid: str
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class BridgeFoundation(BridgeStructure):
    """.NET: Autodesk.Civil.DatabaseServices.BridgeFoundation"""
    def __init__(self, *args) -> None: ...
    PierId: ObjectId
    AbutmentId: ObjectId
    BridgeStructureType: BridgeStructureType
    BridgeId: ObjectId
    BridgeStructureGuid: str
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class BridgeGenericObject(BridgeStructure):
    """.NET: Autodesk.Civil.DatabaseServices.BridgeGenericObject"""
    def __init__(self, *args) -> None: ...
    GenericObjectType: BridgeGenericObjectType
    BridgeStructureType: BridgeStructureType
    BridgeId: ObjectId
    BridgeStructureGuid: str
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class BridgeGenericObjectType:
    """.NET: Autodesk.Civil.DatabaseServices.BridgeGenericObjectType"""
    def __init__(self, *args) -> None: ...
    ...

class BridgeGirder(BridgeStructure):
    """.NET: Autodesk.Civil.DatabaseServices.BridgeGirder"""
    def __init__(self, *args) -> None: ...
    GirderGroupId: ObjectId
    BridgeStructureType: BridgeStructureType
    BridgeId: ObjectId
    BridgeStructureGuid: str
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class BridgeGirderGroup(BridgeStructure):
    """.NET: Autodesk.Civil.DatabaseServices.BridgeGirderGroup"""
    def __init__(self, *args) -> None: ...
    BridgeStructureType: BridgeStructureType
    BridgeId: ObjectId
    BridgeStructureGuid: str
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetGirderIds(self, ) -> ObjectIdCollection: ...

class BridgePier(BridgeStructure):
    """.NET: Autodesk.Civil.DatabaseServices.BridgePier"""
    def __init__(self, *args) -> None: ...
    FoundationId: ObjectId
    BridgeStructureType: BridgeStructureType
    BridgeId: ObjectId
    BridgeStructureGuid: str
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class BridgeStructure(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.BridgeStructure"""
    def __init__(self, *args) -> None: ...
    BridgeStructureType: BridgeStructureType
    BridgeId: ObjectId
    BridgeStructureGuid: str
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetContentIds(self, ) -> ObjectIdCollection: ...

class BridgeStructureType:
    """.NET: Autodesk.Civil.DatabaseServices.BridgeStructureType"""
    def __init__(self, *args) -> None: ...
    ...

class CANTCriticalStation:
    """.NET: Autodesk.Civil.DatabaseServices.CANTCriticalStation"""
    def __init__(self, *args) -> None: ...
    CantJerk: float
    CantRatio: float
    EquilibriumCantVerticalSpeed: float
    LateralAcceleration: float
    DesignSpeed: float
    CurveRadius: float
    CantDeficiencyVerticalSpeed: float
    VerticalSpeed: float
    EquilibriumCantGradient: float
    CantDeficiencyGradient: float
    CantGradient: float
    CantDeficiency: float
    EquilibriumCant: float
    RightRailElevationDifference: float
    LeftRailElevationDifference: float
    AppliedCANT: float
    TransitionDescription: str
    Station: float
    TransitionRegionType: SuperelevationTransitionRegionType
    StationType: SuperelevationCriticalStationType
    CANTCurveName: str
    ParentAlignmentId: ObjectId
    def Dispose(self, ) -> None: ...

class CANTCriticalStationCollection:
    """.NET: Autodesk.Civil.DatabaseServices.CANTCriticalStationCollection"""
    def __init__(self, *args) -> None: ...
    ParentAlignmentId: ObjectId
    Count: int
    Item: CANTCriticalStation
    def Add(self, station: float, criticalStationType: SuperelevationCriticalStationType, attainmentRegionType: SuperelevationAttainmentRegionType) -> None: ...
    def GetCriticalStationAt(self, station: float, tolerance: float) -> CANTCriticalStation: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def IsCriticalStation(self, station: float, tolerance: float) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class CANTCurve(SECurve):
    """.NET: Autodesk.Civil.DatabaseServices.CANTCurve"""
    def __init__(self, *args) -> None: ...
    CantPivotMethod: CantPivotMethodType
    Name: str
    ParentAlignmentId: ObjectId
    EndStation: float
    StartStation: float
    CANTCriticalStations: CANTCriticalStationCollection
    CriticalStations: SuperelevationCriticalStationCollection

class CANTCurveCollection:
    """.NET: Autodesk.Civil.DatabaseServices.CANTCurveCollection"""
    def __init__(self, *args) -> None: ...
    ParentAlignmentId: ObjectId
    Count: int
    Item: CANTCurve
    Item: CANTCurve
    def AddUserDefinedCurve(self, startSubEntity: AlignmentSubEntity, endSubEntity: AlignmentSubEntity) -> CANTCurve: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class CalculatedLink(CalculatedSubentity):
    """.NET: Autodesk.Civil.DatabaseServices.CalculatedLink"""
    def __init__(self, *args) -> None: ...
    DrawOverride: CorridorLinkDrawOverride
    CalculatedPoints: CalculatedPointCollection
    CorridorCodes: CorridorCodeCollection
    SubassemblyBelongedTo: AppliedSubassembly
    CorridorId: ObjectId

class CalculatedLinkCollection(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.CalculatedLinkCollection"""
    def __init__(self, *args) -> None: ...
    Item: CalculatedLink
    Count: int
    CorridorId: ObjectId
    def Add(self, point1: CalculatedPoint, point2: CalculatedPoint, code: str) -> CalculatedLink: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, link: CalculatedLink) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class CalculatedPoint(CalculatedSubentity):
    """.NET: Autodesk.Civil.DatabaseServices.CalculatedPoint"""
    def __init__(self, *args) -> None: ...
    NormalToBaseline: Vector3d
    NormalToSubassembly: Vector3d
    XYZ: Point3d
    StationOffsetElevationToSubassembly: Point3d
    StationOffsetElevationToBaseline: Point3d
    CorridorCodes: CorridorCodeCollection
    SubassemblyBelongedTo: AppliedSubassembly
    CorridorId: ObjectId

class CalculatedPointCollection(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.CalculatedPointCollection"""
    def __init__(self, *args) -> None: ...
    Item: CalculatedPoint
    Count: int
    CorridorId: ObjectId
    def Add(self, link: CalculatedLink, code: str) -> CalculatedPoint: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, point: CalculatedPoint) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class CalculatedShape(CalculatedSubentity):
    """.NET: Autodesk.Civil.DatabaseServices.CalculatedShape"""
    def __init__(self, *args) -> None: ...
    Area: float
    CalculatedLinks: CalculatedLinkCollection
    CorridorCodes: CorridorCodeCollection
    SubassemblyBelongedTo: AppliedSubassembly
    CorridorId: ObjectId

class CalculatedShapeCollection(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.CalculatedShapeCollection"""
    def __init__(self, *args) -> None: ...
    Item: CalculatedShape
    Count: int
    CorridorId: ObjectId
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class CalculatedSubentity(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.CalculatedSubentity"""
    def __init__(self, *args) -> None: ...
    SubassemblyBelongedTo: AppliedSubassembly
    CorridorCodes: CorridorCodeCollection
    CorridorId: ObjectId

class Catchment(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.Catchment"""
    def __init__(self, *args) -> None: ...
    DurationOfPeak: float
    RecessionMultiplier: float
    InitialDeficit: float
    Conductivity: float
    SuctionHead: float
    MaxInfiltrationVolume: float
    HortonDryingTime: float
    CurveNumberDryingTime: float
    DecayConstant: float
    MinInfiltrationRate: float
    MaxInfiltrationRate: float
    InfiltrationMethod: InfiltrationMethod
    PerviousManningsN: float
    PerviousDepressionStorageDepth: float
    PerviousDeppressionStorageDepth: float
    ImperviousNoDepression: float
    ImperviousManningsN: float
    ImperviousDepressionStorageDepth: float
    ImperviousDeppressionStorageDepth: float
    RoutingPercentage: float
    InternalRouting: InternalRouting
    EquivalentWidth: float
    AverageSlope: float
    CompositeCurveNumber: int
    InitialAbstractionFraction: float
    InitialAbstractionDepth: float
    InitialAbstractionType: InitialAbstractionType
    ShapeFactor: int
    ShapeType: HydrographShapeType
    RunoffMethod: RunoffMethod
    ChannelFlowTravelTime: float
    ChannelFlowSegments: int
    ShallowFlowTravelTime: float
    ShallowFlowSegments: int
    SheetFlowTravelTime: float
    SheetFlowSegments: int
    ReferencePipeNetworkName: str
    ReferencePipeNetworkId: ObjectId
    ReferenceDischargeObjectId: ObjectId
    ReferenceDischargeObjectName: str
    ReferencePipeNetworkStructureId: ObjectId
    ReferencePipeNetworkStructureName: str
    ReferenceSurfaceName: str
    ReferenceSurfaceId: ObjectId
    RunoffCoefficient: float
    ManningsCoefficient: float
    TimeOfConcentrationCalculationMethod: TimeOfConcentrationCalculationMethod
    TimeOfConcentration: float
    Exclusionary: bool
    FlowPathLength: float
    HydrologicallyMostDistantLength: float
    HydrologicallyMostDistantPoint: Point3d
    UnconnectedImperviousArea: float
    ImperviousArea: float
    AntecedentWetness: int
    HydrologicalSoilGroup: HydrologicalSoilGroup
    CurveNumber: int
    DischargePoint: Point3d
    ContainingGroupId: ObjectId
    BoundaryPolyline3d: Point3dCollection
    BoundaryPolyline2d: Point2dCollection
    Perimeter2d: float
    Area2d: float
    StyleId: ObjectId
    FlowPath: FlowPath
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(name: str, styleId: ObjectId, catchmentGroupId: ObjectId, surfaceId: ObjectId, boundary: Point3dCollection) -> ObjectId: ...
    @staticmethod
    def CreateCopy(catchmentId: ObjectId, groupId: ObjectId) -> ObjectId: ...
    def GetAvailableCatchmentLabelIds(self, ) -> ObjectIdCollection: ...
    def GetAvailableFlowSegmentLabelIds(self, ) -> ObjectIdCollection: ...
    def GetFlowPath(self, ) -> FlowPath: ...
    def SetFlowPath(self, FlowPath: Point3dCollection) -> None: ...

class CatchmentGroup(DBObject):
    """.NET: Autodesk.Civil.DatabaseServices.CatchmentGroup"""
    def __init__(self, *args) -> None: ...
    IsUsed: bool
    Description: str
    Name: str
    Document: object
    Application: object
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddCatchmentId(self, catchmentId: ObjectId) -> None: ...
    @staticmethod
    def Create(database: Database, catchmentGroupName: str) -> ObjectId: ...
    def GetAllCatchmentIds(self, ) -> ObjectIdCollection: ...
    def GetCatchmentId(self, catchmentName: str) -> ObjectId: ...
    @staticmethod
    def MoveCatchment(catchmentId: ObjectId, catchmentGroupIdTo: ObjectId) -> None: ...
    def RemoveAllCatchments(self, ) -> None: ...
    def RemoveCatchmentId(self, catchmentId: ObjectId) -> None: ...

class CatchmentGroupCollection(TreeNodeCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.CatchmentGroupCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ObjectId
    Item: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...
    def ForceRemove(self, name: str) -> None: ...
    @staticmethod
    def GetCatchmentGroups(database: Database) -> CatchmentGroupCollection: ...
    def Remove(self, index: int) -> None: ...

class CatchmentLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.CatchmentLabel"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(catchmentId: ObjectId, labelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelIds(catchmentId: ObjectId) -> ObjectIdCollection: ...

class CodeCollection(CivilWrapper<AeccDbEntity>):
    """.NET: Autodesk.Civil.DatabaseServices.CodeCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: str
    def Add(self, codes: list) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, code: str) -> bool: ...
    def TryAdd(self, codes: list) -> None: ...

class CogoPoint(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.CogoPoint"""
    def __init__(self, *args) -> None: ...
    LeaderAttachment: LeaderAttachmentBehaviorType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderVisibility: LeaderVisibilityType
    IsLabelVisible: bool
    IsLabelPinned: bool
    IsLabelDragged: bool
    IsCheckedOut: bool
    ProjectVersion: int
    IsProjectPoint: bool
    GridEasting: float
    GridNorthing: float
    Longitude: float
    Latitude: float
    Convergence: float
    StyleIdOverride: ObjectId
    StyleId: ObjectId
    LabelStyleIdOverride: ObjectId
    LabelStyleId: ObjectId
    Scale: float
    ScaleZ: float
    ScaleXY: float
    LabelLocation: Point3d
    LabelRotation: float
    MarkerRotation: float
    ElevationOverride: float
    Elevation: float
    Northing: float
    Easting: float
    ShowToolTip: bool
    IsLocked: bool
    PrimaryPointGroupId: ObjectId
    DescriptionFormat: str
    FullDescriptionOverride: str
    FullDescription: str
    RawDescriptionOverride: str
    RawDescription: str
    PointNumber: int
    PointName: str
    IsMovable: bool
    IsSurveyPoint: bool
    Location: Point3d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ApplyDescriptionKeys(self, ) -> None: ...
    def ClearAllLabelTextComponentOverrides(self, ) -> None: ...
    def ClearLabelTextComponentOverrides(self, labelComponentId: ObjectId) -> None: ...
    def GetLabelTextComponentIds(self, ) -> ObjectIdCollection: ...
    def GetLabelTextComponentJustificationOverride(self, labelComponentId: ObjectId) -> TextJustificationType: ...
    def GetLabelTextComponentOverride(self, labelComponentId: ObjectId) -> str: ...
    def GetUDPValue(self, udp: UDPEnumeration) -> str: ...
    def IsLabelTextComponentOverriden(self, labelComponentId: ObjectId) -> bool: ...
    def Renumber(self, newPointNumber: int, resolveType: PointNumberResolveType) -> int: ...
    def ResetLabel(self, ) -> None: ...
    def ResetLabelLocation(self, ) -> None: ...
    def ResetLabelRotation(self, ) -> None: ...
    def SetLabelTextComponentJustificationOverride(self, labelComponentId: ObjectId, textJustificationType: TextJustificationType) -> None: ...
    def SetLabelTextComponentOverride(self, labelComponentId: ObjectId, textOverride: str) -> None: ...
    def SetUDPValue(self, udp: UDPEnumeration, value: str) -> None: ...

class CogoPointCollection:
    """.NET: Autodesk.Civil.DatabaseServices.CogoPointCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    def Add(self, locations: Point3dCollection, desc: str, useDescriptionKey: bool, matchOnParams: bool, useNextPointNumSetting: bool) -> ObjectIdCollection: ...
    def Clear(self, ) -> None: ...
    def Contains(self, pointNumber: int) -> bool: ...
    @staticmethod
    def ExportPoints(pointFileFullName: str, fileFormat: PointFileFormat, useAdjustedElevation: bool, shouldTransformCoordinate: bool, shouldExpandCoordinateData: bool, pointGroupId: ObjectId) -> int: ...
    @staticmethod
    def GetCogoPoints(pDatabase: Database) -> CogoPointCollection: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def GetPointByPointNumber(self, pointNumber: int) -> ObjectId: ...
    @staticmethod
    def ImportPoints(pointFileFullName: str, fileFormat: PointFileFormat, useAdjustedElevation: bool, shouldTransformCoordinate: bool, shouldExpandCoordinateData: bool, pointGroupId: ObjectId) -> int: ...
    def Remove(self, pointId: ObjectId) -> None: ...
    def SetDescriptionFormat(self, pointIds: IEnumerable, values: IEnumerable) -> ObjectIdCollection: ...
    def SetEasting(self, pointIds: IEnumerable, values: IEnumerable) -> ObjectIdCollection: ...
    def SetElevation(self, pointIds: IEnumerable, elevations: IEnumerable) -> ObjectIdCollection: ...
    def SetElevationByOffset(self, pointIds: IEnumerable, offsets: IEnumerable) -> ObjectIdCollection: ...
    def SetElevationBySurface(self, pointIds: IEnumerable, surfaceId: ObjectId) -> ObjectIdCollection: ...
    def SetIsLocked(self, pointIds: IEnumerable, values: IEnumerable) -> ObjectIdCollection: ...
    def SetLabelRotation(self, pointIds: IEnumerable, values: IEnumerable) -> ObjectIdCollection: ...
    def SetLabelStyleId(self, pointIds: IEnumerable, styleIds: IEnumerable) -> ObjectIdCollection: ...
    def SetMarkerRotation(self, pointIds: IEnumerable, values: IEnumerable) -> ObjectIdCollection: ...
    def SetNorthing(self, pointIds: IEnumerable, values: IEnumerable) -> ObjectIdCollection: ...
    def SetPointName(self, pointIds: IEnumerable, values: IEnumerable) -> ObjectIdCollection: ...
    def SetPointNumber(self, pointIds: IEnumerable, additiveFactor: int) -> ObjectIdCollection: ...
    def SetRawDescription(self, pointIds: IEnumerable, rawDescs: IEnumerable) -> ObjectIdCollection: ...
    def SetScaleXY(self, pointIds: IEnumerable, values: IEnumerable) -> ObjectIdCollection: ...
    def SetScaleZ(self, pointIds: IEnumerable, values: IEnumerable) -> ObjectIdCollection: ...
    def SetShowTooltips(self, pointIds: IEnumerable, values: IEnumerable) -> ObjectIdCollection: ...
    def SetStyleId(self, pointIds: IEnumerable, styleIds: IEnumerable) -> ObjectIdCollection: ...

class CogoPointEnumerator:
    """.NET: Autodesk.Civil.DatabaseServices.CogoPointEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: ObjectId
    CurrentObject: object
    def Dispose(self, ) -> None: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ConnectedAlignmentArcInfo(ConnectedAlignmentInfo):
    """.NET: Autodesk.Civil.DatabaseServices.ConnectedAlignmentArcInfo"""
    def __init__(self, *args) -> None: ...
    CurveRadius: float
    ConnectionOverlapLengthOut: float
    ConnectionOverlapLengthIn: float
    GreaterThan180: bool
    OffsetOut: float
    OffsetIn: float
    CurveGroupType: CurbReturnCurveGroupType
    UpdateMode: AlignmentUpdateModeType
    OutgoingParentAlignmentId: ObjectId
    IncomingParentAlignmentId: ObjectId

class ConnectedAlignmentCCCInfo(ConnectedAlignmentInfo):
    """.NET: Autodesk.Civil.DatabaseServices.ConnectedAlignmentCCCInfo"""
    def __init__(self, *args) -> None: ...
    ArcOutLength: float
    ArcOutRadius: float
    ArcMiddleRadius: float
    ArcInLength: float
    ArcInRadius: float
    ConnectionOverlapLengthOut: float
    ConnectionOverlapLengthIn: float
    GreaterThan180: bool
    OffsetOut: float
    OffsetIn: float
    CurveGroupType: CurbReturnCurveGroupType
    UpdateMode: AlignmentUpdateModeType
    OutgoingParentAlignmentId: ObjectId
    IncomingParentAlignmentId: ObjectId

class ConnectedAlignmentInfo:
    """.NET: Autodesk.Civil.DatabaseServices.ConnectedAlignmentInfo"""
    def __init__(self, *args) -> None: ...
    ConnectionOverlapLengthOut: float
    ConnectionOverlapLengthIn: float
    GreaterThan180: bool
    OffsetOut: float
    OffsetIn: float
    CurveGroupType: CurbReturnCurveGroupType
    UpdateMode: AlignmentUpdateModeType
    OutgoingParentAlignmentId: ObjectId
    IncomingParentAlignmentId: ObjectId

class ConnectedAlignmentParams:
    """.NET: Autodesk.Civil.DatabaseServices.ConnectedAlignmentParams"""
    def __init__(self, *args) -> None: ...
    ArcOutLength: float
    ArcOutRadius: float
    ArcMiddleRadius: float
    ArcInLength: float
    ArcInRadius: float
    ReverseSpiralOutLength: float
    SpiralOutLength: float
    ReverseSpiralInLength: float
    SpiralInLength: float
    SpiralDefinition: SpiralType
    CurveRadius: float
    GreaterThan180: bool
    CurveGroupType: CurbReturnCurveGroupType
    ConnectionOverlapLengthOut: float
    OffsetOut: float
    OutgoingParentAlignmentStation: float
    OutgoingParentAlignmentId: ObjectId
    ConnectionOverlapLengthIn: float
    OffsetIn: float
    IncomingParentAlignmentStation: float
    IncomingParentAlignmentId: ObjectId

class ConnectedAlignmentSCSInfo(ConnectedAlignmentInfo):
    """.NET: Autodesk.Civil.DatabaseServices.ConnectedAlignmentSCSInfo"""
    def __init__(self, *args) -> None: ...
    SpiralOutLength: float
    SpiralInLength: float
    SpiralDefinition: SpiralType
    CurveRadius: float
    ConnectionOverlapLengthOut: float
    ConnectionOverlapLengthIn: float
    GreaterThan180: bool
    OffsetOut: float
    OffsetIn: float
    CurveGroupType: CurbReturnCurveGroupType
    UpdateMode: AlignmentUpdateModeType
    OutgoingParentAlignmentId: ObjectId
    IncomingParentAlignmentId: ObjectId

class ConnectedAlignmentSCSSInfo(ConnectedAlignmentInfo):
    """.NET: Autodesk.Civil.DatabaseServices.ConnectedAlignmentSCSSInfo"""
    def __init__(self, *args) -> None: ...
    ReverseSpiralOutLength: float
    SpiralOutLength: float
    SpiralInLength: float
    SpiralDefinition: SpiralType
    CurveRadius: float
    ConnectionOverlapLengthOut: float
    ConnectionOverlapLengthIn: float
    GreaterThan180: bool
    OffsetOut: float
    OffsetIn: float
    CurveGroupType: CurbReturnCurveGroupType
    UpdateMode: AlignmentUpdateModeType
    OutgoingParentAlignmentId: ObjectId
    IncomingParentAlignmentId: ObjectId

class ConnectedAlignmentSSCSInfo(ConnectedAlignmentInfo):
    """.NET: Autodesk.Civil.DatabaseServices.ConnectedAlignmentSSCSInfo"""
    def __init__(self, *args) -> None: ...
    SpiralOutLength: float
    SpiralInLength: float
    ReverseSpiralInLength: float
    SpiralDefinition: SpiralType
    CurveRadius: float
    ConnectionOverlapLengthOut: float
    ConnectionOverlapLengthIn: float
    GreaterThan180: bool
    OffsetOut: float
    OffsetIn: float
    CurveGroupType: CurbReturnCurveGroupType
    UpdateMode: AlignmentUpdateModeType
    OutgoingParentAlignmentId: ObjectId
    IncomingParentAlignmentId: ObjectId

class ConnectedAlignmentSSCSSInfo(ConnectedAlignmentInfo):
    """.NET: Autodesk.Civil.DatabaseServices.ConnectedAlignmentSSCSSInfo"""
    def __init__(self, *args) -> None: ...
    ReverseSpiralOutLength: float
    SpiralOutLength: float
    SpiralInLength: float
    ReverseSpiralInLength: float
    SpiralDefinition: SpiralType
    CurveRadius: float
    ConnectionOverlapLengthOut: float
    ConnectionOverlapLengthIn: float
    GreaterThan180: bool
    OffsetOut: float
    OffsetIn: float
    CurveGroupType: CurbReturnCurveGroupType
    UpdateMode: AlignmentUpdateModeType
    OutgoingParentAlignmentId: ObjectId
    IncomingParentAlignmentId: ObjectId

class ConnectorPositionType:
    """.NET: Autodesk.Civil.DatabaseServices.ConnectorPositionType"""
    def __init__(self, *args) -> None: ...
    ...

class Corridor(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.Corridor"""
    def __init__(self, *args) -> None: ...
    StyleId: ObjectId
    StyleName: str
    RegionLockMode: CorridorRegionLockType
    IsOutOfDate: bool
    RebuildAutomatic: bool
    CorridorSurfaces: CorridorSurfaceCollection
    SlopePatterns: CorridorSlopePatternCollection
    FeatureLineCodeInfos: FeatureLineCodeInfoCollection
    Baselines: BaselineCollection
    CodeSetStyleId: ObjectId
    CodeSetStyleName: str
    MaximumTriangleSideLength: float
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ExportFeatureLinesAsCogoPoints(self, pointGroupName: str, codes: CorridorPointCodeSelector, baseLineRange: ValueType) -> ObjectId: ...
    def ExportSolids(self, params: ExportCorridorSolidsParams, targetDatabase: Database) -> ObjectIdCollection: ...
    def GetLinkCodes(self, ) -> list: ...
    def GetPointCodes(self, ) -> list: ...
    def GetShapeCodes(self, ) -> list: ...
    def GetTargets(self, ) -> SubassemblyTargetInfoCollection: ...
    def Rebuild(self, ) -> None: ...
    def SetTargets(self, updatedTargets: SubassemblyTargetInfoCollection) -> None: ...

class CorridorBaselineType:
    """.NET: Autodesk.Civil.DatabaseServices.CorridorBaselineType"""
    def __init__(self, *args) -> None: ...
    ...

class CorridorCodeCollection(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.CorridorCodeCollection"""
    def __init__(self, *args) -> None: ...
    Item: str
    Count: int
    CorridorId: ObjectId
    def Add(self, code: str) -> None: ...
    def Clear(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class CorridorCollection(CivilWrapper<AcDbDatabase>):
    """.NET: Autodesk.Civil.DatabaseServices.CorridorCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    def Add(self, corridorName: str, baselineName: str, alignmentId: ObjectId, profileId: ObjectId, baselineRegionName: str, assemblyId: ObjectId) -> ObjectId: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def RebuildAll(self, ) -> None: ...

class CorridorFeatureLine(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.CorridorFeatureLine"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    FeatureLinePoints: FeatureLinePointCollection
    CodeName: str
    CorridorId: ObjectId
    def ExportAsAlignment(self, alignmentName: str, siteId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId, alignmentType: AlignmentType) -> ObjectId: ...
    def ExportAsGradingFeatureLine(self, siteId: ObjectId, isDynamic: bool, featureLineName: str, layerId: ObjectId, styleId: ObjectId, smoothOption: GradingSmoothOption) -> ObjectId: ...
    def ExportAsPolyline3d(self, ) -> ObjectId: ...
    def ExportAsPolyline3dCollection(self, ) -> ObjectIdCollection: ...
    def ExportAsProfile(self, profileName: str, alignmentId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId) -> ObjectId: ...

class CorridorLinkDisplay:
    """.NET: Autodesk.Civil.DatabaseServices.CorridorLinkDisplay"""
    def __init__(self, *args) -> None: ...
    ...

class CorridorLinkDrawOverride:
    """.NET: Autodesk.Civil.DatabaseServices.CorridorLinkDrawOverride"""
    def __init__(self, *args) -> None: ...
    ...

class CorridorPointCodeOption:
    """.NET: Autodesk.Civil.DatabaseServices.CorridorPointCodeOption"""
    def __init__(self, *args) -> None: ...
    Selected: bool
    CodeName: str

class CorridorPointCodeSelector:
    """.NET: Autodesk.Civil.DatabaseServices.CorridorPointCodeSelector"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: CorridorPointCodeOption
    Item: CorridorPointCodeOption
    def GetAllCodes(self, ) -> list: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def SelectAll(self, ) -> None: ...
    def UnSelectAll(self, ) -> None: ...

class CorridorSection(Section):
    """.NET: Autodesk.Civil.DatabaseServices.CorridorSection"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    CorridorSurfaceId: ObjectId
    SourceName: str
    MaximumElevation: float
    MinmumElevation: float
    RightSwathWidth: float
    LeftSwathWidth: float
    RightOffset: float
    LeftOffset: float
    SourceType: SectionSourceType
    UpdateMode: SectionUpdateType
    Station: float
    SectionPoints: SectionPointCollection
    SourceId: ObjectId
    ParentId: ObjectId
    SampleLineId: ObjectId
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetCorridor(self, ) -> ObjectId: ...
    def GetLinkCodes(self, ) -> list: ...
    def GetPointCodes(self, ) -> list: ...
    def GetShapeCodes(self, ) -> list: ...
    def SetCorridor(self, corridorName: str) -> None: ...

class CorridorSlopePattern(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.CorridorSlopePattern"""
    def __init__(self, *args) -> None: ...
    EndStation: float
    StartStation: float
    BaselineGuid: Guid
    BaselineId: ObjectId
    FeatureLine2: CorridorFeatureLine
    FeatureLine1: CorridorFeatureLine
    StyleName: str
    StyleId: ObjectId
    CorridorId: ObjectId
    def GetGeometries(self, regionIndex: int) -> DBObjectCollection: ...

class CorridorSlopePatternCollection(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.CorridorSlopePatternCollection"""
    def __init__(self, *args) -> None: ...
    Item: CorridorSlopePattern
    Count: int
    CorridorId: ObjectId
    def Add(self, featureLine1: CorridorFeatureLine, featureLine2: CorridorFeatureLine, slopePatternStyleId: ObjectId) -> CorridorSlopePattern: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, slopePattern: CorridorSlopePattern) -> bool: ...
    def RemoveAt(self, index: int) -> bool: ...

class CorridorSurface(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.CorridorSurface"""
    def __init__(self, *args) -> None: ...
    Masks: CorridorSurfaceMaskCollection
    Boundaries: CorridorSurfaceBoundaryCollection
    RenderMaterialId: ObjectId
    OverhangCorrection: OverhangCorrectionType
    SectionStyleId: ObjectId
    SurfaceStyleId: ObjectId
    IsDraw: bool
    IsBuild: bool
    Description: str
    Name: str
    SurfaceId: ObjectId
    CorridorId: ObjectId
    def AddFeatureLineCode(self, codeName: str) -> None: ...
    def AddLinkCode(self, codeName: str, addAsBreakLine: bool) -> None: ...
    def FeatureLineCodeIsBreak(self, name: str) -> bool: ...
    def FeatureLineCodes(self, ) -> list: ...
    def FindElevationAtXY(self, x: float, y: float) -> float: ...
    def GetSampleElevations(self, startX: float, startY: float, endX: float, endY: float) -> Point3dCollection: ...
    def IsLinkCodeAsBreakLine(self, codeName: str) -> bool: ...
    def LinkCodes(self, ) -> list: ...
    def PointCodes(self, ) -> list: ...
    def RemoveFeatureLineCode(self, codeName: str) -> bool: ...
    def RemoveLinkCode(self, codeName: str) -> bool: ...
    def SetLinkCodeAsBreakLine(self, codeName: str, asBreakLine: bool) -> None: ...

class CorridorSurfaceBaseMask(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.CorridorSurfaceBaseMask"""
    def __init__(self, *args) -> None: ...
    IsDefinedFromPolygon: bool
    FeatureLineComponents: FeatureLineComponentCollection
    Description: str
    Name: str
    CorridorId: ObjectId
    def PolygonPoints(self, ) -> list: ...

class CorridorSurfaceBoundary(CorridorSurfaceBaseMask):
    """.NET: Autodesk.Civil.DatabaseServices.CorridorSurfaceBoundary"""
    def __init__(self, *args) -> None: ...
    IsCorridorExtents: bool
    BoundaryType: CorridorSurfaceBoundaryType
    IsDefinedFromPolygon: bool
    FeatureLineComponents: FeatureLineComponentCollection
    Description: str
    Name: str
    CorridorId: ObjectId
    def GetExtentsBoundaries(self, ) -> list: ...

class CorridorSurfaceBoundaryCollection(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.CorridorSurfaceBoundaryCollection"""
    def __init__(self, *args) -> None: ...
    Item: CorridorSurfaceBoundary
    Item: CorridorSurfaceBoundary
    Count: int
    CorridorId: ObjectId
    def Add(self, boundaryName: str, points: Point3dCollection) -> CorridorSurfaceBoundary: ...
    def AddCorridorExtentsBoundary(self, boundaryName: str) -> CorridorSurfaceBoundary: ...
    def BoundaryNames(self, ) -> list: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, boundary: CorridorSurfaceBoundary) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class CorridorSurfaceBoundaryType:
    """.NET: Autodesk.Civil.DatabaseServices.CorridorSurfaceBoundaryType"""
    def __init__(self, *args) -> None: ...
    ...

class CorridorSurfaceCollection(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.CorridorSurfaceCollection"""
    def __init__(self, *args) -> None: ...
    Item: CorridorSurface
    Item: CorridorSurface
    Count: int
    CorridorId: ObjectId
    def Add(self, corridorSurfaceName: str, styleId: ObjectId) -> CorridorSurface: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, corridorSurface: CorridorSurface) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...
    def SurfaceNames(self, ) -> list: ...

class CorridorSurfaceMask(CorridorSurfaceBaseMask):
    """.NET: Autodesk.Civil.DatabaseServices.CorridorSurfaceMask"""
    def __init__(self, *args) -> None: ...
    RenderMaterialId: ObjectId
    IsDefinedFromPolygon: bool
    FeatureLineComponents: FeatureLineComponentCollection
    Description: str
    Name: str
    CorridorId: ObjectId

class CorridorSurfaceMaskCollection(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.CorridorSurfaceMaskCollection"""
    def __init__(self, *args) -> None: ...
    Item: CorridorSurfaceMask
    Item: CorridorSurfaceMask
    Count: int
    CorridorId: ObjectId
    def Add(self, maskName: str, points: Point3dCollection) -> CorridorSurfaceMask: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def MaskNames(self, ) -> list: ...
    def Remove(self, mask: CorridorSurfaceMask) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class CorridorTransition:
    """.NET: Autodesk.Civil.DatabaseServices.CorridorTransition"""
    def __init__(self, *args) -> None: ...
    Side: SubassemblySideType
    HasSide: bool
    TransitionType: CorridorTransitionType
    EndValue: object
    StartValue: object
    EndStation: float
    HasEndStation: bool
    StartStation: float
    HasStartStation: bool
    ParameterName: str

class CorridorTransitionNameType:
    """.NET: Autodesk.Civil.DatabaseServices.CorridorTransitionNameType"""
    def __init__(self, *args) -> None: ...
    ...

class CorridorTransitionSet(DisposableWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.CorridorTransitionSet"""
    def __init__(self, *args) -> None: ...
    TransitionCount: int
    NameType: CorridorTransitionNameType
    SubassemblyName: str
    StationLocked: bool
    Comment: str
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddTransition(self, parameterName: str) -> CorridorTransition: ...
    def GetTransitionAt(self, index: int) -> CorridorTransition: ...

class CorridorTransitionType:
    """.NET: Autodesk.Civil.DatabaseServices.CorridorTransitionType"""
    def __init__(self, *args) -> None: ...
    ...

class CrossingPipeProfileLabel(PartProfileLabel):
    """.NET: Autodesk.Civil.DatabaseServices.CrossingPipeProfileLabel"""
    def __init__(self, *args) -> None: ...
    ReferenceAlignmentId: ObjectId
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(profileViewPartId: ObjectId, profileViewId: ObjectId, labelStyleId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelIds(profileViewPartId: ObjectId, profileViewId: ObjectId) -> ObjectIdCollection: ...

class CurbReturnJoiningType:
    """.NET: Autodesk.Civil.DatabaseServices.CurbReturnJoiningType"""
    def __init__(self, *args) -> None: ...
    ...

class CurveCurveReverseCurveTransitionDescription(TransitionDescriptionBase):
    """.NET: Autodesk.Civil.DatabaseServices.CurveCurveReverseCurveTransitionDescription"""
    def __init__(self, *args) -> None: ...
    ReverseCurveRadius: float
    SecondCurveRadius: float
    FirstCurveRadius: float
    StartStation: float
    Length: float
    EndStation: float

class CurveLineCurveTransitionDescription(TransitionDescriptionBase):
    """.NET: Autodesk.Civil.DatabaseServices.CurveLineCurveTransitionDescription"""
    def __init__(self, *args) -> None: ...
    ExitCurveRadius: float
    EntryCurveRadius: float
    StartStation: float
    Length: float
    EndStation: float

class CurveParamType:
    """.NET: Autodesk.Civil.DatabaseServices.CurveParamType"""
    def __init__(self, *args) -> None: ...
    ...

class CurveReverseCurveTransitionDescription(TransitionDescriptionBase):
    """.NET: Autodesk.Civil.DatabaseServices.CurveReverseCurveTransitionDescription"""
    def __init__(self, *args) -> None: ...
    ReverseCurveRadius: float
    EntryCurveRadius: float
    StartStation: float
    Length: float
    EndStation: float

class CurveType:
    """.NET: Autodesk.Civil.DatabaseServices.CurveType"""
    def __init__(self, *args) -> None: ...
    ...

class CustomPointGroupQuery(PointGroupQuery):
    """.NET: Autodesk.Civil.DatabaseServices.CustomPointGroupQuery"""
    def __init__(self, *args) -> None: ...
    QueryString: str
    UseCaseSensitiveMatch: bool

class DBObject(DBObject):
    """.NET: Autodesk.Civil.DatabaseServices.DBObject"""
    def __init__(self, *args) -> None: ...
    IsUsed: bool
    Description: str
    Name: str
    Document: object
    Application: object
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class DatumRoundingType:
    """.NET: Autodesk.Civil.DatabaseServices.DatumRoundingType"""
    def __init__(self, *args) -> None: ...
    ...

class DesignSpeed(CivilWrapper<AeccDbAlignment>):
    """.NET: Autodesk.Civil.DatabaseServices.DesignSpeed"""
    def __init__(self, *args) -> None: ...
    Comment: str
    Value: float
    Station: float
    SpeedNumber: int

class DesignSpeedCollection(CivilWrapper<AeccDbAlignment>):
    """.NET: Autodesk.Civil.DatabaseServices.DesignSpeedCollection"""
    def __init__(self, *args) -> None: ...
    Item: DesignSpeed
    Count: int
    def Add(self, station: float, speed: float) -> DesignSpeed: ...
    def GetDesignSpeed(self, rawStation: float) -> DesignSpeed: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, rawStation: float) -> None: ...

class DomainType:
    """.NET: Autodesk.Civil.DatabaseServices.DomainType"""
    def __init__(self, *args) -> None: ...
    ...

class ElevationRangeType:
    """.NET: Autodesk.Civil.DatabaseServices.ElevationRangeType"""
    def __init__(self, *args) -> None: ...
    ...

class Entity(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.Entity"""
    def __init__(self, *args) -> None: ...
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ComputeFingerPrint(self, ) -> int: ...
    def GetReferenceInfo(self, ) -> DataShortcutKey: ...

class EntityAttachType:
    """.NET: Autodesk.Civil.DatabaseServices.EntityAttachType"""
    def __init__(self, *args) -> None: ...
    ...

class EntityVerticalConstraintType:
    """.NET: Autodesk.Civil.DatabaseServices.EntityVerticalConstraintType"""
    def __init__(self, *args) -> None: ...
    ...

class Event:
    """.NET: Autodesk.Civil.DatabaseServices.Event"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def Log(type: Type, source: str, text: str, database: Database) -> None: ...

class ExportCorridorSolidsParams:
    """.NET: Autodesk.Civil.DatabaseServices.ExportCorridorSolidsParams"""
    def __init__(self, *args) -> None: ...
    ExcludedCodes: list
    IncludedCodes: list
    SweepSolidForShape: bool
    CreateSolidForShape: bool
    ExportLinks: bool
    ExportShapes: bool

class Feature(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.Feature"""
    def __init__(self, *args) -> None: ...
    IsEditable: bool
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def IsEditableFeature(featureId: ObjectId) -> bool: ...

class FeatureLabel(Label):
    """.NET: Autodesk.Civil.DatabaseServices.FeatureLabel"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class FeatureLine(Feature):
    """.NET: Autodesk.Civil.DatabaseServices.FeatureLine"""
    def __init__(self, *args) -> None: ...
    CurvesCount: int
    ElevationPointsCount: int
    PIPointsCount: int
    PointsCount: int
    RelativeSurfaceId: ObjectId
    Length3D: float
    Length2D: float
    MaxGrade: float
    MinGrade: float
    MaxElevation: float
    MinElevation: float
    SiteId: ObjectId
    StyleName: str
    StyleId: ObjectId
    IsEditable: bool
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AssignElevationsFromSurface(self, surfaceId: ObjectId, bIncIntermediate: bool) -> None: ...
    @staticmethod
    def Create(featurelineName: str, idCreatedFrom: ObjectId, siteId: ObjectId) -> ObjectId: ...
    def DeleteElevationPoint(self, pt: Point3d) -> None: ...
    def DeleteElevationPoints(self, cliPoints: Point3dCollection) -> None: ...
    def DeletePIPoint(self, pt: Point3d) -> None: ...
    def ExtendWithFixedCurve(self, extendFromStart: bool, secondPoint: Point3d, targetPoint: Point3d) -> None: ...
    def ExtendWithFixedLine(self, extendFromStart: bool, length: float) -> None: ...
    def Get3dDistanceAtPoint(self, pt: Point3d) -> float: ...
    def GetBulge(self, index: int) -> float: ...
    def GetCurveRadius(self, index: int) -> float: ...
    def GetDeflectionAngleAtPoint(self, pt: Point3d) -> float: ...
    def GetGradeInAtPoint(self, pt: Point3d) -> float: ...
    def GetGradeOutAtPoint(self, pt: Point3d) -> float: ...
    def GetPointRelativeElevation(self, pt: Point3d) -> float: ...
    def GetPoints(self, type: FeatureLinePointType) -> Point3dCollection: ...
    def InsertElevationPoint(self, pt: Point3d) -> None: ...
    def InsertElevationPoints(self, cliPoints: Point3dCollection) -> None: ...
    def InsertPIPoint(self, pt: Point3d) -> None: ...
    def IsElevationRelativeToSurface(self, pt: Point3d) -> bool: ...
    @staticmethod
    def MoveToNoneSite(featureLineId: ObjectId) -> None: ...
    @staticmethod
    def MoveToSite(featureLineId: ObjectId, destinationSiteId: ObjectId) -> None: ...
    def SetBulge(self, index: int, bugle: float) -> None: ...
    def SetCurveRadius(self, index: int, radius: float) -> None: ...
    def SetPointElevation(self, index: int, elevation: float) -> None: ...
    def SetPointRelativeElevation(self, pt: Point3d, relative: bool, elevation: float) -> None: ...

class FeatureLineCodeInfo(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.FeatureLineCodeInfo"""
    def __init__(self, *args) -> None: ...
    PayItems: list
    IsConnected: bool
    IsConnect: bool
    IsDraw: bool
    CodeName: str
    CorridorId: ObjectId

class FeatureLineCodeInfoCollection(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.FeatureLineCodeInfoCollection"""
    def __init__(self, *args) -> None: ...
    Item: FeatureLineCodeInfo
    Item: FeatureLineCodeInfo
    Count: int
    CorridorId: ObjectId
    def CodeNames(self, ) -> list: ...
    def GetConnectedFeatureLineCodeInfos(self, ) -> list: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class FeatureLineCollection(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.FeatureLineCollection"""
    def __init__(self, *args) -> None: ...
    ConnectDirection: FeatureLineConnectDirectionType
    IsConnectExtraPoints: bool
    FeatureLineCodeInfo: FeatureLineCodeInfo
    Item: CorridorFeatureLine
    Count: int
    CorridorId: ObjectId
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class FeatureLineCollectionMap(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.FeatureLineCollectionMap"""
    def __init__(self, *args) -> None: ...
    Item: FeatureLineCollection
    Item: FeatureLineCollection
    Count: int
    CorridorId: ObjectId
    def CodeNames(self, ) -> list: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class FeatureLineComponent(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.FeatureLineComponent"""
    def __init__(self, *args) -> None: ...
    UseEndStation: bool
    UseStartStation: bool
    EndStation: float
    StartStation: float
    IsReversed: bool
    FeatureLine: CorridorFeatureLine
    BaselineAlignmentId: ObjectId
    CorridorId: ObjectId

class FeatureLineComponentCollection(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.FeatureLineComponentCollection"""
    def __init__(self, *args) -> None: ...
    Item: FeatureLineComponent
    Count: int
    CorridorId: ObjectId
    def Add(self, featureLine: CorridorFeatureLine) -> FeatureLineComponent: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, featureLineComponent: FeatureLineComponent) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...
    def Swap(self, component1: FeatureLineComponent, component2: FeatureLineComponent) -> None: ...
    def SwapAt(self, index1: int, index2: int) -> None: ...
    def Validate(self, ) -> bool: ...

class FeatureLinePoint(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.FeatureLinePoint"""
    def __init__(self, *args) -> None: ...
    IsBreak: bool
    XYZ: Point3d
    Offset: float
    Station: float
    CorridorId: ObjectId

class FeatureLinePointCollection(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.FeatureLinePointCollection"""
    def __init__(self, *args) -> None: ...
    Item: FeatureLinePoint
    Count: int
    CorridorId: ObjectId
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class FlowDirectionMethodType:
    """.NET: Autodesk.Civil.DatabaseServices.FlowDirectionMethodType"""
    def __init__(self, *args) -> None: ...
    ...

class FlowDirectionType:
    """.NET: Autodesk.Civil.DatabaseServices.FlowDirectionType"""
    def __init__(self, *args) -> None: ...
    ...

class FlowPath:
    """.NET: Autodesk.Civil.DatabaseServices.FlowPath"""
    def __init__(self, *args) -> None: ...
    FlowSegmentCount: int
    def AddSegment(self, indexOfOriginalSegment: int, distanceFromFlowSegmentStartPoint: float) -> FlowSegment: ...
    def Clear(self, ) -> None: ...
    def GetFlowSegmentAt(self, index: int) -> FlowSegment: ...
    def GetPath(self, ) -> Point3dCollection: ...
    def RemoveSegment(self, index: int) -> None: ...
    def SetPath(self, vertices: Point3dCollection) -> None: ...
    def SetPathFromSurface(self, mostDistantPoint: Point2d) -> None: ...

class FlowSegment:
    """.NET: Autodesk.Civil.DatabaseServices.FlowSegment"""
    def __init__(self, *args) -> None: ...
    IsTravelTimeCalculated: bool
    TravelTime: float
    Velocity: float
    WettedPerimeter: float
    CrossSectionArea: float
    ManningRoughness: float
    SurfaceType: ShallowFlowSurfaceType
    Rainfall2yr24hr: float
    Slope: float
    Length: float
    FlowType: TR55FlowSegmentType
    Index: int
    def Dispose(self, ) -> None: ...
    def SetFlowType(self, flowType: TR55FlowSegmentType) -> bool: ...

class FlowSegmentLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.FlowSegmentLabel"""
    def __init__(self, *args) -> None: ...
    FlowSegmentIndex: int
    Ratio: float
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(flowSegment: FlowSegment, labelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelIds(catchmentId: ObjectId) -> ObjectIdCollection: ...

class Folder(DBObject):
    """.NET: Autodesk.Civil.DatabaseServices.Folder"""
    def __init__(self, *args) -> None: ...
    IsUsed: bool
    Description: str
    Name: str
    Document: object
    Application: object
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddEntity(self, entityId: ObjectId) -> None: ...
    def CreateFolder(self, name: str) -> ObjectId: ...
    def DeleteFolder(self, ) -> None: ...
    def GetFolder(self, nameOrPath: str) -> ObjectId: ...
    def GetParent(self, ) -> ObjectId: ...
    def GetPath(self, ) -> str: ...
    def GetSubFolders(self, ) -> ObjectIdCollection: ...
    def RenameFolder(self, newName: str) -> None: ...

class FolderUtil:
    """.NET: Autodesk.Civil.DatabaseServices.FolderUtil"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetAlignmentRootFolder(aType: AlignmentType, database: Database) -> ObjectId: ...
    @staticmethod
    def GetNonAlignmentRootFolder(rxClass: RXClass, database: Database) -> ObjectId: ...

class GeneralSegmentLabel(Label):
    """.NET: Autodesk.Civil.DatabaseServices.GeneralSegmentLabel"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    CurveLabelStyleId: ObjectId
    LineLabelStyleId: ObjectId
    Ratio: float
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(featureId: ObjectId, ratio: float, lineLabelStyleId: ObjectId, curveLabelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelIds(featureId: ObjectId) -> ObjectIdCollection: ...

class GeneralSurfaceProperties:
    """.NET: Autodesk.Civil.DatabaseServices.GeneralSurfaceProperties"""
    def __init__(self, *args) -> None: ...
    MeanElevation: float
    MaximumElevation: float
    MinimumElevation: float
    MaximumCoordinateY: float
    MaximumCoordinateX: float
    MinimumCoordinateY: float
    MinimumCoordinateX: float
    NumberOfPoints: int
    RevisionNumber: int

class GeoEntity(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.GeoEntity"""
    def __init__(self, *args) -> None: ...
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Grading(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.Grading"""
    def __init__(self, *args) -> None: ...
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GradingSmoothOption:
    """.NET: Autodesk.Civil.DatabaseServices.GradingSmoothOption"""
    def __init__(self, *args) -> None: ...
    HorizDeviation: float
    WeedingDistance: float
    ArcInclusionDistance: float
    NeedSmooth: bool

class Graph(GeoEntity):
    """.NET: Autodesk.Civil.DatabaseServices.Graph"""
    def __init__(self, *args) -> None: ...
    Location: Point3d
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GraphBandSet:
    """.NET: Autodesk.Civil.DatabaseServices.GraphBandSet"""
    def __init__(self, *args) -> None: ...
    MatchIncrementToGridIntervals: bool
    def ImportBandSetStyle(self, bandSetId: ObjectId) -> None: ...
    def SaveAsBandSetStyle(self, name: str) -> ObjectId: ...

class GraphDisplayOption(DisposableWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.GraphDisplayOption"""
    def __init__(self, *args) -> None: ...
    LabelSetId: ObjectId
    OverrideStyleId: ObjectId
    OverrideStyleName: str
    UseOverrideStyle: bool
    Draw: bool
    SourceName: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GraphDisplayOptionCollection:
    """.NET: Autodesk.Civil.DatabaseServices.GraphDisplayOptionCollection`1"""
    def __init__(self, *args) -> None: ...
    ClipGridAt: str
    Count: int
    Item: ItemType
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class GraphOverride(CivilWrapper<AeccDbGraph>):
    """.NET: Autodesk.Civil.DatabaseServices.GraphOverride"""
    def __init__(self, *args) -> None: ...
    OverrideStyleId: ObjectId
    OverrideStyleName: str
    UseOverrideStyle: bool
    Draw: bool

class GraphOverrideCollection:
    """.NET: Autodesk.Civil.DatabaseServices.GraphOverrideCollection`1"""
    def __init__(self, *args) -> None: ...
    ClipGridAt: str
    Count: int
    Item: ItemType
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class GraphRangeOptions:
    """.NET: Autodesk.Civil.DatabaseServices.GraphRangeOptions"""
    def __init__(self, *args) -> None: ...
    ...

class GridLocation:
    """.NET: Autodesk.Civil.DatabaseServices.GridLocation"""
    def __init__(self, *args) -> None: ...
    RowIndex: int
    ColumnIndex: int
    def Equals(self, obj: object) -> bool: ...

class GridSurface(Surface):
    """.NET: Autodesk.Civil.DatabaseServices.GridSurface"""
    def __init__(self, *args) -> None: ...
    Cells: GridSurfaceCellCollection
    Vertices: GridSurfaceVertexCollection
    DEMFilesDefinition: SurfaceDefinitionDEMFiles
    OriginationType: SurfaceOriginationType
    IsLevelOfDetailEnabled: bool
    Masks: SurfaceMaskCollection
    AutoRebuild: bool
    Lock: bool
    StyleId: ObjectId
    IsSnapshotOutOfDate: bool
    HasSnapshot: bool
    IsOutOfDate: bool
    PartialReferenceBoundaryManager: SurfacePartialReferenceBoundaryMgr
    BuildOptions: SurfaceBuildOptions
    Operations: SurfaceOperationCollection
    BoundariesDefinition: SurfaceDefinitionBoundaries
    Analysis: SurfaceAnalysis
    IsVolumeSurface: bool
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddPoint(self, location: GridLocation, elevation: float) -> SurfaceOperationAddGridPoint: ...
    @staticmethod
    def Create(surfaceName: str, spacingX: float, spacingY: float, orientation: float, styleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def CreateFromDEM(DEMFileName: str, styleId: ObjectId) -> ObjectId: ...
    def DeleteLine(self, edge: GridSurfaceEdge) -> SurfaceOperationDeleteLine: ...
    def DeleteLines(self, edges: IEnumerable) -> SurfaceOperationDeleteMultipleLines: ...
    def DeletePoint(self, location: GridLocation) -> SurfaceOperationDeleteGridPoint: ...
    def DeletePoints(self, locations: IEnumerable) -> SurfaceOperationDeleteMultipleGridPoints: ...
    def ExtractBorder(self, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection: ...
    def ExtractContours(self, lowElev: float, highElev: float, interval: float, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection: ...
    def ExtractContoursAt(self, elevation: float, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection: ...
    def ExtractGridded(self, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection: ...
    def ExtractMajorContours(self, settingsType: SurfaceExtractionSettingsType, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection: ...
    def ExtractMinorContours(self, settingsType: SurfaceExtractionSettingsType, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection: ...
    def ExtractWatershed(self, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection: ...
    def FindCellAtXY(self, x: float, y: float) -> GridSurfaceCell: ...
    def FindEdgeAtXY(self, x: float, y: float) -> GridSurfaceEdge: ...
    def FindVertexAtXY(self, x: float, y: float) -> GridSurfaceVertex: ...
    def GetCells(self, includeInvisible: bool) -> GridSurfaceCellCollection: ...
    def GetGridProperties(self, ) -> GridSurfaceProperties: ...
    def GetTerrainProperties(self, ) -> TerrainSurfaceProperties: ...
    def GetVertices(self, includeInvisible: bool) -> GridSurfaceVertexCollection: ...
    def RaisePoints(self, locations: IEnumerable, deltaElevation: float) -> SurfaceOperationModifyMultipleGridPointsElevation: ...
    def RaiseSurface(self, deltaElevation: float) -> SurfaceOperationRaise: ...
    def SampleElevations(self, pt1: Point3d, pt2: Point3d) -> Point3dCollection: ...
    def SetPointElevation(self, location: GridLocation, newElevation: float) -> SurfaceOperationModifyGridPointElevation: ...
    def SetPointsElevation(self, locations: IEnumerable, newElevation: float) -> SurfaceOperationModifyMultipleGridPointsElevation: ...

class GridSurfaceCell(GridSurfaceObject):
    """.NET: Autodesk.Civil.DatabaseServices.GridSurfaceCell"""
    def __init__(self, *args) -> None: ...
    BottomEdge: GridSurfaceEdge
    RightEdge: GridSurfaceEdge
    TopEdge: GridSurfaceEdge
    LeftEdge: GridSurfaceEdge
    BottomRightVertex: GridSurfaceVertex
    BottomLeftVertex: GridSurfaceVertex
    TopRightVertex: GridSurfaceVertex
    TopLeftVertex: GridSurfaceVertex
    GridLocation: GridLocation
    Surface: GridSurface
    IsValid: bool
    def Equals(self, rhs: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class GridSurfaceCellCollection:
    """.NET: Autodesk.Civil.DatabaseServices.GridSurfaceCellCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    def Contains(self, location: GridLocation) -> bool: ...
    def GetAt(self, location: GridLocation) -> GridSurfaceCell: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetIndexRange(self, minColIndex: int, minRowIndex: int, maxColIndex: int, maxRowIndex: int) -> None: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class GridSurfaceCellEnumerator:
    """.NET: Autodesk.Civil.DatabaseServices.GridSurfaceCellEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: GridSurfaceCell
    CurrentObject: object
    def Dispose(self, ) -> None: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class GridSurfaceEdge(GridSurfaceObject):
    """.NET: Autodesk.Civil.DatabaseServices.GridSurfaceEdge"""
    def __init__(self, *args) -> None: ...
    Cell2: GridSurfaceCell
    Cell1: GridSurfaceCell
    Vertex2: GridSurfaceVertex
    Vertex1: GridSurfaceVertex
    IsValid: bool
    Surface: GridSurface
    def Equals(self, rhs: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class GridSurfaceObject:
    """.NET: Autodesk.Civil.DatabaseServices.GridSurfaceObject"""
    def __init__(self, *args) -> None: ...
    Surface: GridSurface
    IsValid: bool
    def Dispose(self, ) -> None: ...

class GridSurfaceProperties:
    """.NET: Autodesk.Civil.DatabaseServices.GridSurfaceProperties"""
    def __init__(self, *args) -> None: ...
    Orientation: float
    SpacingY: float
    SpacingX: float

class GridSurfaceVertex(GridSurfaceObject):
    """.NET: Autodesk.Civil.DatabaseServices.GridSurfaceVertex"""
    def __init__(self, *args) -> None: ...
    Location: Point3d
    GridLocation: GridLocation
    Surface: GridSurface
    IsValid: bool
    def Equals(self, rhs: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class GridSurfaceVertexCollection:
    """.NET: Autodesk.Civil.DatabaseServices.GridSurfaceVertexCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    def Contains(self, location: GridLocation) -> bool: ...
    def GetAt(self, location: GridLocation) -> GridSurfaceVertex: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetIndexRange(self, minColIndex: int, minRowIndex: int, maxColIndex: int, maxRowIndex: int) -> None: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class GridSurfaceVertexEnumerator:
    """.NET: Autodesk.Civil.DatabaseServices.GridSurfaceVertexEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: GridSurfaceVertex
    CurrentObject: object
    def Dispose(self, ) -> None: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class GridVolumeSurface(Surface):
    """.NET: Autodesk.Civil.DatabaseServices.GridVolumeSurface"""
    def __init__(self, *args) -> None: ...
    FillFactor: float
    CutFactor: float
    OriginationType: SurfaceOriginationType
    IsLevelOfDetailEnabled: bool
    Masks: SurfaceMaskCollection
    AutoRebuild: bool
    Lock: bool
    StyleId: ObjectId
    IsSnapshotOutOfDate: bool
    HasSnapshot: bool
    IsOutOfDate: bool
    PartialReferenceBoundaryManager: SurfacePartialReferenceBoundaryMgr
    BuildOptions: SurfaceBuildOptions
    Operations: SurfaceOperationCollection
    BoundariesDefinition: SurfaceDefinitionBoundaries
    Analysis: SurfaceAnalysis
    IsVolumeSurface: bool
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(surfaceName: str, baseSurfaceId: ObjectId, comparisonSurfaceId: ObjectId, spacingX: float, spacingY: float, orientation: float, styleId: ObjectId) -> ObjectId: ...
    def GetGridProperties(self, ) -> GridSurfaceProperties: ...
    def GetVolumeProperties(self, ) -> VolumeSurfaceProperties: ...

class HardcodedOffsetBaseline(BaseBaseline):
    """.NET: Autodesk.Civil.DatabaseServices.HardcodedOffsetBaseline"""
    def __init__(self, *args) -> None: ...
    RelatedOffsetBaselineFeatureLines: BaselineFeatureLines
    OffsetElevationFromMainBaseline: Point2d
    Name: str
    ProfileId: ObjectId
    AlignmentId: ObjectId
    BaselineType: CorridorBaselineType
    DirectionAtStation: Vector3d
    EndStation: float
    StartStation: float
    baselineGUID: Guid
    BaselineGuid: Guid
    FeatureLineId: ObjectId
    CorridorId: ObjectId
    def IsFeatureLineBased(self, ) -> bool: ...
    def SortedStations(self, ) -> list: ...

class HatchCriteriaBoundaryType:
    """.NET: Autodesk.Civil.DatabaseServices.HatchCriteriaBoundaryType"""
    def __init__(self, *args) -> None: ...
    ...

class HoldOnResizeType:
    """.NET: Autodesk.Civil.DatabaseServices.HoldOnResizeType"""
    def __init__(self, *args) -> None: ...
    ...

class HorizontalGeometryBandLabelGroup(ProfileBandLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.HorizontalGeometryBandLabelGroup"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(profileViewId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class HydrographShapeType:
    """.NET: Autodesk.Civil.DatabaseServices.HydrographShapeType"""
    def __init__(self, *args) -> None: ...
    ...

class HydrologicalSoilGroup:
    """.NET: Autodesk.Civil.DatabaseServices.HydrologicalSoilGroup"""
    def __init__(self, *args) -> None: ...
    ...

class IAppliedSubassemblyParam:
    """.NET: Autodesk.Civil.DatabaseServices.IAppliedSubassemblyParam"""
    def __init__(self, *args) -> None: ...
    ValueAsObject: object
    DesignValueAsObject: object
    ValueType: Type
    IsOverriden: bool
    Comment: str
    DisplayName: str
    KeyName: str
    def ClearOverride(self, ) -> bool: ...

class ICommonLabel:
    """.NET: Autodesk.Civil.DatabaseServices.ICommonLabel"""
    def __init__(self, *args) -> None: ...
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    def ClearAllTextComponentOverrides(self, ) -> None: ...
    def GetReferenceTextTarget(self, referenceTextComponentId: ObjectId) -> ObjectId: ...
    def GetTextComponentIds(self, ) -> ObjectIdCollection: ...
    def GetTextComponentJustificationOverride(self, labelStyleComponentId: ObjectId) -> TextJustificationType: ...
    def GetTextComponentOverride(self, labelStyleComponentId: ObjectId) -> str: ...
    def IsTextComponentOverriden(self, labelStyleComponentId: ObjectId) -> bool: ...
    def Reset(self, ) -> None: ...
    def ResetLocation(self, ) -> None: ...
    def ResetProperties(self, ) -> None: ...
    def SetReferenceTextTarget(self, referenceTextComponentId: ObjectId, referenceObjectId: ObjectId) -> None: ...
    def SetTextComponentJustificationOverride(self, labelStyleComponentId: ObjectId, textJustificationType: TextJustificationType) -> None: ...
    def SetTextComponentOverride(self, labelStyleComponentId: ObjectId, textOverride: str, textJustificationType: TextJustificationType) -> None: ...

class ICommonLabelOptions:
    """.NET: Autodesk.Civil.DatabaseServices.ICommonLabelOptions"""
    def __init__(self, *args) -> None: ...
    RotationType: LabelRotationType
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool

class IGridSurface:
    """.NET: Autodesk.Civil.DatabaseServices.IGridSurface"""
    def __init__(self, *args) -> None: ...
    def GetGridProperties(self, ) -> GridSurfaceProperties: ...

class IPoint:
    """.NET: Autodesk.Civil.DatabaseServices.IPoint"""
    def __init__(self, *args) -> None: ...
    Index: int
    Elevation: float
    Offset: float
    Station: float
    Codes: CodeCollection

class ITerrainSurface:
    """.NET: Autodesk.Civil.DatabaseServices.ITerrainSurface"""
    def __init__(self, *args) -> None: ...
    DEMFilesDefinition: SurfaceDefinitionDEMFiles
    def ExtractBorder(self, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection: ...
    def ExtractContours(self, lowElev: float, highElev: float, interval: float, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection: ...
    def ExtractContoursAt(self, elevation: float, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection: ...
    def ExtractGridded(self, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection: ...
    def ExtractMajorContours(self, settingsType: SurfaceExtractionSettingsType, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection: ...
    def ExtractMinorContours(self, settingsType: SurfaceExtractionSettingsType, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection: ...
    def ExtractWatershed(self, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection: ...
    def GetTerrainProperties(self, ) -> TerrainSurfaceProperties: ...
    def RaiseSurface(self, deltaElevation: float) -> SurfaceOperationRaise: ...
    def SampleElevations(self, curveId: ObjectId) -> Point3dCollection: ...

class ITinSurface:
    """.NET: Autodesk.Civil.DatabaseServices.ITinSurface"""
    def __init__(self, *args) -> None: ...
    def GetTinProperties(self, ) -> TinSurfaceProperties: ...

class IVolumeSurface:
    """.NET: Autodesk.Civil.DatabaseServices.IVolumeSurface"""
    def __init__(self, *args) -> None: ...
    FillFactor: float
    CutFactor: float
    def GetVolumeProperties(self, ) -> VolumeSurfaceProperties: ...

class InfiltrationMethod:
    """.NET: Autodesk.Civil.DatabaseServices.InfiltrationMethod"""
    def __init__(self, *args) -> None: ...
    ...

class InitialAbstractionType:
    """.NET: Autodesk.Civil.DatabaseServices.InitialAbstractionType"""
    def __init__(self, *args) -> None: ...
    ...

class InletGrateType:
    """.NET: Autodesk.Civil.DatabaseServices.InletGrateType"""
    def __init__(self, *args) -> None: ...
    ...

class InletLocationType:
    """.NET: Autodesk.Civil.DatabaseServices.InletLocationType"""
    def __init__(self, *args) -> None: ...
    ...

class InletThroatAngleType:
    """.NET: Autodesk.Civil.DatabaseServices.InletThroatAngleType"""
    def __init__(self, *args) -> None: ...
    ...

class Interference(GeoEntity):
    """.NET: Autodesk.Civil.DatabaseServices.Interference"""
    def __init__(self, *args) -> None: ...
    Network2Id: ObjectId
    Network1Id: ObjectId
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class InterferenceCheck(GeoEntity):
    """.NET: Autodesk.Civil.DatabaseServices.InterferenceCheck"""
    def __init__(self, *args) -> None: ...
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class InternalRouting:
    """.NET: Autodesk.Civil.DatabaseServices.InternalRouting"""
    def __init__(self, *args) -> None: ...
    ...

class Intersection(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.Intersection"""
    def __init__(self, *args) -> None: ...
    Location: Point3d
    RoadwayDrivingDirection: DrivingDirectionType
    GradeRuleType: IntersectionCorridorType
    IntersectionRegions: IntersectionRegionCollection
    IntersectionRoads: IntersectionRoadCollection
    CorridorId: ObjectId
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetIntersectionLocaitonLabelIds(self, ) -> ObjectIdCollection: ...

class IntersectionCorridorType:
    """.NET: Autodesk.Civil.DatabaseServices.IntersectionCorridorType"""
    def __init__(self, *args) -> None: ...
    ...

class IntersectionLocationLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.IntersectionLocationLabel"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(intersectionId: ObjectId, labelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelIds(intersectionId: ObjectId) -> ObjectIdCollection: ...

class IntersectionRegion(CivilWrapper<AeccDbIntersection>):
    """.NET: Autodesk.Civil.DatabaseServices.IntersectionRegion"""
    def __init__(self, *args) -> None: ...
    OutAlignmentId: ObjectId
    InAlignmentId: ObjectId
    Angle: float
    Name: str
    CurbReturnProfileId: ObjectId
    CurbReturnAlignmentId: ObjectId

class IntersectionRegionCollection(CivilWrapper<AeccDbIntersection>):
    """.NET: Autodesk.Civil.DatabaseServices.IntersectionRegionCollection"""
    def __init__(self, *args) -> None: ...
    Item: IntersectionRegion
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class IntersectionRoad(CivilWrapper<AeccDbIntersection>):
    """.NET: Autodesk.Civil.DatabaseServices.IntersectionRoad"""
    def __init__(self, *args) -> None: ...
    OffsetRightProfileId: ObjectId
    OffsetRightAlignmentId: ObjectId
    OffsetLeftProfileId: ObjectId
    OffsetLeftAlignmentId: ObjectId
    CenterlineProfileId: ObjectId
    CenterlineAlignmentId: ObjectId

class IntersectionRoadCollection(CivilWrapper<AeccDbIntersection>):
    """.NET: Autodesk.Civil.DatabaseServices.IntersectionRoadCollection"""
    def __init__(self, *args) -> None: ...
    Item: IntersectionRoad
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class KrigingMethodOptions:
    """.NET: Autodesk.Civil.DatabaseServices.KrigingMethodOptions"""
    def __init__(self, *args) -> None: ...
    NuggetEffect: float
    VariogramParamC: float
    VariogramParamA: float
    SemivariogramModel: KrigingSemivariogramType
    SampleVertices: IEnumerable

class Label(LabelBase):
    """.NET: Autodesk.Civil.DatabaseServices.Label"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ClearAllTextComponentOverrides(self, ) -> None: ...
    def GetReferenceTextTarget(self, referenceTextComponentId: ObjectId) -> ObjectId: ...
    def GetTextComponentIds(self, ) -> ObjectIdCollection: ...
    def GetTextComponentJustificationOverride(self, labelStyleComponentId: ObjectId) -> TextJustificationType: ...
    def GetTextComponentOverride(self, labelStyleComponentId: ObjectId) -> str: ...
    def IsTextComponentOverriden(self, labelStyleComponentId: ObjectId) -> bool: ...
    def Reset(self, ) -> None: ...
    def ResetLocation(self, ) -> None: ...
    def ResetProperties(self, ) -> None: ...
    def SetReferenceTextTarget(self, referenceTextComponentId: ObjectId, referenceObjectId: ObjectId) -> None: ...
    def SetTextComponentJustificationOverride(self, labelStyleComponentId: ObjectId, textJustificationType: TextJustificationType) -> None: ...
    def SetTextComponentOverride(self, labelStyleComponentId: ObjectId, textOverride: str, textJustificationType: TextJustificationType) -> None: ...

class LabelBase(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.LabelBase"""
    def __init__(self, *args) -> None: ...
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelGroup(LabelBase):
    """.NET: Autodesk.Civil.DatabaseServices.LabelGroup"""
    def __init__(self, *args) -> None: ...
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetAt(self, index: int) -> LabelGroupSubEntity: ...
    def ResetAllSubCommonLabelLocations(self, ) -> None: ...
    def ResetAllSubCommonLabelProperties(self, ) -> None: ...
    def ResetAllSubCommonLabels(self, ) -> None: ...

class LabelGroupSubEntity:
    """.NET: Autodesk.Civil.DatabaseServices.LabelGroupSubEntity"""
    def __init__(self, *args) -> None: ...
    StyleId: ObjectId
    Visibility: bool
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    RotationType: LabelRotationType
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    Index: int
    Parent: LabelGroup
    def ClearAllTextComponentOverrides(self, ) -> None: ...
    def GetReferenceTextTarget(self, referenceTextComponentId: ObjectId) -> ObjectId: ...
    def GetTextComponentIds(self, ) -> ObjectIdCollection: ...
    def GetTextComponentJustificationOverride(self, labelStyleComponentId: ObjectId) -> TextJustificationType: ...
    def GetTextComponentOverride(self, labelStyleComponentId: ObjectId) -> str: ...
    def IsTextComponentOverriden(self, newVal: ObjectId) -> bool: ...
    def Reset(self, ) -> None: ...
    def ResetLocation(self, ) -> None: ...
    def ResetProperties(self, ) -> None: ...
    def SetReferenceTextTarget(self, referenceTextComponentId: ObjectId, referenceObjectId: ObjectId) -> None: ...
    def SetTextComponentJustificationOverride(self, labelStyleComponentId: ObjectId, textJustificationType: TextJustificationType) -> None: ...
    def SetTextComponentOverride(self, labelStyleComponentId: ObjectId, textOverride: str, textJustificationType: TextJustificationType) -> None: ...

class LabelSelectionProperties:
    """.NET: Autodesk.Civil.DatabaseServices.LabelSelectionProperties"""
    def __init__(self, *args) -> None: ...
    TagLabel: bool
    ClearMultiLabelText: bool
    ClearLabelText: bool
    EditLabelText: bool
    LeaderTail: bool
    Leader: bool
    ResetLabel: bool
    ToggleLabelPin: bool
    ReverseLabel: bool
    FlipLabel: bool
    def Dispose(self, ) -> None: ...
    @staticmethod
    def Instance(objIds: ObjectIdCollection) -> LabelSelectionProperties: ...

class LabelType:
    """.NET: Autodesk.Civil.DatabaseServices.LabelType"""
    def __init__(self, *args) -> None: ...
    ...

class LandDatabaseExtension:
    """.NET: Autodesk.Civil.DatabaseServices.LandDatabaseExtension"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetCivilAlignmentIds(database: Database) -> ObjectIdCollection: ...
    @staticmethod
    def GetCivilAlignmentTableIds(database: Database) -> ObjectIdCollection: ...
    @staticmethod
    def GetCivilBridgeIds(database: Database) -> ObjectIdCollection: ...
    @staticmethod
    def GetCivilCatchmentGroups(database: Database) -> CatchmentGroupCollection: ...
    @staticmethod
    def GetCivilLegendTableIds(database: Database) -> ObjectIdCollection: ...
    @staticmethod
    def GetCivilParcelSegmentTableIds(database: Database) -> ObjectIdCollection: ...
    @staticmethod
    def GetCivilParcelTableIds(database: Database) -> ObjectIdCollection: ...
    @staticmethod
    def GetCivilPointTableIds(database: Database) -> ObjectIdCollection: ...
    @staticmethod
    def GetCivilSiteIds(database: Database) -> ObjectIdCollection: ...
    @staticmethod
    def GetCivilSitelessAlignmentIds(database: Database) -> ObjectIdCollection: ...
    @staticmethod
    def GetCivilSitelessFeatureLineIds(database: Database) -> ObjectIdCollection: ...
    @staticmethod
    def GetCivilSurfaceIds(database: Database) -> ObjectIdCollection: ...
    @staticmethod
    def GetCivilViewFrameGroupIds(database: Database) -> ObjectIdCollection: ...

class LegendTable(Table):
    """.NET: Autodesk.Civil.DatabaseServices.LegendTable"""
    def __init__(self, *args) -> None: ...
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LinearTransitionDescription(TransitionDescriptionBase):
    """.NET: Autodesk.Civil.DatabaseServices.LinearTransitionDescription"""
    def __init__(self, *args) -> None: ...
    TaperInput: TaperInputType
    TaperRatio: float
    StartStation: float
    Length: float
    EndStation: float

class Link(CivilWrapper<AeccDbEntity>):
    """.NET: Autodesk.Civil.DatabaseServices.Link"""
    def __init__(self, *args) -> None: ...
    Points: PointCollection
    Index: int
    IsHidden: bool
    Codes: CodeCollection

class LinkCollection(CivilWrapper<AeccDbEntity>):
    """.NET: Autodesk.Civil.DatabaseServices.LinkCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: Link
    def Add(self, point1: IPoint, point2: IPoint, codes: list, displayMode: CorridorLinkDisplay) -> Link: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, link: Link) -> None: ...

class MassHaulLine(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.MassHaulLine"""
    def __init__(self, *args) -> None: ...
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class MassHaulView(Graph):
    """.NET: Autodesk.Civil.DatabaseServices.MassHaulView"""
    def __init__(self, *args) -> None: ...
    MassHaulLineId: ObjectId
    Location: Point3d
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class MatchLine(GeoEntity):
    """.NET: Autodesk.Civil.DatabaseServices.MatchLine"""
    def __init__(self, *args) -> None: ...
    Number: int
    Station: float
    AlignmentId: ObjectId
    IsRightLabelVisible: bool
    IsLeftLabelVisible: bool
    RightLabelStyleId: ObjectId
    LeftLabelStyleId: ObjectId
    RightLabelAnchorPosition: MatchLineLabelLocationType
    LeftLabelAnchorPosition: MatchLineLabelLocationType
    GroupId: ObjectId
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class MatchLineLabelGroup(AutoFeatureLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.MatchLineLabelGroup"""
    def __init__(self, *args) -> None: ...
    Side: EntitySideType
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(viewFrameGroupId: ObjectId, side: EntitySideType, labelStyleId: ObjectId, anchorPosition: MatchLineLabelLocationType) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(viewFrameGroupId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetLabelGroupIdBySide(viewFrameGroupId: ObjectId, side: EntitySideType) -> ObjectId: ...

class MaterialConditionType:
    """.NET: Autodesk.Civil.DatabaseServices.MaterialConditionType"""
    def __init__(self, *args) -> None: ...
    ...

class MaterialFactorType:
    """.NET: Autodesk.Civil.DatabaseServices.MaterialFactorType"""
    def __init__(self, *args) -> None: ...
    ...

class MaterialItemType:
    """.NET: Autodesk.Civil.DatabaseServices.MaterialItemType"""
    def __init__(self, *args) -> None: ...
    ...

class MaterialQuantityType:
    """.NET: Autodesk.Civil.DatabaseServices.MaterialQuantityType"""
    def __init__(self, *args) -> None: ...
    ...

class MaterialSection(Section):
    """.NET: Autodesk.Civil.DatabaseServices.MaterialSection"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    CorridorSurfaceId: ObjectId
    SourceName: str
    MaximumElevation: float
    MinmumElevation: float
    RightSwathWidth: float
    LeftSwathWidth: float
    RightOffset: float
    LeftOffset: float
    SourceType: SectionSourceType
    UpdateMode: SectionUpdateType
    Station: float
    SectionPoints: SectionPointCollection
    SourceId: ObjectId
    ParentId: ObjectId
    SampleLineId: ObjectId
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class MaterialSectionSource:
    """.NET: Autodesk.Civil.DatabaseServices.MaterialSectionSource"""
    def __init__(self, *args) -> None: ...
    IsSampled: bool
    UpdateMode: SectionUpdateType
    StyleId: ObjectId
    Material: QTOMaterial
    SourceType: SectionSourceType
    def GetMaterialSectionIds(self, ) -> ObjectIdCollection: ...

class MaterialSectionSourceCollection:
    """.NET: Autodesk.Civil.DatabaseServices.MaterialSectionSourceCollection"""
    def __init__(self, *args) -> None: ...
    Item: MaterialSectionSource
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class MaterialVolumeCalculationMethodType:
    """.NET: Autodesk.Civil.DatabaseServices.MaterialVolumeCalculationMethodType"""
    def __init__(self, *args) -> None: ...
    ...

class MultipleProfileViewsCreationOptions:
    """.NET: Autodesk.Civil.DatabaseServices.MultipleProfileViewsCreationOptions"""
    def __init__(self, *args) -> None: ...
    GapBetweenViewsInColumn: float
    GapBetweenViewsInRow: float
    StartCorner: ProfileViewStartCornerType
    MaxViewInRowOrColumn: int
    DrawOrder: ProfileViewPlotType
    LengthOfEachView: float

class Network(GeoEntity):
    """.NET: Autodesk.Civil.DatabaseServices.Network"""
    def __init__(self, *args) -> None: ...
    PartsListName: str
    PartsListId: ObjectId
    ReferenceAlignmentName: str
    ReferenceAlignmentId: ObjectId
    ReferenceSurfaceName: str
    ReferenceSurfaceId: ObjectId
    StructureNameTemplate: str
    StructureProfileLabelStyleName: str
    StructureProfileLabelStyleId: ObjectId
    StructurePlanLabelStyleName: str
    StructurePlanLabelStyleId: ObjectId
    PipeNameTemplate: str
    PipeProfileLabelStyleName: str
    PipeProfileLabelStyleId: ObjectId
    PipePlanLabelStyleName: str
    PipePlanLabelStyleId: ObjectId
    PipeNetworkSectionLayerId: ObjectId
    PipeNetworkSectionLayerName: str
    ModifiedPipeNetworkSectionLayerName: str
    StructureProfileLayerId: ObjectId
    StructureProfileLayerName: str
    ModifiedStructureProfileLayerName: str
    StructurePlanLayerId: ObjectId
    StructurePlanLayerName: str
    ModifiedStructurePlanLayerName: str
    PipeProfileLayerId: ObjectId
    PipeProfileLayerName: str
    ModifiedPipeProfileLayerName: str
    PipePlanLayerId: ObjectId
    PipePlanLayerName: str
    ModifiedPipePlanLayerName: str
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddCurvePipe(self, pipeFamilyId: ObjectId, pipeSizeId: ObjectId, curve: Curve3d, clockwise: bool, newPipeId: ObjectId, applyRules: bool) -> None: ...
    def AddLinePipe(self, pipeFamilyId: ObjectId, pipeSizeId: ObjectId, line: LineSegment3d, newPipeId: ObjectId, applyRules: bool) -> None: ...
    def AddStructure(self, structureFamilyId: ObjectId, structureSizeId: ObjectId, location: Point3d, rotation: float, newStructureId: ObjectId, applyRules: bool) -> None: ...
    def BreakPipe(self, pipeIdToBreak: ObjectId, breakPoint: Point3d, existingStructureId: ObjectId, newPipeId: ObjectId) -> None: ...
    @staticmethod
    def Create(document: CivilDocument, networkName: str) -> ObjectId: ...
    @staticmethod
    def FindShortestNetworkPath(startPartId: ObjectId, endPartId: ObjectId, minLength: float) -> ObjectIdCollection: ...
    def GetPipeIds(self, ) -> ObjectIdCollection: ...
    def GetSpanningPipePlanLabelIds(self, ) -> ObjectIdCollection: ...
    def GetSpanningPipeProfileLabelIds(self, ) -> ObjectIdCollection: ...
    def GetStructureIds(self, ) -> ObjectIdCollection: ...
    def MoveParts(self, partIds: ObjectIdCollection, dstNetworkId: ObjectId) -> None: ...

class NetworkCatalogDef:
    """.NET: Autodesk.Civil.DatabaseServices.NetworkCatalogDef"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def DeclareNewParameter(globalContext: str, displayContext: str, paramName: str, paramDesc: str, dataType: PartCatalogDataType, usage: PartParamUsageType, defaultUnits: str, singleton: bool, catManagedList: bool) -> None: ...
    @staticmethod
    def DeclarePartProperty(globalContext: str, domain: DomainType, partType: PartType) -> None: ...

class NetworkRule(DBObject):
    """.NET: Autodesk.Civil.DatabaseServices.NetworkRule"""
    def __init__(self, *args) -> None: ...
    ParamsDouble: ParamDoubleCollection
    ParamsLong: ParamLongCollection
    IsUsed: bool
    Description: str
    Name: str
    Document: object
    Application: object
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class NoteLabel(Label):
    """.NET: Autodesk.Civil.DatabaseServices.NoteLabel"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(location: Point3d, labelStyleId: ObjectId, markerStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelIds(database: Database) -> ObjectIdCollection: ...

class OffsetAlignmentInfo(CivilWrapper<AeccDbAlignment>):
    """.NET: Autodesk.Civil.DatabaseServices.OffsetAlignmentInfo"""
    def __init__(self, *args) -> None: ...
    Side: EntitySideType
    UpdateMode: AlignmentUpdateModeType
    NominalOffset: float
    LockToEndStation: bool
    LockToStartStation: bool
    LockMode: AlignmentLockModeType
    Transitions: AlignmentTransitionCollection
    Regions: AlignmentRegionCollection
    ParentAlignmentId: ObjectId
    def AddAutoWidenings(self, wideningCriteria: AutoWideningCriteriaInfo, curveGroups: list) -> None: ...
    def AddWidening(self, startStation: float, endStation: float, offsetDistance: float) -> None: ...

class OffsetAlignmentWideningCriteria:
    """.NET: Autodesk.Civil.DatabaseServices.OffsetAlignmentWideningCriteria"""
    def __init__(self, *args) -> None: ...
    WheelbaseLength: float
    RightLanesCount: int
    LeftLanesCount: int
    LaneWidth: float
    TangentPercentForTC: float
    SpiralPercentForSC: float
    AttainmentMethod: str
    TransitionLengthTableName: str
    MinimumRadiusTableName: str
    WideningSide: WideningSide
    WideningMethod: str

class OffsetAssembly:
    """.NET: Autodesk.Civil.DatabaseServices.OffsetAssembly"""
    def __init__(self, *args) -> None: ...
    AssemblyId: ObjectId
    Groups: AssemblyGroupCollection
    Offset: Vector2d
    Name: str
    def AddSubassembly(self, subassemblyId: ObjectId, pointHookTo: Point) -> None: ...
    def CopySubassembly(self, subassemblyIdFrom: ObjectId, pointHookTo: Point) -> ObjectId: ...
    def Dispose(self, ) -> None: ...
    def InsertSubassemblyAfter(self, subassemblyId: ObjectId, pointHookTo: Point) -> None: ...
    def InsertSubassemblyBefore(self, subassemblyId: ObjectId, targetSubassemblyId: ObjectId) -> None: ...
    def MirrorSubassembly(self, subassemblyIdFrom: ObjectId, pointHookTo: Point) -> ObjectId: ...
    def ReplaceSubassembly(self, subassemblyId: ObjectId, targetSubassemblyId: ObjectId) -> None: ...

class OffsetAssemblyCollection:
    """.NET: Autodesk.Civil.DatabaseServices.OffsetAssemblyCollection"""
    def __init__(self, *args) -> None: ...
    Item: OffsetAssembly
    Item: OffsetAssembly
    Count: int
    def Add(self, offsetAssemblyName: str, offset: Vector2d) -> OffsetAssembly: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, offsetAssembly: OffsetAssembly) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class OffsetBaseline(BaseBaseline):
    """.NET: Autodesk.Civil.DatabaseServices.OffsetBaseline"""
    def __init__(self, *args) -> None: ...
    FeatureLineIdVertical: ObjectId
    RelatedOffsetBaselineFeatureLines: BaselineFeatureLines
    EndStationOnMainBaseline: float
    StartStationOnMainBaseline: float
    OffsetGUID: Guid
    Name: str
    EndStation: float
    StartStation: float
    ProfileId: ObjectId
    AlignmentId: ObjectId
    BaselineType: CorridorBaselineType
    DirectionAtStation: Vector3d
    baselineGUID: Guid
    BaselineGuid: Guid
    FeatureLineId: ObjectId
    CorridorId: ObjectId
    def GetOffsetElevationFromMainBaselineStation(self, mainBaselineStation: float) -> Point2d: ...
    def IsFeatureLineBased(self, ) -> bool: ...
    def MainBaselineStationToOffsetBaselineStation(self, mainBaselineStation: float) -> float: ...
    def OffsetBaselineStationToMainBaselineStation(self, offsetBaselineStation: float) -> float: ...
    def SetFeatureLine(self, horizontalFeatureLineId: ObjectId, verticalFeatureLineId: ObjectId) -> None: ...
    def SortedStations(self, ) -> list: ...

class OffsetBaselineCollection(CivilWrapper<AeccDbCorridor>):
    """.NET: Autodesk.Civil.DatabaseServices.OffsetBaselineCollection"""
    def __init__(self, *args) -> None: ...
    Item: OffsetBaseline
    Item: OffsetBaseline
    Item: OffsetBaseline
    Count: int
    CorridorId: ObjectId
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def OffsetBaselineNames(self, ) -> list: ...

class OffsetLengthOption:
    """.NET: Autodesk.Civil.DatabaseServices.OffsetLengthOption"""
    def __init__(self, *args) -> None: ...
    ...

class OverhangCorrectionType:
    """.NET: Autodesk.Civil.DatabaseServices.OverhangCorrectionType"""
    def __init__(self, *args) -> None: ...
    ...

class OverriddenStationInfo:
    """.NET: Autodesk.Civil.DatabaseServices.OverriddenStationInfo"""
    def __init__(self, *args) -> None: ...
    ...

class Parcel(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.Parcel"""
    def __init__(self, *args) -> None: ...
    StyleId: ObjectId
    Address: str
    TaxId: int
    IsAreaSelectionLabelPinned: bool
    Centroid: Point3d
    AreaLocation: Point3d
    AreaSelectionLabelLocation: Point3d
    AreaSelectionLabelStyleId: ObjectId
    Number: int
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetAvailableParcelAreaLabelIds(self, ) -> ObjectIdCollection: ...
    def GetUDPValue(self, udp: UDPEnumeration) -> str: ...
    def ResetAreaSelectionLabel(self, ) -> None: ...
    def SetUDPValue(self, udp: UDPEnumeration, value: str) -> None: ...

class ParcelAreaLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.ParcelAreaLabel"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(parcelId: ObjectId, labelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelIds(parcelId: ObjectId) -> ObjectIdCollection: ...

class ParcelSegment(Feature):
    """.NET: Autodesk.Civil.DatabaseServices.ParcelSegment"""
    def __init__(self, *args) -> None: ...
    IsEditable: bool
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetAvailableParcelSegmentLabelIds(self, ) -> ObjectIdCollection: ...

class ParcelSegmentLabel(GeneralSegmentLabel):
    """.NET: Autodesk.Civil.DatabaseServices.ParcelSegmentLabel"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    CurveLabelStyleId: ObjectId
    LineLabelStyleId: ObjectId
    Ratio: float
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(featureId: ObjectId, ratio: float, lineLabelStyleId: ObjectId, curveLabelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelIds(featureId: ObjectId) -> ObjectIdCollection: ...

class ParcelSegmentTable(Table):
    """.NET: Autodesk.Civil.DatabaseServices.ParcelSegmentTable"""
    def __init__(self, *args) -> None: ...
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ParcelTable(Table):
    """.NET: Autodesk.Civil.DatabaseServices.ParcelTable"""
    def __init__(self, *args) -> None: ...
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Part(GeoEntity):
    """.NET: Autodesk.Civil.DatabaseServices.Part"""
    def __init__(self, *args) -> None: ...
    PartFamilyName: str
    PartFamilyId: ObjectId
    Solid3dBody: Solid3d
    OverrideRuleSet: bool
    RuleSetStyleName: str
    RuleSetStyleId: ObjectId
    PartData: PartDataRecord
    PartDefId: ObjectId
    SectionViewPartId: ObjectId
    ProfileViewPartId: ObjectId
    KnownFlow: float
    ConnectedPartCount: int
    RefSurfaceName: str
    RefSurfaceId: ObjectId
    SurfaceId: ObjectId
    RefAlignmentName: str
    RefAlignmentId: ObjectId
    NetworkName: str
    NetworkId: ObjectId
    WallThickness: float
    Material: str
    PartDescription: str
    PartSizeName: str
    Name: str
    Domain: DomainType
    PartSubType: str
    ParamsString: ParamStringCollection
    ParamsLong: ParamLongCollection
    ParamsDouble: ParamDoubleCollection
    ParamsBool: ParamBoolCollection
    PartType: PartType
    Position: Point3d
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddToProfileView(self, profileViewId: ObjectId) -> None: ...
    def AddToSectionView(self, sectionViewId: ObjectId) -> None: ...
    def ApplyRules(self, ) -> bool: ...
    def GetOverriddenRuleIds(self, ) -> ObjectIdCollection: ...
    def GetPartSizeId(self, ) -> ObjectId: ...
    def GetProfileViewsDisplayingMe(self, ) -> ObjectIdCollection: ...
    def GetSectionViewsDisplayingMe(self, ) -> ObjectIdCollection: ...
    def RemoveFromAllProfileViews(self, ) -> None: ...
    def RemoveFromAllSectionViews(self, ) -> None: ...
    def RemoveFromProfileView(self, profileViewId: ObjectId) -> None: ...
    def RemoveFromSectionView(self, sectionViewId: ObjectId) -> None: ...
    def SwapPartFamilyAndSize(self, partFamilyId: ObjectId, partSizeId: ObjectId) -> None: ...

class PartCatalogDataType:
    """.NET: Autodesk.Civil.DatabaseServices.PartCatalogDataType"""
    def __init__(self, *args) -> None: ...
    ...

class PartContextType:
    """.NET: Autodesk.Civil.DatabaseServices.PartContextType"""
    def __init__(self, *args) -> None: ...
    ...

class PartDataField:
    """.NET: Autodesk.Civil.DatabaseServices.PartDataField"""
    def __init__(self, *args) -> None: ...
    Units: str
    Index: int
    Context: PartContextType
    ContextString: str
    Description: str
    Name: str
    Value: object
    IsReadOnly: bool
    ValueRange: PartDataRange
    ValueList: PartDataList
    IsFromRange: bool
    IsFromList: bool
    DataType: PartCatalogDataType

class PartDataList:
    """.NET: Autodesk.Civil.DatabaseServices.PartDataList"""
    def __init__(self, *args) -> None: ...
    Index: int
    Context: PartContextType
    DataType: PartCatalogDataType
    Item: object
    Count: int
    def Dispose(self, ) -> None: ...
    def IsValidValue(self, value: object) -> bool: ...

class PartDataRange:
    """.NET: Autodesk.Civil.DatabaseServices.PartDataRange"""
    def __init__(self, *args) -> None: ...
    Index: int
    Context: PartContextType
    DataType: PartCatalogDataType
    RangeDefault: object
    RangeMin: object
    RangeMax: object
    def Dispose(self, ) -> None: ...
    def IsValidValue(self, value: object) -> bool: ...

class PartDataRecord:
    """.NET: Autodesk.Civil.DatabaseServices.PartDataRecord"""
    def __init__(self, *args) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetAllDataFields(self, ) -> list: ...
    def GetDataFieldBy(self, context: PartContextType, index: int) -> PartDataField: ...
    def GetMaxIndex(self, context: PartContextType) -> int: ...
    def GetSupportedContexts(self, ) -> list: ...

class PartDef(DBObject):
    """.NET: Autodesk.Civil.DatabaseServices.PartDef"""
    def __init__(self, *args) -> None: ...
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Get3dBody(self, ) -> Solid3d: ...
    def GetBoundingShapeBody(self, ) -> Solid3d: ...
    def GetNetworkPartViewDef(self, ) -> PartViewDef: ...
    def GetProfileInFrontView(self, ) -> Profile: ...

class PartParamUsageType:
    """.NET: Autodesk.Civil.DatabaseServices.PartParamUsageType"""
    def __init__(self, *args) -> None: ...
    ...

class PartProfileLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.PartProfileLabel"""
    def __init__(self, *args) -> None: ...
    ReferenceAlignmentId: ObjectId
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PartSectionLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.PartSectionLabel"""
    def __init__(self, *args) -> None: ...
    ReferenceAlignmentId: ObjectId
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PartType:
    """.NET: Autodesk.Civil.DatabaseServices.PartType"""
    def __init__(self, *args) -> None: ...
    ...

class PartViewDef(ImpObject):
    """.NET: Autodesk.Civil.DatabaseServices.PartViewDef"""
    def __init__(self, *args) -> None: ...
    BoundingBodyBlockName: str
    BoundingBodyBlockId: ObjectId
    PartBodyGraphicsBlockName: str
    PartBodyGraphicsBlockId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PayItemFileFormat:
    """.NET: Autodesk.Civil.DatabaseServices.PayItemFileFormat"""
    def __init__(self, *args) -> None: ...
    ...

class Pipe(Part):
    """.NET: Autodesk.Civil.DatabaseServices.Pipe"""
    def __init__(self, *args) -> None: ...
    ManningCoefficient: float
    HasManningCoefficient: bool
    AverageLoss: float
    ExitLoss: float
    EntryLoss: float
    ReturnPeriod: int
    JunctionLoss: float
    FlowRate: float
    CurveGeometry: PipeCurveGeometry
    Curve2d: CircularArc2d
    EnergyGradeLineDown: float
    EnergyGradeLineUp: float
    HydraulicGradeLineDown: float
    HydraulicGradeLineUp: float
    CoverOfEndpoint: float
    CoverOfStartPoint: float
    CrossSectionalShape: SweptShapeType
    EndOffset: float
    StartOffset: float
    EndStation: float
    StartStation: float
    Bearing: float
    SubEntityType: PipeSubEntityType
    StyleId: ObjectId
    Radius: float
    OuterHeight: float
    InnerHeight: float
    HoldOnResizeType: HoldOnResizeType
    EndObjectId: ObjectId
    StartObjectId: ObjectId
    EndStructureId: ObjectId
    StartStructureId: ObjectId
    Slope: float
    MinimumCover: float
    MaximumCover: float
    OuterDiameterOrWidth: float
    InnerDiameterOrWidth: float
    Length3DToInsideEdge: float
    Length2DToInsideEdge: float
    Length3DCenterToCenter: float
    Length3D: float
    Length2DCenterToCenter: float
    Length2D: float
    FlowDirectionMethod: FlowDirectionMethodType
    FlowDirection: FlowDirectionType
    StartPoint: Point3d
    EndPoint: Point3d
    PartFamilyName: str
    PartFamilyId: ObjectId
    Solid3dBody: Solid3d
    OverrideRuleSet: bool
    RuleSetStyleName: str
    RuleSetStyleId: ObjectId
    PartData: PartDataRecord
    PartDefId: ObjectId
    SectionViewPartId: ObjectId
    ProfileViewPartId: ObjectId
    KnownFlow: float
    ConnectedPartCount: int
    RefSurfaceName: str
    RefSurfaceId: ObjectId
    SurfaceId: ObjectId
    RefAlignmentName: str
    RefAlignmentId: ObjectId
    NetworkName: str
    NetworkId: ObjectId
    WallThickness: float
    Material: str
    PartDescription: str
    PartSizeName: str
    Name: str
    Domain: DomainType
    PartSubType: str
    ParamsString: ParamStringCollection
    ParamsLong: ParamLongCollection
    ParamsDouble: ParamDoubleCollection
    ParamsBool: ParamBoolCollection
    PartType: PartType
    Position: Point3d
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AdjustEndpoint(self, endpointToAdjust: ConnectorPositionType, targetLocation: PipeEndLocation, dOffset: float) -> bool: ...
    def ConnectToPipe(self, sourceType: ConnectorPositionType, destinationPipeId: ObjectId, destinationType: ConnectorPositionType, structureFamilyId: ObjectId, structureSizeId: ObjectId, newStructureId: ObjectId, applyRules: bool, force: bool) -> None: ...
    def ConnectToStructure(self, sourcePosition: ConnectorPositionType, destinationStructureId: ObjectId, force: bool) -> None: ...
    def Disconnect(self, pos: ConnectorPositionType) -> None: ...
    def GetAvailablePipeLabelIds(self, ) -> ObjectIdCollection: ...
    def GetAvailableSpanningPipeLabelIds(self, ) -> ObjectIdCollection: ...
    def GetClosestPointTo(self, sourcePoint: Point3d) -> Point3d: ...
    def GetLabelIds(self, ) -> ObjectIdCollection: ...
    def GetParamAtPoint(self, point: Point3d) -> float: ...
    def GetPipeLabelIds(self, ) -> ObjectIdCollection: ...
    def GetPointAtParam(self, paramInterval: float) -> Point3d: ...
    def GetProject2dPointVertically(self, sourcePoint: Point2d, projectPoint: Point3d) -> bool: ...
    def IsMaxCoverViolated(self, maxCover: float, pointsViolated: list, differences: list, params: list) -> bool: ...
    def IsMinCoverViolated(self, minCover: float, pointsViolated: list, differences: list, params: list) -> bool: ...
    def ResizeByInnerDiameterOrWidth(self, innerDiameterOrWidth: float, useClosestSize: bool) -> None: ...
    def SetSlopeHoldEnd(self, endValue: float) -> None: ...
    def SetSlopeHoldStart(self, startValue: float) -> None: ...

class PipeCurveGeometry(DisposableWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.PipeCurveGeometry"""
    def __init__(self, *args) -> None: ...
    Bulge: float
    EndPoint: Point3d
    StartPoint: Point3d
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetArc2d(self, ) -> CircularArc2d: ...

class PipeEndLocation:
    """.NET: Autodesk.Civil.DatabaseServices.PipeEndLocation"""
    def __init__(self, *args) -> None: ...
    ...

class PipeLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.PipeLabel"""
    def __init__(self, *args) -> None: ...
    Ratio: float
    ReferenceAlignmentId: ObjectId
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(pipeId: ObjectId, ratio: float, labelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelIds(pipeId: ObjectId) -> ObjectIdCollection: ...

class PipeNetworkBandLabelGroup(ProfileBandLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.PipeNetworkBandLabelGroup"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(profileViewId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class PipeNetworkDatabaseExtension:
    """.NET: Autodesk.Civil.DatabaseServices.PipeNetworkDatabaseExtension"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetCivilPipeNetworkIds(database: Database) -> ObjectIdCollection: ...

class PipeNetworkStructureType:
    """.NET: Autodesk.Civil.DatabaseServices.PipeNetworkStructureType"""
    def __init__(self, *args) -> None: ...
    ...

class PipeOverride(GraphOverride):
    """.NET: Autodesk.Civil.DatabaseServices.PipeOverride"""
    def __init__(self, *args) -> None: ...
    OverrideStyleId: ObjectId
    OverrideStyleName: str
    PipeName: str
    PipeId: ObjectId
    Draw: bool
    UseOverrideStyle: bool

class PipeOverrideCollection(GraphOverrideCollection):
    """.NET: Autodesk.Civil.DatabaseServices.PipeOverrideCollection"""
    def __init__(self, *args) -> None: ...
    SplitAt: str
    ClipGridAt: str
    Count: int
    Item: PipeOverride
    def GetEnumerator(self, ) -> IEnumerator: ...

class PipeProfileLabel(PartProfileLabel):
    """.NET: Autodesk.Civil.DatabaseServices.PipeProfileLabel"""
    def __init__(self, *args) -> None: ...
    Ratio: float
    ReferenceAlignmentId: ObjectId
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(profileViewPartId: ObjectId, profileViewId: ObjectId, ratio: float, labelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelIds(profileViewId: ObjectId) -> ObjectIdCollection: ...

class PipeSectionLabel(PartSectionLabel):
    """.NET: Autodesk.Civil.DatabaseServices.PipeSectionLabel"""
    def __init__(self, *args) -> None: ...
    ReferenceAlignmentId: ObjectId
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(sectionViewId: ObjectId, pipeId: ObjectId, sectionPipeNetworkId: ObjectId, partIndex: int, labelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelIds(sectionViewId: ObjectId) -> ObjectIdCollection: ...

class PipeSubEntityType:
    """.NET: Autodesk.Civil.DatabaseServices.PipeSubEntityType"""
    def __init__(self, *args) -> None: ...
    ...

class Point(CivilWrapper<AeccDbEntity>):
    """.NET: Autodesk.Civil.DatabaseServices.Point"""
    def __init__(self, *args) -> None: ...
    IsLoopPoint: bool
    Index: int
    Elevation: float
    Offset: float
    Station: float
    IsHidden: bool
    Codes: CodeCollection
    def GetXYZ(self, x: float, y: float, z: float) -> None: ...

class PointCloud(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.PointCloud"""
    def __init__(self, *args) -> None: ...
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PointCloudUtility:
    """.NET: Autodesk.Civil.DatabaseServices.PointCloudUtility"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetCivilPointCloudName(A_0: ObjectId) -> str: ...
    @staticmethod
    def IsCivilPointCloud(A_0: ObjectId) -> bool: ...

class PointCollection(CivilWrapper<AeccDbEntity>):
    """.NET: Autodesk.Civil.DatabaseServices.PointCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: Point
    def Add(self, offset: float, elevation: float, codes: list) -> Point: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, point: Point) -> None: ...

class PointDescriptionKey(DBObject):
    """.NET: Autodesk.Civil.DatabaseServices.PointDescriptionKey"""
    def __init__(self, *args) -> None: ...
    RotationDirection: RotationDirType
    FixedLabelRotation: float
    ApplyFixedLabelRotation: bool
    LabelRotationParameter: int
    ApplyLabelRotationParameter: bool
    FixedMarkerRotation: float
    ApplyFixedMarkerRotation: bool
    MarkerRotationParameter: int
    ApplyMarkerRotationParameter: bool
    ApplyScaleZ: bool
    ApplyScaleXY: bool
    ApplyDrawingScale: bool
    FixedScaleFactor: float
    ApplyFixedScaleFactor: bool
    ScaleParameter: int
    ApplyScaleParameter: bool
    LayerId: ObjectId
    ApplyLayerId: bool
    Format: str
    LabelStyleId: ObjectId
    ApplyLabelStyleId: bool
    StyleId: ObjectId
    ApplyStyleId: bool
    Code: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PointDescriptionKeySet(DBObject):
    """.NET: Autodesk.Civil.DatabaseServices.PointDescriptionKeySet"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ObjectId
    IsUsed: bool
    Description: str
    Name: str
    Document: object
    Application: object
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, codeName: str) -> ObjectId: ...
    def Clear(self, ) -> None: ...
    def Contains(self, name: str) -> bool: ...
    def GetPointDescriptionKeyIds(self, ) -> ObjectIdCollection: ...
    def Remove(self, keyId: ObjectId) -> bool: ...

class PointDescriptionKeySetCollection:
    """.NET: Autodesk.Civil.DatabaseServices.PointDescriptionKeySetCollection"""
    def __init__(self, *args) -> None: ...
    SearchOrder: ObjectIdCollection
    Count: int
    Item: ObjectId
    Item: ObjectId
    def Add(self, name: str) -> ObjectId: ...
    def Clear(self, ) -> None: ...
    def Contains(self, name: str) -> bool: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    @staticmethod
    def GetPointDescriptionKeySets(database: Database) -> PointDescriptionKeySetCollection: ...
    def Remove(self, objectId: ObjectId) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class PointFileFormat(DisposableWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.PointFileFormat"""
    def __init__(self, *args) -> None: ...
    FileFormatType: PointFileFormatType
    CommentTag: str
    FileExtension: str
    Delimiter: str
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Equals(self, obj: object) -> bool: ...

class PointFileFormatCollection:
    """.NET: Autodesk.Civil.DatabaseServices.PointFileFormatCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: PointFileFormat
    Item: PointFileFormat
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    @staticmethod
    def GetPointFileFormats(pDatabase: Database) -> PointFileFormatCollection: ...

class PointGroup(DBObject):
    """.NET: Autodesk.Civil.DatabaseServices.PointGroup"""
    def __init__(self, *args) -> None: ...
    UDPClassificationApplyType: UDPClassificationApplyType
    UDPClassificationName: str
    AllPointsGroupName: str
    PointLabelStyleId: ObjectId
    IsPointLabelStyleOverridden: bool
    PointStyleId: ObjectId
    IsPointStyleOverridden: bool
    ElevationOverride: PointGroupElevationOverrideInfo
    IsElevationOverridden: bool
    RawDescriptionOverride: PointGroupRawDescriptionOverrideInfo
    IsRawDescriptionOverridden: bool
    IsLocked: bool
    IsOutOfDate: bool
    RawDescription: str
    PointsCount: int
    IsAllPointsGroup: bool
    Description: str
    Name: str
    IsUsed: bool
    Document: object
    Application: object
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ApplyDescriptionKeys(self, ) -> None: ...
    def ContainsPoint(self, pointNumber: int) -> bool: ...
    def DeletePoints(self, ) -> None: ...
    def GetPendingChanges(self, ) -> PointGroupChangeInfo: ...
    def GetPointNumbers(self, ) -> list: ...
    def GetQuery(self, ) -> PointGroupQuery: ...
    def LockPoints(self, ) -> None: ...
    def SetQuery(self, query: PointGroupQuery) -> None: ...
    def UnlockPoints(self, ) -> None: ...
    def Update(self, ) -> None: ...
    def UseAllClassifications(self, ) -> None: ...
    def UseCustomClassification(self, udpClassification: UDPClassification) -> None: ...
    def UseNoneClassification(self, ) -> None: ...

class PointGroupChangeInfo:
    """.NET: Autodesk.Civil.DatabaseServices.PointGroupChangeInfo"""
    def __init__(self, *args) -> None: ...
    PointsToRemove: list
    PointsToAdd: list

class PointGroupCollection:
    """.NET: Autodesk.Civil.DatabaseServices.PointGroupCollection"""
    def __init__(self, *args) -> None: ...
    DrawOrder: ObjectIdCollection
    AllPointsPointGroupId: ObjectId
    Count: int
    Item: ObjectId
    Item: ObjectId
    def Add(self, name: str) -> ObjectId: ...
    def Contains(self, name: str) -> bool: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def GetOutOfDatePointGroupIds(self, ) -> ObjectIdCollection: ...
    @staticmethod
    def GetPointGroups(pDatabase: Database) -> PointGroupCollection: ...
    def Remove(self, pointGroupId: ObjectId) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    def UpdateAllPointGroups(self, ) -> None: ...

class PointGroupElevationOverrideInfo(PointGroupOverrideInfo):
    """.NET: Autodesk.Civil.DatabaseServices.PointGroupElevationOverrideInfo"""
    def __init__(self, *args) -> None: ...
    UDP: UDPDouble
    FixedElevation: float
    XDRefId: ObjectId
    ActiveOverrideType: PointGroupOverrideType

class PointGroupOverrideInfo:
    """.NET: Autodesk.Civil.DatabaseServices.PointGroupOverrideInfo"""
    def __init__(self, *args) -> None: ...
    XDRefId: ObjectId
    ActiveOverrideType: PointGroupOverrideType

class PointGroupOverrideType:
    """.NET: Autodesk.Civil.DatabaseServices.PointGroupOverrideType"""
    def __init__(self, *args) -> None: ...
    ...

class PointGroupQuery:
    """.NET: Autodesk.Civil.DatabaseServices.PointGroupQuery"""
    def __init__(self, *args) -> None: ...
    QueryString: str
    UseCaseSensitiveMatch: bool

class PointGroupQueryInvalidPointGroupValueException(ArgumentException):
    """.NET: Autodesk.Civil.DatabaseServices.PointGroupQueryInvalidPointGroupValueException"""
    def __init__(self, *args) -> None: ...
    InvalidPointGroup: str
    Message: str
    ParamName: str
    TargetSite: MethodBase
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class PointGroupQueryOperationFailedException(ArgumentException):
    """.NET: Autodesk.Civil.DatabaseServices.PointGroupQueryOperationFailedException"""
    def __init__(self, *args) -> None: ...
    Message: str
    ParamName: str
    TargetSite: MethodBase
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class PointGroupQueryParserException(ArgumentException):
    """.NET: Autodesk.Civil.DatabaseServices.PointGroupQueryParserException"""
    def __init__(self, *args) -> None: ...
    Position: int
    Query: str
    Message: str
    ParamName: str
    TargetSite: MethodBase
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class PointGroupQueryToken:
    """.NET: Autodesk.Civil.DatabaseServices.PointGroupQueryToken"""
    def __init__(self, *args) -> None: ...
    SingleQuoteCode: str
    ValueDelimiter: str
    ClosingParenthesis: str
    OpeningParenthesis: str
    GreaterThanOrEqual: str
    LessThanOrEqual: str
    GreaterThan: str
    LessThan: str
    NotEqual: str
    Equal: str
    NOT: str
    OR: str
    AND: str
    PointGroupField: str
    PointElevationField: str
    PointNumberField: str
    FullDescriptionField: str
    RawDescriptionField: str
    NameField: str

class PointGroupRawDescriptionOverrideInfo(PointGroupOverrideInfo):
    """.NET: Autodesk.Civil.DatabaseServices.PointGroupRawDescriptionOverrideInfo"""
    def __init__(self, *args) -> None: ...
    UDP: UDP
    FixedRawDescription: str
    XDRefId: ObjectId
    ActiveOverrideType: PointGroupOverrideType

class PointInMem:
    """.NET: Autodesk.Civil.DatabaseServices.PointInMem"""
    def __init__(self, *args) -> None: ...
    Index: int
    Elevation: float
    Offset: float
    Station: float
    Codes: CodeCollection

class PointNumberResolveType:
    """.NET: Autodesk.Civil.DatabaseServices.PointNumberResolveType"""
    def __init__(self, *args) -> None: ...
    ...

class PointTable(Table):
    """.NET: Autodesk.Civil.DatabaseServices.PointTable"""
    def __init__(self, *args) -> None: ...
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PolylineOptions:
    """.NET: Autodesk.Civil.DatabaseServices.PolylineOptions"""
    def __init__(self, *args) -> None: ...
    EraseExistingEntities: bool
    AddCurvesBetweenTangents: bool
    PlineId: ObjectId
    def Equals(self, other: PolylineOptions) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class Profile(Feature):
    """.NET: Autodesk.Civil.DatabaseServices.Profile"""
    def __init__(self, *args) -> None: ...
    DesignCheckSetName: str
    DesignCheckSetId: ObjectId
    UseDesignCheckSet: bool
    UseDesignCriteriaFile: bool
    DesignSpeedBased: bool
    Entities: ProfileEntityCollection
    Plinegen: bool
    ElevationMax: float
    ElevationMin: float
    DataSourceName: str
    DataSourceId: ObjectId
    PVIs: ProfilePVICollection
    UpdateMode: ProfileUpdateType
    Length: float
    Offset: float
    EndingStation: float
    StartingStation: float
    ProfileType: ProfileType
    StyleId: ObjectId
    StyleName: str
    OffsetParameters: OffsetProfileParameters
    AlignmentId: ObjectId
    IsEditable: bool
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateByLayout(profileName: str, document: CivilDocument, alignmentName: str, layerName: str, styleName: str, labelSetName: str) -> ObjectId: ...
    @staticmethod
    def CreateFromFeatureLine(profileName: str, corridorFeatureLine: CorridorFeatureLine, alignmentId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId) -> ObjectId: ...
    @staticmethod
    def CreateFromSurface(profileName: str, document: CivilDocument, alignmentName: str, surfaceName: str, layerName: str, styleName: str, labelSetName: str, offset: float, sampleStart: float, sampleEnd: float) -> ObjectId: ...
    def CreateOffsetProfileBySlope(self, profileName: str, offsetAlignmentName: str, styleName: str, slope: float) -> ObjectId: ...
    @staticmethod
    def CreateStaticFGFromProfile(profileName: str, document: CivilDocument, srcProfileName: str, layerName: str, styleName: str, labelSetName: str) -> ObjectId: ...
    def ElevationAt(self, station: float) -> float: ...
    def GradeAt(self, station: float) -> float: ...

class ProfileBandLabelGroup(AutoFeatureLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileBandLabelGroup"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetAvailableLabelGroupIds(runtimeClass: RXClass, profileViewId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(runtimeClass: RXClass, profileViewId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class ProfileCircular(ProfileEntity):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileCircular"""
    def __init__(self, *args) -> None: ...
    M: float
    TangentOffsetAtPVI: float
    HighLowPointElevation: float
    HighLowPointStation: float
    Radius: float
    K: float
    GradeChange: float
    GradeOut: float
    GradeIn: float
    PVIElevation: float
    PVIStation: float
    CurveType: VerticalCurveType
    EntityType: ProfileEntityType
    Constraint2: EntityVerticalConstraintType
    MinimumKValueHSD: float
    MinimumKValuePSD: float
    MinimumKValueSSD: float
    HighestDesignSpeed: float
    EndElevation: float
    EndStation: float
    StartElevation: float
    StartStation: float
    Length: float
    EntityAfter: int
    EntityBefore: int
    Constraint1: ProfileEntityConstraintType
    EntityId: int

class ProfileCrestCurveLabelGroup(ProfileLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileCrestCurveLabelGroup"""
    def __init__(self, *args) -> None: ...
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class ProfileCriteria(CivilWrapper<AeccDbGraphProfile>):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileCriteria"""
    def __init__(self, *args) -> None: ...
    BoundaryType: HatchCriteriaBoundaryType
    ProfileName: str
    ProfileId: ObjectId

class ProfileCriteriaCollection(CivilWrapper<AeccDbGraphProfile>):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileCriteriaCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ProfileCriteria
    def Add(self, profileId: ObjectId, type: HatchCriteriaBoundaryType) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def RemoveAt(self, index: int) -> None: ...

class ProfileCrossing(ProfileProjection):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileCrossing"""
    def __init__(self, *args) -> None: ...
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ProfileDataBandLabelGroup(ProfileBandLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileDataBandLabelGroup"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(profileViewId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class ProfileEntity(CivilWrapper<AeccDbVAlignment>):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileEntity"""
    def __init__(self, *args) -> None: ...
    Constraint2: EntityVerticalConstraintType
    MinimumKValueHSD: float
    MinimumKValuePSD: float
    MinimumKValueSSD: float
    HighestDesignSpeed: float
    EndElevation: float
    EndStation: float
    StartElevation: float
    StartStation: float
    Length: float
    EntityAfter: int
    EntityBefore: int
    Constraint1: ProfileEntityConstraintType
    EntityId: int
    EntityType: ProfileEntityType
    def DesignChecks(self, ) -> list: ...
    def ValidateDesignCheck(self, designCheck: ProfileDesignCheck, curveType: ProfileApplyCurveType) -> bool: ...

class ProfileEntityCollection(CivilWrapper<AeccDbVAlignment>):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileEntityCollection"""
    def __init__(self, *args) -> None: ...
    LastEntity: int
    FirstEntity: int
    Count: int
    Item: ProfileEntity
    def AddFixedSymmetricParabolaByEntityEndAndThroughPoint(self, attachEntityId: int, passPoint: Point3d) -> ProfileParabolaSymmetric: ...
    def AddFixedSymmetricParabolaByThreePoints(self, point: Point3d, point2: Point3d, point3: Point3d) -> ProfileParabolaSymmetric: ...
    def AddFixedSymmetricParabolaByTwoPointsAndEndGrade(self, point1: Point3d, point2: Point3d, endGrade: float) -> ProfileParabolaSymmetric: ...
    def AddFixedSymmetricParabolaByTwoPointsAndK(self, point1: Point3d, point2: Point3d, curveType: VerticalCurveType, k: float) -> ProfileParabolaSymmetric: ...
    def AddFixedSymmetricParabolaByTwoPointsAndRadius(self, point1: Point3d, point2: Point3d, curType: VerticalCurveType, radius: float) -> ProfileParabolaSymmetric: ...
    def AddFixedSymmetricParabolaByTwoPointsAndStartGrade(self, point1: Point3d, point2: Point3d, startGrade: float) -> ProfileParabolaSymmetric: ...
    def AddFixedTangent(self, startPoint: Point3d, endPoint: Point3d) -> ProfileTangent: ...
    def AddFixedTangentWithPreviousEntity(self, previousEntityId: int, startPoint: Point3d, endPoint: Point3d) -> ProfileTangent: ...
    def AddFloatingSymmetricParabolaByThroughPointAndGrade(self, attachEntityId: int, passPoint: Point3d, grade: float, attachType: EntityAttachType) -> ProfileParabolaSymmetric: ...
    def AddFloatingSymmetricParabolaByThroughPointAndK(self, attachEntityId: int, passPoint: Point3d, k: float, attachType: EntityAttachType) -> ProfileParabolaSymmetric: ...
    def AddFloatingSymmetricParabolaByThroughPointAndRadius(self, attachEntityId: int, passPoint: Point3d, radius: float, attachType: EntityAttachType) -> ProfileParabolaSymmetric: ...
    def AddFloatingTangent(self, entityId: int, passPoint: Point3d, attachType: EntityAttachType) -> ProfileTangent: ...
    def AddFreeAsymmetricParabolaByPVIAndLengths(self, attachProfilePVI: ProfilePVI, length1: float, length2: float) -> ProfileParabolaAsymmetric: ...
    def AddFreeCircularCurveByPVIAndLength(self, attachProfilePVI: ProfilePVI, length: float) -> ProfileCircular: ...
    def AddFreeCircularCurveByPVIAndRadius(self, attachProfilePVI: ProfilePVI, radius: float) -> ProfileCircular: ...
    def AddFreeCircularCurveByPVIAndThroughPoint(self, attachProfilePVI: ProfilePVI, passPoint: Point3d) -> ProfileCircular: ...
    def AddFreeSymmetricParabolaByK(self, previousEntityId: int, nextEntityId: int, curveType: VerticalCurveType, k: float) -> ProfileParabolaSymmetric: ...
    def AddFreeSymmetricParabolaByLength(self, previousEntityId: int, nextEntityId: int, curveType: VerticalCurveType, length: float, preferFlat: bool) -> ProfileParabolaSymmetric: ...
    def AddFreeSymmetricParabolaByPVIAndCurveLength(self, attachProfilePVI: ProfilePVI, curveLength: float) -> ProfileParabolaSymmetric: ...
    def AddFreeSymmetricParabolaByPVIAndK(self, attachProfilePVI: ProfilePVI, k: float) -> ProfileParabolaSymmetric: ...
    def AddFreeSymmetricParabolaByPVIAndThroughPoint(self, attachProfilePVI: ProfilePVI, passPoint: Point3d) -> ProfileParabolaSymmetric: ...
    def AddFreeSymmetricParabolaByRadius(self, previousEntityId: int, nextEntityId: int, curveType: VerticalCurveType, radius: float) -> ProfileParabolaSymmetric: ...
    def AddFreeTangent(self, previousEntityId: int, nextEntityId: int) -> ProfileTangent: ...
    def Clear(self, ) -> None: ...
    def EntityAtId(self, id: int) -> ProfileEntity: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, entity: ProfileEntity) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class ProfileEntityConstraintType:
    """.NET: Autodesk.Civil.DatabaseServices.ProfileEntityConstraintType"""
    def __init__(self, *args) -> None: ...
    ...

class ProfileEntityType:
    """.NET: Autodesk.Civil.DatabaseServices.ProfileEntityType"""
    def __init__(self, *args) -> None: ...
    ...

class ProfileHatchArea(CivilWrapper<AeccDbGraphProfile>):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileHatchArea"""
    def __init__(self, *args) -> None: ...
    Criteria: ProfileCriteriaCollection
    ShapeStyleId: ObjectId
    ShapeStyleName: str
    Name: str

class ProfileHatchAreaCollection(CivilWrapper<AeccDbGraphProfile>):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileHatchAreaCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ProfileHatchArea
    Item: ProfileHatchArea
    def Add(self, hatchAreaName: str, upperProfileId: ObjectId, lowerProfileId: ObjectId, shapeStyleId: ObjectId) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, hatchAreaName: str) -> None: ...

class ProfileHorizontalGeometryPointLabelGroup(ProfileLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileHorizontalGeometryPointLabelGroup"""
    def __init__(self, *args) -> None: ...
    StaggerLineHeight2: float
    StaggerLineHeight1: float
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...
    def GetGeometryPointsOptions(self, ) -> GeometryPointSelector: ...
    def SetGeometryPointsOptions(self, profileGeometryPoints: GeometryPointSelector) -> None: ...

class ProfileLabelGroup(AutoFeatureLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileLabelGroup"""
    def __init__(self, *args) -> None: ...
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetAvailableLabelGroupIds(runtimeClass: RXClass, profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(runtimeClass: RXClass, profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class ProfileLineLabelGroup(ProfileLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileLineLabelGroup"""
    def __init__(self, *args) -> None: ...
    Weeding: float
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class ProfileMinorStationLabelGroup(ProfileStationLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileMinorStationLabelGroup"""
    def __init__(self, *args) -> None: ...
    MajorStationLabelGroup: ObjectId
    StaggerLineHeight2: float
    StaggerLineHeight1: float
    Increment: float
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(styleId: ObjectId, majorStationLabelGroupId: ObjectId, increment: float) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class ProfileOverride(GraphOverride):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileOverride"""
    def __init__(self, *args) -> None: ...
    OverrideStyleId: ObjectId
    OverrideStyleName: str
    ProfileName: str
    ProfileId: ObjectId
    UseOverrideStyle: bool
    Draw: bool
    def GetLabelGroupIds(self, ) -> ObjectIdCollection: ...
    def GetProfileLabelGroupIds(self, ) -> ObjectIdCollection: ...

class ProfileOverrideCollection(GraphOverrideCollection):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileOverrideCollection"""
    def __init__(self, *args) -> None: ...
    SplitAt: str
    ClipGridAt: str
    Count: int
    Item: ProfileOverride
    def GetEnumerator(self, ) -> IEnumerator: ...

class ProfilePVI(CivilWrapper<AeccDbVAlignment>):
    """.NET: Autodesk.Civil.DatabaseServices.ProfilePVI"""
    def __init__(self, *args) -> None: ...
    EntityAfter: int
    EntityBefore: int
    HeadlightSightDistance: float
    StoppingSightDistance: float
    PassingSightDistance: float
    GradeOut: float
    GradeIn: float
    Elevation: float
    RawStation: float
    Station: float
    PVIType: ProfileEntityType
    VerticalCurve: ProfileEntity

class ProfilePVICollection(CivilWrapper<AeccDbVAlignment>):
    """.NET: Autodesk.Civil.DatabaseServices.ProfilePVICollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ProfilePVI
    def AddPVI(self, station: float, elevation: float) -> ProfilePVI: ...
    def AddPVIArc(self, station: float, elevation: float, radius: float) -> ProfilePVI: ...
    def AddPVIAsymParabola(self, station: float, elevation: float, tangentLen1: float, tangentLen2: float) -> ProfilePVI: ...
    def AddPVISymParabola(self, station: float, elevation: float, curveLength: float) -> ProfilePVI: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def GetPVIAt(self, station: float, elevation: float) -> ProfilePVI: ...
    def Remove(self, profilePVI: ProfilePVI) -> None: ...
    def RemoveAt(self, station: float, elevation: float) -> None: ...

class ProfilePVILabelGroup(ProfileLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.ProfilePVILabelGroup"""
    def __init__(self, *args) -> None: ...
    StaggerLineHeight2: float
    StaggerLineHeight1: float
    Weeding: float
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class ProfileParabolaAsymmetric(ProfileEntity):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileParabolaAsymmetric"""
    def __init__(self, *args) -> None: ...
    AsymmetricLength2: float
    AsymmetricLength1: float
    TangentOffsetAtPVI: float
    HighLowPointElevation: float
    HighLowPointStation: float
    K: float
    GradeChange: float
    GradeOut: float
    GradeIn: float
    PVIElevation: float
    PVIStation: float
    CurveType: VerticalCurveType
    EntityType: ProfileEntityType
    Constraint2: EntityVerticalConstraintType
    MinimumKValueHSD: float
    MinimumKValuePSD: float
    MinimumKValueSSD: float
    HighestDesignSpeed: float
    EndElevation: float
    EndStation: float
    StartElevation: float
    StartStation: float
    Length: float
    EntityAfter: int
    EntityBefore: int
    Constraint1: ProfileEntityConstraintType
    EntityId: int

class ProfileParabolaSymmetric(ProfileEntity):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileParabolaSymmetric"""
    def __init__(self, *args) -> None: ...
    GradeAtThroughPoint2: float
    GradeAtThroughPoint1: float
    ThroughPoint3Elevation: float
    ThroughPoint3Station: float
    ThroughPoint2Elevation: float
    ThroughPoint2Station: float
    ThroughPoint1Elevation: float
    ThroughPoint1Station: float
    M: float
    TangentOffsetAtPVI: float
    HighLowPointElevation: float
    HighLowPointStation: float
    Radius: float
    K: float
    GradeChange: float
    GradeOut: float
    GradeIn: float
    PVIElevation: float
    PVIStation: float
    CurveType: VerticalCurveType
    EntityType: ProfileEntityType
    Constraint2: EntityVerticalConstraintType
    MinimumKValueHSD: float
    MinimumKValuePSD: float
    MinimumKValueSSD: float
    HighestDesignSpeed: float
    EndElevation: float
    EndStation: float
    StartElevation: float
    StartStation: float
    Length: float
    EntityAfter: int
    EntityBefore: int
    Constraint1: ProfileEntityConstraintType
    EntityId: int
    def GetHeadlightSightDistance(self, maxAngle: float, headlightHeight: float) -> float: ...
    def GetPassingSightDistance(self, eyeHeight: float, objectHeight: float) -> float: ...
    def GetStoppingSightDistance(self, eyeHeight: float, objectHeight: float) -> float: ...
    def SetHeadlightSightDistance(self, maxAngle: float, headlightHeight: float, distance: float) -> None: ...
    def SetPassingSightDistance(self, eyeHeight: float, objectHeight: float, distance: float) -> None: ...
    def SetStoppingSightDistance(self, eyeHeight: float, objectHeight: float, distance: float) -> None: ...

class ProfileProjection(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileProjection"""
    def __init__(self, *args) -> None: ...
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ProfileProjectionLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileProjectionLabel"""
    def __init__(self, *args) -> None: ...
    ProjectionSourceId: ObjectId
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(profileViewId: ObjectId, profileProjectionId: ObjectId, labelStyleId: ObjectId) -> ObjectId: ...

class ProfileSagCurveLabelGroup(ProfileLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileSagCurveLabelGroup"""
    def __init__(self, *args) -> None: ...
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class ProfileStationLabelGroup(ProfileLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileStationLabelGroup"""
    def __init__(self, *args) -> None: ...
    StaggerLineHeight2: float
    StaggerLineHeight1: float
    Increment: float
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId, increment: float) -> ObjectId: ...
    @staticmethod
    def CreateMajor(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId, increment: float) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class ProfileTangent(ProfileEntity):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileTangent"""
    def __init__(self, *args) -> None: ...
    ThroughPoint2Elevation: float
    ThroughPoint2Station: float
    ThroughPoint1Elevation: float
    ThroughPoint1Station: float
    Grade: float
    EntityType: ProfileEntityType
    Constraint2: EntityVerticalConstraintType
    MinimumKValueHSD: float
    MinimumKValuePSD: float
    MinimumKValueSSD: float
    HighestDesignSpeed: float
    EndElevation: float
    EndStation: float
    StartElevation: float
    StartStation: float
    Length: float
    EntityAfter: int
    EntityBefore: int
    Constraint1: ProfileEntityConstraintType
    EntityId: int

class ProfileType:
    """.NET: Autodesk.Civil.DatabaseServices.ProfileType"""
    def __init__(self, *args) -> None: ...
    ...

class ProfileUpdateType:
    """.NET: Autodesk.Civil.DatabaseServices.ProfileUpdateType"""
    def __init__(self, *args) -> None: ...
    ...

class ProfileView(Graph):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileView"""
    def __init__(self, *args) -> None: ...
    Bands: ProfileViewBandSet
    HatchAreas: ProfileHatchAreaCollection
    StructureOverrides: StructureOverrideCollection
    PipeOverrides: PipeOverrideCollection
    GraphOverrides: ProfileOverrideCollection
    SplitDataLines: ProfileViewSplitDataCollection
    SplitDatumRounding: DatumRoundingType
    SplitStationRounding: StationRoundingType
    SplitStationMode: SplitStationType
    SplitHeight: float
    SplitProfileView: bool
    ElevationMax: float
    ElevationMin: float
    ElevationRangeMode: ElevationRangeType
    StationEnd: float
    StationStart: float
    StationRangeMode: StationRangeType
    AlignmentId: ObjectId
    AlignmentName: str
    StyleId: ObjectId
    StyleName: str
    Location: Point3d
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(alignmentId: ObjectId, insertPosition: Point3d, profileViewName: str, profileViewBandSetId: ObjectId, stackedOptions: StackedProfileViewsCreationOptions, splitOptions: SplitProfileViewCreationOptions) -> ObjectIdCollection: ...
    @staticmethod
    def CreateMultiple(alignmentId: ObjectId, insertPosition: Point3d, profileViewName: str, profileViewBandSetId: ObjectId, stackedOptions: StackedProfileViewsCreationOptions, multipleOptions: MultipleProfileViewsCreationOptions, splitOptions: SplitProfileViewCreationOptions, datumType: ProfileViewDatumType) -> ObjectIdCollection: ...
    def FindStationAndElevationAtXY(self, x: float, y: float, station: float, elevation: float) -> bool: ...
    def FindXYAtStationAndElevation(self, station: float, elevation: float, x: float, y: float) -> bool: ...
    def GetAvailablePipeProfileLabelIds(self, ) -> ObjectIdCollection: ...
    def GetAvailableSpanningPipeProfileLabelIds(self, ) -> ObjectIdCollection: ...
    def GetAvailableStructureProfileLabelIds(self, ) -> ObjectIdCollection: ...
    def GetLabelIds(self, ) -> ObjectIdCollection: ...
    def GetPressureNetworkPartsInGraph(self, ) -> ObjectIdCollection: ...
    def GetProfileViewLabelIds(self, ) -> ObjectIdCollection: ...

class ProfileViewBandItem(ProfileViewBandSetItem):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileViewBandItem"""
    def __init__(self, *args) -> None: ...
    MaxOffsetDistance: Nullable
    Alignment2Id: ObjectId
    MaterialName: str
    DataSourceId: ObjectId
    Profile2Id: ObjectId
    Profile1Id: ObjectId
    AlignmentId: ObjectId
    LabelAtEndStation: bool
    LabelAtStartStation: bool
    BandStyleId: ObjectId
    MinorInterval: float
    MajorInterval: float
    StaggerLineHeight: float
    StaggerLabel: StaggerLabelType
    Weeding: float
    Gap: float
    ShowLabels: bool
    BandType: BandType
    Location: BandLocationType

class ProfileViewBandItemCollection(BandSetItemCollection):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileViewBandItemCollection"""
    def __init__(self, *args) -> None: ...
    Item: ProfileViewBandItem
    Count: int
    Location: BandLocationType
    def Add(self, bandType: BandType, profileBandStyleName: str) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class ProfileViewBandSet(GraphBandSet):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileViewBandSet"""
    def __init__(self, *args) -> None: ...
    MatchIncrementToGridIntervals: bool
    def GetBottomBandItems(self, ) -> ProfileViewBandItemCollection: ...
    def GetTopBandItems(self, ) -> ProfileViewBandItemCollection: ...
    def SetBottomBandItems(self, bandItems: ProfileViewBandItemCollection) -> None: ...
    def SetTopBandItems(self, bandItems: ProfileViewBandItemCollection) -> None: ...

class ProfileViewDepthLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileViewDepthLabel"""
    def __init__(self, *args) -> None: ...
    EndPoint: Point2d
    StartPoint: Point2d
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(profileViewId: ObjectId, labelStyleId: ObjectId, startPoint: Point2d, endPoint: Point2d) -> ObjectId: ...

class ProfileViewPart(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileViewPart"""
    def __init__(self, *args) -> None: ...
    ModelPartId: ObjectId
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetLabelIds(self, ) -> ObjectIdCollection: ...
    def GetPartProfileLabelIds(self, ) -> ObjectIdCollection: ...

class ProfileViewSplitData(CivilWrapper<AeccDbGraphProfile>):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileViewSplitData"""
    def __init__(self, *args) -> None: ...
    ProfileViewStyleId: ObjectId
    ProfileViewStyleName: str
    AdjustedDatum: float
    SplitStation: float

class ProfileViewSplitDataCollection(CivilWrapper<AeccDbGraphProfile>):
    """.NET: Autodesk.Civil.DatabaseServices.ProfileViewSplitDataCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ProfileViewSplitData
    def Add(self, rawStation: float, datum: float) -> ProfileViewSplitData: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def RemoveAt(self, index: int) -> None: ...

class PropertiesSet:
    """.NET: Autodesk.Civil.DatabaseServices.PropertiesSet"""
    def __init__(self, *args) -> None: ...
    ...

class QTOAreaResult(CivilWrapper<AeccQuantityTakeoffResult::SECTIONAL_RESULT>):
    """.NET: Autodesk.Civil.DatabaseServices.QTOAreaResult"""
    def __init__(self, *args) -> None: ...
    MomentOfFactoredUsableArea: float
    MomentOfFactoredFillArea: float
    MomentOfFactoredCutArea: float
    FactoredUsableArea: float
    FactoredFillArea: float
    FactoredCutArea: float
    MomentOfFillArea: float
    MomentOfCutArea: float
    FillArea: float
    CutArea: float

class QTOCriteriaNameMapping:
    """.NET: Autodesk.Civil.DatabaseServices.QTOCriteriaNameMapping"""
    def __init__(self, *args) -> None: ...
    isMappingCompleted: bool
    def Dispose(self, ) -> None: ...
    def GetMappedCorridorShape(self, materialName: str, shapeName: str, mappedCorridorId: ObjectId, mappedShapeName: str) -> None: ...
    def GetMappedSurfaceId(self, materialName: str, surfaceName: str) -> ObjectId: ...
    def MapCorridorShape(self, materialName: str, shapeName: str, mappedCorridorId: ObjectId, mappedShapeName: str) -> None: ...
    def MapSurface(self, materialName: str, surfaceName: str, mappedSurfaceId: ObjectId) -> None: ...

class QTOGenerateDetail:
    """.NET: Autodesk.Civil.DatabaseServices.QTOGenerateDetail"""
    def __init__(self, *args) -> None: ...
    AlignmentOffsetId: ObjectId
    ReportSelectedPayItemsOnly: bool
    EndStation: float
    StartStation: float
    AlignmentId: ObjectId
    ReportSheetOnly: bool
    ReportExtent: QTOReportExtent
    ReportType: QTOReportType
    Properties: int

class QTOMaterial:
    """.NET: Autodesk.Civil.DatabaseServices.QTOMaterial"""
    def __init__(self, *args) -> None: ...
    Item: QTOMaterialItem
    Item: QTOMaterialItem
    Count: int
    MaterialGaps: QTOMaterialGapCollection
    Subcriteria: QTOSubcriteriaCollection
    IsSubcriteriaSupported: bool
    ShapeStyleId: ObjectId
    QuantityType: MaterialQuantityType
    Name: str
    Guid: Guid
    MaterialListGuid: Guid
    SampleLineGroupId: ObjectId
    def Add(self, corridorId: ObjectId, shapeCode: str) -> QTOMaterialItem: ...
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetFactor(self, type: MaterialFactorType) -> float: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def IsFactorApplicable(self, type: MaterialFactorType) -> bool: ...
    def Remove(self, materialItem: QTOMaterialItem) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...
    def SetFactor(self, type: MaterialFactorType, newValue: float) -> None: ...

class QTOMaterialGap:
    """.NET: Autodesk.Civil.DatabaseServices.QTOMaterialGap"""
    def __init__(self, *args) -> None: ...
    Description: str
    RunInDistance: float
    RunOutDistance: float
    EndStation: float
    StartStation: float
    Applied: bool
    def Dispose(self, ) -> None: ...

class QTOMaterialGapCollection:
    """.NET: Autodesk.Civil.DatabaseServices.QTOMaterialGapCollection"""
    def __init__(self, *args) -> None: ...
    Item: QTOMaterialGap
    Count: int
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class QTOMaterialItem:
    """.NET: Autodesk.Civil.DatabaseServices.QTOMaterialItem"""
    def __init__(self, *args) -> None: ...
    Type: MaterialItemType
    Condition: MaterialConditionType
    Name: str
    MaterialGuid: Guid
    MaterialListGuid: Guid
    SampleLineGroupId: ObjectId
    def Dispose(self, ) -> None: ...
    def IsConditionApplicable(self, conditionType: MaterialConditionType) -> bool: ...

class QTOMaterialList:
    """.NET: Autodesk.Civil.DatabaseServices.QTOMaterialList"""
    def __init__(self, *args) -> None: ...
    MaterialListGaps: QTOMaterialListGapCollection
    CurveCorrectionTolerance: float
    IsCurveCorrectionEnabled: bool
    Name: str
    Guid: Guid
    SampleLineGroupId: ObjectId
    Item: QTOMaterial
    Item: QTOMaterial
    Item: QTOMaterial
    Count: int
    def Add(self, materialName: str) -> QTOMaterial: ...
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, material: QTOMaterial) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class QTOMaterialListCollection:
    """.NET: Autodesk.Civil.DatabaseServices.QTOMaterialListCollection"""
    def __init__(self, *args) -> None: ...
    VolumeCalculationMethodType: MaterialVolumeCalculationMethodType
    Item: QTOMaterialList
    Item: QTOMaterialList
    Item: QTOMaterialList
    Count: int
    def Add(self, materialListName: str) -> QTOMaterialList: ...
    def Fix(self, methodType: MaterialVolumeCalculationMethodType) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def ImportCriteria(self, criteriaNameMapping: QTOCriteriaNameMapping) -> QTOMaterialList: ...
    def Remove(self, materialList: QTOMaterialList) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...
    def Validate(self, methodType: MaterialVolumeCalculationMethodType) -> bool: ...

class QTOMaterialListGap:
    """.NET: Autodesk.Civil.DatabaseServices.QTOMaterialListGap"""
    def __init__(self, *args) -> None: ...
    Description: str
    EndStation: float
    StartStation: float
    def Dispose(self, ) -> None: ...

class QTOMaterialListGapCollection:
    """.NET: Autodesk.Civil.DatabaseServices.QTOMaterialListGapCollection"""
    def __init__(self, *args) -> None: ...
    Item: QTOMaterialListGap
    Count: int
    def Add(self, startStation: float, endStation: float) -> QTOMaterialListGap: ...
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, materialListGap: QTOMaterialListGap) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class QTOReportExtent:
    """.NET: Autodesk.Civil.DatabaseServices.QTOReportExtent"""
    def __init__(self, *args) -> None: ...
    ...

class QTOReportFormat:
    """.NET: Autodesk.Civil.DatabaseServices.QTOReportFormat"""
    def __init__(self, *args) -> None: ...
    ...

class QTOReportType:
    """.NET: Autodesk.Civil.DatabaseServices.QTOReportType"""
    def __init__(self, *args) -> None: ...
    ...

class QTOResultType:
    """.NET: Autodesk.Civil.DatabaseServices.QTOResultType"""
    def __init__(self, *args) -> None: ...
    ...

class QTOSectionalResult(CivilWrapper<AeccQuantityTakeoffResult::SECTIONAL_RESULT>):
    """.NET: Autodesk.Civil.DatabaseServices.QTOSectionalResult"""
    def __init__(self, *args) -> None: ...
    SampleLineId: ObjectId
    SampleLineName: str
    Station: float
    VolumeResult: QTOVolumeResult
    AreaResult: QTOAreaResult

class QTOSubcriteria:
    """.NET: Autodesk.Civil.DatabaseServices.QTOSubcriteria"""
    def __init__(self, *args) -> None: ...
    Item: QTOMaterialItem
    Item: QTOMaterialItem
    Count: int
    Name: str
    MaterialGuid: Guid
    MaterialListGuid: Guid
    SampleLineGroupId: ObjectId
    def Add(self, surfaceId: ObjectId) -> QTOMaterialItem: ...
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, materialItem: QTOMaterialItem) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class QTOSubcriteriaCollection:
    """.NET: Autodesk.Civil.DatabaseServices.QTOSubcriteriaCollection"""
    def __init__(self, *args) -> None: ...
    Item: QTOSubcriteria
    Count: int
    def Add(self, subcriteriaName: str) -> QTOSubcriteria: ...
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, subcriteria: QTOSubcriteria) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class QTOUtility:
    """.NET: Autodesk.Civil.DatabaseServices.QTOUtility"""
    def __init__(self, *args) -> None: ...
    PayItemCategorizationPath: str
    PayItemFileFormat: PayItemFileFormat
    PayItemFilePath: str
    @staticmethod
    def AddPayItemId(oid: ObjectId, payItemID: str) -> None: ...
    @staticmethod
    def DeleteAllPayItemsIds(oid: ObjectId) -> None: ...
    @staticmethod
    def DeletePayItemIds(oid: ObjectId, payItemIDs: StringCollection) -> None: ...
    @staticmethod
    def DrawXMLReport(__unnamed000: QTOReportFormat, strPayItemFilePath: str, generatedPayItemIds: list) -> bool: ...
    @staticmethod
    def GenerateXMLReport(reportInfo: QTOGenerateDetail, reportFilePath: str, generatedPayItemIds: list) -> bool: ...
    @staticmethod
    def GetPayItemIds(oid: ObjectId) -> StringCollection: ...
    @staticmethod
    def OpenPayItemFile(fileFormat: PayItemFileFormat, strPayItemFilePath: str, strPayItemCategorizationFilePath: str) -> bool: ...
    @staticmethod
    def TransformXMLReport(relXslFilePath: str, strPayItemFilePath: str, generatedPayItemIds: list, outFormatFilePath: str) -> bool: ...

class QTOVolumeResult(CivilWrapper<AeccQuantityTakeoffResult::SECTIONAL_RESULT>):
    """.NET: Autodesk.Civil.DatabaseServices.QTOVolumeResult"""
    def __init__(self, *args) -> None: ...
    IncrementalUsableVolume: float
    IncrementalFillVolume: float
    IncrementalCutVolume: float
    CumulativeUsableVolume: float
    CumulativeFillVolume: float
    CumulativeCutVolume: float

class QuantityTakeoffResult(CivilWrapper<AeccQuantityTakeoffResult>):
    """.NET: Autodesk.Civil.DatabaseServices.QuantityTakeoffResult"""
    def __init__(self, *args) -> None: ...
    def GetResult(self, sampleLineStation: float, tolerance: float) -> QTOSectionalResult: ...
    def GetResultsAlongSampleLines(self, ) -> list: ...

class RailAlignmentInfo:
    """.NET: Autodesk.Civil.DatabaseServices.RailAlignmentInfo"""
    def __init__(self, *args) -> None: ...
    TrackWidth: float
    def GetCantInfoAtStation(self, station: float) -> RailCANTInfo: ...
    def GetCantInfoAtStations(self, stations: IEnumerable) -> list: ...

class RailCANTInfo:
    """.NET: Autodesk.Civil.DatabaseServices.RailCANTInfo"""
    def __init__(self, *args) -> None: ...
    DesignSpeed: float
    VerticalSpeed: float
    CantJerk: float
    CantRatio: float
    CantDeficiencyVerticalSpeed: float
    CantDeficiencyGradient: float
    CantDeficiency: float
    EquilibriumCantVerticalSpeed: float
    EquilibriumCantGradient: float
    EquilibriumCant: float
    CurveRadius: float
    CantGradient: float
    LateralAcceleration: float
    RightRailElevationDifference: float
    LeftRailElevationDifference: float
    AppliedCANT: float
    Pivot: RailAlignmentPivotType

class RegionMatchType:
    """.NET: Autodesk.Civil.DatabaseServices.RegionMatchType"""
    def __init__(self, *args) -> None: ...
    ...

class RunoffMethod:
    """.NET: Autodesk.Civil.DatabaseServices.RunoffMethod"""
    def __init__(self, *args) -> None: ...
    ...

class SCSCSConstraints(CivilWrapper<AeccGeSCSCSConstraints>):
    """.NET: Autodesk.Civil.DatabaseServices.SCSCSConstraints"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CreateByArc1Angle(arc1Angle: float, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints: ...
    @staticmethod
    def CreateByArc1Length(arc1Len: float, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints: ...
    @staticmethod
    def CreateByArc1PassPt(ptArc1PassThru: Point2d, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints: ...
    @staticmethod
    def CreateByArc2Angle(arc2Angle: float, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints: ...
    @staticmethod
    def CreateByArc2Length(arc2Len: float, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints: ...
    @staticmethod
    def CreateByArc2PassPt(ptArc2PassThru: Point2d, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints: ...
    @staticmethod
    def CreateByEndPoint(endPoint: Point2d, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints: ...
    @staticmethod
    def CreateByStartPoint(startPoint: Point2d, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints: ...
    @staticmethod
    def CreateByTan1Length(extTan1Len: float, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints: ...
    @staticmethod
    def CreateByTan2Length(extTan2Len: float, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints: ...

class SCSSCSConstraints(CivilWrapper<AeccGeSCSSCSConstraints>):
    """.NET: Autodesk.Civil.DatabaseServices.SCSSCSConstraints"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CreateByArc1Angle(arc1Angle: float, sp1Param: float, arc1Radius: float, sp2Param: float, sp3Param: float, arc2Radius: float, sp4Param: float, isParamAValue: bool) -> SCSSCSConstraints: ...
    @staticmethod
    def CreateByArc1Length(arc1Len: float, sp1Param: float, arc1Radius: float, sp2Param: float, sp3Param: float, arc2Radius: float, sp4Param: float, isParamAValue: bool) -> SCSSCSConstraints: ...
    @staticmethod
    def CreateByArc1PassPt(ptArc1PassThru: Point2d, sp1Param: float, arc1Radius: float, sp2Param: float, sp3Param: float, arc2Radius: float, sp4Param: float, isParamAValue: bool) -> SCSSCSConstraints: ...
    @staticmethod
    def CreateByArc2Angle(arc2Angle: float, sp1Param: float, arc1Radius: float, sp2Param: float, sp3Param: float, arc2Radius: float, sp4Param: float, isParamAValue: bool) -> SCSSCSConstraints: ...
    @staticmethod
    def CreateByArc2Length(arc2Len: float, sp1Param: float, arc1Radius: float, sp2Param: float, sp3Param: float, arc2Radius: float, sp4Param: float, isParamAValue: bool) -> SCSSCSConstraints: ...
    @staticmethod
    def CreateByArc2PassPt(ptArc2PassThru: Point2d, sp1Param: float, arc1Radius: float, sp2Param: float, sp3Param: float, arc2Radius: float, sp4Param: float, isParamAValue: bool) -> SCSSCSConstraints: ...
    @staticmethod
    def CreateByEndPoint(endPoint: Point2d, sp1Param: float, arc1Radius: float, sp2Param: float, sp3Param: float, arc2Radius: float, sp4Param: float, isParamAValue: bool) -> SCSSCSConstraints: ...
    @staticmethod
    def CreateByStartPoint(startPoint: Point2d, sp1Param: float, arc1Radius: float, sp2Param: float, sp3Param: float, arc2Radius: float, sp4Param: float, isParamAValue: bool) -> SCSSCSConstraints: ...

class SECurve:
    """.NET: Autodesk.Civil.DatabaseServices.SECurve"""
    def __init__(self, *args) -> None: ...
    Name: str
    ParentAlignmentId: ObjectId
    EndStation: float
    StartStation: float
    CANTCriticalStations: CANTCriticalStationCollection
    CriticalStations: SuperelevationCriticalStationCollection

class SampleLine(GeoEntity):
    """.NET: Autodesk.Civil.DatabaseServices.SampleLine"""
    def __init__(self, *args) -> None: ...
    Vertices: SampleLineVertexCollection
    Station: float
    LockToStation: bool
    Number: int
    StyleName: str
    StyleId: ObjectId
    GroupId: ObjectId
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(sampleLineName: str, sampleLineGroupId: ObjectId, points: Point2dCollection) -> ObjectId: ...
    def GetMaterialSectionId(self, materialListGuid: Guid, materialGuid: Guid) -> ObjectId: ...
    def GetSectionId(self, sampledSourceId: ObjectId) -> ObjectId: ...
    def GetSectionIds(self, ) -> ObjectIdCollection: ...
    def GetSectionViewIds(self, ) -> ObjectIdCollection: ...

class SampleLineGroup(GeoEntity):
    """.NET: Autodesk.Civil.DatabaseServices.SampleLineGroup"""
    def __init__(self, *args) -> None: ...
    DefaultSamplineLabelStyleId: ObjectId
    DefaultSamplineStyleId: ObjectId
    MaterialLists: QTOMaterialListCollection
    IndividualSectionViewGroup: SectionViewGroup
    SectionViewGroups: SectionViewGroupCollection
    ParentAlignmentId: ObjectId
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(groupName: str, alignmentId: ObjectId) -> ObjectId: ...
    def GetAvailableSampleLineLabelGroupIds(self, ) -> ObjectIdCollection: ...
    def GetMappingGuid(self, mappingName: str) -> Guid: ...
    def GetMassHaulViewIds(self, ) -> ObjectIdCollection: ...
    def GetMaterialGuid(self, mappingGuid: Guid, materialName: str) -> Guid: ...
    def GetMaterialNamesInMapping(self, mappingGuid: Guid) -> list: ...
    def GetMaterialSectionSources(self, ) -> MaterialSectionSourceCollection: ...
    def GetQTOMappingNames(self, ) -> list: ...
    def GetSampleLineIds(self, station: float, tolerance: float) -> ObjectIdCollection: ...
    def GetSectionSources(self, ) -> SectionSourceCollection: ...
    def GetTotalVolumeResultDataForMaterialList(self, mappingGuid: Guid) -> QuantityTakeoffResult: ...
    @staticmethod
    def ReportQuantities(sampleLineGroupId: ObjectId, materialList: str, reportFile: str, styleSheetFile: str) -> None: ...

class SampleLineLabelGroup(AutoFeatureLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.SampleLineLabelGroup"""
    def __init__(self, *args) -> None: ...
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(sampleLineGroupId: ObjectId, labelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(sampleLineGroupId: ObjectId) -> ObjectIdCollection: ...

class SampleLineVertex(CivilWrapper<AeccDbSampleLine>):
    """.NET: Autodesk.Civil.DatabaseServices.SampleLineVertex"""
    def __init__(self, *args) -> None: ...
    OffsetIndex: int
    Side: SampleLineVertexSideType
    Location: Point3d

class SampleLineVertexCollection(CivilWrapper<AeccDbSampleLine>):
    """.NET: Autodesk.Civil.DatabaseServices.SampleLineVertexCollection"""
    def __init__(self, *args) -> None: ...
    Item: SampleLineVertex
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class SampleLineVertexSideType:
    """.NET: Autodesk.Civil.DatabaseServices.SampleLineVertexSideType"""
    def __init__(self, *args) -> None: ...
    ...

class SampledSectionLink(CivilWrapper<Autodesk::Civil::DatabaseServices::SampleSectionLinkData>):
    """.NET: Autodesk.Civil.DatabaseServices.SampledSectionLink"""
    def __init__(self, *args) -> None: ...
    StartPointElevation: float
    StartPointOffset: float
    EndPointStation: float
    StartPointStation: float
    EndPointElevation: float
    EndPointOffset: float

class SampledSectionLinkCollection(CivilWrapper<std::vector<Autodesk::Civil::DatabaseServices::SampleSectionLinkData \*\,std::allocator<Autodesk::Civil::DatabaseServices::SampleSectionLinkData \*> > >):
    """.NET: Autodesk.Civil.DatabaseServices.SampledSectionLinkCollection"""
    def __init__(self, *args) -> None: ...
    Item: SampledSectionLink
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class Section(GeoEntity):
    """.NET: Autodesk.Civil.DatabaseServices.Section"""
    def __init__(self, *args) -> None: ...
    CorridorSurfaceId: ObjectId
    SourceName: str
    MaximumElevation: float
    MinmumElevation: float
    RightSwathWidth: float
    LeftSwathWidth: float
    RightOffset: float
    LeftOffset: float
    SourceType: SectionSourceType
    UpdateMode: SectionUpdateType
    Station: float
    StyleName: str
    StyleId: ObjectId
    SectionPoints: SectionPointCollection
    SourceId: ObjectId
    ParentId: ObjectId
    SampleLineId: ObjectId
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SectionBandLabelGroup(AutoFeatureLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.SectionBandLabelGroup"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetAvailableLabelGroupIds(bandLabelGroupClassType: Type, sectionViewId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class SectionCorridorPointLabelGroup(SectionLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.SectionCorridorPointLabelGroup"""
    def __init__(self, *args) -> None: ...
    StaggerLineHeight2: float
    StaggerLineHeight1: float
    SubEntities: IList
    RangeEndFromFeature: bool
    RangeEnd: float
    RangeStartFromFeature: bool
    RangeStart: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(sectionViewId: ObjectId, sectionId: ObjectId, labelGroupStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(sectionViewId: ObjectId, sectionId: ObjectId) -> ObjectIdCollection: ...
    def getDisplayedSubEntities(self, ) -> IList: ...

class SectionDataBandLabelGroup(SectionBandLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.SectionDataBandLabelGroup"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetAvailableLabelGroupIds(sectionViewId: ObjectId) -> ObjectIdCollection: ...

class SectionDisplayOption(GraphDisplayOption):
    """.NET: Autodesk.Civil.DatabaseServices.SectionDisplayOption"""
    def __init__(self, *args) -> None: ...
    LabelSetId: ObjectId
    OverrideStyleId: ObjectId
    OverrideStyleName: str
    UseOverrideStyle: bool
    SourceType: SectionSourceType
    SourceName: str
    Draw: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SectionDisplayOptionCollection(GraphDisplayOptionCollection):
    """.NET: Autodesk.Civil.DatabaseServices.SectionDisplayOptionCollection"""
    def __init__(self, *args) -> None: ...
    ClipGridAt: str
    Count: int
    Item: SectionDisplayOption
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def SetLabelSet(self, sectionLabelSetId: ObjectId) -> None: ...

class SectionGradeBreakLabelGroup(SectionLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.SectionGradeBreakLabelGroup"""
    def __init__(self, *args) -> None: ...
    Weeding: float
    StaggerLineHeight2: float
    StaggerLineHeight1: float
    RangeEndFromFeature: bool
    RangeEnd: float
    RangeStartFromFeature: bool
    RangeStart: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(sectionViewId: ObjectId, sectionId: ObjectId, labelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(sectionViewId: ObjectId, sectionId: ObjectId) -> ObjectIdCollection: ...

class SectionLabelGroup(AutoFeatureLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.SectionLabelGroup"""
    def __init__(self, *args) -> None: ...
    RangeEndFromFeature: bool
    RangeEnd: float
    RangeStartFromFeature: bool
    RangeStart: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetAvailableLabelGroupIds(labelGroupClassType: Type, sectionViewId: ObjectId, sectionId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class SectionMinorOffsetLabelGroup(SectionOffsetLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.SectionMinorOffsetLabelGroup"""
    def __init__(self, *args) -> None: ...
    RangeEndFromFeature: bool
    RangeEnd: float
    RangeStartFromFeature: bool
    RangeStart: float
    MajorOffsetLabelGroupId: ObjectId
    StaggerLineHeight2: float
    StaggerLineHeight1: float
    Increment: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(majorOffsetLabelGroupId: ObjectId, increment: float, labelGroupStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(sectionViewId: ObjectId, sectionId: ObjectId) -> ObjectIdCollection: ...

class SectionOffsetLabelGroup(SectionLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.SectionOffsetLabelGroup"""
    def __init__(self, *args) -> None: ...
    StaggerLineHeight2: float
    StaggerLineHeight1: float
    Increment: float
    RangeEndFromFeature: bool
    RangeEnd: float
    RangeStartFromFeature: bool
    RangeStart: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateMajor(sectionViewId: ObjectId, sectionId: ObjectId, increment: float, labelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(sectionViewId: ObjectId, sectionId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class SectionOverride(GraphOverride):
    """.NET: Autodesk.Civil.DatabaseServices.SectionOverride"""
    def __init__(self, *args) -> None: ...
    OverrideStyleId: ObjectId
    OverrideStyleName: str
    SectionName: str
    SectionId: ObjectId
    UseOverrideStyle: bool
    Draw: bool
    def GetSectionLabelGroupIds(self, ) -> ObjectIdCollection: ...
    def ImportLabelSet(self, sectionLabelSetId: ObjectId) -> None: ...

class SectionOverrideCollection(GraphOverrideCollection):
    """.NET: Autodesk.Civil.DatabaseServices.SectionOverrideCollection"""
    def __init__(self, *args) -> None: ...
    ClipGridAt: str
    Count: int
    Item: SectionOverride
    def GetEnumerator(self, ) -> IEnumerator: ...

class SectionPipeNetwork(Section):
    """.NET: Autodesk.Civil.DatabaseServices.SectionPipeNetwork"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    CorridorSurfaceId: ObjectId
    SourceName: str
    MaximumElevation: float
    MinmumElevation: float
    RightSwathWidth: float
    LeftSwathWidth: float
    RightOffset: float
    LeftOffset: float
    SourceType: SectionSourceType
    UpdateMode: SectionUpdateType
    Station: float
    SectionPoints: SectionPointCollection
    SourceId: ObjectId
    ParentId: ObjectId
    SampleLineId: ObjectId
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SectionPoint(CivilWrapper<AeccDbSection>):
    """.NET: Autodesk.Civil.DatabaseServices.SectionPoint"""
    def __init__(self, *args) -> None: ...
    SegmentTo: int
    Location: Point3d

class SectionPointCollection(CivilWrapper<AeccDbSection>):
    """.NET: Autodesk.Civil.DatabaseServices.SectionPointCollection"""
    def __init__(self, *args) -> None: ...
    Item: SectionPoint
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class SectionProjection(Section):
    """.NET: Autodesk.Civil.DatabaseServices.SectionProjection"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    CorridorSurfaceId: ObjectId
    SourceName: str
    MaximumElevation: float
    MinmumElevation: float
    RightSwathWidth: float
    LeftSwathWidth: float
    RightOffset: float
    LeftOffset: float
    SourceType: SectionSourceType
    UpdateMode: SectionUpdateType
    Station: float
    SectionPoints: SectionPointCollection
    SourceId: ObjectId
    ParentId: ObjectId
    SampleLineId: ObjectId
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SectionProjectionLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.SectionProjectionLabel"""
    def __init__(self, *args) -> None: ...
    ProjectionSourceId: ObjectId
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(sectionViewId: ObjectId, sectionProjectionId: ObjectId, labelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelIds(sectionViewId: ObjectId) -> ObjectIdCollection: ...

class SectionSegmentBandLabelGroup(SectionBandLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.SectionSegmentBandLabelGroup"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetAvailableLabelGroupIds(sectionViewId: ObjectId) -> ObjectIdCollection: ...

class SectionSegmentLabelGroup(SectionLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.SectionSegmentLabelGroup"""
    def __init__(self, *args) -> None: ...
    RangeEndFromFeature: bool
    RangeEnd: float
    RangeStartFromFeature: bool
    RangeStart: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(sectionViewId: ObjectId, sectionId: ObjectId, labelGroupStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(sectionViewId: ObjectId, sectionId: ObjectId) -> ObjectIdCollection: ...

class SectionSource:
    """.NET: Autodesk.Civil.DatabaseServices.SectionSource"""
    def __init__(self, *args) -> None: ...
    IsSampled: bool
    UpdateMode: SectionUpdateType
    StyleId: ObjectId
    SourceName: str
    SourceType: SectionSourceType
    SourceId: ObjectId
    def GetSectionIds(self, ) -> ObjectIdCollection: ...

class SectionSourceCollection:
    """.NET: Autodesk.Civil.DatabaseServices.SectionSourceCollection"""
    def __init__(self, *args) -> None: ...
    Item: SectionSource
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class SectionSourceType:
    """.NET: Autodesk.Civil.DatabaseServices.SectionSourceType"""
    def __init__(self, *args) -> None: ...
    ...

class SectionUpdateType:
    """.NET: Autodesk.Civil.DatabaseServices.SectionUpdateType"""
    def __init__(self, *args) -> None: ...
    ...

class SectionView(Graph):
    """.NET: Autodesk.Civil.DatabaseServices.SectionView"""
    def __init__(self, *args) -> None: ...
    GraphOverrides: SectionOverrideCollection
    OffsetRight: float
    OffsetLeft: float
    IsOffsetRangeAutomatic: bool
    ElevationMax: float
    ElevationMin: float
    IsElevationRangeAutomatic: bool
    VolumeTables: SectionViewVolumeTableGroup
    ProfileGradePoints: SectionViewProfileGradePointCollection
    Bands: SectionViewBandSet
    SectionViewGroupName: str
    SampleLineId: ObjectId
    ParentEntityId: ObjectId
    StyleId: ObjectId
    Location: Point3d
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(sectionViewName: str, sampleLineId: ObjectId, location: Point3d) -> ObjectId: ...
    def FindOffsetAndElevationAtXY(self, x: float, y: float, offset: float, elevation: float) -> bool: ...
    def FindXYAtOffsetAndElevation(self, offset: float, elevation: float, x: float, y: float) -> bool: ...
    def GetPipeSectionLabelIds(self, ) -> ObjectIdCollection: ...
    def GetSectionCorridorPointLabelGroupIds(self, ) -> ObjectIdCollection: ...
    def GetSectionCrossingLabelIds(self, ) -> ObjectIdCollection: ...
    def GetSectionGradeBreakLabelGroupIds(self, ) -> ObjectIdCollection: ...
    def GetSectionMinorOffsetLabelGroupIds(self, ) -> ObjectIdCollection: ...
    def GetSectionOffsetLabelGroupIds(self, ) -> ObjectIdCollection: ...
    def GetSectionProjectionLabelIds(self, ) -> ObjectIdCollection: ...
    def GetSectionSegmentLabelGroupIds(self, ) -> ObjectIdCollection: ...
    def GetSectionViewDepthLabelIds(self, ) -> ObjectIdCollection: ...
    def GetSectionViewGroup(self, ) -> SectionViewGroup: ...
    def GetSectionViewOffsetElevationLabelIds(self, ) -> ObjectIdCollection: ...
    def GetStructureSectionLabelIds(self, ) -> ObjectIdCollection: ...

class SectionViewBandItem(SectionViewBandSetItem):
    """.NET: Autodesk.Civil.DatabaseServices.SectionViewBandItem"""
    def __init__(self, *args) -> None: ...
    Section2Id: ObjectId
    Section1Id: ObjectId
    SampleLineId: ObjectId
    LabelAtEndOffset: bool
    LabelAtStartOffset: bool
    BandStyleId: ObjectId
    MinorInterval: float
    MajorInterval: float
    StaggerLineHeight: float
    StaggerLabel: StaggerLabelType
    Weeding: float
    Gap: float
    ShowLabels: bool
    BandType: BandType
    Location: BandLocationType

class SectionViewBandItemCollection(BandSetItemCollection):
    """.NET: Autodesk.Civil.DatabaseServices.SectionViewBandItemCollection"""
    def __init__(self, *args) -> None: ...
    Item: SectionViewBandItem
    Count: int
    Location: BandLocationType
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class SectionViewBandSet(GraphBandSet):
    """.NET: Autodesk.Civil.DatabaseServices.SectionViewBandSet"""
    def __init__(self, *args) -> None: ...
    MatchIncrementToGridIntervals: bool
    def GetBottomBandItems(self, ) -> SectionViewBandItemCollection: ...
    def GetTopBandItems(self, ) -> SectionViewBandItemCollection: ...
    def ImportBandSetStyle(self, bandSetId: ObjectId) -> None: ...
    def SetBottomBandItems(self, bandItems: SectionViewBandItemCollection) -> None: ...
    def SetTopBandItems(self, bandItems: SectionViewBandItemCollection) -> None: ...

class SectionViewDepthLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.SectionViewDepthLabel"""
    def __init__(self, *args) -> None: ...
    EndPoint: Point2d
    StartPoint: Point2d
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(sectionViewId: ObjectId, startPoint: Point2d, endPoint: Point2d, labelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelIds(sectionViewId: ObjectId) -> ObjectIdCollection: ...

class SectionViewGroup:
    """.NET: Autodesk.Civil.DatabaseServices.SectionViewGroup"""
    def __init__(self, *args) -> None: ...
    LayoutName: str
    TemplateFilePath: str
    SampleLineGroupId: ObjectId
    IsIndividual: bool
    Name: str
    PlotStyleId: ObjectId
    def GetSectionViewIds(self, ) -> ObjectIdCollection: ...
    def ImportLabelSetForSectionsInGroup(self, sectionSource: SectionSource, labelSetId: ObjectId) -> None: ...
    def UpdateLayout(self, ) -> None: ...

class SectionViewGroupCollection:
    """.NET: Autodesk.Civil.DatabaseServices.SectionViewGroupCollection"""
    def __init__(self, *args) -> None: ...
    Item: SectionViewGroup
    Count: int
    def Add(self, insertPosition: Point3d, startStation: float, endStation: float, rangeOptions: SectionViewGroupCreationRangeOptions, placementOptions: SectionViewGroupCreationPlacementOptions, sectionDisplayOptions: SectionDisplayOptionCollection, sectionViewStyleId: ObjectId, sectionViewBandSetStyleId: ObjectId) -> SectionViewGroup: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, sectionViewGroup: SectionViewGroup) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class SectionViewGroupCreationPlacementOptions:
    """.NET: Autodesk.Civil.DatabaseServices.SectionViewGroupCreationPlacementOptions"""
    def __init__(self, *args) -> None: ...
    LayoutName: str
    TemplateFilePath: str
    PlacementOption: PlacementOptionType
    def GetAvailableLayoutNames(self, templateFilePath: str) -> list: ...
    def UseDraftPlacement(self, ) -> None: ...
    def UseProductionPlacement(self, templateFilePath: str, layoutName: str) -> None: ...

class SectionViewGroupCreationRangeOptions:
    """.NET: Autodesk.Civil.DatabaseServices.SectionViewGroupCreationRangeOptions"""
    def __init__(self, *args) -> None: ...
    ElevationRangeType: SectionViewElevationRangeType
    Elevation: float
    UseUserSpecifiedElevation: bool
    RightOffset: float
    LeftOffset: float
    UseUserSpecifiedOffset: bool
    def Dispose(self, ) -> None: ...
    def FollowSection(self, sectionSource: SectionSource) -> None: ...
    def SetOffsetRange(self, leftOffset: float, rightOffset: float) -> None: ...

class SectionViewOffsetElevationLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.SectionViewOffsetElevationLabel"""
    def __init__(self, *args) -> None: ...
    Section2Id: ObjectId
    Section1Id: ObjectId
    Elevation: float
    Offset: float
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(sectionViewId: ObjectId, offset: float, elevation: float, labelStyleId: ObjectId, markerStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelIds(sectionViewId: ObjectId) -> ObjectIdCollection: ...

class SectionViewProfileGradePoint:
    """.NET: Autodesk.Civil.DatabaseServices.SectionViewProfileGradePoint"""
    def __init__(self, *args) -> None: ...
    MarkerStyleId: ObjectId
    ProfileId: ObjectId
    IsShow: bool
    AlignmentId: ObjectId

class SectionViewProfileGradePointCollection:
    """.NET: Autodesk.Civil.DatabaseServices.SectionViewProfileGradePointCollection"""
    def __init__(self, *args) -> None: ...
    Item: SectionViewProfileGradePoint
    Count: int
    def Add(self, alignmentId: ObjectId) -> SectionViewProfileGradePoint: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, pgPoint: SectionViewProfileGradePoint) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class SectionViewQuantityTakeoffTable(Table):
    """.NET: Autodesk.Civil.DatabaseServices.SectionViewQuantityTakeoffTable"""
    def __init__(self, *args) -> None: ...
    MaterialListGuid: Guid
    Type: VolumeTableType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddSelectedMaterial(self, materialGuid: Guid) -> bool: ...
    def GetSelectedMaterials(self, ) -> list: ...
    def RemoveSelectedMaterial(self, materialGuid: Guid) -> bool: ...

class SectionViewVolumeTableAnchorType:
    """.NET: Autodesk.Civil.DatabaseServices.SectionViewVolumeTableAnchorType"""
    def __init__(self, *args) -> None: ...
    ...

class SectionViewVolumeTableGroup:
    """.NET: Autodesk.Civil.DatabaseServices.SectionViewVolumeTableGroup"""
    def __init__(self, *args) -> None: ...
    OffsetY: float
    OffsetX: float
    TableLayoutType: SectionViewVolumeTableLayoutType
    TableAnchorType: SectionViewVolumeTableAnchorType
    SectionViewAnchorType: SectionViewVolumeTableAnchorType
    def CreateVolumeTable(self, type: VolumeTableType, materialListGuid: Guid) -> ObjectId: ...
    def GetVolumeTableIds(self, ) -> ObjectIdCollection: ...
    def Swap(self, tableId1: ObjectId, tableId2: ObjectId) -> None: ...
    def SwapAt(self, index1: int, index2: int) -> None: ...

class SectionViewVolumeTableLayoutType:
    """.NET: Autodesk.Civil.DatabaseServices.SectionViewVolumeTableLayoutType"""
    def __init__(self, *args) -> None: ...
    ...

class SectionalDataBandLabelGroup(ProfileBandLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.SectionalDataBandLabelGroup"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(profileViewId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class ShallowFlowSurfaceType:
    """.NET: Autodesk.Civil.DatabaseServices.ShallowFlowSurfaceType"""
    def __init__(self, *args) -> None: ...
    ...

class Shape(CivilWrapper<AeccDbEntity>):
    """.NET: Autodesk.Civil.DatabaseServices.Shape"""
    def __init__(self, *args) -> None: ...
    Index: int
    Links: LinkCollection
    IsHidden: bool
    Codes: CodeCollection
    def AddHole(self, links: list) -> None: ...

class ShapeCollection(CivilWrapper<AeccDbEntity>):
    """.NET: Autodesk.Civil.DatabaseServices.ShapeCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: Shape
    def Add(self, link1: Link, link2: Link, link3: Link, link4: Link, codes: list) -> Shape: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, shape: Shape) -> None: ...

class Sheet(GeoEntity):
    """.NET: Autodesk.Civil.DatabaseServices.Sheet"""
    def __init__(self, *args) -> None: ...
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SideRoadProfileDistanceRuleType:
    """.NET: Autodesk.Civil.DatabaseServices.SideRoadProfileDistanceRuleType"""
    def __init__(self, *args) -> None: ...
    ...

class Site(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.Site"""
    def __init__(self, *args) -> None: ...
    UDPClassificationApplyType: UDPClassificationApplyType
    UDPClassificationName: str
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(document: CivilDocument, siteName: str) -> ObjectId: ...
    def GetAlignmentIds(self, ) -> ObjectIdCollection: ...
    def GetFeatureLineIds(self, ) -> ObjectIdCollection: ...
    def GetParcelIds(self, ) -> ObjectIdCollection: ...
    def UseAllClassifications(self, ) -> None: ...
    def UseCustomClassification(self, udpClassification: UDPClassification) -> None: ...
    def UseNoneClassification(self, ) -> None: ...

class SlopeElevationTarget(CivilWrapper<AeccSlopeElevationTarget>):
    """.NET: Autodesk.Civil.DatabaseServices.SlopeElevationTarget"""
    def __init__(self, *args) -> None: ...
    TargetId: ObjectId
    def GetElevation(self, alignmentId: ObjectId, stationOnAlignment: float, side: AlignmentSide) -> float: ...
    def GetNearestPipeOfNetworkToAlignment(self, alignmentId: ObjectId, stationOnAlignment: float, side: AlignmentSide, pipeId: ObjectId) -> None: ...

class SlopeLineDefinition:
    """.NET: Autodesk.Civil.DatabaseServices.SlopeLineDefinition"""
    def __init__(self, *args) -> None: ...
    index: int
    side: SlopeLineSide
    type: SlopeLineType

class SlopeLineSide:
    """.NET: Autodesk.Civil.DatabaseServices.SlopeLineSide"""
    def __init__(self, *args) -> None: ...
    ...

class SlopeLineType:
    """.NET: Autodesk.Civil.DatabaseServices.SlopeLineType"""
    def __init__(self, *args) -> None: ...
    ...

class SpanningPipeLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.SpanningPipeLabel"""
    def __init__(self, *args) -> None: ...
    ShowSpannedPipes: bool
    AnchorPipeId: ObjectId
    StructureIds: ObjectIdCollection
    PipeIds: ObjectIdCollection
    Length3DEdgeToEdge: float
    Length2DEdgeToEdge: float
    Length3DCenterToCenter: float
    Length2DCenterToCenter: float
    Ratio: float
    ReferenceAlignmentId: ObjectId
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(partIds: ObjectIdCollection, anchorPipeId: ObjectId, ratio: float, labelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelIds(pipeId: ObjectId) -> ObjectIdCollection: ...

class SpanningPipeProfileLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.SpanningPipeProfileLabel"""
    def __init__(self, *args) -> None: ...
    AnchorProfileViewPartId: ObjectId
    ProfileViewStructureIds: ObjectIdCollection
    ProfileViewPipeIds: ObjectIdCollection
    ShowSpannedProfileViewPipes: bool
    Length3DEdgeToEdge: float
    Length2DEdgeToEdge: float
    Length3DCenterToCenter: float
    Length2DCenterToCenter: float
    Ratio: float
    ReferenceAlignmentId: ObjectId
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(profileViewPartIds: ObjectIdCollection, anchorProfileViewPartId: ObjectId, profileViewId: ObjectId, ratio: float, labelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelIds(profileViewId: ObjectId) -> ObjectIdCollection: ...

class SpiralCurveType:
    """.NET: Autodesk.Civil.DatabaseServices.SpiralCurveType"""
    def __init__(self, *args) -> None: ...
    ...

class SpiralDirectionType:
    """.NET: Autodesk.Civil.DatabaseServices.SpiralDirectionType"""
    def __init__(self, *args) -> None: ...
    ...

class SpiralParamType:
    """.NET: Autodesk.Civil.DatabaseServices.SpiralParamType"""
    def __init__(self, *args) -> None: ...
    ...

class SplitProfileViewCreationOptions:
    """.NET: Autodesk.Civil.DatabaseServices.SplitProfileViewCreationOptions"""
    def __init__(self, *args) -> None: ...
    SplitDatumOption: ProfileViewSplitDatumType
    SplitStationOption: ProfileViewSplitStationType
    LastViewStyleId: ObjectId
    IntermediateViewStyleId: ObjectId
    FirstViewStyleId: ObjectId
    ViewHeight: float

class SplitStationType:
    """.NET: Autodesk.Civil.DatabaseServices.SplitStationType"""
    def __init__(self, *args) -> None: ...
    ...

class StackedProfileViewsCreationOptions:
    """.NET: Autodesk.Civil.DatabaseServices.StackedProfileViewsCreationOptions"""
    def __init__(self, *args) -> None: ...
    BottomViewStyleId: ObjectId
    MiddleViewStyleId: ObjectId
    TopViewStyleId: ObjectId
    GapBetweenViews: float
    NumberOfViews: int

class StandardPointGroupQuery(PointGroupQuery):
    """.NET: Autodesk.Civil.DatabaseServices.StandardPointGroupQuery"""
    def __init__(self, *args) -> None: ...
    PointGroups: IList
    ExcludeFullDescriptions: str
    IncludeFullDescriptions: str
    ExcludeRawDescriptions: str
    IncludeRawDescriptions: str
    ExcludeNames: str
    IncludeNames: str
    ExcludeElevations: str
    IncludeElevations: str
    ExcludeNumbers: str
    IncludeNumbers: str
    IncludeAllPoints: bool
    QueryString: str
    UseCaseSensitiveMatch: bool

class Station:
    """.NET: Autodesk.Civil.DatabaseServices.Station"""
    def __init__(self, *args) -> None: ...
    Location: Point2d
    StationType: StationTypes
    GeometryStationType: AlignmentGeometryPointStationType
    RawStation: float

class StationElevationLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.StationElevationLabel"""
    def __init__(self, *args) -> None: ...
    Profile2Id: ObjectId
    Profile1Id: ObjectId
    Elevation: float
    Station: float
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(profileViewId: ObjectId, labelStyleId: ObjectId, markerStyleId: ObjectId, station: float, elevation: float) -> ObjectId: ...

class StationEquation(CivilWrapper<AeccDbAlignment>):
    """.NET: Autodesk.Civil.DatabaseServices.StationEquation"""
    def __init__(self, *args) -> None: ...
    EquationType: StationEquationType
    StationAhead: float
    StationBack: float
    RawStationBack: float

class StationEquationCollection(CivilWrapper<AeccDbAlignment>):
    """.NET: Autodesk.Civil.DatabaseServices.StationEquationCollection"""
    def __init__(self, *args) -> None: ...
    Item: StationEquation
    Count: int
    def Add(self, rawStationBack: float, stationAhead: float, stationEquationType: StationEquationType) -> StationEquation: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def GetStationEquation(self, rawStationBack: float) -> StationEquation: ...
    def Remove(self, rawStationBack: float) -> None: ...

class StationEquationType:
    """.NET: Autodesk.Civil.DatabaseServices.StationEquationType"""
    def __init__(self, *args) -> None: ...
    ...

class StationOffsetLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.StationOffsetLabel"""
    def __init__(self, *args) -> None: ...
    Location: Point2d
    AnchorAtXY: bool
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(alignmentId: ObjectId, labelStyleId: ObjectId, markerStyleId: ObjectId, location: Point2d) -> ObjectId: ...

class StationRangeType:
    """.NET: Autodesk.Civil.DatabaseServices.StationRangeType"""
    def __init__(self, *args) -> None: ...
    ...

class StationRoundingType:
    """.NET: Autodesk.Civil.DatabaseServices.StationRoundingType"""
    def __init__(self, *args) -> None: ...
    ...

class StationTypes:
    """.NET: Autodesk.Civil.DatabaseServices.StationTypes"""
    def __init__(self, *args) -> None: ...
    ...

class Structure(Part):
    """.NET: Autodesk.Civil.DatabaseServices.Structure"""
    def __init__(self, *args) -> None: ...
    InletCurbOpeningHeight: float
    InletCurbOpeningLength: float
    InletGrateLength: float
    InletGrateWidth: float
    InletLocalDepression: float
    BypassTarget: ObjectId
    InletLocation: InletLocationType
    InletGutterManningsCoefficient: float
    InletGutterWidth: float
    InletGutterCrossSlope: float
    InletRoadCrossSlope: float
    InletLongitudinalSlope: float
    InletClogging: float
    InletThroatAngle: InletThroatAngleType
    InletGrateType: InletGrateType
    StructureType: PipeNetworkStructureType
    KnownCapacity: float
    EnergyGradeLine: float
    HydraulicGradeLine: float
    CatchmentsRunoffCoefficient: float
    CatchmentsTimeOfConcentration: float
    CatchmentsArea: float
    StyleId: ObjectId
    Location: Point3d
    HeadwallBaseThickness: float
    HeadwallBaseWidth: float
    ConeHeight: float
    BarrelPipeClearance: float
    FrameDiameter: float
    FrameHeight: float
    Cover: str
    Grate: str
    Frame: str
    FloorThickness: float
    RimToSumpHeight: float
    VerticalPipeClearance: float
    Easting: float
    Northing: float
    Station: float
    Offset: float
    SurfaceElevationAtInsertionPoint: float
    RimElevation: float
    SumpDepth: float
    AutomaticRimSurfaceAdjustment: bool
    SurfaceAdjustmentValue: float
    SumpElevation: float
    Height: float
    InnerLength: float
    Length: float
    InnerDiameterOrWidth: float
    DiameterOrWidth: float
    PipeUpperTopDepth: float
    PipeLowestBottomDepth: float
    PipeOuterTopDepth: float
    PipeOuterBottomDepth: float
    PipeInvertDepth: float
    PipeCenterDepth: float
    PipeInnerDiameterOrWidth: float
    PipeWallThickness: float
    BoundingShape: BoundingShapeType
    Rotation: float
    ControlSumpBy: StructureControlSumpType
    ConnectedPipesCount: int
    ConnectedPipe: ObjectId
    PartFamilyName: str
    PartFamilyId: ObjectId
    Solid3dBody: Solid3d
    OverrideRuleSet: bool
    RuleSetStyleName: str
    RuleSetStyleId: ObjectId
    PartData: PartDataRecord
    PartDefId: ObjectId
    SectionViewPartId: ObjectId
    ProfileViewPartId: ObjectId
    KnownFlow: float
    ConnectedPartCount: int
    RefSurfaceName: str
    RefSurfaceId: ObjectId
    SurfaceId: ObjectId
    RefAlignmentName: str
    RefAlignmentId: ObjectId
    NetworkName: str
    NetworkId: ObjectId
    WallThickness: float
    Material: str
    PartDescription: str
    PartSizeName: str
    Name: str
    Domain: DomainType
    PartSubType: str
    ParamsString: ParamStringCollection
    ParamsLong: ParamLongCollection
    ParamsDouble: ParamDoubleCollection
    ParamsBool: ParamBoolCollection
    PartType: PartType
    Position: Point3d
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ConnectToPipe(self, pipeId: ObjectId, positionType: ConnectorPositionType) -> None: ...
    def Disconnect(self, pipeId: ObjectId) -> None: ...
    def GetAvailableStructureLabelIds(self, ) -> ObjectIdCollection: ...
    def GetConnectedCatchmentIds(self, ) -> ObjectIdCollection: ...
    def GetConnectedPipeNames(self, ) -> list: ...
    def GetConnectedPressurePipeIds(self, ) -> ObjectIdCollection: ...
    def GetLabelIds(self, ) -> ObjectIdCollection: ...
    def IsConnectedPipeFlowingIn(self, index: int) -> bool: ...
    def IsConnectedPipeFlowingOut(self, index: int) -> bool: ...
    def IsPointInsideStructureRegion(self, point: Point3d) -> bool: ...
    def ResizeByPipeDepths(self, ) -> bool: ...
    def ResizeJunctionStructure(self, partFamilyGuid: str, rimElevation: float, sumpElevation: float) -> None: ...

class StructureControlSumpType:
    """.NET: Autodesk.Civil.DatabaseServices.StructureControlSumpType"""
    def __init__(self, *args) -> None: ...
    ...

class StructureLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.StructureLabel"""
    def __init__(self, *args) -> None: ...
    ReferenceAlignmentId: ObjectId
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(structureId: ObjectId, labelStyleId: ObjectId, labelLocation: Point3d) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelIds(structureId: ObjectId) -> ObjectIdCollection: ...

class StructureOverride(GraphOverride):
    """.NET: Autodesk.Civil.DatabaseServices.StructureOverride"""
    def __init__(self, *args) -> None: ...
    OverrideStyleId: ObjectId
    OverrideStyleName: str
    StructName: str
    StructId: ObjectId
    Draw: bool
    UseOverrideStyle: bool

class StructureOverrideCollection(GraphOverrideCollection):
    """.NET: Autodesk.Civil.DatabaseServices.StructureOverrideCollection"""
    def __init__(self, *args) -> None: ...
    SplitAt: str
    ClipGridAt: str
    Count: int
    Item: StructureOverride
    def GetEnumerator(self, ) -> IEnumerator: ...

class StructureProfileLabel(PartProfileLabel):
    """.NET: Autodesk.Civil.DatabaseServices.StructureProfileLabel"""
    def __init__(self, *args) -> None: ...
    ReferenceAlignmentId: ObjectId
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(profileViewId: ObjectId, profileViewPartId: ObjectId, labelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelIds(profileViewId: ObjectId) -> ObjectIdCollection: ...

class StructureSectionLabel(PartSectionLabel):
    """.NET: Autodesk.Civil.DatabaseServices.StructureSectionLabel"""
    def __init__(self, *args) -> None: ...
    ReferenceAlignmentId: ObjectId
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(sectionViewId: ObjectId, structureId: ObjectId, sectionPipeNetworkId: ObjectId, partIndex: int, labelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelIds(sectionViewId: ObjectId) -> ObjectIdCollection: ...

class Subassembly(GeoEntity):
    """.NET: Autodesk.Civil.DatabaseServices.Subassembly"""
    def __init__(self, *args) -> None: ...
    IsFromSubassemblyComposer: bool
    Origin: Point3d
    Side: SubassemblySideType
    HasSide: bool
    Status: SubassemblyStatus
    Version: str
    OffsetToParentAssembly: Vector2d
    OffsetToBaseline: Vector2d
    OffsetToAssembly: Vector2d
    OffsetAssemblyName: str
    AttachedToOffsetAssembly: bool
    PointIndexHookTo: int
    SubassemblyHookTo: ObjectId
    HasParentAssembly: bool
    AssemblyId: ObjectId
    ResourceModule: str
    HelpData: str
    HelpCommand: str
    HelpFile: str
    UseEmbeddedProject: bool
    CodeSetStyleName: str
    IsDynamic: bool
    DefaultLoopInLayoutMode: bool
    DefaultLoopOffsetInLayoutMode: float
    Shapes: ShapeCollection
    Links: LinkCollection
    Points: PointCollection
    ParamsString: ParamStringCollection
    ParamsDouble: ParamDoubleCollection
    ParamsLong: ParamLongCollection
    ParamsBool: ParamBoolCollection
    GeometryGenerator: SubassemblyGenerator
    StyleName: str
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def EraseAllParams(self, ) -> None: ...
    def GetResourceString(self, resourceId: str) -> str: ...
    def Run(self, ) -> None: ...
    def ShowHelp(self, ) -> None: ...

class SubassemblyCollection(CivilWrapper<AcDbDatabase>):
    """.NET: Autodesk.Civil.DatabaseServices.SubassemblyCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    def Add(self, subassemblyName: str, entityId: ObjectId, midOrdinateDist: float, linkCreationOption: LinkCreationType) -> ObjectId: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def GetSubassemblyIdsByName(self, subassemblyName: str) -> ObjectIdCollection: ...
    def ImportSACSubassembly(self, subassemblyName: str, pktFilePath: str, location: Point3d) -> ObjectId: ...
    def ImportStockSubassembly(self, subassemblyName: str, className: str, location: Point3d) -> ObjectId: ...
    def ImportSubassembly(self, subassemblyName: str, atcFilePath: str, itemId: str, location: Point3d) -> ObjectId: ...
    def Remove(self, subassemblyId: ObjectId) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class SubassemblyGenerator:
    """.NET: Autodesk.Civil.DatabaseServices.SubassemblyGenerator"""
    def __init__(self, *args) -> None: ...
    MacroOrClassName: str
    ProjectOrAssemblyName: str
    GeometryGenerateMode: SubassemblyGeometryGenerateMode

class SubassemblyGeometryGenerateMode:
    """.NET: Autodesk.Civil.DatabaseServices.SubassemblyGeometryGenerateMode"""
    def __init__(self, *args) -> None: ...
    ...

class SubassemblyLogicalNameType:
    """.NET: Autodesk.Civil.DatabaseServices.SubassemblyLogicalNameType"""
    def __init__(self, *args) -> None: ...
    ...

class SubassemblySideType:
    """.NET: Autodesk.Civil.DatabaseServices.SubassemblySideType"""
    def __init__(self, *args) -> None: ...
    ...

class SubassemblyStatus:
    """.NET: Autodesk.Civil.DatabaseServices.SubassemblyStatus"""
    def __init__(self, *args) -> None: ...
    ...

class SubassemblyTargetInfo(DisposableWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.SubassemblyTargetInfo"""
    def __init__(self, *args) -> None: ...
    UseSameSideTarget: bool
    TargetToOption: SubassemblyTargetToOption
    TargetType: SubassemblyLogicalNameType
    TargetIds: ObjectIdCollection
    DisplayName: str
    LogicalName: str
    SubassemblyName: str
    AssemblyGroupName: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SubassemblyTargetInfoCollection(DisposableWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.SubassemblyTargetInfoCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: SubassemblyTargetInfo
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class SubassemblyTargetToOption:
    """.NET: Autodesk.Civil.DatabaseServices.SubassemblyTargetToOption"""
    def __init__(self, *args) -> None: ...
    ...

class SuperElevationBandLabelGroup(ProfileBandLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.SuperElevationBandLabelGroup"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(profileViewId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class SuperelevationCriticalStation:
    """.NET: Autodesk.Civil.DatabaseServices.SuperelevationCriticalStation"""
    def __init__(self, *args) -> None: ...
    TransitionDescription: str
    Station: float
    StationType: SuperelevationCriticalStationType
    TransitionRegionType: SuperelevationTransitionRegionType
    SuperelevationCurveName: str
    ParentAlignmentId: ObjectId
    def BreakSegment(self, crossSegmentType: SuperelevationCrossSegmentType) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetSlope(self, crossSegmentType: SuperelevationCrossSegmentType) -> float: ...
    def GetSmoothingLength(self, crossSegmentType: SuperelevationCrossSegmentType) -> float: ...
    def IsGradeBreak(self, crossSegmentType: SuperelevationCrossSegmentType) -> bool: ...
    def RemoveGradeBreak(self, crossSegmentType: SuperelevationCrossSegmentType) -> None: ...
    def SetSlope(self, crossSegmentType: SuperelevationCrossSegmentType, slope: float) -> None: ...
    def SetSmoothingLength(self, crossSegmentType: SuperelevationCrossSegmentType, length: float) -> None: ...

class SuperelevationCriticalStationCollection:
    """.NET: Autodesk.Civil.DatabaseServices.SuperelevationCriticalStationCollection"""
    def __init__(self, *args) -> None: ...
    ParentAlignmentId: ObjectId
    Count: int
    Item: SuperelevationCriticalStation
    def Add(self, station: float, criticalStationType: SuperelevationCriticalStationType, attainmentRegionType: SuperelevationAttainmentRegionType) -> None: ...
    def GetCriticalStationAt(self, station: float, tolerance: float) -> SuperelevationCriticalStation: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def IsCriticalStation(self, station: float, tolerance: float) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class SuperelevationCurve(SECurve):
    """.NET: Autodesk.Civil.DatabaseServices.SuperelevationCurve"""
    def __init__(self, *args) -> None: ...
    Name: str
    ParentAlignmentId: ObjectId
    EndStation: float
    StartStation: float
    CANTCriticalStations: CANTCriticalStationCollection
    CriticalStations: SuperelevationCriticalStationCollection

class SuperelevationCurveCollection:
    """.NET: Autodesk.Civil.DatabaseServices.SuperelevationCurveCollection"""
    def __init__(self, *args) -> None: ...
    ParentAlignmentId: ObjectId
    Count: int
    Item: SuperelevationCurve
    Item: SuperelevationCurve
    def AddUserDefinedCurve(self, startSubEntity: AlignmentSubEntity, endSubEntity: AlignmentSubEntity) -> SuperelevationCurve: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    @staticmethod
    def ImportSuperelevationDataFromFile(fileName: str, alignmentId: ObjectId, acceptGarbage: bool) -> None: ...

class SuperelevationType:
    """.NET: Autodesk.Civil.DatabaseServices.SuperelevationType"""
    def __init__(self, *args) -> None: ...
    ...

class SuperelevationView(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.SuperelevationView"""
    def __init__(self, *args) -> None: ...
    StyleId: ObjectId
    Location: Point3d
    StationEnd: float
    StationStart: float
    RangeOption: GraphRangeOptions
    AlignmentId: ObjectId
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(document: CivilDocument, alignmentName: str, strNameTemplate: str, strDesc: str, useLayer: bool, strLayer: str, strBaseLayer: str, location: Point3d) -> ObjectId: ...
    def CreatePolyline(self, slopeLineDef: SlopeLineDefinition) -> ObjectId: ...
    def GetPolylineColor(self, slopeLineDef: SlopeLineDefinition) -> Color: ...
    def GetPolylineVisible(self, slopeLineDef: SlopeLineDefinition) -> bool: ...
    def GetStationAndCrossSlope(self, pt: Point3d, dStation: float, dCrossSlope: float) -> None: ...
    def SetPolylineColor(self, slopeLineDef: SlopeLineDefinition, color: Color) -> None: ...
    def SetPolylineVisible(self, slopeLineDef: SlopeLineDefinition, visible: bool) -> None: ...

class Surface(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.Surface"""
    def __init__(self, *args) -> None: ...
    OriginationType: SurfaceOriginationType
    IsLevelOfDetailEnabled: bool
    Masks: SurfaceMaskCollection
    AutoRebuild: bool
    Lock: bool
    StyleId: ObjectId
    IsSnapshotOutOfDate: bool
    HasSnapshot: bool
    IsOutOfDate: bool
    PartialReferenceBoundaryManager: SurfacePartialReferenceBoundaryMgr
    BuildOptions: SurfaceBuildOptions
    Operations: SurfaceOperationCollection
    BoundariesDefinition: SurfaceDefinitionBoundaries
    Analysis: SurfaceAnalysis
    IsVolumeSurface: bool
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CreateSnapshot(self, ) -> None: ...
    def ExportToDEM(self, fileName: str, coordinateSystemCode: str, gridSpacing: float, deteElevBy: ExportDetermineElevationType, useCustomNullElevationation: bool, customNullElevation: float) -> None: ...
    def FindDirectionAtXY(self, x: float, y: float) -> float: ...
    def FindElevationAtXY(self, x: float, y: float) -> float: ...
    def FindPointsAlongLine(self, lineSeg3d: LineSegment3d) -> Point3dCollection: ...
    def FindSlopeAtXY(self, x: float, y: float) -> float: ...
    def GetBoundedVolumes(self, polygon: Point3dCollection, datumElevation: float) -> SurfaceVolumeInfo: ...
    def GetGeneralProperties(self, ) -> GeneralSurfaceProperties: ...
    def GetIntersectionPoint(self, startPoint: Point3d, dir: Vector3d) -> Point3d: ...
    def Rebuild(self, ) -> None: ...
    def RebuildSnapshot(self, ) -> None: ...
    def RemoveSnapshot(self, ) -> None: ...

class SurfaceAnalysis:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceAnalysis"""
    def __init__(self, *args) -> None: ...
    def CreateWaterdrop(self, location: Point2d, objectType: WaterdropObjectType) -> ObjectIdCollection: ...
    def Dispose(self, ) -> None: ...
    def GetContourData(self, ) -> list: ...
    def GetDirectionData(self, ) -> list: ...
    def GetElevationData(self, ) -> list: ...
    def GetSlopeArrowData(self, ) -> list: ...
    def GetSlopeData(self, ) -> list: ...
    def GetUserDefinedContourData(self, ) -> list: ...
    def GetWatershedData(self, ) -> SurfaceAnalysisWatershedDataCollection: ...
    def SetContourData(self, analysisData: list) -> None: ...
    def SetDirectionData(self, analysisData: list) -> None: ...
    def SetElevationData(self, analysisData: list) -> None: ...
    def SetSlopeArrowData(self, analysisData: list) -> None: ...
    def SetSlopeData(self, analysisData: list) -> None: ...
    def SetUserDefinedContourData(self, analysisData: list) -> None: ...
    def SetWatershedData(self, analysisData: SurfaceAnalysisWatershedDataCollection) -> None: ...

class SurfaceAnalysisContourData:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceAnalysisContourData"""
    def __init__(self, *args) -> None: ...
    ContourValue: ContourValues
    MaximumElevation: float
    MinimumElevation: float
    def Initialize(self, codeValue: ColorValue) -> None: ...
    def Update(self, codeValue: ColorValue) -> None: ...

class SurfaceAnalysisDirectionData:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceAnalysisDirectionData"""
    def __init__(self, *args) -> None: ...
    Scheme: Color
    MaximumDirection: float
    MinimumDirection: float
    def Initialize(self, codeValue: ColorValue) -> None: ...
    def Update(self, A_0: ColorValue) -> None: ...

class SurfaceAnalysisElevationData:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceAnalysisElevationData"""
    def __init__(self, *args) -> None: ...
    Scheme: Color
    MaximumElevation: float
    MinimumElevation: float
    def Initialize(self, codeValue: ColorValue) -> None: ...
    def Update(self, A_0: ColorValue) -> None: ...

class SurfaceAnalysisSlopeArrowData:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceAnalysisSlopeArrowData"""
    def __init__(self, *args) -> None: ...
    Scheme: Color
    MaximumSlope: float
    MinimumSlope: float
    def Initialize(self, codeValue: ColorValue) -> None: ...
    def Update(self, A_0: ColorValue) -> None: ...

class SurfaceAnalysisSlopeData:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceAnalysisSlopeData"""
    def __init__(self, *args) -> None: ...
    Scheme: Color
    MaximumSlope: float
    MinimumSlope: float
    def Initialize(self, codeValue: ColorValue) -> None: ...
    def Update(self, A_0: ColorValue) -> None: ...

class SurfaceAnalysisUserDefinedContourData:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceAnalysisUserDefinedContourData"""
    def __init__(self, *args) -> None: ...
    LineWeight: LineWeight
    LineTypeId: ObjectId
    Color: Color
    Elevation: float
    Description: str
    def Initialize(self, codeValue: ColorValue) -> None: ...
    def Update(self, A_0: ColorValue) -> None: ...

class SurfaceAnalysisWatershedData:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceAnalysisWatershedData"""
    def __init__(self, *args) -> None: ...
    AreaColor: Color
    AreaHatchPatternName: str
    SegmentLineWeight: LineWeight
    SegmentLineTypeId: ObjectId
    SegmentColor: Color
    Description: str
    DrainsInto: list
    Visible: bool
    Type: WatershedType
    AreaID: int
    def Initialize(self, codeValue: ColorValue) -> None: ...
    def Update(self, A_0: ColorValue) -> None: ...

class SurfaceAnalysisWatershedDataCollection:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceAnalysisWatershedDataCollection"""
    def __init__(self, *args) -> None: ...
    ParentSurfaceId: ObjectId
    Count: int
    Item: SurfaceAnalysisWatershedData
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class SurfaceBoundary:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceBoundary"""
    def __init__(self, *args) -> None: ...
    BoundaryType: SurfaceBoundaryType
    Vertices: Point3dCollection

class SurfaceBreakline:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceBreakline"""
    def __init__(self, *args) -> None: ...
    Vertices: Point3dCollection
    BreaklineType: SurfaceBreaklineType
    Description: str
    def InsertIntoDrawing(self, ) -> ObjectId: ...

class SurfaceBuildOptions:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceBuildOptions"""
    def __init__(self, *args) -> None: ...
    CrossingBreaklinesElevationOption: CrossingBreaklinesElevationType
    NeedConvertBreaklines: bool
    MaximumTriangleLength: float
    UseMaximumTriangleLength: bool
    MaximumAngleBetweenAdjacentTinLines: float
    UseMaximumAngle: bool
    MaximumElevation: float
    ExecludeMaximumElevation: bool
    MinimumElevation: float
    ExecludeMinimumElevation: bool
    CopyDeletedDependentObjects: bool

class SurfaceContourLabelGroup(AutoFeatureLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceContourLabelGroup"""
    def __init__(self, *args) -> None: ...
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    LabelLinePoints: Point2dCollection
    UserContourLabelStyleId: ObjectId
    MinorContourLabelStyleId: ObjectId
    MajorContourLabelStyleId: ObjectId
    IsUserContourLabelVisible: bool
    IsMinorContourLabelVisible: bool
    IsMajorContourLabelVisible: bool
    IsLabelLineVisible: bool
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(surfaceId: ObjectId, labelLinePoints: Point2dCollection, majorContourlabelStyleId: ObjectId, minorContourlabelStyleId: ObjectId, userContourlabelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def CreateMultipleAtInterval(surfaceId: ObjectId, labelLineStartPoint: Point2d, labelLineEndPoint: Point2d, interval: float, options: SurfaceContourLabelGroupCreateOption) -> None: ...
    @staticmethod
    def GetAvailableLabelGroupIds(surfaceId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(surfaceId: ObjectId) -> ObjectIdCollection: ...
    def GetLabelLinePoint(self, index: int) -> Point2d: ...
    def SetLabelLinePoint(self, index: int, __unnamed001: Point2d) -> None: ...

class SurfaceContourLabelGroupCreateOption:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceContourLabelGroupCreateOption"""
    def __init__(self, *args) -> None: ...
    MaskType: LabelMaskType
    ShowUserDefinedContourlabelgroup: bool
    UserDefinedContourlabelStyleId: ObjectId
    ShowMinorContourlabelgroup: bool
    MinorContourlabelStyleId: ObjectId
    ShowMajorContourlabelgroup: bool
    MajorContourlabelStyleId: ObjectId
    ShowLabelLine: bool

class SurfaceDefinitionAddFigureSurveyQueries(SurfaceDefinitionBase):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceDefinitionAddFigureSurveyQueries"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: SurfaceOperationAddFigureSurveyQuery
    def AddFigureSurveyQuery(self, surveyProjectGuid: Guid, surveyQueryGuid: Guid, queryChecksum: int, surfaceOpDescription: str, midOrdinateDis: float) -> SurfaceOperationAddFigureSurveyQuery: ...

class SurfaceDefinitionAddPointSurveyQueries(SurfaceDefinitionBase):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceDefinitionAddPointSurveyQueries"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: SurfaceOperationAddPointSurveyQuery
    def AddPointSurveyQuery(self, surveyProjectGuid: Guid, surveyQueryGuid: Guid, queryChecksum: int, surfaceOpDescription: str, midOrdinateDis: float) -> SurfaceOperationAddPointSurveyQuery: ...

class SurfaceDefinitionBase:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceDefinitionBase`1"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: T
    def RemoveAt(self, index: int) -> None: ...

class SurfaceDefinitionBoundaries(SurfaceDefinitionBase):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceDefinitionBoundaries"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: SurfaceOperationAddBoundary
    def AddBoundaries(self, points: Point3dCollection, midOrdinateDistance: float, boundaryType: SurfaceBoundaryType, useNonDestructiveBreakline: bool) -> SurfaceOperationAddBoundary: ...

class SurfaceDefinitionBreaklines(SurfaceDefinitionBase):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceDefinitionBreaklines"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: SurfaceOperationAddBreakline
    def AddBreaklinesFromFile(self, filename: str) -> SurfaceOperationAddBreaklineFromFile: ...
    def AddNonDestructiveBreaklines(self, points: Point3dCollection, midOrdinateDistance: float) -> SurfaceOperationAddBreakline: ...
    def AddProximityBreaklines(self, points: Point3dCollection, midOrdinateDistance: float) -> SurfaceOperationAddBreakline: ...
    def AddStandardBreaklines(self, points: Point3dCollection, midOrdinateDistance: float, maximumDistance: float, weedingDistance: float, weedingAngle: float) -> SurfaceOperationAddBreakline: ...
    def AddWallBreaklines(self, creationData: list, midOrdinateDistance: float, maximumDistance: float, weedingDistance: float, weedingAngle: float) -> SurfaceOperationAddBreakline: ...
    def ImportBreaklinesFromFile(self, filename: str) -> list: ...

class SurfaceDefinitionContours(SurfaceDefinitionBase):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceDefinitionContours"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: SurfaceOperationAddContour
    def AddContours(self, points: Point3dCollection, midOrdinateDistance: float, maximumDistance: float, weedingDistance: float, weedingAngle: float, options: SurfaceMinimizeFlatAreaOptions) -> SurfaceOperationAddContour: ...

class SurfaceDefinitionDEMFiles(SurfaceDefinitionBase):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceDefinitionDEMFiles"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: SurfaceOperationAddDEMFile
    def AddDEMFile(self, filename: str, coordinateSystemCode: str, useCustomNullElevation: bool, customeNullElevation: float) -> SurfaceOperationAddDEMFile: ...

class SurfaceDefinitionDrawingObjects(SurfaceDefinitionBase):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceDefinitionDrawingObjects"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: SurfaceOperationAddDrawingObject
    def AddFrom3DFaces(self, points: Point3dCollection, edges: IEnumerable, description: str) -> SurfaceOperationAdd3DFaces: ...
    def AddFromBlocks(self, blockIds: ObjectIdCollection, description: str) -> SurfaceOperationAddDrawingObject: ...
    def AddFromLines(self, lineIds: ObjectIdCollection, needMaintainEdge: bool, description: str) -> SurfaceOperationAddDrawingObject: ...
    def AddFromPoints(self, pointIds: ObjectIdCollection, description: str) -> SurfaceOperationAddDrawingObject: ...
    def AddFromPolyFaces(self, polyfaceIds: ObjectIdCollection, needMaintainEdge: bool, description: str) -> SurfaceOperationAddDrawingObject: ...
    def AddFromTexts(self, textIds: ObjectIdCollection, description: str) -> SurfaceOperationAddDrawingObject: ...

class SurfaceDefinitionPointFiles(SurfaceDefinitionBase):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceDefinitionPointFiles"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: SurfaceOperationAddPointFile
    def AddPointFile(self, pointFilename: str, pointFileFormat: PointFileFormat, useAdjustedElevation: bool, shouldTransformPointCoordinate: bool, shouldExpandCoordinateData: bool) -> SurfaceOperationAddPointFile: ...

class SurfaceDefinitionPointGroups(SurfaceDefinitionBase):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceDefinitionPointGroups"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: SurfaceOperationAddPointGroup
    def AddPointGroup(self, pointGroupId: ObjectId) -> SurfaceOperationAddPointGroup: ...

class SurfaceElevationLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceElevationLabel"""
    def __init__(self, *args) -> None: ...
    Location: Point2d
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(surfaceId: ObjectId, location: Point2d, labelStyleId: ObjectId, markerStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableSurfaceElevationLabelIds(surfaceId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableSurfaceElevationLabels(surfaceId: ObjectId) -> ObjectIdCollection: ...

class SurfaceMask:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceMask"""
    def __init__(self, *args) -> None: ...
    IsRenderOnly: bool
    Type: SurfaceMaskType
    Linkages: ObjectIdCollection
    MaterialId: ObjectId
    MidOrdinateDistance: float
    SurfaceId: ObjectId
    Description: str
    Name: str
    ObjectId: ObjectId
    def Dispose(self, ) -> None: ...

class SurfaceMaskCollection:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceMaskCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: SurfaceMask
    Item: SurfaceMask
    def Add(self, creationData: SurfaceMaskCreationData) -> SurfaceMask: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, mask: SurfaceMask) -> int: ...
    def MoveDown(self, mask: SurfaceMask) -> None: ...
    def MoveUp(self, mask: SurfaceMask) -> None: ...
    def Remove(self, mask: SurfaceMask) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    def Swap(self, mask1: SurfaceMask, mask2: SurfaceMask) -> None: ...

class SurfaceMaskCreationData:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceMaskCreationData"""
    def __init__(self, *args) -> None: ...
    SurfaceId: ObjectId
    IsRenderOnly: bool
    Type: SurfaceMaskType
    Linkages: ObjectIdCollection
    MaterialId: ObjectId
    MidOrdinateDistance: float
    Description: str
    Name: str

class SurfaceMaskType:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceMaskType"""
    def __init__(self, *args) -> None: ...
    ...

class SurfaceMinimizeFlatAreaOptions:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceMinimizeFlatAreaOptions"""
    def __init__(self, *args) -> None: ...
    AddPointsToEdges: bool
    AddPointsToTriangles: bool
    SwapEdges: bool
    FillGaps: bool

class SurfaceOperation:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperation"""
    def __init__(self, *args) -> None: ...
    Guid: Guid
    Enabled: bool
    def Dispose(self, ) -> None: ...
    def MoveDown(self, ) -> None: ...
    def MoveToBottom(self, ) -> None: ...
    def MoveToTop(self, ) -> None: ...
    def MoveUp(self, ) -> None: ...

class SurfaceOperationAdd3DFaces(SurfaceOperationAddDrawingObject):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAdd3DFaces"""
    def __init__(self, *args) -> None: ...
    MaintainEdge: bool
    ObjectType: SurfaceDrawObjectType
    Description: str
    Guid: Guid
    Enabled: bool

class SurfaceOperationAddBoundary(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAddBoundary"""
    def __init__(self, *args) -> None: ...
    MidOrdinateDistance: float
    IsTrimmed: bool
    BoundaryType: SurfaceBoundaryType
    Name: str
    Count: int
    Item: SurfaceBoundary
    Guid: Guid
    Enabled: bool
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def InsertIntoDrawing(self, ) -> ObjectIdCollection: ...

class SurfaceOperationAddBreakline(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAddBreakline"""
    def __init__(self, *args) -> None: ...
    WeedingAngle: float
    WeedingDistance: float
    MaximumDistance: float
    MidOrdinateDistance: float
    BreaklineType: SurfaceBreaklineType
    Count: int
    Description: str
    Item: SurfaceBreakline
    Guid: Guid
    Enabled: bool
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def InsertIntoDrawing(self, ) -> ObjectIdCollection: ...

class SurfaceOperationAddBreaklineFromFile(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAddBreaklineFromFile"""
    def __init__(self, *args) -> None: ...
    BreaklineFileName: str
    Description: str
    Guid: Guid
    Enabled: bool

class SurfaceOperationAddContour(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAddContour"""
    def __init__(self, *args) -> None: ...
    WeedingAngle: float
    WeedingDistance: float
    MaximumDistance: float
    MidOrdinateDistance: float
    Summary: str
    Description: str
    Guid: Guid
    Enabled: bool
    def InsertIntoDrawing(self, ) -> ObjectIdCollection: ...

class SurfaceOperationAddDEMFile(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAddDEMFile"""
    def __init__(self, *args) -> None: ...
    CustomeNullElevation: float
    UseCustomNullElevation: bool
    CoordinateSystemCode: str
    FileSize: float
    DEMFileName: str
    Guid: Guid
    Enabled: bool

class SurfaceOperationAddDrawingObject(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAddDrawingObject"""
    def __init__(self, *args) -> None: ...
    MaintainEdge: bool
    ObjectType: SurfaceDrawObjectType
    Description: str
    Guid: Guid
    Enabled: bool

class SurfaceOperationAddFigureSurveyQuery(SurfaceOperationAddSurveyQuery):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAddFigureSurveyQuery"""
    def __init__(self, *args) -> None: ...
    SurveyQueryType: SurfaceSurveyQueryType
    Description: str
    QueryName: str
    QueryGuid: Guid
    ProjectName: str
    ProjectGuid: Guid
    Guid: Guid
    Enabled: bool

class SurfaceOperationAddGridPoint(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAddGridPoint"""
    def __init__(self, *args) -> None: ...
    Elevation: float
    Location: GridLocation
    Guid: Guid
    Enabled: bool

class SurfaceOperationAddImxFile(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAddImxFile"""
    def __init__(self, *args) -> None: ...
    FileSize: float
    DoCoordinateConversion: bool
    GitHash: str
    Query: str
    SurfaceName: str
    ImxFileName: str
    Guid: Guid
    Enabled: bool

class SurfaceOperationAddLine(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAddLine"""
    def __init__(self, *args) -> None: ...
    EndLocation: Point2d
    StartLocation: Point2d
    Guid: Guid
    Enabled: bool

class SurfaceOperationAddPointFile(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAddPointFile"""
    def __init__(self, *args) -> None: ...
    ShouldExpandCoordinateData: bool
    ShouldTransformPointCoordinates: bool
    UseAdjustedElevation: bool
    PointFileName: str
    FileFormat: PointFileFormat
    Guid: Guid
    Enabled: bool

class SurfaceOperationAddPointGroup(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAddPointGroup"""
    def __init__(self, *args) -> None: ...
    PointGroupId: ObjectId
    Guid: Guid
    Enabled: bool

class SurfaceOperationAddPointSurveyQuery(SurfaceOperationAddSurveyQuery):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAddPointSurveyQuery"""
    def __init__(self, *args) -> None: ...
    SurveyQueryType: SurfaceSurveyQueryType
    Description: str
    QueryName: str
    QueryGuid: Guid
    ProjectName: str
    ProjectGuid: Guid
    Guid: Guid
    Enabled: bool

class SurfaceOperationAddSurveyQuery(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAddSurveyQuery"""
    def __init__(self, *args) -> None: ...
    SurveyQueryType: SurfaceSurveyQueryType
    Description: str
    QueryName: str
    QueryGuid: Guid
    ProjectName: str
    ProjectGuid: Guid
    Guid: Guid
    Enabled: bool

class SurfaceOperationAddTinFile(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAddTinFile"""
    def __init__(self, *args) -> None: ...
    FileSize: float
    TinFileName: str
    Guid: Guid
    Enabled: bool

class SurfaceOperationAddTinMultipleVertices(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAddTinMultipleVertices"""
    def __init__(self, *args) -> None: ...
    Locations: Point3dCollection
    Guid: Guid
    Enabled: bool

class SurfaceOperationAddTinVertex(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAddTinVertex"""
    def __init__(self, *args) -> None: ...
    Location: Point3d
    Guid: Guid
    Enabled: bool

class SurfaceOperationAddXmlFile(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationAddXmlFile"""
    def __init__(self, *args) -> None: ...
    XmlFileName: str
    Guid: Guid
    Enabled: bool

class SurfaceOperationCollection:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: SurfaceOperation
    Item: SurfaceOperation
    def DisableOperations(self, operationClassType: Type) -> None: ...
    def EnableOperations(self, operationClassType: Type) -> None: ...
    def GetOperationStatus(self, operationClassType: Type) -> SurfaceOpeartionStatusType: ...
    def Remove(self, operationGuid: Guid) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    def Swap(self, firstOperation: SurfaceOperation, secondOperation: SurfaceOperation) -> None: ...
    def SwapAt(self, firstIndex: int, secondIndex: int) -> None: ...

class SurfaceOperationCreateByCropping(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationCreateByCropping"""
    def __init__(self, *args) -> None: ...
    CroppedBoundary: Point3dCollection
    SourceFileName: str
    Guid: Guid
    Enabled: bool

class SurfaceOperationCreatedFromCorridor(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationCreatedFromCorridor"""
    def __init__(self, *args) -> None: ...
    CorridorSurfaceName: str
    CorridorId: ObjectId
    Guid: Guid
    Enabled: bool

class SurfaceOperationDeleteGridPoint(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationDeleteGridPoint"""
    def __init__(self, *args) -> None: ...
    Location: GridLocation
    Guid: Guid
    Enabled: bool

class SurfaceOperationDeleteLine(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationDeleteLine"""
    def __init__(self, *args) -> None: ...
    MidLocation: Point2d
    Guid: Guid
    Enabled: bool

class SurfaceOperationDeleteMultipleGridPoints(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationDeleteMultipleGridPoints"""
    def __init__(self, *args) -> None: ...
    Locations: list
    Guid: Guid
    Enabled: bool

class SurfaceOperationDeleteMultipleLines(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationDeleteMultipleLines"""
    def __init__(self, *args) -> None: ...
    MidLocations: Point2dCollection
    Guid: Guid
    Enabled: bool

class SurfaceOperationDeleteMultipleTinVertices(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationDeleteMultipleTinVertices"""
    def __init__(self, *args) -> None: ...
    Locations: Point2dCollection
    Guid: Guid
    Enabled: bool

class SurfaceOperationDeleteTinVertex(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationDeleteTinVertex"""
    def __init__(self, *args) -> None: ...
    Location: Point2d
    Guid: Guid
    Enabled: bool

class SurfaceOperationMinimizeFlatAreas(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationMinimizeFlatAreas"""
    def __init__(self, *args) -> None: ...
    CountOfRemovedPoints: int
    CountOfAddedPoints: int
    MinimizeFlatAreaOptions: SurfaceMinimizeFlatAreaOptions
    Guid: Guid
    Enabled: bool

class SurfaceOperationModifyGridPointElevation(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationModifyGridPointElevation"""
    def __init__(self, *args) -> None: ...
    NewElevation: float
    Location: GridLocation
    Guid: Guid
    Enabled: bool

class SurfaceOperationModifyMultipleGridPointsElevation(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationModifyMultipleGridPointsElevation"""
    def __init__(self, *args) -> None: ...
    IsDeltaElevation: bool
    Elevation: float
    Locations: list
    Guid: Guid
    Enabled: bool

class SurfaceOperationModifyMultipleTinVerticesElevation(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationModifyMultipleTinVerticesElevation"""
    def __init__(self, *args) -> None: ...
    IsDeltaElevation: bool
    Elevation: float
    Locations: Point2dCollection
    Guid: Guid
    Enabled: bool

class SurfaceOperationModifyTinVertexElevation(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationModifyTinVertexElevation"""
    def __init__(self, *args) -> None: ...
    NewElevation: float
    Location: Point2d
    Guid: Guid
    Enabled: bool

class SurfaceOperationMoveTinVertex(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationMoveTinVertex"""
    def __init__(self, *args) -> None: ...
    NewLocation: Point2d
    OriginalLocation: Point2d
    Guid: Guid
    Enabled: bool

class SurfaceOperationPasteSurface(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationPasteSurface"""
    def __init__(self, *args) -> None: ...
    SurfaceId: ObjectId
    Guid: Guid
    Enabled: bool

class SurfaceOperationRaise(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationRaise"""
    def __init__(self, *args) -> None: ...
    DeltaElevation: float
    Guid: Guid
    Enabled: bool

class SurfaceOperationSimplify(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationSimplify"""
    def __init__(self, *args) -> None: ...
    CountOfRemovedPoints: int
    SimplifyOptions: SurfaceSimplifyOptions
    Guid: Guid
    Enabled: bool

class SurfaceOperationSmooth(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationSmooth"""
    def __init__(self, *args) -> None: ...
    OutPutPoints: Point3dCollection
    SurfaceSmoothMethod: SurfaceSmoothType
    Guid: Guid
    Enabled: bool

class SurfaceOperationSwapEdge(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationSwapEdge"""
    def __init__(self, *args) -> None: ...
    MidLocation: Point2d
    Guid: Guid
    Enabled: bool

class SurfaceOperationTransformBy(SurfaceOperation):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOperationTransformBy"""
    def __init__(self, *args) -> None: ...
    TransformMatrix: Matrix3d
    TransformType: SurfaceTransformOperationType
    Guid: Guid
    Enabled: bool

class SurfaceOriginationType:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceOriginationType"""
    def __init__(self, *args) -> None: ...
    ...

class SurfacePartialReferenceBoundaryMgr:
    """.NET: Autodesk.Civil.DatabaseServices.SurfacePartialReferenceBoundaryMgr"""
    def __init__(self, *args) -> None: ...
    def AddBoundary(self, refBoundaryId: ObjectId) -> None: ...
    def DeleteBoundary(self, refBoundaryId: ObjectId) -> None: ...
    def ReferenceBoundaryIds(self, ) -> ObjectIdCollection: ...

class SurfacePointOutputOptions:
    """.NET: Autodesk.Civil.DatabaseServices.SurfacePointOutputOptions"""
    def __init__(self, *args) -> None: ...
    RandomPointsNumber: int
    GridOrientation: float
    GridSpacingY: float
    GridSpacingX: float
    Edges: IEnumerable
    OutputRegions: IEnumerable
    OutputLocations: SurfacePointOutputLocationsType

class SurfaceSimplifyOptions:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceSimplifyOptions"""
    def __init__(self, *args) -> None: ...
    MaximumChangeInElevation: float
    UseMaximumChangeInElevation: bool
    PercentageToRemove: float
    UsePercentageToRemove: bool
    UserSpecifiedPolygonRegion: Point3dCollection
    RegionOption: SurfaceSimplifyRegionType
    SimplifyMethod: SurfaceSimplifyType
    def Equals(self, right: object) -> bool: ...
    def SetSurfaceBorderAsRegion(self, ) -> None: ...
    def SetUserSpecifiedPolygonRegionByEntityId(self, entityId: ObjectId, midOrdinate: float) -> None: ...

class SurfaceSimplifyRegionType:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceSimplifyRegionType"""
    def __init__(self, *args) -> None: ...
    ...

class SurfaceSlopeLabel(FeatureLabel):
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceSlopeLabel"""
    def __init__(self, *args) -> None: ...
    Location2: Point2d
    Location: Point2d
    SlopeLabelType: SurfaceSlopeLabelType
    StyleName: str
    StyleId: ObjectId
    AnchorMarkerRotationAngle: float
    RotationAngle: float
    CanRotate: bool
    Reversed: bool
    Pinned: bool
    LeaderVisibility: LeaderVisibilityType
    LeaderTailVisibility: LeaderTailVisibilityType
    LeaderAttachment: LeaderAttachmentBehaviorType
    Flipped: bool
    LabelLocation: Point3d
    DraggedOffset: Vector3d
    DimensionAnchorValue: float
    DimensionAnchorOption: DimensionAnchorOptionType
    AnchorMarkerStyleId: ObjectId
    Dragged: bool
    DimensionAnchorInfo: AnchorInfo
    AnchorInfo: AnchorInfo
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(surfaceId: ObjectId, point1: Point2d, point2: Point2d, labelStyleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetAvailableSurfaceSlopeLabelIds(surfaceId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableSurfaceSlopeLabels(surfaceId: ObjectId) -> ObjectIdCollection: ...

class SurfaceSlopeLabelType:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceSlopeLabelType"""
    def __init__(self, *args) -> None: ...
    ...

class SurfaceTransformOperationType:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceTransformOperationType"""
    def __init__(self, *args) -> None: ...
    ...

class SurfaceVolumeInfo:
    """.NET: Autodesk.Civil.DatabaseServices.SurfaceVolumeInfo"""
    def __init__(self, *args) -> None: ...
    Net: float
    Fill: float
    Cut: float

class SurveyFigure(FeatureLine):
    """.NET: Autodesk.Civil.DatabaseServices.SurveyFigure"""
    def __init__(self, *args) -> None: ...
    CurvesCount: int
    ElevationPointsCount: int
    PIPointsCount: int
    PointsCount: int
    RelativeSurfaceId: ObjectId
    Length3D: float
    Length2D: float
    MaxGrade: float
    MinGrade: float
    MaxElevation: float
    MinElevation: float
    SiteId: ObjectId
    StyleName: str
    StyleId: ObjectId
    IsEditable: bool
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SurveyNetworkEntity(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.SurveyNetworkEntity"""
    def __init__(self, *args) -> None: ...
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SweptShapeType:
    """.NET: Autodesk.Civil.DatabaseServices.SweptShapeType"""
    def __init__(self, *args) -> None: ...
    ...

class TR55FlowSegmentType:
    """.NET: Autodesk.Civil.DatabaseServices.TR55FlowSegmentType"""
    def __init__(self, *args) -> None: ...
    ...

class Table(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.Table"""
    def __init__(self, *args) -> None: ...
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class TerrainSurfaceProperties:
    """.NET: Autodesk.Civil.DatabaseServices.TerrainSurfaceProperties"""
    def __init__(self, *args) -> None: ...
    MeanGradeOrSlope: float
    MaximumGradeOrSlope: float
    MinimumGradeOrSlope: float
    SurfaceArea3D: float
    SurfaceArea2D: float

class TimeOfConcentrationCalculationMethod:
    """.NET: Autodesk.Civil.DatabaseServices.TimeOfConcentrationCalculationMethod"""
    def __init__(self, *args) -> None: ...
    ...

class TinSurface(Surface):
    """.NET: Autodesk.Civil.DatabaseServices.TinSurface"""
    def __init__(self, *args) -> None: ...
    SurveyQueriesAddPointDefinition: SurfaceDefinitionAddPointSurveyQueries
    SurveyQueriesAddFigureDefinition: SurfaceDefinitionAddFigureSurveyQueries
    PointFilesDefinition: SurfaceDefinitionPointFiles
    PointGroupsDefinition: SurfaceDefinitionPointGroups
    DrawingObjectsDefinition: SurfaceDefinitionDrawingObjects
    Triangles: TinSurfaceTriangleCollection
    Vertices: TinSurfaceVertexCollection
    DEMFilesDefinition: SurfaceDefinitionDEMFiles
    ContoursDefinition: SurfaceDefinitionContours
    BreaklinesDefinition: SurfaceDefinitionBreaklines
    OriginationType: SurfaceOriginationType
    IsLevelOfDetailEnabled: bool
    Masks: SurfaceMaskCollection
    AutoRebuild: bool
    Lock: bool
    StyleId: ObjectId
    IsSnapshotOutOfDate: bool
    HasSnapshot: bool
    IsOutOfDate: bool
    PartialReferenceBoundaryManager: SurfacePartialReferenceBoundaryMgr
    BuildOptions: SurfaceBuildOptions
    Operations: SurfaceOperationCollection
    BoundariesDefinition: SurfaceDefinitionBoundaries
    Analysis: SurfaceAnalysis
    IsVolumeSurface: bool
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddLine(self, vertex1: TinSurfaceVertex, vertex2: TinSurfaceVertex) -> SurfaceOperationAddLine: ...
    def AddVertex(self, location: Point2d) -> SurfaceOperationAddTinVertex: ...
    def AddVertices(self, locations: Point2dCollection) -> SurfaceOperationAddTinMultipleVertices: ...
    @staticmethod
    def Create(surfaceName: str, styleId: ObjectId) -> ObjectId: ...
    @staticmethod
    def CreateByCropping(destDatabase: Database, surfaceName: str, srcSurfaceId: ObjectId, objects: ObjectIdCollection, location: Point2d) -> ObjectId: ...
    @staticmethod
    def CreateFromCorridorSurface(surfaceName: str, corridorSurface: CorridorSurface) -> ObjectId: ...
    @staticmethod
    def CreateFromIMX(database: Database, styleId: ObjectId, imxFileName: str, surfaceName: str, gitHash: str, query: str, doCoordSysConversion: bool) -> ObjectId: ...
    @staticmethod
    def CreateFromLandXML(database: Database, newSurfaceName: str, landXMLfileName: str, landXMLSurfaceName: str) -> ObjectId: ...
    @staticmethod
    def CreateFromTin(database: Database, tinFileName: str) -> ObjectId: ...
    def CreateSolidsAtDepth(self, depth: float, layer: str, penIndex: int) -> ObjectIdCollection: ...
    def CreateSolidsAtDepthToFile(self, depth: float, layer: str, penIndex: int, fileName: str) -> ObjectIdCollection: ...
    def CreateSolidsAtFixedElevation(self, elevation: float, layer: str, penIndex: int) -> ObjectIdCollection: ...
    def CreateSolidsAtFixedElevationToFile(self, elevation: float, layer: str, penIndex: int, fileName: str) -> ObjectIdCollection: ...
    def CreateSolidsAtSurface(self, bottomSurfaceId: ObjectId, layer: str, penIndex: int) -> ObjectIdCollection: ...
    def CreateSolidsAtSurfaceToFile(self, bottomSurfaceId: ObjectId, layer: str, penIndex: int, fileName: str) -> ObjectIdCollection: ...
    def DeleteLine(self, tinTriangleEdge: TinSurfaceEdge) -> SurfaceOperationDeleteLine: ...
    def DeleteLines(self, tinTriangleEdges: IEnumerable) -> SurfaceOperationDeleteMultipleLines: ...
    def DeleteVertex(self, vertex: TinSurfaceVertex) -> SurfaceOperationDeleteTinVertex: ...
    def DeleteVertices(self, vertices: IEnumerable) -> SurfaceOperationDeleteMultipleTinVertices: ...
    def ExtractBorder(self, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection: ...
    def ExtractContours(self, lowElev: float, highElev: float, interval: float, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection: ...
    def ExtractContoursAt(self, elevation: float, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection: ...
    def ExtractGridded(self, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection: ...
    def ExtractMajorContours(self, settingsType: SurfaceExtractionSettingsType, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection: ...
    def ExtractMinorContours(self, settingsType: SurfaceExtractionSettingsType, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection: ...
    def ExtractWatershed(self, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection: ...
    def FindEdgeAtXY(self, x: float, y: float) -> TinSurfaceEdge: ...
    def FindTriangleAtXY(self, x: float, y: float) -> TinSurfaceTriangle: ...
    def FindVertexAtXY(self, x: float, y: float) -> TinSurfaceVertex: ...
    def GetTerrainProperties(self, ) -> TerrainSurfaceProperties: ...
    def GetTinProperties(self, ) -> TinSurfaceProperties: ...
    def GetTriangles(self, includeInvisible: bool) -> TinSurfaceTriangleCollection: ...
    def GetVerticesInsideBorder(self, border: Point3dCollection) -> list: ...
    def GetVerticesInsideBorderRandom(self, border: Point3dCollection, randomNumber: int) -> list: ...
    def GetVerticesInsidePolylines(self, polylineIds: ObjectIdCollection) -> list: ...
    def GetVerticesInsidePolylinesRandom(self, polylineIds: ObjectIdCollection, randomNumber: int) -> list: ...
    def IdentifyFeatureTypeAtXY(self, x: float, y: float) -> Type: ...
    def MinimizeFlatAreas(self, minimizeOptions: SurfaceMinimizeFlatAreaOptions) -> SurfaceOperationMinimizeFlatAreas: ...
    def MoveVertex(self, vertex: TinSurfaceVertex, newLocation: Point2d) -> SurfaceOperationMoveTinVertex: ...
    def PasteSurface(self, surfaceId: ObjectId) -> SurfaceOperationPasteSurface: ...
    def RaiseSurface(self, deltaElevation: float) -> SurfaceOperationRaise: ...
    def RaiseVertices(self, vertices: IEnumerable, deltaElevation: float) -> SurfaceOperationModifyMultipleTinVerticesElevation: ...
    def SampleElevations(self, pt1: Point3d, pt2: Point3d) -> Point3dCollection: ...
    def SetVertexElevation(self, vertex: TinSurfaceVertex, newElevation: float) -> SurfaceOperationModifyTinVertexElevation: ...
    def SetVerticesElevation(self, vertices: IEnumerable, newElevation: float) -> SurfaceOperationModifyMultipleTinVerticesElevation: ...
    def SimplifySurface(self, simplifyOptions: SurfaceSimplifyOptions) -> SurfaceOperationSimplify: ...
    def SmoothSurfaceByKriging(self, krigingOptions: KrigingMethodOptions, pointOutputOptions: SurfacePointOutputOptions) -> SurfaceOperationSmooth: ...
    def SmoothSurfaceByNNI(self, pointOutputOptions: SurfacePointOutputOptions) -> SurfaceOperationSmooth: ...
    def SwapEdge(self, tinTriangleEdge: TinSurfaceEdge) -> SurfaceOperationSwapEdge: ...

class TinSurfaceEdge(TinSurfaceObject):
    """.NET: Autodesk.Civil.DatabaseServices.TinSurfaceEdge"""
    def __init__(self, *args) -> None: ...
    IsLocked: bool
    Triangle2: TinSurfaceTriangle
    Triangle1: TinSurfaceTriangle
    Vertex2: TinSurfaceVertex
    Vertex1: TinSurfaceVertex
    IsValid: bool
    Surface: TinSurface
    def Equals(self, rhs: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class TinSurfaceEdgeCollection:
    """.NET: Autodesk.Civil.DatabaseServices.TinSurfaceEdgeCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class TinSurfaceEdgeEnumerator:
    """.NET: Autodesk.Civil.DatabaseServices.TinSurfaceEdgeEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: TinSurfaceEdge
    CurrentObject: object
    def Dispose(self, ) -> None: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class TinSurfaceObject:
    """.NET: Autodesk.Civil.DatabaseServices.TinSurfaceObject"""
    def __init__(self, *args) -> None: ...
    Surface: TinSurface
    IsValid: bool
    def Dispose(self, ) -> None: ...
    def Equals(self, rhs: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class TinSurfaceProperties:
    """.NET: Autodesk.Civil.DatabaseServices.TinSurfaceProperties"""
    def __init__(self, *args) -> None: ...
    MinimumTriangleLength: float
    MaximumTriangleLength: float
    MinimumTriangleArea: float
    MaximumTriangleArea: float
    NumberOfTriangles: int

class TinSurfaceTriangle(TinSurfaceObject):
    """.NET: Autodesk.Civil.DatabaseServices.TinSurfaceTriangle"""
    def __init__(self, *args) -> None: ...
    IsVisible: bool
    Edge3: TinSurfaceEdge
    Edge2: TinSurfaceEdge
    Edge1: TinSurfaceEdge
    Vertex3: TinSurfaceVertex
    Vertex2: TinSurfaceVertex
    Vertex1: TinSurfaceVertex
    Surface: TinSurface
    IsValid: bool

class TinSurfaceTriangleCollection:
    """.NET: Autodesk.Civil.DatabaseServices.TinSurfaceTriangleCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class TinSurfaceTriangleEnumerator:
    """.NET: Autodesk.Civil.DatabaseServices.TinSurfaceTriangleEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: TinSurfaceTriangle
    CurrentObject: object
    def Dispose(self, ) -> None: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class TinSurfaceVertex(TinSurfaceObject):
    """.NET: Autodesk.Civil.DatabaseServices.TinSurfaceVertex"""
    def __init__(self, *args) -> None: ...
    Edges: TinSurfaceEdgeCollection
    Triangles: TinSurfaceTriangleCollection
    Vertices: TinSurfaceVertexCollection
    Location: Point3d
    Surface: TinSurface
    IsValid: bool

class TinSurfaceVertexCollection:
    """.NET: Autodesk.Civil.DatabaseServices.TinSurfaceVertexCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class TinSurfaceVertexEnumerator:
    """.NET: Autodesk.Civil.DatabaseServices.TinSurfaceVertexEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: TinSurfaceVertex
    CurrentObject: object
    def Dispose(self, ) -> None: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class TinVolumeSurface(Surface):
    """.NET: Autodesk.Civil.DatabaseServices.TinVolumeSurface"""
    def __init__(self, *args) -> None: ...
    FillFactor: float
    CutFactor: float
    OriginationType: SurfaceOriginationType
    IsLevelOfDetailEnabled: bool
    Masks: SurfaceMaskCollection
    AutoRebuild: bool
    Lock: bool
    StyleId: ObjectId
    IsSnapshotOutOfDate: bool
    HasSnapshot: bool
    IsOutOfDate: bool
    PartialReferenceBoundaryManager: SurfacePartialReferenceBoundaryMgr
    BuildOptions: SurfaceBuildOptions
    Operations: SurfaceOperationCollection
    BoundariesDefinition: SurfaceDefinitionBoundaries
    Analysis: SurfaceAnalysis
    IsVolumeSurface: bool
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(surfaceName: str, baseSurfaceId: ObjectId, comparisonSurfaceId: ObjectId, styleId: ObjectId) -> ObjectId: ...
    def GetTinProperties(self, ) -> TinSurfaceProperties: ...
    def GetVolumeProperties(self, ) -> VolumeSurfaceProperties: ...

class TrackDistanceCalculationMode:
    """.NET: Autodesk.Civil.DatabaseServices.TrackDistanceCalculationMode"""
    def __init__(self, *args) -> None: ...
    ...

class TransitionDescriptionBase(CivilWrapper<AeccDbAlignment>):
    """.NET: Autodesk.Civil.DatabaseServices.TransitionDescriptionBase"""
    def __init__(self, *args) -> None: ...
    StartStation: float
    Length: float
    EndStation: float

class TreeNodeCollectionBase(TreeOidWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.TreeNodeCollectionBase"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ObjectId
    Item: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...
    def Contains(self, name: str) -> bool: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, name: str) -> None: ...
    def ToObjectIds(self, ) -> ObjectIdCollection: ...

class Turnout(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.Turnout"""
    def __init__(self, *args) -> None: ...
    MainProfileId: ObjectId
    MainAlignmentId: ObjectId
    AutomaticUpdate: bool
    TurnoutOwnSide: TurnoutSideType
    TurnoutSide: TurnoutSideType
    TurnoutDirection: TurnoutDirectionType
    TurnoutModelName: str
    TurnoutTypeName: str
    CatalogName: str
    CatalogId: ObjectId
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(turnoutName: str, creationParams: TurnoutCreationParams) -> ObjectId: ...
    @staticmethod
    def GetAllTurnoutIds(database: Database) -> ObjectIdCollection: ...
    @staticmethod
    def GetAllTurnoutIdsOnAlignment(alignmentId: ObjectId) -> ObjectIdCollection: ...
    def GetCriticalPointLocation(self, entryName: str, criticalPointName: str) -> Point2d: ...
    def GetCriticalPointStation(self, entryName: str, criticalPointName: str) -> float: ...
    def GetCriticalPointType(self, entryName: str, criticalPointName: str) -> TurnoutCriticalPointType: ...
    def GetCriticalPoints(self, entryName: str) -> IList: ...
    def GetCustomParameterValue(self, name: str) -> object: ...
    def GetCustomParameters(self, ) -> list: ...
    def GetDivertedAlignmentId(self, entryName: str) -> ObjectId: ...
    def GetDivertedProfileId(self, entryName: str) -> ObjectId: ...
    def IsCriticalPointStationEditable(self, entryName: str, criticalPointName: str) -> bool: ...
    def SetCriticalPointStation(self, entryName: str, criticalPointName: str, station: float) -> None: ...
    def SetCustomParameterValue(self, name: str, value: object) -> None: ...

class TurnoutCatalog(Entity):
    """.NET: Autodesk.Civil.DatabaseServices.TurnoutCatalog"""
    def __init__(self, *args) -> None: ...
    Name: str
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class TurnoutCatalogManager:
    """.NET: Autodesk.Civil.DatabaseServices.TurnoutCatalogManager"""
    def __init__(self, *args) -> None: ...
    def AddCatalog(self, path: str) -> ObjectId: ...
    def GetAllCatalogIds(self, ) -> ObjectIdCollection: ...
    def GetCatalogByName(self, name: str) -> ObjectId: ...
    @staticmethod
    def GetTurnoutCatalogManager(db: Database) -> TurnoutCatalogManager: ...
    def RemoveAllUnusedCatalogs(self, ) -> None: ...
    def RemoveCatalog(self, catalogId: ObjectId) -> bool: ...
    def RemoveCatalogByName(self, name: str) -> bool: ...
    def UpdateCatalog(self, catalogId: ObjectId, path: str) -> bool: ...

class TurnoutCreationParams:
    """.NET: Autodesk.Civil.DatabaseServices.TurnoutCreationParams"""
    def __init__(self, *args) -> None: ...
    IsCreateDivertedProfiles: bool
    ReferenceStation: float
    InsertionPoint: str
    InsertionPointEntry: str
    TurnoutSide: TurnoutSideType
    TurnoutDirection: TurnoutDirectionType
    CustomParameterValues: Dictionary
    TurnoutModelName: str
    TurnoutTypeName: str
    CatalogId: ObjectId
    MainProfileId: ObjectId
    MainAlignmentId: ObjectId
    def AddMergedAlignment(self, entry: str, alignmentId: ObjectId) -> None: ...
    def AddMergedProfile(self, entry: str, profileId: ObjectId) -> None: ...
    def ClearMergedAlignment(self, ) -> None: ...
    def ClearMergedProfile(self, ) -> None: ...
    def CreateDivertedAlignment(self, entry: str) -> bool: ...
    def CreateDivertedProfile(self, entry: str) -> bool: ...

class TurnoutCriticalPointType:
    """.NET: Autodesk.Civil.DatabaseServices.TurnoutCriticalPointType"""
    def __init__(self, *args) -> None: ...
    ...

class TurnoutDirectionType:
    """.NET: Autodesk.Civil.DatabaseServices.TurnoutDirectionType"""
    def __init__(self, *args) -> None: ...
    ...

class TurnoutSideType:
    """.NET: Autodesk.Civil.DatabaseServices.TurnoutSideType"""
    def __init__(self, *args) -> None: ...
    ...

class UDP:
    """.NET: Autodesk.Civil.DatabaseServices.UDP"""
    def __init__(self, *args) -> None: ...
    IsInUsed: bool
    UseDefaultValue: bool
    DefaultValue: object
    Description: str
    ClassificationName: str
    Guid: Guid
    Name: str

class UDPBoolean(UDP):
    """.NET: Autodesk.Civil.DatabaseServices.UDPBoolean"""
    def __init__(self, *args) -> None: ...
    DefaultValue: bool
    IsInUsed: bool
    UseDefaultValue: bool
    DefaultValue: object
    Description: str
    ClassificationName: str
    Guid: Guid
    Name: str
    def InternalGetAttributeTypeInfo(self, ) -> AeccAttributeTypeInfoBool: ...

class UDPClassification:
    """.NET: Autodesk.Civil.DatabaseServices.UDPClassification"""
    def __init__(self, *args) -> None: ...
    UDPs: UDPCollection
    Name: str
    def ContainsUDP(self, udp: UDP) -> bool: ...
    def CreateUDP(self, udpTypeInfo: AttributeTypeInfoDouble, guid: Guid) -> UDPDouble: ...
    def RemoveUDP(self, udp: UDP) -> bool: ...

class UDPClassificationApplyType:
    """.NET: Autodesk.Civil.DatabaseServices.UDPClassificationApplyType"""
    def __init__(self, *args) -> None: ...
    ...

class UDPClassificationCollection:
    """.NET: Autodesk.Civil.DatabaseServices.UDPClassificationCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: UDPClassification
    Item: UDPClassification
    def Add(self, name: str) -> UDPClassification: ...
    def Contains(self, name: str) -> bool: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    @staticmethod
    def GetPointUDPClassifications(pDatabase: Database) -> UDPClassificationCollection: ...
    def Remove(self, udpClassification: UDPClassification) -> bool: ...

class UDPCollection:
    """.NET: Autodesk.Civil.DatabaseServices.UDPCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: UDP
    Item: list
    Item: list
    def Contains(self, udp: UDP) -> bool: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def ToArray(self, ) -> list: ...

class UDPDouble(UDP):
    """.NET: Autodesk.Civil.DatabaseServices.UDPDouble"""
    def __init__(self, *args) -> None: ...
    LowerBoundValue: float
    UpperBoundValue: float
    LowerBoundInclusive: bool
    UpperBoundInclusive: bool
    DefaultValue: float
    DataType: AttributeTypeInfoDoubleDataType
    IsInUsed: bool
    UseDefaultValue: bool
    DefaultValue: object
    Description: str
    ClassificationName: str
    Guid: Guid
    Name: str

class UDPEnumeration(UDP):
    """.NET: Autodesk.Civil.DatabaseServices.UDPEnumeration"""
    def __init__(self, *args) -> None: ...
    DefaultValue: str
    IsInUsed: bool
    UseDefaultValue: bool
    DefaultValue: object
    Description: str
    ClassificationName: str
    Guid: Guid
    Name: str
    def GetEnumValues(self, ) -> list: ...

class UDPInteger(UDP):
    """.NET: Autodesk.Civil.DatabaseServices.UDPInteger"""
    def __init__(self, *args) -> None: ...
    LowerBoundValue: int
    UpperBoundValue: int
    LowerBoundInclusive: bool
    UpperBoundInclusive: bool
    DefaultValue: int
    IsInUsed: bool
    UseDefaultValue: bool
    DefaultValue: object
    Description: str
    ClassificationName: str
    Guid: Guid
    Name: str

class UDPString(UDP):
    """.NET: Autodesk.Civil.DatabaseServices.UDPString"""
    def __init__(self, *args) -> None: ...
    DefaultValue: str
    IsInUsed: bool
    UseDefaultValue: bool
    DefaultValue: object
    Description: str
    ClassificationName: str
    Guid: Guid
    Name: str

class VerticalCurveType:
    """.NET: Autodesk.Civil.DatabaseServices.VerticalCurveType"""
    def __init__(self, *args) -> None: ...
    ...

class VerticalGeometryBandLabelGroup(ProfileBandLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.VerticalGeometryBandLabelGroup"""
    def __init__(self, *args) -> None: ...
    StyleName: str
    StyleId: ObjectId
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAvailableLabelGroups(profileViewId: ObjectId, includeDerived: bool) -> ObjectIdCollection: ...

class ViewFrame(GeoEntity):
    """.NET: Autodesk.Civil.DatabaseServices.ViewFrame"""
    def __init__(self, *args) -> None: ...
    SheetSet: str
    Sheet: str
    EndStation: float
    StartStation: float
    AlignmentId: ObjectId
    IsLabelVisible: bool
    LabelStyleId: ObjectId
    LabelAnchorPosition: ViewFrameLabelLocationType
    GroupId: ObjectId
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ViewFrameGroup(GeoEntity):
    """.NET: Autodesk.Civil.DatabaseServices.ViewFrameGroup"""
    def __init__(self, *args) -> None: ...
    DefaultRightMatchLineLabelStyleId: ObjectId
    DefaultLeftMatchLineLabelStyleId: ObjectId
    DefaultRightMatchLineLabelAnchorPosition: MatchLineLabelLocationType
    DefaultLeftMatchLineLabelAnchorPosition: MatchLineLabelLocationType
    DefaultViewFrameLabelStyleId: ObjectId
    DefaultViewFrameLabelAnchorPosition: ViewFrameLabelLocationType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    StyleId: ObjectId
    StyleName: str
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetAvailableMatchLineLabelGroupIds(self, ) -> ObjectIdCollection: ...
    def GetAvailableViewFrameLabelGroupIds(self, ) -> ObjectIdCollection: ...
    def GetMatchLineIds(self, ) -> ObjectIdCollection: ...
    def GetMatchLineLabelGroupIdBySide(self, side: EntitySideType) -> ObjectId: ...
    def GetViewFrameIds(self, ) -> ObjectIdCollection: ...

class ViewFrameLabelGroup(AutoFeatureLabelGroup):
    """.NET: Autodesk.Civil.DatabaseServices.ViewFrameLabelGroup"""
    def __init__(self, *args) -> None: ...
    RangeStartFromFeature: bool
    RangeStart: float
    RangeEndFromFeature: bool
    RangeEnd: float
    DefaultDimensionAnchorValue: float
    DefaultDimensionAnchorOption: DimensionAnchorOptionType
    StyleName: str
    StyleId: ObjectId
    SubEntities: IList
    SubEntityCount: int
    ApplicableLabelStyleIds: LabelStyleCollection
    Mask: LabelMaskType
    FeatureId: ObjectId
    AutoStagger: StaggerLabelType
    ViewId: ObjectId
    RotationType: LabelRotationType
    AllowsReversing: bool
    AllowsPinning: bool
    AllowsLeaderAttachment: bool
    AllowsFlipping: bool
    AllowsDragging: bool
    AllowsDimensionAnchors: bool
    AllowsAnchorMarker: bool
    LabelType: LabelType
    FolderId: ObjectId
    IsPartialReferenceObject: bool
    IsReferencedSourceExisting: bool
    IsReferenceStale: bool
    IsReferenceValid: bool
    IsReadOnlyReferenceObject: bool
    IsCWSReferenceObject: bool
    IsCWSSourceObject: bool
    IsReferenceSubObject: bool
    IsReferenceObject: bool
    IsUsed: bool
    FingerPrint: int
    ShowToolTip: bool
    DisplayName: str
    Description: str
    Name: str
    Document: object
    Application: object
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    TypeIcon: Icon
    Overrides: OverrideCollection
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(viewFrameGroupId: ObjectId, labelStyleId: ObjectId, anchorPosition: ViewFrameLabelLocationType) -> ObjectId: ...
    @staticmethod
    def GetAvailableLabelGroupIds(viewFrameGroupId: ObjectId) -> ObjectIdCollection: ...

class VolumeSurfaceProperties:
    """.NET: Autodesk.Civil.DatabaseServices.VolumeSurfaceProperties"""
    def __init__(self, *args) -> None: ...
    UnadjustedNetVolume: float
    UnadjustedFillVolume: float
    UnadjustedCutVolume: float
    AdjustedNetVolume: float
    AdjustedFillVolume: float
    AdjustedCutVolume: float
    FillFactor: float
    CutFactor: float
    ComparisonSurface: ObjectId
    BaseSurface: ObjectId

class VolumeTableType:
    """.NET: Autodesk.Civil.DatabaseServices.VolumeTableType"""
    def __init__(self, *args) -> None: ...
    ...

class WallBreaklineCreationData:
    """.NET: Autodesk.Civil.DatabaseServices.WallBreaklineCreationData"""
    def __init__(self, *args) -> None: ...
    ...

class WallBreaklineCreationDataEx:
    """.NET: Autodesk.Civil.DatabaseServices.WallBreaklineCreationDataEx"""
    def __init__(self, *args) -> None: ...
    ...

class WidthOffsetTarget(CivilWrapper<AeccWidthOffsetTarget>):
    """.NET: Autodesk.Civil.DatabaseServices.WidthOffsetTarget"""
    def __init__(self, *args) -> None: ...
    TargetId: ObjectId
    def GetDistanceToAlignment(self, alignmentId: ObjectId, stationOnAlignment: float, side: AlignmentSide, xOnTarget: float, yOnTarget: float) -> float: ...
    def GetNearestPipeOfNetworkToAlignment(self, alignmentId: ObjectId, stationOnAlignment: float, side: AlignmentSide, pipeId: ObjectId) -> None: ...
