# encoding: utf-8
# module Autodesk.Revit.DB.Structure.StructuralSections calls itself StructuralSections
# from RevitAPI, Version=22.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class StructuralElementDefinitionData(object, IDisposable):
    """
    Class containing information about section and position of the structural element.
    
    StructuralElementDefinitionData()
    """
    def Dispose(self):
        """ Dispose(self: StructuralElementDefinitionData) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralElementDefinitionData, disposing: bool) """
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

    CenterCurve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The curve lying in the geometrical center of the element.

Get: CenterCurve(self: StructuralElementDefinitionData) -> Curve

"""

    Curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The definition curve of the element.

Get: Curve(self: StructuralElementDefinitionData) -> Curve

"""

    EndShortening = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Cutback or extension at element curve end.

Get: EndShortening(self: StructuralElementDefinitionData) -> float

"""

    IsMirrored = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """States if the structural section of the element is mirrored.

Get: IsMirrored(self: StructuralElementDefinitionData) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: StructuralElementDefinitionData) -> bool

"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The local Z direction of the element section in the start point of the curve.

Get: Normal(self: StructuralElementDefinitionData) -> XYZ

"""

    Section = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Structural section of the element.

Get: Section(self: StructuralElementDefinitionData) -> StructuralSection

"""

    StartShortening = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Cutback or extension at element curve start.

Get: StartShortening(self: StructuralElementDefinitionData) -> float

"""

    YJust = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Y justification (ref axis).

Get: YJust(self: StructuralElementDefinitionData) -> YJustification

"""

    YOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Y offset.

Get: YOffset(self: StructuralElementDefinitionData) -> float

"""

    ZJust = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Z justification (ref axis).

Get: ZJust(self: StructuralElementDefinitionData) -> ZJustification

"""

    ZOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Z offset.

Get: ZOffset(self: StructuralElementDefinitionData) -> float

"""



class StructuralSection(object, IEnumerable, IDisposable):
    """ The base class for StructuralSection specific classes, designed to provide common parameters and ability to differentiate between different structural section shapes. """
    def Dispose(self):
        """ Dispose(self: StructuralSection) """
        pass

    def GetBoundarySize(self):
        """
        GetBoundarySize(self: StructuralSection) -> UV
        
            Returns size of the section boundary.
            Returns: Size of the section boundary.
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: StructuralSection) -> IEnumerator """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AnalysisParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Common set of parameters for structural analysis.

Get: AnalysisParams(self: StructuralSection) -> StructuralSectionAnalysisParams

"""

    ElasticModulusStrongAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Elastic section modulus about main strong axis for calculation of bending stresses.

Get: ElasticModulusStrongAxis(self: StructuralSection) -> float

Set: ElasticModulusStrongAxis(self: StructuralSection) = value
"""

    ElasticModulusWeakAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Elastic section modulus about main weak axis for calculation of bending stresses.

Get: ElasticModulusWeakAxis(self: StructuralSection) -> float

Set: ElasticModulusWeakAxis(self: StructuralSection) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: StructuralSection) -> bool

"""

    MomentOfInertiaStrongAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Moment of Inertia about main strong axis (I).

Get: MomentOfInertiaStrongAxis(self: StructuralSection) -> float

Set: MomentOfInertiaStrongAxis(self: StructuralSection) = value
"""

    MomentOfInertiaWeakAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Moment of Inertia about main weak axis (I).

Get: MomentOfInertiaWeakAxis(self: StructuralSection) -> float

Set: MomentOfInertiaWeakAxis(self: StructuralSection) = value
"""

    NominalWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unit weight (not mass) per unit length, for self-weight calculation or quantity survey.

Get: NominalWeight(self: StructuralSection) -> float

Set: NominalWeight(self: StructuralSection) = value
"""

    Perimeter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Painting surface of the unit length.

Get: Perimeter(self: StructuralSection) -> float

Set: Perimeter(self: StructuralSection) = value
"""

    PlasticModulusStrongAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Plastic section modulus in bending about main strong axis (Z, Wpl).

Get: PlasticModulusStrongAxis(self: StructuralSection) -> float

Set: PlasticModulusStrongAxis(self: StructuralSection) = value
"""

    PlasticModulusWeakAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Plastic section modulus in bending about main weak axis.

Get: PlasticModulusWeakAxis(self: StructuralSection) -> float

Set: PlasticModulusWeakAxis(self: StructuralSection) = value
"""

    PrincipalAxesAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Rotation angle between the principal axes and cross section reference planes.

Get: PrincipalAxesAngle(self: StructuralSection) -> float

Set: PrincipalAxesAngle(self: StructuralSection) = value
"""

    SectionArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Cross section area.

Get: SectionArea(self: StructuralSection) -> float

Set: SectionArea(self: StructuralSection) = value
"""

    SectionNameKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A parameter in structural families which allows for family type identification.
   This will be used for data mapping during model exchange with another program, namely Advance Steel.

Get: SectionNameKey(self: StructuralSection) -> str

Set: SectionNameKey(self: StructuralSection) = value
"""

    ShearAreaStrongAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Shear area (reduced extreme shear stress coefficient) in the direction of strong axis (Wq).

Get: ShearAreaStrongAxis(self: StructuralSection) -> float

Set: ShearAreaStrongAxis(self: StructuralSection) = value
"""

    ShearAreaWeakAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Shear area (reduced extreme shear stress coefficient) in the direction of weak axis (Wq).

Get: ShearAreaWeakAxis(self: StructuralSection) -> float

Set: ShearAreaWeakAxis(self: StructuralSection) = value
"""

    StructuralSectionGeneralShape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The general type of structural section shape.

Get: StructuralSectionGeneralShape(self: StructuralSection) -> StructuralSectionGeneralShape

"""

    StructuralSectionShape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of structural section shape.

Get: StructuralSectionShape(self: StructuralSection) -> StructuralSectionShape

"""

    StructuralSectionShapeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A human readable string representing the structural section shape.

Get: StructuralSectionShapeName(self: StructuralSection) -> str

"""

    TorsionalModulus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Section modulus for calculations of torsion stresses (Ct).

Get: TorsionalModulus(self: StructuralSection) -> float

Set: TorsionalModulus(self: StructuralSection) = value
"""

    TorsionalMomentOfInertia = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Torsional Moment of inertia (J, IT, K), for calculation of torsional deformation

Get: TorsionalMomentOfInertia(self: StructuralSection) -> float

Set: TorsionalMomentOfInertia(self: StructuralSection) = value
"""

    WarpingConstant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Warping constant (Cw, Iomega, H).

Get: WarpingConstant(self: StructuralSection) -> float

Set: WarpingConstant(self: StructuralSection) = value
"""



class StructuralSectionAnalysisParams(object, IDisposable):
    """
    Defines common set of parameters for structural analysis.
    
    StructuralSectionAnalysisParams(principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    StructuralSectionAnalysisParams()
    """
    def Dispose(self):
        """ Dispose(self: StructuralSectionAnalysisParams) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSectionAnalysisParams, disposing: bool) """
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
    def __new__(self, principalAxesAngle=None, sectionArea=None, perimeter=None, nominalWeight=None, momentOfInertiaStrongAxis=None, momentOfInertiaWeakAxis=None, elasticModulusStrongAxis=None, elasticModulusWeakAxis=None, plasticModulusStrongAxis=None, plasticModulusWeakAxis=None, torsionalMomentOfInertia=None, torsionalModulus=None, warpingConstant=None, shearAreaStrongAxis=None, shearAreaWeakAxis=None):
        """
        __new__(cls: type, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ElasticModulusStrongAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Elastic section modulus about main strong axis for calculation of bending stresses.

Get: ElasticModulusStrongAxis(self: StructuralSectionAnalysisParams) -> float

Set: ElasticModulusStrongAxis(self: StructuralSectionAnalysisParams) = value
"""

    ElasticModulusWeakAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Elastic section modulus about main weak axis for calculation of bending stresses.

Get: ElasticModulusWeakAxis(self: StructuralSectionAnalysisParams) -> float

Set: ElasticModulusWeakAxis(self: StructuralSectionAnalysisParams) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: StructuralSectionAnalysisParams) -> bool

"""

    MomentOfInertiaStrongAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Moment of Inertia about main strong axis (I).

Get: MomentOfInertiaStrongAxis(self: StructuralSectionAnalysisParams) -> float

Set: MomentOfInertiaStrongAxis(self: StructuralSectionAnalysisParams) = value
"""

    MomentOfInertiaWeakAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Moment of Inertia about main weak axis (I).

Get: MomentOfInertiaWeakAxis(self: StructuralSectionAnalysisParams) -> float

Set: MomentOfInertiaWeakAxis(self: StructuralSectionAnalysisParams) = value
"""

    NominalWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unit weight (not mass) per unit length, for self-weight calculation or quantity survey.

Get: NominalWeight(self: StructuralSectionAnalysisParams) -> float

Set: NominalWeight(self: StructuralSectionAnalysisParams) = value
"""

    Perimeter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Painting surface of the unit length.

Get: Perimeter(self: StructuralSectionAnalysisParams) -> float

Set: Perimeter(self: StructuralSectionAnalysisParams) = value
"""

    PlasticModulusStrongAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Plastic section modulus in bending about main strong axis (Z, Wpl)

Get: PlasticModulusStrongAxis(self: StructuralSectionAnalysisParams) -> float

Set: PlasticModulusStrongAxis(self: StructuralSectionAnalysisParams) = value
"""

    PlasticModulusWeakAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Plastic section modulus in bending about main weak axis.

Get: PlasticModulusWeakAxis(self: StructuralSectionAnalysisParams) -> float

Set: PlasticModulusWeakAxis(self: StructuralSectionAnalysisParams) = value
"""

    PrincipalAxesAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Rotation angle between the principal axes and cross section reference planes.

Get: PrincipalAxesAngle(self: StructuralSectionAnalysisParams) -> float

Set: PrincipalAxesAngle(self: StructuralSectionAnalysisParams) = value
"""

    SectionArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Cross section area.

Get: SectionArea(self: StructuralSectionAnalysisParams) -> float

Set: SectionArea(self: StructuralSectionAnalysisParams) = value
"""

    ShearAreaStrongAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Shear area (reduced extreme shear stress coefficient) in the direction of strong axis (Wq).

Get: ShearAreaStrongAxis(self: StructuralSectionAnalysisParams) -> float

Set: ShearAreaStrongAxis(self: StructuralSectionAnalysisParams) = value
"""

    ShearAreaWeakAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Shear area (reduced extreme shear stress coefficient) in the direction of weak axis (Wq).

Get: ShearAreaWeakAxis(self: StructuralSectionAnalysisParams) -> float

Set: ShearAreaWeakAxis(self: StructuralSectionAnalysisParams) = value
"""

    TorsionalModulus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Section modulus for calculations of torsion stresses (Ct)

Get: TorsionalModulus(self: StructuralSectionAnalysisParams) -> float

Set: TorsionalModulus(self: StructuralSectionAnalysisParams) = value
"""

    TorsionalMomentOfInertia = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Torsional Moment of inertia (J, IT, K), for calculation of torsional deformation

Get: TorsionalMomentOfInertia(self: StructuralSectionAnalysisParams) -> float

Set: TorsionalMomentOfInertia(self: StructuralSectionAnalysisParams) = value
"""

    WarpingConstant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Warping constant (Cw, Iomega, H)

Get: WarpingConstant(self: StructuralSectionAnalysisParams) -> float

Set: WarpingConstant(self: StructuralSectionAnalysisParams) = value
"""



class StructuralSectionRectangular(StructuralSection, IEnumerable, IDisposable):
    """ Defines common set of parameters for structural section rectangular contour. """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CentroidHorizontal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance from centroid to the left extremites along horizontal axis.

Get: CentroidHorizontal(self: StructuralSectionRectangular) -> float

Set: CentroidHorizontal(self: StructuralSectionRectangular) = value
"""

    CentroidVertical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance from centroid to the upper extremites along vertical axis.

Get: CentroidVertical(self: StructuralSectionRectangular) -> float

Set: CentroidVertical(self: StructuralSectionRectangular) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Section height, depth.

Get: Height(self: StructuralSectionRectangular) -> float

Set: Height(self: StructuralSectionRectangular) = value
"""

    NameKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name Key

Get: NameKey(self: StructuralSectionRectangular) -> str

Set: NameKey(self: StructuralSectionRectangular) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Section width.

Get: Width(self: StructuralSectionRectangular) -> float

Set: Width(self: StructuralSectionRectangular) = value
"""



class StructuralSectionColdFormed(StructuralSectionRectangular, IEnumerable, IDisposable):
    """ Defines parameters for Hot Formed structural section. """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    InnerFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Inner Fillet - Corner fillet inner radius.

Get: InnerFillet(self: StructuralSectionColdFormed) -> float

Set: InnerFillet(self: StructuralSectionColdFormed) = value
"""

    WallDesignThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents wall design thickness of rectangle.

Get: WallDesignThickness(self: StructuralSectionColdFormed) -> float

Set: WallDesignThickness(self: StructuralSectionColdFormed) = value
"""

    WallNominalThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents wall nominal thickness of rectangle.

Get: WallNominalThickness(self: StructuralSectionColdFormed) -> float

Set: WallNominalThickness(self: StructuralSectionColdFormed) = value
"""



class StructuralSectionConcreteCross(StructuralSectionRectangular, IEnumerable, IDisposable):
    """
    Defines parameters for parameterized concrete cross structural section.
    
    StructuralSectionConcreteCross(width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, cantileverLength: float, cantileverHeight: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, cantileverLength, cantileverHeight):
        """ __new__(cls: type, width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, cantileverLength: float, cantileverHeight: float) """
        pass

    CantileverHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange cantilever thickness.

Get: CantileverHeight(self: StructuralSectionConcreteCross) -> float

Set: CantileverHeight(self: StructuralSectionConcreteCross) = value
"""

    CantileverLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange cantilever length.

Get: CantileverLength(self: StructuralSectionConcreteCross) -> float

Set: CantileverLength(self: StructuralSectionConcreteCross) = value
"""



class StructuralSectionConcreteRectangle(StructuralSectionRectangular, IEnumerable, IDisposable):
    """
    Defines parameters for parameterized concrete rectangle structural section.
    
    StructuralSectionConcreteRectangle(width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionConcreteRectangleCut(StructuralSectionRectangular, IEnumerable, IDisposable):
    """
    Defines parameters for parameterized concrete rectangle cut structural section.
    
    StructuralSectionConcreteRectangleCut(width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, topCutWidth: float, topCutHeight: float, bottomCutWidth: float, bottomCutHeight: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, topCutWidth, topCutHeight, bottomCutWidth, bottomCutHeight):
        """ __new__(cls: type, width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, topCutWidth: float, topCutHeight: float, bottomCutWidth: float, bottomCutHeight: float) """
        pass

    BottomCutHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Section height left Cut.

Get: BottomCutHeight(self: StructuralSectionConcreteRectangleCut) -> float

Set: BottomCutHeight(self: StructuralSectionConcreteRectangleCut) = value
"""

    BottomCutWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Section width left Cut.

Get: BottomCutWidth(self: StructuralSectionConcreteRectangleCut) -> float

Set: BottomCutWidth(self: StructuralSectionConcreteRectangleCut) = value
"""

    TopCutHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Section height right Cut.

Get: TopCutHeight(self: StructuralSectionConcreteRectangleCut) -> float

Set: TopCutHeight(self: StructuralSectionConcreteRectangleCut) = value
"""

    TopCutWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Section width right Cut.

Get: TopCutWidth(self: StructuralSectionConcreteRectangleCut) -> float

Set: TopCutWidth(self: StructuralSectionConcreteRectangleCut) = value
"""



class StructuralSectionRound(StructuralSection, IEnumerable, IDisposable):
    """ Defines common set of  parameters for structural section round contour. """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CentroidHorizontal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance from centroid to the left extremites along horizontal axis.

Get: CentroidHorizontal(self: StructuralSectionRound) -> float

Set: CentroidHorizontal(self: StructuralSectionRound) = value
"""

    CentroidVertical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance from centroid to the upper extremites along vertical axis.

Get: CentroidVertical(self: StructuralSectionRound) -> float

Set: CentroidVertical(self: StructuralSectionRound) = value
"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Pipe Diameter.

Get: Diameter(self: StructuralSectionRound) -> float

Set: Diameter(self: StructuralSectionRound) = value
"""

    NameKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name Key

Get: NameKey(self: StructuralSectionRound) -> str

Set: NameKey(self: StructuralSectionRound) = value
"""



class StructuralSectionConcreteRound(StructuralSectionRound, IEnumerable, IDisposable):
    """
    Creates a new instance of Structural Section Concrete Round shape with the associated set of parameters,
       used to attach to structural element.
    
    StructuralSectionConcreteRound(diameter: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, diameter, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, diameter: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionConcreteT(StructuralSectionRectangular, IEnumerable, IDisposable):
    """
    Defines parameters for parameterized concrete T structural section.
    
    StructuralSectionConcreteT(width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, cantileverLength: float, cantileverHeight: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, cantileverLength, cantileverHeight):
        """ __new__(cls: type, width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, cantileverLength: float, cantileverHeight: float) """
        pass

    CantileverHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange cantilever thickness.

Get: CantileverHeight(self: StructuralSectionConcreteT) -> float

Set: CantileverHeight(self: StructuralSectionConcreteT) = value
"""

    CantileverLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange cantilever length.

Get: CantileverLength(self: StructuralSectionConcreteT) -> float

Set: CantileverLength(self: StructuralSectionConcreteT) = value
"""



class StructuralSectionHotRolled(StructuralSectionRectangular, IEnumerable, IDisposable):
    """ Defines parameters for hot rolled structural sections. """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    FlangeThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange Thickness.

Get: FlangeThickness(self: StructuralSectionHotRolled) -> float

Set: FlangeThickness(self: StructuralSectionHotRolled) = value
"""

    FlangeThicknessLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange Thickness Location.

Get: FlangeThicknessLocation(self: StructuralSectionHotRolled) -> float

Set: FlangeThicknessLocation(self: StructuralSectionHotRolled) = value
"""

    WebFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Web Fillet - fillet radius between web and flange.

Get: WebFillet(self: StructuralSectionHotRolled) -> float

Set: WebFillet(self: StructuralSectionHotRolled) = value
"""

    WebThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Web Thickness.

Get: WebThickness(self: StructuralSectionHotRolled) -> float

Set: WebThickness(self: StructuralSectionHotRolled) = value
"""

    WebThicknessLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Web Thickness Location.

Get: WebThicknessLocation(self: StructuralSectionHotRolled) -> float

Set: WebThicknessLocation(self: StructuralSectionHotRolled) = value
"""



class StructuralSectionGeneralU(StructuralSectionHotRolled, IEnumerable, IDisposable):
    """
    Defines parameters for general Channel shape.
    
    StructuralSectionGeneralU(width: float, height: float, flangeThickness: float, flangeThicknessLocation: float, flangeFillet: float, flangeToeOfFillet: float, slopedFlangeAngle: float, webThickness: float, webFillet: float, webToeOfFillet: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def GetFlangeThicknessInFlangeCenter(self):
        """
        GetFlangeThicknessInFlangeCenter(self: StructuralSectionGeneralU) -> float
        
            Returns thickness of flange measured in the 0.5 * (width - webThickess),
           
             sometimes used for sections with width > 300 mm.
        """
        pass

    def GetFlangeThicknessInWidthCenter(self):
        """
        GetFlangeThicknessInWidthCenter(self: StructuralSectionGeneralU) -> float
        
            Returns thickness of flange measured in the 0.5 * width,
           sometimes used for 
             sections with width <= 300 mm.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, flangeThicknessLocation, flangeFillet, flangeToeOfFillet, slopedFlangeAngle, webThickness, webFillet, webToeOfFillet, centroidHorizontal, centroidVertical, analysisParams):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, flangeThicknessLocation: float, flangeFillet: float, flangeToeOfFillet: float, slopedFlangeAngle: float, webThickness: float, webFillet: float, webToeOfFillet: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams) """
        pass

    FlangeFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange Fillet - fillet radius at the flange end.

Get: FlangeFillet(self: StructuralSectionGeneralU) -> float

Set: FlangeFillet(self: StructuralSectionGeneralU) = value
"""

    FlangeToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from center of web to flange toe of fillet, in. (mm)

Get: FlangeToeOfFillet(self: StructuralSectionGeneralU) -> float

Set: FlangeToeOfFillet(self: StructuralSectionGeneralU) = value
"""

    SlopedFlangeAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sloped flange angle. (rad)

Get: SlopedFlangeAngle(self: StructuralSectionGeneralU) -> float

Set: SlopedFlangeAngle(self: StructuralSectionGeneralU) = value
"""

    WebToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from outer face of flange to web toe of fillet, in. (mm)

Get: WebToeOfFillet(self: StructuralSectionGeneralU) -> float

Set: WebToeOfFillet(self: StructuralSectionGeneralU) = value
"""



class StructuralSectionCParallelFlange(StructuralSectionGeneralU, IEnumerable, IDisposable):
    """
    Defines parameters for C-channel Parallel Flange structural section.
    
    StructuralSectionCParallelFlange(width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, flangeToeOfFillet: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, webThickness, webFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, clearWebHeight, flangeToeOfFillet, webToeOfFillet, boltSpacing, boltDiameter):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, flangeToeOfFillet: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float) """
        pass

    BoltDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter, in. (mm)

Get: BoltDiameter(self: StructuralSectionCParallelFlange) -> float

Set: BoltDiameter(self: StructuralSectionCParallelFlange) = value
"""

    BoltSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing, in. (mm)

Get: BoltSpacing(self: StructuralSectionCParallelFlange) -> float

Set: BoltSpacing(self: StructuralSectionCParallelFlange) = value
"""

    ClearWebHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing depth between the web toes of the fillets, in.(mm)

Get: ClearWebHeight(self: StructuralSectionCParallelFlange) -> float

Set: ClearWebHeight(self: StructuralSectionCParallelFlange) = value
"""



class StructuralSectionGeneralC(StructuralSectionColdFormed, IEnumerable, IDisposable):
    """
    Defines parameters for Channel Cold Formed shape.
    
    StructuralSectionGeneralC(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, lipLength: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, lipLength, centroidHorizontal, centroidVertical, analysisParams):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, lipLength: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams) """
        pass

    LipLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lip segment length.

Get: LipLength(self: StructuralSectionGeneralC) -> float

Set: LipLength(self: StructuralSectionGeneralC) = value
"""



class StructuralSectionCProfile(StructuralSectionGeneralC, IEnumerable, IDisposable):
    """
    Defines parameters for C Profile structural section.
    
    StructuralSectionCProfile(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionGeneralCEx(StructuralSectionColdFormed, IEnumerable, IDisposable):
    """
    Defines parameters for Channel With Fold Cold Formed shape.
    
    StructuralSectionGeneralCEx(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, lipLength: float, foldLength: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, lipLength, foldLength, centroidHorizontal, centroidVertical, analysisParams):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, lipLength: float, foldLength: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams) """
        pass

    FoldLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fold segment length.

Get: FoldLength(self: StructuralSectionGeneralCEx) -> float

Set: FoldLength(self: StructuralSectionGeneralCEx) = value
"""

    LipLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lip segment length.

Get: LipLength(self: StructuralSectionGeneralCEx) -> float

Set: LipLength(self: StructuralSectionGeneralCEx) = value
"""



class StructuralSectionCProfileWithFold(StructuralSectionGeneralCEx, IEnumerable, IDisposable):
    """
    Defines parameters for C Profile with fold structural section.
    
    StructuralSectionCProfileWithFold(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, lipLength: float, foldLength: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, lipLength, foldLength):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, lipLength: float, foldLength: float) """
        pass


class StructuralSectionCProfileWithLips(StructuralSectionGeneralC, IEnumerable, IDisposable):
    """
    Defines parameters for C Profile with lips structural section.
    
    StructuralSectionCProfileWithLips(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, lipLength: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, lipLength):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, lipLength: float) """
        pass


class StructuralSectionCSlopedFlange(StructuralSectionGeneralU, IEnumerable, IDisposable):
    """
    Defines parameters for C-channel Sloped Flange structural section.
    
    StructuralSectionCSlopedFlange(width: float, height: float, flangeThickness: float, flangeThicknessLocation: float, webThickness: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float, slopedFlangeAngle: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, flangeThicknessLocation, webThickness, webFillet, flangeFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, clearWebHeight, webToeOfFillet, boltSpacing, boltDiameter, slopedFlangeAngle):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, flangeThicknessLocation: float, webThickness: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float, slopedFlangeAngle: float) """
        pass

    BoltDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter, in. (mm)

Get: BoltDiameter(self: StructuralSectionCSlopedFlange) -> float

Set: BoltDiameter(self: StructuralSectionCSlopedFlange) = value
"""

    BoltSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing, in. (mm)

Get: BoltSpacing(self: StructuralSectionCSlopedFlange) -> float

Set: BoltSpacing(self: StructuralSectionCSlopedFlange) = value
"""

    ClearWebHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing depth between the web toes of the fillets, in.(mm)

Get: ClearWebHeight(self: StructuralSectionCSlopedFlange) -> float

Set: ClearWebHeight(self: StructuralSectionCSlopedFlange) = value
"""



class StructuralSectionErrorCode(Enum, IComparable, IFormattable, IConvertible):
    """
    Error codes for StructuralSection related operations.
    
    enum StructuralSectionErrorCode, values: ElementHasIndependentJustification (7), ElementNotSupported (4), Failure (1), IncompleteDefinition (3), MediumAndFineDetailShapesAreInconsistent (6), MediumDetailShapeHasRounding (5), ShapeNotRecognized (2), Success (0)
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

    ElementHasIndependentJustification = None
    ElementNotSupported = None
    Failure = None
    IncompleteDefinition = None
    MediumAndFineDetailShapesAreInconsistent = None
    MediumDetailShapeHasRounding = None
    ShapeNotRecognized = None
    Success = None
    value__ = None


class StructuralSectionGeneralF(StructuralSectionRectangular, IEnumerable, IDisposable):
    """
    Defines parameters for Flat Bar.
    
    StructuralSectionGeneralF(width: float, height: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, centroidHorizontal, centroidVertical, analysisParams):
        """ __new__(cls: type, width: float, height: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams) """
        pass


class StructuralSectionGeneralH(StructuralSectionRectangular, IEnumerable, IDisposable):
    """
    Defines parameters for Rectangular Pipe structural section.
    
    StructuralSectionGeneralH(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, outerFillet: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, outerFillet, centroidHorizontal, centroidVertical, analysisParams):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, outerFillet: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams) """
        pass

    InnerFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Inner Fillet - Corner fillet inner radius.

Get: InnerFillet(self: StructuralSectionGeneralH) -> float

Set: InnerFillet(self: StructuralSectionGeneralH) = value
"""

    OuterFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Outer Fillet - Corner fillet outer radius.

Get: OuterFillet(self: StructuralSectionGeneralH) -> float

Set: OuterFillet(self: StructuralSectionGeneralH) = value
"""

    WallDesignThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents wall design thickness of rectangle.

Get: WallDesignThickness(self: StructuralSectionGeneralH) -> float

Set: WallDesignThickness(self: StructuralSectionGeneralH) = value
"""

    WallNominalThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents wall nominal thickness of rectangle.

Get: WallNominalThickness(self: StructuralSectionGeneralH) -> float

Set: WallNominalThickness(self: StructuralSectionGeneralH) = value
"""



class StructuralSectionGeneralI(StructuralSectionHotRolled, IEnumerable, IDisposable):
    """
    Defines parameters for general Double T shape.
    
    StructuralSectionGeneralI(width: float, height: float, flangeThickness: float, flangeThicknessLocation: float, flangeFillet: float, flangeToeOfFillet: float, slopedFlangeAngle: float, webThickness: float, webFillet: float, webToeOfFillet: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def GetFlangeThicknessInFlangeCenter(self):
        """
        GetFlangeThicknessInFlangeCenter(self: StructuralSectionGeneralI) -> float
        
            Returns thickness of flange measured in the 0.25 * (width - webThickess),
           
             sometimes used for sections with width > 300 mm.
        """
        pass

    def GetFlangeThicknessInQuarterWidth(self):
        """
        GetFlangeThicknessInQuarterWidth(self: StructuralSectionGeneralI) -> float
        
            Returns thickness of flange measured in the 0.25 * width,
           sometimes used 
             for sections with width <= 300 mm.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, flangeThicknessLocation, flangeFillet, flangeToeOfFillet, slopedFlangeAngle, webThickness, webFillet, webToeOfFillet, centroidHorizontal, centroidVertical, analysisParams):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, flangeThicknessLocation: float, flangeFillet: float, flangeToeOfFillet: float, slopedFlangeAngle: float, webThickness: float, webFillet: float, webToeOfFillet: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams) """
        pass

    FlangeFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange Fillet - fillet radius at the flange end.

Get: FlangeFillet(self: StructuralSectionGeneralI) -> float

Set: FlangeFillet(self: StructuralSectionGeneralI) = value
"""

    FlangeToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from center of web to flange toe of fillet, in. (mm)

Get: FlangeToeOfFillet(self: StructuralSectionGeneralI) -> float

Set: FlangeToeOfFillet(self: StructuralSectionGeneralI) = value
"""

    SlopedFlangeAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sloped flange angle. (rad)

Get: SlopedFlangeAngle(self: StructuralSectionGeneralI) -> float

Set: SlopedFlangeAngle(self: StructuralSectionGeneralI) = value
"""

    WebToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from outer face of flange to web toe of fillet, in. (mm)

Get: WebToeOfFillet(self: StructuralSectionGeneralI) -> float

Set: WebToeOfFillet(self: StructuralSectionGeneralI) = value
"""



class StructuralSectionGeneralLA(StructuralSectionColdFormed, IEnumerable, IDisposable):
    """
    Defines parameters for Angle Cold Formed structural section.
    
    StructuralSectionGeneralLA(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, lipLength: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, lipLength, centroidHorizontal, centroidVertical, analysisParams):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, lipLength: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams) """
        pass

    LipLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lip segment length.

Get: LipLength(self: StructuralSectionGeneralLA) -> float

Set: LipLength(self: StructuralSectionGeneralLA) = value
"""



class StructuralSectionGeneralLZ(StructuralSectionColdFormed, IEnumerable, IDisposable):
    """
    Defines parameters for Z Cold Formed shape.
    
    StructuralSectionGeneralLZ(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, bottomFlangeLength: float, lipLength: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, bottomFlangeLength, lipLength, centroidHorizontal, centroidVertical, analysisParams):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, bottomFlangeLength: float, lipLength: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams) """
        pass

    BottomFlangeLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bottom Flange segment length.

Get: BottomFlangeLength(self: StructuralSectionGeneralLZ) -> float

Set: BottomFlangeLength(self: StructuralSectionGeneralLZ) = value
"""

    LipLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lip segment length.

Get: LipLength(self: StructuralSectionGeneralLZ) -> float

Set: LipLength(self: StructuralSectionGeneralLZ) = value
"""



class StructuralSectionGeneralR(StructuralSectionRound, IEnumerable, IDisposable):
    """
    Defines parameters for pipes.
    
    StructuralSectionGeneralR(diameter: float, wallNominalThickness: float, wallDesignThickness: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, diameter, wallNominalThickness, wallDesignThickness, centroidHorizontal, centroidVertical, analysisParams):
        """ __new__(cls: type, diameter: float, wallNominalThickness: float, wallDesignThickness: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams) """
        pass

    WallDesignThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents wall design thickness of rectangle.

Get: WallDesignThickness(self: StructuralSectionGeneralR) -> float

Set: WallDesignThickness(self: StructuralSectionGeneralR) = value
"""

    WallNominalThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents wall nominal thickness of rectangle.

Get: WallNominalThickness(self: StructuralSectionGeneralR) -> float

Set: WallNominalThickness(self: StructuralSectionGeneralR) = value
"""



class StructuralSectionGeneralS(StructuralSectionRound, IEnumerable, IDisposable):
    """
    Defines parameters for Round Bar structural section.
    
    StructuralSectionGeneralS(diameter: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, diameter, centroidHorizontal, centroidVertical, analysisParams):
        """ __new__(cls: type, diameter: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams) """
        pass


class StructuralSectionGeneralShape(Enum, IComparable, IFormattable, IConvertible):
    """
    General shapes for structural sections.
    
    enum StructuralSectionGeneralShape, values: GeneralC (2), GeneralCEx (11), GeneralF (10), GeneralH (7), GeneralI (1), GeneralLA (4), GeneralLZ (12), GeneralR (9), GeneralS (8), GeneralT (6), GeneralU (3), GeneralW (5), NotDefined (0)
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

    GeneralC = None
    GeneralCEx = None
    GeneralF = None
    GeneralH = None
    GeneralI = None
    GeneralLA = None
    GeneralLZ = None
    GeneralR = None
    GeneralS = None
    GeneralT = None
    GeneralU = None
    GeneralW = None
    NotDefined = None
    value__ = None


class StructuralSectionGeneralT(StructuralSectionHotRolled, IEnumerable, IDisposable):
    """
    Defines parameters for Tees shape.
    
    StructuralSectionGeneralT(width: float, height: float, flangeThickness: float, flangeThicknessLocation: float, flangeFillet: float, flangeToeOfFillet: float, slopedFlangeAngle: float, webThickness: float, webThicknessLocation: float, webFillet: float, topWebFillet: float, webToeOfFillet: float, slopedWebAngle: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def GetFlangeThicknessInFlangeCenter(self):
        """
        GetFlangeThicknessInFlangeCenter(self: StructuralSectionGeneralT) -> float
        
            Returns thickness of flange measured in the 0.25 * (width - webThickess),
           
             sometimes used for sections with width > 300 mm.
        """
        pass

    def GetFlangeThicknessInQuarterWidth(self):
        """
        GetFlangeThicknessInQuarterWidth(self: StructuralSectionGeneralT) -> float
        
            Returns thickness of flange measured in the 0.25 * width,
           sometimes used 
             for sections with width <= 300 mm.
        """
        pass

    def GetWebThicknessInHeightCenter(self):
        """
        GetWebThicknessInHeightCenter(self: StructuralSectionGeneralT) -> float
        
            Returns thickness of web measured in the 0.5 * height,
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, flangeThicknessLocation, flangeFillet, flangeToeOfFillet, slopedFlangeAngle, webThickness, webThicknessLocation, webFillet, topWebFillet, webToeOfFillet, slopedWebAngle, centroidHorizontal, centroidVertical, analysisParams):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, flangeThicknessLocation: float, flangeFillet: float, flangeToeOfFillet: float, slopedFlangeAngle: float, webThickness: float, webThicknessLocation: float, webFillet: float, topWebFillet: float, webToeOfFillet: float, slopedWebAngle: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams) """
        pass

    FlangeFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange Fillet - fillet radius at the flange end.

Get: FlangeFillet(self: StructuralSectionGeneralT) -> float

Set: FlangeFillet(self: StructuralSectionGeneralT) = value
"""

    FlangeToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from center of web to flange toe of fillet, in. (mm)

Get: FlangeToeOfFillet(self: StructuralSectionGeneralT) -> float

Set: FlangeToeOfFillet(self: StructuralSectionGeneralT) = value
"""

    SlopedFlangeAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sloped flange angle. (rad)

Get: SlopedFlangeAngle(self: StructuralSectionGeneralT) -> float

Set: SlopedFlangeAngle(self: StructuralSectionGeneralT) = value
"""

    SlopedWebAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sloped web angle. (rad)

Get: SlopedWebAngle(self: StructuralSectionGeneralT) -> float

Set: SlopedWebAngle(self: StructuralSectionGeneralT) = value
"""

    TopWebFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Top Web Fillet - fillet radius at the top of web.

Get: TopWebFillet(self: StructuralSectionGeneralT) -> float

Set: TopWebFillet(self: StructuralSectionGeneralT) = value
"""

    WebToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from outer face of flange to web toe of fillet, in. (mm)

Get: WebToeOfFillet(self: StructuralSectionGeneralT) -> float

Set: WebToeOfFillet(self: StructuralSectionGeneralT) = value
"""



class StructuralSectionGeneralW(StructuralSectionHotRolled, IEnumerable, IDisposable):
    """
    Defines parameters for Angle structural section.
    
    StructuralSectionGeneralW(width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, flangeFillet: float, topWebFillet: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, webThickness, webFillet, flangeFillet, topWebFillet, centroidHorizontal, centroidVertical, analysisParams):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, flangeFillet: float, topWebFillet: float, centroidHorizontal: float, centroidVertical: float, analysisParams: StructuralSectionAnalysisParams) """
        pass

    FlangeFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange Fillet - fillet radius at the flange end.

Get: FlangeFillet(self: StructuralSectionGeneralW) -> float

Set: FlangeFillet(self: StructuralSectionGeneralW) = value
"""

    TopWebFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Top Web Fillet - fillet radius at the top of web.

Get: TopWebFillet(self: StructuralSectionGeneralW) -> float

Set: TopWebFillet(self: StructuralSectionGeneralW) = value
"""



class StructuralSectionIParallelFlange(StructuralSectionGeneralI, IEnumerable, IDisposable):
    """
    Defines parameters for I-shape Parallel Flange structural section.
    
    StructuralSectionIParallelFlange(width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, flangeToeOfFillet: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, webThickness, webFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, clearWebHeight, flangeToeOfFillet, webToeOfFillet, boltSpacing, boltDiameter):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, flangeToeOfFillet: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float) """
        pass

    BoltDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter, in. (mm)

Get: BoltDiameter(self: StructuralSectionIParallelFlange) -> float

Set: BoltDiameter(self: StructuralSectionIParallelFlange) = value
"""

    BoltSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing, in. (mm)

Get: BoltSpacing(self: StructuralSectionIParallelFlange) -> float

Set: BoltSpacing(self: StructuralSectionIParallelFlange) = value
"""

    ClearWebHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing depth between the web toes of the fillets, in.(mm)

Get: ClearWebHeight(self: StructuralSectionIParallelFlange) -> float

Set: ClearWebHeight(self: StructuralSectionIParallelFlange) = value
"""



class StructuralSectionISlopedFlange(StructuralSectionGeneralI, IEnumerable, IDisposable):
    """
    Defines parameters for I-shape Sloped Flange structural section.
    
    StructuralSectionISlopedFlange(width: float, height: float, flangeThickness: float, flangeThicknessLocation: float, webThickness: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float, slopedFlangeAngle: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, flangeThicknessLocation, webThickness, webFillet, flangeFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, clearWebHeight, webToeOfFillet, boltSpacing, boltDiameter, slopedFlangeAngle):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, flangeThicknessLocation: float, webThickness: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float, slopedFlangeAngle: float) """
        pass

    BoltDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter, in. (mm)

Get: BoltDiameter(self: StructuralSectionISlopedFlange) -> float

Set: BoltDiameter(self: StructuralSectionISlopedFlange) = value
"""

    BoltSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing, in. (mm)

Get: BoltSpacing(self: StructuralSectionISlopedFlange) -> float

Set: BoltSpacing(self: StructuralSectionISlopedFlange) = value
"""

    ClearWebHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing depth between the web toes of the fillets, in.(mm)

Get: ClearWebHeight(self: StructuralSectionISlopedFlange) -> float

Set: ClearWebHeight(self: StructuralSectionISlopedFlange) = value
"""



class StructuralSectionISplitParallelFlange(StructuralSectionGeneralT, IEnumerable, IDisposable):
    """
    Defines parameters for I-split Parallel Flange structural section.
    
    StructuralSectionISplitParallelFlange(width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, flangeToeOfFillet: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, webThickness, webFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, clearWebHeight, flangeToeOfFillet, webToeOfFillet, boltSpacing, boltDiameter):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, flangeToeOfFillet: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float) """
        pass

    BoltDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter, in. (mm)

Get: BoltDiameter(self: StructuralSectionISplitParallelFlange) -> float

Set: BoltDiameter(self: StructuralSectionISplitParallelFlange) = value
"""

    BoltSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing, in. (mm)

Get: BoltSpacing(self: StructuralSectionISplitParallelFlange) -> float

Set: BoltSpacing(self: StructuralSectionISplitParallelFlange) = value
"""

    ClearWebHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing depth between the web toes of the fillets, in.(mm)

Get: ClearWebHeight(self: StructuralSectionISplitParallelFlange) -> float

Set: ClearWebHeight(self: StructuralSectionISplitParallelFlange) = value
"""



class StructuralSectionISplitSlopedFlange(StructuralSectionGeneralT, IEnumerable, IDisposable):
    """
    Defines parameters for I-split Sloped Flange structural section.
    
    StructuralSectionISplitSlopedFlange(width: float, height: float, flangeThickness: float, flangeThicknessLocation: float, webThickness: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float, slopedFlangeAngle: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, flangeThicknessLocation, webThickness, webFillet, flangeFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, clearWebHeight, webToeOfFillet, boltSpacing, boltDiameter, slopedFlangeAngle):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, flangeThicknessLocation: float, webThickness: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float, slopedFlangeAngle: float) """
        pass

    BoltDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter, in. (mm)

Get: BoltDiameter(self: StructuralSectionISplitSlopedFlange) -> float

Set: BoltDiameter(self: StructuralSectionISplitSlopedFlange) = value
"""

    BoltSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing, in. (mm)

Get: BoltSpacing(self: StructuralSectionISplitSlopedFlange) -> float

Set: BoltSpacing(self: StructuralSectionISplitSlopedFlange) = value
"""

    ClearWebHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing depth between the web toes of the fillets, in.(mm)

Get: ClearWebHeight(self: StructuralSectionISplitSlopedFlange) -> float

Set: ClearWebHeight(self: StructuralSectionISplitSlopedFlange) = value
"""



class StructuralSectionIWelded(StructuralSectionRectangular, IEnumerable, IDisposable):
    """
    Defines parameters for I-shape Welded structural section.
    
    StructuralSectionIWelded(width: float, height: float, topFlangeThickness: float, topFlangeWidth: float, bottomFlangeThickness: float, bottomFlangeWidth: float, webThickness: float, webHeight: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, topFlangeThickness, topFlangeWidth, bottomFlangeThickness, bottomFlangeWidth, webThickness, webHeight, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, width: float, height: float, topFlangeThickness: float, topFlangeWidth: float, bottomFlangeThickness: float, bottomFlangeWidth: float, webThickness: float, webHeight: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass

    BottomFlangeThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bottom Flange Thickness.

Get: BottomFlangeThickness(self: StructuralSectionIWelded) -> float

Set: BottomFlangeThickness(self: StructuralSectionIWelded) = value
"""

    BottomFlangeWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bottom Flange Width.

Get: BottomFlangeWidth(self: StructuralSectionIWelded) -> float

Set: BottomFlangeWidth(self: StructuralSectionIWelded) = value
"""

    TopFlangeThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Top Flange Thickness.

Get: TopFlangeThickness(self: StructuralSectionIWelded) -> float

Set: TopFlangeThickness(self: StructuralSectionIWelded) = value
"""

    TopFlangeWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Top Flange Width.

Get: TopFlangeWidth(self: StructuralSectionIWelded) -> float

Set: TopFlangeWidth(self: StructuralSectionIWelded) = value
"""

    WebHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Web Height.

Get: WebHeight(self: StructuralSectionIWelded) -> float

Set: WebHeight(self: StructuralSectionIWelded) = value
"""

    WebThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Web Thickness.

Get: WebThickness(self: StructuralSectionIWelded) -> float

Set: WebThickness(self: StructuralSectionIWelded) = value
"""



class StructuralSectionIWideFlange(StructuralSectionHotRolled, IEnumerable, IDisposable):
    """
    Defines parameters for I-shape Wide Flange structural section.
    
    StructuralSectionIWideFlange(width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, flangeToeOfFillet: float, webToeOfFillet: float, boltSpacing: float, boltSpacingTwoRows: float, boltSpacingBetweenRows: float, boltDiameter: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, webThickness, webFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, clearWebHeight, flangeToeOfFillet, webToeOfFillet, boltSpacing, boltSpacingTwoRows, boltSpacingBetweenRows, boltDiameter):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, flangeToeOfFillet: float, webToeOfFillet: float, boltSpacing: float, boltSpacingTwoRows: float, boltSpacingBetweenRows: float, boltDiameter: float) """
        pass

    BoltDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter, in. (mm)

Get: BoltDiameter(self: StructuralSectionIWideFlange) -> float

Set: BoltDiameter(self: StructuralSectionIWideFlange) = value
"""

    BoltSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing, in. (mm)

Get: BoltSpacing(self: StructuralSectionIWideFlange) -> float

Set: BoltSpacing(self: StructuralSectionIWideFlange) = value
"""

    BoltSpacingBetweenRows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing between rows, in. (mm)

Get: BoltSpacingBetweenRows(self: StructuralSectionIWideFlange) -> float

Set: BoltSpacingBetweenRows(self: StructuralSectionIWideFlange) = value
"""

    BoltSpacingTwoRows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing for two rows , in. (mm)

Get: BoltSpacingTwoRows(self: StructuralSectionIWideFlange) -> float

Set: BoltSpacingTwoRows(self: StructuralSectionIWideFlange) = value
"""

    ClearWebHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing depth between the web toes of the fillets, in.(mm)

Get: ClearWebHeight(self: StructuralSectionIWideFlange) -> float

Set: ClearWebHeight(self: StructuralSectionIWideFlange) = value
"""

    FlangeToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from center of web to flange toe of fillet, in. (mm)

Get: FlangeToeOfFillet(self: StructuralSectionIWideFlange) -> float

Set: FlangeToeOfFillet(self: StructuralSectionIWideFlange) = value
"""

    WebToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from outer face of flange to web toe of fillet, in. (mm)

Get: WebToeOfFillet(self: StructuralSectionIWideFlange) -> float

Set: WebToeOfFillet(self: StructuralSectionIWideFlange) = value
"""



class StructuralSectionLAngle(StructuralSectionGeneralW, IEnumerable, IDisposable):
    """
    Defines parameters for L-angle Flange structural section.
    
    StructuralSectionLAngle(width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, boltSpacing1LongerFlange: float, boltSpacing2LongerFlange: float, boltSpacingShorterFlange: float, boltDiameterLongerFlange: float, boltDiameterShorterFlange: float, topWebFillet: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, webThickness, webFillet, flangeFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, boltSpacing1LongerFlange, boltSpacing2LongerFlange, boltSpacingShorterFlange, boltDiameterLongerFlange, boltDiameterShorterFlange, topWebFillet):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, boltSpacing1LongerFlange: float, boltSpacing2LongerFlange: float, boltSpacingShorterFlange: float, boltDiameterLongerFlange: float, boltDiameterShorterFlange: float, topWebFillet: float) """
        pass

    BoltDiameterLongerFlange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter in the longer flange, in. (mm)

Get: BoltDiameterLongerFlange(self: StructuralSectionLAngle) -> float

Set: BoltDiameterLongerFlange(self: StructuralSectionLAngle) = value
"""

    BoltDiameterShorterFlange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter in the shorter flange, in. (mm)

Get: BoltDiameterShorterFlange(self: StructuralSectionLAngle) -> float

Set: BoltDiameterShorterFlange(self: StructuralSectionLAngle) = value
"""

    BoltSpacing1LongerFlange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing first row in the longer flange, in. (mm)

Get: BoltSpacing1LongerFlange(self: StructuralSectionLAngle) -> float

Set: BoltSpacing1LongerFlange(self: StructuralSectionLAngle) = value
"""

    BoltSpacing2LongerFlange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing second row in the longer flange, in. (mm)

Get: BoltSpacing2LongerFlange(self: StructuralSectionLAngle) -> float

Set: BoltSpacing2LongerFlange(self: StructuralSectionLAngle) = value
"""

    BoltSpacingShorterFlange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing in the shorter flange, in. (mm)

Get: BoltSpacingShorterFlange(self: StructuralSectionLAngle) -> float

Set: BoltSpacingShorterFlange(self: StructuralSectionLAngle) = value
"""



class StructuralSectionLProfile(StructuralSectionGeneralLA, IEnumerable, IDisposable):
    """
    Defines parameters for L profile structural section.
    
    StructuralSectionLProfile(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionLProfileWithLips(StructuralSectionGeneralLA, IEnumerable, IDisposable):
    """
    Defines parameters for L Profile with lips structural section.
    
    StructuralSectionLProfileWithLips(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, lipLength: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, lipLength):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, lipLength: float) """
        pass


class StructuralSectionPipeStandard(StructuralSectionGeneralR, IEnumerable, IDisposable):
    """
    Defines parameters for pipes also known as RoundHSS or HollowStructuralSection (HSS).
    
    StructuralSectionPipeStandard(diameter: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, wallNominalThickness: float, wallDesignThickness: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, diameter, centroidHorizontal, centroidVertical, principalAxesAngle, wallNominalThickness, wallDesignThickness, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, diameter: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, wallNominalThickness: float, wallDesignThickness: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionRectangleHSS(StructuralSectionGeneralH, IEnumerable, IDisposable):
    """
    Defines parameters for parameterized rectangle HSS structural section.
    
    StructuralSectionRectangleHSS(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, outerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, outerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, outerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionRectangleParameterized(StructuralSectionGeneralF, IEnumerable, IDisposable):
    """
    Defines parameters for parameterized rectangle structural section.
    
    StructuralSectionRectangleParameterized(width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionRectangularBar(StructuralSectionGeneralF, IEnumerable, IDisposable):
    """
    Defines parameters for Rectangular Bar structural section.
    
    StructuralSectionRectangularBar(width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionRoundBar(StructuralSectionGeneralS, IEnumerable, IDisposable):
    """
    Defines parameters for Round Bar structural section.
    
    StructuralSectionRoundBar(diameter: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, diameter, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, diameter: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionRoundHSS(StructuralSectionGeneralR, IEnumerable, IDisposable):
    """
    Defines parameters for pipes known as Round HSS (HollowStructuralSection).
    
    StructuralSectionRoundHSS(diameter: float, wallNominalThickness: float, wallDesignThickness: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, diameter, wallNominalThickness, wallDesignThickness, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, diameter: float, wallNominalThickness: float, wallDesignThickness: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionShape(Enum, IComparable, IFormattable, IConvertible):
    """
    Shapes for structural sections.
    
    enum StructuralSectionShape, values: ConcreteCross (34), ConcreteRectangle (31), ConcreteRectangleCut (32), ConcreteRound (35), ConcreteT (33), CParallelFlange (9), CProfile (20), CProfileWithFold (22), CProfileWithLips (21), CSlopedFlange (10), Invalid (-1), IParallelFlange (6), ISlopedFlange (7), ISplitParallelFlange (17), ISplitSlopedFlange (18), IWelded (16), IWideFlange (8), LAngle (11), LProfile (23), LProfileWithLips (24), NotDefined (0), PipeStandard (5), RectangleHSS (14), RectangleParameterized (2), RectangularBar (12), RoundBar (13), RoundHSS (15), SigmaProfile (27), SigmaProfileWithFold (29), SigmaProfileWithLips (28), StructuralTees (19), UserDefined (30), ZProfile (25), ZProfileWithLips (26)
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

    ConcreteCross = None
    ConcreteRectangle = None
    ConcreteRectangleCut = None
    ConcreteRound = None
    ConcreteT = None
    CParallelFlange = None
    CProfile = None
    CProfileWithFold = None
    CProfileWithLips = None
    CSlopedFlange = None
    Invalid = None
    IParallelFlange = None
    ISlopedFlange = None
    ISplitParallelFlange = None
    ISplitSlopedFlange = None
    IWelded = None
    IWideFlange = None
    LAngle = None
    LProfile = None
    LProfileWithLips = None
    NotDefined = None
    PipeStandard = None
    RectangleHSS = None
    RectangleParameterized = None
    RectangularBar = None
    RoundBar = None
    RoundHSS = None
    SigmaProfile = None
    SigmaProfileWithFold = None
    SigmaProfileWithLips = None
    StructuralTees = None
    UserDefined = None
    value__ = None
    ZProfile = None
    ZProfileWithLips = None


class StructuralSectionSigmaProfile(StructuralSectionColdFormed, IEnumerable, IDisposable):
    """
    Defines parameters for Sigma Profile structural section.
    
    StructuralSectionSigmaProfile(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, bendWidth: float, middleBendLength: float, topBendLength: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, bendWidth, middleBendLength, topBendLength):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, bendWidth: float, middleBendLength: float, topBendLength: float) """
        pass

    BendWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bend segment width.

Get: BendWidth(self: StructuralSectionSigmaProfile) -> float

Set: BendWidth(self: StructuralSectionSigmaProfile) = value
"""

    MiddleBendLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Middle Bend segment length.

Get: MiddleBendLength(self: StructuralSectionSigmaProfile) -> float

Set: MiddleBendLength(self: StructuralSectionSigmaProfile) = value
"""

    TopBendLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Top Bend segment length.

Get: TopBendLength(self: StructuralSectionSigmaProfile) -> float

Set: TopBendLength(self: StructuralSectionSigmaProfile) = value
"""



class StructuralSectionSigmaProfileWithFold(StructuralSectionColdFormed, IEnumerable, IDisposable):
    """
    Defines parameters for structural Sigma profile section with fold.
    
    StructuralSectionSigmaProfileWithFold(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, foldWidth: float, lipLength: float, bendWidth: float, middleBendLength: float, topBendLength: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, foldWidth, lipLength, bendWidth, middleBendLength, topBendLength):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, foldWidth: float, lipLength: float, bendWidth: float, middleBendLength: float, topBendLength: float) """
        pass

    BendWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bend segment width.

Get: BendWidth(self: StructuralSectionSigmaProfileWithFold) -> float

Set: BendWidth(self: StructuralSectionSigmaProfileWithFold) = value
"""

    FoldWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fold segment width.

Get: FoldWidth(self: StructuralSectionSigmaProfileWithFold) -> float

Set: FoldWidth(self: StructuralSectionSigmaProfileWithFold) = value
"""

    LipLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lip segment length.

Get: LipLength(self: StructuralSectionSigmaProfileWithFold) -> float

Set: LipLength(self: StructuralSectionSigmaProfileWithFold) = value
"""

    MiddleBendLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Middle Bend segment length.

Get: MiddleBendLength(self: StructuralSectionSigmaProfileWithFold) -> float

Set: MiddleBendLength(self: StructuralSectionSigmaProfileWithFold) = value
"""

    TopBendLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Top Bend segment length.

Get: TopBendLength(self: StructuralSectionSigmaProfileWithFold) -> float

Set: TopBendLength(self: StructuralSectionSigmaProfileWithFold) = value
"""



class StructuralSectionSigmaProfileWithLips(StructuralSectionColdFormed, IEnumerable, IDisposable):
    """
    Defines parameters for structural Sigma Profile section with lips.
    
    StructuralSectionSigmaProfileWithLips(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, lipLength: float, bendWidth: float, middleBendLength: float, topBendLength: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, lipLength, bendWidth, middleBendLength, topBendLength):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, lipLength: float, bendWidth: float, middleBendLength: float, topBendLength: float) """
        pass

    BendWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bend segment width.

Get: BendWidth(self: StructuralSectionSigmaProfileWithLips) -> float

Set: BendWidth(self: StructuralSectionSigmaProfileWithLips) = value
"""

    LipLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lip segment length.

Get: LipLength(self: StructuralSectionSigmaProfileWithLips) -> float

Set: LipLength(self: StructuralSectionSigmaProfileWithLips) = value
"""

    MiddleBendLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Middle Bend segment length.

Get: MiddleBendLength(self: StructuralSectionSigmaProfileWithLips) -> float

Set: MiddleBendLength(self: StructuralSectionSigmaProfileWithLips) = value
"""

    TopBendLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Top Bend segment length.

Get: TopBendLength(self: StructuralSectionSigmaProfileWithLips) -> float

Set: TopBendLength(self: StructuralSectionSigmaProfileWithLips) = value
"""



class StructuralSectionStructuralTees(StructuralSectionGeneralT, IEnumerable, IDisposable):
    """
    Defines parameters for Structural Tees structural section.
    
    StructuralSectionStructuralTees(width: float, height: float, flangeThickness: float, flangeThicknessLocation: float, webThickness: float, webThicknessLocation: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, boltSpacing: float, boltSpacingWeb: float, boltDiameter: float, slopedFlangeAngle: float, slopedWebAngle: float, topWebFillet: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, flangeThicknessLocation, webThickness, webThicknessLocation, webFillet, flangeFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, boltSpacing, boltSpacingWeb, boltDiameter, slopedFlangeAngle, slopedWebAngle, topWebFillet):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, flangeThicknessLocation: float, webThickness: float, webThicknessLocation: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, boltSpacing: float, boltSpacingWeb: float, boltDiameter: float, slopedFlangeAngle: float, slopedWebAngle: float, topWebFillet: float) """
        pass

    BoltDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter, in. (mm)

Get: BoltDiameter(self: StructuralSectionStructuralTees) -> float

Set: BoltDiameter(self: StructuralSectionStructuralTees) = value
"""

    BoltSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing in the flange, in. (mm)

Get: BoltSpacing(self: StructuralSectionStructuralTees) -> float

Set: BoltSpacing(self: StructuralSectionStructuralTees) = value
"""

    BoltSpacingWeb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing in the web, in. (mm)

Get: BoltSpacingWeb(self: StructuralSectionStructuralTees) -> float

Set: BoltSpacingWeb(self: StructuralSectionStructuralTees) = value
"""



class StructuralSectionUserDefined(StructuralSectionRectangular, IEnumerable, IDisposable):
    """
    Defines parameters for parameterized user defined structural section.
    
    StructuralSectionUserDefined(width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionUtils(object):
    """ This class provides utilities related to Structural Section Properties. """
    @staticmethod
    def GetStructuralElementDefinitionData(document, elementId, data):
        """
        GetStructuralElementDefinitionData(document: Document, elementId: ElementId) -> (StructuralSectionErrorCode, StructuralElementDefinitionData)
        
            Return structural element definition data.
        
            document: The document that owns the beam, brace or structural column.
            elementId: ID of family instance for beam, brace or structural column.
            Returns: Success code is returned if StructuralElementDefinitionData was provided 
             successfully, error code otherwise.
        """
        pass

    @staticmethod
    def GetStructuralSection(document, elementId):
        """
        GetStructuralSection(document: Document, elementId: ElementId) -> StructuralSection
        
            Return structural section from element.
        
            document: The document that owns the family for beam, brace or structural column.
            elementId: ID of family symbol or family instance for beam, brace or structural column.
            Returns: Structural section returned if element have one.
           For elements that do not 
             have structural section or can not have structural section ll will be returned.
        """
        pass

    @staticmethod
    def SetStructuralSection(document, familySymbolId, structuralSection):
        """
        SetStructuralSection(document: Document, familySymbolId: ElementId, structuralSection: StructuralSection) -> bool
        
            Set structural section in element.
        
            document: The document that owns the family for beam, brace or structural column.
            familySymbolId: ID of family symbol for beam, brace or structural column.
            structuralSection: Structural section with values that will be set.
            Returns: True is returned when requested shape with values was properly set. Return 
             false otherwise.
        """
        pass

    __all__ = [
        'GetStructuralElementDefinitionData',
        'GetStructuralSection',
        'SetStructuralSection',
    ]


class StructuralSectionZProfile(StructuralSectionGeneralLZ, IEnumerable, IDisposable):
    """
    Defines parameters for Z Profile structural section.
    
    StructuralSectionZProfile(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, bottomFlangeLength: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, bottomFlangeLength):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, bottomFlangeLength: float) """
        pass


class StructuralSectionZProfileWithLips(StructuralSectionGeneralLZ, IEnumerable, IDisposable):
    """
    Defines parameters for Z Profile with lips structural section.
    
    StructuralSectionZProfileWithLips(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, bottomFlangeLength: float, lipLength: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, bottomFlangeLength, lipLength):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, bottomFlangeLength: float, lipLength: float) """
        pass


