# Auto-generated — Revit 2027 — Autodesk.Revit.Exceptions

class AccessDeniedException(ApplicationException):
    """.NET: Autodesk.Revit.Exceptions.AccessDeniedException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class ApplicationException(Exception):
    """.NET: Autodesk.Revit.Exceptions.ApplicationException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class ArgumentException(ApplicationException):
    """.NET: Autodesk.Revit.Exceptions.ArgumentException"""
    def __init__(self, *args) -> None: ...
    ParamName: str
    Message: str
    FunctionId: FunctionId
    TargetSite: MethodBase
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class ArgumentNullException(ArgumentException):
    """.NET: Autodesk.Revit.Exceptions.ArgumentNullException"""
    def __init__(self, *args) -> None: ...
    ParamName: str
    Message: str
    FunctionId: FunctionId
    TargetSite: MethodBase
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class ArgumentOutOfRangeException(ArgumentException):
    """.NET: Autodesk.Revit.Exceptions.ArgumentOutOfRangeException"""
    def __init__(self, *args) -> None: ...
    ParamName: str
    Message: str
    FunctionId: FunctionId
    TargetSite: MethodBase
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class ArgumentsInconsistentException(ArgumentException):
    """.NET: Autodesk.Revit.Exceptions.ArgumentsInconsistentException"""
    def __init__(self, *args) -> None: ...
    ParamName: str
    Message: str
    FunctionId: FunctionId
    TargetSite: MethodBase
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class AutoJoinFailedException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.AutoJoinFailedException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class BackgroundTaskCancelledException(ApplicationException):
    """.NET: Autodesk.Revit.Exceptions.BackgroundTaskCancelledException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class CannotOpenBothCentralAndLocalException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.CannotOpenBothCentralAndLocalException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class CentralFileCommunicationException(CentralModelException):
    """.NET: Autodesk.Revit.Exceptions.CentralFileCommunicationException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class CentralModelAccessDeniedException(CentralModelException):
    """.NET: Autodesk.Revit.Exceptions.CentralModelAccessDeniedException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class CentralModelAlreadyExistsException(CentralModelException):
    """.NET: Autodesk.Revit.Exceptions.CentralModelAlreadyExistsException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class CentralModelContentionException(CentralModelException):
    """.NET: Autodesk.Revit.Exceptions.CentralModelContentionException"""
    def __init__(self, *args) -> None: ...
    CurrentUser: str
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class CentralModelException(ApplicationException):
    """.NET: Autodesk.Revit.Exceptions.CentralModelException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class CentralModelVersionArchivedException(CentralModelException):
    """.NET: Autodesk.Revit.Exceptions.CentralModelVersionArchivedException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class CheckoutElementsRequestTooLargeException(CentralModelException):
    """.NET: Autodesk.Revit.Exceptions.CheckoutElementsRequestTooLargeException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class CorruptModelException(ApplicationException):
    """.NET: Autodesk.Revit.Exceptions.CorruptModelException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class DefaultValueException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.DefaultValueException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class DirectoryNotEmptyException(ArgumentException):
    """.NET: Autodesk.Revit.Exceptions.DirectoryNotEmptyException"""
    def __init__(self, *args) -> None: ...
    ParamName: str
    Message: str
    FunctionId: FunctionId
    TargetSite: MethodBase
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class DirectoryNotFoundException(IOException):
    """.NET: Autodesk.Revit.Exceptions.DirectoryNotFoundException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class DisabledDisciplineException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.DisabledDisciplineException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class ExternalApplicationException(ApplicationException):
    """.NET: Autodesk.Revit.Exceptions.ExternalApplicationException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class FamilyContextException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.FamilyContextException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class FileAccessException(IOException):
    """.NET: Autodesk.Revit.Exceptions.FileAccessException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class FileArgumentAlreadyExistsException(ArgumentException):
    """.NET: Autodesk.Revit.Exceptions.FileArgumentAlreadyExistsException"""
    def __init__(self, *args) -> None: ...
    ParamName: str
    Message: str
    FunctionId: FunctionId
    TargetSite: MethodBase
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class FileArgumentNotFoundException(ArgumentException):
    """.NET: Autodesk.Revit.Exceptions.FileArgumentNotFoundException"""
    def __init__(self, *args) -> None: ...
    ParamName: str
    Message: str
    FunctionId: FunctionId
    TargetSite: MethodBase
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class FileNotFoundException(IOException):
    """.NET: Autodesk.Revit.Exceptions.FileNotFoundException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class ForbiddenForDynamicUpdateException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.ForbiddenForDynamicUpdateException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class FunctionId:
    """.NET: Autodesk.Revit.Exceptions.FunctionId"""
    def __init__(self, *args) -> None: ...
    Function: str
    Line: int
    File: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class IOException(ApplicationException):
    """.NET: Autodesk.Revit.Exceptions.IOException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class InapplicableDataException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.InapplicableDataException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class InsufficientResourcesException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.InsufficientResourcesException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class InternalException(ApplicationException):
    """.NET: Autodesk.Revit.Exceptions.InternalException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class InvalidDataStreamException(IOException):
    """.NET: Autodesk.Revit.Exceptions.InvalidDataStreamException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class InvalidObjectException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.InvalidObjectException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class InvalidOperationException(ApplicationException):
    """.NET: Autodesk.Revit.Exceptions.InvalidOperationException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class InvalidPathArgumentException(ArgumentException):
    """.NET: Autodesk.Revit.Exceptions.InvalidPathArgumentException"""
    def __init__(self, *args) -> None: ...
    ParamName: str
    Message: str
    FunctionId: FunctionId
    TargetSite: MethodBase
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class ModificationForbiddenException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.ModificationForbiddenException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class ModificationOutsideTransactionException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.ModificationOutsideTransactionException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class NetworkCommunicationException(ApplicationException):
    """.NET: Autodesk.Revit.Exceptions.NetworkCommunicationException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class NotTransmittedModelException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.NotTransmittedModelException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class ObjectAccessException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.ObjectAccessException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class OperationCanceledException(ApplicationException):
    """.NET: Autodesk.Revit.Exceptions.OperationCanceledException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class OptionalFunctionalityNotAvailableException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.OptionalFunctionalityNotAvailableException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class OutdatedDirectlyOpenedCentralException(CentralModelException):
    """.NET: Autodesk.Revit.Exceptions.OutdatedDirectlyOpenedCentralException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class RegenerationFailedException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.RegenerationFailedException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class ResourceNotFoundException(ApplicationException):
    """.NET: Autodesk.Revit.Exceptions.ResourceNotFoundException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class RevitServerCollaborationNotAvailableException(RevitServerException):
    """.NET: Autodesk.Revit.Exceptions.RevitServerCollaborationNotAvailableException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class RevitServerCommunicationException(RevitServerException):
    """.NET: Autodesk.Revit.Exceptions.RevitServerCommunicationException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class RevitServerException(ApplicationException):
    """.NET: Autodesk.Revit.Exceptions.RevitServerException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class RevitServerInternalException(RevitServerException):
    """.NET: Autodesk.Revit.Exceptions.RevitServerInternalException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class RevitServerModelAlreadyExistsException(RevitServerException):
    """.NET: Autodesk.Revit.Exceptions.RevitServerModelAlreadyExistsException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class RevitServerModelNameBreaksConventionException(RevitServerException):
    """.NET: Autodesk.Revit.Exceptions.RevitServerModelNameBreaksConventionException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class RevitServerUnauthenticatedUserException(RevitServerException):
    """.NET: Autodesk.Revit.Exceptions.RevitServerUnauthenticatedUserException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class RevitServerUnauthorizedException(RevitServerException):
    """.NET: Autodesk.Revit.Exceptions.RevitServerUnauthorizedException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class SchemaException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.SchemaException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class ServerInternalException(ApplicationException):
    """.NET: Autodesk.Revit.Exceptions.ServerInternalException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class ServerModelCorruptedException(CentralModelException):
    """.NET: Autodesk.Revit.Exceptions.ServerModelCorruptedException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class TransientElementCreationException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.TransientElementCreationException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class TransmittedModelException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.TransmittedModelException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class UnauthenticatedException(ApplicationException):
    """.NET: Autodesk.Revit.Exceptions.UnauthenticatedException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class WrongUserException(InvalidOperationException):
    """.NET: Autodesk.Revit.Exceptions.WrongUserException"""
    def __init__(self, *args) -> None: ...
    FunctionId: FunctionId
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
