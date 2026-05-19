# encoding: utf-8
# module Autodesk.Navisworks.Api.Schema calls itself Schema
# from Autodesk.Navisworks.Api, Version=19.0.1374.1, Culture=neutral, PublicKeyToken=d85e58fa5af9b484
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Field(NativeHandle, IDisposable):
    """ Base class for all fields used within Autodesk.Navisworks.Api.Schema.SchemaDefinitionSchemaDefinitions. """
    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: Field, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> Field """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalGetEditAccessType(self, *args): #cannot find CLR method
        """ InternalGetEditAccessType(self: Field) -> Type """
        pass

    def InternalGetReadAccessType(self, *args): #cannot find CLR method
        """ InternalGetReadAccessType(self: Field) -> Type """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: Field) -> Void* """
        pass

    def ValueEquals(self, *__args):
        """
        ValueEquals(self: Field, value: Field) -> bool
        
            Performs comparison 'By Value'
        ValueEquals(value1: Field, value2: Field) -> bool
        
            Compares the two references 'By Value'
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
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Concepts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Field-specific semantics associated with this field.

Get: Concepts(self: Field) -> ConceptCollection

"""

    DisplayNameId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The field's display name internal ID. Used for looking up the localized display name.

Get: DisplayNameId(self: Field) -> str

Set: DisplayNameId(self: Field) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The identifier for the field.

Get: Id(self: Field) -> str

Set: Id(self: Field) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: Field) -> bool

"""



class SimpleField(Field, IDisposable):
    """ Intermediate base class for all simple value Autodesk.Navisworks.Api.Schema.FieldFields. """
    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: Field, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> SimpleField """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalGetEditAccessType(self, *args): #cannot find CLR method
        """ InternalGetEditAccessType(self: SimpleField) -> Type """
        pass

    def InternalGetReadAccessType(self, *args): #cannot find CLR method
        """ InternalGetReadAccessType(self: SimpleField) -> Type """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: Field) -> Void* """
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
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: SimpleField) -> bool

"""



class BooleanField(SimpleField, IDisposable):
    """
    Represents the definition of a System.Boolean value within a Autodesk.Navisworks.Api.Schema.SchemaDefinition.
    
    BooleanField(id: str)
    BooleanField()
    """
    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def GetValue(self, accessor):
        """
        GetValue(self: BooleanField, accessor: ReadAccessor) -> bool
        
            Gets a value from a given Autodesk.Navisworks.Api.Schema.SchemaData via the associated Autodesk.Navisworks.Api.Schema.ReadAccessor.
        """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: Field, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> BooleanField """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalGetEditAccessType(self, *args): #cannot find CLR method
        """ InternalGetEditAccessType(self: SimpleField) -> Type """
        pass

    def InternalGetReadAccessType(self, *args): #cannot find CLR method
        """ InternalGetReadAccessType(self: SimpleField) -> Type """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: Field) -> Void* """
        pass

    def SetValue(self, accessor, value):
        """
        SetValue(self: BooleanField, accessor: EditAccessor, value: bool)
            Sets a value into a given Autodesk.Navisworks.Api.Schema.SchemaData via the associated Autodesk.Navisworks.Api.Schema.EditAccessor.
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
    def __new__(self, id=None):
        """
        __new__(cls: type, id: str)
        __new__(cls: type)
        __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Default value that created Autodesk.Navisworks.Api.Schema.SchemaData objects will contain at creation time.

Get: DefaultValue(self: BooleanField) -> bool

Set: DefaultValue(self: BooleanField) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: BooleanField) -> bool

"""



class ComplexField(Field, IDisposable):
    """ Intermediate base class for all complex structural Autodesk.Navisworks.Api.Schema.FieldFields. """
    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: Field, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> ComplexField """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalGetEditAccessType(self, *args): #cannot find CLR method
        """ InternalGetEditAccessType(self: Field) -> Type """
        pass

    def InternalGetReadAccessType(self, *args): #cannot find CLR method
        """ InternalGetReadAccessType(self: Field) -> Type """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: Field) -> Void* """
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
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: ComplexField) -> bool

"""



class ConceptCollection(NativeHandle, IDisposable, IList[str], ICollection[str], IEnumerable[str], IEnumerable, IList, ICollection):
    """
    A collection of concept strings.
    
    ConceptCollection(from: ConceptCollection)
    ConceptCollection()
    """
    def Add(self, item):
        """
        Add(self: ConceptCollection, item: str)
            Adds item to the end of the collection.
        """
        pass

    def AddRange(self, from):
        """ AddRange(self: ConceptCollection, from: IEnumerable[str]) """
        pass

    def Clear(self):
        """
        Clear(self: ConceptCollection)
            Removes all items from the collection
        """
        pass

    def Contains(self, item):
        """
        Contains(self: ConceptCollection, item: str) -> bool
        
            Determines whether the SavedItemCollection contains a specific value.
        """
        pass

    def CopyFrom(self, from):
        """ CopyFrom(self: ConceptCollection, from: IEnumerable[str]) """
        pass

    def CopyTo(self, *__args):
        """
        CopyTo(self: ConceptCollection, to: ICollection[str])CopyTo(self: ConceptCollection, array: Array[str], arrayIndex: int)
            Copies the elements of the System.Collections.Generic.ICollection to an System.Array, starting at a particular System.Array index.
        
            array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.Generic.ICollection. The System.Array must have zero-based indexing.
            arrayIndex: The zero-based index in array at which copying begins.
        """
        pass

    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ConceptCollection) -> IEnumerator[str]
        
            Returns an enumerator that can iterate through the collection.
            Returns: An IEnumerator that can be used to iterate through the collection.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: ConceptCollection, item: str) -> int
        
            Determines the index of a specific item in the Collection
        """
        pass

    def Insert(self, index, item):
        """
        Insert(self: ConceptCollection, index: int, item: str)
            Inserts item into the collection at the specified index
        """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: ConceptCollection, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> ConceptCollection """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: ConceptCollection) -> Void* """
        pass

    def Remove(self, item):
        """
        Remove(self: ConceptCollection, item: str) -> bool
        
            Removes the first occurrence of a specific item from the collection.
        
            item: The object to remove from the collection.
            Returns: true if item was successfully removed from the collection; otherwise, false. 
        This method also returns false if item is not found in the original collection.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: ConceptCollection, index: int)
            Removes the System.Collections.Generic.IList item at the specified index.
        
            index: The zero-based index of the item to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[str], item: str) -> bool
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
        """ x.__getitem__(y) <==> x[y] """
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

    @staticmethod # known case of __new__
    def __new__(self, from=None):
        """
        __new__(cls: type, from: ConceptCollection)
        __new__(cls: type)
        __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements contained in the collection.

Get: Count(self: ConceptCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: ConceptCollection) -> bool

"""



class DoubleField(SimpleField, IDisposable):
    """
    Represents the definition of a System.Double value within a Autodesk.Navisworks.Api.Schema.SchemaDefinition.
    
    DoubleField(id: str)
    DoubleField()
    """
    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def GetValue(self, accessor):
        """
        GetValue(self: DoubleField, accessor: ReadAccessor) -> float
        
            Gets a value from a given Autodesk.Navisworks.Api.Schema.SchemaData via the associated Autodesk.Navisworks.Api.Schema.ReadAccessor.
        """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: Field, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> DoubleField """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalGetEditAccessType(self, *args): #cannot find CLR method
        """ InternalGetEditAccessType(self: SimpleField) -> Type """
        pass

    def InternalGetReadAccessType(self, *args): #cannot find CLR method
        """ InternalGetReadAccessType(self: SimpleField) -> Type """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: Field) -> Void* """
        pass

    def SetValue(self, accessor, value):
        """
        SetValue(self: DoubleField, accessor: EditAccessor, value: float)
            Sets a value into a given Autodesk.Navisworks.Api.Schema.SchemaData via the associated Autodesk.Navisworks.Api.Schema.EditAccessor.
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
    def __new__(self, id=None):
        """
        __new__(cls: type, id: str)
        __new__(cls: type)
        __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Default value that created Autodesk.Navisworks.Api.Schema.SchemaData objects will contain at creation time.

Get: DefaultValue(self: DoubleField) -> float

Set: DefaultValue(self: DoubleField) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: DoubleField) -> bool

"""

    UnitGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents the unit group (eg. length, volume, angle, etc) of the field value.

Get: UnitGroup(self: DoubleField) -> UnitGroup

Set: UnitGroup(self: DoubleField) = value
"""



class ReadAccessor(NativeHandle, IDisposable):
    """ Provides read-only access into a Autodesk.Navisworks.Api.Schema.SchemaData via an associated Autodesk.Navisworks.Api.Schema.Field. Represents a given position inside Autodesk.Navisworks.Api.Schema.SchemaData. """
    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: ReadAccessor, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> ReadAccessor """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: ReadAccessor) -> Void* """
        pass

    def IsValid(self, instance):
        """
        IsValid(self: ReadAccessor, instance: SchemaData) -> bool
        
            Tests to see if this accessor is associated with a given Autodesk.Navisworks.Api.Schema.SchemaData.
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
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: ReadAccessor) -> bool

"""



class EditAccessor(ReadAccessor, IDisposable):
    """ Provides editing access into a Autodesk.Navisworks.Api.Schema.SchemaData via an associated Autodesk.Navisworks.Api.Schema.Field. Represents a given position inside Autodesk.Navisworks.Api.Schema.SchemaData. """
    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: ReadAccessor, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> EditAccessor """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: ReadAccessor) -> Void* """
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
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: EditAccessor) -> bool

"""



class FieldCollection(NativeHandle, IDisposable, IList[Field], ICollection[Field], IEnumerable[Field], IEnumerable, IList, ICollection):
    """
    A collection of Autodesk.Navisworks.Api.Schema.FieldFields.
    
    FieldCollection(from: FieldCollection)
    FieldCollection()
    """
    def Add(self, item):
        """
        Add(self: FieldCollection, item: Field)
            Adds item to the end of the collection.
        """
        pass

    def AddRange(self, from):
        """ AddRange(self: FieldCollection, from: IEnumerable[Field]) """
        pass

    def Clear(self):
        """
        Clear(self: FieldCollection)
            Removes all items from the collection
        """
        pass

    def Contains(self, item):
        """
        Contains(self: FieldCollection, item: Field) -> bool
        
            Determines whether the SavedItemCollection contains a specific value.
        """
        pass

    def CopyFrom(self, from):
        """ CopyFrom(self: FieldCollection, from: IEnumerable[Field]) """
        pass

    def CopyTo(self, *__args):
        """
        CopyTo(self: FieldCollection, to: ICollection[Field])CopyTo(self: FieldCollection, array: Array[Field], arrayIndex: int)
            Copies the elements of the System.Collections.Generic.ICollection to an System.Array, starting at a particular System.Array index.
        
            array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.Generic.ICollection. The System.Array must have zero-based indexing.
            arrayIndex: The zero-based index in array at which copying begins.
        """
        pass

    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: FieldCollection) -> IEnumerator[Field]
        
            Returns an enumerator that can iterate through the collection.
            Returns: An IEnumerator that can be used to iterate through the collection.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: FieldCollection, item: Field) -> int
        
            Determines the index of a specific item in the Collection
        """
        pass

    def Insert(self, index, item):
        """
        Insert(self: FieldCollection, index: int, item: Field)
            Inserts item into the collection at the specified index
        """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: FieldCollection, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> FieldCollection """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: FieldCollection) -> Void* """
        pass

    def Remove(self, item):
        """
        Remove(self: FieldCollection, item: Field) -> bool
        
            Removes the first occurrence of a specific item from the collection.
        
            item: The object to remove from the collection.
            Returns: true if item was successfully removed from the collection; otherwise, false. 
        This method also returns false if item is not found in the original collection.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: FieldCollection, index: int)
            Removes the System.Collections.Generic.IList item at the specified index.
        
            index: The zero-based index of the item to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[Field], item: Field) -> bool
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
        """ x.__getitem__(y) <==> x[y] """
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

    @staticmethod # known case of __new__
    def __new__(self, from=None):
        """
        __new__(cls: type, from: FieldCollection)
        __new__(cls: type)
        __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements contained in the collection.

Get: Count(self: FieldCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: FieldCollection) -> bool

"""



class GroupField(ComplexField, IDisposable):
    """ Intermediate base class for all complex group Autodesk.Navisworks.Api.Schema.FieldFields. """
    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: Field, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> GroupField """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalGetEditAccessType(self, *args): #cannot find CLR method
        """ InternalGetEditAccessType(self: GroupField) -> Type """
        pass

    def InternalGetReadAccessType(self, *args): #cannot find CLR method
        """ InternalGetReadAccessType(self: GroupField) -> Type """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: Field) -> Void* """
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
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: GroupField) -> bool

"""



class GuidField(SimpleField, IDisposable):
    """
    Represents the definition of a System.Guid value within a Autodesk.Navisworks.Api.Schema.SchemaDefinition.
    
    GuidField(id: str, ownership: GuidFieldOwnershipType)
    GuidField(ownership: GuidFieldOwnershipType)
    GuidField(id: str)
    """
    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def GetValue(self, accessor):
        """
        GetValue(self: GuidField, accessor: ReadAccessor) -> Guid
        
            Gets a value from a given Autodesk.Navisworks.Api.Schema.SchemaData via the associated Autodesk.Navisworks.Api.Schema.ReadAccessor.
        """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: Field, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> GuidField """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalGetEditAccessType(self, *args): #cannot find CLR method
        """ InternalGetEditAccessType(self: SimpleField) -> Type """
        pass

    def InternalGetReadAccessType(self, *args): #cannot find CLR method
        """ InternalGetReadAccessType(self: SimpleField) -> Type """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: Field) -> Void* """
        pass

    def SetValue(self, accessor, value):
        """
        SetValue(self: GuidField, accessor: EditAccessor, value: Guid)
            Sets a value into a given Autodesk.Navisworks.Api.Schema.SchemaData via the associated Autodesk.Navisworks.Api.Schema.EditAccessor.
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
        __new__(cls: type, id: str, ownership: GuidFieldOwnershipType)
        __new__(cls: type, ownership: GuidFieldOwnershipType)
        __new__(cls: type, id: str)
        __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Default value that created Autodesk.Navisworks.Api.Schema.SchemaData objects will contain at creation time.

Get: DefaultValue(self: GuidField) -> Guid

Set: DefaultValue(self: GuidField) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: GuidField) -> bool

"""

    OwnershipSemantics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ownership semantics for this GUID.

Get: OwnershipSemantics(self: GuidField) -> GuidFieldOwnershipType

Set: OwnershipSemantics(self: GuidField) = value
"""

    TargetConcept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Target concept, if any, that we expect the referenced resource to implement.

Get: TargetConcept(self: GuidField) -> str

Set: TargetConcept(self: GuidField) = value
"""



class GuidFieldOwnershipType(Enum, IComparable, IFormattable, IConvertible):
    """
    Ownership semantics for a given GUID.
    
    enum GuidFieldOwnershipType, values: ExternalReference (6), Generic (0), Identifier (1), OwnerReference (5), SharedReference (3), UniqueReference (2), WeakReference (4)
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

    ExternalReference = None
    Generic = None
    Identifier = None
    OwnerReference = None
    SharedReference = None
    UniqueReference = None
    value__ = None
    WeakReference = None


class Int32Field(SimpleField, IDisposable):
    """
    Represents the definition of a System.Int32 value within a Autodesk.Navisworks.Api.Schema.SchemaDefinition.
    
    Int32Field(id: str)
    Int32Field()
    """
    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def GetValue(self, accessor):
        """
        GetValue(self: Int32Field, accessor: ReadAccessor) -> int
        
            Gets a value from a given Autodesk.Navisworks.Api.Schema.SchemaData via the associated Autodesk.Navisworks.Api.Schema.ReadAccessor.
        """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: Field, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> Int32Field """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalGetEditAccessType(self, *args): #cannot find CLR method
        """ InternalGetEditAccessType(self: SimpleField) -> Type """
        pass

    def InternalGetReadAccessType(self, *args): #cannot find CLR method
        """ InternalGetReadAccessType(self: SimpleField) -> Type """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: Field) -> Void* """
        pass

    def SetValue(self, accessor, value):
        """
        SetValue(self: Int32Field, accessor: EditAccessor, value: int)
            Sets a value into a given Autodesk.Navisworks.Api.Schema.SchemaData via the associated Autodesk.Navisworks.Api.Schema.EditAccessor.
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
    def __new__(self, id=None):
        """
        __new__(cls: type, id: str)
        __new__(cls: type)
        __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Default value that created Autodesk.Navisworks.Api.Schema.SchemaData objects will contain at creation time.

Get: DefaultValue(self: Int32Field) -> int

Set: DefaultValue(self: Int32Field) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: Int32Field) -> bool

"""



class SchemaBuilder(NativeHandle, IDisposable):
    """
    Enables construction of Autodesk.Navisworks.Api.Schema.SchemaDefinitionSchemaDefinitions.
    
    SchemaBuilder()
    """
    def AddConcept(self, concept):
        """
        AddConcept(self: SchemaBuilder, concept: str)
            Adds a given concept string onto the Autodesk.Navisworks.Api.Schema.SchemaDefinitionschema definition under construction.
        """
        pass

    def AddField(self, field):
        """
        AddField(self: SchemaBuilder, field: Field)
            Copies & adds in the field to the builder's internal collection.
        """
        pass

    def BuildDefinition(self):
        """
        BuildDefinition(self: SchemaBuilder) -> SchemaDefinition
        
            Constructs a Autodesk.Navisworks.Api.Schema.SchemaDefinitionschema definition matching what has been passed into 
             Autodesk.Navisworks.Api.Schema.SchemaBuilder.AddField(Autodesk.Navisworks.Api.Schema.Field) & Autodesk.Navisworks.Api.Schema.SchemaBuilder.AddConcept(System.String).
        """
        pass

    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: SchemaBuilder, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> SchemaBuilder """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: SchemaBuilder) -> Void* """
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
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: SchemaBuilder) -> bool

"""



class SchemaData(NativeHandle, IDisposable, IHasDynamicProperties, IDynamicMetaObjectProvider, IStructuralEquatable, IStructuralComparable):
    """ Contains data values defined by a given Autodesk.Navisworks.Api.Schema.SchemaDefinitionschema definition. May be traversed manually or accessed via NET DLR dynamic typing. """
    def Copy(self):
        """
        Copy(self: SchemaData) -> SchemaData
        
            Creates a copy of the current state of this data object.
        """
        pass

    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: SchemaData, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> SchemaData """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: NativeHandle) -> Void* """
        pass

    def ValueCompares(self, rhs):
        """
        ValueCompares(self: SchemaData, rhs: SchemaData) -> int
        
            Performs a value comparison.
        """
        pass

    def ValueEquals(self, *__args):
        """
        ValueEquals(self: SchemaData, value: SchemaData) -> bool
        
            Performs comparison 'By Value'
        ValueEquals(value1: SchemaData, value2: SchemaData) -> bool
        
            Compares the two references 'By Value'
        """
        pass

    def __dir__(self, *args): #cannot find CLR method
        """ __dir__(self: IDynamicMetaObjectProvider) -> list """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __hash__(self, *args): #cannot find CLR method
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Definition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Schema definition that defines this data object.

Get: Definition(self: SchemaData) -> SchemaDefinition

"""

    EditAccessor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Accessor for editing values when beginning a query into this data object.

Get: EditAccessor(self: SchemaData) -> EditAccessor

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: SchemaData) -> bool

"""

    ReadAccessor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Read-only accessor for beginning a query into this data object.

Get: ReadAccessor(self: SchemaData) -> ReadAccessor

"""



class SchemaDefinition(NativeHandle, IDisposable):
    """ Autodesk.Navisworks.Api.Schema.SchemaDefinitionSchema definitions are used to define data structures that are then created as Autodesk.Navisworks.Api.Schema.SchemaDataschema data objects for use with various Navisworks API calls. """
    def CreateData(self):
        """
        CreateData(self: SchemaDefinition) -> SchemaData
        
            Creates a concrete data object to hold values structured according to the Autodesk.Navisworks.Api.Schema.FieldFields within this definition.
        """
        pass

    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def Equals(self, obj):
        """
        Equals(self: SchemaDefinition, obj: object) -> bool
        
            Determines whether the specified object and the current object refer to the same
        underlying native object. Returns false if either object has been disposed.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: SchemaDefinition) -> int
        
            Serves as a hash function for a particular type. System.Object.GetHashCode is suitable for use in hashing algorithms and data structures like a hash table.
            Returns: A hash code for the current System.Object.
        """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: SchemaDefinition, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> SchemaDefinition """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: SchemaDefinition) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: SchemaDefinition) -> Void* """
        pass

    def ValueEquals(self, *__args):
        """
        ValueEquals(self: SchemaDefinition, value: SchemaDefinition) -> bool
        
            Performs comparison 'By Value'
        ValueEquals(value1: SchemaDefinition, value2: SchemaDefinition) -> bool
        
            Compares the two references 'By Value'
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Concepts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The concepts that this definition implements.

Get: Concepts(self: SchemaDefinition) -> ConceptCollection

"""

    Fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The top level of Autodesk.Navisworks.Api.Schema.FieldFields within this definition.

Get: Fields(self: SchemaDefinition) -> FieldCollection

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: SchemaDefinition) -> bool

"""



class SchemaDefinitionCollection(NativeHandle, IDisposable, IList[SchemaDefinition], ICollection[SchemaDefinition], IEnumerable[SchemaDefinition], IEnumerable, IList, ICollection):
    """
    A collection of Autodesk.Navisworks.Api.Schema.SchemaDefinitionDefinitions.
    
    SchemaDefinitionCollection(from: SchemaDefinitionCollection)
    SchemaDefinitionCollection()
    """
    def Contains(self, item):
        """
        Contains(self: SchemaDefinitionCollection, item: SchemaDefinition) -> bool
        
            Determines whether the SavedItemCollection contains a specific value.
        """
        pass

    def CopyTo(self, *__args):
        """
        CopyTo(self: SchemaDefinitionCollection, to: ICollection[SchemaDefinition])CopyTo(self: SchemaDefinitionCollection, array: Array[SchemaDefinition], arrayIndex: int)
            Copies the elements of the System.Collections.Generic.ICollection to an System.Array, starting at a particular System.Array index.
        
            array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.Generic.ICollection. The System.Array must have zero-based indexing.
            arrayIndex: The zero-based index in array at which copying begins.
        """
        pass

    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: SchemaDefinitionCollection) -> IEnumerator[SchemaDefinition]
        
            Returns an enumerator that can iterate through the collection.
            Returns: An IEnumerator that can be used to iterate through the collection.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: SchemaDefinitionCollection, item: SchemaDefinition) -> int
        
            Determines the index of a specific item in the Collection
        """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: SchemaDefinitionCollection, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> SchemaDefinitionCollection """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: SchemaDefinitionCollection) -> Void* """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[SchemaDefinition], item: SchemaDefinition) -> bool
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
        """ x.__getitem__(y) <==> x[y] """
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

    @staticmethod # known case of __new__
    def __new__(self, from=None):
        """
        __new__(cls: type, from: SchemaDefinitionCollection)
        __new__(cls: type)
        __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements contained in the collection.

Get: Count(self: SchemaDefinitionCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: SchemaDefinitionCollection) -> bool

"""



class StringField(SimpleField, IDisposable):
    """
    Represents the definition of a System.String value within a Autodesk.Navisworks.Api.Schema.SchemaDefinition.
    
    StringField(id: str)
    StringField()
    """
    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def GetValue(self, accessor):
        """
        GetValue(self: StringField, accessor: ReadAccessor) -> str
        
            Gets a value from a given Autodesk.Navisworks.Api.Schema.SchemaData via the associated Autodesk.Navisworks.Api.Schema.ReadAccessor.
        """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: Field, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> StringField """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalGetEditAccessType(self, *args): #cannot find CLR method
        """ InternalGetEditAccessType(self: SimpleField) -> Type """
        pass

    def InternalGetReadAccessType(self, *args): #cannot find CLR method
        """ InternalGetReadAccessType(self: SimpleField) -> Type """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: Field) -> Void* """
        pass

    def SetValue(self, accessor, value):
        """
        SetValue(self: StringField, accessor: EditAccessor, value: str)
            Sets a value into a given Autodesk.Navisworks.Api.Schema.SchemaData via the associated Autodesk.Navisworks.Api.Schema.EditAccessor.
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
    def __new__(self, id=None):
        """
        __new__(cls: type, id: str)
        __new__(cls: type)
        __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Default value that created Autodesk.Navisworks.Api.Schema.SchemaData objects will contain at creation time.

Get: DefaultValue(self: StringField) -> str

Set: DefaultValue(self: StringField) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: StringField) -> bool

"""



class StructField(GroupField, IDisposable):
    """
    Represents the definition of a structure within a Autodesk.Navisworks.Api.Schema.SchemaDefinition.
    
    StructField(id: str)
    StructField()
    """
    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: Field, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> StructField """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalGetEditAccessType(self, *args): #cannot find CLR method
        """ InternalGetEditAccessType(self: GroupField) -> Type """
        pass

    def InternalGetReadAccessType(self, *args): #cannot find CLR method
        """ InternalGetReadAccessType(self: GroupField) -> Type """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: Field) -> Void* """
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
    def __new__(self, id=None):
        """
        __new__(cls: type, id: str)
        __new__(cls: type)
        __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fields that comprise the struct content.

Get: Fields(self: StructField) -> FieldCollection

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: StructField) -> bool

"""



class UnitGroup(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents the unit group (eg. length, volume, angle, etc) of the field value.
    
    enum UnitGroup, values: Angle (32768), Area (12288), Length (8192), None (0), Volume (16384)
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

    Angle = None
    Area = None
    Length = None
    None = None
    value__ = None
    Volume = None


class VectorField(ComplexField, IDisposable):
    """
    Represents the definition of a vector within a Autodesk.Navisworks.Api.Schema.SchemaDefinition.
    
    VectorField(id: str, value: Field)
    VectorField(value: Field)
    """
    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def GetCount(self, accessor):
        """
        GetCount(self: VectorField, accessor: ReadAccessor) -> int
        
            Obtains the number of values held within a distinct Autodesk.Navisworks.Api.Schema.SchemaData object.
        
            accessor: Accessor provided by parent object e.g. from Autodesk.Navisworks.Api.Schema.SchemaData, or a containing Autodesk.Navisworks.Api.Schema.VectorFieldVectorField's IndexAccessor.
        """
        pass

    def GetIndexAccessor(self, accessor, index):
        """
        GetIndexAccessor(self: VectorField, accessor: EditAccessor, index: int) -> EditAccessor
        
            Obtains the appropriate accessor for a given index into the vector.
        
            accessor: Accessor provided by parent object e.g. from Autodesk.Navisworks.Api.Schema.SchemaData, or a containing Autodesk.Navisworks.Api.Schema.VectorFieldVectorField's IndexAccessor.
        GetIndexAccessor(self: VectorField, accessor: ReadAccessor, index: int) -> ReadAccessor
        
            Obtains the appropriate accessor for a given index into the vector.
        
            accessor: Accessor provided by parent object e.g. from Autodesk.Navisworks.Api.Schema.SchemaData, or a containing Autodesk.Navisworks.Api.Schema.VectorFieldVectorField's IndexAccessor.
        """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: Field, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> VectorField """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalGetEditAccessType(self, *args): #cannot find CLR method
        """ InternalGetEditAccessType(self: VectorField) -> Type """
        pass

    def InternalGetReadAccessType(self, *args): #cannot find CLR method
        """ InternalGetReadAccessType(self: VectorField) -> Type """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: Field) -> Void* """
        pass

    def SetCount(self, accessor, count):
        """
        SetCount(self: VectorField, accessor: EditAccessor, count: int)
            Sets the number of values held within a distinct Autodesk.Navisworks.Api.Schema.SchemaData object. Each index will be initialised to its default value.
        
            accessor: Accessor provided by parent object e.g. from Autodesk.Navisworks.Api.Schema.SchemaData, or a containing Autodesk.Navisworks.Api.Schema.VectorFieldVectorField's IndexAccessor.
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
        __new__(cls: type, id: str, value: Field)
        __new__(cls: type, value: Field)
        __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CollectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents collection metadata, including whether the collection is ordered, and whether the elements are unique.

Get: CollectionType(self: VectorField) -> VectorFieldCollectionType

Set: CollectionType(self: VectorField) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the object is read-only.

Get: IsReadOnly(self: VectorField) -> bool

"""

    ValueField = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A field object that identifies the type used within the vector & provides access to each index.

Get: ValueField(self: VectorField) -> Field

"""



class VectorFieldCollectionType(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents collection metadata, including whether the collection is ordered, and whether the elements are unique.
    
    enum VectorFieldCollectionType, values: Ordered (1), OrderedUnique (3), Unordered (0), UnorderedUnique (2)
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

    Ordered = None
    OrderedUnique = None
    Unordered = None
    UnorderedUnique = None
    value__ = None


