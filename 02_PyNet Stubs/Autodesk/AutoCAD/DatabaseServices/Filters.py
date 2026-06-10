# Auto-generated — Civil 26 — Autodesk.AutoCAD.DatabaseServices.Filters

class Filter(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Filters.Filter"""
    def __init__(self, *args) -> None: ...
    IndexClass: RXClass
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

class FilteredBlockIterator(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Filters.FilteredBlockIterator"""
    def __init__(self, *args) -> None: ...
    BuffersForComposition: bool
    EstimatedHitFraction: float
    Id: ObjectId
    Next: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Accepts(self, id: ObjectId) -> bool: ...
    def AddToBuffer(self, id: ObjectId) -> None: ...
    def Seek(self, id: ObjectId) -> None: ...
    def Start(self, ) -> None: ...

class Index(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Filters.Index"""
    def __init__(self, *args) -> None: ...
    IsUptoDate: bool
    LastUpdatedAtU: DateTime
    LastUpdatedAt: DateTime
    ObjectBeingIndexedId: ObjectId
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
    def GetIterator(self, filter: Filter) -> FilteredBlockIterator: ...
    def RebuildFull(self, indexData: IndexUpdateData) -> None: ...

class IndexUpdateData(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Filters.IndexUpdateData"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddId(self, id: ObjectId) -> None: ...
    def GetIdData(self, id: ObjectId) -> int: ...
    def GetIdDataPtr(self, id: ObjectId) -> IntPtr: ...
    def GetIdFlags(self, id: ObjectId) -> int: ...
    def SetIdData(self, id: ObjectId, data: IntPtr) -> None: ...
    def SetIdFlags(self, id: ObjectId, flags: int) -> None: ...

class LayerFilter(Filter):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Filters.LayerFilter"""
    def __init__(self, *args) -> None: ...
    LayerCount: int
    IsValid: bool
    IndexClass: RXClass
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
    def Add(self, layer: str) -> None: ...
    def GetAt(self, index: int, name: str) -> None: ...
    def Remove(self, layer: str) -> None: ...

class LayerIndex(Index):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Filters.LayerIndex"""
    def __init__(self, *args) -> None: ...
    IsUptoDate: bool
    LastUpdatedAtU: DateTime
    LastUpdatedAt: DateTime
    ObjectBeingIndexedId: ObjectId
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
    def Compute(self, pLT: LayerTable, record: BlockTableRecord) -> None: ...

class SpatialFilter(Filter):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Filters.SpatialFilter"""
    def __init__(self, *args) -> None: ...
    Inverted: bool
    OriginalInverseBlockTransform: Matrix3d
    ClipSpaceToWorldCoordinateSystemTransform: Matrix3d
    HasPerspectiveCamera: bool
    Definition: SpatialFilterDefinition
    IndexClass: RXClass
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
    def ClipVolumeIntersectsExtents(self, ext: Extents3d) -> bool: ...
    def GetQueryBounds(self, blockReference: BlockReference) -> Extents3d: ...
    def GetVolume(self, ) -> SpatialFilterVolume: ...
    def SetPerspectiveCamera(self, fromPoint: Point3d) -> None: ...

class SpatialFilterDefinition:
    """.NET: Autodesk.AutoCAD.DatabaseServices.Filters.SpatialFilterDefinition"""
    def __init__(self, *args) -> None: ...
    Enabled: bool
    BackClip: float
    FrontClip: float
    Elevation: float
    Normal: Vector3d
    def GetPoints(self, ) -> Point2dCollection: ...

class SpatialFilterVolume:
    """.NET: Autodesk.AutoCAD.DatabaseServices.Filters.SpatialFilterVolume"""
    def __init__(self, *args) -> None: ...
    ViewField: Vector2d
    UpDirection: Vector3d
    ToPoint: Point3d
    FromPoint: Point3d

class SpatialIndex(Index):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Filters.SpatialIndex"""
    def __init__(self, *args) -> None: ...
    IsUptoDate: bool
    LastUpdatedAtU: DateTime
    LastUpdatedAt: DateTime
    ObjectBeingIndexedId: ObjectId
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
