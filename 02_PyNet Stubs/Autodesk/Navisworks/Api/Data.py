# encoding: utf-8
# module Autodesk.Navisworks.Api.Data calls itself Data
# from Autodesk.Navisworks.Api, Version=19.0.1374.1, Culture=neutral, PublicKeyToken=d85e58fa5af9b484
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DatabaseActionType(Enum, IComparable, IFormattable, IConvertible):
    """
    Enumeration of database edit.
    
    enum DatabaseActionType, values: Do (0), Redo (1), Undo (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Do = None
    Redo = None
    Undo = None
    value__ = None


class DatabaseChange(object):
    """ The element of Autodesk.Navisworks.Api.Data.DatabaseChangeCollection DatabaseChangeCollection. """
    ChangedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of change Autodesk.Navisworks.Api.Data.DatabaseChangeTypesDatabaseChangeTypes.

Get: ChangedType(self: DatabaseChange) -> DatabaseChangeTypes

"""

    RowId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The row id of current database change, use the RowId to find out all columns.

Get: RowId(self: DatabaseChange) -> Int64

"""

    TableName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The table name of current database change.

Get: TableName(self: DatabaseChange) -> str

"""



class DatabaseChangeCollection(object, IEnumerable[DatabaseChange], IEnumerable):
    """ Collection of Autodesk.Navisworks.Api.Data.DatabaseChangeDatabaseChange that only supports Enumerable style interfaces """
    def GetEnumerator(self):
        """
        GetEnumerator(self: DatabaseChangeCollection) -> IEnumerator[DatabaseChange]
        
            Returns an enumerator that can iterate through the collection.
            Returns: An System.Collections.IEnumeratorIEnumerator that can be used to iterate through the collection.
        """
        pass

    def InternalGetEnumerator(self):
        """ InternalGetEnumerator(self: DatabaseChangeCollection) -> IEnumerator """
        pass

    def ToString(self):
        """
        ToString(self: DatabaseChangeCollection) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def Where(self, *__args):
        """
        Where(self: DatabaseChangeCollection, changeType: DatabaseChangeTypes) -> IEnumerable[DatabaseChange]
        
            Filters the changes based on changeType
        
            changeType: Which Autodesk.Navisworks.Api.Data.DatabaseChangeTypesDatabaseChangeTypes will be cared
        Where(self: DatabaseChangeCollection, tableNames: str) -> IEnumerable[DatabaseChange]
        
            Filters the changes based on tablesName
        
            tableNames: Which tables would be cared. support multi tables and use white space between table names, Like "ABC def".
        Where(self: DatabaseChangeCollection, tableNames: str, changeType: DatabaseChangeTypes) -> IEnumerable[DatabaseChange]
        
            Filters the changes based on tableNames and changeType
        
            tableNames: Which tables would be cared. support multi tables and use white space between table names, Like "ABC def".
            changeType: Which Autodesk.Navisworks.Api.Data.DatabaseChangeTypesDatabaseChangeTypes will be cared
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[DatabaseChange](enumerable: IEnumerable[DatabaseChange], value: DatabaseChange) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class DatabaseChangedAction(Enum, IComparable, IFormattable, IConvertible):
    """
    Determines which action should do after transaction
    
    enum DatabaseChangedAction, values: Edited (0), Reset (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Edited = None
    Reset = None
    value__ = None


class DatabaseChangedEventArgs(EventArgs):
    """ Event arguments when a database changed event. """
    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the action that caused the event

Get: Action(self: DatabaseChangedEventArgs) -> DatabaseChangedAction

"""

    ActionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets action type of database editing.

Get: ActionType(self: DatabaseChangedEventArgs) -> DatabaseActionType

"""

    Changes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets change collection that were edited, if Action is not Edited, Changes will be null.

Get: Changes(self: DatabaseChangedEventArgs) -> DatabaseChangeCollection

"""



class DatabaseChangeTypes(Enum, IComparable, IFormattable, IConvertible):
    """
    Change type
    
    enum (flags) DatabaseChangeTypes, values: All (7), Delete (2), Insert (1), None (0), Update (4)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    All = None
    Delete = None
    Insert = None
    None = None
    Update = None
    value__ = None


class DatabaseException(InvalidOperationException, ISerializable, _Exception):
    """
    The exception that is thrown when database failed
    
    DatabaseException(errorCode: int, message: str, innerException: Exception)
    DatabaseException(errorCode: int, message: str)
    DatabaseException(errorCode: int)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, errorCode, message=None, innerException=None):
        """
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, errorCode: int, message: str, innerException: Exception)
        __new__(cls: type, errorCode: int, message: str)
        __new__(cls: type, errorCode: int)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ErrorCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get database failed error code.

Get: ErrorCode(self: DatabaseException) -> int

"""


    SerializeObjectState = None


class NavisworksCommand(DbCommand, IComponent, IDisposable, IDbCommand):
    """
    Implementation of DbCommand.
    
    NavisworksCommand(commandText: str, connection: NavisworksConnection)
    NavisworksCommand(connection: NavisworksConnection)
    NavisworksCommand(commandText: str)
    NavisworksCommand()
    """
    def Cancel(self):
        """
        Cancel(self: NavisworksCommand)
            Not implemented
        """
        pass

    def CreateDbParameter(self, *args): #cannot find CLR method
        """
        CreateDbParameter(self: NavisworksCommand) -> DbParameter
        
            Forwards to the local CreateParameter() function
            Returns: Returns a NavisWorksDataReader object
        """
        pass

    def CreateParameter(self):
        """
        CreateParameter(self: NavisworksCommand) -> NavisworksParameter
        
            Create a new parameter.
            Returns: Return Autodesk.Navisworks.Api.Data.NavisworksParameterNavisworksParameter
        """
        pass

    def Dispose(self):
        """ Dispose(self: NavisworksCommand, A_0: bool) """
        pass

    def ExecuteDbDataReader(self, *args): #cannot find CLR method
        """
        ExecuteDbDataReader(self: NavisworksCommand, behavior: CommandBehavior) -> DbDataReader
        
            Creates a new NavisWorksDataReader to execute/iterate the array of prepared statements
        
            behavior: The behavior the data reader should adopt
            Returns: Returns a NavisWorksDataReader object
        """
        pass

    def ExecuteDbDataReaderAsync(self, *args): #cannot find CLR method
        """
        ExecuteDbDataReaderAsync(self: DbCommand, behavior: CommandBehavior, cancellationToken: CancellationToken) -> Task[DbDataReader]
        
            Providers should implement this method to provide a non-default implementation for erload:System.Data.Common.DbCommand.ExecuteReader overloads.  
         The default implementation 
             invokes the synchronous System.Data.Common.DbCommand.ExecuteReader method and returns a completed task, blocking the calling thread. The default implementation will return a 
             cancelled task if passed an already cancelled cancellation token. Exceptions thrown by ExecuteReader will be communicated via the returned Task Exception property.  
         This method 
             accepts a cancellation token that can be used to request the operation to be cancelled early. Implementations may ignore this request.
        
        
            behavior: Options for statement execution and data retrieval.
            cancellationToken: The token to monitor for cancellation requests.
            Returns: A task representing the asynchronous operation.
        """
        pass

    def ExecuteNonQuery(self):
        """
        ExecuteNonQuery(self: NavisworksCommand) -> int
        
            Execute the command and return the number of rows inserted/updated affected by it.
            Returns: The number of rows inserted/updated affected by this executed command
        """
        pass

    def ExecuteReader(self, behavior=None):
        """
        ExecuteReader(self: NavisworksCommand, behavior: CommandBehavior) -> NavisWorksDataReader
        
            Overrides the default behavior to return a NavisWorksDataReader specialization class
        
            behavior: The flags to be associated with the reader
            Returns: Return Autodesk.Navisworks.Api.Data.NavisWorksDataReaderNavisWorksDataReader
        ExecuteReader(self: NavisworksCommand) -> NavisWorksDataReader
        
            Overrides the default behavior of DbDataReader to return a specialized NavisWorksDataReader class
            Returns: Return Autodesk.Navisworks.Api.Data.NavisWorksDataReaderNavisWorksDataReader
        """
        pass

    def ExecuteScalar(self):
        """
        ExecuteScalar(self: NavisworksCommand) -> object
        
            Execute the command and return the first column of the first row of the resultset
        (if present), or null if no resultset was returned.
            Returns: The first column of the first row of the first resultset from the query
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or by its System.ComponentModel.Container.
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or ll if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A 
             value of lse is usually appropriate. ue to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the 
             remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def Prepare(self):
        """
        Prepare(self: NavisworksCommand)
            Does nothing.  Commands are prepared as they are executed the first time, and kept in prepared state afterwards.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, commandText: str, connection: NavisworksConnection)
        __new__(cls: type, connection: NavisworksConnection)
        __new__(cls: type, commandText: str)
        __new__(cls: type)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    CommandText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The SQL command text associated with the command

Get: CommandText(self: NavisworksCommand) -> str

Set: CommandText(self: NavisworksCommand) = value
"""

    CommandTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not implement

Get: CommandTimeout(self: NavisworksCommand) -> int

Set: CommandTimeout(self: NavisworksCommand) = value
"""

    CommandType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of the command. NavisworksCommand only supports CommandType.Text

Get: CommandType(self: NavisworksCommand) -> CommandType

Set: CommandType(self: NavisworksCommand) = value
"""

    Connection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connection associated with this command

Get: Connection(self: NavisworksCommand) -> NavisworksConnection

Set: Connection(self: NavisworksCommand) = value
"""

    DbConnection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Forwards to the local Connection property

"""

    DbParameterCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Forwards to the local Parameters property

"""

    DbTransaction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not implement

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    DesignTimeVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not implement

Get: DesignTimeVisible(self: NavisworksCommand) -> bool

Set: DesignTimeVisible(self: NavisworksCommand) = value
"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not implement, will implement
Returns the NavisworksParameterCollection for this command

Get: Parameters(self: NavisworksCommand) -> NavisworksParameterCollection

"""

    UpdatedRowSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not implement

Get: UpdatedRowSource(self: NavisworksCommand) -> UpdateRowSource

Set: UpdatedRowSource(self: NavisworksCommand) = value
"""



class NavisworksConnection(DbConnection, IComponent, IDisposable, IDbConnection):
    """ Implementation of DbConnection. """
    def BeginDbTransaction(self, A_0):
        """
        BeginDbTransaction(self: NavisworksConnection, A_0: IsolationLevel) -> DbTransaction
        
            Not implement
        """
        pass

    def ChangeDatabase(self, databaseName):
        """
        ChangeDatabase(self: NavisworksConnection, databaseName: str)
            Not implement
        """
        pass

    def Close(self):
        """
        Close(self: NavisworksConnection)
            Does nothing, always keep open.
        """
        pass

    def CreateCommand(self):
        """
        CreateCommand(self: NavisworksConnection) -> NavisworksCommand
        
            Create a new NavisworksCommand and associate it with this connection.
            Returns: Returns an instantiated NavisworksCommand object already assigned to this connection.
        """
        pass

    def CreateDbCommand(self, *args): #cannot find CLR method
        """
        CreateDbCommand(self: NavisworksConnection) -> DbCommand
        
            Forwards to the local CreateCommand() function
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Component, disposing: bool)
            Releases the unmanaged resources used by the System.ComponentModel.Component and optionally releases the managed resources.
        
            disposing: ue to release both managed and unmanaged resources; lse to release only unmanaged resources.
        """
        pass

    def GetSchema(self, collectionName=None, restrictionValues=None):
        """
        GetSchema(self: NavisworksConnection, collectionName: str, restrictionValues: Array[str]) -> DataTable
        
            Returns schema information for the data source of this connection
        using the specified string for the schema name and the specified string array
        for the restriction values.
        
            collectionName: Specifies the name of the schema to return. Now only support "INDEXES" and "INDEXCOLUMNS"
            restrictionValues: Specifies a set of restriction values for the requested schema.
            Returns: A System.Data.DataTable that contains schema information.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or by its System.ComponentModel.Container.
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or ll if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    def InternalGetConnection(self):
        """ InternalGetConnection(self: NavisworksConnection) -> LcUSQLiteConnection """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A 
             value of lse is usually appropriate. ue to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the 
             remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def OnStateChange(self, *args): #cannot find CLR method
        """
        OnStateChange(self: DbConnection, stateChange: StateChangeEventArgs)
            Raises the System.Data.Common.DbConnection.StateChange event.
        
            stateChange: A System.Data.StateChangeEventArgs that contains the event data.
        """
        pass

    def Open(self):
        """
        Open(self: NavisworksConnection)
            Does nothing, connection is automatically opened by DocumentDatabase.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    ConnectionString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not implement

Get: ConnectionString(self: NavisworksConnection) -> str

Set: ConnectionString(self: NavisworksConnection) = value
"""

    Database = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not implement

Get: Database(self: NavisworksConnection) -> str

"""

    DataSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not implement

Get: DataSource(self: NavisworksConnection) -> str

"""

    DbProviderFactory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Data.Common.DbProviderFactory for this System.Data.Common.DbConnection.

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    ServerVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not implement

Get: ServerVersion(self: NavisworksConnection) -> str

"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the state of the connection

Get: State(self: NavisworksConnection) -> ConnectionState

"""



class NavisworksDataAdapter(DbDataAdapter, IComponent, IDisposable, IDataAdapter, IDbDataAdapter, ICloneable):
    """
    Implementation of DbDataAdapter.
    
    NavisworksDataAdapter(commandText: str, connection: NavisworksConnection)
    NavisworksDataAdapter(selectCommand: NavisworksCommand)
    NavisworksDataAdapter()
    """
    def AddToBatch(self, *args): #cannot find CLR method
        """
        AddToBatch(self: DbDataAdapter, command: IDbCommand) -> int
        
            Adds a System.Data.IDbCommand to the current batch.
        
            command: The System.Data.IDbCommand to add to the batch.
            Returns: The number of commands in the batch before adding the System.Data.IDbCommand.
        """
        pass

    def ClearBatch(self, *args): #cannot find CLR method
        """
        ClearBatch(self: DbDataAdapter)
            Removes all System.Data.IDbCommand objects from the batch.
        """
        pass

    def CloneInternals(self, *args): #cannot find CLR method
        """
        CloneInternals(self: DataAdapter) -> DataAdapter
        
            Creates a copy of this instance of System.Data.Common.DataAdapter.
            Returns: The cloned instance of System.Data.Common.DataAdapter.
        """
        pass

    def CreateRowUpdatedEvent(self, *args): #cannot find CLR method
        """
        CreateRowUpdatedEvent(self: DbDataAdapter, dataRow: DataRow, command: IDbCommand, statementType: StatementType, tableMapping: DataTableMapping) -> RowUpdatedEventArgs
        
            Initializes a new instance of the System.Data.Common.RowUpdatedEventArgs class.
        
            dataRow: The System.Data.DataRow used to update the data source.
            command: The System.Data.IDbCommand executed during the System.Data.IDataAdapter.Update(System.Data.DataSet).
            statementType: Whether the command is an UPDATE, INSERT, DELETE, or SELECT statement.
            tableMapping: A System.Data.Common.DataTableMapping object.
            Returns: A new instance of the System.Data.Common.RowUpdatedEventArgs class.
        """
        pass

    def CreateRowUpdatingEvent(self, *args): #cannot find CLR method
        """
        CreateRowUpdatingEvent(self: DbDataAdapter, dataRow: DataRow, command: IDbCommand, statementType: StatementType, tableMapping: DataTableMapping) -> RowUpdatingEventArgs
        
            Initializes a new instance of the System.Data.Common.RowUpdatingEventArgs class.
        
            dataRow: The System.Data.DataRow that updates the data source.
            command: The System.Data.IDbCommand to execute during the System.Data.IDataAdapter.Update(System.Data.DataSet).
            statementType: Whether the command is an UPDATE, INSERT, DELETE, or SELECT statement.
            tableMapping: A System.Data.Common.DataTableMapping object.
            Returns: A new instance of the System.Data.Common.RowUpdatingEventArgs class.
        """
        pass

    def CreateTableMappings(self, *args): #cannot find CLR method
        """
        CreateTableMappings(self: DataAdapter) -> DataTableMappingCollection
        
            Creates a new System.Data.Common.DataTableMappingCollection.
            Returns: A new table mapping collection.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: DbDataAdapter, disposing: bool)
            Releases the unmanaged resources used by the System.Data.Common.DbDataAdapter and optionally releases the managed resources.
        
            disposing: ue to release both managed and unmanaged resources; lse to release only unmanaged resources.
        """
        pass

    def ExecuteBatch(self, *args): #cannot find CLR method
        """
        ExecuteBatch(self: DbDataAdapter) -> int
        
            Executes the current batch.
            Returns: The return value from the last command in the batch.
        """
        pass

    def Fill(self, *__args):
        """
        Fill(self: DbDataAdapter, dataSet: DataSet, startRecord: int, maxRecords: int, srcTable: str, command: IDbCommand, behavior: CommandBehavior) -> int
        
            Adds or refreshes rows in a specified range in the System.Data.DataSet to match those in the data source using the System.Data.DataSet and source table names, command string, and 
             command behavior.
        
        
            dataSet: A System.Data.DataSet to fill with records and, if necessary, schema.
            startRecord: The zero-based record number to start with.
            maxRecords: The maximum number of records to retrieve.
            srcTable: The name of the source table to use for table mapping.
            command: The SQL SELECT statement used to retrieve rows from the data source.
            behavior: One of the System.Data.CommandBehavior values.
            Returns: The number of rows successfully added to or refreshed in the System.Data.DataSet. This does not include rows affected by statements that do not return rows.
        Fill(self: DbDataAdapter, dataTable: DataTable, command: IDbCommand, behavior: CommandBehavior) -> int
        
            Adds or refreshes rows in a System.Data.DataTable to match those in the data source using the specified System.Data.DataTable, System.Data.IDbCommand and 
             System.Data.CommandBehavior.
        
        
            dataTable: A System.Data.DataTable to fill with records and, if necessary, schema.
            command: The SQL SELECT statement used to retrieve rows from the data source.
            behavior: One of the System.Data.CommandBehavior values.
            Returns: The number of rows successfully added to or refreshed in the System.Data.DataTable. This does not include rows affected by statements that do not return rows.
        Fill(self: DbDataAdapter, dataTables: Array[DataTable], startRecord: int, maxRecords: int, command: IDbCommand, behavior: CommandBehavior) -> int
        
            Adds or refreshes rows in a specified range in the System.Data.DataSet to match those in the data source using the System.Data.DataSet and System.Data.DataTable names.
        
            dataTables: The System.Data.DataTable objects to fill from the data source.
            startRecord: The zero-based record number to start with.
            maxRecords: The maximum number of records to retrieve.
            command: The System.Data.IDbCommand executed to fill the System.Data.DataTable objects.
            behavior: One of the System.Data.CommandBehavior values.
            Returns: The number of rows added to or refreshed in the data tables.
        Fill(self: DataAdapter, dataSet: DataSet, srcTable: str, dataReader: IDataReader, startRecord: int, maxRecords: int) -> int
        
            Adds or refreshes rows in a specified range in the System.Data.DataSet to match those in the data source using the System.Data.DataSet and System.Data.DataTable names.
        
            dataSet: A System.Data.DataSet to fill with records.
            srcTable: A string indicating the name of the source table.
            dataReader: An instance of System.Data.IDataReader.
            startRecord: The zero-based index of the starting record.
            maxRecords: An integer indicating the maximum number of records.
            Returns: The number of rows successfully added to or refreshed in the System.Data.DataSet. This does not include rows affected by statements that do not return rows.
        Fill(self: DataAdapter, dataTable: DataTable, dataReader: IDataReader) -> int
        
            Adds or refreshes rows in the System.Data.DataTable to match those in the data source using the System.Data.DataTable name and the specified System.Data.IDataReader.
        
            dataTable: A System.Data.DataTable to fill with records.
            dataReader: An instance of System.Data.IDataReader.
            Returns: The number of rows successfully added to or refreshed in the System.Data.DataTable. This does not include rows affected by statements that do not return rows.
        Fill(self: DataAdapter, dataTables: Array[DataTable], dataReader: IDataReader, startRecord: int, maxRecords: int) -> int
        
            Adds or refreshes rows in a specified range in the collection of System.Data.DataTable objects to match those in the data source.
        
            dataTables: A collection of System.Data.DataTable objects to fill with records.
            dataReader: An instance of System.Data.IDataReader.
            startRecord: The zero-based index of the starting record.
            maxRecords: An integer indicating the maximum number of records.
            Returns: The number of rows successfully added to or refreshed in the System.Data.DataTable. This does not include rows affected by statements that do not return rows.
        """
        pass

    def FillSchema(self, *__args):
        """
        FillSchema(self: DbDataAdapter, dataSet: DataSet, schemaType: SchemaType, command: IDbCommand, srcTable: str, behavior: CommandBehavior) -> Array[DataTable]
        
            Adds a System.Data.DataTable to the specified System.Data.DataSet and configures the schema to match that in the data source based on the specified System.Data.SchemaType.
        
            dataSet: The System.Data.DataSet to be filled with the schema from the data source.
            schemaType: One of the System.Data.SchemaType values.
            command: The SQL SELECT statement used to retrieve rows from the data source.
            srcTable: The name of the source table to use for table mapping.
            behavior: One of the System.Data.CommandBehavior values.
            Returns: An array of System.Data.DataTable objects that contain schema information returned from the data source.
        FillSchema(self: DbDataAdapter, dataTable: DataTable, schemaType: SchemaType, command: IDbCommand, behavior: CommandBehavior) -> DataTable
        
            Configures the schema of the specified System.Data.DataTable based on the specified System.Data.SchemaType, command string, and System.Data.CommandBehavior values.
        
            dataTable: The System.Data.DataTable to be filled with the schema from the data source.
            schemaType: One of the System.Data.SchemaType values.
            command: The SQL SELECT statement used to retrieve rows from the data source.
            behavior: One of the System.Data.CommandBehavior values.
            Returns: A of System.Data.DataTable object that contains schema information returned from the data source.
        FillSchema(self: DataAdapter, dataSet: DataSet, schemaType: SchemaType, srcTable: str, dataReader: IDataReader) -> Array[DataTable]
        
            Adds a System.Data.DataTable to the specified System.Data.DataSet.
        
            dataSet: The System.Data.DataTable to be filled from the System.Data.IDataReader.
            schemaType: One of the System.Data.SchemaType values.
            srcTable: The name of the source table to use for table mapping.
            dataReader: The System.Data.IDataReader to be used as the data source when filling the System.Data.DataTable.
            Returns: A reference to a collection of System.Data.DataTable objects that were added to the System.Data.DataSet.
        FillSchema(self: DataAdapter, dataTable: DataTable, schemaType: SchemaType, dataReader: IDataReader) -> DataTable
        
            Adds a System.Data.DataTable to the specified System.Data.DataSet.
        
            dataTable: The System.Data.DataTable to be filled from the System.Data.IDataReader.
            schemaType: One of the System.Data.SchemaType values.
            dataReader: The System.Data.IDataReader to be used as the data source when filling the System.Data.DataTable.
            Returns: A System.Data.DataTable object that contains schema information returned from the data source.
        """
        pass

    def GetBatchedParameter(self, *args): #cannot find CLR method
        """
        GetBatchedParameter(self: DbDataAdapter, commandIdentifier: int, parameterIndex: int) -> IDataParameter
        
            Returns a System.Data.IDataParameter from one of the commands in the current batch.
        
            commandIdentifier: The index of the command to retrieve the parameter from.
            parameterIndex: The index of the parameter within the command.
            Returns: The System.Data.IDataParameter specified.
        """
        pass

    def GetBatchedRecordsAffected(self, *args): #cannot find CLR method
        """
        GetBatchedRecordsAffected(self: DbDataAdapter, commandIdentifier: int) -> (bool, int, Exception)
        
            Returns information about an individual update attempt within a larger batched update.
        
            commandIdentifier: The zero-based column ordinal of the individual command within the batch.
            Returns: Information about an individual update attempt within a larger batched update.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or by its System.ComponentModel.Container.
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or ll if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    def HasTableMappings(self, *args): #cannot find CLR method
        """
        HasTableMappings(self: DataAdapter) -> bool
        
            Indicates whether a System.Data.Common.DataTableMappingCollection has been created.
            Returns: ue if a System.Data.Common.DataTableMappingCollection has been created; otherwise lse.
        """
        pass

    def InitializeBatching(self, *args): #cannot find CLR method
        """
        InitializeBatching(self: DbDataAdapter)
            Initializes batching for the System.Data.Common.DbDataAdapter.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A 
             value of lse is usually appropriate. ue to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the 
             remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def OnFillError(self, *args): #cannot find CLR method
        """
        OnFillError(self: DataAdapter, value: FillErrorEventArgs)
            Invoked when an error occurs during a ll.
        
            value: A System.Data.FillErrorEventArgs object.
        """
        pass

    def OnRowUpdated(self, *args): #cannot find CLR method
        """
        OnRowUpdated(self: NavisworksDataAdapter, value: RowUpdatedEventArgs)
            Raised by DbDataAdapter after a row is updated
        
            value: The event's specifics
        """
        pass

    def OnRowUpdating(self, *args): #cannot find CLR method
        """
        OnRowUpdating(self: NavisworksDataAdapter, value: RowUpdatingEventArgs)
            Raised by the underlying DbDataAdapter when a row is being updated
        
            value: The event's specifics
        """
        pass

    def ShouldSerializeTableMappings(self, *args): #cannot find CLR method
        """
        ShouldSerializeTableMappings(self: DataAdapter) -> bool
        
            Determines whether one or more System.Data.Common.DataTableMapping objects exist and they should be persisted.
            Returns: ue if one or more System.Data.Common.DataTableMapping objects exist; otherwise lse.
        """
        pass

    def TerminateBatching(self, *args): #cannot find CLR method
        """
        TerminateBatching(self: DbDataAdapter)
            Ends batching for the System.Data.Common.DbDataAdapter.
        """
        pass

    def Update(self, *__args):
        """
        Update(self: NavisworksDataAdapter, dt: DataSet, datatable_name: str) -> int
        
            Not implement
        Update(self: NavisworksDataAdapter, dt: DataTable) -> int
        
            Not implement
        Update(self: NavisworksDataAdapter, ds: DataSet) -> int
        
            Not implement
        Update(self: NavisworksDataAdapter, data_row: Array[DataRow]) -> int
        
            Not implement
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, commandText: str, connection: NavisworksConnection)
        __new__(cls: type, selectCommand: NavisworksCommand)
        __new__(cls: type)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    DeleteCommand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets/sets the delete command for this DataAdapter

Get: DeleteCommand(self: NavisworksDataAdapter) -> NavisworksCommand

Set: DeleteCommand(self: NavisworksDataAdapter) = value
"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    FillCommandBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the behavior of the command used to fill the data adapter.

"""

    InsertCommand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets/sets the insert command for this DataAdapter

Get: InsertCommand(self: NavisworksDataAdapter) -> NavisworksCommand

Set: InsertCommand(self: NavisworksDataAdapter) = value
"""

    SelectCommand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets/sets the select command for this DataAdapter

Get: SelectCommand(self: NavisworksDataAdapter) -> NavisworksCommand

Set: SelectCommand(self: NavisworksDataAdapter) = value
"""

    UpdateCommand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets/sets the update command for this DataAdapter

Get: UpdateCommand(self: NavisworksDataAdapter) -> NavisworksCommand

Set: UpdateCommand(self: NavisworksDataAdapter) = value
"""


    RowUpdated = None
    RowUpdating = None


class NavisWorksDataReader(DbDataReader, IDataReader, IDisposable, IDataRecord, IEnumerable):
    """ Implementation of DbDataReader. """
    def Close(self):
        """
        Close(self: NavisWorksDataReader)
            Closes the datareader.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: DbDataReader, disposing: bool)
            Releases the managed resources used by the System.Data.Common.DbDataReader and optionally releases the unmanaged resources.
        
            disposing: ue to release managed and unmanaged resources; lse to release only unmanaged resources.
        """
        pass

    def GetBoolean(self, ordinal):
        """
        GetBoolean(self: NavisWorksDataReader, ordinal: int) -> bool
        
            Retrieves the column as a boolean value
        
            ordinal: The index of the column to retrieve
            Returns: bool
        """
        pass

    def GetByte(self, ordinal):
        """
        GetByte(self: NavisWorksDataReader, ordinal: int) -> Byte
        
            Retrieves the column as a single byte value
        
            ordinal: The index of the column to retrieve
            Returns: byte
        """
        pass

    def GetBytes(self, ordinal, dataOffset, buffer, bufferOffset, length):
        """
        GetBytes(self: NavisWorksDataReader, ordinal: int, dataOffset: Int64, buffer: Array[Byte], bufferOffset: int, length: int) -> Int64
        
            Retrieves a column as an array of bytes (blob).
        To determine the number of bytes in the column, pass a null value for the buffer.The total length will be returned.
        
            ordinal: The index of the column to retrieve
            dataOffset: The zero-based index of where to begin reading the data
            buffer: The buffer to write the bytes into
            bufferOffset: The zero-based index of where to begin writing into the array
            length: The number of bytes to retrieve
            Returns: The actual number of bytes written into the array, if buffer is null, will return total length
        """
        pass

    def GetChar(self, ordinal):
        """
        GetChar(self: NavisWorksDataReader, ordinal: int) -> Char
        
            Returns the column as a single character
        
            ordinal: The index of the column to retrieve
            Returns: char
        """
        pass

    def GetChars(self, ordinal, dataOffset, buffer, bufferOffset, length):
        """
        GetChars(self: NavisWorksDataReader, ordinal: int, dataOffset: Int64, buffer: Array[Char], bufferOffset: int, length: int) -> Int64
        
            Retrieves a column as an array of chars (blob)
        To determine the number of characters in the column, pass a null value for the buffer.  The total length will be returned.
        
            ordinal: The index of the column to retrieve
            dataOffset: The zero-based index of where to begin reading the data
            buffer: The buffer to write the characters into
            bufferOffset: The zero-based index of where to begin writing into the array
            length: The number of bytes to retrieve
            Returns: The actual number of bytes written into the array, if buffer is null, will return total length
        """
        pass

    def GetDataTypeName(self, ordinal):
        """
        GetDataTypeName(self: NavisWorksDataReader, ordinal: int) -> str
        
            Retrieves the name of the back-end datatype of the column
        
            ordinal: The index of the column to retrieve
            Returns: string
        """
        pass

    def GetDateTime(self, ordinal):
        """
        GetDateTime(self: NavisWorksDataReader, ordinal: int) -> DateTime
        
            Retrieve the column as a date/time value
        
            ordinal: The index of the column to retrieve
            Returns: DateTime
        """
        pass

    def GetDbDataReader(self, *args): #cannot find CLR method
        """
        GetDbDataReader(self: DbDataReader, ordinal: int) -> DbDataReader
        
            Returns a System.Data.Common.DbDataReader object for the requested column ordinal that can be overridden with a provider-specific implementation.
        
            ordinal: The zero-based column ordinal.
            Returns: A System.Data.Common.DbDataReader object.
        """
        pass

    def GetDecimal(self, ordinal):
        """
        GetDecimal(self: NavisWorksDataReader, ordinal: int) -> Decimal
        
            Retrieve the column as a decimal value
        
            ordinal: The index of the column to retrieve
            Returns: decimal
        """
        pass

    def GetDouble(self, ordinal):
        """
        GetDouble(self: NavisWorksDataReader, ordinal: int) -> float
        
            Returns the column as a double
        
            ordinal: The index of the column to retrieve
            Returns: double
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: NavisWorksDataReader) -> IEnumerator """
        pass

    def GetFieldType(self, ordinal):
        """
        GetFieldType(self: NavisWorksDataReader, ordinal: int) -> Type
        
            Returns the .NET type of a given column
        
            ordinal: The index of the column to retrieve
            Returns: Type
        """
        pass

    def GetFloat(self, ordinal):
        """
        GetFloat(self: NavisWorksDataReader, ordinal: int) -> Single
        
            Returns a column as a float value
        
            ordinal: The index of the column to retrieve
            Returns: float
        """
        pass

    def GetGuid(self, ordinal):
        """
        GetGuid(self: NavisWorksDataReader, ordinal: int) -> Guid
        
            Returns the column as a Guid
        
            ordinal: The index of the column to retrieve
            Returns: Guid
        """
        pass

    def GetInt16(self, ordinal):
        """
        GetInt16(self: NavisWorksDataReader, ordinal: int) -> Int16
        
            Returns the column as a short
        
            ordinal: The index of the column to retrieve
            Returns: Int16
        """
        pass

    def GetInt32(self, ordinal):
        """
        GetInt32(self: NavisWorksDataReader, ordinal: int) -> int
        
            Retrieves the column as an int
        
            ordinal: The index of the column to retrieve
            Returns: Int32
        """
        pass

    def GetInt64(self, ordinal):
        """
        GetInt64(self: NavisWorksDataReader, ordinal: int) -> Int64
        
            Retrieves the column as a long
        
            ordinal: The index of the column to retrieve
            Returns: Int64
        """
        pass

    def GetName(self, ordinal):
        """
        GetName(self: NavisWorksDataReader, ordinal: int) -> str
        
            Retrieves the name of the column
        
            ordinal: The index of the column to retrieve
            Returns: string
        """
        pass

    def GetOrdinal(self, name):
        """
        GetOrdinal(self: NavisWorksDataReader, name: str) -> int
        
            Retrieves the index of a column, given its name
        
            name: The name of the column to retrieve
            Returns: The int index of the column
        """
        pass

    def GetSchemaTable(self):
        """
        GetSchemaTable(self: NavisWorksDataReader) -> DataTable
        
            Schema information in SQLite is difficult to map into .NET conventions, so a lot of work must be done
        to gather the necessary information so it can be represented in an ADO.NET 
             manner.
        
            Returns: Returns a DataTable containing the schema information for the active SELECT statement being processed.
        """
        pass

    def GetString(self, ordinal):
        """
        GetString(self: NavisWorksDataReader, ordinal: int) -> str
        
            Retrieves the column as a string
        
            ordinal: The index of the column to retrieve
            Returns: string
        """
        pass

    def GetValue(self, ordinal):
        """
        GetValue(self: NavisWorksDataReader, ordinal: int) -> object
        
            Retrieves the column as an object corresponding to the underlying datatype of the column
        
            ordinal: The index of the column to retrieve
            Returns: object
        """
        pass

    def GetValues(self, values):
        """
        GetValues(self: NavisWorksDataReader, values: Array[object]) -> int
        
            Retrieves the values of multiple columns, up to the size of the supplied array
        
            values: The array to fill with values from the columns in the current resultset
            Returns: The number of columns retrieved
        """
        pass

    def IsDBNull(self, ordinal):
        """
        IsDBNull(self: NavisWorksDataReader, ordinal: int) -> bool
        
            Returns True if the specified column is null
        
            ordinal: The index of the column to retrieve
            Returns: True or False
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A 
             value of lse is usually appropriate. ue to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the 
             remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def NextResult(self):
        """
        NextResult(self: NavisWorksDataReader) -> bool
        
            Moves to the next resultset in multiple row-returning SQL command.
            Returns: True if the command was successful and a new resultset is available, False otherwise.
        """
        pass

    def Read(self):
        """
        Read(self: NavisWorksDataReader) -> bool
        
            Reads the next row from the resultset
            Returns: True if a new row was successfully loaded and is ready for processing
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not implemented.  Returns 0

Get: Depth(self: NavisWorksDataReader) -> int

"""

    FieldCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of columns in the current resultset.

Get: FieldCount(self: NavisWorksDataReader) -> int

"""

    HasRows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns True if the resultset has rows that can be fetched

Get: HasRows(self: NavisWorksDataReader) -> bool

"""

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns True if the data reader is closed

Get: IsClosed(self: NavisWorksDataReader) -> bool

"""

    RecordsAffected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve the count of records affected by an update/insert/delete command.  Only valid once the data reader is closed!

Get: RecordsAffected(self: NavisWorksDataReader) -> int

"""



class NavisworksParameter(DbParameter, IDbDataParameter, IDataParameter):
    """
    Implementation of DbParameter.
    
    NavisworksParameter(parameterName: str, value: object)
    NavisworksParameter()
    """
    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A 
             value of lse is usually appropriate. ue to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the 
             remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def ResetDbType(self):
        """ ResetDbType(self: NavisworksParameter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, parameterName=None, value=None):
        """
        __new__(cls: type, parameterName: str, value: object)
        __new__(cls: type)
        """
        pass

    DbType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the datatype of the parameter

Get: DbType(self: NavisworksParameter) -> DbType

Set: DbType(self: NavisworksParameter) = value
"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Supports only input parameters

Get: Direction(self: NavisworksParameter) -> ParameterDirection

Set: Direction(self: NavisworksParameter) = value
"""

    IsNullable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether or not the parameter can contain a null value

Get: IsNullable(self: NavisworksParameter) -> bool

Set: IsNullable(self: NavisworksParameter) = value
"""

    ParameterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the parameter name

Get: ParameterName(self: NavisworksParameter) -> str

Set: ParameterName(self: NavisworksParameter) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the size of the parameter

Get: Size(self: NavisworksParameter) -> int

Set: Size(self: NavisworksParameter) = value
"""

    SourceColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets/sets the source column

Get: SourceColumn(self: NavisworksParameter) -> str

Set: SourceColumn(self: NavisworksParameter) = value
"""

    SourceColumnNullMapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Used by DbCommandBuilder to determine the mapping for nullable fields

Get: SourceColumnNullMapping(self: NavisworksParameter) -> bool

Set: SourceColumnNullMapping(self: NavisworksParameter) = value
"""

    SourceVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets and sets the row version

Get: SourceVersion(self: NavisworksParameter) -> DataRowVersion

Set: SourceVersion(self: NavisworksParameter) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets and sets the parameter value.  If no datatype was specified, the datatype will assume the type from the value given.

Get: Value(self: NavisworksParameter) -> object

Set: Value(self: NavisworksParameter) = value
"""



class NavisworksParameterCollection(DbParameterCollection, IDataParameterCollection, IList, ICollection, IEnumerable, IDisposable):
    """ Implementation of DbParameterCollection. """
    def Add(self, *__args):
        """
        Add(self: NavisworksParameterCollection, parameter: NavisworksParameter) -> int
        
            Adds a parameter to the collection
        
            parameter: The parameter to add
            Returns: A zero-based index of where the parameter is located in the array
        Add(self: NavisworksParameterCollection, value: object) -> int
        
            Adds a parameter to the collection
        
            value: The parameter to add
            Returns: A zero-based index of where the parameter is located in the array
        """
        pass

    def AddRange(self, values):
        """
        AddRange(self: NavisworksParameterCollection, values: Array)
            Adds an array of parameters to the collection
        
            values: The array of parameters to add
        """
        pass

    def AddWithValue(self, parameterName, value):
        """
        AddWithValue(self: NavisworksParameterCollection, parameterName: str, value: object) -> NavisworksParameter
        
            Adds a named/unnamed parameter and its value to the parameter collection.
        
            parameterName: Name of the parameter, or null to indicate an unnamed parameter
            value: The initial value of the parameter
            Returns: Returns the NavisworksParameter object created during the call.
        """
        pass

    def Clear(self):
        """
        Clear(self: NavisworksParameterCollection)
            Clears the array and resets the collection
        """
        pass

    def Contains(self, value):
        """
        Contains(self: NavisworksParameterCollection, value: str) -> bool
        
            Determines if the named parameter exists in the collection
        
            value: The name of the parameter to check
            Returns: True if the parameter is in the collection
        Contains(self: NavisworksParameterCollection, value: object) -> bool
        
            Determines if the parameter exists in the collection
        
            value: The NavisworksParameter to check
            Returns: True if the parameter is in the collection
        """
        pass

    def CopyTo(self, values, index):
        """
        CopyTo(self: NavisworksParameterCollection, values: Array, index: int)
            Not implemented
        """
        pass

    def Dispose(self):
        """ Dispose(self: NavisworksParameterCollection) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: NavisworksParameterCollection) -> IEnumerator """
        pass

    def GetParameter(self, *args): #cannot find CLR method
        """
        GetParameter(self: NavisworksParameterCollection, parameterName: str) -> DbParameter
        
            Retrieve a parameter by name from the collection
        
            parameterName: The name of the parameter to fetch
            Returns: A DbParameter object
        GetParameter(self: NavisworksParameterCollection, index: int) -> DbParameter
        
            Retrieves a parameter by its index in the collection
        
            index: The index of the parameter to retrieve
            Returns: A DbParameter object
        """
        pass

    def IndexOf(self, *__args):
        """
        IndexOf(self: NavisworksParameterCollection, parameterName: str) -> int
        
            Returns the index of a parameter given its name
        
            parameterName: The name of the parameter to find
            Returns: -1 if not found, otherwise a zero-based index of the parameter
        IndexOf(self: NavisworksParameterCollection, value: object) -> int
        
            Returns the index of a parameter
        
            value: The parameter to find
            Returns: -1 if not found, otherwise a zero-based index of the parameter
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: NavisworksParameterCollection, index: int, value: object)
            Inserts a parameter into the array at the specified location
        
            index: The zero-based index to insert the parameter at
            value: The parameter to insert
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A 
             value of lse is usually appropriate. ue to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the 
             remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: NavisworksParameterCollection, value: object)
            Removes specified parameter from the collection
        
            value: The parameter to remove
        """
        pass

    def RemoveAt(self, *__args):
        """
        RemoveAt(self: NavisworksParameterCollection, parameterName: str)
            Removes a parameter from the collection given its name
        
            parameterName: The name of the parameter to remove
        RemoveAt(self: NavisworksParameterCollection, index: int)
            Removes a parameter from the collection given its index
        
            index: The zero-based parameter index to remove
        """
        pass

    def SetParameter(self, *args): #cannot find CLR method
        """
        SetParameter(self: NavisworksParameterCollection, parameterName: str, value: DbParameter)
            Re-assign the named parameter to a new parameter object
        
            parameterName: The name of the parameter to replace
            value: The new parameter
        SetParameter(self: NavisworksParameterCollection, index: int, value: DbParameter)
            Re-assign a parameter at the specified index
        
            index: The zero-based index of the parameter to replace
            value: The new parameter
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: ue if the System.Object is found in the System.Collections.IList; otherwise, lse.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a count of parameters in the collection

Get: Count(self: NavisworksParameterCollection) -> int

"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns false

Get: IsFixedSize(self: NavisworksParameterCollection) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns false

Get: IsReadOnly(self: NavisworksParameterCollection) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true

Get: IsSynchronized(self: NavisworksParameterCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns null

Get: SyncRoot(self: NavisworksParameterCollection) -> object

"""



class NavisworksTransaction(DbTransaction, IDbTransaction, IDisposable):
    """ Implementation of DbTransaction. """
    def Commit(self):
        """
        Commit(self: NavisworksTransaction)
            Commits the current transaction.
        """
        pass

    def Dispose(self):
        """ Dispose(self: NavisworksTransaction, A_0: bool) """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A 
             value of lse is usually appropriate. ue to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the 
             remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def Rollback(self):
        """
        Rollback(self: NavisworksTransaction)
            Rolls back the active transaction.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Connection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the underlying connection to which this transaction applies.

Get: Connection(self: NavisworksTransaction) -> NavisworksConnection

"""

    DbConnection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Forwards to the local Connection property

"""

    IsolationLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the isolation level of the transaction.  NavisworksTransaction only supports Serializable transactions.

Get: IsolationLevel(self: NavisworksTransaction) -> IsolationLevel

"""



