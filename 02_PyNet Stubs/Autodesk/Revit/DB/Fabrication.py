# encoding: utf-8
# module Autodesk.Revit.DB.Fabrication calls itself Fabrication
# from RevitAPI, Version=22.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DesignToFabricationConverter(object, IDisposable):
    """
    This class represents the MEP design to fabrication part convert tool.
    
    DesignToFabricationConverter(document: Document)
    """
    def Convert(self, selection, serviceId):
        """ Convert(self: DesignToFabricationConverter, selection: ISet[ElementId], serviceId: int) -> DesignToFabricationConverterResult """
        pass

    def Dispose(self):
        """ Dispose(self: DesignToFabricationConverter) """
        pass

    def GetConvertedFabricationParts(self):
        """
        GetConvertedFabricationParts(self: DesignToFabricationConverter) -> ISet[ElementId]
        
            Gets the set of element identifiers for newly created fabrication parts.
        """
        pass

    def GetConvertedFabricationPartsWithInvalidConnections(self):
        """
        GetConvertedFabricationPartsWithInvalidConnections(self: DesignToFabricationConverter) -> IDictionary[ElementId, ElementId]
        
            Gets the collection of converted fabrication parts with invalid connections.
        """
        pass

    def GetDesignElementAndFabricationPartsWithDifferentOffsets(self):
        """
        GetDesignElementAndFabricationPartsWithDifferentOffsets(self: DesignToFabricationConverter) -> IDictionary[ElementId, ISet[ElementId]]
        
            Gets the collection of design elements that failed to convert and the 
             associated set of fabrication parts with different offsets.
        
            Returns: A map of design element identifiers that were not converted and the associated 
             set fabrication parts left with different offsets.
        """
        pass

    def GetDesignElementAndFabricationPartsWithOpenConnectors(self):
        """
        GetDesignElementAndFabricationPartsWithOpenConnectors(self: DesignToFabricationConverter) -> IDictionary[ElementId, ISet[ElementId]]
        
            Gets the collection of design elements that failed to convert and the 
             associated set of fabrication parts with open connectors.
        
            Returns: A map of design element identifiers that were not converted and the associated 
             set fabrication parts left with open connectors.
        """
        pass

    def GetElementsWithOpenConnector(self):
        """
        GetElementsWithOpenConnector(self: DesignToFabricationConverter) -> ISet[ElementId]
        
            Gets the set of fabrication part or MEP design element identifiers with open 
             connectors, caused by fittings failing to convert.
        """
        pass

    def GetPartialConvertFailureResults(self):
        """
        GetPartialConvertFailureResults(self: DesignToFabricationConverter) -> IList[PartialFailureResults]
        
            Gets the partial failure results.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DesignToFabricationConverter, disposing: bool) """
        pass

    def SetMapForFamilySymbolToFabricationPartType(self, typeMappings):
        """ SetMapForFamilySymbolToFabricationPartType(self: DesignToFabricationConverter, typeMappings: IDictionary[ElementId, ElementId]) -> DesignToFabricationMappingResult """
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
    def __new__(self, document):
        """ __new__(cls: type, document: Document) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: DesignToFabricationConverter) -> bool

"""



class DesignToFabricationConverterResult(Enum, IComparable, IFormattable, IConvertible):
    """
    Possible results from invoking the DesignToFabricationConverter.
    
    enum DesignToFabricationConverterResult, values: PartialFailure (1), Success (0)
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

    PartialFailure = None
    Success = None
    value__ = None


class DesignToFabricationMappingResult(Enum, IComparable, IFormattable, IConvertible):
    """
    Possible results from setting the mapping from Family symbols to Fabrication part types.
    
    enum DesignToFabricationMappingResult, values: InvalidFabricationPartType (3), InvalidFamilySymbol (2), Success (0), Undefined (1), UnsupportedFabricationPartType (5), UnsupportedFamilySymbol (4)
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

    InvalidFabricationPartType = None
    InvalidFamilySymbol = None
    Success = None
    Undefined = None
    UnsupportedFabricationPartType = None
    UnsupportedFamilySymbol = None
    value__ = None


class FabricationAncillaryType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all fabrication ancillary types.
    
    enum FabricationAncillaryType, values: AirturnTrack (9), AirturnVane (10), AncillaryMaterial (8), Clip (3), Corner (2), Fixing (1), Gasket (5), Isolator (11), Sealant (6), SeamMaterial (12), SupportRod (7), TieRod (4), Unknown (0)
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

    AirturnTrack = None
    AirturnVane = None
    AncillaryMaterial = None
    Clip = None
    Corner = None
    Fixing = None
    Gasket = None
    Isolator = None
    Sealant = None
    SeamMaterial = None
    SupportRod = None
    TieRod = None
    Unknown = None
    value__ = None


class FabricationAncillaryUsageType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type describing where an ancillary is used on a fabrication part.
    
    enum FabricationAncillaryUsageType, values: Airturn (5), Connector (2), Hanger (6), Loose (1), Seam (3), Splitter (4), Stiffener (7), Undefined (0)
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

    Airturn = None
    Connector = None
    Hanger = None
    Loose = None
    Seam = None
    Splitter = None
    Stiffener = None
    Undefined = None
    value__ = None


class FabricationCustomDataType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all fabrication custom data value types.
    
    enum FabricationCustomDataType, values: Integer (2), Real (3), Text (1)
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

    Integer = None
    Real = None
    Text = None
    value__ = None


class FabricationNetworkChangeService(object, IDisposable):
    """
    This class represents the fabrication part change service and change size tools.
    
    FabricationNetworkChangeService(document: Document)
    """
    def ApplyChange(self):
        """
        ApplyChange(self: FabricationNetworkChangeService) -> FabricationNetworkChangeServiceResult
        
            Applies the previously set changes to the selection of fabrication parts to 
             change the size, change the service, or both.
        """
        pass

    def ChangeService(self, selection, serviceId, paletteId, restrictPalette=None):
        """
        ChangeService(self: FabricationNetworkChangeService, selection: ISet[ElementId], serviceId: int, paletteId: int) -> FabricationNetworkChangeServiceResult
        ChangeService(self: FabricationNetworkChangeService, selection: ISet[ElementId], serviceId: int, paletteId: int, restrictPalette: bool) -> FabricationNetworkChangeServiceResult
        """
        pass

    def ChangeSize(self, selection, fabricationPartSizeMaps):
        """ ChangeSize(self: FabricationNetworkChangeService, selection: ISet[ElementId], fabricationPartSizeMaps: ISet[FabricationPartSizeMap]) -> FabricationNetworkChangeServiceResult """
        pass

    def Dispose(self):
        """ Dispose(self: FabricationNetworkChangeService) """
        pass

    def GetElementsThatFailed(self):
        """
        GetElementsThatFailed(self: FabricationNetworkChangeService) -> ISet[ElementId]
        
            Gets the set of fabrication parts that had failures due to either there was no 
             corresponding part in the service, the size was out of range, or a connection 
             could not be made.
        """
        pass

    def GetInLinePartTypes(self):
        """
        GetInLinePartTypes(self: FabricationNetworkChangeService) -> ISet[ElementId]
        
            Get a set of element identifiers of fabrication part types for in-line parts.
            Returns: Returns the set of element identifiers for in-line parts or an empty set if 
             there are none.
        """
        pass

    def GetMapOfAllSizesForStraights(self):
        """
        GetMapOfAllSizesForStraights(self: FabricationNetworkChangeService) -> ISet[FabricationPartSizeMap]
        
            Get a set of FabricationPartSizeMapSet of all straight sizes for all services.
            Returns: Returns the map of sizes for straights or an empty map if there are none.
        """
        pass

    def GetStraightsThatWereNotChanged(self):
        """
        GetStraightsThatWereNotChanged(self: FabricationNetworkChangeService) -> ISet[ElementId]
        
            Gets the set of fabrication part straights that were not changed due to either 
             there was no corresponding part in the service or the size was out of range.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FabricationNetworkChangeService, disposing: bool) """
        pass

    def SetGroupId(self, groupId):
        """
        SetGroupId(self: FabricationNetworkChangeService, groupId: int)
            This method is deprecated in Revit 2022 and may be removed in a future version 
             of Revit.
           Please use the `SetPaletteId` method instead.
        """
        pass

    def SetMapOfInLinePartTypes(self, fabricationPartTypes):
        """ SetMapOfInLinePartTypes(self: FabricationNetworkChangeService, fabricationPartTypes: IDictionary[ElementId, ElementId]) """
        pass

    def SetMapOfSizesForStraights(self, fabricationPartSizeMaps):
        """ SetMapOfSizesForStraights(self: FabricationNetworkChangeService, fabricationPartSizeMaps: ISet[FabricationPartSizeMap]) """
        pass

    def SetPaletteId(self, paletteId):
        """
        SetPaletteId(self: FabricationNetworkChangeService, paletteId: int)
            Set the fabrication palette identifier to change the elements to.
        """
        pass

    def SetRestrictGroup(self, restrictGroup):
        """
        SetRestrictGroup(self: FabricationNetworkChangeService, restrictGroup: bool)
            This method is deprecated in Revit 2022 and may be removed in a future version 
             of Revit.
           Please use the `SetRestrictPalette` method instead.
        """
        pass

    def SetRestrictPalette(self, restrictPalette):
        """
        SetRestrictPalette(self: FabricationNetworkChangeService, restrictPalette: bool)
            Restrict the placement of parts to only use parts associated to the passed in 
             fabrication palette identifier.
        """
        pass

    def SetSelection(self, selection):
        """ SetSelection(self: FabricationNetworkChangeService, selection: ISet[ElementId]) -> FabricationNetworkChangeServiceResult """
        pass

    def SetServiceId(self, serviceId):
        """
        SetServiceId(self: FabricationNetworkChangeService, serviceId: int)
            Set the fabrication service identifier to change the elements to.
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
    def __new__(self, document):
        """ __new__(cls: type, document: Document) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FabricationNetworkChangeService) -> bool

"""



class FabricationNetworkChangeServiceResult(Enum, IComparable, IFormattable, IConvertible):
    """
    Possible results from invoking the FabricationNetworkChangeService.
    
    enum FabricationNetworkChangeServiceResult, values: InvalidSelection (3), PartialFailure (1), Success (0), UserAborted (2)
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

    InvalidSelection = None
    PartialFailure = None
    Success = None
    UserAborted = None
    value__ = None


class FabricationPartCompareType(Enum, IComparable, IFormattable, IConvertible):
    """
    Fabrication Part Comparison Types
    
    enum FabricationPartCompareType, values: Alias (25), Alt (23), BoxNo (18), ButtonAlias (28), CID (11), CustomData (27), CutType (1), Description (10), Drawing (20), DuctFacing (6), ETag (22), Filename (9), Insulation (7), InsulationSpecification (4), Material (2), MaterialGauge (5), Notes (8), OrderNo (19), Pallet (17), PCFKey (26), Section (14), Service (16), SkinGauge (13), SkinMaterial (12), Specification (3), Spool (24), Status (15), Zone (21)
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

    Alias = None
    Alt = None
    BoxNo = None
    ButtonAlias = None
    CID = None
    CustomData = None
    CutType = None
    Description = None
    Drawing = None
    DuctFacing = None
    ETag = None
    Filename = None
    Insulation = None
    InsulationSpecification = None
    Material = None
    MaterialGauge = None
    Notes = None
    OrderNo = None
    Pallet = None
    PCFKey = None
    Section = None
    Service = None
    SkinGauge = None
    SkinMaterial = None
    Specification = None
    Spool = None
    Status = None
    value__ = None
    Zone = None


class FabricationPartFitResult(Enum, IComparable, IFormattable, IConvertible):
    """
    Fabrication part stretch/fill result.
    
    enum FabricationPartFitResult, values: BadDimensions (4), DimensionLocked (3), IncompatibleConnection (7), IncompatibleGeometry (1), MisalignedEnds (2), OffsetRequired (8), ShapeMismatch (5), SizeMismatch (6), Success (0), Unsupported (255)
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

    BadDimensions = None
    DimensionLocked = None
    IncompatibleConnection = None
    IncompatibleGeometry = None
    MisalignedEnds = None
    OffsetRequired = None
    ShapeMismatch = None
    SizeMismatch = None
    Success = None
    Unsupported = None
    value__ = None


class FabricationPartJustification(Enum, IComparable, IFormattable, IConvertible):
    """
    Fabrication part eccentric justifications for alignment for flat edged parts.
    
    enum FabricationPartJustification, values: Bottom (1), Middle (0), Top (2)
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

    Bottom = None
    Middle = None
    Top = None
    value__ = None


class FabricationPartPlacementUtils(object):
    """ General utility placement methods in the Autodesk Revit MEP product for fabrication. """
    __all__ = []


class FabricationPartRouteEnd(object, IDisposable):
    """ Class to hold fabrication part routing start or end information. """
    @staticmethod
    def CreateFromCenterline(element, ptAt):
        """
        CreateFromCenterline(element: Element, ptAt: XYZ) -> FabricationPartRouteEnd
        
            Create fabrication routing end from centreline point on straight element.
        
            element: The straight element that the centerline is on.
            ptAt: A point along the straight element where the fitting to be cut in should be 
             positioned.
        """
        pass

    @staticmethod
    def CreateFromConnector(connnector):
        """
        CreateFromConnector(connnector: Connector) -> FabricationPartRouteEnd
        
            Create fabrication routing end from connector end point.
        
            connnector: The connector that the route will connect to. Must not already be connected.
        """
        pass

    def Dispose(self):
        """ Dispose(self: FabricationPartRouteEnd) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FabricationPartRouteEnd, disposing: bool) """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FabricationPartRouteEnd) -> bool

"""



class FabricationPartSizeMap(object, IDisposable):
    """
    This class represents the fabrication part size map for straights allowing the sizes to be changed from a user interface for multiple straights with diffent sizes.
    
    FabricationPartSizeMap(size: str, widthDiameter: float, depth: float, isProductList: bool, profileType: ConnectorProfileType, serviceId: int, paletteId: int)
    FabricationPartSizeMap(size: str, widthDiameter: float, depth: float, isProductList: bool)
    """
    def Dispose(self):
        """ Dispose(self: FabricationPartSizeMap) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FabricationPartSizeMap, disposing: bool) """
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
    def __new__(self, size, widthDiameter, depth, isProductList, profileType=None, serviceId=None, paletteId=None):
        """
        __new__(cls: type, size: str, widthDiameter: float, depth: float, isProductList: bool, profileType: ConnectorProfileType, serviceId: int, paletteId: int)
        __new__(cls: type, size: str, widthDiameter: float, depth: float, isProductList: bool)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AllowMultipleServiceSizes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """State flag to allow multiple services to include the same size.

Get: AllowMultipleServiceSizes(self: FabricationPartSizeMap) -> bool

Set: AllowMultipleServiceSizes(self: FabricationPartSizeMap) = value
"""

    Depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The depth of the straight.

Get: Depth(self: FabricationPartSizeMap) -> float

Set: Depth(self: FabricationPartSizeMap) = value
"""

    GroupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is deprecated in Revit 2022 and may be removed in a future version of Revit.
   Please use the `PaletteId` method instead.

Get: GroupId(self: FabricationPartSizeMap) -> int

Set: GroupId(self: FabricationPartSizeMap) = value
"""

    IsMappedProductList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Are the mapped sizes for a product listed fabrication part.

Get: IsMappedProductList(self: FabricationPartSizeMap) -> bool

Set: IsMappedProductList(self: FabricationPartSizeMap) = value
"""

    IsProductList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Are the sizes for a product listed fabrication part.

Get: IsProductList(self: FabricationPartSizeMap) -> bool

Set: IsProductList(self: FabricationPartSizeMap) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FabricationPartSizeMap) -> bool

"""

    MappedDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mapped size for the depth of the straight.

Get: MappedDepth(self: FabricationPartSizeMap) -> float

Set: MappedDepth(self: FabricationPartSizeMap) = value
"""

    MappedProfileType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mapped shape of the straight.

Get: MappedProfileType(self: FabricationPartSizeMap) -> ConnectorProfileType

Set: MappedProfileType(self: FabricationPartSizeMap) = value
"""

    MappedServiceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mapped service identifier of the straight.

Get: MappedServiceId(self: FabricationPartSizeMap) -> int

Set: MappedServiceId(self: FabricationPartSizeMap) = value
"""

    MappedWidthDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mapped size for the width or diameter of the straight.

Get: MappedWidthDiameter(self: FabricationPartSizeMap) -> float

Set: MappedWidthDiameter(self: FabricationPartSizeMap) = value
"""

    PaletteId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The palette identifier of the straight.

Get: PaletteId(self: FabricationPartSizeMap) -> int

Set: PaletteId(self: FabricationPartSizeMap) = value
"""

    ProfileType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The shape of the straight.

Get: ProfileType(self: FabricationPartSizeMap) -> ConnectorProfileType

Set: ProfileType(self: FabricationPartSizeMap) = value
"""

    ServiceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The service identifier of the straight.

Get: ServiceId(self: FabricationPartSizeMap) -> int

Set: ServiceId(self: FabricationPartSizeMap) = value
"""

    SizeString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size display string for the straight that can be used by the user interface.

Get: SizeString(self: FabricationPartSizeMap) -> str

Set: SizeString(self: FabricationPartSizeMap) = value
"""

    WidthDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The width or diameter of the straight.

Get: WidthDiameter(self: FabricationPartSizeMap) -> float

Set: WidthDiameter(self: FabricationPartSizeMap) = value
"""



class FabricationSaveJobOptions(object, IDisposable):
    """
    Options for FabricationPart.SaveAsFabricationJob() method.
    
    FabricationSaveJobOptions(addHolesForTaps: bool)
    FabricationSaveJobOptions()
    """
    def Dispose(self):
        """ Dispose(self: FabricationSaveJobOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FabricationSaveJobOptions, disposing: bool) """
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
    def __new__(self, addHolesForTaps=None):
        """
        __new__(cls: type, addHolesForTaps: bool)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AddHolesForTaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set true to have holes for taps on straights added to the created fabrication job.

Get: AddHolesForTaps(self: FabricationSaveJobOptions) -> bool

Set: AddHolesForTaps(self: FabricationSaveJobOptions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FabricationSaveJobOptions) -> bool

"""



class FabricationUtils(object):
    """ General utility methods in the Autodesk Revit MEP product for fabrication. """
    @staticmethod
    def ExportToPCF(document, ids, filename):
        """ ExportToPCF(document: Document, ids: IList[ElementId], filename: str) """
        pass

    @staticmethod
    def ValidateConnectivity(document, connector1, connector2):
        """
        ValidateConnectivity(document: Document, connector1: Connector, connector2: Connector) -> bool
        
            Check if two connectors are valid to connect directly without couplings
        
            document: The document.
            connector1: First connector to check.
            connector2: Second connector to check against.
            Returns: True if connection is valid, false otherwise.
        """
        pass

    __all__ = [
        'ExportToPCF',
        'ValidateConnectivity',
    ]


class PartialFailureResults(Enum, IComparable, IFormattable, IConvertible):
    """
    Possible results of the partial failure from invoking the DesignToFabricationConverter.
    
    enum PartialFailureResults, values: HaveDifferentOffsets (3), HaveOpenConnectors (2), InvalidConnections (1), NoMatchingSize (4), NotAllPartsConverted (0)
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

    HaveDifferentOffsets = None
    HaveOpenConnectors = None
    InvalidConnections = None
    NoMatchingSize = None
    NotAllPartsConverted = None
    value__ = None


class ValidationStatus(Enum, IComparable, IFormattable, IConvertible):
    """
    Lists the validation type of the fabrication part.
    
    enum ValidationStatus, values: InvalidDimensions (1), NoMaterial (2), Valid (0)
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

    InvalidDimensions = None
    NoMaterial = None
    Valid = None
    value__ = None


