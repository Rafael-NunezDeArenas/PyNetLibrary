# encoding: utf-8
# module Autodesk.Revit.DB.Steel calls itself Steel
# from RevitAPI, Version=22.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class SteelElementProperties(APIObject, IDisposable):
    """ This class is used to attach steel fabrication information to various Revit elements. """
    @staticmethod
    def AddFabricationInformationForRevitElements(aDoc, elementIds):
        """ AddFabricationInformationForRevitElements(aDoc: Document, elementIds: IList[ElementId]) -> IList[ElementId] """
        pass

    def Dispose(self):
        """ Dispose(self: SteelElementProperties, A_0: bool) """
        pass

    @staticmethod
    def GetFabricationUniqueID(aDoc, reference):
        """
        GetFabricationUniqueID(aDoc: Document, reference: Reference) -> Guid
        
            This method will return the fabrication id for the given reference.
        
            aDoc: Document to which the reference belongs.
            reference: The reference to the element or subelement for which fabrication id is required.
            Returns: The fabrication id of the element or subelement for this reference, if it has 
             fabrication information attached, or an Guid.Empty otherwise.
        """
        pass

    @staticmethod
    def GetReference(aDoc, guid):
        """
        GetReference(aDoc: Document, guid: Guid) -> Reference
        
            This method will return the reference for the given fabrication id.
        
            aDoc: Document in which to search for the reference.
            guid: The fabrication id for which a reference is required.
            Returns: The reference to the element or subelement corresponding to the given id.
        """
        pass

    @staticmethod
    def GetSteelElementProperties(pElement):
        """
        GetSteelElementProperties(pElement: Element) -> SteelElementProperties
        
            Get SteelElementProperties for the input element if they exist.
        
            pElement: The element from which we try to obtain SteelElementProperties.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: SteelElementProperties, disposing: bool)ReleaseUnmanagedResources(self: APIObject) """
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

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: SteelElementProperties) -> bool

"""

    UniqueID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This method will return the fabrication id. This represents the link between the Revit and the Steel Core element.

Get: UniqueID(self: SteelElementProperties) -> Guid

"""



