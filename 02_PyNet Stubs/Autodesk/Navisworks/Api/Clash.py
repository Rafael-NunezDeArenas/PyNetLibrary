# Auto-generated Navisworks API stubs (clean reflection)

class IClashResult(object):
    """ .NET type: Autodesk.Navisworks.Api.Clash.IClashResult """

    def __init__(self, *args) -> None:
        pass
        

    def CreateCopy(self, *args):
        """
        Signature:
        CreateCopy() -> IClashResult
        """
        pass
            

    def CreateCopyWithoutChildren(self, *args):
        """
        Signature:
        CreateCopyWithoutChildren() -> IClashResult
        """
        pass
            

    Selection2: ModelItemCollection = property(lambda self: None, lambda self, v: None)
    

    Selection1: ModelItemCollection = property(lambda self: None, lambda self, v: None)
    

    CompositeItemSelection2: ModelItemCollection = property(lambda self: None, lambda self, v: None)
    

    CompositeItemSelection1: ModelItemCollection = property(lambda self: None, lambda self, v: None)
    

    HasRedlines: bool = property(lambda self: None, lambda self, v: None)
    

    HasSavedViewpoint: bool = property(lambda self: None, lambda self, v: None)
    

    AssignedToVaries: bool = property(lambda self: None, lambda self, v: None)
    

    SimulationTypeVaries: bool = property(lambda self: None, lambda self, v: None)
    

    SimulationEventNameVaries: bool = property(lambda self: None, lambda self, v: None)
    

    DescriptionVaries: bool = property(lambda self: None, lambda self, v: None)
    

    CreatedTimeVaries: bool = property(lambda self: None, lambda self, v: None)
    

    ApprovedTimeVaries: bool = property(lambda self: None, lambda self, v: None)
    

    ApprovedByVaries: bool = property(lambda self: None, lambda self, v: None)
    

    Center: Point3D = property(lambda self: None, lambda self, v: None)
    

    Comments: CommentCollection = property(lambda self: None, lambda self, v: None)
    

    ViewBounds: BoundingBox3D = property(lambda self: None, lambda self, v: None)
    

    BoundingBox: BoundingBox3D = property(lambda self: None, lambda self, v: None)
    

    RepresentativeResult: ClashResult = property(lambda self: None, lambda self, v: None)
    

    SimulationName: str = property(lambda self: None, lambda self, v: None)
    

    SimulationType: Nullable`1 = property(lambda self: None, lambda self, v: None)
    

    SimulationEndTime: Nullable`1 = property(lambda self: None, lambda self, v: None)
    

    SimulationStartTime: Nullable`1 = property(lambda self: None, lambda self, v: None)
    

    AssignedTo: str = property(lambda self: None, lambda self, v: None)
    

    ApprovedBy: str = property(lambda self: None, lambda self, v: None)
    

    ApprovedTime: Nullable`1 = property(lambda self: None, lambda self, v: None)
    

    CreatedTime: Nullable`1 = property(lambda self: None, lambda self, v: None)
    

    Distance: float = property(lambda self: None, lambda self, v: None)
    

    Description: str = property(lambda self: None, lambda self, v: None)
    

    Status: ClashResultStatus = property(lambda self: None, lambda self, v: None)
    

    DisplayName: str = property(lambda self: None, lambda self, v: None)
    

class LcOclClashResultStatus(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcOclClashResultStatus """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcOclClashResultStatus
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcOclTestSortEnum(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcOclTestSortEnum """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcOclTestSortEnum
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcOclDirectionSortEnum(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcOclDirectionSortEnum """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcOclDirectionSortEnum
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcOclResultSortEnum(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcOclResultSortEnum """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcOclResultSortEnum
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class ClashSelection(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Clash.ClashSelection """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> ClashSelection
        """
        pass
            

    @staticmethod
    def ValueEquals(*args):
        """
        Signature:
        ValueEquals(value1: ClashSelection, value2: ClashSelection) -> bool
        """
        pass
            

    def CopyFrom(self, *args):
        """
        Signature:
        CopyFrom(other: ClashSelection) -> None
        """
        pass
            

    PrimitiveTypes: PrimitiveTypes = property(lambda self: None, lambda self, v: None)
    

    SelfIntersect: bool = property(lambda self: None, lambda self, v: None)
    

    Selection: Selection = property(lambda self: None, lambda self, v: None)
    

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class ClashTest(GroupItem):
    """ .NET type: Autodesk.Navisworks.Api.Clash.ClashTest """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> ClashTest
        """
        pass
            

    MergeComposites: bool = property(lambda self: None, lambda self, v: None)
    

    CustomTestName: str = property(lambda self: None, lambda self, v: None)
    

    SimulationStep: float = property(lambda self: None, lambda self, v: None)
    

    AnimatorSimulation: SavedItemReference = property(lambda self: None, lambda self, v: None)
    

    SimulationType: SimulationType = property(lambda self: None, lambda self, v: None)
    

    IgnoreRules: RuleCollection = property(lambda self: None, lambda self, v: None)
    

    Tolerance: float = property(lambda self: None, lambda self, v: None)
    

    SelectionB: ClashSelection = property(lambda self: None, lambda self, v: None)
    

    SelectionA: ClashSelection = property(lambda self: None, lambda self, v: None)
    

    TestType: ClashTestType = property(lambda self: None, lambda self, v: None)
    

    Status: ClashTestStatus = property(lambda self: None, lambda self, v: None)
    

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    LastRun: Nullable`1 = property(lambda self: None, lambda self, v: None)
    

    Children: SavedItemCollection = property(lambda self: None, lambda self, v: None)
    

    Guid: Guid = property(lambda self: None, lambda self, v: None)
    

    IsGroup: bool = property(lambda self: None, lambda self, v: None)
    

    Parent: GroupItem = property(lambda self: None, lambda self, v: None)
    

    Comments: CommentCollection = property(lambda self: None, lambda self, v: None)
    

    DisplayName: str = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcOclTestIssue(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcOclTestIssue """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcOclTestIssue
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class ClashResult(SavedItem):
    """ .NET type: Autodesk.Navisworks.Api.Clash.ClashResult """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> ClashResult
        """
        pass
            

    def CreateCopyWithoutChildren(self, *args):
        """
        Signature:
        CreateCopyWithoutChildren() -> ClashResult
        """
        pass
            

    HasRedlines: bool = property(lambda self: None, lambda self, v: None)
    

    HasSavedViewpoint: bool = property(lambda self: None, lambda self, v: None)
    

    CompositeItemSelection2: ModelItemCollection = property(lambda self: None, lambda self, v: None)
    

    CompositeItemSelection1: ModelItemCollection = property(lambda self: None, lambda self, v: None)
    

    Selection2: ModelItemCollection = property(lambda self: None, lambda self, v: None)
    

    Selection1: ModelItemCollection = property(lambda self: None, lambda self, v: None)
    

    CompositeItem2: ModelItem = property(lambda self: None, lambda self, v: None)
    

    CompositeItem1: ModelItem = property(lambda self: None, lambda self, v: None)
    

    Item2: ModelItem = property(lambda self: None, lambda self, v: None)
    

    Item1: ModelItem = property(lambda self: None, lambda self, v: None)
    

    Center: Point3D = property(lambda self: None, lambda self, v: None)
    

    ViewBounds: BoundingBox3D = property(lambda self: None, lambda self, v: None)
    

    BoundingBox: BoundingBox3D = property(lambda self: None, lambda self, v: None)
    

    RepresentativeResult: ClashResult = property(lambda self: None, lambda self, v: None)
    

    SimulationName: str = property(lambda self: None, lambda self, v: None)
    

    AssignedTo: str = property(lambda self: None, lambda self, v: None)
    

    ApprovedBy: str = property(lambda self: None, lambda self, v: None)
    

    Distance: float = property(lambda self: None, lambda self, v: None)
    

    Description: str = property(lambda self: None, lambda self, v: None)
    

    Status: ClashResultStatus = property(lambda self: None, lambda self, v: None)
    

    DisplayName: str = property(lambda self: None, lambda self, v: None)
    

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    AssignedToVaries: bool = property(lambda self: None, lambda self, v: None)
    

    SimulationTypeVaries: bool = property(lambda self: None, lambda self, v: None)
    

    SimulationEventNameVaries: bool = property(lambda self: None, lambda self, v: None)
    

    DescriptionVaries: bool = property(lambda self: None, lambda self, v: None)
    

    CreatedTimeVaries: bool = property(lambda self: None, lambda self, v: None)
    

    ApprovedTimeVaries: bool = property(lambda self: None, lambda self, v: None)
    

    ApprovedByVaries: bool = property(lambda self: None, lambda self, v: None)
    

    Comments: CommentCollection = property(lambda self: None, lambda self, v: None)
    

    SimulationEndTime: Nullable`1 = property(lambda self: None, lambda self, v: None)
    

    SimulationStartTime: Nullable`1 = property(lambda self: None, lambda self, v: None)
    

    SimulationType: Nullable`1 = property(lambda self: None, lambda self, v: None)
    

    ApprovedTime: Nullable`1 = property(lambda self: None, lambda self, v: None)
    

    CreatedTime: Nullable`1 = property(lambda self: None, lambda self, v: None)
    

    Guid: Guid = property(lambda self: None, lambda self, v: None)
    

    IsGroup: bool = property(lambda self: None, lambda self, v: None)
    

    Parent: GroupItem = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class ClashResultGroup(GroupItem):
    """ .NET type: Autodesk.Navisworks.Api.Clash.ClashResultGroup """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> ClashResultGroup
        """
        pass
            

    HasRedlines: bool = property(lambda self: None, lambda self, v: None)
    

    HasSavedViewpoint: bool = property(lambda self: None, lambda self, v: None)
    

    CompositeItemSelection2: ModelItemCollection = property(lambda self: None, lambda self, v: None)
    

    CompositeItemSelection1: ModelItemCollection = property(lambda self: None, lambda self, v: None)
    

    Selection2: ModelItemCollection = property(lambda self: None, lambda self, v: None)
    

    Selection1: ModelItemCollection = property(lambda self: None, lambda self, v: None)
    

    SimulationTypeVaries: bool = property(lambda self: None, lambda self, v: None)
    

    ApprovedTimeVaries: bool = property(lambda self: None, lambda self, v: None)
    

    CreatedTimeVaries: bool = property(lambda self: None, lambda self, v: None)
    

    Center: Point3D = property(lambda self: None, lambda self, v: None)
    

    ViewBounds: BoundingBox3D = property(lambda self: None, lambda self, v: None)
    

    BoundingBox: BoundingBox3D = property(lambda self: None, lambda self, v: None)
    

    RepresentativeResult: ClashResult = property(lambda self: None, lambda self, v: None)
    

    SimulationEventNameVaries: bool = property(lambda self: None, lambda self, v: None)
    

    SimulationName: str = property(lambda self: None, lambda self, v: None)
    

    AssignedToVaries: bool = property(lambda self: None, lambda self, v: None)
    

    AssignedTo: str = property(lambda self: None, lambda self, v: None)
    

    ApprovedByVaries: bool = property(lambda self: None, lambda self, v: None)
    

    ApprovedBy: str = property(lambda self: None, lambda self, v: None)
    

    Distance: float = property(lambda self: None, lambda self, v: None)
    

    DescriptionVaries: bool = property(lambda self: None, lambda self, v: None)
    

    Description: str = property(lambda self: None, lambda self, v: None)
    

    Status: ClashResultStatus = property(lambda self: None, lambda self, v: None)
    

    DisplayName: str = property(lambda self: None, lambda self, v: None)
    

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    Comments: CommentCollection = property(lambda self: None, lambda self, v: None)
    

    SimulationEndTime: Nullable`1 = property(lambda self: None, lambda self, v: None)
    

    SimulationStartTime: Nullable`1 = property(lambda self: None, lambda self, v: None)
    

    SimulationType: Nullable`1 = property(lambda self: None, lambda self, v: None)
    

    ApprovedTime: Nullable`1 = property(lambda self: None, lambda self, v: None)
    

    CreatedTime: Nullable`1 = property(lambda self: None, lambda self, v: None)
    

    Children: SavedItemCollection = property(lambda self: None, lambda self, v: None)
    

    Guid: Guid = property(lambda self: None, lambda self, v: None)
    

    IsGroup: bool = property(lambda self: None, lambda self, v: None)
    

    Parent: GroupItem = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcOclClashUtils(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcOclClashUtils """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcOclClashUtils
        """
        pass
            

    @staticmethod
    def CountByStatus(*args):
        """
        Signature:
        CountByStatus(group: GroupItem, status: ClashResultStatus, recurse: bool) -> int
        """
        pass
            

    @staticmethod
    def CalculateMinimumClearance(*args):
        """
        Signature:
        CalculateMinimumClearance(state: LcOpState, sel1: ModelItemCollection, sel2: ModelItemCollection, use_center_lines: bool, pt1: Point3D, pt2: Point3D, pt1_on_CL: Boolean&, pt2_on_CL: Boolean&) -> bool
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class ClashTestFolder(FolderItem):
    """ .NET type: Autodesk.Navisworks.Api.Clash.ClashTestFolder """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> ClashTestFolder
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    Children: SavedItemCollection = property(lambda self: None, lambda self, v: None)
    

    Guid: Guid = property(lambda self: None, lambda self, v: None)
    

    IsGroup: bool = property(lambda self: None, lambda self, v: None)
    

    Parent: GroupItem = property(lambda self: None, lambda self, v: None)
    

    Comments: CommentCollection = property(lambda self: None, lambda self, v: None)
    

    DisplayName: str = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcOpClashElement(LcOpSavedItemsElement):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcOpClashElement """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcOpClashElement
        """
        pass
            

    @staticmethod
    def Create(*args):
        """
        Signature:
        Create() -> LcOpElement
        """
        pass
            

    @staticmethod
    def GetClass(*args):
        """
        Signature:
        GetClass() -> LcOpElementClass
        """
        pass
            

    @staticmethod
    def Edit(*args):
        """
        Signature:
        Edit(state: LcOpState, lock: LcOpLock) -> LcOpClashElement
        """
        pass
            

    @staticmethod
    def Get(*args):
        """
        Signature:
        Get(state: LcOpState) -> LcOpClashElement
        """
        pass
            

    @staticmethod
    def GetElementClassName(*args):
        """
        Signature:
        GetElementClassName() -> str
        """
        pass
            

    @staticmethod
    def GetClassUserName(*args):
        """
        Signature:
        GetClassUserName() -> str
        """
        pass
            

    @staticmethod
    def Delete(*args):
        """
        Signature:
        Delete(state: LcOpState, lock: LcOpLock) -> bool
        """
        pass
            

    def GetNumTests(self, *args):
        """
        Signature:
        GetNumTests() -> int
        """
        pass
            

    def GetTestFolder(self, *args):
        """
        Signature:
        GetTestFolder() -> ClashTestFolder
        """
        pass
            

    def EditTestFolder(self, *args):
        """
        Signature:
        EditTestFolder() -> ClashTestFolder
        """
        pass
            

    @staticmethod
    def GetProxyTestFolder(*args):
        """
        Signature:
        GetProxyTestFolder() -> ClashTestFolder
        """
        pass
            

    def AddTestCopy(self, *args):
        """
        Signature:
        AddTestCopy(test: ClashTest) -> None
        """
        pass
            

    def ClearTests(self, *args):
        """
        Signature:
        ClearTests() -> None
        """
        pass
            

    def GetTest(self, *args):
        """
        Signature:
        GetTest(idx: int) -> ClashTest
        """
        pass
            

    @staticmethod
    def EditTest(*args):
        """
        Signature:
        EditTest(state: LcOpState, parent: GroupItem, index: int, test: ClashTest, parts: SavedItemParts) -> bool
        """
        pass
            

    def RemoveTest(self, *args):
        """
        Signature:
        RemoveTest(idx: int) -> ClashTest
        """
        pass
            

    @staticmethod
    def InsertTestCopy(*args):
        """
        Signature:
        InsertTestCopy(state: LcOpState, parent: GroupItem, index: int, test: SavedItem) -> LcOpSavedItemsElementStatus
        """
        pass
            

    @staticmethod
    def ReplaceTestWithCopy(*args):
        """
        Signature:
        ReplaceTestWithCopy(state: LcOpState, parent: GroupItem, index: int, item: SavedItem) -> LcOpSavedItemsElementStatus
        """
        pass
            

    @staticmethod
    def ReplaceTest(*args):
        """
        Signature:
        ReplaceTest(state: LcOpState, parent: GroupItem, index: int, copy: SavedItem) -> LcOpSavedItemsElementStatus
        """
        pass
            

    @staticmethod
    def MoveTest(*args):
        """
        Signature:
        MoveTest(state: LcOpState, item: SavedItem, new_parent: GroupItem, new_index: int) -> bool
        """
        pass
            

    @staticmethod
    def DeleteTest(*args):
        """
        Signature:
        DeleteTest(state: LcOpState, parent: GroupItem, index: int) -> bool
        """
        pass
            

    @staticmethod
    def EditTestWithCopy(*args):
        """
        Signature:
        EditTestWithCopy(state: LcOpState, parent: GroupItem, index: int, copy_from: ClashTest, parts: SavedItemParts) -> bool
        """
        pass
            

    @staticmethod
    def EditIssueWithCopy(*args):
        """
        Signature:
        EditIssueWithCopy(state: LcOpState, parent: GroupItem, index: int, copy_from: LcOclTestIssue, parts: SavedItemParts) -> bool
        """
        pass
            

    @staticmethod
    def EditIssue(*args):
        """
        Signature:
        EditIssue(state: LcOpState, parent: GroupItem, index: int, issue: LcOclTestIssue, parts: SavedItemParts) -> bool
        """
        pass
            

    @staticmethod
    def EditItem(*args):
        """
        Signature:
        EditItem(state: LcOpState, parent: GroupItem, index: int, item: SavedItem, parts: SavedItemParts) -> LcOpSavedItemsElementStatus
        """
        pass
            

    @staticmethod
    def EditItemWithCopy(*args):
        """
        Signature:
        EditItemWithCopy(state: LcOpState, parent: GroupItem, index: int, copy_from: SavedItem, parts: SavedItemParts) -> LcOpSavedItemsElementStatus
        """
        pass
            

    @staticmethod
    def ReplaceAllFoldersCopy(*args):
        """
        Signature:
        ReplaceAllFoldersCopy(state: LcOpState, tests: ClashTestFolder) -> LcOpSavedItemsElementStatus
        """
        pass
            

    def SortTests(self, *args):
        """
        Signature:
        SortTests(sort_by: ClashTestSortMode, direction: ClashSortDirection) -> None
        """
        pass
            

    @staticmethod
    def SortResults(*args):
        """
        Signature:
        SortResults(state: LcOpState, test: ClashTest, sort_by: ClashResultSortMode, direction: ClashSortDirection, point: Point3D) -> None
        """
        pass
            

    @staticmethod
    def SetFlagAndMergeComposites(*args):
        """
        Signature:
        SetFlagAndMergeComposites(state: LcOpState, test: ClashTest) -> None
        """
        pass
            

    @staticmethod
    def GetItem(*args):
        """
        Signature:
        GetItem(state: LcOpState, guid: Guid) -> SavedItem
        """
        pass
            

    CustomHighlightColorObject2: Color = property(lambda self: None, lambda self, v: None)
    

    CustomHighlightColorObject1: Color = property(lambda self: None, lambda self, v: None)
    

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcClClashGUIProxy(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcClClashGUIProxy """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcClClashGUIProxy
        """
        pass
            

    def PromptForFilename(self, *args):
        """
        Signature:
        PromptForFilename(extension: str, suggestedName: str, filter: str, out_filename: String&) -> bool
        """
        pass
            

    def PromptForFolder(self, *args):
        """
        Signature:
        PromptForFolder(title: str, startFolder: str, out_folder: String&) -> bool
        """
        pass
            

    def ReportError(self, *args):
        """
        Signature:
        ReportError(error_msg: str) -> None
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcClClashUtils(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcClClashUtils """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcClClashUtils
        """
        pass
            

    @staticmethod
    def Initialise(*args):
        """
        Signature:
        Initialise() -> None
        """
        pass
            

    @staticmethod
    def Terminate(*args):
        """
        Signature:
        Terminate() -> None
        """
        pass
            

    @staticmethod
    def IsInitialised(*args):
        """
        Signature:
        IsInitialised() -> bool
        """
        pass
            

    @staticmethod
    def InitializeCustomTests(*args):
        """
        Signature:
        InitializeCustomTests(state: LcOpState) -> None
        """
        pass
            

    @staticmethod
    def AddFakeIgnorePluginForUnitTest(*args):
        """
        Signature:
        AddFakeIgnorePluginForUnitTest(version: int) -> None
        """
        pass
            

    @staticmethod
    def RegisterPluginsForUnitTest(*args):
        """
        Signature:
        RegisterPluginsForUnitTest() -> None
        """
        pass
            

    @staticmethod
    def SetPathsForUnitTest(*args):
        """
        Signature:
        SetPathsForUnitTest(result: ClashResult, state: LcOpState, whichPath1: int, whichPath2: int) -> None
        """
        pass
            

    @staticmethod
    def SetHasViewpointForUnitTest(*args):
        """
        Signature:
        SetHasViewpointForUnitTest(result: ClashResult, add_redline: bool) -> None
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcClClashRules(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcClClashRules """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcClClashRules
        """
        pass
            

    @staticmethod
    def Initialise(*args):
        """
        Signature:
        Initialise() -> None
        """
        pass
            

    @staticmethod
    def Terminate(*args):
        """
        Signature:
        Terminate() -> None
        """
        pass
            

    @staticmethod
    def IsInitialised(*args):
        """
        Signature:
        IsInitialised() -> bool
        """
        pass
            

    @staticmethod
    def LoadBaseRuleSet(*args):
        """
        Signature:
        LoadBaseRuleSet(rules: RuleCollection, state: LcOpState) -> None
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcClashReportResultSelector(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcClashReportResultSelector """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcClashReportResultSelector
        """
        pass
            

    def AddGuid(self, *args):
        """
        Signature:
        AddGuid(guid: Guid) -> None
        """
        pass
            

    def Clear(self, *args):
        """
        Signature:
        Clear() -> None
        """
        pass
            

    def ContainsGuid(self, *args):
        """
        Signature:
        ContainsGuid(guid: Guid) -> bool
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcClClashReport(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcClClashReport """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcClClashReport
        """
        pass
            

    @staticmethod
    def Initialise(*args):
        """
        Signature:
        Initialise() -> None
        """
        pass
            

    @staticmethod
    def Terminate(*args):
        """
        Signature:
        Terminate() -> None
        """
        pass
            

    @staticmethod
    def IsInitialised(*args):
        """
        Signature:
        IsInitialised() -> bool
        """
        pass
            

    @staticmethod
    def NumReportFields(*args):
        """
        Signature:
        NumReportFields() -> int
        """
        pass
            

    @staticmethod
    def GetReportField(*args):
        """
        Signature:
        GetReportField(index: int) -> LcClReportField
        """
        pass
            

    @staticmethod
    def NumStatusFlags(*args):
        """
        Signature:
        NumStatusFlags() -> int
        """
        pass
            

    @staticmethod
    def GetStatusFlag(*args):
        """
        Signature:
        GetStatusFlag(index: int) -> LcClStatusFlag
        """
        pass
            

    @staticmethod
    def GroupModesEnabled(*args):
        """
        Signature:
        GroupModesEnabled(state: LcOpState) -> bool
        """
        pass
            

    @staticmethod
    def NumGroupModes(*args):
        """
        Signature:
        NumGroupModes() -> int
        """
        pass
            

    @staticmethod
    def GetGroupModeName(*args):
        """
        Signature:
        GetGroupModeName(index: int, groupMode: String&) -> None
        """
        pass
            

    @staticmethod
    def GetCurrentGroupMode(*args):
        """
        Signature:
        GetCurrentGroupMode() -> int
        """
        pass
            

    @staticmethod
    def SetCurrentGroupMode(*args):
        """
        Signature:
        SetCurrentGroupMode(index: int) -> None
        """
        pass
            

    @staticmethod
    def NumReportDrivers(*args):
        """
        Signature:
        NumReportDrivers() -> int
        """
        pass
            

    @staticmethod
    def GetReportDriverName(*args):
        """
        Signature:
        GetReportDriverName(index: int, reportDriver: String&) -> None
        """
        pass
            

    @staticmethod
    def GetReportDriverInternalName(*args):
        """
        Signature:
        GetReportDriverInternalName(index: int, reportDriver: String&) -> None
        """
        pass
            

    @staticmethod
    def GetCurrentReportDriver(*args):
        """
        Signature:
        GetCurrentReportDriver() -> int
        """
        pass
            

    @staticmethod
    def SetCurrentReportDriver(*args):
        """
        Signature:
        SetCurrentReportDriver(index: int) -> None
        """
        pass
            

    @staticmethod
    def NumReportFormatters(*args):
        """
        Signature:
        NumReportFormatters() -> int
        """
        pass
            

    @staticmethod
    def GetReportFormatterName(*args):
        """
        Signature:
        GetReportFormatterName(index: int, reportFormatter: String&) -> None
        """
        pass
            

    @staticmethod
    def GetCurrentReportFormatter(*args):
        """
        Signature:
        GetCurrentReportFormatter() -> int
        """
        pass
            

    @staticmethod
    def SetCurrentReportFormatter(*args):
        """
        Signature:
        SetCurrentReportFormatter(index: int) -> None
        """
        pass
            

    @staticmethod
    def GetReportFormatterInternalName(*args):
        """
        Signature:
        GetReportFormatterInternalName(index: int, internalName: String&) -> None
        """
        pass
            

    @staticmethod
    def FormatterIsViewpoints(*args):
        """
        Signature:
        FormatterIsViewpoints(index: int) -> bool
        """
        pass
            

    @staticmethod
    def GetCurrentFilterMode(*args):
        """
        Signature:
        GetCurrentFilterMode() -> bool
        """
        pass
            

    @staticmethod
    def SetCurrentFilterMode(*args):
        """
        Signature:
        SetCurrentFilterMode(filter: bool) -> None
        """
        pass
            

    @staticmethod
    def GetViewpointsRespectHighlighting(*args):
        """
        Signature:
        GetViewpointsRespectHighlighting() -> bool
        """
        pass
            

    @staticmethod
    def SetViewpointsRespectHighlighting(*args):
        """
        Signature:
        SetViewpointsRespectHighlighting(highlight: bool) -> None
        """
        pass
            

    @staticmethod
    def WriteReport(*args):
        """
        Signature:
        WriteReport(state: LcOpState, guiProxy: LcClClashGUIProxy, selection: LcClashReportResultSelector, name_annotation: str) -> bool
        """
        pass
            

    @staticmethod
    def CanWriteReport(*args):
        """
        Signature:
        CanWriteReport(state: LcOpState) -> bool
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcClReportField(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcClReportField """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcClReportField
        """
        pass
            

    def GetUserNameW(self, *args):
        """
        Signature:
        GetUserNameW(buff: String&) -> None
        """
        pass
            

    def GetEnabled(self, *args):
        """
        Signature:
        GetEnabled() -> bool
        """
        pass
            

    def SetEnabled(self, *args):
        """
        Signature:
        SetEnabled(enabled: bool) -> None
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcClStatusFlag(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcClStatusFlag """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcClStatusFlag
        """
        pass
            

    def GetUserNameW(self, *args):
        """
        Signature:
        GetUserNameW(buff: String&) -> None
        """
        pass
            

    def GetEnabled(self, *args):
        """
        Signature:
        GetEnabled() -> bool
        """
        pass
            

    def SetEnabled(self, *args):
        """
        Signature:
        SetEnabled(enabled: bool) -> None
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcClCurrentIssueNotify(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcClCurrentIssueNotify """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcClCurrentIssueNotify
        """
        pass
            

    def OnCurrentIssueChanged(self, *args):
        """
        Signature:
        OnCurrentIssueChanged(showIssue: bool) -> None
        """
        pass
            

    def OnCurrentTestChanged(self, *args):
        """
        Signature:
        OnCurrentTestChanged() -> None
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcClCurrentIssue(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcClCurrentIssue """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcClCurrentIssue
        """
        pass
            

    @staticmethod
    def Initialise(*args):
        """
        Signature:
        Initialise() -> None
        """
        pass
            

    @staticmethod
    def Terminate(*args):
        """
        Signature:
        Terminate() -> None
        """
        pass
            

    @staticmethod
    def IsInitialised(*args):
        """
        Signature:
        IsInitialised() -> bool
        """
        pass
            

    @staticmethod
    def InitialiseForState(*args):
        """
        Signature:
        InitialiseForState(state: LcOpState) -> None
        """
        pass
            

    @staticmethod
    def TerminateForState(*args):
        """
        Signature:
        TerminateForState(state: LcOpState) -> None
        """
        pass
            

    @staticmethod
    def GetInstance(*args):
        """
        Signature:
        GetInstance(state: LcOpState) -> LcClCurrentIssue
        """
        pass
            

    def OnGotFocus(self, *args):
        """
        Signature:
        OnGotFocus() -> None
        """
        pass
            

    def GetCurrentIssueAsSavedItem(self, *args):
        """
        Signature:
        GetCurrentIssueAsSavedItem() -> SavedItem
        """
        pass
            

    def SetCurrentIssueFromSavedItem(self, *args):
        """
        Signature:
        SetCurrentIssueFromSavedItem(issue: SavedItem, comment_index: int, force_take_comment_element: bool) -> None
        """
        pass
            

    def ClearCurrentIssue(self, *args):
        """
        Signature:
        ClearCurrentIssue() -> None
        """
        pass
            

    def GetCurrentTest(self, *args):
        """
        Signature:
        GetCurrentTest() -> ClashTest
        """
        pass
            

    def SetCurrentTest(self, *args):
        """
        Signature:
        SetCurrentTest(test: ClashTest) -> None
        """
        pass
            

    def ClearCurrentTest(self, *args):
        """
        Signature:
        ClearCurrentTest() -> None
        """
        pass
            

    def AddNotify(self, *args):
        """
        Signature:
        AddNotify(notify: LcClCurrentIssueNotify) -> None
        """
        pass
            

    def DelNotify(self, *args):
        """
        Signature:
        DelNotify(notify: LcClCurrentIssueNotify) -> None
        """
        pass
            

    def RefreshComment(self, *args):
        """
        Signature:
        RefreshComment() -> None
        """
        pass
            

    def PushDisable(self, *args):
        """
        Signature:
        PushDisable() -> None
        """
        pass
            

    def PopDisable(self, *args):
        """
        Signature:
        PopDisable() -> None
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcClTestDefaultsStore(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcClTestDefaultsStore """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcClTestDefaultsStore
        """
        pass
            

    @staticmethod
    def Initialise(*args):
        """
        Signature:
        Initialise() -> None
        """
        pass
            

    @staticmethod
    def Terminate(*args):
        """
        Signature:
        Terminate() -> None
        """
        pass
            

    @staticmethod
    def IsInitialised(*args):
        """
        Signature:
        IsInitialised() -> bool
        """
        pass
            

    @staticmethod
    def RecordDefaults(*args):
        """
        Signature:
        RecordDefaults(test: ClashTest, state: LcOpState) -> None
        """
        pass
            

    @staticmethod
    def ApplyDefaults(*args):
        """
        Signature:
        ApplyDefaults(test: ClashTest, state: LcOpState) -> None
        """
        pass
            

    @staticmethod
    def GetDefaultRules(*args):
        """
        Signature:
        GetDefaultRules(state: LcOpState, rules: RuleCollection) -> None
        """
        pass
            

    @staticmethod
    def UpdateDefaultRules(*args):
        """
        Signature:
        UpdateDefaultRules(rules: RuleCollection) -> None
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcClClashProgress(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcClClashProgress """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcClClashProgress
        """
        pass
            

    def Progress(self, *args):
        """
        Signature:
        Progress(fraction_done: float) -> bool
        """
        pass
            

    def ClashesFoundSoFar(self, *args):
        """
        Signature:
        ClashesFoundSoFar(num_clashes: int) -> None
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcClClashTestRunner(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcClClashTestRunner """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcClClashTestRunner
        """
        pass
            

    @staticmethod
    def Initialise(*args):
        """
        Signature:
        Initialise() -> None
        """
        pass
            

    @staticmethod
    def Terminate(*args):
        """
        Signature:
        Terminate() -> None
        """
        pass
            

    @staticmethod
    def IsInitialised(*args):
        """
        Signature:
        IsInitialised() -> bool
        """
        pass
            

    @staticmethod
    def InitialiseForState(*args):
        """
        Signature:
        InitialiseForState(state: LcOpState) -> None
        """
        pass
            

    @staticmethod
    def TerminateForState(*args):
        """
        Signature:
        TerminateForState(state: LcOpState) -> None
        """
        pass
            

    @staticmethod
    def GetInstance(*args):
        """
        Signature:
        GetInstance(state: LcOpState) -> LcClClashTestRunner
        """
        pass
            

    def RunOneTest(self, *args):
        """
        Signature:
        RunOneTest(test: ClashTest) -> bool
        """
        pass
            

    def RunAllTests(self, *args):
        """
        Signature:
        RunAllTests() -> bool
        """
        pass
            

    def CanRunTest(self, *args):
        """
        Signature:
        CanRunTest(test: ClashTest) -> bool
        """
        pass
            

    def CompactOneTest(self, *args):
        """
        Signature:
        CompactOneTest(test: ClashTest) -> None
        """
        pass
            

    def CompactAllTests(self, *args):
        """
        Signature:
        CompactAllTests() -> None
        """
        pass
            

    def SetProgress(self, *args):
        """
        Signature:
        SetProgress(progress_controller: LcClClashProgress) -> None
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcClClashElementHelper(LcOpStateWatcher):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcClClashElementHelper """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcClClashElementHelper
        """
        pass
            

    @staticmethod
    def Initialise(*args):
        """
        Signature:
        Initialise() -> None
        """
        pass
            

    @staticmethod
    def Terminate(*args):
        """
        Signature:
        Terminate() -> None
        """
        pass
            

    @staticmethod
    def IsInitialised(*args):
        """
        Signature:
        IsInitialised() -> bool
        """
        pass
            

    @staticmethod
    def InitialiseForState(*args):
        """
        Signature:
        InitialiseForState(state: LcOpState) -> None
        """
        pass
            

    @staticmethod
    def TerminateForState(*args):
        """
        Signature:
        TerminateForState(state: LcOpState) -> None
        """
        pass
            

    @staticmethod
    def GetInstance(*args):
        """
        Signature:
        GetInstance(state: LcOpState) -> LcClClashElementHelper
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcClClashDisplaySettings(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcClClashDisplaySettings """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcClClashDisplaySettings
        """
        pass
            

    CustomHighlightColors: bool = property(lambda self: None, lambda self, v: None)
    

    ViewContextMode: ViewContextMode = property(lambda self: None, lambda self, v: None)
    

    Object2Highlight: bool = property(lambda self: None, lambda self, v: None)
    

    Object1Highlight: bool = property(lambda self: None, lambda self, v: None)
    

    AutoSimulate: bool = property(lambda self: None, lambda self, v: None)
    

    HideOther: bool = property(lambda self: None, lambda self, v: None)
    

    TransparentDimming: bool = property(lambda self: None, lambda self, v: None)
    

    DimOther: bool = property(lambda self: None, lambda self, v: None)
    

    HighlightAll: bool = property(lambda self: None, lambda self, v: None)
    

    AnimateTransitions: bool = property(lambda self: None, lambda self, v: None)
    

    AutoSave: bool = property(lambda self: None, lambda self, v: None)
    

    AutoLoad: bool = property(lambda self: None, lambda self, v: None)
    

    AutoZoom: bool = property(lambda self: None, lambda self, v: None)
    

    AutoReveal: bool = property(lambda self: None, lambda self, v: None)
    

    SelectionFiltering: SelectionFilteringMode = property(lambda self: None, lambda self, v: None)
    

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcClClashResultHighlighter(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcClClashResultHighlighter """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcClClashResultHighlighter
        """
        pass
            

    @staticmethod
    def Initialise(*args):
        """
        Signature:
        Initialise() -> None
        """
        pass
            

    @staticmethod
    def Terminate(*args):
        """
        Signature:
        Terminate() -> None
        """
        pass
            

    @staticmethod
    def IsInitialised(*args):
        """
        Signature:
        IsInitialised() -> bool
        """
        pass
            

    @staticmethod
    def InitialiseForState(*args):
        """
        Signature:
        InitialiseForState(state: LcOpState) -> None
        """
        pass
            

    @staticmethod
    def TerminateForState(*args):
        """
        Signature:
        TerminateForState(state: LcOpState) -> None
        """
        pass
            

    @staticmethod
    def GetInstance(*args):
        """
        Signature:
        GetInstance(state: LcOpState) -> LcClClashResultHighlighter
        """
        pass
            

    def BeginResultHighlighting(self, *args):
        """
        Signature:
        BeginResultHighlighting(test: ClashTest) -> None
        """
        pass
            

    def EndResultHighlighting(self, *args):
        """
        Signature:
        EndResultHighlighting() -> None
        """
        pass
            

    def IsResultHighlighting(self, *args):
        """
        Signature:
        IsResultHighlighting() -> bool
        """
        pass
            

    def HighlightResult(self, *args):
        """
        Signature:
        HighlightResult(item: SavedItem, test: ClashTest) -> None
        """
        pass
            

    def OnVICButtonDown(self, *args):
        """
        Signature:
        OnVICButtonDown() -> None
        """
        pass
            

    def OnVICButtonUp(self, *args):
        """
        Signature:
        OnVICButtonUp() -> None
        """
        pass
            

    def IssueFilteredOut(self, *args):
        """
        Signature:
        IssueFilteredOut(item: SavedItem) -> bool
        """
        pass
            

    def ResetCurrentResultSavedViewpoint(self, *args):
        """
        Signature:
        ResetCurrentResultSavedViewpoint() -> None
        """
        pass
            

    def SaveCurrentResultView(self, *args):
        """
        Signature:
        SaveCurrentResultView(force_wipe_redlines: bool, not_auto_save: bool) -> None
        """
        pass
            

    def LoadCurrentResultView(self, *args):
        """
        Signature:
        LoadCurrentResultView() -> bool
        """
        pass
            

    def DeleteCurrentResultView(self, *args):
        """
        Signature:
        DeleteCurrentResultView() -> None
        """
        pass
            

    def DeleteResultView(self, *args):
        """
        Signature:
        DeleteResultView(item: SavedItem, force_delete: bool) -> None
        """
        pass
            

    def IsAnimating(self, *args):
        """
        Signature:
        IsAnimating() -> bool
        """
        pass
            

    def ViewChangedSinceLoaded(self, *args):
        """
        Signature:
        ViewChangedSinceLoaded() -> bool
        """
        pass
            

    @staticmethod
    def MakeClashResultView(*args):
        """
        Signature:
        MakeClashResultView(state: LcOpState, result: ClashResultGroup) -> Viewpoint
        """
        pass
            

    @staticmethod
    def MakeClashResultImage(*args):
        """
        Signature:
        MakeClashResultImage(kernel: LcOmWin32Kernel, result: ClashResultGroup, width: int, height: int, purpose: ThumbnailGeneratorPurpose) -> LcOwDIB
        """
        pass
            

    DisplaySettings: LcClClashDisplaySettings = property(lambda self: None, lambda self, v: None)
    

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class LcClCustomClashTests(NativeHandle):
    """ .NET type: Autodesk.Navisworks.Api.Interop.LcClCustomClashTests """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InternalFactory(*args):
        """
        Signature:
        InternalFactory(reserved: NativeHandleInit&) -> NativeHandle
        """
        pass
            

    @staticmethod
    def InternalCreator(*args):
        """
        Signature:
        InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> LcClCustomClashTests
        """
        pass
            

    @staticmethod
    def Count(*args):
        """
        Signature:
        Count() -> int
        """
        pass
            

    @staticmethod
    def GetName(*args):
        """
        Signature:
        GetName(index: int, name: String&) -> None
        """
        pass
            

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

class CurrentIssueChangedEventArgs(EventArgs):
    """ .NET type: Autodesk.Navisworks.Api.Interop.CurrentIssueChangedEventArgs """

    def __init__(self, *args) -> None:
        pass
        


    ShowIssue: bool = property(lambda self: None, lambda self, v: None)
    

class ClashCurrentIssue(object):
    """ .NET type: Autodesk.Navisworks.Api.Interop.ClashCurrentIssue """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def Initialise(*args):
        """
        Signature:
        Initialise() -> None
        """
        pass
            

    @staticmethod
    def Terminate(*args):
        """
        Signature:
        Terminate() -> None
        """
        pass
            

    @staticmethod
    def IsInitialised(*args):
        """
        Signature:
        IsInitialised() -> bool
        """
        pass
            

    @staticmethod
    def OnGotFocus(*args):
        """
        Signature:
        OnGotFocus() -> None
        """
        pass
            

    @staticmethod
    def ClearCurrentIssue(*args):
        """
        Signature:
        ClearCurrentIssue() -> None
        """
        pass
            

    @staticmethod
    def RefreshComment(*args):
        """
        Signature:
        RefreshComment() -> None
        """
        pass
            

    @staticmethod
    def ClearCurrentTest(*args):
        """
        Signature:
        ClearCurrentTest() -> None
        """
        pass
            

    @staticmethod
    def PushDisable(*args):
        """
        Signature:
        PushDisable() -> None
        """
        pass
            

    @staticmethod
    def PopDisable(*args):
        """
        Signature:
        PopDisable() -> None
        """
        pass
            

    CurrentTest: ClashTest = property(lambda self: None, lambda self, v: None)
    

    CurrentIssue: IClashResult = property(lambda self: None, lambda self, v: None)
    

class MinimumClearanceResult(object):
    """ .NET type: Autodesk.Navisworks.Api.Clash.MinimumClearanceResult """

    def __init__(self, *args) -> None:
        pass
        


    Point2OnCenterline: bool = property(lambda self: None, lambda self, v: None)
    

    Point1OnCenterline: bool = property(lambda self: None, lambda self, v: None)
    

    ClosestPointOnSelection2: Point3D = property(lambda self: None, lambda self, v: None)
    

    ClosestPointOnSelection1: Point3D = property(lambda self: None, lambda self, v: None)
    

class DocumentClash(object):
    """ .NET type: Autodesk.Navisworks.Api.Clash.DocumentClash """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def ClashInstance(*args):
        """
        Signature:
        ClashInstance(doc: Document) -> DocumentClash
        """
        pass
            

    @staticmethod
    def CreateInstance(*args):
        """
        Signature:
        CreateInstance(doc: Document) -> DocumentClash
        """
        pass
            

    def TryCalculateMinimumClearance(self, *args):
        """
        Signature:
        TryCalculateMinimumClearance(selection1: ModelItemCollection, selection2: ModelItemCollection, useCenterlines: bool, clearanceResult: MinimumClearanceResult&) -> bool
        """
        pass
            

    TestsData: DocumentClashTests = property(lambda self: None, lambda self, v: None)
    

class DocumentExtensions(object):
    """ .NET type: Autodesk.Navisworks.Api.Clash.DocumentExtensions """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def GetClash(*args):
        """
        Signature:
        GetClash(doc: Document) -> DocumentClash
        """
        pass
            

class ClashImpl(object):
    """ .NET type: Autodesk.Navisworks.Internal.ApiImplementation.ClashImpl """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def InitialiseApi(*args):
        """
        Signature:
        InitialiseApi(document: Document) -> None
        """
        pass
            

    @staticmethod
    def TerminateApi(*args):
        """
        Signature:
        TerminateApi(document: Document) -> None
        """
        pass
            

class ClashResultStatus(Enum):
    """ .NET type: Autodesk.Navisworks.Api.Clash.ClashResultStatus """

    def __init__(self, *args) -> None:
        pass
        


class ClashTestSortMode(Enum):
    """ .NET type: Autodesk.Navisworks.Api.Clash.ClashTestSortMode """

    def __init__(self, *args) -> None:
        pass
        


class ClashSortDirection(Enum):
    """ .NET type: Autodesk.Navisworks.Api.Clash.ClashSortDirection """

    def __init__(self, *args) -> None:
        pass
        


class ClashResultSortMode(Enum):
    """ .NET type: Autodesk.Navisworks.Api.Clash.ClashResultSortMode """

    def __init__(self, *args) -> None:
        pass
        


class ClashTestStatus(Enum):
    """ .NET type: Autodesk.Navisworks.Api.Clash.ClashTestStatus """

    def __init__(self, *args) -> None:
        pass
        


class ClashTestType(Enum):
    """ .NET type: Autodesk.Navisworks.Api.Clash.ClashTestType """

    def __init__(self, *args) -> None:
        pass
        


class ClashTestParts(Enum):
    """ .NET type: Autodesk.Navisworks.Api.Clash.ClashTestParts """

    def __init__(self, *args) -> None:
        pass
        


class ClashResultParts(Enum):
    """ .NET type: Autodesk.Navisworks.Api.Clash.ClashResultParts """

    def __init__(self, *args) -> None:
        pass
        


class ValidateIssueResult(Enum):
    """ .NET type: Autodesk.Navisworks.Api.Interop.ValidateIssueResult """

    def __init__(self, *args) -> None:
        pass
        


class ViewContextMode(Enum):
    """ .NET type: Autodesk.Navisworks.Api.Interop.ViewContextMode """

    def __init__(self, *args) -> None:
        pass
        


class SelectionFilteringMode(Enum):
    """ .NET type: Autodesk.Navisworks.Api.Interop.SelectionFilteringMode """

    def __init__(self, *args) -> None:
        pass
        


class ClashTestsData(object):
    """ .NET type: Autodesk.Navisworks.Api.Clash.ClashTestsData """

    def __init__(self, *args) -> None:
        pass
        

    def CreateCopy(self, *args):
        """
        Signature:
        CreateCopy() -> ClashTestsData
        """
        pass
            

    def Dispose(self, *args):
        """
        Signature:
        Dispose() -> None
        """
        pass
            

    TestsRoot: ClashTestFolder = property(lambda self: None, lambda self, v: None)
    

    Tests: SavedItemCollection = property(lambda self: None, lambda self, v: None)
    

    IsDisposed: bool = property(lambda self: None, lambda self, v: None)
    

    IsReadOnly: bool = property(lambda self: None, lambda self, v: None)
    

class DocumentClashTestsExceptions(object):
    """ .NET type: Autodesk.Navisworks.Api.Interop.DocumentClashTestsExceptions """

    def __init__(self, *args) -> None:
        pass
        

    @staticmethod
    def CannotSetPropertyMessage(*args):
        """
        Signature:
        CannotSetPropertyMessage(propertyName: str) -> str
        """
        pass
            

    LockFailedMessage: str = property(lambda self: None, lambda self, v: None)
    

    InternalErrorMessage: str = property(lambda self: None, lambda self, v: None)
    

    DuplicateGuidMessage: str = property(lambda self: None, lambda self, v: None)
    

    UnsupportedSavedItemMessage: str = property(lambda self: None, lambda self, v: None)
    

    NotInParentMessage: str = property(lambda self: None, lambda self, v: None)
    

    PartIdNotMatchedMessage: str = property(lambda self: None, lambda self, v: None)
    

    NotInClashMessage: str = property(lambda self: None, lambda self, v: None)
    

class DocumentClashTests(object):
    """ .NET type: Autodesk.Navisworks.Api.Clash.DocumentClashTests """

    def __init__(self, *args) -> None:
        pass
        

    def CreateReference(self, *args):
        """
        Signature:
        CreateReference(item: SavedItem) -> SavedItemReference
        """
        pass
            

    def ResolveReference(self, *args):
        """
        Signature:
        ResolveReference(reference: SavedItemReference) -> SavedItem
        """
        pass
            

    def ResolveGuid(self, *args):
        """
        Signature:
        ResolveGuid(value: Guid) -> SavedItem
        """
        pass
            

    def TestsCopyFrom(self, *args):
        """
        Signature:
        TestsCopyFrom(value: SavedItemCollection) -> None
        """
        pass
            

    def CopyFrom(self, *args):
        """
        Signature:
        CopyFrom(value: ClashTestsData) -> None
        """
        pass
            

    def CreateCopy(self, *args):
        """
        Signature:
        CreateCopy() -> ClashTestsData
        """
        pass
            

    def TestsAddCopy(self, *args):
        """
        Signature:
        TestsAddCopy(parent: GroupItem, item: SavedItem) -> None
        """
        pass
            

    def TestsInsertCopy(self, *args):
        """
        Signature:
        TestsInsertCopy(parent: GroupItem, index: int, item: SavedItem) -> None
        """
        pass
            

    def TestsReplaceWithCopy(self, *args):
        """
        Signature:
        TestsReplaceWithCopy(parent: GroupItem, index: int, item: SavedItem) -> None
        """
        pass
            

    def TestsEditResultStatus(self, *args):
        """
        Signature:
        TestsEditResultStatus(result: IClashResult, status: ClashResultStatus) -> None
        """
        pass
            

    def TestsEditResultDescription(self, *args):
        """
        Signature:
        TestsEditResultDescription(result: IClashResult, description: str) -> None
        """
        pass
            

    def TestsEditResultDistance(self, *args):
        """
        Signature:
        TestsEditResultDistance(result: IClashResult, distance: float) -> None
        """
        pass
            

    def TestsEditResultCreatedTime(self, *args):
        """
        Signature:
        TestsEditResultCreatedTime(result: IClashResult, createdTime: DateTime) -> None
        """
        pass
            

    def TestsEditResultApprovedTime(self, *args):
        """
        Signature:
        TestsEditResultApprovedTime(result: IClashResult, approvedTime: DateTime) -> None
        """
        pass
            

    def TestsEditResultApprovedBy(self, *args):
        """
        Signature:
        TestsEditResultApprovedBy(result: IClashResult, approvedBy: str) -> None
        """
        pass
            

    def TestsEditResultAssignedTo(self, *args):
        """
        Signature:
        TestsEditResultAssignedTo(result: IClashResult, assignedTo: str) -> None
        """
        pass
            

    def TestsEditResultBoundingBox(self, *args):
        """
        Signature:
        TestsEditResultBoundingBox(result: IClashResult, boundingBox: BoundingBox3D) -> None
        """
        pass
            

    def TestsEditResultCenter(self, *args):
        """
        Signature:
        TestsEditResultCenter(result: IClashResult, center: Point3D) -> None
        """
        pass
            

    def TestsEditResultComments(self, *args):
        """
        Signature:
        TestsEditResultComments(result: IClashResult, comments: CommentCollection) -> None
        """
        pass
            

    def TestsEditTestFromCopy(self, *args):
        """
        Signature:
        TestsEditTestFromCopy(test: ClashTest, copyFrom: ClashTest) -> None
        """
        pass
            

    def TestsEditDisplayName(self, *args):
        """
        Signature:
        TestsEditDisplayName(item: SavedItem, name: str) -> None
        """
        pass
            

    def TestsMove(self, *args):
        """
        Signature:
        TestsMove(oldParent: GroupItem, oldIndex: int, newParent: GroupItem, newIndex: int) -> None
        """
        pass
            

    def TestsRemoveAt(self, *args):
        """
        Signature:
        TestsRemoveAt(parent: GroupItem, index: int) -> None
        """
        pass
            

    def TestsRemove(self, *args):
        """
        Signature:
        TestsRemove(parent: GroupItem, item: SavedItem) -> None
        """
        pass
            

    def TestsClear(self, *args):
        """
        Signature:
        TestsClear() -> None
        """
        pass
            

    def TestsClearResults(self, *args):
        """
        Signature:
        TestsClearResults(test: ClashTest) -> None
        """
        pass
            

    def TestsRunTest(self, *args):
        """
        Signature:
        TestsRunTest(test: ClashTest) -> None
        """
        pass
            

    def TestsRunAllTests(self, *args):
        """
        Signature:
        TestsRunAllTests() -> None
        """
        pass
            

    def TestsCompactTest(self, *args):
        """
        Signature:
        TestsCompactTest(test: ClashTest) -> None
        """
        pass
            

    def TestsCompactAllTests(self, *args):
        """
        Signature:
        TestsCompactAllTests() -> None
        """
        pass
            

    def TestsSortTests(self, *args):
        """
        Signature:
        TestsSortTests(sortBy: ClashTestSortMode, direction: ClashSortDirection) -> None
        """
        pass
            

    def TestsSortResults(self, *args):
        """
        Signature:
        TestsSortResults(test: ClashTest, sortBy: ClashResultSortMode, direction: ClashSortDirection, proximityTo: Point3D) -> None
        """
        pass
            

    def TestsViewpointForResult(self, *args):
        """
        Signature:
        TestsViewpointForResult(result: IClashResult) -> Viewpoint
        """
        pass
            

    def TestsImageForResult(self, *args):
        """
        Signature:
        TestsImageForResult(result: IClashResult, style: ImageGenerationStyle, width: int, height: int) -> Bitmap
        """
        pass
            

    Tests: SavedItemCollection = property(lambda self: None, lambda self, v: None)
    

    Value: ClashTestsData = property(lambda self: None, lambda self, v: None)
    

    Id: str = property(lambda self: None, lambda self, v: None)
    

