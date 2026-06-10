# Auto-generated — Civil 26 — Autodesk.Civil.DatabaseServices.Styles

class AlignmentDesignCheckSet(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AlignmentDesignCheckSet"""
    def __init__(self, *args) -> None: ...
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def AddDesignCheck(self, type: AlignmentDesignCheckType, name: str) -> AlignmentDesignCheck: ...
    def GetAllDesignChecks(self, ) -> list: ...
    def RemoveAllDesignCheck(self, ) -> None: ...
    def RemoveDesignCheck(self, type: AlignmentDesignCheckType, name: str) -> None: ...

class AlignmentDesignCheckSetCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AlignmentDesignCheckSetCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class AlignmentDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AlignmentDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class AlignmentLabelSetItem(BaseLabelSetItem):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AlignmentLabelSetItem"""
    def __init__(self, *args) -> None: ...
    Increment: float
    LabelStyleName: str
    LabelStyleId: ObjectId
    LabelStyleType: LabelStyleType
    def GetLabeledAlignmentGeometryPoints(self, ) -> Dictionary: ...
    def GetLabeledProfileGeometryPoints(self, ) -> Dictionary: ...
    def GetLabeledSuperelevationTransitionPoints(self, ) -> Dictionary: ...
    def SetLabeledAlignmentGeometryPoints(self, pointTypes: Dictionary) -> None: ...
    def SetLabeledProfileGeometryPoints(self, pointTypes: Dictionary) -> None: ...
    def SetLabeledSuperelevationTransitionPoints(self, pointTypes: Dictionary) -> None: ...

class AlignmentLabelSetStyle(BaseLabelSetStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AlignmentLabelSetStyle"""
    def __init__(self, *args) -> None: ...
    Item: AlignmentLabelSetItem
    Count: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class AlignmentLabelSetStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AlignmentLabelSetStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class AlignmentStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AlignmentStyle"""
    def __init__(self, *args) -> None: ...
    ArrowHeadOption: ArrowHeadOption
    LineMarkerDisplayStyleSection: DisplayStyle
    CurveSpiralIntersectPointMarkerStyle: ObjectId
    EndPointMarkerStyle: ObjectId
    SpiralCurveIntersectPointMarkerStyle: ObjectId
    LineCurveIntersectPointMarkerStyle: ObjectId
    LineSpiralIntersectPointMarkerStyle: ObjectId
    SpiralLineIntersectPointMarkerStyle: ObjectId
    StationReferencePointMarkerStyle: ObjectId
    RadiusSnapValue: float
    CompoundCurveIntersectPointMarkerStyle: ObjectId
    ThroughPointMarkerStyle: ObjectId
    EnableRadiusSnap: bool
    BeginPointMarkerStyle: ObjectId
    ReverseSpiralIntersectPointMarkerStyle: ObjectId
    SpiralSpiralIntersectPointMarkerStyle: ObjectId
    ReverseCurveIntersectPointMarkerStyle: ObjectId
    IntersectionPointMarkerStyle: ObjectId
    CurveLineIntersectPointMarkerStyle: ObjectId
    MidPointMarkerStyle: ObjectId
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleModel(self, type: AlignmentDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: AlignmentDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, ) -> DisplayStyle: ...
    def GetLineMarkerDisplayStyleSection(self, ) -> DisplayStyle: ...

class AlignmentStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AlignmentStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class ArrowHeadOption(CivilWrapper<AeccDbStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ArrowHeadOption"""
    def __init__(self, *args) -> None: ...
    FixedScaleZ: float
    FixedScaleY: float
    FixedScaleX: float
    Fit: ArrowHeadFitType
    SizeValue: float
    SizeOption: ArrowHeadSizeType
    ArrowBlockName: str
    ArrowType: ArrowHeadType

class AssemblyStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AssemblyStyle"""
    def __init__(self, *args) -> None: ...
    MarkerStyleAtOffsetBaselineOriginId: ObjectId
    MarkerStyleAtOffsetBaselineId: ObjectId
    MarkerStyleAtMainBaselineOriginId: ObjectId
    MarkerStyleAtMainBaselineId: ObjectId
    MarkerStyleAtAssemblyOriginId: ObjectId
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleModel(self, type: AssemblyDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: AssemblyDisplayStyleType) -> DisplayStyle: ...

class AssemblyStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AssemblyStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class AxisPosition:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AxisPosition"""
    def __init__(self, *args) -> None: ...
    ...

class AxisStyle(CivilWrapper<AeccDbGraphStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AxisStyle"""
    def __init__(self, *args) -> None: ...
    HorizontalGeometryTickStyle: AxisTickStyle
    MinorTickStyle: AxisTickStyle
    MajorTickStyle: AxisTickStyle
    TitleStyle: AxisTitleStyle
    ShowTickAndLabel: bool

class AxisTickJustificationType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AxisTickJustificationType"""
    def __init__(self, *args) -> None: ...
    ...

class AxisTickStyle(CivilWrapper<AeccDbGraphStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AxisTickStyle"""
    def __init__(self, *args) -> None: ...
    TickAndLabelStartElevation: bool
    OffsetY: float
    OffsetX: float
    Rotation: float
    Justification: AxisTickJustificationType
    TextHeight: float
    TextStyle: str
    LabelText: str
    Size: float
    Interval: float

class AxisTickType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AxisTickType"""
    def __init__(self, *args) -> None: ...
    ...

class AxisTitleLocationType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AxisTitleLocationType"""
    def __init__(self, *args) -> None: ...
    ...

class AxisTitleStyle(CivilWrapper<AeccDbGraphStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AxisTitleStyle"""
    def __init__(self, *args) -> None: ...
    OffsetY: float
    OffsetX: float
    Rotation: float
    Location: AxisTitleLocationType
    TextHeight: float
    TextStyle: str
    Text: str

class BandLabelStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BandLabelStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class BandSetItem:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BandSetItem"""
    def __init__(self, *args) -> None: ...
    StaggerLineHeight: float
    StaggerLabel: StaggerLabelType
    Weeding: float
    Gap: float
    ShowLabels: bool
    BandStyleId: ObjectId
    BandType: BandType
    MinorInterval: float
    MajorInterval: float
    Location: BandLocationType

class BandSetItemCollection:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BandSetItemCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Location: BandLocationType
    def Add(self, bandStyleId: ObjectId) -> None: ...
    def Dispose(self, ) -> None: ...
    def RemoveAll(self, ) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    def Swap(self, index1: int, index2: int) -> None: ...

class BandSetStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BandSetStyle"""
    def __init__(self, *args) -> None: ...
    MatchIncrementToGridIntervals: bool
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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

class BandStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BandStyle"""
    def __init__(self, *args) -> None: ...
    WeedingFactor: float
    TextHeight: float
    TextLocation: BandTitleTextLocation
    TextBoxPosition: BandTitleBoxPosition
    OffsetFromBand: float
    TextBoxWidth: float
    BandHeight: float
    Text: str
    TextStyle: str
    TitleTextLabelStyleId: ObjectId
    BandType: BandType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    @staticmethod
    def GetBandStyleId(database: Database, bandType: BandType, bandStyleName: str) -> ObjectId: ...

class BandStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BandStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class BandStylesRoot(TreeOidWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BandStylesRoot"""
    def __init__(self, *args) -> None: ...
    SectionViewSegmentsBandStyles: BandStyleCollection
    SectionViewSectionDataBandStyles: BandStyleCollection
    ProfileViewPipeNetworkBandStyles: BandStyleCollection
    ProfileViewVerticalGeometryBandStyles: BandStyleCollection
    ProfileViewSuperElevationBandStyles: BandStyleCollection
    ProfileViewSectionalDataBandStyles: BandStyleCollection
    ProfileViewProfileDataBandStyles: BandStyleCollection
    ProfileViewHorizontalGeometryBandStyles: BandStyleCollection
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class BandTickStyle(CivilWrapper<AeccDbGraphStyleBands>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BandTickStyle"""
    def __init__(self, *args) -> None: ...
    SmallTicksAtBottomSize: float
    SmallTicksAtMiddleSize: float
    SmallTicksAtTopSize: float
    IncrementSmallTicksAtBottom: bool
    IncrementSmallTicksAtMiddle: bool
    IncrementSmallTicksAtTop: bool
    IncrementTicksToFullHeight: bool

class BandTitleBoxPosition:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BandTitleBoxPosition"""
    def __init__(self, *args) -> None: ...
    ...

class BandTitleTextLocation:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BandTitleTextLocation"""
    def __init__(self, *args) -> None: ...
    ...

class BaseLabelSetItem(CivilWrapper<AeccDbAlignStnLabelsDlgTemplate>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BaseLabelSetItem"""
    def __init__(self, *args) -> None: ...
    LabelStyleName: str
    LabelStyleId: ObjectId
    LabelStyleType: LabelStyleType

class BaseLabelSetStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BaseLabelSetStyle"""
    def __init__(self, *args) -> None: ...
    Count: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def Add(self, majorStation: BaseLabelSetItem, minorStationLabelStyleName: str) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class BuildingSiteDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BuildingSiteDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class BuildingSiteStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BuildingSiteStyle"""
    def __init__(self, *args) -> None: ...
    MarkerStyleName: str
    MarkerStyleId: ObjectId
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleModel(self, type: BuildingSiteDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: BuildingSiteDisplayStyleType) -> DisplayStyle: ...

class BuildingSiteStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BuildingSiteStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class CantViewStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CantViewStyle"""
    def __init__(self, *args) -> None: ...
    UseSmallTicksAtBottom: bool
    UseSmallTicksAtMiddle: bool
    UseSmallTicksAtTop: bool
    UseFullHeightTick: bool
    AxisBottomMajorTickInterval: float
    AxisTopMajorTickInterval: float
    VerticalExaggeration: float
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStylePlan(self, type: CantViewDisplayStyleType) -> DisplayStyle: ...

class CantViewStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CantViewStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class CatchmentDisplayStylePlanType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CatchmentDisplayStylePlanType"""
    def __init__(self, *args) -> None: ...
    ...

class CatchmentStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CatchmentStyle"""
    def __init__(self, *args) -> None: ...
    FlowSegmentStartPointMarkerStyle: ObjectId
    MostDistantPointMarkerStyle: ObjectId
    DischargePointMarkerStyle: ObjectId
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStylePlan(self, type: CatchmentDisplayStylePlanType) -> DisplayStyle: ...

class CatchmentStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CatchmentStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class CenterMarkerSizeType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CenterMarkerSizeType"""
    def __init__(self, *args) -> None: ...
    ...

class CodeSetStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CodeSetStyle"""
    def __init__(self, *args) -> None: ...
    SubentityStyleType: SubassemblySubentityStyleType
    Item: CodeSetStyleItem
    Count: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def Add(self, code: str, styleId: ObjectId) -> CodeSetStyleItem: ...
    @staticmethod
    def GetCurrentStyleSetId() -> ObjectId: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetItemBy(self, itemType: CodeSetStyleItemType, code: str) -> CodeSetStyleItem: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, code: str) -> None: ...

class CodeSetStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CodeSetStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class CodeSetStyleItem(CivilWrapper<AeccDbRoadwayStyleSet>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CodeSetStyleItem"""
    def __init__(self, *args) -> None: ...
    PayItems: list
    RenderMaterialStyleName: str
    RenderMaterialStyleId: ObjectId
    MaterialAreaFillStyleName: str
    MaterialAreaFillStyleId: ObjectId
    FeatureLineStyleName: str
    FeatureLineStyleId: ObjectId
    LabelStyleName: str
    LabelStyleId: ObjectId
    ItemType: CodeSetStyleItemType
    StyleType: SubassemblySubentityStyleType
    Description: str
    Classification: str
    CodeStyleName: str
    CodeStyleId: ObjectId
    Code: str

class CodeSetStyleItemType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CodeSetStyleItemType"""
    def __init__(self, *args) -> None: ...
    ...

class ColorSchemeType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ColorSchemeType"""
    def __init__(self, *args) -> None: ...
    ...

class ColumnStyle(CivilWrapper<AeccDbScheduleTableStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ColumnStyle"""
    def __init__(self, *args) -> None: ...
    ContentJustification: TextJustificationType
    ContentStringFormatted: str
    ContentString: str
    HeaderJustification: TextJustificationType
    HeaderStringFormatted: str
    HeaderString: str
    ColumnWidth: float

class ColumnStyleCollection(CivilWrapper<AeccDbScheduleTableStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ColumnStyleCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ColumnStyle
    def Add(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def RemoveAt(self, index: int) -> None: ...

class ContourSmoothingType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType"""
    def __init__(self, *args) -> None: ...
    ...

class ContourValues:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ContourValues"""
    def __init__(self, *args) -> None: ...
    MinorLineWeight: LineWeight
    MajorLineWeight: LineWeight
    MinorLineTypeId: ObjectId
    MajorLineTypeId: ObjectId
    MinorColor: Color
    MajorColor: Color

class CorridorDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CorridorDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class CorridorStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CorridorStyle"""
    def __init__(self, *args) -> None: ...
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleModel(self, type: CorridorDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: CorridorDisplayStyleType) -> DisplayStyle: ...

class CorridorStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CorridorStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class CustomMarkerSuperimposeType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CustomMarkerSuperimposeType"""
    def __init__(self, *args) -> None: ...
    ...

class CustomMarkerType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CustomMarkerType"""
    def __init__(self, *args) -> None: ...
    ...

class DataBandingType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.DataBandingType"""
    def __init__(self, *args) -> None: ...
    ...

class DataPartFamily:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.DataPartFamily"""
    def __init__(self, *args) -> None: ...
    SweptShape: SweptShapeType
    BoundingShape: BoundingShapeType
    Domain: DomainType
    PartType: PartType
    GUID: str
    Description: str

class DisplayStyle(CivilWrapper<AeccDbStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.DisplayStyle"""
    def __init__(self, *args) -> None: ...
    Color: Color
    PlotStyle: str
    LinetypeScale: float
    Lineweight: LineWeight
    Linetype: str
    Layer: str
    Visible: bool

class Expression:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.Expression"""
    def __init__(self, *args) -> None: ...
    FormatResultAs: ExpressionFormatedType
    ReferenceString: str
    ExpressionString: str
    Description: str
    Name: str

class ExpressionCollection:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ExpressionCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: Expression
    Item: Expression
    def Add(self, name: str, description: str, expression: str) -> Expression: ...
    def Clear(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def RemoveAt(self, index: int) -> None: ...

class ExpressionFormatedType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ExpressionFormatedType"""
    def __init__(self, *args) -> None: ...
    ...

class FeatureLineDisplayStyleProfileType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.FeatureLineDisplayStyleProfileType"""
    def __init__(self, *args) -> None: ...
    ...

class FeatureLineStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.FeatureLineStyle"""
    def __init__(self, *args) -> None: ...
    ProfileEndingVertexMarkerStyleName: str
    ProfileEndingVertexMarkerStyleId: ObjectId
    ProfileInternalVertexMarkerStyleName: str
    ProfileInternalVertexMarkerStyleId: ObjectId
    ProfileBeginningVertexMarkerStyleName: str
    ProfileBeginningVertexMarkerStyleId: ObjectId
    SectionMarkerStyleName: str
    SectionMarkerStyleId: ObjectId
    SectionMarkerDisplayStyleSection: DisplayStyle
    FeatureLineDisplayStyleModel: DisplayStyle
    FeatureLineDisplayStylePlan: DisplayStyle
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleProfile(self, type: FeatureLineDisplayStyleProfileType) -> DisplayStyle: ...
    def GetFeatureLineDisplayStyleModel(self, ) -> DisplayStyle: ...
    def GetFeatureLineDisplayStylePlan(self, ) -> DisplayStyle: ...
    def GetSectionMarkerDisplayStyleSection(self, ) -> DisplayStyle: ...

class FeatureLineStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.FeatureLineStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class GradingCriteria(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GradingCriteria"""
    def __init__(self, *args) -> None: ...
    InteriorCornerOverlap: PropertyEnum
    Slope: PropertyDouble
    SlopeFormatType: PropertyEnum
    FillSlope: PropertyDouble
    FillSlopeFormatType: PropertyEnum
    CutSlope: PropertyDouble
    CutSlopeFormatType: PropertyEnum
    ProjectionDistance: PropertyDouble
    Distance: PropertyDouble
    Elevation: PropertyDouble
    RelativeElevation: PropertyDouble
    ProjectionRelativeElevation: PropertyDouble
    SearchOrder: PropertyEnum
    DistanceProjectionType: GradingDistanceProjectionType
    RelativeElevationProjectionType: GradingRelativeElevationProjectionType
    ElevationProjectionType: GradingElevationProjectionType
    SurfaceProjectionType: GradingSurfaceProjectionType
    Target: GradingTargetType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def CopyAsSibling(self, criteriaName: str) -> ObjectId: ...

class GradingCriteriaSet(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GradingCriteriaSet"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def AddCriteria(self, criteriaName: str) -> None: ...
    def GradingCriteriaIds(self, ) -> ObjectIdCollection: ...
    def MoveCriteria(self, criteriaName: str, criteriaSetName: str) -> None: ...
    def RemoveCriteria(self, index: int) -> None: ...

class GradingCriteriaSetCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GradingCriteriaSetCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class GradingDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GradingDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class GradingStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GradingStyle"""
    def __init__(self, *args) -> None: ...
    SlopeRangeMax: float
    SlopeRangeMin: float
    UseSlopeRange: bool
    SlopePatternStyleName: str
    SlopePatternStyleId: ObjectId
    UseSlopePatternStyle: bool
    FixedSize: float
    PlottedSize: float
    PercentageOfScreen: float
    CenterMarker: CenterMarkerSizeType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleModel(self, type: GradingDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: GradingDisplayStyleType) -> DisplayStyle: ...

class GradingStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GradingStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...
    def SetCenterMarkerVisable(self, isVisable: bool) -> None: ...
    def SetSlopePatternVisable(self, isVisable: bool) -> None: ...

class GraphDirectionType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GraphDirectionType"""
    def __init__(self, *args) -> None: ...
    ...

class GraphStyle(CivilWrapper<AeccDbGraphStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GraphStyle"""
    def __init__(self, *args) -> None: ...
    TitleStyle: GraphTitleStyle
    Direction: GraphDirectionType
    VerticalExaggeration: float
    CurrentHorizontalScale: float
    VerticalScale: float

class GraphTitleJustificationType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GraphTitleJustificationType"""
    def __init__(self, *args) -> None: ...
    ...

class GraphTitleLocationType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GraphTitleLocationType"""
    def __init__(self, *args) -> None: ...
    ...

class GraphTitleStyle(CivilWrapper<AeccDbGraphStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GraphTitleStyle"""
    def __init__(self, *args) -> None: ...
    BorderGap: float
    Border: bool
    OffsetY: float
    OffsetX: float
    Justification: GraphTitleJustificationType
    Location: GraphTitleLocationType
    TextHeight: float
    TextStyle: str
    Text: str

class GridOptions(CivilWrapper<AeccDbGraphStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GridOptions"""
    def __init__(self, *args) -> None: ...
    OmitGridInPaddingAreas: bool
    ClipToHighestProfile: bool
    UseClipGrid: bool

class GridStyle(CivilWrapper<AeccDbGraphStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GridStyle"""
    def __init__(self, *args) -> None: ...
    AxisOffsetRight: float
    AxisOffsetLeft: float
    AxisOffsetBottom: float
    AxisOffsetAbove: float
    GridPaddingRight: float
    GridPaddingLeft: float
    GridPaddingBottom: float
    GridPaddingAbove: float
    HorizontalGridOptions: GridOptions
    VerticalGridOptions: GridOptions

class GridType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GridType"""
    def __init__(self, *args) -> None: ...
    ...

class GroupPlotAlignType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GroupPlotAlignType"""
    def __init__(self, *args) -> None: ...
    ...

class GroupPlotCellSizeType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GroupPlotCellSizeType"""
    def __init__(self, *args) -> None: ...
    ...

class GroupPlotDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GroupPlotDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class GroupPlotStartCornerType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GroupPlotStartCornerType"""
    def __init__(self, *args) -> None: ...
    ...

class GroupPlotStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GroupPlotStyle"""
    def __init__(self, *args) -> None: ...
    GridVerticalMinor: float
    GridVerticalMajor: float
    GridHorizontalMinor: float
    GridHorizontalMajor: float
    GapBetweenPages: float
    SpaceRow: float
    SpaceColumn: float
    CellSizeType: GroupPlotCellSizeType
    AlignType: GroupPlotAlignType
    StartCorner: GroupPlotStartCornerType
    MaximumInColumn: int
    MaximumInRow: int
    PlotRule: SectionViewPlotRuleType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayPlan(self, type: GroupPlotDisplayStyleType) -> DisplayStyle: ...

class GroupPlotStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GroupPlotStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class HatchDisplayStyle(CivilWrapper<AeccDbStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.HatchDisplayStyle"""
    def __init__(self, *args) -> None: ...
    IsDoubleHatch: bool
    VOffset: float
    UOffset: float
    Spacing: float
    UseAngleOfObject: bool
    Angle: float
    ScaleFactor: float
    Pattern: str
    HatchType: HatchType

class HatchType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.HatchType"""
    def __init__(self, *args) -> None: ...
    ...

class HorizontalGeometryBandStyle(BandStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.HorizontalGeometryBandStyle"""
    def __init__(self, *args) -> None: ...
    PointOfIntersectionTickStyle: BandTickStyle
    SpiralTickStyle: BandTickStyle
    CurveTickStyle: BandTickStyle
    TangentTickStyle: BandTickStyle
    PointOfIntersectionLabelStyleId: ObjectId
    SpiralLabelStyleId: ObjectId
    CurveLabelStyleId: ObjectId
    TangentLabelStyleId: ObjectId
    SchematicLineType: SchematicLineOption
    TitleTextLabelStyleId: ObjectId
    BandType: BandType
    WeedingFactor: float
    TextHeight: float
    TextLocation: BandTitleTextLocation
    TextBoxPosition: BandTitleBoxPosition
    OffsetFromBand: float
    TextBoxWidth: float
    BandHeight: float
    Text: str
    TextStyle: str
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStylePlan(self, type: HorizontalGeometryDisplayStyleType) -> DisplayStyle: ...

class HorizontalGeometryDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.HorizontalGeometryDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class InterferenceDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.InterferenceDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class InterferenceModelSizeOptionType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.InterferenceModelSizeOptionType"""
    def __init__(self, *args) -> None: ...
    ...

class InterferenceModelSizeType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.InterferenceModelSizeType"""
    def __init__(self, *args) -> None: ...
    ...

class InterferenceModelType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.InterferenceModelType"""
    def __init__(self, *args) -> None: ...
    ...

class InterferenceStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.InterferenceStyle"""
    def __init__(self, *args) -> None: ...
    DrawingScaleModelSize: float
    AbsoluteModelSize: float
    ModelSizeOptions: InterferenceModelSizeOptionType
    ModelSizeType: InterferenceModelSizeType
    ModelOptions: InterferenceModelType
    MarkerStyle: ObjectId
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleModel(self, component: InterferenceDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, component: InterferenceDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, component: InterferenceDisplayStyleType) -> DisplayStyle: ...

class InterferenceStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.InterferenceStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class IntersectionStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.IntersectionStyle"""
    def __init__(self, *args) -> None: ...
    MarkerStyleId: ObjectId
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleModel(self, ) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, ) -> DisplayStyle: ...

class IntersectionStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.IntersectionStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class LabelDisplayModeType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelDisplayModeType"""
    def __init__(self, *args) -> None: ...
    ...

class LabelSetStylesRoot(TreeOidWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelSetStylesRoot"""
    def __init__(self, *args) -> None: ...
    SectionLabelSetStyles: SectionLabelSetStyleCollection
    ProfileLabelSetStyles: ProfileLabelSetStyleCollection
    AlignmentLabelSetStyles: AlignmentLabelSetStyleCollection
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyle"""
    def __init__(self, *args) -> None: ...
    ChildrenCount: int
    Item: ObjectId
    Item: ObjectId
    ParentLabelStyleId: ObjectId
    Properties: LabelStyleBase
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def AddChild(self, labelStyleName: str) -> ObjectId: ...
    def AddComponent(self, name: str, type: LabelStyleComponentType) -> ObjectId: ...
    def AddReferenceTextComponent(self, name: str, selectedType: ReferenceTextComponentSelectedType) -> ObjectId: ...
    def AddTextForEachComponent(self, name: str, selectedType: TextForEachComponentSelectedType) -> ObjectId: ...
    def GetComponents(self, type: LabelStyleComponentType) -> ObjectIdCollection: ...
    def GetComponentsCount(self, type: LabelStyleComponentType) -> int: ...
    def GetComponentsDrawOrder(self, ) -> list: ...
    def GetDescendantIds(self, ) -> ObjectIdCollection: ...
    def IsSupportedComponent(self, type: LabelStyleComponentType) -> bool: ...
    def RemoveAllDescendants(self, ) -> None: ...
    def RemoveChild(self, index: int) -> None: ...
    def RemoveComponent(self, name: str) -> None: ...
    def SetComponentsDrawOrder(self, componentIds: list) -> None: ...
    def SwitchComponentsDrawOrder(self, index1: int, index2: int) -> None: ...

class LabelStyleBase(CivilWrapper<AeccDbLabelStyleCollector>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleBase"""
    def __init__(self, *args) -> None: ...
    DraggedStateComponents: BaseDraggedStateComponents
    Leader: BaseLeader
    PlanReadability: BasePlanReadability
    Behavior: BaseBehavior
    Label: BaseLabel

class LabelStyleBlockComponent(LabelStyleComponent):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleBlockComponent"""
    def __init__(self, *args) -> None: ...
    Block: StyleBlock
    General: StyleGeneral
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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

class LabelStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleCollection"""
    def __init__(self, *args) -> None: ...
    Expressions: ExpressionCollection
    DefaultLabelStyle: LabelStyleDefault
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...
    def GetDescendantIds(self, ) -> ObjectIdCollection: ...
    def Remove(self, styleName: str) -> None: ...

class LabelStyleComponent(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleComponent"""
    def __init__(self, *args) -> None: ...
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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

class LabelStyleComponentType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleComponentType"""
    def __init__(self, *args) -> None: ...
    ...

class LabelStyleDefault(TreeOidWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleDefault"""
    def __init__(self, *args) -> None: ...
    DraggedStateComponents: DefaultDraggedStateComponents
    Leader: DefaultLeader
    Components: DefaultComponents
    PlanReadability: DefaultPlanReadability
    Behavior: DefaultBehavior
    Label: DefaultLabel
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStyleDirectionArrowComponent(LabelStyleComponent):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleDirectionArrowComponent"""
    def __init__(self, *args) -> None: ...
    DirectionArrow: StyleDirectionArrow
    General: StyleGeneral
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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

class LabelStyleLineComponent(LabelStyleComponent):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleLineComponent"""
    def __init__(self, *args) -> None: ...
    Line: StyleLine
    General: StyleGeneral
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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

class LabelStyleReferenceTextComponent(LabelStyleComponent):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleReferenceTextComponent"""
    def __init__(self, *args) -> None: ...
    Border: StyleBorder
    Text: StyleText
    General: StyleGeneral
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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

class LabelStyleTextComponent(LabelStyleComponent):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleTextComponent"""
    def __init__(self, *args) -> None: ...
    Border: StyleBorder
    Text: StyleText
    General: StyleGeneral
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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

class LabelStyleTextForEachComponent(LabelStyleComponent):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleTextForEachComponent"""
    def __init__(self, *args) -> None: ...
    Border: StyleBorder
    Text: StyleText
    General: StyleGeneral
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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

class LabelStyleTickComponent(LabelStyleComponent):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleTickComponent"""
    def __init__(self, *args) -> None: ...
    Tick: StyleTick
    General: StyleGeneral
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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

class LabelStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class LabelStylesAlignmentRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesAlignmentRoot"""
    def __init__(self, *args) -> None: ...
    PointOfIntersectionLabelStyles: LabelStyleCollection
    VerticalGeometryPointLabelStyles: LabelStyleCollection
    CantCriticalPointsLabelStyles: LabelStyleCollection
    SuperelevationCriticalPointsLabelStyles: LabelStyleCollection
    TangentIntersectionLabelStyles: LabelStyleCollection
    StationOffsetLabelStyles: LabelStyleCollection
    StationEquationLabelStyles: LabelStyleCollection
    SpiralLabelStyles: LabelStyleCollection
    MinorStationLabelStyles: LabelStyleCollection
    MajorStationLabelStyles: LabelStyleCollection
    LineLabelStyles: LabelStyleCollection
    GeometryPointLabelStyles: LabelStyleCollection
    DesignSpeedLabelStyles: LabelStyleCollection
    CurveLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesCatchmentRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesCatchmentRoot"""
    def __init__(self, *args) -> None: ...
    FlowSegmentLabelStyles: LabelStyleCollection
    AreaLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesIntersectionRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesIntersectionRoot"""
    def __init__(self, *args) -> None: ...
    LocationLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesMatchLineRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesMatchLineRoot"""
    def __init__(self, *args) -> None: ...
    RightLabelStyles: LabelStyleCollection
    LeftLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesNode(TreeOidWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesNode"""
    def __init__(self, *args) -> None: ...
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesParcelRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesParcelRoot"""
    def __init__(self, *args) -> None: ...
    LineLabelStyles: LabelStyleCollection
    AreaLabelStyles: LabelStyleCollection
    CurveLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesPipeRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesPipeRoot"""
    def __init__(self, *args) -> None: ...
    CrossProfileLabelStyles: LabelStyleCollection
    CrossSectionLabelStyles: LabelStyleCollection
    PlanProfileLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesPointRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesPointRoot"""
    def __init__(self, *args) -> None: ...
    LabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesProfileRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesProfileRoot"""
    def __init__(self, *args) -> None: ...
    MinorStationLabelStyles: LabelStyleCollection
    MajorStationLabelStyles: LabelStyleCollection
    LineLabelStyles: LabelStyleCollection
    HorizontalGeometryPointLabelStyles: LabelStyleCollection
    GradeBreakLabelStyles: LabelStyleCollection
    GradeBreadLabelStyles: LabelStyleCollection
    CurveLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesProfileViewRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesProfileViewRoot"""
    def __init__(self, *args) -> None: ...
    StationElevationLabelStyles: LabelStyleCollection
    DepthLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesProjectionRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesProjectionRoot"""
    def __init__(self, *args) -> None: ...
    SectionViewProjectionLabelStyles: LabelStyleCollection
    ProfileViewProjectionLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesRoot"""
    def __init__(self, *args) -> None: ...
    GeneralShapeLabelStyles: LabelStyleCollection
    GeneralLinkLabelStyles: LabelStyleCollection
    GeneralMarkerLabelStyles: LabelStyleCollection
    GeneralCurveLabelStyles: LabelStyleCollection
    GeneralLineLabelStyles: LabelStyleCollection
    GeneralNoteLabelStyles: LabelStyleCollection
    ProjectionLabelStyles: LabelStylesProjectionRoot
    PointLabelStyles: LabelStylesPointRoot
    MatchLineLabelStyles: LabelStylesMatchLineRoot
    ViewFrameLabelStyles: LabelStylesViewFrameRoot
    IntersectionLabelStyles: LabelStylesIntersectionRoot
    SampleLineLabelStyles: LabelStylesSampleLineRoot
    SectionViewLabelStyles: LabelStylesSectionViewRoot
    CatchmentLabelStyles: LabelStylesCatchmentRoot
    StructureLabelStyles: LabelStylesStructureRoot
    PipeLabelStyles: LabelStylesPipeRoot
    SectionLabelStyles: LabelStylesSectionRoot
    ProfileViewLabelStyles: LabelStylesProfileViewRoot
    ProfileLabelStyles: LabelStylesProfileRoot
    ParcelLabelStyles: LabelStylesParcelRoot
    SurfaceLabelStyles: LabelStylesSurfaceRoot
    AlignmentLabelStyles: LabelStylesAlignmentRoot
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetSurveyLabelStyles(self, ) -> LabelStylesSurveyRoot: ...

class LabelStylesSampleLineRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesSampleLineRoot"""
    def __init__(self, *args) -> None: ...
    LabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesSectionRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesSectionRoot"""
    def __init__(self, *args) -> None: ...
    CorridorPointLabelStyles: LabelStyleCollection
    SegmentLabelStyles: LabelStyleCollection
    MinorOffsetLabelStyles: LabelStyleCollection
    MajorOffsetLabelStyles: LabelStyleCollection
    GradeBreakLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesSectionViewRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesSectionViewRoot"""
    def __init__(self, *args) -> None: ...
    OffsetElevationLabelStyles: LabelStyleCollection
    GradeLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesStructureRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesStructureRoot"""
    def __init__(self, *args) -> None: ...
    LabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesSurfaceRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesSurfaceRoot"""
    def __init__(self, *args) -> None: ...
    WatershedLabelStyles: LabelStyleCollection
    SpotElevationLabelStyles: LabelStyleCollection
    SlopeLabelStyles: LabelStyleCollection
    ContourLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesSurveyRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesSurveyRoot"""
    def __init__(self, *args) -> None: ...
    LineLabelStyles: LabelStyleCollection
    FigureLabelStyles: LabelStyleCollection
    CurveLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesViewFrameRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesViewFrameRoot"""
    def __init__(self, *args) -> None: ...
    LabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LinkStyle(SubassemblySubentityStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LinkStyle"""
    def __init__(self, *args) -> None: ...
    StyleType: SubassemblySubentityStyleType
    LinkDisplayStyleModel: DisplayStyle
    LinkDisplayStylePlan: DisplayStyle
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleModel(self, ) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, ) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, ) -> DisplayStyle: ...
    def GetLinkDisplayStyleModel(self, ) -> DisplayStyle: ...
    def GetLinkDisplayStylePlan(self, ) -> DisplayStyle: ...

class LinkStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LinkStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class MarkerDisplayType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MarkerDisplayType"""
    def __init__(self, *args) -> None: ...
    ...

class MarkerOrientationType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MarkerOrientationType"""
    def __init__(self, *args) -> None: ...
    ...

class MarkerSizeType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MarkerSizeType"""
    def __init__(self, *args) -> None: ...
    ...

class MarkerStyle(MarkerStyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MarkerStyle"""
    def __init__(self, *args) -> None: ...
    MarkerDisplayStyleSection: DisplayStyle
    MarkerDisplayStyleProfile: DisplayStyle
    MarkerType: MarkerDisplayType
    MarkerDisplayStyleModel: DisplayStyle
    MarkerDisplayStylePlan: DisplayStyle
    Orientation: MarkerOrientationType
    MarkerFixedScale: Point3d
    MarkerSize: float
    SizeType: MarkerSizeType
    MarkerRotationAngle: float
    MarkerSymbolName: str
    CustomMarkerSuperimposeStyle: CustomMarkerSuperimposeType
    CustomMarkerStyle: CustomMarkerType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetMarkerDisplayStyleProfile(self, ) -> DisplayStyle: ...
    def GetMarkerDisplayStyleSection(self, ) -> DisplayStyle: ...

class MarkerStyleBase(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MarkerStyleBase"""
    def __init__(self, *args) -> None: ...
    MarkerDisplayStyleModel: DisplayStyle
    MarkerDisplayStylePlan: DisplayStyle
    Orientation: MarkerOrientationType
    MarkerFixedScale: Point3d
    MarkerSize: float
    SizeType: MarkerSizeType
    MarkerRotationAngle: float
    MarkerSymbolName: str
    CustomMarkerSuperimposeStyle: CustomMarkerSuperimposeType
    CustomMarkerStyle: CustomMarkerType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetMarkerDisplayStyleModel(self, ) -> DisplayStyle: ...
    def GetMarkerDisplayStylePlan(self, ) -> DisplayStyle: ...

class MarkerStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MarkerStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class MassHaulLineStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MassHaulLineStyle"""
    def __init__(self, *args) -> None: ...
    FreeHaulOption: FreeHaulDisplayType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleProfile(self, type: MassHaulLineDisplayStyleType) -> DisplayStyle: ...
    def GetHatchDisplayStyleProfile(self, type: MassHaulLineHatchDisplayStyleType) -> HatchDisplayStyle: ...

class MassHaulLineStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MassHaulLineStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class MassHaulViewStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MassHaulViewStyle"""
    def __init__(self, *args) -> None: ...
    RightAxis: AxisStyle
    LeftAxis: AxisStyle
    BottomAxis: AxisStyle
    MiddleAxis: AxisStyle
    TopAxis: AxisStyle
    GridStyle: GridStyle
    GraphStyle: GraphStyle
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStylePlan(self, type: MassHaulViewDisplayStyleType) -> DisplayStyle: ...

class MassHaulViewStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MassHaulViewStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class MatchLineStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MatchLineStyle"""
    def __init__(self, *args) -> None: ...
    MatchLineMaskHatchDisplayStyle: HatchDisplayStyle
    MatchLineMaskDisplayStylePlan: DisplayStyle
    LinesDisplayStylePlan: DisplayStyle
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetLinesDisplayStylePlan(self, ) -> DisplayStyle: ...
    def GetMatchLineMaskDisplayStylePlan(self, ) -> DisplayStyle: ...
    def GetMatchLineMaskHatchDisplayStyle(self, ) -> HatchDisplayStyle: ...

class MatchLineStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MatchLineStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class NetworkRuleSetStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.NetworkRuleSetStyle"""
    def __init__(self, *args) -> None: ...
    RulesCount: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def CloneAndAddRule(self, sourceRuleId: ObjectId) -> None: ...
    def GetRuleIds(self, ) -> ObjectIdCollection: ...
    def RemoveAllRules(self, ) -> None: ...
    def RemoveRule(self, ruleId: ObjectId) -> None: ...

class ParcelDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ParcelDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class ParcelStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ParcelStyle"""
    def __init__(self, *args) -> None: ...
    AreaFillHatchDisplayStyleModel: HatchDisplayStyle
    AreaFillHatchDisplayStylePlan: HatchDisplayStyle
    ParcelSegmentsMarkerStyle: ObjectId
    NameTemplate: str
    PatternFillDistance: float
    ObservePatternFillDistance: bool
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetAreaFillHatchDisplayStyleModel(self, ) -> HatchDisplayStyle: ...
    def GetAreaFillHatchDisplayStylePlan(self, ) -> HatchDisplayStyle: ...
    def GetDisplayStyleModel(self, type: ParcelDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: ParcelDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, ) -> DisplayStyle: ...

class ParcelStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ParcelStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class PartDataSourceType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PartDataSourceType"""
    def __init__(self, *args) -> None: ...
    ...

class PartFamily(DBObject):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PartFamily"""
    def __init__(self, *args) -> None: ...
    PartSizeFilter: SizeFilterRecord
    Item: ObjectId
    Item: ObjectId
    PartSizeCount: int
    SweptShape: SweptShapeType
    BoundingShape: BoundingShapeType
    PartType: PartType
    Description: str
    GUID: str
    Domain: DomainType
    IsUsed: bool
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
    def AddPartSize(self, partSizeFilter: SizeFilterRecord) -> None: ...
    def RemovePartSize(self, partSizeId: ObjectId) -> None: ...

class PartSize(DBObject):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PartSize"""
    def __init__(self, *args) -> None: ...
    PayItems: list
    SizeDataRecord: PartDataRecord
    PartStyleId: ObjectId
    RulesStyleId: ObjectId
    MaterialStyleId: ObjectId
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

class PartsList(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PartsList"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    PartFamilyCount: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def AddPartFamilyByDescription(self, domain: DomainType, description: str) -> None: ...
    def AddPartFamilyByGuid(self, domain: DomainType, guid: str) -> None: ...
    @staticmethod
    def GetAvailablePartFamilies(domain: DomainType) -> list: ...
    def GetPartFamilyIdsByDomain(self, domain: DomainType) -> ObjectIdCollection: ...
    def RemovePartFamily(self, partFamilyId: ObjectId) -> None: ...

class PartsListCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PartsListCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class PipeCenterlineType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeCenterlineType"""
    def __init__(self, *args) -> None: ...
    ...

class PipeCenterlineWidthType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeCenterlineWidthType"""
    def __init__(self, *args) -> None: ...
    ...

class PipeDisplayStylePlanType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeDisplayStylePlanType"""
    def __init__(self, *args) -> None: ...
    ...

class PipeDisplayStyleProfileType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeDisplayStyleProfileType"""
    def __init__(self, *args) -> None: ...
    ...

class PipeDisplayStyleSectionType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeDisplayStyleSectionType"""
    def __init__(self, *args) -> None: ...
    ...

class PipeEndSizeType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeEndSizeType"""
    def __init__(self, *args) -> None: ...
    ...

class PipeHatchStyleProfileType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeHatchStyleProfileType"""
    def __init__(self, *args) -> None: ...
    ...

class PipeHatchType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeHatchType"""
    def __init__(self, *args) -> None: ...
    ...

class PipeNetworkBandStyle(BandStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeNetworkBandStyle"""
    def __init__(self, *args) -> None: ...
    PipeTickStyle: BandTickStyle
    StructureTickStyle: BandTickStyle
    PipeLabelStyleId: ObjectId
    StructureLabelStyleId: ObjectId
    TitleTextLabelStyleId: ObjectId
    BandType: BandType
    WeedingFactor: float
    TextHeight: float
    TextLocation: BandTitleTextLocation
    TextBoxPosition: BandTitleBoxPosition
    OffsetFromBand: float
    TextBoxWidth: float
    BandHeight: float
    Text: str
    TextStyle: str
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStylePlan(self, type: PipeNetworkDisplayStyleType) -> DisplayStyle: ...

class PipeNetworkDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeNetworkDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class PipeRuleSetStyle(NetworkRuleSetStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeRuleSetStyle"""
    def __init__(self, *args) -> None: ...
    RulesCount: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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

class PipeRuleSetStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeRuleSetStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class PipeStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeStyle"""
    def __init__(self, *args) -> None: ...
    SectionCrossingHatch: PipeHatchType
    ProfileOption: PipeStyleProfileOption
    PlanOption: PipeStylePlanOption
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleModel(self, ) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, component: PipeDisplayStylePlanType) -> DisplayStyle: ...
    def GetDisplayStyleProfile(self, component: PipeDisplayStyleProfileType) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, component: PipeDisplayStyleSectionType) -> DisplayStyle: ...
    def GetHatchStylePlan(self, ) -> HatchDisplayStyle: ...
    def GetHatchStyleProfile(self, component: PipeHatchStyleProfileType) -> HatchDisplayStyle: ...
    def GetHatchStyleSection(self, ) -> HatchDisplayStyle: ...

class PipeStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class PipeStyleOptionBase(CivilWrapper<AeccDbPipeStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeStyleOptionBase"""
    def __init__(self, *args) -> None: ...
    PipeToPipeEndCleanup: bool
    AlignHatchToPipe: bool
    EndSizeOptions: PipeUserDefinedType
    WallSizeOptions: PipeUserDefinedType
    EndSizeType: PipeEndSizeType
    WallSizeType: PipeWallSizeType
    HatchOptions: PipeHatchType
    EndLineSizePercent: float
    EndLineSize: float
    OuterDiameterPercent: float
    OuterDiameter: float
    InnerDiameterPercent: float
    InnerDiameter: float

class PipeStylePlanOption(PipeStyleOptionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeStylePlanOption"""
    def __init__(self, *args) -> None: ...
    CenterlineOptions: PipeCenterlineType
    CenterlineWidthOptions: PipeCenterlineWidthType
    CenterlineSizePercent: float
    CenterlineSize: float
    PipeToPipeEndCleanup: bool
    AlignHatchToPipe: bool
    EndSizeOptions: PipeUserDefinedType
    WallSizeOptions: PipeUserDefinedType
    EndSizeType: PipeEndSizeType
    WallSizeType: PipeWallSizeType
    HatchOptions: PipeHatchType
    EndLineSizePercent: float
    EndLineSize: float
    OuterDiameterPercent: float
    OuterDiameter: float
    InnerDiameterPercent: float
    InnerDiameter: float

class PipeStyleProfileOption(PipeStyleOptionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeStyleProfileOption"""
    def __init__(self, *args) -> None: ...
    CrossingHatch: PipeHatchType
    PipeToPipeEndCleanup: bool
    AlignHatchToPipe: bool
    EndSizeOptions: PipeUserDefinedType
    WallSizeOptions: PipeUserDefinedType
    EndSizeType: PipeEndSizeType
    WallSizeType: PipeWallSizeType
    HatchOptions: PipeHatchType
    EndLineSizePercent: float
    EndLineSize: float
    OuterDiameterPercent: float
    OuterDiameter: float
    InnerDiameterPercent: float
    InnerDiameter: float

class PipeUserDefinedType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeUserDefinedType"""
    def __init__(self, *args) -> None: ...
    ...

class PipeWallSizeType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeWallSizeType"""
    def __init__(self, *args) -> None: ...
    ...

class PointCloudClassificationInfo:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PointCloudClassificationInfo"""
    def __init__(self, *args) -> None: ...
    LayerId: ObjectId
    Color: Color
    Selected: bool
    def Dispose(self, ) -> None: ...

class PointCloudClassificationInfoCollection:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PointCloudClassificationInfoCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: PointCloudClassificationInfo
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class PointCloudPointStyle:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PointCloudPointStyle"""
    def __init__(self, *args) -> None: ...
    ScaleFactor: float
    PointElevation: float
    Display3dType: PointDisplay3dType
    ElevationRangeInterval: float
    NumberOfElevationRanges: int
    RangesColorScheme: PointCloudRangeColorSchemeType
    ElevatinoRangeCreationType: PointCloudElevationRangeCreationType
    SingleColor: Color
    IntensityRangeMaximum: float
    IntensityRangeMinimum: float
    ScaledColorIntensityScheme: PointCloudRangeColorSchemeType
    PointsColorScheme: PointCouldColorSchemeType
    SizeInPixels: int

class PointCloudStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PointCloudStyle"""
    def __init__(self, *args) -> None: ...
    ClassificationInfos: PointCloudClassificationInfoCollection
    PointStyle: PointCloudPointStyle
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleModel(self, type: PointCloudDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: PointCloudDisplayStyleType) -> DisplayStyle: ...

class PointCloudStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PointCloudStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class PointDisplay3dType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PointDisplay3dType"""
    def __init__(self, *args) -> None: ...
    ...

class PointDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PointDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class PointMarkerDisplayType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PointMarkerDisplayType"""
    def __init__(self, *args) -> None: ...
    ...

class PointStyle(MarkerStyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PointStyle"""
    def __init__(self, *args) -> None: ...
    LabelDisplayStyleModel: DisplayStyle
    LabelDisplayStylePlan: DisplayStyle
    MarkerType: PointMarkerDisplayType
    ScaleFactor: float
    Elevation: float
    Display3dType: PointDisplay3dType
    MarkerDisplayStyleModel: DisplayStyle
    MarkerDisplayStylePlan: DisplayStyle
    Orientation: MarkerOrientationType
    MarkerFixedScale: Point3d
    MarkerSize: float
    SizeType: MarkerSizeType
    MarkerRotationAngle: float
    MarkerSymbolName: str
    CustomMarkerSuperimposeStyle: CustomMarkerSuperimposeType
    CustomMarkerStyle: CustomMarkerType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleModel(self, type: PointDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: PointDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStyleProfile(self, ) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, ) -> DisplayStyle: ...
    def GetLabelDisplayStyleModel(self, ) -> DisplayStyle: ...
    def GetLabelDisplayStylePlan(self, ) -> DisplayStyle: ...

class PointStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PointStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class PointSymbolType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PointSymbolType"""
    def __init__(self, *args) -> None: ...
    ...

class PrecisionRangeType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PrecisionRangeType"""
    def __init__(self, *args) -> None: ...
    ...

class ProfileDataBandStyle(BandStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileDataBandStyle"""
    def __init__(self, *args) -> None: ...
    StationEquationTickStyle: BandTickStyle
    VGPTickStyle: BandTickStyle
    HGPTickStyle: BandTickStyle
    MinorIncrementTickStyle: BandTickStyle
    MajorIncrementTickStyle: BandTickStyle
    IncrementalDistanceLabelStyleId: ObjectId
    StationEquationLabelStyleId: ObjectId
    VGPLabelStyleId: ObjectId
    HGPLabelStyleId: ObjectId
    MinorIncrementLabelStyleId: ObjectId
    MajorIncrementLabelStyleId: ObjectId
    TitleTextLabelStyleId: ObjectId
    BandType: BandType
    WeedingFactor: float
    TextHeight: float
    TextLocation: BandTitleTextLocation
    TextBoxPosition: BandTitleBoxPosition
    OffsetFromBand: float
    TextBoxWidth: float
    BandHeight: float
    Text: str
    TextStyle: str
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStylePlan(self, type: ProfileDataDisplayStyleType) -> DisplayStyle: ...

class ProfileDataDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileDataDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class ProfileDesignCheckCurveType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileDesignCheckCurveType"""
    def __init__(self, *args) -> None: ...
    ...

class ProfileDesignCheckSet(AlignmentDesignCheckSet):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileDesignCheckSet"""
    def __init__(self, *args) -> None: ...
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def AddDesignCheck(self, type: AlignmentDesignCheckType, name: str) -> AlignmentDesignCheck: ...
    def GetAllDesignChecks(self, ) -> list: ...
    def GetCurveDesignCheckType(self, name: str) -> ProfileDesignCheckCurveType: ...
    def RemoveAllDesignCheck(self, ) -> None: ...
    def RemoveDesignCheck(self, type: AlignmentDesignCheckType, name: str) -> None: ...
    def SetCurveDesignCheckType(self, name: str, type: ProfileDesignCheckCurveType) -> None: ...

class ProfileDesignCheckSetCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileDesignCheckSetCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class ProfileDisplayStyleProfileType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileDisplayStyleProfileType"""
    def __init__(self, *args) -> None: ...
    ...

class ProfileLabelSetItem(BaseLabelSetItem):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileLabelSetItem"""
    def __init__(self, *args) -> None: ...
    StaggerLabel: StaggerLabelType
    StaggerLineHeight2: float
    StaggerLineHeight1: float
    Weeding: float
    DimensionAnchorOption: DimensionAnchorType
    DimensionAnchorValue: float
    Increment: float
    LabelStyleName: str
    LabelStyleId: ObjectId
    LabelStyleType: LabelStyleType
    def GetLabeledAlignmentGeometryPoints(self, ) -> Dictionary: ...
    def SetLabeledAlignmentGeometryPoints(self, pointTypes: Dictionary) -> None: ...

class ProfileLabelSetStyle(BaseLabelSetStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileLabelSetStyle"""
    def __init__(self, *args) -> None: ...
    Item: ProfileLabelSetItem
    Count: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def AddCrestCurve(self, labelStyleId: ObjectId) -> None: ...
    def AddSagCurve(self, labelStyleId: ObjectId) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class ProfileLabelSetStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileLabelSetStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class ProfileStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileStyle"""
    def __init__(self, *args) -> None: ...
    ArrowHeadOption: ArrowHeadOption
    ProfileMarkerDisplayStyleSection: DisplayStyle
    Chain3DDisplayStyleModel: DisplayStyle
    ProfileMarkerSectionViewMarkerStyle: ObjectId
    LowPointMarkerStyle: ObjectId
    HighPointMarkerStyle: ObjectId
    VCurveTangentIntersectPointMarkerStyle: ObjectId
    VReverseCurveIntersectPointMarkerStyle: ObjectId
    VCompoundCurveIntersectPointMarkerStyle: ObjectId
    VTangentCurveIntersectPointMarkerStyle: ObjectId
    EndPointMarkerStyle: ObjectId
    BeginPointMarkerStyle: ObjectId
    VIntersectionPointMarkerStyle: ObjectId
    ThroughPointMarkerStyle: ObjectId
    ChainTessellationDistance3D: float
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetChain3DDisplayStyleModel(self, ) -> DisplayStyle: ...
    def GetDisplayStyleProfile(self, type: ProfileDisplayStyleProfileType) -> DisplayStyle: ...
    def GetProfileMarkerDisplayStyleSection(self, ) -> DisplayStyle: ...

class ProfileStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class ProfileViewBandSetItem(BandSetItem):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileViewBandSetItem"""
    def __init__(self, *args) -> None: ...
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
    def GetHorizontalGeometryPointsOptions(self, ) -> GeometryPointSelector: ...
    def GetVerticalGeometryPointsOptions(self, ) -> GeometryPointSelector: ...
    def SetHorizontalGeometryPointsOptions(self, alignmentGeometryPoints: GeometryPointSelector) -> None: ...
    def SetVerticalGeometryPointsOptions(self, alignmentVerticalGeometryPoints: GeometryPointSelector) -> None: ...

class ProfileViewBandSetItemCollection(BandSetItemCollection):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileViewBandSetItemCollection"""
    def __init__(self, *args) -> None: ...
    Item: ProfileViewBandSetItem
    Count: int
    Location: BandLocationType
    def Add(self, database: Database, bandType: BandType, profileBandStyleName: str) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class ProfileViewBandSetStyle(BandSetStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileViewBandSetStyle"""
    def __init__(self, *args) -> None: ...
    MatchIncrementToGridIntervals: bool
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetBottomBandSetItems(self, ) -> ProfileViewBandSetItemCollection: ...
    def GetTopBandSetItems(self, ) -> ProfileViewBandSetItemCollection: ...
    def SetBottomBandSetItems(self, bandSetItems: ProfileViewBandSetItemCollection) -> None: ...
    def SetTopBandSetItems(self, bandSetItems: ProfileViewBandSetItemCollection) -> None: ...

class ProfileViewBandSetStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileViewBandSetStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class ProfileViewDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileViewDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class ProfileViewStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileViewStyle"""
    def __init__(self, *args) -> None: ...
    RightAxis: AxisStyle
    LeftAxis: AxisStyle
    BottomAxis: AxisStyle
    TopAxis: AxisStyle
    GridStyle: GridStyle
    GraphStyle: GraphStyle
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStylePlan(self, type: ProfileViewDisplayStyleType) -> DisplayStyle: ...

class ProfileViewStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileViewStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class ProjectionBlockDisplayType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProjectionBlockDisplayType"""
    def __init__(self, *args) -> None: ...
    ...

class ProjectionDisplayStyleProfileType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProjectionDisplayStyleProfileType"""
    def __init__(self, *args) -> None: ...
    ...

class ProjectionDisplayStyleSectionType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProjectionDisplayStyleSectionType"""
    def __init__(self, *args) -> None: ...
    ...

class ProjectionEntityDisplayType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProjectionEntityDisplayType"""
    def __init__(self, *args) -> None: ...
    ...

class ProjectionProfileOptions(CivilWrapper<AeccDbProfileSectionEntityStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProjectionProfileOptions"""
    def __init__(self, *args) -> None: ...
    VerticallyExaggerateMultiViewBlocks: bool
    MultiViewBlockSymbolBlockName: str
    MultiViewBlockSymbolBlockId: ObjectId
    MultiViewBlockDirection: ViewDirection
    MultiViewBlockDisplayRepresentationName: str
    MultiViewBlockDisplayRepresentationId: ObjectId
    MultiViewBlockMarkerStyleName: str
    MultiViewBlockMarkerStyleId: ObjectId
    MultiViewBlockDisplayOptions: ProjectionBlockDisplayType
    VerticallyExaggerateBlocks: bool
    AutoCADBlockSymbolBlockName: str
    AutoCADBlockSymbolBlockId: ObjectId
    AutoCADBlockMarkerStyleName: str
    AutoCADBlockMarkerStyleId: ObjectId
    AutoCADBlockDisplayOptions: ProjectionBlockDisplayType
    AutoCAD3dPolylineEndVertexMarkerStyleName: str
    AutoCAD3dPolylineEndVertexMarkerStyleId: ObjectId
    AutoCAD3dPolylineInternalVertexMarkerStyleName: str
    AutoCAD3dPolylineInternalVertexMarkerStyleId: ObjectId
    AutoCAD3dPolylineBeginVertexMarkerStyleName: str
    AutoCAD3dPolylineBeginVertexMarkerStyleId: ObjectId
    VerticallyExaggerateSolids: bool
    AutoCADSolidMarkerStyleName: str
    AutoCADSolidMarkerStyleId: ObjectId
    AutoCADSolidDisplayOptions: ProjectionEntityDisplayType
    AutoCADPointMarkerStyleName: str
    AutoCADPointMarkerStyleId: ObjectId
    AutoCADPointDisplayOptions: ProjectionEntityDisplayType

class ProjectionSectionOptions(CivilWrapper<AeccDbProfileSectionEntityStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProjectionSectionOptions"""
    def __init__(self, *args) -> None: ...
    VerticallyExaggerateMultiViewBlocks: bool
    MultiViewBlockSymbolBlockName: str
    MultiViewBlockSymbolBlockId: ObjectId
    MultiViewBlockDirection: ViewDirection
    MultiViewBlockDisplayRepresentationName: str
    MultiViewBlockDisplayRepresentationId: ObjectId
    MultiViewBlockMarkerStyleName: str
    MultiViewBlockMarkerStyleId: ObjectId
    MultiViewBlockDisplayOptions: ProjectionBlockDisplayType
    VerticallyExaggerateBlocks: bool
    AutoCADBlockSymbolBlockName: str
    AutoCADBlockSymbolBlockId: ObjectId
    AutoCADBlockMarkerStyleName: str
    AutoCADBlockMarkerStyleId: ObjectId
    AutoCADBlockDisplayOptions: ProjectionBlockDisplayType
    AutoCAD3dPolylineCrossingMarkerStyleName: str
    AutoCAD3dPolylineCrossingMarkerStyleId: ObjectId
    VerticallyExaggerateSolids: bool
    AutoCADSolidMarkerStyleName: str
    AutoCADSolidMarkerStyleId: ObjectId
    AutoCADSolidDisplayAsTrueSection: bool
    AutoCADSolidDisplayOptions: ProjectionEntityDisplayType
    AutoCADPointMarkerStyleName: str
    AutoCADPointMarkerStyleId: ObjectId
    AutoCADPointDisplayOptions: ProjectionEntityDisplayType

class ProjectionStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProjectionStyle"""
    def __init__(self, *args) -> None: ...
    SectionOptions: ProjectionSectionOptions
    ProfileOptions: ProjectionProfileOptions
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleProfile(self, type: ProjectionDisplayStyleProfileType) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, type: ProjectionDisplayStyleSectionType) -> DisplayStyle: ...

class ProjectionStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProjectionStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class QuantityTakeoffCriteria(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.QuantityTakeoffCriteria"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: QuantityTakeoffCriteriaItem
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def AddMaterial(self, materialName: str) -> None: ...
    def Clear(self, ) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class QuantityTakeoffCriteriaCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.QuantityTakeoffCriteriaCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class QuantityTakeoffCriteriaData(CivilWrapper<AeccDbQuantityTakeoffCriteria>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.QuantityTakeoffCriteriaData"""
    def __init__(self, *args) -> None: ...
    ItemType: MaterialItemType
    Condition: MaterialConditionType
    Name: str

class QuantityTakeoffCriteriaItem(CivilWrapper<AeccDbQuantityTakeoffCriteria>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.QuantityTakeoffCriteriaItem"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: QuantityTakeoffCriteriaData
    ShapeStyleName: str
    ShapeStyleId: ObjectId
    ReFillFactor: float
    FillFactor: float
    CutFactor: float
    QuantityType: MaterialQuantityType
    MaterialName: str
    def AddCorridorShape(self, shapeName: str) -> None: ...
    def AddSurface(self, surfaceName: str) -> None: ...
    def RemoveCorridorShape(self, shapeName: str) -> None: ...
    def RemoveSurface(self, surfaceName: str) -> None: ...

class ReferenceTextComponentSelectedType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ReferenceTextComponentSelectedType"""
    def __init__(self, *args) -> None: ...
    ...

class SampleLineDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SampleLineDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class SampleLineStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SampleLineStyle"""
    def __init__(self, *args) -> None: ...
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleModel(self, type: SampleLineDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: SampleLineDisplayStyleType) -> DisplayStyle: ...

class SampleLineStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SampleLineStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class ScaleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ScaleType"""
    def __init__(self, *args) -> None: ...
    ...

class ScalingMethodType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ScalingMethodType"""
    def __init__(self, *args) -> None: ...
    ...

class SchematicLineOption:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SchematicLineOption"""
    def __init__(self, *args) -> None: ...
    ...

class SectionDataBandStyle(BandStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionDataBandStyle"""
    def __init__(self, *args) -> None: ...
    GradeBreaksTickStyle: BandTickStyle
    SampleLineVerticesTickStyle: BandTickStyle
    CenterlineTickStyle: BandTickStyle
    MinorIncrementTickStyle: BandTickStyle
    MajorIncrementTickStyle: BandTickStyle
    IncrementalDistanceLabelStyleId: ObjectId
    GradeBreaksLabelStyleId: ObjectId
    SampleLineVerticesLabelStyleId: ObjectId
    CenterlineLabelStyleId: ObjectId
    MinorIncrementLabelStyleId: ObjectId
    MajorIncrementLabelStyleId: ObjectId
    TitleTextLabelStyleId: ObjectId
    BandType: BandType
    WeedingFactor: float
    TextHeight: float
    TextLocation: BandTitleTextLocation
    TextBoxPosition: BandTitleBoxPosition
    OffsetFromBand: float
    TextBoxWidth: float
    BandHeight: float
    Text: str
    TextStyle: str
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStylePlan(self, type: SectionDataDisplayStyleType) -> DisplayStyle: ...

class SectionDataDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionDataDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class SectionDisplayStyleSectionType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionDisplayStyleSectionType"""
    def __init__(self, *args) -> None: ...
    ...

class SectionLabelSetItem(BaseLabelSetItem):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionLabelSetItem"""
    def __init__(self, *args) -> None: ...
    StaggerLabel: StaggerLabelType
    StaggerLineHeight2: float
    StaggerLineHeight1: float
    Weeding: float
    DimensionAnchorOption: DimensionAnchorType
    DimensionAnchorValue: float
    Increment: float
    LabelStyleName: str
    LabelStyleId: ObjectId
    LabelStyleType: LabelStyleType

class SectionLabelSetStyle(BaseLabelSetStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionLabelSetStyle"""
    def __init__(self, *args) -> None: ...
    Item: SectionLabelSetItem
    Count: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class SectionLabelSetStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionLabelSetStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class SectionSegmentBandStyle(BandStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionSegmentBandStyle"""
    def __init__(self, *args) -> None: ...
    SegmentLabelsTickStyle: BandTickStyle
    SegmentsLabelStyleId: ObjectId
    TitleTextLabelStyleId: ObjectId
    BandType: BandType
    WeedingFactor: float
    TextHeight: float
    TextLocation: BandTitleTextLocation
    TextBoxPosition: BandTitleBoxPosition
    OffsetFromBand: float
    TextBoxWidth: float
    BandHeight: float
    Text: str
    TextStyle: str
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStylePlan(self, type: SectionSegmentDisplayStyleType) -> DisplayStyle: ...

class SectionSegmentDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionSegmentDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class SectionStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionStyle"""
    def __init__(self, *args) -> None: ...
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleSection(self, type: SectionDisplayStyleSectionType) -> DisplayStyle: ...

class SectionStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class SectionViewBandSetItem(BandSetItem):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionViewBandSetItem"""
    def __init__(self, *args) -> None: ...
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

class SectionViewBandSetItemCollection(BandSetItemCollection):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionViewBandSetItemCollection"""
    def __init__(self, *args) -> None: ...
    Item: SectionViewBandSetItem
    Count: int
    Location: BandLocationType
    def Add(self, database: Database, bandType: BandType, sectionBandStyleName: str) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class SectionViewBandSetStyle(BandSetStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionViewBandSetStyle"""
    def __init__(self, *args) -> None: ...
    MatchIncrementToGridIntervals: bool
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetBottomBandSetItems(self, ) -> SectionViewBandSetItemCollection: ...
    def GetTopBandSetItems(self, ) -> SectionViewBandSetItemCollection: ...
    def SetBottomBandSetItems(self, bandSetItems: SectionViewBandSetItemCollection) -> None: ...
    def SetTopBandSetItems(self, bandSetItems: SectionViewBandSetItemCollection) -> None: ...

class SectionViewBandSetStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionViewBandSetStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class SectionViewDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionViewDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class SectionViewPlotRuleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionViewPlotRuleType"""
    def __init__(self, *args) -> None: ...
    ...

class SectionViewStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionViewStyle"""
    def __init__(self, *args) -> None: ...
    RightAxis: AxisStyle
    CenterAxis: AxisStyle
    LeftAxis: AxisStyle
    BottomAxis: AxisStyle
    TopAxis: AxisStyle
    GridStyle: GridStyle
    GraphStyle: GraphStyle
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStylePlan(self, type: SectionViewDisplayStyleType) -> DisplayStyle: ...

class SectionViewStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionViewStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class SectionalDataBandStyle(BandStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionalDataBandStyle"""
    def __init__(self, *args) -> None: ...
    IncrementalSectionDataTickStyle: BandTickStyle
    SampleLineStationTickStyle: BandTickStyle
    IncrementalSectionDataLabelStyleId: ObjectId
    SampleLineStationLabelStyleId: ObjectId
    TitleTextLabelStyleId: ObjectId
    BandType: BandType
    WeedingFactor: float
    TextHeight: float
    TextLocation: BandTitleTextLocation
    TextBoxPosition: BandTitleBoxPosition
    OffsetFromBand: float
    TextBoxWidth: float
    BandHeight: float
    Text: str
    TextStyle: str
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStylePlan(self, type: SectionalDataDisplayStyleType) -> DisplayStyle: ...

class SectionalDataDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionalDataDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class SegmentColumnStyle(ColumnStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SegmentColumnStyle"""
    def __init__(self, *args) -> None: ...
    ContentJustification: TextJustificationType
    ContentStringFormatted: str
    ContentString: str
    HeaderJustification: TextJustificationType
    HeaderStringFormatted: str
    HeaderString: str
    ColumnWidth: float
    def GetContentString(self, type: TableSegmentDataType) -> str: ...
    def GetContentStringFormatted(self, type: TableSegmentDataType) -> str: ...
    def SetContentString(self, type: TableSegmentDataType, newVal: str) -> None: ...
    def SetContentStringFormatted(self, type: TableSegmentDataType, newVal: str) -> None: ...

class ShapeDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ShapeDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class ShapeStyle(SubassemblySubentityStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ShapeStyle"""
    def __init__(self, *args) -> None: ...
    AreaFillHatchDisplayStyleModel: HatchDisplayStyle
    AreaFillHatchDisplayStylePlan: HatchDisplayStyle
    StyleType: SubassemblySubentityStyleType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleModel(self, type: ShapeDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: ShapeDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStyleProfile(self, type: ShapeDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, type: ShapeDisplayStyleType) -> DisplayStyle: ...
    def GetHatchDisplayStyleModel(self, ) -> HatchDisplayStyle: ...
    def GetHatchDisplayStylePlan(self, ) -> HatchDisplayStyle: ...
    def GetHatchDisplayStyleProfile(self, ) -> HatchDisplayStyle: ...
    def GetHatchDisplayStyleSection(self, ) -> HatchDisplayStyle: ...

class ShapeStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ShapeStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class SheetDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SheetDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class SheetStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SheetStyle"""
    def __init__(self, *args) -> None: ...
    PageMarginRight: float
    PageMarginLeft: float
    PageMarginBottom: float
    PageMarginTop: float
    PageLayoutId: ObjectId
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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

class SheetStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SheetStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class SizeFilterField(PartDataField):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SizeFilterField"""
    def __init__(self, *args) -> None: ...
    DataSource: PartDataSourceType
    IsMultipleSelect: bool
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

class SizeFilterRecord:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SizeFilterRecord"""
    def __init__(self, *args) -> None: ...
    PartFamilyGuid: str
    Item: SizeFilterField
    Item: SizeFilterField
    ParamCount: int
    def Dispose(self, ) -> None: ...
    def GetParamByContextAndIndex(self, context: PartContextType, index: int) -> SizeFilterField: ...

class SlopeArrowType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SlopeArrowType"""
    def __init__(self, *args) -> None: ...
    ...

class SlopePatternComponent(CivilWrapper<AeccDbSlopePatternStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SlopePatternComponent"""
    def __init__(self, *args) -> None: ...
    SlopeLineSymbol: SlopePatternLineSymbol
    SlopeLineOffset: SlopePatternLineOffset
    SlopeLine: SlopePatternLine

class SlopePatternLine(CivilWrapper<AeccDbSlopePatternStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SlopePatternLine"""
    def __init__(self, *args) -> None: ...
    Color: Color
    LineWeight: LineWeight
    Linetype: str
    Grade2: float
    Grade1: float
    PercentofLength2: float
    PercentofLength1: float
    Length: float
    MaximumLength: float
    PercentofLength: float
    LengthType: SlopePatternLengthType
    StartType: SlopePatternStartType

class SlopePatternLineOffset(CivilWrapper<AeccDbSlopePatternStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SlopePatternLineOffset"""
    def __init__(self, *args) -> None: ...
    Numberoflines: int
    Distance: float
    RadialOffsetAngle: float
    MaximumDistance: float
    MinimumDistance: float
    PercentofLength: float
    OffsetType: SlopePatternOffsetType

class SlopePatternLineSymbol(CivilWrapper<AeccDbSlopePatternStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SlopePatternLineSymbol"""
    def __init__(self, *args) -> None: ...
    Numberoflines: int
    Color: Color
    LineWeight: LineWeight
    Linetype: str
    WidthRatio: float
    Length: float
    PercentofLength: float
    LengthType: SlopePatternLengthType
    BlockName: str
    SymbolType: SlopePatternSymbolType

class SlopePatternStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SlopePatternStyle"""
    def __init__(self, *args) -> None: ...
    PreviewSlope: float
    PreviewSlopeLength: float
    PreviewFeatureLength: float
    MinDisplayLength: float
    Count: int
    Item: SlopePatternComponent
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def AddComponent(self, position: int) -> None: ...
    def CopyComponent(self, index: int, insertPosition: int) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class SlopePatternStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SlopePatternStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class StaggerLabelType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StaggerLabelType"""
    def __init__(self, *args) -> None: ...
    ...

class StructureColumnComponentData(CivilWrapper<tableCellComponentVec>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureColumnComponentData"""
    def __init__(self, *args) -> None: ...
    ComponentType: StructureColumnComponentType
    Content: str
    Name: str

class StructureColumnComponents(CivilWrapper<tableCellComponentVec>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureColumnComponents"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: StructureColumnComponentData
    def AddComponent(self, name: str, componentType: StructureColumnComponentType) -> None: ...
    def Clear(self, ) -> None: ...
    def RemoveAt(self, name: str) -> None: ...
    def SwitchComponentsOrder(self, index1: int, index2: int) -> None: ...

class StructureColumnStyle(ColumnStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureColumnStyle"""
    def __init__(self, *args) -> None: ...
    ContentJustification: TextJustificationType
    ContentStringFormatted: str
    ContentString: str
    HeaderJustification: TextJustificationType
    HeaderStringFormatted: str
    HeaderString: str
    ColumnWidth: float
    def GetComponents(self, ) -> StructureColumnComponents: ...
    def SetComponents(self, componentDatas: StructureColumnComponents) -> None: ...

class StructureDisplayStylePlanType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureDisplayStylePlanType"""
    def __init__(self, *args) -> None: ...
    ...

class StructureDisplayStyleProfileType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureDisplayStyleProfileType"""
    def __init__(self, *args) -> None: ...
    ...

class StructureDisplayStyleSectionType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureDisplayStyleSectionType"""
    def __init__(self, *args) -> None: ...
    ...

class StructureInsertionLocation:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureInsertionLocation"""
    def __init__(self, *args) -> None: ...
    ...

class StructureModelViewOptionType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureModelViewOptionType"""
    def __init__(self, *args) -> None: ...
    ...

class StructurePlanViewType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructurePlanViewType"""
    def __init__(self, *args) -> None: ...
    ...

class StructureRuleSetStyle(NetworkRuleSetStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureRuleSetStyle"""
    def __init__(self, *args) -> None: ...
    RulesCount: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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

class StructureRuleSetStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureRuleSetStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class StructureSimpleSolidType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureSimpleSolidType"""
    def __init__(self, *args) -> None: ...
    ...

class StructureSizeOptionsType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureSizeOptionsType"""
    def __init__(self, *args) -> None: ...
    ...

class StructureStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureStyle"""
    def __init__(self, *args) -> None: ...
    SectionOption: StructureStyleSectionOption
    ModelOption: StructureStyleModelOption
    ProfileOption: StructureStyleProfileOption
    PlanOption: StructureStylePlanOption
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleModel(self, ) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, component: StructureDisplayStylePlanType) -> DisplayStyle: ...
    def GetDisplayStyleProfile(self, component: StructureDisplayStyleProfileType) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, component: StructureDisplayStyleSectionType) -> DisplayStyle: ...
    def GetHatchStylePlan(self, ) -> HatchDisplayStyle: ...
    def GetHatchStyleProfile(self, ) -> HatchDisplayStyle: ...
    def GetHatchStyleSection(self, ) -> HatchDisplayStyle: ...

class StructureStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class StructureStyleModelOption(CivilWrapper<AeccDbStructureStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureStyleModelOption"""
    def __init__(self, *args) -> None: ...
    SimpleSolidType: StructureSimpleSolidType
    ModelViewOptions: StructureModelViewOptionType

class StructureStyleOptionBase(CivilWrapper<AeccDbStructureStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureStyleOptionBase"""
    def __init__(self, *args) -> None: ...
    MaskConnectedObjects: bool
    YSizePercent: float
    YSize: float
    XSizePercent: float
    XSize: float
    SymbolBlockZScale: float
    SymbolBlockYScale: float
    SymbolBlockXScale: float
    SymbolBlockName: str
    BlockInsertLocation: StructureInsertionLocation
    SizeType: StructureSizeOptionsType
    ViewOptions: StructureViewType

class StructureStylePlanOption(CivilWrapper<AeccDbStructureStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureStylePlanOption"""
    def __init__(self, *args) -> None: ...
    SizePercent: float
    Size: float
    MaskConnectedObjects: bool
    SymbolBlockZScale: float
    SymbolBlockYScale: float
    SymbolBlockXScale: float
    SymbolBlockName: str
    SizeType: StructureSizeOptionsType
    PlanViewOptions: StructurePlanViewType

class StructureStyleProfileOption(StructureStyleOptionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureStyleProfileOption"""
    def __init__(self, *args) -> None: ...
    MaskConnectedObjects: bool
    YSizePercent: float
    YSize: float
    XSizePercent: float
    XSize: float
    SymbolBlockZScale: float
    SymbolBlockYScale: float
    SymbolBlockXScale: float
    SymbolBlockName: str
    BlockInsertLocation: StructureInsertionLocation
    SizeType: StructureSizeOptionsType
    ViewOptions: StructureViewType

class StructureStyleSectionOption(StructureStyleOptionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureStyleSectionOption"""
    def __init__(self, *args) -> None: ...
    MaskConnectedObjects: bool
    YSizePercent: float
    YSize: float
    XSizePercent: float
    XSize: float
    SymbolBlockZScale: float
    SymbolBlockYScale: float
    SymbolBlockXScale: float
    SymbolBlockName: str
    BlockInsertLocation: StructureInsertionLocation
    SizeType: StructureSizeOptionsType
    ViewOptions: StructureViewType

class StructureViewType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureViewType"""
    def __init__(self, *args) -> None: ...
    ...

class StyleBase(DBObject):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StyleBase"""
    def __init__(self, *args) -> None: ...
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def CopyAsSibling(self, styleName: str) -> ObjectId: ...
    @staticmethod
    def ExportTo(styleIds: ObjectIdCollection, destinationDatabase: Database, conflictResolution: StyleConflictResolverType) -> None: ...

class StyleCollectionBase(TreeNodeCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StyleCollectionBase"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...
    def Remove(self, style: StyleBase) -> None: ...

class StylesRoot(TreeOidWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StylesRoot"""
    def __init__(self, *args) -> None: ...
    ProfileDesignCheckSets: ProfileDesignCheckSetCollection
    AlignmentDesignCheckSets: AlignmentDesignCheckSetCollection
    ProjectionStyles: ProjectionStyleCollection
    SurveyNetworkStyles: SurveyNetworkStyleCollection
    SurveyFigureStyles: SurveyFigureStyleCollection
    QuantityTakeoffCriterias: QuantityTakeoffCriteriaCollection
    IntersectionStyles: IntersectionStyleCollection
    CorridorStyles: CorridorStyleCollection
    AssemblyStyles: AssemblyStyleCollection
    CodeSetStyles: CodeSetStyleCollection
    ShapeStyles: ShapeStyleCollection
    LinkStyles: LinkStyleCollection
    PartsListSet: PartsListCollection
    StructureRuleSetStyles: StructureRuleSetStyleCollection
    PipeRuleSetStyles: PipeRuleSetStyleCollection
    InterferenceStyles: InterferenceStyleCollection
    StructureStyles: StructureStyleCollection
    PipeStyles: PipeStyleCollection
    CatchmentStyles: CatchmentStyleCollection
    CantViewStyles: CantViewStyleCollection
    SuperelevationViewStyles: SuperelevationViewStyleCollection
    PointCloudStyles: PointCloudStyleCollection
    GradingCriteriaSets: GradingCriteriaSetCollection
    BuildingSiteStyles: BuildingSiteStyleCollection
    SlopePatternStyles: SlopePatternStyleCollection
    MassHaulViewStyles: MassHaulViewStyleCollection
    MassHaulLineStyles: MassHaulLineStyleCollection
    SectionViewBandSetStyles: SectionViewBandSetStyleCollection
    ProfileViewBandSetStyles: ProfileViewBandSetStyleCollection
    ProfileViewStyles: ProfileViewStyleCollection
    ProfileStyles: ProfileStyleCollection
    ViewFrameStyles: ViewFrameStyleCollection
    SheetStyles: SheetStyleCollection
    MatchLineStyles: MatchLineStyleCollection
    GroupPlotStyles: GroupPlotStyleCollection
    GradingStyles: GradingStyleCollection
    FeatureLineStyles: FeatureLineStyleCollection
    SurfaceStyles: SurfaceStyleCollection
    SectionViewStyles: SectionViewStyleCollection
    SectionStyles: SectionStyleCollection
    SampleLineStyles: SampleLineStyleCollection
    PointStyles: PointStyleCollection
    ParcelStyles: ParcelStyleCollection
    AlignmentStyles: AlignmentStyleCollection
    MarkerStyles: MarkerStyleCollection
    BandStyles: BandStylesRoot
    LabelSetStyles: LabelSetStylesRoot
    LabelStyles: LabelStylesRoot
    TableStyles: TableStylesRoot
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SubassemblySubentityStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SubassemblySubentityStyle"""
    def __init__(self, *args) -> None: ...
    StyleType: SubassemblySubentityStyleType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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

class SubassemblySubentityStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SubassemblySubentityStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class SuperelevationDataBandStyle(BandStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SuperelevationDataBandStyle"""
    def __init__(self, *args) -> None: ...
    SlopeTransitionRegionTickStyle: BandTickStyle
    ShoulderCriticalPointsTickStyle: BandTickStyle
    FullSuperTickStyle: BandTickStyle
    ReverseCrownTickStyle: BandTickStyle
    LevelCrownTickStyle: BandTickStyle
    NormalCrownTickStyle: BandTickStyle
    SlopeTransitionRegionLabelStyleId: ObjectId
    ShoulderCriticalPointsLabelStyleId: ObjectId
    FullSuperLabelStyleId: ObjectId
    ReverseCrownLabelStyleId: ObjectId
    LevelCrownLabelStyleId: ObjectId
    NormalCrownLabelStyleId: ObjectId
    TitleTextLabelStyleId: ObjectId
    BandType: BandType
    WeedingFactor: float
    TextHeight: float
    TextLocation: BandTitleTextLocation
    TextBoxPosition: BandTitleBoxPosition
    OffsetFromBand: float
    TextBoxWidth: float
    BandHeight: float
    Text: str
    TextStyle: str
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStylePlan(self, type: SuperelevationDataDisplayStyleType) -> DisplayStyle: ...

class SuperelevationDataDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SuperelevationDataDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class SuperelevationViewStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SuperelevationViewStyle"""
    def __init__(self, *args) -> None: ...
    UseSmallTicksAtBottom: bool
    UseSmallTicksAtMiddle: bool
    UseSmallTicksAtTop: bool
    UseFullHeightTick: bool
    AxisBottomMajorTickInterval: float
    AxisTopMajorTickInterval: float
    VerticalUnitHeight: float
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStylePlan(self, type: SuperElevationViewDisplayStyleType) -> DisplayStyle: ...

class SuperelevationViewStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SuperelevationViewStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class SurfaceBaseStyle(CivilWrapper<AeccDbSurfaceStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceBaseStyle"""
    def __init__(self, *args) -> None: ...
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurfaceBoundaryStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceBoundaryStyle"""
    def __init__(self, *args) -> None: ...
    DatumElevation: float
    ProjectGridToDatum: bool
    UseDatum: bool
    DisplayInteriorBoundaries: bool
    DisplayExteriorBoundaries: bool
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurfaceContourStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceContourStyle"""
    def __init__(self, *args) -> None: ...
    SmoothingFactor: int
    SmoothingType: ContourSmoothingType
    SmoothContours: bool
    DepressionTickMarkLength: float
    DepressionTickMarkInterval: float
    DisplayDepressions: bool
    MinorContourColorScheme: ColorSchemeType
    MajorContourColorScheme: ColorSchemeType
    UseColorScheme: bool
    RangePrecision: PrecisionRangeType
    NumberOfRanges: int
    GroupRangeValuesBy: SurfaceGroupValuesByType
    MinorContourInterval: float
    MajorContourInterval: float
    BaseElevationInterval: float
    LegendStyleId: ObjectId
    LegendStyleName: str
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType
    def GetContourValues(self, ) -> list: ...
    def SetContourValues(self, contourValuesArray: list) -> None: ...

class SurfaceDirectionStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceDirectionStyle"""
    def __init__(self, *args) -> None: ...
    LegendStyleId: ObjectId
    LegendStyleName: str
    ColorScheme: ColorSchemeType
    DisplayEntityMode: SurfaceDisplayType
    RangePrecision: PrecisionRangeType
    NumberOfRanges: int
    GroupValuesBy: SurfaceGroupValuesByType
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurfaceDisplay3dType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceDisplay3dType"""
    def __init__(self, *args) -> None: ...
    ...

class SurfaceDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class SurfaceDisplayType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceDisplayType"""
    def __init__(self, *args) -> None: ...
    ...

class SurfaceElevationStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceElevationStyle"""
    def __init__(self, *args) -> None: ...
    IntervalLength: float
    DataBandingMode: DataBandingType
    LegendStyleId: ObjectId
    LegendStyleName: str
    FillScheme: ColorSchemeType
    CutScheme: ColorSchemeType
    ColorScheme: ColorSchemeType
    DisplayEntityMode: SurfaceDisplayType
    RangePrecision: PrecisionRangeType
    NumberOfRanges: int
    GroupValuesBy: SurfaceGroupValuesByType
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurfaceGridStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceGridStyle"""
    def __init__(self, *args) -> None: ...
    SecondaryGridOrientation: float
    SecondaryGridInterval: float
    UseSecondaryGrid: bool
    PrimaryGridOrientation: float
    PrimaryGridInterval: float
    UsePrimaryGrid: bool
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurfaceGroupValuesByType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceGroupValuesByType"""
    def __init__(self, *args) -> None: ...
    ...

class SurfaceHatchInfo:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceHatchInfo"""
    def __init__(self, *args) -> None: ...
    PatternDouble: bool
    PatternSpace: float
    PatternAngle: float
    PatternScaleType: bool
    PatternScale: float
    PatternName: str
    PatternType: HatchPatternType
    def SetHatchPattern(self, patternType: HatchPatternType, patternName: str) -> None: ...

class SurfacePointStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfacePointStyle"""
    def __init__(self, *args) -> None: ...
    NondestructivePointsColor: Color
    NondestructivePointsSymbol: PointSymbolType
    DerivedPointsColor: Color
    DerivedPointsSymbol: PointSymbolType
    DataPointsColor: Color
    DataPointsSymbol: PointSymbolType
    Units: float
    ScalingMethodType: ScaleType
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurfaceSlopeArrowStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceSlopeArrowStyle"""
    def __init__(self, *args) -> None: ...
    LegendStyleName: str
    LegendStyleId: ObjectId
    ColorScheme: ColorSchemeType
    ArrowScale: float
    ArrowType: SlopeArrowType
    RangePrecision: PrecisionRangeType
    NumberOfRanges: int
    GroupValuesBy: SurfaceGroupValuesByType
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurfaceSlopeStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceSlopeStyle"""
    def __init__(self, *args) -> None: ...
    LegendStyleName: str
    LegendStyleId: ObjectId
    ColorScheme: ColorSchemeType
    RangePrecision: PrecisionRangeType
    NumberOfRanges: int
    GroupValuesBy: SurfaceGroupValuesByType
    DisplayEntityMode: SurfaceDisplayType
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurfaceStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceStyle"""
    def __init__(self, *args) -> None: ...
    TriangleStyle: SurfaceTriangleStyle
    WatershedStyle: SurfaceWatershedStyle
    SlopeStyle: SurfaceSlopeStyle
    SlopeArrowStyle: SurfaceSlopeArrowStyle
    PointStyle: SurfacePointStyle
    GridStyle: SurfaceGridStyle
    ElevationStyle: SurfaceElevationStyle
    DirectionStyle: SurfaceDirectionStyle
    ContourStyle: SurfaceContourStyle
    BoundaryStyle: SurfaceBoundaryStyle
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleModel(self, type: SurfaceDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: SurfaceDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, ) -> DisplayStyle: ...

class SurfaceStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class SurfaceTriangleStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceTriangleStyle"""
    def __init__(self, *args) -> None: ...
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurfaceWatershedStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceWatershedStyle"""
    def __init__(self, *args) -> None: ...
    MultipleDrainNotchStyle: WatershedMultipleDrainNotchStyle
    MultipleDrainStyle: WatershedMultipleDrainStyle
    FlatAreaStyle: WatershedFlatAreaStyle
    DepressionStyle: WatershedDepressionStyle
    BoundarySegmentStyle: WatershedBoundarySegmentStyle
    BoundaryPointStyle: WatershedBoundaryPointStyle
    LabelStyleId: ObjectId
    LabelStyleName: str
    LegendStyleId: ObjectId
    LegendStyleName: str
    PointScalingMethod: ScalingMethodType
    PointUnits: float
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurveyElevationDisplayType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurveyElevationDisplayType"""
    def __init__(self, *args) -> None: ...
    ...

class SurveyFigureDisplayType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureDisplayType"""
    def __init__(self, *args) -> None: ...
    ...

class SurveyFigureMarkerPlacementType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureMarkerPlacementType"""
    def __init__(self, *args) -> None: ...
    ...

class SurveyFigureProfileDisplayType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureProfileDisplayType"""
    def __init__(self, *args) -> None: ...
    ...

class SurveyFigureSectionDisplayType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureSectionDisplayType"""
    def __init__(self, *args) -> None: ...
    ...

class SurveyFigureStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureStyle"""
    def __init__(self, *args) -> None: ...
    CrossingMarkerStyleId: ObjectId
    EndingVertexMarkerStyleId: ObjectId
    InternalVertexMarkerStyleId: ObjectId
    BeginningVertexMarkerStyleId: ObjectId
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    NetworkDisplayMode: SurveyElevationDisplayType
    PlaceAdditionalMarkerAtFigureEndPoint: bool
    PlaceAdditionalMarkerAtFigureStartPoint: bool
    AdditionalMarkerDivideFigureBy: int
    AdditionalMarkerInterval: float
    AdditionalMarkerPlacementMethod: SurveyFigureMarkerPlacementType
    AlignAdditionalMarkersWithFigure: bool
    AlignEndpointMarkersWithFigure: bool
    AlignMidpointMarkersWithFigure: bool
    AlignVertexMarkersWithFigure: bool
    AdditionalMarkerStyleId: ObjectId
    EndPointMarkerStyleId: ObjectId
    StartPointMarkerStyleId: ObjectId
    MidpointMarkerStyleId: ObjectId
    VertexMarkerStyleId: ObjectId
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleModel(self, displayType: SurveyFigureDisplayType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, displayType: SurveyFigureDisplayType) -> DisplayStyle: ...
    def GetDisplayStyleProfile(self, displayType: SurveyFigureProfileDisplayType) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, displayType: SurveyFigureSectionDisplayType) -> DisplayStyle: ...

class SurveyFigureStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class SurveyNetworkDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurveyNetworkDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class SurveyNetworkStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurveyNetworkStyle"""
    def __init__(self, *args) -> None: ...
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    NetworkDisplayMode: SurveyElevationDisplayType
    ErrorEllipseScaleFactor: float
    ToleranceErrorPointsMarkerStyleId: ObjectId
    SideshotPointsMarkerStyleId: ObjectId
    NonControlPointsMarkerStyleId: ObjectId
    UnknownControlPointsMarkerStyleId: ObjectId
    KnownControlPointsMarkerStyleId: ObjectId
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleModel(self, type: SurveyNetworkDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: SurveyNetworkDisplayStyleType) -> DisplayStyle: ...

class SurveyNetworkStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurveyNetworkStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class TableDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.TableDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class TableSortingOrderType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.TableSortingOrderType"""
    def __init__(self, *args) -> None: ...
    ...

class TableStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.TableStyle"""
    def __init__(self, *args) -> None: ...
    DataTextDisplayStyleModel: DisplayStyle
    DataTextDisplayStylePlan: DisplayStyle
    HeaderTextDisplayStyleModel: DisplayStyle
    HeaderTextDisplayStylePlan: DisplayStyle
    TitleTextDisplayStyleModel: DisplayStyle
    TitleTextDisplayStylePlan: DisplayStyle
    DataAreaFillDisplayStyleModel: DisplayStyle
    DataAreaFillDisplayStylePlan: DisplayStyle
    HeaderAreaFillDisplayStyleModel: DisplayStyle
    HeaderAreaFillDisplayStylePlan: DisplayStyle
    TitleAreaFillDisplayStyleModel: DisplayStyle
    TitleAreaFillDisplayStylePlan: DisplayStyle
    DataDividerDisplayStyleModel: DisplayStyle
    DataDividerDisplayStylePlan: DisplayStyle
    DataSeparatorDisplayStyleModel: DisplayStyle
    DataSeparatorDisplayStylePlan: DisplayStyle
    HeaderSeparatorDisplayStyleModel: DisplayStyle
    HeaderSeparatorDisplayStylePlan: DisplayStyle
    TitleSeparatorDisplayStyleModel: DisplayStyle
    TitleSeparatorDisplayStylePlan: DisplayStyle
    BorderDisplayStyleModel: DisplayStyle
    BorderDisplayStylePlan: DisplayStyle
    ColumnStyles: ColumnStyleCollection
    DataTextHeight: float
    HeaderTextHeight: float
    TitleTextHeight: float
    DataTextStyle: str
    HeaderTextStyle: str
    TitleTextStyle: str
    MaintainViewOrientation: bool
    EnableWordWrapping: bool
    SortingColumn: int
    SortingOrder: TableSortingOrderType
    SortData: bool
    TransposeSectionViewTable: bool
    RepeatHeaderInSplitTables: bool
    RepeatTitleInSplitTables: bool
    TitleJustification: TextJustificationType
    TitleUnformatted: str
    Title: str
    TableType: TableStyleType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStyleModel(self, type: TableDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: TableDisplayStyleType) -> DisplayStyle: ...

class TableStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.TableStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class TableStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.TableStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class TableStylesRoot(TreeOidWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.TableStylesRoot"""
    def __init__(self, *args) -> None: ...
    SectionViewMaterialTableStyles: TableStyleCollection
    SectionViewTotalVolumeTableStyles: TableStyleCollection
    QuantityTakeoffMaterialTableStyles: TableStyleCollection
    QuantityTakeoffTotalVolumeTableStyles: TableStyleCollection
    StructureTableStyles: TableStyleCollection
    PipeTableStyles: TableStyleCollection
    PointTableStyles: TableStyleCollection
    SurfaceUserDefinedContourTableStyles: TableStyleCollection
    SurfaceWatershedTableStyles: TableStyleCollection
    SurfaceDirectionTableStyles: TableStyleCollection
    SurfaceSlopeArrowContourTableStyles: TableStyleCollection
    SurfaceElevationTableStyles: TableStyleCollection
    SurfaceSlopeTableStyles: TableStyleCollection
    SurfaceContourTableStyles: TableStyleCollection
    ParcelSegmentTableStyles: TableStyleCollection
    ParcelLineTableStyles: TableStyleCollection
    ParcelAreaTableStyles: TableStyleCollection
    ParcelCurveTableStyles: TableStyleCollection
    AlignmentLineTableStyles: TableStyleCollection
    AlignmentSpiralTableStyles: TableStyleCollection
    AlignmentSegmentTableStyles: TableStyleCollection
    AlignmentCurveTableStyles: TableStyleCollection
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class TextForEachComponentSelectedType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.TextForEachComponentSelectedType"""
    def __init__(self, *args) -> None: ...
    ...

class VerticalGeometryBandStyle(BandStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.VerticalGeometryBandStyle"""
    def __init__(self, *args) -> None: ...
    LabelOnlyTangents: bool
    SagCurveTickStyle: BandTickStyle
    CrestCurveTickStyle: BandTickStyle
    DownhillTangentTickStyle: BandTickStyle
    UphillTangentTickStyle: BandTickStyle
    SagCurveLabelStyleId: ObjectId
    CrestCurveLabelStyleId: ObjectId
    DownhillTangentLabelStyleId: ObjectId
    UphillTangentLabelStyleId: ObjectId
    TitleTextLabelStyleId: ObjectId
    BandType: BandType
    WeedingFactor: float
    TextHeight: float
    TextLocation: BandTitleTextLocation
    TextBoxPosition: BandTitleBoxPosition
    OffsetFromBand: float
    TextBoxWidth: float
    BandHeight: float
    Text: str
    TextStyle: str
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetDisplayStylePlan(self, type: VerticalGeometryDisplayStyleType) -> DisplayStyle: ...

class VerticalGeometryDisplayStyleType:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.VerticalGeometryDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class ViewFrameStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ViewFrameStyle"""
    def __init__(self, *args) -> None: ...
    ViewFrameBoundaryDisplayStylePlan: DisplayStyle
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
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
    def GetViewFrameBoundaryDisplayStylePlan(self, ) -> DisplayStyle: ...

class ViewFrameStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ViewFrameStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class WatershedBaseStyle(CivilWrapper<AeccDbSurfaceStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedBaseStyle"""
    def __init__(self, *args) -> None: ...
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color

class WatershedBoundaryPointStyle(WatershedDrainPointStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedBoundaryPointStyle"""
    def __init__(self, *args) -> None: ...
    PointColor: Color
    PointDisplayType: PointSymbolType
    DrawDrainPoint: bool
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color

class WatershedBoundarySegmentStyle(WatershedDrainSegmentStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedBoundarySegmentStyle"""
    def __init__(self, *args) -> None: ...
    SegmentColor: Color
    SegmentLinetypeId: ObjectId
    SegmentLinetypeName: str
    DrawDrainSegment: bool
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color

class WatershedDepressionStyle(WatershedDrainPointSegmentStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedDepressionStyle"""
    def __init__(self, *args) -> None: ...
    SegmentColor: Color
    SegmentLinetypeId: ObjectId
    SegmentLinetypeName: str
    DrawDrainSegment: bool
    PointColor: Color
    PointDisplayType: PointSymbolType
    DrawDrainPoint: bool
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color

class WatershedDrainPointSegmentStyle(WatershedBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedDrainPointSegmentStyle"""
    def __init__(self, *args) -> None: ...
    SegmentColor: Color
    SegmentLinetypeId: ObjectId
    SegmentLinetypeName: str
    DrawDrainSegment: bool
    PointColor: Color
    PointDisplayType: PointSymbolType
    DrawDrainPoint: bool
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color

class WatershedDrainPointStyle(WatershedBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedDrainPointStyle"""
    def __init__(self, *args) -> None: ...
    PointColor: Color
    PointDisplayType: PointSymbolType
    DrawDrainPoint: bool
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color

class WatershedDrainSegmentStyle(WatershedBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedDrainSegmentStyle"""
    def __init__(self, *args) -> None: ...
    SegmentColor: Color
    SegmentLinetypeId: ObjectId
    SegmentLinetypeName: str
    DrawDrainSegment: bool
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color

class WatershedFlatAreaStyle(WatershedBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedFlatAreaStyle"""
    def __init__(self, *args) -> None: ...
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color

class WatershedMultipleDrainNotchStyle(WatershedDrainSegmentStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedMultipleDrainNotchStyle"""
    def __init__(self, *args) -> None: ...
    SegmentColor: Color
    SegmentLinetypeId: ObjectId
    SegmentLinetypeName: str
    DrawDrainSegment: bool
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color

class WatershedMultipleDrainStyle(WatershedDrainPointStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedMultipleDrainStyle"""
    def __init__(self, *args) -> None: ...
    PointColor: Color
    PointDisplayType: PointSymbolType
    DrawDrainPoint: bool
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color
