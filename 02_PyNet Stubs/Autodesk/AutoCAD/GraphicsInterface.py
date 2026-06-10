# Auto-generated — Civil 26 — Autodesk.AutoCAD.GraphicsInterface

class ArcType:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ArcType"""
    def __init__(self, *args) -> None: ...
    ...

class AttenuationType:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.AttenuationType"""
    def __init__(self, *args) -> None: ...
    ...

class AutoTransform:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.AutoTransform"""
    def __init__(self, *args) -> None: ...
    ...

class ChannelFlags:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ChannelFlags"""
    def __init__(self, *args) -> None: ...
    ...

class ClipBoundary(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ClipBoundary"""
    def __init__(self, *args) -> None: ...
    DrawBoundary: bool
    BackClipZ: float
    FrontClipZ: float
    ClippingBack: bool
    ClippingFront: bool
    TransformInverseBlockRefXForm: Matrix3d
    TransformToClipSpace: Matrix3d
    Point: Point3d
    NormalVector: Vector3d
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetAptPoints(self, ) -> Point2dCollection: ...
    def SetAptPoints(self, point: Point2dCollection) -> None: ...

class ColorRGB:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ColorRGB"""
    def __init__(self, *args) -> None: ...
    Blue: float
    Green: float
    Red: float

class ColorRGBA:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ColorRGBA"""
    def __init__(self, *args) -> None: ...
    Alpha: float
    Blue: float
    Green: float
    Red: float

class CommonDraw(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.CommonDraw"""
    def __init__(self, *args) -> None: ...
    NumberOfIsolines: int
    IsDragging: bool
    Context: Context
    RawGeometry: Geometry
    SubEntityTraits: SubEntityTraits
    RegenAbort: bool
    RegenType: RegenType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Deviation(self, deviationType: DeviationType, pointOnCurve: Point3d) -> float: ...

class Context(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Context"""
    def __init__(self, *args) -> None: ...
    SupportsCurveTrait: bool
    SupportsTrueTypeText: bool
    ByBlockPlotStyleNameId: ObjectId
    ByBlockLineWeight: LineWeight
    EffectiveColor: EntityColor
    IsNesting: bool
    IsBoundaryClipping: bool
    Database: Database
    IsPlotGeneration: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DisableFastMoveDrag(self, ) -> None: ...

class ContextualColors(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ContextualColors"""
    def __init__(self, *args) -> None: ...
    LightDistanceColor: Color
    LightShapeColor: Color
    WebMeshMissingColor: Color
    WebMeshColor: Color
    CameraClipping: int
    CameraFrustrum: int
    CameraGlyphs: int
    LightEndLimit: int
    LightStartLimit: int
    LightFalloff: int
    LightHotspot: int
    LightGlyphs: int
    GridAxisLineTintXYZ: int
    GridMinorLineTintXYZ: int
    GridMajorLineTintXYZ: int
    GridAxisLines: int
    GridMinorLines: int
    GridMajorLines: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def FlagsSet(self, flag: int) -> bool: ...
    def SetContextFlags(self, flag: int, set: bool) -> None: ...

class DefaultLightingType:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.DefaultLightingType"""
    def __init__(self, *args) -> None: ...
    ...

class DeviationType:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.DeviationType"""
    def __init__(self, *args) -> None: ...
    ...

class DistantLightTraits(StandardLightTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.DistantLightTraits"""
    def __init__(self, *args) -> None: ...
    SkyParameters: SkyParameters
    LampColor: ColorRGB
    PhysicalIntensity: float
    IsSunlight: bool
    LightDirection: Vector3d
    Shadow: ShadowParameters
    LightColor: Color
    Intensity: float
    On: bool
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class DrawFlags:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.DrawFlags"""
    def __init__(self, *args) -> None: ...
    ...

class DrawStream(Drawable):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.DrawStream"""
    def __init__(self, *args) -> None: ...
    Owner: Drawable
    IsValid: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    Id: ObjectId
    IsPersistent: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Drawable(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Drawable"""
    def __init__(self, *args) -> None: ...
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    Id: ObjectId
    IsPersistent: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetAttributes(self, traits: DrawableTraits) -> int: ...
    def ViewportDraw(self, vd: ViewportDraw) -> None: ...
    def ViewportDrawLogicalFlags(self, vd: ViewportDraw) -> int: ...
    def WorldDraw(self, wd: WorldDraw) -> bool: ...

class DrawableAttributes:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.DrawableAttributes"""
    def __init__(self, *args) -> None: ...
    ...

class DrawableOverrule(Overrule):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.DrawableOverrule"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetAttributes(self, drawable: Drawable, traits: DrawableTraits) -> int: ...
    def SetCustomFilter(self, ) -> None: ...
    def SetExtensionDictionaryEntryFilter(self, entryName: str) -> None: ...
    def SetIdFilter(self, ids: list) -> None: ...
    def SetNoFilter(self, ) -> None: ...
    def SetXDataFilter(self, registeredApplicationName: str) -> None: ...
    def ViewportDraw(self, drawable: Drawable, vd: ViewportDraw) -> None: ...
    def ViewportDrawLogicalFlags(self, drawable: Drawable, vd: ViewportDraw) -> int: ...
    def WorldDraw(self, drawable: Drawable, wd: WorldDraw) -> bool: ...

class DrawableTraits(SubEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.DrawableTraits"""
    def __init__(self, *args) -> None: ...
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddLight(self, lightId: ObjectId) -> None: ...
    def GetHighlightProperty(self, propertyType: HighlightProperty) -> object: ...
    def SetHighlightProperty(self, propertyType: HighlightProperty, value: object) -> None: ...
    def SetupForEntity(self, entity: Entity) -> None: ...

class DrawableType:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.DrawableType"""
    def __init__(self, *args) -> None: ...
    ...

class EdgeData:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.EdgeData"""
    def __init__(self, *args) -> None: ...
    def GetColors(self, ) -> list: ...
    def GetLayers(self, ) -> list: ...
    def GetLineTypes(self, ) -> list: ...
    def GetSelectionMarkers(self, ) -> list: ...
    def GetTrueColors(self, ) -> list: ...
    def GetVisibility(self, ) -> list: ...
    def SetColors(self, colors: list) -> None: ...
    def SetLayers(self, layers: list) -> None: ...
    def SetLineTypes(self, lineTypes: list) -> None: ...
    def SetSelectionMarkers(self, selectionMarkers: list) -> None: ...
    def SetTrueColors(self, colors: list) -> None: ...
    def SetVisibility(self, visibility: list) -> None: ...

class ExtendedLightShape:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ExtendedLightShape"""
    def __init__(self, *args) -> None: ...
    ...

class ExteriorDaylightMode:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ExteriorDaylightMode"""
    def __init__(self, *args) -> None: ...
    ...

class FaceData:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.FaceData"""
    def __init__(self, *args) -> None: ...
    def GetColors(self, ) -> list: ...
    def GetLayers(self, ) -> list: ...
    def GetMappers(self, ) -> list: ...
    def GetMaterials(self, ) -> list: ...
    def GetNormalVectors(self, ) -> list: ...
    def GetSelectionMarkers(self, ) -> list: ...
    def GetTransparency(self, ) -> list: ...
    def GetTrueColors(self, ) -> list: ...
    def GetVisibility(self, ) -> list: ...
    def SetColors(self, colors: list) -> None: ...
    def SetLayers(self, layers: list) -> None: ...
    def SetMappers(self, mappers: list) -> None: ...
    def SetMaterials(self, materials: list) -> None: ...
    def SetNormalVectors(self, normal: list) -> None: ...
    def SetSelectionMarkers(self, selectionMarker: list) -> None: ...
    def SetTransparency(self, transparency: list) -> None: ...
    def SetTrueColors(self, colors: list) -> None: ...
    def SetVisibility(self, visibility: list) -> None: ...

class Fill(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Fill"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class FillType:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.FillType"""
    def __init__(self, *args) -> None: ...
    ...

class FinalGatherMode:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.FinalGatherMode"""
    def __init__(self, *args) -> None: ...
    ...

class FontDescriptor:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.FontDescriptor"""
    def __init__(self, *args) -> None: ...
    PitchAndFamily: int
    CharacterSet: int
    Italic: bool
    Bold: bool
    TypeFace: str
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class FrontAndBackClipping:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.FrontAndBackClipping"""
    def __init__(self, *args) -> None: ...
    Back: float
    Front: float
    ClipBack: bool
    ClipFront: bool
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def IsEqualTo(self, a: FrontAndBackClipping, tolerance: Tolerance) -> bool: ...

class GdiDrawObject(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.GdiDrawObject"""
    def __init__(self, *args) -> None: ...
    Height: int
    Width: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Draw(self, hDC: IntPtr, bounds: Rectangle) -> bool: ...

class GenericTexture(ProceduralTexture):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.GenericTexture"""
    def __init__(self, *args) -> None: ...
    Definition: object
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> GenericTexture: ...
    def CopyFrom(self, pSrc: GenericTexture) -> None: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def Set(self, value: GenericTexture) -> None: ...

class Geometry(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Geometry"""
    def __init__(self, *args) -> None: ...
    WorldToModelTransform: Matrix3d
    ModelToWorldTransform: Matrix3d
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Circle(self, firstPoint: Point3d, secondPoint: Point3d, thirdPoint: Point3d) -> bool: ...
    def CircularArc(self, center: Point3d, radius: float, normal: Vector3d, startVector: Vector3d, sweepAngle: float, arcType: ArcType) -> bool: ...
    def Curve(self, curve3d: Curve3d) -> bool: ...
    def Draw(self, value: Drawable) -> bool: ...
    def Edge(self, e: Curve2dCollection) -> bool: ...
    def EllipticalArc(self, center: Point3d, normal: Vector3d, majorAxisLength: float, minorAxisLength: float, startDegreeInRads: float, endDegreeInRads: float, tiltDegreeInRads: float, arcType: ArcType) -> bool: ...
    def Image(self, imageSource: ImageBGRA32, position: Point3d, u: Vector3d, v: Vector3d, transparencyMode: TransparencyMode) -> bool: ...
    def Mesh(self, rows: int, columns: int, points: Point3dCollection, edgeData: EdgeData, faceData: FaceData, vertexData: VertexData, bAutoGenerateNormals: bool) -> bool: ...
    def OwnerDraw(self, gdiDrawObject: GdiDrawObject, position: Point3d, u: Vector3d, v: Vector3d) -> bool: ...
    def PolyPolygon(self, numPolygonPositions: UInt32Collection, polygonPositions: Point3dCollection, numPolygonPoints: UInt32Collection, polygonPoints: Point3dCollection, outlineColors: EntityColorCollection, outlineTypes: LinetypeCollection, fillColors: EntityColorCollection, fillOpacities: TransparencyCollection) -> bool: ...
    def PolyPolyline(self, polylineCollection: PolylineCollection) -> bool: ...
    def Polygon(self, points: Point3dCollection) -> bool: ...
    def Polyline(self, value: Polyline, fromIndex: int, segments: int) -> bool: ...
    def Polypoint(self, points: Point3dCollection, normals: Vector3dCollection, subentityMarkers: IntPtrCollection) -> bool: ...
    def PopClipBoundary(self, ) -> None: ...
    def PopModelTransform(self, ) -> bool: ...
    def PushClipBoundary(self, boundary: ClipBoundary) -> bool: ...
    def PushModelTransform(self, matrix: Matrix3d) -> bool: ...
    def PushOrientationTransform(self, behavior: OrientationBehavior) -> Matrix3d: ...
    def PushPositionTransform(self, behavior: PositionBehavior, offset: Point2d) -> Matrix3d: ...
    def PushScaleTransform(self, behavior: ScaleBehavior, extents: Point2d) -> Matrix3d: ...
    def Ray(self, point1: Point3d, point2: Point3d) -> bool: ...
    def RowOfDots(self, count: int, start: Point3d, step: Vector3d) -> bool: ...
    def Shell(self, points: Point3dCollection, faces: IntegerCollection, edgeData: EdgeData, faceData: FaceData, vertexData: VertexData, bAutoGenerateNormals: bool) -> bool: ...
    def Text(self, position: Point3d, normal: Vector3d, direction: Vector3d, height: float, width: float, oblique: float, message: str) -> bool: ...
    def WorldLine(self, startPoint: Point3d, endPoint: Point3d) -> bool: ...
    def Xline(self, point1: Point3d, point2: Point3d) -> bool: ...

class GlobalIlluminationMode:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.GlobalIlluminationMode"""
    def __init__(self, *args) -> None: ...
    ...

class Glyph(Drawable):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Glyph"""
    def __init__(self, *args) -> None: ...
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetLocation(self, point: Point3d) -> None: ...

class GradientBackgroundTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.GradientBackgroundTraits"""
    def __init__(self, *args) -> None: ...
    Rotation: float
    Height: float
    Horizon: float
    ColorBottom: EntityColor
    ColorMiddle: EntityColor
    ColorTop: EntityColor
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GradientFill(Fill):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.GradientFill"""
    def __init__(self, *args) -> None: ...
    Type: GradientType
    GradientColors: list
    IsAdjustAspect: bool
    GradientShift: float
    GradientAngle: float
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GradientType:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.GradientType"""
    def __init__(self, *args) -> None: ...
    ...

class GroundPlaneBackgroundTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.GroundPlaneBackgroundTraits"""
    def __init__(self, *args) -> None: ...
    ColorGroundPlaneFar: EntityColor
    ColorGroundPlaneNear: EntityColor
    ColorUndergroundAzimuth: EntityColor
    ColorUndergroundHorizon: EntityColor
    ColorSkyHorizon: EntityColor
    ColorSkyZenith: EntityColor
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class HatchPattern(Fill):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.HatchPattern"""
    def __init__(self, *args) -> None: ...
    PatternLines: list
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class HatchPatternDefinition(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.HatchPatternDefinition"""
    def __init__(self, *args) -> None: ...
    DashList: DoubleCollection
    OffsetY: float
    OffsetX: float
    BaseY: float
    BaseX: float
    Angle: float
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class HighlightStyle:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.HighlightStyle"""
    def __init__(self, *args) -> None: ...
    ...

class IBLBackgroundTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.IBLBackgroundTraits"""
    def __init__(self, *args) -> None: ...
    SecondaryBackground: ObjectId
    DisplayImage: bool
    Rotation: float
    IBLImageName: str
    Enable: bool
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class IlluminationModel:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.IlluminationModel"""
    def __init__(self, *args) -> None: ...
    ...

class ImageBGRA32(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ImageBGRA32"""
    def __init__(self, *args) -> None: ...
    Image: IntPtr
    Height: int
    Width: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ImageBackgroundTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ImageBackgroundTraits"""
    def __init__(self, *args) -> None: ...
    YScale: float
    XScale: float
    YOffset: float
    XOffset: float
    UseTiling: bool
    MaintainAspectRatio: bool
    FitToScreen: bool
    ImageFilename: str
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ImageFileTexture(ImageTexture):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ImageFileTexture"""
    def __init__(self, *args) -> None: ...
    SourceFileName: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> object: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class ImageOrg:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ImageOrg"""
    def __init__(self, *args) -> None: ...
    ...

class ImageSource:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ImageSource"""
    def __init__(self, *args) -> None: ...
    ...

class ImageTexture(MaterialTexture):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ImageTexture"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LightAttenuation(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.LightAttenuation"""
    def __init__(self, *args) -> None: ...
    EndLimit: float
    StartLimit: float
    UseLimits: bool
    AttenuationType: AttenuationType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def SetLimits(self, startLimit: float, endLimit: float) -> None: ...

class LightTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.LightTraits"""
    def __init__(self, *args) -> None: ...
    On: bool
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Linetype:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Linetype"""
    def __init__(self, *args) -> None: ...
    ...

class LinetypeCollection(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.LinetypeCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: Linetype
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, value: Linetype) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: Linetype) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: Linetype) -> int: ...
    def Insert(self, index: int, value: Linetype) -> None: ...
    def Remove(self, value: Linetype) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class LuminanceMode:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.LuminanceMode"""
    def __init__(self, *args) -> None: ...
    ...

class MapChannel:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MapChannel"""
    def __init__(self, *args) -> None: ...
    ...

class MapFilter:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MapFilter"""
    def __init__(self, *args) -> None: ...
    ...

class Mapper(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Mapper"""
    def __init__(self, *args) -> None: ...
    VTiling: Tiling
    UTiling: Tiling
    Transform: Matrix3d
    AutoTransform: AutoTransform
    Projection: Projection
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Equals(self, other: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class MarbleTexture(ProceduralTexture):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MarbleTexture"""
    def __init__(self, *args) -> None: ...
    VeinWidth: float
    VeinSpacing: float
    VeinColor: MaterialColor
    StoneColor: MaterialColor
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> MarbleTexture: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def Set(self, value: MarbleTexture) -> None: ...

class MaterialColor(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MaterialColor"""
    def __init__(self, *args) -> None: ...
    Color: EntityColor
    Factor: float
    Method: Method
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Equals(self, other: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class MaterialDiffuseComponent:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MaterialDiffuseComponent"""
    def __init__(self, *args) -> None: ...
    Map: MaterialMap
    Color: MaterialColor
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class MaterialMap(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MaterialMap"""
    def __init__(self, *args) -> None: ...
    SourceFileName: str
    Mapper: Mapper
    Filter: MapFilter
    BlendFactor: float
    Texture: MaterialTexture
    Source: Source
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Equals(self, other: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class MaterialNormalMapComponent:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MaterialNormalMapComponent"""
    def __init__(self, *args) -> None: ...
    Strength: float
    Method: NormalMapMethod
    Map: MaterialMap
    def Equals(self, other: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class MaterialOpacityComponent:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MaterialOpacityComponent"""
    def __init__(self, *args) -> None: ...
    Percentage: float
    Map: MaterialMap
    def Equals(self, other: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class MaterialRefractionComponent:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MaterialRefractionComponent"""
    def __init__(self, *args) -> None: ...
    Index: float
    Map: MaterialMap
    def Equals(self, other: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class MaterialSpecularComponent:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MaterialSpecularComponent"""
    def __init__(self, *args) -> None: ...
    Gloss: float
    Map: MaterialMap
    Color: MaterialColor
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class MaterialTexture(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MaterialTexture"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class MaterialTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MaterialTraits"""
    def __init__(self, *args) -> None: ...
    FinalGather: FinalGatherMode
    GlobalIllumination: GlobalIlluminationMode
    NormalMap: MaterialNormalMapComponent
    Luminance: float
    LuminanceMode: LuminanceMode
    TwoSided: bool
    TransmittanceScale: float
    ReflectanceScale: float
    IndirectBumpScale: float
    ColorBleedScale: float
    Opacity: MaterialOpacityComponent
    Refraction: MaterialRefractionComponent
    Specular: MaterialSpecularComponent
    Diffuse: MaterialDiffuseComponent
    Mode: Mode
    ChannelFlags: ChannelFlags
    IlluminationModel: IlluminationModel
    Reflectivity: float
    SelfIllumination: float
    Translucence: float
    Bump: MaterialMap
    Reflection: MaterialMap
    Ambient: MaterialColor
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Method:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Method"""
    def __init__(self, *args) -> None: ...
    ...

class Mode:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Mode"""
    def __init__(self, *args) -> None: ...
    ...

class NonEntityTraits(DrawableTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.NonEntityTraits"""
    def __init__(self, *args) -> None: ...
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddLight(self, lightId: ObjectId) -> None: ...
    def GetHighlightProperty(self, propertyType: HighlightProperty) -> object: ...
    def SetHighlightProperty(self, propertyType: HighlightProperty, value: object) -> None: ...
    def SetSelectionMarker(self, markerId: IntPtr) -> None: ...
    def SetupForEntity(self, entity: Entity) -> None: ...

class NormalMapMethod:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.NormalMapMethod"""
    def __init__(self, *args) -> None: ...
    ...

class OrientationBehavior:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.OrientationBehavior"""
    def __init__(self, *args) -> None: ...
    ...

class OrientationType:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.OrientationType"""
    def __init__(self, *args) -> None: ...
    ...

class PhotographicExposureParameters(ToneOperatorParameters):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.PhotographicExposureParameters"""
    def __init__(self, *args) -> None: ...
    WhiteColor: Color
    WhitePoint: float
    Exposure: float
    ExteriorDaylight: ExteriorDaylightMode
    MidTones: float
    Contrast: float
    Brightness: float
    ProcessBackground: bool
    ColorDifferentiation: bool
    ChromaticAdaptation: bool
    IsActive: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CopyFrom(self, source: RXObject) -> None: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class PixelBGRA32:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.PixelBGRA32"""
    def __init__(self, *args) -> None: ...
    Alpha: int
    Blue: int
    Green: int
    Red: int
    def init(self, ) -> None: ...

class PointLightTraits(StandardLightTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.PointLightTraits"""
    def __init__(self, *args) -> None: ...
    HasTarget: bool
    TargetLocation: Point3d
    LampColor: ColorRGB
    PhysicalIntensity: float
    Attenuation: LightAttenuation
    Position: Point3d
    Shadow: ShadowParameters
    LightColor: Color
    Intensity: float
    On: bool
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Polyline(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Polyline"""
    def __init__(self, *args) -> None: ...
    BaseSubEntMarker: IntPtr
    Normal: Vector3d
    Points: Point3dCollection
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PolylineCollection(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.PolylineCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: Polyline
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, value: Polyline) -> int: ...
    def Clear(self, ) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class PositionBehavior:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.PositionBehavior"""
    def __init__(self, *args) -> None: ...
    ...

class ProceduralTexture(MaterialTexture):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ProceduralTexture"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ProceduralTextureType:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ProceduralTextureType"""
    def __init__(self, *args) -> None: ...
    ...

class Projection:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Projection"""
    def __init__(self, *args) -> None: ...
    ...

class RapidRTFilterType:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.RapidRTFilterType"""
    def __init__(self, *args) -> None: ...
    ...

class RapidRTLightingMode:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.RapidRTLightingMode"""
    def __init__(self, *args) -> None: ...
    ...

class RapidRTQuitCondition:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.RapidRTQuitCondition"""
    def __init__(self, *args) -> None: ...
    ...

class RapidRTRenderSettingsTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.RapidRTRenderSettingsTraits"""
    def __init__(self, *args) -> None: ...
    FilterHeight: float
    FilterWidth: float
    FilterType: RapidRTFilterType
    LightingMode: RapidRTLightingMode
    RenderLevel: int
    RenderTime: int
    QuitCondition: RapidRTQuitCondition
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class RegenType:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.RegenType"""
    def __init__(self, *args) -> None: ...
    ...

class RenderEnvironmentTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.RenderEnvironmentTraits"""
    def __init__(self, *args) -> None: ...
    EnvironmentMap: MaterialTexture
    FarPercentage: float
    NearPercentage: float
    FarDistance: float
    NearDistance: float
    FogColor: EntityColor
    IsBackground: bool
    Enable: bool
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class RenderSettingsTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.RenderSettingsTraits"""
    def __init__(self, *args) -> None: ...
    ModelScaleFactor: float
    DiagnosticBackgroundEnabled: bool
    ShadowsEnabled: bool
    BackFacesEnabled: bool
    TextureSampling: bool
    MaterialEnabled: bool
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ScaleBehavior:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ScaleBehavior"""
    def __init__(self, *args) -> None: ...
    ...

class SelectionFlags:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.SelectionFlags"""
    def __init__(self, *args) -> None: ...
    ...

class ShadowFlags:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ShadowFlags"""
    def __init__(self, *args) -> None: ...
    ...

class ShadowParameters(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ShadowParameters"""
    def __init__(self, *args) -> None: ...
    ExtendedLightRadius: float
    ExtendedLightWidth: float
    ExtendedLightLength: float
    ExtendedLightShape: ExtendedLightShape
    ShapeVisibility: bool
    ShadowSamples: int
    ShadowMapSoftness: int
    ShadowMapSize: int
    ShadowType: ShadowType
    ShadowsOn: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class ShadowType:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ShadowType"""
    def __init__(self, *args) -> None: ...
    ...

class SkyBackgroundTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.SkyBackgroundTraits"""
    def __init__(self, *args) -> None: ...
    SkyParameters: SkyParameters
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SkyParameters(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.SkyParameters"""
    def __init__(self, *args) -> None: ...
    Saturation: float
    RedBlueShift: float
    SunDirection: Vector3d
    NightColor: Color
    GroundColor: Color
    SolarDiskSamples: int
    DiskIntensity: float
    GlowIntensity: float
    DiskScale: float
    VisibilityDistance: float
    HorizonBlur: float
    HorizonHeight: float
    Haze: float
    IntensityFactor: float
    AerialPerspective: bool
    Illumination: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class SolidBackgroundTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.SolidBackgroundTraits"""
    def __init__(self, *args) -> None: ...
    ColorSolid: EntityColor
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Source:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Source"""
    def __init__(self, *args) -> None: ...
    ...

class SpotLightTraits(StandardLightTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.SpotLightTraits"""
    def __init__(self, *args) -> None: ...
    LampColor: ColorRGB
    PhysicalIntensity: float
    Attenuation: LightAttenuation
    Falloff: float
    Hotspot: float
    TargetLocation: Point3d
    Position: Point3d
    Shadow: ShadowParameters
    LightColor: Color
    Intensity: float
    On: bool
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetHotspotAndFalloff(self, hotspot: float, falloff: float) -> bool: ...

class StandardLightTraits(LightTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.StandardLightTraits"""
    def __init__(self, *args) -> None: ...
    Shadow: ShadowParameters
    LightColor: Color
    Intensity: float
    On: bool
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SubEntityTraits(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.SubEntityTraits"""
    def __init__(self, *args) -> None: ...
    Fill: Fill
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetSelectionMarker(self, markerId: IntPtr) -> None: ...

class TextStyle(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.TextStyle"""
    def __init__(self, *args) -> None: ...
    PreLoaded: bool
    Font: FontDescriptor
    StyleName: str
    BigFontFileName: str
    FileName: str
    Strikethrough: bool
    Overlined: bool
    Underlined: bool
    Vertical: bool
    UpsideDown: bool
    Backward: bool
    TrackingPercent: float
    ObliquingAngle: float
    XScale: float
    TextSize: float
    LoadStyleRec: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(unmanagedPointer: IntPtr, autoDelete: bool) -> TextStyle: ...
    def ExtentsBox(self, value1: str, includeSpaces: bool, raw: bool, context: WorldDraw) -> Extents2d: ...
    def FromTextStyleTableRecord(self, AcDbStyleName: str) -> None: ...
    def SetTrackKerning(self, trackPercent: float) -> None: ...
    def ToTextStyleTableRecord(self, AcDbStyleName: str) -> ObjectId: ...

class Tiling:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Tiling"""
    def __init__(self, *args) -> None: ...
    ...

class ToneOperatorParameters(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ToneOperatorParameters"""
    def __init__(self, *args) -> None: ...
    ExteriorDaylight: ExteriorDaylightMode
    WhiteColor: Color
    MidTones: float
    Contrast: float
    Brightness: float
    ProcessBackground: bool
    ColorDifferentiation: bool
    ChromaticAdaptation: bool
    IsActive: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CopyFrom(self, source: RXObject) -> None: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class TransientDrawingMode:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.TransientDrawingMode"""
    def __init__(self, *args) -> None: ...
    ...

class TransientManager(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.TransientManager"""
    def __init__(self, *args) -> None: ...
    CurrentTransientManager: TransientManager
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddChildTransient(self, added: Drawable, parent: Drawable) -> bool: ...
    def AddTransient(self, added: Drawable, mode: TransientDrawingMode, subDrawingMode: int, viewportNumbers: IntegerCollection) -> bool: ...
    def EraseChildTransient(self, erased: Drawable, parent: Drawable) -> bool: ...
    def EraseTransient(self, erased: Drawable, viewportNumbers: IntegerCollection) -> bool: ...
    def EraseTransients(self, mode: TransientDrawingMode, subDrawingMode: int, viewportNumbers: IntegerCollection) -> bool: ...
    def GetFreeSubDrawingMode(self, mode: TransientDrawingMode, viewportNumbers: IntegerCollection, subDrawingMode: int) -> int: ...
    def UpdateChildTransient(self, updated: Drawable, parent: Drawable) -> None: ...
    def UpdateTransient(self, updated: Drawable, viewportNumbers: IntegerCollection) -> None: ...

class TransparencyMode:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.TransparencyMode"""
    def __init__(self, *args) -> None: ...
    ...

class VSDisplayShadowType:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VSDisplayShadowType"""
    def __init__(self, *args) -> None: ...
    ...

class VSDisplayStyles:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VSDisplayStyles"""
    def __init__(self, *args) -> None: ...
    ...

class VSEdgeJitterAmount:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VSEdgeJitterAmount"""
    def __init__(self, *args) -> None: ...
    ...

class VSEdgeLinePattern:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VSEdgeLinePattern"""
    def __init__(self, *args) -> None: ...
    ...

class VSEdgeModel:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VSEdgeModel"""
    def __init__(self, *args) -> None: ...
    ...

class VSEdgeModifiers:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VSEdgeModifiers"""
    def __init__(self, *args) -> None: ...
    ...

class VSEdgeStyles:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VSEdgeStyles"""
    def __init__(self, *args) -> None: ...
    ...

class VSFaceColorMode:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VSFaceColorMode"""
    def __init__(self, *args) -> None: ...
    ...

class VSFaceLightingModel:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VSFaceLightingModel"""
    def __init__(self, *args) -> None: ...
    ...

class VSFaceLightingQuality:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VSFaceLightingQuality"""
    def __init__(self, *args) -> None: ...
    ...

class VSFaceModifiers:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VSFaceModifiers"""
    def __init__(self, *args) -> None: ...
    ...

class VariantType:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VariantType"""
    def __init__(self, *args) -> None: ...
    ...

class VertexData:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VertexData"""
    def __init__(self, *args) -> None: ...
    OrientationFlag: OrientationType
    def GetNormalVectors(self, ) -> list: ...
    def GetTrueColors(self, ) -> list: ...
    def SetNormalVectors(self, normal: list) -> None: ...
    def SetTrueColors(self, colors: list) -> None: ...
    def get_MappingCoords(self, mapChannel: MapChannel) -> list: ...
    def set_MappingCoords(self, mapChannel: MapChannel, coords: list) -> None: ...

class Viewport(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Viewport"""
    def __init__(self, *args) -> None: ...
    ViewDirection: Vector3d
    LinetypeGenerationCriteria: float
    LinetypeScaleMultiplier: float
    FrontAndBackClipping: FrontAndBackClipping
    DeviceContextViewportCorners: Extents2d
    AcadWindowId: int
    ViewportId: IntPtr
    CameraUpVector: Vector3d
    CameraTarget: Point3d
    CameraLocation: Point3d
    IsPerspective: bool
    EyeToWorldTransform: Matrix3d
    WorldToEyeTransform: Matrix3d
    EyeToModelTransform: Matrix3d
    ModelToEyeTransform: Matrix3d
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DoInversePerspective(self, value: Point3d) -> Point3d: ...
    def DoPerspective(self, value: Point3d) -> Point3d: ...
    def GetNumPixelsInUnitSquare(self, givenWorldPoint: Point3d) -> Point2d: ...
    def LayerVisible(self, idLayer: ObjectId) -> bool: ...

class ViewportDraw(CommonDraw):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ViewportDraw"""
    def __init__(self, *args) -> None: ...
    ViewportObjectId: ObjectId
    SequenceNumber: int
    Geometry: ViewportGeometry
    Viewport: Viewport
    NumberOfIsolines: int
    IsDragging: bool
    Context: Context
    RawGeometry: Geometry
    SubEntityTraits: SubEntityTraits
    RegenAbort: bool
    RegenType: RegenType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def IsValidId(self, id: IntPtr) -> bool: ...

class ViewportGeometry(Geometry):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ViewportGeometry"""
    def __init__(self, *args) -> None: ...
    WorldToModelTransform: Matrix3d
    ModelToWorldTransform: Matrix3d
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DeviceContextPolygon(self, points: Point3dCollection) -> bool: ...
    def DeviceContextPolyline(self, points: Point3dCollection) -> bool: ...
    def DeviceContextRasterImage(self, origin: Point3d, u: Vector3d, v: Vector3d, pixel: Matrix2d, entityId: ObjectId, imageOrg: ImageOrg, imageWidth: int, imageHeight: int, imageColorDepth: int, transparency: bool, source: ImageSource, unRotated: Vector3d, originalImage: ImageOrg, unRotatedPixel: Matrix2d, unRotatedImageWidth: int, unRotatedImageHeight: int) -> bool: ...
    def PolygonEye(self, points: Point3dCollection) -> bool: ...
    def PolylineEye(self, points: Point3dCollection) -> bool: ...

class ViewportTraits(DrawableTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ViewportTraits"""
    def __init__(self, *args) -> None: ...
    ToneOperatorParameters: ToneOperatorParameters
    RenderSettings: ObjectId
    RenderEnvironment: ObjectId
    Contrast: float
    Brightness: float
    AmbientLightColor: Color
    DefaultLightingType: DefaultLightingType
    DefaultLightingOn: bool
    Background: ObjectId
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class VisualStyle(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VisualStyle"""
    def __init__(self, *args) -> None: ...
    Type: VisualStyleType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetPropertyType(self, prop: VisualStyleProperty) -> VariantType: ...
    def GetTrait(self, prop: VisualStyleProperty) -> object: ...
    def GetTraitFlag(self, prop: VisualStyleProperty, flagVal: int) -> bool: ...
    def Operation(self, prop: VisualStyleProperty) -> VisualStyleOperation: ...
    def SetTrait(self, prop: VisualStyleProperty, red: float, green: float, blue: float, op: VisualStyleOperation) -> None: ...
    def SetTraitFlag(self, prop: VisualStyleProperty, flagVal: int, bEnable: bool) -> None: ...

class VisualStyleOperation:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VisualStyleOperation"""
    def __init__(self, *args) -> None: ...
    ...

class VisualStyleProperty:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty"""
    def __init__(self, *args) -> None: ...
    ...

class VisualStyleTraits(DrawableTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VisualStyleTraits"""
    def __init__(self, *args) -> None: ...
    AcGiVisualStyle: VisualStyle
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class VisualStyleType:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VisualStyleType"""
    def __init__(self, *args) -> None: ...
    ...

class WebFileType:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.WebFileType"""
    def __init__(self, *args) -> None: ...
    ...

class WebLightTraits(PointLightTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.WebLightTraits"""
    def __init__(self, *args) -> None: ...
    WebHorzAng90to270: bool
    WebSymmetry: WebSymmetry
    WebFileType: WebFileType
    WebFlux: float
    WebRotation: Vector3d
    WebFile: str
    HasTarget: bool
    TargetLocation: Point3d
    LampColor: ColorRGB
    PhysicalIntensity: float
    Attenuation: LightAttenuation
    Position: Point3d
    Shadow: ShadowParameters
    LightColor: Color
    Intensity: float
    On: bool
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class WebSymmetry:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.WebSymmetry"""
    def __init__(self, *args) -> None: ...
    ...

class WoodTexture(ProceduralTexture):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.WoodTexture"""
    def __init__(self, *args) -> None: ...
    GrainThickness: float
    AxialNoise: float
    RadialNoise: float
    Color2: MaterialColor
    Color1: MaterialColor
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> WoodTexture: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def Set(self, value: WoodTexture) -> None: ...

class WorldDraw(CommonDraw):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.WorldDraw"""
    def __init__(self, *args) -> None: ...
    Geometry: WorldGeometry
    NumberOfIsolines: int
    IsDragging: bool
    Context: Context
    RawGeometry: Geometry
    SubEntityTraits: SubEntityTraits
    RegenAbort: bool
    RegenType: RegenType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class WorldGeometry(Geometry):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.WorldGeometry"""
    def __init__(self, *args) -> None: ...
    WorldToModelTransform: Matrix3d
    ModelToWorldTransform: Matrix3d
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetExtents(self, extents: Extents3d) -> None: ...
    def StartAttributesSegment(self, ) -> None: ...
