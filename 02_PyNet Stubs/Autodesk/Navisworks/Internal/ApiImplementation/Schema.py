# Auto-generated — Navisworks 24 — Autodesk.Navisworks.Internal.ApiImplementation.Schema

class ArrayAccess(FieldAccess):
    """.NET: Autodesk.Navisworks.Internal.ApiImplementation.Schema.ArrayAccess`2"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool
    Item: CollectionType
    Field: FieldType
    def GetEnumerator(self, ) -> IEnumerator: ...

class FieldAccess:
    """.NET: Autodesk.Navisworks.Internal.ApiImplementation.Schema.FieldAccess`1"""
    def __init__(self, *args) -> None: ...
    Field: FieldType

class GroupAccess(FieldAccess):
    """.NET: Autodesk.Navisworks.Internal.ApiImplementation.Schema.GroupAccess"""
    def __init__(self, *args) -> None: ...
    Field: GroupField

class GroupEditor(GroupAccess):
    """.NET: Autodesk.Navisworks.Internal.ApiImplementation.Schema.GroupEditor"""
    def __init__(self, *args) -> None: ...
    Accessor: EditAccessor
    Field: GroupField

class GroupReader(GroupAccess):
    """.NET: Autodesk.Navisworks.Internal.ApiImplementation.Schema.GroupReader"""
    def __init__(self, *args) -> None: ...
    Accessor: ReadAccessor
    Field: GroupField

class IDataEditAccess:
    """.NET: Autodesk.Navisworks.Internal.ApiImplementation.Schema.IDataEditAccess"""
    def __init__(self, *args) -> None: ...
    Accessor: EditAccessor

class IDataReadAccess:
    """.NET: Autodesk.Navisworks.Internal.ApiImplementation.Schema.IDataReadAccess"""
    def __init__(self, *args) -> None: ...
    Accessor: ReadAccessor

class SimpleAccess(FieldAccess):
    """.NET: Autodesk.Navisworks.Internal.ApiImplementation.Schema.SimpleAccess`2"""
    def __init__(self, *args) -> None: ...
    DefaultValue: SimpleType
    Field: SimpleFieldType
    def Equals(self, rhs: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class SimpleEditor(SimpleAccess):
    """.NET: Autodesk.Navisworks.Internal.ApiImplementation.Schema.SimpleEditor`2"""
    def __init__(self, *args) -> None: ...
    Accessor: EditAccessor
    DefaultValue: SimpleType
    Field: SimpleFieldType

class SimpleReader(SimpleAccess):
    """.NET: Autodesk.Navisworks.Internal.ApiImplementation.Schema.SimpleReader`2"""
    def __init__(self, *args) -> None: ...
    Accessor: ReadAccessor
    DefaultValue: SimpleType
    Field: SimpleFieldType

class VectorEditor(ArrayAccess):
    """.NET: Autodesk.Navisworks.Internal.ApiImplementation.Schema.VectorEditor`1"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool
    Item: ValueType
    Length: int
    Accessor: EditAccessor
    Field: VectorField

class VectorReader(ArrayAccess):
    """.NET: Autodesk.Navisworks.Internal.ApiImplementation.Schema.VectorReader`1"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool
    Item: ValueType
    Length: int
    Accessor: ReadAccessor
    Field: VectorField

class VectorSimpleEditor(VectorEditor):
    """.NET: Autodesk.Navisworks.Internal.ApiImplementation.Schema.VectorSimpleEditor`1"""
    def __init__(self, *args) -> None: ...
    DefaultValue: ValueType
    IsReadOnly: bool
    Item: ValueType
    Length: int
    Accessor: EditAccessor
    Field: VectorField

class VectorSimpleReader(VectorReader):
    """.NET: Autodesk.Navisworks.Internal.ApiImplementation.Schema.VectorSimpleReader`1"""
    def __init__(self, *args) -> None: ...
    DefaultValue: ValueType
    IsReadOnly: bool
    Item: ValueType
    Length: int
    Accessor: ReadAccessor
    Field: VectorField
