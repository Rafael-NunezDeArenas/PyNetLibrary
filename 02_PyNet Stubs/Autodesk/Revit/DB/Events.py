# Auto-generated — Revit 2027 — Autodesk.Revit.DB.Events

class ApplicationInitializedEventArgs(RevitAPISingleEventArgs):
    """.NET: Autodesk.Revit.DB.Events.ApplicationInitializedEventArgs"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Cancellable: bool

class CreateRelatedFileProgressChangedEventArgs(DataTransferProgressChangedEventArgs):
    """.NET: Autodesk.Revit.DB.Events.CreateRelatedFileProgressChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    DownloadFinished: bool
    FullDownload: bool
    CreatingCloudSharedLocal: bool
    TotalSize: float
    FinishedSize: float
    Speed: float
    TransferMode: DataTransferMode
    Status: RevitAPIEventStatus
    Location: str
    IsValidObject: bool
    Cancellable: bool

class DataTransferMode:
    """.NET: Autodesk.Revit.DB.Events.DataTransferMode"""
    def __init__(self, *args) -> None: ...
    ...

class DataTransferProgressChangedEventArgs(WorksharedOperationProgressChangedEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DataTransferProgressChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    TotalSize: float
    FinishedSize: float
    Speed: float
    TransferMode: DataTransferMode
    Status: RevitAPIEventStatus
    Location: str
    IsValidObject: bool
    Cancellable: bool

class DocumentChangedEventArgs(RevitAPISingleEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    Operation: UndoOperation
    IsValidObject: bool
    Cancellable: bool
    def GetAddedElementIds(self, filter: ElementFilter) -> ICollection: ...
    def GetDeletedElementIds(self, ) -> ICollection: ...
    def GetDocument(self, ) -> Document: ...
    def GetModifiedElementIds(self, filter: ElementFilter) -> ICollection: ...
    def GetTransactionNames(self, ) -> IList: ...

class DocumentClosedEventArgs(RevitAPIPostEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentClosedEventArgs"""
    def __init__(self, *args) -> None: ...
    DocumentId: int
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool

class DocumentClosingEventArgs(RevitAPIPreDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentClosingEventArgs"""
    def __init__(self, *args) -> None: ...
    DocumentId: int
    Document: Document
    IsValidObject: bool
    Cancellable: bool

class DocumentCreatedEventArgs(RevitAPIPostDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentCreatedEventArgs"""
    def __init__(self, *args) -> None: ...
    Document: Document
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool

class DocumentCreatingEventArgs(RevitAPIPreEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentCreatingEventArgs"""
    def __init__(self, *args) -> None: ...
    DocumentType: DocumentType
    Template: str
    IsValidObject: bool
    Cancellable: bool

class DocumentOpenedEventArgs(RevitAPIPostDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentOpenedEventArgs"""
    def __init__(self, *args) -> None: ...
    Document: Document
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool

class DocumentOpeningEventArgs(RevitAPIPreEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentOpeningEventArgs"""
    def __init__(self, *args) -> None: ...
    DocumentType: DocumentType
    PathName: str
    IsValidObject: bool
    Cancellable: bool

class DocumentPrintedEventArgs(RevitAPIPostDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentPrintedEventArgs"""
    def __init__(self, *args) -> None: ...
    Document: Document
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool
    def GetFailedViewElementIds(self, ) -> IList: ...
    def GetPrintedViewElementIds(self, ) -> IList: ...

class DocumentPrintingEventArgs(RevitAPIPreDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentPrintingEventArgs"""
    def __init__(self, *args) -> None: ...
    Document: Document
    IsValidObject: bool
    Cancellable: bool
    def GetSettings(self, ) -> IPrintSetting: ...
    def GetViewElementIds(self, ) -> IList: ...

class DocumentReloadLatestProgressChangedEventArgs(DataTransferProgressChangedEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentReloadLatestProgressChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    ReloadLatestFinished: bool
    IsMerging: bool
    RetryTimes: int
    TotalSize: float
    FinishedSize: float
    Speed: float
    TransferMode: DataTransferMode
    Status: RevitAPIEventStatus
    Location: str
    IsValidObject: bool
    Cancellable: bool

class DocumentReloadedLatestEventArgs(RevitAPIPostDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentReloadedLatestEventArgs"""
    def __init__(self, *args) -> None: ...
    Location: str
    Document: Document
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool

class DocumentReloadingLatestEventArgs(RevitAPIPreDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentReloadingLatestEventArgs"""
    def __init__(self, *args) -> None: ...
    Document: Document
    IsValidObject: bool
    Cancellable: bool

class DocumentSaveToCentralProgressChangedEventArgs(DataTransferProgressChangedEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentSaveToCentralProgressChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    FailureDueToConflicts: bool
    SaveToCentralFinished: bool
    RetryTimes: int
    TotalSize: float
    FinishedSize: float
    Speed: float
    TransferMode: DataTransferMode
    Status: RevitAPIEventStatus
    Location: str
    IsValidObject: bool
    Cancellable: bool

class DocumentSaveToLocalProgressChangedEventArgs(WorksharedOperationProgressChangedEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentSaveToLocalProgressChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    SaveToLocalFinished: bool
    TotalStreams: int
    FinishedStreams: int
    BeforeSaveToCentral: bool
    Status: RevitAPIEventStatus
    Location: str
    IsValidObject: bool
    Cancellable: bool

class DocumentSavedAsEventArgs(RevitAPIPostDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentSavedAsEventArgs"""
    def __init__(self, *args) -> None: ...
    IsSavingAsCentralFile: bool
    OriginalPath: str
    Document: Document
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool

class DocumentSavedEventArgs(RevitAPIPostDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentSavedEventArgs"""
    def __init__(self, *args) -> None: ...
    Document: Document
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool

class DocumentSavingAsEventArgs(RevitAPIPreDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentSavingAsEventArgs"""
    def __init__(self, *args) -> None: ...
    IsSavingAsCentralFile: bool
    PathName: str
    Document: Document
    IsValidObject: bool
    Cancellable: bool

class DocumentSavingEventArgs(RevitAPIPreDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentSavingEventArgs"""
    def __init__(self, *args) -> None: ...
    Document: Document
    IsValidObject: bool
    Cancellable: bool

class DocumentSynchronizedWithCentralEventArgs(RevitAPIPostDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentSynchronizedWithCentralEventArgs"""
    def __init__(self, *args) -> None: ...
    Document: Document
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool

class DocumentSynchronizingWithCentralEventArgs(RevitAPIPreDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentSynchronizingWithCentralEventArgs"""
    def __init__(self, *args) -> None: ...
    Options: SynchronizeWithCentralOptions
    Comments: str
    Location: str
    Document: Document
    IsValidObject: bool
    Cancellable: bool

class DocumentWorksharingEnabledEventArgs(RevitAPISingleEventArgs):
    """.NET: Autodesk.Revit.DB.Events.DocumentWorksharingEnabledEventArgs"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Cancellable: bool
    def GetDocument(self, ) -> Document: ...

class ElementTypeDuplicatedEventArgs(RevitAPIPostDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.ElementTypeDuplicatedEventArgs"""
    def __init__(self, *args) -> None: ...
    NewElementTypeId: ElementId
    NewName: str
    OriginalElementTypeId: ElementId
    Document: Document
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool

class ElementTypeDuplicatingEventArgs(RevitAPIPreDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.ElementTypeDuplicatingEventArgs"""
    def __init__(self, *args) -> None: ...
    ElementTypeId: ElementId
    Document: Document
    IsValidObject: bool
    Cancellable: bool

class EventStatus:
    """.NET: Autodesk.Revit.DB.Events.EventStatus"""
    def __init__(self, *args) -> None: ...
    ...

class FailuresProcessingEventArgs(RevitAPISingleEventArgs):
    """.NET: Autodesk.Revit.DB.Events.FailuresProcessingEventArgs"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Cancellable: bool
    def GetFailuresAccessor(self, ) -> FailuresAccessor: ...
    def GetProcessingResult(self, ) -> FailureProcessingResult: ...
    def SetProcessingResult(self, result: FailureProcessingResult) -> None: ...

class FamilyLoadedIntoDocumentEventArgs(RevitAPIPostDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.FamilyLoadedIntoDocumentEventArgs"""
    def __init__(self, *args) -> None: ...
    NewFamilyId: ElementId
    OriginalFamilyId: ElementId
    FamilyPath: str
    FamilyName: str
    Document: Document
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool

class FamilyLoadingIntoDocumentEventArgs(RevitAPIPreDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.FamilyLoadingIntoDocumentEventArgs"""
    def __init__(self, *args) -> None: ...
    FamilyPath: str
    FamilyName: str
    Document: Document
    IsValidObject: bool
    Cancellable: bool

class FileExportedEventArgs(RevitAPIPostDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.FileExportedEventArgs"""
    def __init__(self, *args) -> None: ...
    BackgroundOperation: bool
    Format: ImportExportFileFormat
    Path: str
    Document: Document
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool

class FileExportingEventArgs(RevitAPIPreDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.FileExportingEventArgs"""
    def __init__(self, *args) -> None: ...
    BackgroundOperation: bool
    Format: ImportExportFileFormat
    Path: str
    Document: Document
    IsValidObject: bool
    Cancellable: bool

class FileImportedEventArgs(RevitAPIPostDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.FileImportedEventArgs"""
    def __init__(self, *args) -> None: ...
    ImportedInstanceId: ElementId
    Format: ImportExportFileFormat
    Path: str
    Document: Document
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool

class FileImportingEventArgs(RevitAPIPreDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.FileImportingEventArgs"""
    def __init__(self, *args) -> None: ...
    Format: ImportExportFileFormat
    Path: str
    Document: Document
    IsValidObject: bool
    Cancellable: bool

class LinkedResourceOpenedEventArgs(RevitAPIPostDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.LinkedResourceOpenedEventArgs"""
    def __init__(self, *args) -> None: ...
    LinkedResourcePathName: str
    ResourceTypeId: ElementId
    ResourceType: ExternalResourceType
    Document: Document
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool

class LinkedResourceOpeningEventArgs(RevitAPIPreEventArgs):
    """.NET: Autodesk.Revit.DB.Events.LinkedResourceOpeningEventArgs"""
    def __init__(self, *args) -> None: ...
    LinkedResourcePathName: str
    ResourceType: ExternalResourceType
    IsValidObject: bool
    Cancellable: bool

class PostDocEventArgs(PostEventArgs):
    """.NET: Autodesk.Revit.DB.Events.PostDocEventArgs"""
    def __init__(self, *args) -> None: ...
    Document: Document
    Status: EventStatus
    Cancellable: bool
    Cancel: bool

class PostEventArgs(RevitEventArgs):
    """.NET: Autodesk.Revit.DB.Events.PostEventArgs"""
    def __init__(self, *args) -> None: ...
    Status: EventStatus
    Cancellable: bool
    Cancel: bool

class PreDocEventArgs(PreEventArgs):
    """.NET: Autodesk.Revit.DB.Events.PreDocEventArgs"""
    def __init__(self, *args) -> None: ...
    Document: Document
    Cancellable: bool
    Cancel: bool

class PreEventArgs(RevitEventArgs):
    """.NET: Autodesk.Revit.DB.Events.PreEventArgs"""
    def __init__(self, *args) -> None: ...
    Cancellable: bool
    Cancel: bool

class ProgressChangedEventArgs(RevitAPISingleEventArgs):
    """.NET: Autodesk.Revit.DB.Events.ProgressChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    Caption: str
    UpperRange: int
    LowerRange: int
    Position: int
    Stage: ProgressStage
    IsValidObject: bool
    Cancellable: bool
    def Cancel(self, ) -> None: ...

class ProgressStage:
    """.NET: Autodesk.Revit.DB.Events.ProgressStage"""
    def __init__(self, *args) -> None: ...
    ...

class RevitAPIEventArgs(EventArgs):
    """.NET: Autodesk.Revit.DB.Events.RevitAPIEventArgs"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Cancellable: bool
    def Dispose(self, ) -> None: ...
    def IsCancelled(self, ) -> bool: ...

class RevitAPIEventStatus:
    """.NET: Autodesk.Revit.DB.Events.RevitAPIEventStatus"""
    def __init__(self, *args) -> None: ...
    ...

class RevitAPIPostDocEventArgs(RevitAPIPostEventArgs):
    """.NET: Autodesk.Revit.DB.Events.RevitAPIPostDocEventArgs"""
    def __init__(self, *args) -> None: ...
    Document: Document
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool

class RevitAPIPostEventArgs(RevitAPIEventArgs):
    """.NET: Autodesk.Revit.DB.Events.RevitAPIPostEventArgs"""
    def __init__(self, *args) -> None: ...
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool

class RevitAPIPreDocEventArgs(RevitAPIPreEventArgs):
    """.NET: Autodesk.Revit.DB.Events.RevitAPIPreDocEventArgs"""
    def __init__(self, *args) -> None: ...
    Document: Document
    IsValidObject: bool
    Cancellable: bool

class RevitAPIPreEventArgs(RevitAPIEventArgs):
    """.NET: Autodesk.Revit.DB.Events.RevitAPIPreEventArgs"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Cancellable: bool
    def Cancel(self, ) -> None: ...

class RevitAPISingleEventArgs(RevitAPIEventArgs):
    """.NET: Autodesk.Revit.DB.Events.RevitAPISingleEventArgs"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Cancellable: bool

class RevitEventArgs(EventArgs):
    """.NET: Autodesk.Revit.DB.Events.RevitEventArgs"""
    def __init__(self, *args) -> None: ...
    Cancellable: bool
    Cancel: bool

class UndoOperation:
    """.NET: Autodesk.Revit.DB.Events.UndoOperation"""
    def __init__(self, *args) -> None: ...
    ...

class ViewExportedEventArgs(RevitAPIPostDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.ViewExportedEventArgs"""
    def __init__(self, *args) -> None: ...
    ViewId: ElementId
    Document: Document
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool

class ViewExportingEventArgs(RevitAPIPreDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.ViewExportingEventArgs"""
    def __init__(self, *args) -> None: ...
    ViewId: ElementId
    Document: Document
    IsValidObject: bool
    Cancellable: bool

class ViewPrintedEventArgs(RevitAPIPostDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.ViewPrintedEventArgs"""
    def __init__(self, *args) -> None: ...
    View: View
    TotalViews: int
    Index: int
    Document: Document
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool

class ViewPrintingEventArgs(RevitAPIPreDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.ViewPrintingEventArgs"""
    def __init__(self, *args) -> None: ...
    View: View
    TotalViews: int
    Index: int
    Document: Document
    IsValidObject: bool
    Cancellable: bool
    def GetSettings(self, ) -> IPrintSetting: ...

class ViewsExportedByContextEventArgs(RevitAPIPostDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.ViewsExportedByContextEventArgs"""
    def __init__(self, *args) -> None: ...
    Document: Document
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool
    def GetViewIds(self, ) -> IList: ...

class ViewsExportingByContextEventArgs(RevitAPIPreDocEventArgs):
    """.NET: Autodesk.Revit.DB.Events.ViewsExportingByContextEventArgs"""
    def __init__(self, *args) -> None: ...
    Document: Document
    IsValidObject: bool
    Cancellable: bool
    def GetViewIds(self, ) -> IList: ...

class WorksharedOperationProgressChangedEventArgs(RevitAPISingleEventArgs):
    """.NET: Autodesk.Revit.DB.Events.WorksharedOperationProgressChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    Status: RevitAPIEventStatus
    Location: str
    IsValidObject: bool
    Cancellable: bool
