# Auto-generated — Navisworks 24 — Autodesk.Navisworks.Api.Clash

class ClashResult(SavedItem):
    """.NET: Autodesk.Navisworks.Api.Clash.ClashResult"""
    def __init__(self, *args) -> None: ...
    ExternalLink: ExternalLink
    HasRedlines: bool
    HasSavedViewpoint: bool
    CompositeItemSelection2: ModelItemCollection
    CompositeItemSelection1: ModelItemCollection
    Selection2: ModelItemCollection
    Selection1: ModelItemCollection
    CompositeItem2: ModelItem
    CompositeItem1: ModelItem
    Item2: ModelItem
    Item1: ModelItem
    Center: Point3D
    ViewBounds: BoundingBox3D
    BoundingBox: BoundingBox3D
    RepresentativeResult: ClashResult
    SimulationName: str
    ResolvedBy: Assignee
    AssignedTo: Assignee
    ApprovedBy: Assignee
    Distance: float
    Priority: int
    Description: str
    TestType: ClashTestType
    Status: ClashResultStatus
    DisplayName: str
    IsReadOnly: bool
    AssignedToVaries: bool
    SimulationTypeVaries: bool
    SimulationEventNameVaries: bool
    CreatedTimeVaries: bool
    ResolvedTimeVaries: bool
    ResolvedByVaries: bool
    ApprovedTimeVaries: bool
    ApprovedByVaries: bool
    TestTypeVaries: bool
    Comments: CommentCollection
    SimulationEndTime: Nullable
    SimulationStartTime: Nullable
    SimulationType: Nullable
    ResolvedTime: Nullable
    ApprovedTime: Nullable
    CreatedTime: Nullable
    Guid: Guid
    IsGroup: bool
    Parent: GroupItem
    IsDisposed: bool
    def CreateCopyWithoutChildren(self, ) -> ClashResult: ...
    @staticmethod
    def InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> ClashResult: ...
    @staticmethod
    def InternalFactory(reserved: NativeHandleInit) -> NativeHandle: ...
    def UserTransitionStatus(self, new_status: ClashResultStatus, who: Assignee) -> SavedItemParts: ...

class ClashResultGroup(GroupItem):
    """.NET: Autodesk.Navisworks.Api.Clash.ClashResultGroup"""
    def __init__(self, *args) -> None: ...
    ExternalLink: ExternalLink
    HasRedlines: bool
    HasSavedViewpoint: bool
    CompositeItemSelection2: ModelItemCollection
    CompositeItemSelection1: ModelItemCollection
    Selection2: ModelItemCollection
    Selection1: ModelItemCollection
    SimulationTypeVaries: bool
    ResolvedTimeVaries: bool
    ApprovedTimeVaries: bool
    CreatedTimeVaries: bool
    Center: Point3D
    ViewBounds: BoundingBox3D
    BoundingBox: BoundingBox3D
    RepresentativeResult: ClashResult
    SimulationEventNameVaries: bool
    SimulationName: str
    ResolvedByVaries: bool
    ResolvedBy: Assignee
    AssignedToVaries: bool
    AssignedTo: Assignee
    ApprovedByVaries: bool
    ApprovedBy: Assignee
    Distance: float
    Priority: int
    Description: str
    TestTypeVaries: bool
    TestType: ClashTestType
    Status: ClashResultStatus
    DisplayName: str
    IsReadOnly: bool
    Comments: CommentCollection
    SimulationEndTime: Nullable
    SimulationStartTime: Nullable
    SimulationType: Nullable
    ResolvedTime: Nullable
    ApprovedTime: Nullable
    CreatedTime: Nullable
    Children: SavedItemCollection
    Guid: Guid
    IsGroup: bool
    Parent: GroupItem
    IsDisposed: bool
    @staticmethod
    def InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> ClashResultGroup: ...
    @staticmethod
    def InternalFactory(reserved: NativeHandleInit) -> NativeHandle: ...
    def UserTransitionStatus(self, new_status: ClashResultStatus, who: Assignee) -> SavedItemParts: ...

class ClashResultParts:
    """.NET: Autodesk.Navisworks.Api.Clash.ClashResultParts"""
    def __init__(self, *args) -> None: ...
    ...

class ClashResultSortMode:
    """.NET: Autodesk.Navisworks.Api.Clash.ClashResultSortMode"""
    def __init__(self, *args) -> None: ...
    ...

class ClashResultStatus:
    """.NET: Autodesk.Navisworks.Api.Clash.ClashResultStatus"""
    def __init__(self, *args) -> None: ...
    ...

class ClashSelection(NativeHandle):
    """.NET: Autodesk.Navisworks.Api.Clash.ClashSelection"""
    def __init__(self, *args) -> None: ...
    PrimitiveTypes: PrimitiveTypes
    SelfIntersect: bool
    Selection: Selection
    IsReadOnly: bool
    IsDisposed: bool
    def CopyFrom(self, other: ClashSelection) -> None: ...
    @staticmethod
    def InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> ClashSelection: ...
    @staticmethod
    def InternalFactory(reserved: NativeHandleInit) -> NativeHandle: ...
    @staticmethod
    def ValueEquals(value1: ClashSelection, value2: ClashSelection) -> bool: ...

class ClashSortDirection:
    """.NET: Autodesk.Navisworks.Api.Clash.ClashSortDirection"""
    def __init__(self, *args) -> None: ...
    ...

class ClashTest(GroupItem):
    """.NET: Autodesk.Navisworks.Api.Clash.ClashTest"""
    def __init__(self, *args) -> None: ...
    MergeComposites: bool
    CustomTestName: str
    SimulationStep: float
    AnimatorSimulation: SavedItemReference
    SimulationType: SimulationType
    IgnoreRules: RuleCollection
    Tolerance: float
    SelectionB: ClashSelection
    SelectionA: ClashSelection
    TestType: ClashTestType
    Priority: int
    DefaultAssignee: Assignee
    Status: ClashTestStatus
    IsReadOnly: bool
    LastRun: Nullable
    Children: SavedItemCollection
    Guid: Guid
    IsGroup: bool
    Parent: GroupItem
    Comments: CommentCollection
    DisplayName: str
    IsDisposed: bool
    def DuplicateTest(self, ) -> ClashTest: ...
    @staticmethod
    def InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> ClashTest: ...
    @staticmethod
    def InternalFactory(reserved: NativeHandleInit) -> NativeHandle: ...

class ClashTestFolder(FolderItem):
    """.NET: Autodesk.Navisworks.Api.Clash.ClashTestFolder"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool
    Children: SavedItemCollection
    Guid: Guid
    IsGroup: bool
    Parent: GroupItem
    Comments: CommentCollection
    DisplayName: str
    IsDisposed: bool
    @staticmethod
    def InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> ClashTestFolder: ...
    @staticmethod
    def InternalFactory(reserved: NativeHandleInit) -> NativeHandle: ...

class ClashTestParts:
    """.NET: Autodesk.Navisworks.Api.Clash.ClashTestParts"""
    def __init__(self, *args) -> None: ...
    ...

class ClashTestSortMode:
    """.NET: Autodesk.Navisworks.Api.Clash.ClashTestSortMode"""
    def __init__(self, *args) -> None: ...
    ...

class ClashTestStatus:
    """.NET: Autodesk.Navisworks.Api.Clash.ClashTestStatus"""
    def __init__(self, *args) -> None: ...
    ...

class ClashTestType:
    """.NET: Autodesk.Navisworks.Api.Clash.ClashTestType"""
    def __init__(self, *args) -> None: ...
    ...

class ClashTestsData:
    """.NET: Autodesk.Navisworks.Api.Clash.ClashTestsData"""
    def __init__(self, *args) -> None: ...
    TestsRoot: ClashTestFolder
    IsDisposed: bool
    IsReadOnly: bool
    def Contains(self, A_0: SavedItem) -> bool: ...
    def CreateCopy(self, ) -> ClashTestsData: ...
    def Dispose(self, ) -> None: ...

class DocumentClash:
    """.NET: Autodesk.Navisworks.Api.Clash.DocumentClash"""
    def __init__(self, *args) -> None: ...
    TestsData: DocumentClashTests
    @staticmethod
    def ClashInstance(doc: Document) -> DocumentClash: ...
    @staticmethod
    def CreateInstance(doc: Document) -> DocumentClash: ...
    def TryCalculateMinimumClearance(self, selection1: ModelItemCollection, selection2: ModelItemCollection, useCenterlines: bool, clearanceResult: MinimumClearanceResult) -> bool: ...

class DocumentClashTests:
    """.NET: Autodesk.Navisworks.Api.Clash.DocumentClashTests"""
    def __init__(self, *args) -> None: ...
    Value: ClashTestsData
    Id: str
    def CopyFrom(self, value: ClashTestsData) -> None: ...
    def CreateCopy(self, ) -> ClashTestsData: ...
    def CreateReference(self, item: SavedItem) -> SavedItemReference: ...
    def ResolveGuid(self, value: Guid) -> SavedItem: ...
    def ResolveReference(self, reference: SavedItemReference) -> SavedItem: ...
    def TestsAddCopy(self, parent: GroupItem, item: SavedItem) -> None: ...
    def TestsClear(self, ) -> None: ...
    def TestsClearResults(self, test: ClashTest) -> None: ...
    def TestsCompactAllTests(self, ) -> None: ...
    def TestsCompactTest(self, test: ClashTest) -> None: ...
    def TestsCopyFrom(self, value: SavedItemCollection) -> None: ...
    def TestsEditDisplayName(self, item: SavedItem, name: str) -> None: ...
    def TestsEditResultApprovedBy(self, result: IClashResult, approvedBy: Assignee) -> None: ...
    def TestsEditResultApprovedTime(self, result: IClashResult, approvedTime: DateTime) -> None: ...
    def TestsEditResultAssignedTo(self, result: IClashResult, assignedTo: Assignee) -> None: ...
    def TestsEditResultBoundingBox(self, result: IClashResult, boundingBox: BoundingBox3D) -> None: ...
    def TestsEditResultCenter(self, result: IClashResult, center: Point3D) -> None: ...
    def TestsEditResultComments(self, result: IClashResult, comments: CommentCollection) -> None: ...
    def TestsEditResultCreatedTime(self, result: IClashResult, createdTime: DateTime) -> None: ...
    def TestsEditResultDescription(self, result: IClashResult, description: str) -> None: ...
    def TestsEditResultDistance(self, result: IClashResult, distance: float) -> None: ...
    def TestsEditResultExternalLink(self, result: IClashResult, externalLink: ExternalLink) -> None: ...
    def TestsEditResultPriority(self, result: IClashResult, priority: int) -> None: ...
    def TestsEditResultStatus(self, result: IClashResult, status: ClashResultStatus, current_user: Assignee) -> None: ...
    def TestsEditTestFromCopy(self, test: ClashTest, copyFrom: ClashTest) -> None: ...
    def TestsImageForResult(self, result: IClashResult, style: ImageGenerationStyle, width: int, height: int) -> Bitmap: ...
    def TestsInsertCopy(self, parent: GroupItem, index: int, item: SavedItem) -> None: ...
    def TestsMove(self, oldParent: GroupItem, oldIndex: int, newParent: GroupItem, newIndex: int) -> None: ...
    def TestsRemove(self, parent: GroupItem, item: SavedItem) -> None: ...
    def TestsRemoveAt(self, parent: GroupItem, index: int) -> None: ...
    def TestsReplaceWithCopy(self, parent: GroupItem, index: int, item: SavedItem) -> None: ...
    def TestsRunAllTests(self, ) -> None: ...
    def TestsRunTest(self, test: ClashTest) -> None: ...
    def TestsSortResults(self, test: ClashTest, sortBy: ClashResultSortMode, direction: ClashSortDirection, proximityTo: Point3D) -> None: ...
    def TestsSortTests(self, sortBy: ClashTestSortMode, direction: ClashSortDirection) -> None: ...
    def TestsViewpointForResult(self, result: IClashResult) -> Viewpoint: ...

class DocumentExtensions:
    """.NET: Autodesk.Navisworks.Api.Clash.DocumentExtensions"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetClash(doc: Document) -> DocumentClash: ...

class ExternalLink(NativeHandle):
    """.NET: Autodesk.Navisworks.Api.Clash.ExternalLink"""
    def __init__(self, *args) -> None: ...
    Color: Color
    Type: str
    Data: str
    Label: str
    IsReadOnly: bool
    IsDisposed: bool
    def AddTag(self, tag: str) -> None: ...
    def HasTag(self, tag: str) -> bool: ...
    @staticmethod
    def InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> ExternalLink: ...
    @staticmethod
    def InternalFactory(reserved: NativeHandleInit) -> NativeHandle: ...
    def RemoveTag(self, tag: str) -> None: ...

class ExternalLinkTags:
    """.NET: Autodesk.Navisworks.Api.Clash.ExternalLinkTags"""
    def __init__(self, *args) -> None: ...
    ...

class IClashResult:
    """.NET: Autodesk.Navisworks.Api.Clash.IClashResult"""
    def __init__(self, *args) -> None: ...
    ExternalLink: ExternalLink
    Selection2: ModelItemCollection
    Selection1: ModelItemCollection
    CompositeItemSelection2: ModelItemCollection
    CompositeItemSelection1: ModelItemCollection
    HasRedlines: bool
    HasSavedViewpoint: bool
    AssignedToVaries: bool
    SimulationTypeVaries: bool
    SimulationEventNameVaries: bool
    CreatedTimeVaries: bool
    ResolvedTimeVaries: bool
    ResolvedByVaries: bool
    ApprovedTimeVaries: bool
    ApprovedByVaries: bool
    TestTypeVaries: bool
    Center: Point3D
    Comments: CommentCollection
    ViewBounds: BoundingBox3D
    BoundingBox: BoundingBox3D
    RepresentativeResult: ClashResult
    SimulationName: str
    SimulationType: Nullable
    SimulationEndTime: Nullable
    SimulationStartTime: Nullable
    AssignedTo: Assignee
    ResolvedBy: Assignee
    ResolvedTime: Nullable
    ApprovedBy: Assignee
    ApprovedTime: Nullable
    CreatedTime: Nullable
    Distance: float
    Description: str
    Priority: int
    TestType: ClashTestType
    Status: ClashResultStatus
    DisplayName: str
    def CreateCopy(self, ) -> IClashResult: ...
    def CreateCopyWithoutChildren(self, ) -> IClashResult: ...

class MinimumClearanceResult:
    """.NET: Autodesk.Navisworks.Api.Clash.MinimumClearanceResult"""
    def __init__(self, *args) -> None: ...
    Point2OnCenterline: bool
    Point1OnCenterline: bool
    ClosestPointOnSelection2: Point3D
    ClosestPointOnSelection1: Point3D
