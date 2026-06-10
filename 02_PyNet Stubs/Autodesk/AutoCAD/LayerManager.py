# Auto-generated — Civil 26 — Autodesk.AutoCAD.LayerManager

class AndExpression:
    """.NET: Autodesk.AutoCAD.LayerManager.AndExpression"""
    def __init__(self, *args) -> None: ...
    def GetRelationalExpressions(self, ) -> list: ...

class LayerCollection:
    """.NET: Autodesk.AutoCAD.LayerManager.LayerCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ObjectId
    def Add(self, value: ObjectId) -> None: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: ObjectId) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, value: ObjectId) -> None: ...

class LayerFilter(RXObject):
    """.NET: Autodesk.AutoCAD.LayerManager.LayerFilter"""
    def __init__(self, *args) -> None: ...
    FilterExpression: str
    DisplayImages: LayerFilterDisplayImages
    IsIdFilter: bool
    IsProxy: bool
    AllowDelete: bool
    DynamicallyGenerated: bool
    AllowNested: bool
    NestedFilters: LayerFilterCollection
    Parent: LayerFilter
    AllowRename: bool
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CompareTo(self, otherFilter: LayerFilter) -> bool: ...
    def Filter(self, layer: LayerTableRecord) -> bool: ...
    def GenerateNested(self, ) -> None: ...
    def GetFilterExpressionTree(self, ) -> list: ...
    def ShowEditor(self, ) -> DialogResult: ...

class LayerFilterCollection:
    """.NET: Autodesk.AutoCAD.LayerManager.LayerFilterCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: LayerFilter
    def Add(self, value: LayerFilter) -> None: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: LayerFilter) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, value: LayerFilter) -> None: ...

class LayerFilterDisplayImages:
    """.NET: Autodesk.AutoCAD.LayerManager.LayerFilterDisplayImages"""
    def __init__(self, *args) -> None: ...
    SelectedImageIndex: int
    ImageIndex: int
    ImageListHandle: IntPtr

class LayerFilterTree:
    """.NET: Autodesk.AutoCAD.LayerManager.LayerFilterTree"""
    def __init__(self, *args) -> None: ...
    Current: LayerFilter
    Root: LayerFilter

class LayerGroup(LayerFilter):
    """.NET: Autodesk.AutoCAD.LayerManager.LayerGroup"""
    def __init__(self, *args) -> None: ...
    LayerIds: LayerCollection
    FilterExpression: str
    DisplayImages: LayerFilterDisplayImages
    IsIdFilter: bool
    IsProxy: bool
    AllowDelete: bool
    DynamicallyGenerated: bool
    AllowNested: bool
    NestedFilters: LayerFilterCollection
    Parent: LayerFilter
    AllowRename: bool
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class RelationalExpression:
    """.NET: Autodesk.AutoCAD.LayerManager.RelationalExpression"""
    def __init__(self, *args) -> None: ...
    Constant: str
    Variable: str
