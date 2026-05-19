# encoding: utf-8
# module Autodesk.Navisworks.Api.Bim360 calls itself Bim360
# from Autodesk.Navisworks.Api, Version=19.0.1374.1, Culture=neutral, PublicKeyToken=d85e58fa5af9b484
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AccountInfo(object):
    """
    Provides information about a BIM 360 Account.
    
    AccountInfo()
    """
    AccountGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Guid identifier of Account.

Get: AccountGuid(self: AccountInfo) -> Guid

Set: AccountGuid(self: AccountInfo) = value
"""

    AccountId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifier of Account.

Get: AccountId(self: AccountInfo) -> str

Set: AccountId(self: AccountInfo) = value
"""

    AuthToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """AuthToken related to this Account.

Get: AuthToken(self: AccountInfo) -> str

Set: AuthToken(self: AccountInfo) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of this Account.

Get: Name(self: AccountInfo) -> str

Set: Name(self: AccountInfo) = value
"""

    UserType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """User type of this Account.

Get: UserType(self: AccountInfo) -> str

Set: UserType(self: AccountInfo) = value
"""



class ResourceInfo(object):
    """
    Provides information about a BIM 360 Resource.
    
    ResourceInfo()
    """
    AccountId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifier of Account the resource belongs to.

Get: AccountId(self: ResourceInfo) -> str

Set: AccountId(self: ResourceInfo) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Display name of the resource.

Get: DisplayName(self: ResourceInfo) -> str

Set: DisplayName(self: ResourceInfo) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Version independent identifier for the resource.

Get: Id(self: ResourceInfo) -> Guid

Set: Id(self: ResourceInfo) = value
"""

    ParentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Optional identifier of Parent of the resource.

Get: ParentId(self: ResourceInfo) -> Nullable[Guid]

Set: ParentId(self: ResourceInfo) = value
"""

    ProjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifier of Project the resource belongs to.

Get: ProjectId(self: ResourceInfo) -> Guid

Set: ProjectId(self: ResourceInfo) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of the resource.

Get: Type(self: ResourceInfo) -> ResourceType

Set: Type(self: ResourceInfo) = value
"""

    VersionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Version dependent identifier for the resource.

Get: VersionId(self: ResourceInfo) -> Guid

Set: VersionId(self: ResourceInfo) = value
"""



class ResourceType(Enum, IComparable, IFormattable, IConvertible):
    """
    Resource Type.
    
    enum ResourceType, values: MergedModel (2), Model (1), Project (0)
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

    MergedModel = None
    Model = None
    Project = None
    value__ = None


