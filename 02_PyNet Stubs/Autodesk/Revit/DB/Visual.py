# Auto-generated — Revit 2027 — Autodesk.Revit.DB.Visual

class AdvancedGlazing:
    """.NET: Autodesk.Revit.DB.Visual.AdvancedGlazing"""
    def __init__(self, *args) -> None: ...
    SurfaceNdfType: str
    SurfaceRoughness: str
    SurfaceRotation: str
    SurfaceCutout: str
    SurfaceNormal: str
    SurfaceAnisotropy: str
    SurfaceAlbedo: str
    GlazingBackfaceCulling: str
    GlazingF0: str
    GlazingTransmissionRoughness: str
    GlazingTransmissionColor: str

class AdvancedLayered:
    """.NET: Autodesk.Revit.DB.Visual.AdvancedLayered"""
    def __init__(self, *args) -> None: ...
    SurfaceNdfType: str
    SurfaceRoughness: str
    SurfaceRotation: str
    SurfaceCutout: str
    SurfaceNormal: str
    SurfaceAnisotropy: str
    SurfaceAlbedo: str
    LayeredNdfType: str
    LayeredRoughness: str
    LayeredRotation: str
    LayeredNormal: str
    LayeredAnisotropy: str
    LayeredDiffuse: str
    LayeredFraction: str
    LayeredF0: str
    LayeredBottomF0: str

class AdvancedMetal:
    """.NET: Autodesk.Revit.DB.Visual.AdvancedMetal"""
    def __init__(self, *args) -> None: ...
    SurfaceNdfType: str
    SurfaceRoughness: str
    SurfaceRotation: str
    SurfaceCutout: str
    SurfaceNormal: str
    SurfaceAnisotropy: str
    SurfaceAlbedo: str
    MetalF0: str

class AdvancedOpaque:
    """.NET: Autodesk.Revit.DB.Visual.AdvancedOpaque"""
    def __init__(self, *args) -> None: ...
    SurfaceNdfType: str
    SurfaceRoughness: str
    SurfaceRotation: str
    SurfaceCutout: str
    SurfaceNormal: str
    SurfaceAnisotropy: str
    SurfaceAlbedo: str
    OpaqueLuminanceModifier: str
    OpaqueLuminance: str
    OpaqueEmission: str
    OpaqueMfpModifier: str
    OpaqueMfp: str
    OpaqueTranslucency: str
    OpaqueF0: str
    OpaqueAlbedo: str

class AdvancedTransparent:
    """.NET: Autodesk.Revit.DB.Visual.AdvancedTransparent"""
    def __init__(self, *args) -> None: ...
    SurfaceNdfType: str
    SurfaceRoughness: str
    SurfaceRotation: str
    SurfaceCutout: str
    SurfaceNormal: str
    SurfaceAnisotropy: str
    SurfaceAlbedo: str
    TransparentIor: str
    TransparentDistance: str
    TransparentColor: str

class AdvancedWood:
    """.NET: Autodesk.Revit.DB.Visual.AdvancedWood"""
    def __init__(self, *args) -> None: ...
    WoodCurlyDistortionMap: str
    WoodCurlyDistortionScale: str
    WoodCurlyDistortionEnable: str
    WoodLatecolorPerlinProf: str
    WoodLatecolorPerlinEnable: str
    WoodEarlycolorPerlinProf: str
    WoodEarlycolorPerlinEnable: str
    WoodSecondaryPerlinScaleZ: str
    WoodSecondaryPerlinProf: str
    WoodSecondaryPerlinEnable: str
    WoodDiffusePerlinScaleZ: str
    WoodDiffusePerlinProf: str
    WoodDiffusePerlinEnable: str
    WoodGrowthPerlinProf: str
    WoodGrowthPerlinEnable: str
    WoodFiberCosineProf: str
    WoodFiberCosineEnable: str
    WoodFiberPerlinScaleZ: str
    WoodFiberPerlinProf: str
    WoodFiberPerlinEnable: str
    WoodGrooveRoughness: str
    WoodUseGrooveRoughness: str
    WoodLatewoodBumpDepth: str
    WoodUseLatewoodBump: str
    WoodDiffuseLobeWeight: str
    WoodFiberRoughness: str
    WoodRayEllipseZ2x: str
    WoodRayEllipseRadiusX: str
    WoodRayNumSlices: str
    WoodRaySegLengthZ: str
    WoodRayColorPower: str
    WoodUseRays: str
    WoodPoreDepth: str
    WoodPoreColorPower: str
    WoodPoreRadius: str
    WoodPoreCellDim: str
    WoodPoreType: str
    WoodUsePores: str
    WoodManualLateColor: str
    WoodUseManualLateColor: str
    WoodSecondaryColorPower: str
    WoodLateColorPower: str
    WoodEarlyColor: str
    WoodLatewoodSharpness: str
    WoodEarlywoodSharpness: str
    WoodLatewoodRatio: str
    WoodRingThickness: str

class AppearanceAssetEditScope:
    """.NET: Autodesk.Revit.DB.Visual.AppearanceAssetEditScope"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsActive: bool
    def Cancel(self, ) -> None: ...
    def Commit(self, updateOpenViews: bool) -> None: ...
    def Dispose(self, ) -> None: ...
    def Start(self, assetElementId: ElementId) -> Asset: ...

class Asset(AssetProperties):
    """.NET: Autodesk.Revit.DB.Visual.Asset"""
    def __init__(self, *args) -> None: ...
    AssetType: AssetType
    LibraryName: str
    Title: str
    Size: int
    Item: AssetProperty
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str

class AssetProperties(AssetProperty):
    """.NET: Autodesk.Revit.DB.Visual.AssetProperties"""
    def __init__(self, *args) -> None: ...
    Size: int
    Item: AssetProperty
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str
    def FindByName(self, name: str) -> AssetProperty: ...
    def Get(self, index: int) -> AssetProperty: ...
    def IsValidIndex(self, index: int) -> bool: ...

class AssetProperty:
    """.NET: Autodesk.Revit.DB.Visual.AssetProperty"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str
    def AddConnectedAsset(self, schema: str) -> None: ...
    def AddCopyAsConnectedAsset(self, pRenderingAsset: Asset) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetAllConnectedProperties(self, ) -> IList: ...
    def GetConnectedProperty(self, index: int) -> AssetProperty: ...
    def GetSingleConnectedAsset(self, ) -> Asset: ...
    @staticmethod
    def GetTypeName(type: AssetPropertyType) -> str: ...
    def IsEditable(self, ) -> bool: ...
    def IsValidSchemaIdentifier(self, schemaID: str) -> bool: ...
    def RemoveConnectedAsset(self, ) -> None: ...

class AssetPropertyBoolean(AssetProperty):
    """.NET: Autodesk.Revit.DB.Visual.AssetPropertyBoolean"""
    def __init__(self, *args) -> None: ...
    Value: bool
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str

class AssetPropertyDistance(AssetProperty):
    """.NET: Autodesk.Revit.DB.Visual.AssetPropertyDistance"""
    def __init__(self, *args) -> None: ...
    Value: float
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str
    def GetUnitTypeId(self, ) -> ForgeTypeId: ...
    def IsValidValue(self, value: float) -> bool: ...

class AssetPropertyDouble(AssetProperty):
    """.NET: Autodesk.Revit.DB.Visual.AssetPropertyDouble"""
    def __init__(self, *args) -> None: ...
    Value: float
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str
    def IsValidValue(self, value: float) -> bool: ...

class AssetPropertyDoubleArray2d(AssetProperty):
    """.NET: Autodesk.Revit.DB.Visual.AssetPropertyDoubleArray2d"""
    def __init__(self, *args) -> None: ...
    Value: DoubleArray
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str

class AssetPropertyDoubleArray3d(AssetProperty):
    """.NET: Autodesk.Revit.DB.Visual.AssetPropertyDoubleArray3d"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str
    def GetValueAsDoubles(self, ) -> IList: ...
    def GetValueAsXYZ(self, ) -> XYZ: ...
    def IsValidValue(self, xyz: XYZ) -> bool: ...
    def SetValueAsXYZ(self, xyz: XYZ) -> None: ...

class AssetPropertyDoubleArray4d(AssetProperty):
    """.NET: Autodesk.Revit.DB.Visual.AssetPropertyDoubleArray4d"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str
    def GetValueAsColor(self, ) -> Color: ...
    def GetValueAsDoubles(self, ) -> IList: ...
    def IsValidValue(self, color: Color) -> bool: ...
    def SetValueAsColor(self, color: Color) -> None: ...
    def SetValueAsDoubles(self, value: IList) -> None: ...

class AssetPropertyDoubleMatrix44(AssetProperty):
    """.NET: Autodesk.Revit.DB.Visual.AssetPropertyDoubleMatrix44"""
    def __init__(self, *args) -> None: ...
    Value: DoubleArray
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str

class AssetPropertyEnum(AssetProperty):
    """.NET: Autodesk.Revit.DB.Visual.AssetPropertyEnum"""
    def __init__(self, *args) -> None: ...
    Value: int
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str
    def IsValidValue(self, value: int) -> bool: ...

class AssetPropertyFloat(AssetProperty):
    """.NET: Autodesk.Revit.DB.Visual.AssetPropertyFloat"""
    def __init__(self, *args) -> None: ...
    Value: float
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str
    def IsValidValue(self, value: float) -> bool: ...

class AssetPropertyFloatArray(AssetProperty):
    """.NET: Autodesk.Revit.DB.Visual.AssetPropertyFloatArray"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str
    def GetValue(self, ) -> IList: ...

class AssetPropertyInt64(AssetProperty):
    """.NET: Autodesk.Revit.DB.Visual.AssetPropertyInt64"""
    def __init__(self, *args) -> None: ...
    Value: int
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str

class AssetPropertyInteger(AssetProperty):
    """.NET: Autodesk.Revit.DB.Visual.AssetPropertyInteger"""
    def __init__(self, *args) -> None: ...
    Value: int
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str
    def IsValidValue(self, value: int) -> bool: ...

class AssetPropertyList(AssetProperty):
    """.NET: Autodesk.Revit.DB.Visual.AssetPropertyList"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str
    def AddNewAssetAsColor(self, value: Color) -> None: ...
    def AddNewAssetPropertyDouble(self, value: float) -> None: ...
    def AddNewAssetPropertyInteger(self, value: int) -> None: ...
    def GetValue(self, ) -> IList: ...
    def InsertNewAssetAsColor(self, value: Color, index: int) -> None: ...
    def InsertNewAssetPropertyDouble(self, value: float, index: int) -> None: ...
    def InsertNewAssetPropertyInteger(self, value: int, index: int) -> None: ...
    def IsValidValue(self, value: IList) -> bool: ...
    def RemoveAssetProperty(self, index: int) -> None: ...
    def SetValue(self, value: IList) -> None: ...

class AssetPropertyReference(AssetProperty):
    """.NET: Autodesk.Revit.DB.Visual.AssetPropertyReference"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str

class AssetPropertyString(AssetProperty):
    """.NET: Autodesk.Revit.DB.Visual.AssetPropertyString"""
    def __init__(self, *args) -> None: ...
    Value: str
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str
    def IsValidValue(self, value: str) -> bool: ...

class AssetPropertyTime(AssetProperty):
    """.NET: Autodesk.Revit.DB.Visual.AssetPropertyTime"""
    def __init__(self, *args) -> None: ...
    Value: DateTime
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str

class AssetPropertyType:
    """.NET: Autodesk.Revit.DB.Visual.AssetPropertyType"""
    def __init__(self, *args) -> None: ...
    ...

class AssetPropertyUInt64(AssetProperty):
    """.NET: Autodesk.Revit.DB.Visual.AssetPropertyUInt64"""
    def __init__(self, *args) -> None: ...
    Value: int
    IsValidObject: bool
    IsReadOnly: bool
    NumberOfConnectedProperties: int
    Type: AssetPropertyType
    Name: str

class AssetSet(APIObject):
    """.NET: Autodesk.Revit.DB.Visual.AssetSet"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Contains(self, item: Asset) -> bool: ...
    def Erase(self, item: Asset) -> int: ...
    def ForwardIterator(self, ) -> AssetSetIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: Asset) -> bool: ...
    def ReverseIterator(self, ) -> AssetSetIterator: ...

class AssetSetIterator(APIObject):
    """.NET: Autodesk.Revit.DB.Visual.AssetSetIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class AssetType:
    """.NET: Autodesk.Revit.DB.Visual.AssetType"""
    def __init__(self, *args) -> None: ...
    ...

class BumpMap:
    """.NET: Autodesk.Revit.DB.Visual.BumpMap"""
    def __init__(self, *args) -> None: ...
    BumpmapType: str
    TextureVRepeat: str
    TextureURepeat: str
    BumpmapNormalScale: str
    BumpmapDepth: str
    TextureScaleLock: str
    TextureRealWorldScaleY: str
    TextureRealWorldScaleX: str
    TextureWAngle: str
    TextureOffsetLock: str
    TextureRealWorldOffsetY: str
    TextureRealWorldOffsetX: str
    TextureLinkTextureTransforms: str
    BumpmapBitmap: str

class BumpmapType:
    """.NET: Autodesk.Revit.DB.Visual.BumpmapType"""
    def __init__(self, *args) -> None: ...
    ...

class Ceramic:
    """.NET: Autodesk.Revit.DB.Visual.Ceramic"""
    def __init__(self, *args) -> None: ...
    CommonTintColor: str
    CommonTintToggle: str
    CeramicPatternAmount: str
    CeramicPatternMap: str
    CeramicPattern: str
    CeramicBumpAmount: str
    CeramicBumpMap: str
    CeramicBump: str
    CeramicApplication: str
    CeramicColorByObject: str
    CeramicColor: str
    CeramicType: str

class CeramicApplicationType:
    """.NET: Autodesk.Revit.DB.Visual.CeramicApplicationType"""
    def __init__(self, *args) -> None: ...
    ...

class CeramicBumpType:
    """.NET: Autodesk.Revit.DB.Visual.CeramicBumpType"""
    def __init__(self, *args) -> None: ...
    ...

class CeramicPatternType:
    """.NET: Autodesk.Revit.DB.Visual.CeramicPatternType"""
    def __init__(self, *args) -> None: ...
    ...

class CeramicType:
    """.NET: Autodesk.Revit.DB.Visual.CeramicType"""
    def __init__(self, *args) -> None: ...
    ...

class Checker:
    """.NET: Autodesk.Revit.DB.Visual.Checker"""
    def __init__(self, *args) -> None: ...
    TextureVRepeat: str
    TextureURepeat: str
    TextureScaleLock: str
    TextureRealWorldScaleY: str
    TextureRealWorldScaleX: str
    TextureWAngle: str
    TextureOffsetLock: str
    TextureRealWorldOffsetY: str
    TextureRealWorldOffsetX: str
    TextureLinkTextureTransforms: str
    CheckerSoften: str
    CheckerColor2: str
    CheckerColor1: str

class CommonSharedAssetType:
    """.NET: Autodesk.Revit.DB.Visual.CommonSharedAssetType"""
    def __init__(self, *args) -> None: ...
    ...

class Concrete:
    """.NET: Autodesk.Revit.DB.Visual.Concrete"""
    def __init__(self, *args) -> None: ...
    CommonTintColor: str
    CommonTintToggle: str
    ConcreteBmMap: str
    ConcreteBrightmode: str
    ConcreteBumpAmount: str
    ConcreteBumpMap: str
    ConcreteFinish: str
    ConcreteSealant: str
    ConcreteColor: str

class ConcreteBrightmodeType:
    """.NET: Autodesk.Revit.DB.Visual.ConcreteBrightmodeType"""
    def __init__(self, *args) -> None: ...
    ...

class ConcreteFinishType:
    """.NET: Autodesk.Revit.DB.Visual.ConcreteFinishType"""
    def __init__(self, *args) -> None: ...
    ...

class ConcreteSealantType:
    """.NET: Autodesk.Revit.DB.Visual.ConcreteSealantType"""
    def __init__(self, *args) -> None: ...
    ...

class Generic:
    """.NET: Autodesk.Revit.DB.Visual.Generic"""
    def __init__(self, *args) -> None: ...
    CommonTintColor: str
    CommonTintToggle: str
    GenericBumpAmount: str
    GenericBumpMap: str
    GenericSelfIllumColorTemperature: str
    GenericSelfIllumLuminance: str
    GenericSelfIllumFilterMap: str
    GenericCutoutOpacity: str
    GenericRefractionIndex: str
    GenericRefractionTranslucencyWeight: str
    GenericTransparencyImageFade: str
    GenericTransparency: str
    GenericReflectivityAt90deg: str
    GenericReflectivityAt0deg: str
    GenericIsMetal: str
    GenericGlossiness: str
    GenericDiffuseImageFade: str
    ColorByObject: str
    GenericDiffuse: str

class Glazing:
    """.NET: Autodesk.Revit.DB.Visual.Glazing"""
    def __init__(self, *args) -> None: ...
    CommonTintColor: str
    CommonTintToggle: str
    GlazingNoLevels: str
    GlazingReflectance: str
    GlazingColorByObject: str
    GlazingTransmittanceMap: str
    GlazingTransmittanceColor: str

class GlazingTransmittanceColorType:
    """.NET: Autodesk.Revit.DB.Visual.GlazingTransmittanceColorType"""
    def __init__(self, *args) -> None: ...
    ...

class Gradient:
    """.NET: Autodesk.Revit.DB.Visual.Gradient"""
    def __init__(self, *args) -> None: ...
    TextureVRepeat: str
    TextureURepeat: str
    TextureScaleLock: str
    TextureRealWorldScaleY: str
    TextureRealWorldScaleX: str
    TextureWAngle: str
    TextureOffsetLock: str
    TextureRealWorldOffsetY: str
    TextureRealWorldOffsetX: str
    TextureLinkTextureTransforms: str
    GradientType: str
    GradientPosition: str
    GradientNoiseSmooth: str
    GradientNoiseSize: str
    GradientNoisePhase: str
    GradientNoiseLow: str
    GradientNoiseLevels: str
    GradientNoiseHigh: str
    GradientNoiseAmount: str
    GradientNoise: str
    GradientInterpolation: str
    GradientColor: str

class GradientInterpolationType:
    """.NET: Autodesk.Revit.DB.Visual.GradientInterpolationType"""
    def __init__(self, *args) -> None: ...
    ...

class GradientNoiseType:
    """.NET: Autodesk.Revit.DB.Visual.GradientNoiseType"""
    def __init__(self, *args) -> None: ...
    ...

class GradientType:
    """.NET: Autodesk.Revit.DB.Visual.GradientType"""
    def __init__(self, *args) -> None: ...
    ...

class Hardwood:
    """.NET: Autodesk.Revit.DB.Visual.Hardwood"""
    def __init__(self, *args) -> None: ...
    CommonTintColor: str
    CommonTintToggle: str
    HardwoodImperfectionsAmount: str
    HardwoodImperfectionsShader: str
    HardwoodImperfections: str
    HardwoodApplication: str
    HardwoodFinish: str
    HardwoodTintColor: str
    HardwoodTintEnabled: str
    HardwoodColor: str

class HardwoodApplicationType:
    """.NET: Autodesk.Revit.DB.Visual.HardwoodApplicationType"""
    def __init__(self, *args) -> None: ...
    ...

class HardwoodFinishType:
    """.NET: Autodesk.Revit.DB.Visual.HardwoodFinishType"""
    def __init__(self, *args) -> None: ...
    ...

class HardwoodImperfectionsType:
    """.NET: Autodesk.Revit.DB.Visual.HardwoodImperfectionsType"""
    def __init__(self, *args) -> None: ...
    ...

class HardwoodTintEnabledType:
    """.NET: Autodesk.Revit.DB.Visual.HardwoodTintEnabledType"""
    def __init__(self, *args) -> None: ...
    ...

class LayeredNdfType:
    """.NET: Autodesk.Revit.DB.Visual.LayeredNdfType"""
    def __init__(self, *args) -> None: ...
    ...

class Marble:
    """.NET: Autodesk.Revit.DB.Visual.Marble"""
    def __init__(self, *args) -> None: ...
    TextureRealWorldOffsetZ: str
    TextureRealWorldOffsetY: str
    TextureRealWorldOffsetX: str
    TextureLinkTextureTransforms: str
    TextureAngle: str
    MarbleWidth: str
    MarbleSize: str
    MarbleColor2: str
    MarbleColor1: str

class MasonryCMU:
    """.NET: Autodesk.Revit.DB.Visual.MasonryCMU"""
    def __init__(self, *args) -> None: ...
    CommonTintColor: str
    CommonTintToggle: str
    MasonryCMUPatternHeight: str
    MasonryCMUPatternMap: str
    MasonryCMUPattern: str
    MasonryCMUApplication: str
    MasonryCMUColorByObject: str
    MasonryCMUColor: str
    MasonryCMUType: str

class MasonryCMUApplicationType:
    """.NET: Autodesk.Revit.DB.Visual.MasonryCMUApplicationType"""
    def __init__(self, *args) -> None: ...
    ...

class MasonryCMUPatternType:
    """.NET: Autodesk.Revit.DB.Visual.MasonryCMUPatternType"""
    def __init__(self, *args) -> None: ...
    ...

class MasonryCMUType:
    """.NET: Autodesk.Revit.DB.Visual.MasonryCMUType"""
    def __init__(self, *args) -> None: ...
    ...

class Metal:
    """.NET: Autodesk.Revit.DB.Visual.Metal"""
    def __init__(self, *args) -> None: ...
    CommonTintColor: str
    CommonTintToggle: str
    MetalPerforationsCenter: str
    MetalPerforationsSize: str
    MetalPerforationsShader: str
    MetalPerforations: str
    MetalPatternScale: str
    MetalPatternHeight: str
    MetalPatternShader: str
    MetalPattern: str
    MetalFinish: str
    MetalPatina: str
    MetalColor: str
    MetalType: str

class MetalFinishType:
    """.NET: Autodesk.Revit.DB.Visual.MetalFinishType"""
    def __init__(self, *args) -> None: ...
    ...

class MetalPatternType:
    """.NET: Autodesk.Revit.DB.Visual.MetalPatternType"""
    def __init__(self, *args) -> None: ...
    ...

class MetalPerforationsType:
    """.NET: Autodesk.Revit.DB.Visual.MetalPerforationsType"""
    def __init__(self, *args) -> None: ...
    ...

class MetalType:
    """.NET: Autodesk.Revit.DB.Visual.MetalType"""
    def __init__(self, *args) -> None: ...
    ...

class MetallicPaint:
    """.NET: Autodesk.Revit.DB.Visual.MetallicPaint"""
    def __init__(self, *args) -> None: ...
    CommonTintColor: str
    CommonTintToggle: str
    MetallicpaintFinishPeelamount: str
    MetallicpaintFinish: str
    MetallicpaintTopcoatFalloff: str
    MetallicpaintTopcoatGlossy: str
    MetallicpaintTopcoat: str
    MetallicpaintPearlIor: str
    MetallicpaintPearlColor: str
    MetallicpaintPearlColorByObject: str
    MetallicpaintPearlAmount: str
    MetallicpaintPearl: str
    MetallicpaintFlecksSize: str
    MetallicpaintFlecksColor: str
    MetallicpaintFlecksColorByObject: str
    MetallicpaintFlecks: str
    MetallicpaintBaseHighlightspread: str
    MetallicpaintBaseColorByObject: str
    MetallicpaintBaseColor: str

class MetallicpaintFinishType:
    """.NET: Autodesk.Revit.DB.Visual.MetallicpaintFinishType"""
    def __init__(self, *args) -> None: ...
    ...

class MetallicpaintFlecksType:
    """.NET: Autodesk.Revit.DB.Visual.MetallicpaintFlecksType"""
    def __init__(self, *args) -> None: ...
    ...

class MetallicpaintPearlType:
    """.NET: Autodesk.Revit.DB.Visual.MetallicpaintPearlType"""
    def __init__(self, *args) -> None: ...
    ...

class MetallicpaintTopcoatType:
    """.NET: Autodesk.Revit.DB.Visual.MetallicpaintTopcoatType"""
    def __init__(self, *args) -> None: ...
    ...

class Mirror:
    """.NET: Autodesk.Revit.DB.Visual.Mirror"""
    def __init__(self, *args) -> None: ...
    CommonTintColor: str
    CommonTintToggle: str
    MirrorColorByObject: str
    MirrorTintcolor: str

class Noise:
    """.NET: Autodesk.Revit.DB.Visual.Noise"""
    def __init__(self, *args) -> None: ...
    TextureRealWorldOffsetZ: str
    TextureRealWorldOffsetY: str
    TextureRealWorldOffsetX: str
    TextureLinkTextureTransforms: str
    TextureAngle: str
    NoisePhase: str
    NoiseLevels: str
    NoiseSize: str
    NoiseThresholdLow: str
    NoiseThresholdHigh: str
    NoiseColor2: str
    NoiseColor1: str
    NoiseType: str

class NoiseType:
    """.NET: Autodesk.Revit.DB.Visual.NoiseType"""
    def __init__(self, *args) -> None: ...
    ...

class PlasticVinyl:
    """.NET: Autodesk.Revit.DB.Visual.PlasticVinyl"""
    def __init__(self, *args) -> None: ...
    CommonTintColor: str
    CommonTintToggle: str
    PlasticvinylPatternAmount: str
    PlasticvinylPatternMap: str
    PlasticvinylPattern: str
    PlasticvinylBumpAmount: str
    PlasticvinylBumpMap: str
    PlasticvinylBump: str
    PlasticvinylApplication: str
    PlasticvinylColorByObject: str
    PlasticvinylColor: str
    PlasticvinylType: str

class PlasticvinylApplicationType:
    """.NET: Autodesk.Revit.DB.Visual.PlasticvinylApplicationType"""
    def __init__(self, *args) -> None: ...
    ...

class PlasticvinylBumpType:
    """.NET: Autodesk.Revit.DB.Visual.PlasticvinylBumpType"""
    def __init__(self, *args) -> None: ...
    ...

class PlasticvinylPatternType:
    """.NET: Autodesk.Revit.DB.Visual.PlasticvinylPatternType"""
    def __init__(self, *args) -> None: ...
    ...

class PlasticvinylType:
    """.NET: Autodesk.Revit.DB.Visual.PlasticvinylType"""
    def __init__(self, *args) -> None: ...
    ...

class SchemaCommon:
    """.NET: Autodesk.Revit.DB.Visual.SchemaCommon"""
    def __init__(self, *args) -> None: ...
    Category: str
    Keyword: str
    UIName: str
    Description: str
    Thumbnail: str
    BaseSchema: str
    VersionGUID: str
    Hidden: str

class SolidGlass:
    """.NET: Autodesk.Revit.DB.Visual.SolidGlass"""
    def __init__(self, *args) -> None: ...
    CommonTintColor: str
    CommonTintToggle: str
    SolidglassBumpAmount: str
    SolidglassBumpMap: str
    SolidglassBumpEnable: str
    SolidglassGlossiness: str
    SolidglassRefractionIor: str
    SolidglassReflectance: str
    SolidglassColorByObject: str
    SolidglassTransmittanceCustomColor: str
    SolidglassTransmittance: str

class SolidglassBumpEnableType:
    """.NET: Autodesk.Revit.DB.Visual.SolidglassBumpEnableType"""
    def __init__(self, *args) -> None: ...
    ...

class SolidglassTransmittanceType:
    """.NET: Autodesk.Revit.DB.Visual.SolidglassTransmittanceType"""
    def __init__(self, *args) -> None: ...
    ...

class Speckle:
    """.NET: Autodesk.Revit.DB.Visual.Speckle"""
    def __init__(self, *args) -> None: ...
    TextureAngle: str
    TextureRealWorldOffsetZ: str
    TextureRealWorldOffsetY: str
    TextureRealWorldOffsetX: str
    TextureLinkTextureTransforms: str
    SpeckleSize: str
    SpeckleColor2: str
    SpeckleColor1: str

class Stone:
    """.NET: Autodesk.Revit.DB.Visual.Stone"""
    def __init__(self, *args) -> None: ...
    CommonTintColor: str
    CommonTintToggle: str
    StonePatternAmount: str
    StonePatternMap: str
    StonePattern: str
    StoneBumpAmount: str
    StoneBumpMap: str
    StoneBump: str
    StoneApplication: str
    StoneColor: str

class StoneApplicationType:
    """.NET: Autodesk.Revit.DB.Visual.StoneApplicationType"""
    def __init__(self, *args) -> None: ...
    ...

class StoneBumpType:
    """.NET: Autodesk.Revit.DB.Visual.StoneBumpType"""
    def __init__(self, *args) -> None: ...
    ...

class StonePatternType:
    """.NET: Autodesk.Revit.DB.Visual.StonePatternType"""
    def __init__(self, *args) -> None: ...
    ...

class SurfaceNdfType:
    """.NET: Autodesk.Revit.DB.Visual.SurfaceNdfType"""
    def __init__(self, *args) -> None: ...
    ...

class Tile:
    """.NET: Autodesk.Revit.DB.Visual.Tile"""
    def __init__(self, *args) -> None: ...
    TextureVRepeat: str
    TextureURepeat: str
    TextureScaleLock: str
    TextureRealWorldScaleY: str
    TextureRealWorldScaleX: str
    TextureWAngle: str
    TextureOffsetLock: str
    TextureRealWorldOffsetY: str
    TextureRealWorldOffsetX: str
    TextureLinkTextureTransforms: str
    TileChangeColumn: str
    TilePerColumn: str
    TileUseColumnEdit: str
    TileChangeRow: str
    TilePerRow: str
    TileUseRowEdit: str
    TileRandomShift: str
    TileLineShift: str
    TileEdgeRoughness: str
    TileVerticalGap: str
    TileHorizontalGap: str
    TileMortarColor: str
    TileRandomSeed: str
    TileFadeVariance: str
    TileColorVariance: str
    TileBrickColor: str
    TileVerticalCount: str
    TileHorizontalCount: str
    TileBrickType: str

class TileBrickType:
    """.NET: Autodesk.Revit.DB.Visual.TileBrickType"""
    def __init__(self, *args) -> None: ...
    ...

class UnifiedBitmap:
    """.NET: Autodesk.Revit.DB.Visual.UnifiedBitmap"""
    def __init__(self, *args) -> None: ...
    TextureVRepeat: str
    TextureURepeat: str
    TextureScaleLock: str
    TextureRealWorldScaleY: str
    TextureRealWorldScaleX: str
    TextureWAngle: str
    TextureOffsetLock: str
    TextureRealWorldOffsetY: str
    TextureRealWorldOffsetX: str
    TextureLinkTextureTransforms: str
    UnifiedbitmapInvert: str
    UnifiedbitmapRGBAmount: str
    UnifiedbitmapBitmap: str

class WallPaint:
    """.NET: Autodesk.Revit.DB.Visual.WallPaint"""
    def __init__(self, *args) -> None: ...
    CommonTintColor: str
    CommonTintToggle: str
    WallpaintApplication: str
    WallpaintFinish: str
    WallpaintColor: str

class WallpaintApplicationType:
    """.NET: Autodesk.Revit.DB.Visual.WallpaintApplicationType"""
    def __init__(self, *args) -> None: ...
    ...

class WallpaintFinishType:
    """.NET: Autodesk.Revit.DB.Visual.WallpaintFinishType"""
    def __init__(self, *args) -> None: ...
    ...

class Water:
    """.NET: Autodesk.Revit.DB.Visual.Water"""
    def __init__(self, *args) -> None: ...
    CommonTintColor: str
    CommonTintToggle: str
    WaterBumpAmount: str
    WaterColorByObject: str
    WaterTintColor: str
    WaterTintEnable: str
    WaterType: str

class WaterTintEnableType:
    """.NET: Autodesk.Revit.DB.Visual.WaterTintEnableType"""
    def __init__(self, *args) -> None: ...
    ...

class WaterType:
    """.NET: Autodesk.Revit.DB.Visual.WaterType"""
    def __init__(self, *args) -> None: ...
    ...

class Wave:
    """.NET: Autodesk.Revit.DB.Visual.Wave"""
    def __init__(self, *args) -> None: ...
    TextureAngle: str
    TextureRealWorldOffsetZ: str
    TextureRealWorldOffsetY: str
    TextureRealWorldOffsetX: str
    TextureLinkTextureTransforms: str
    WaveRandomSeed: str
    WavePhase: str
    WaveAmplitude: str
    WaveWaveLenMax: str
    WaveWaveLenMin: str
    WaveWaveRadius: str
    WaveNumWaveSets: str
    WaveDistribution: str
    WaveColor2: str
    WaveColor1: str

class WaveDistributionType:
    """.NET: Autodesk.Revit.DB.Visual.WaveDistributionType"""
    def __init__(self, *args) -> None: ...
    ...

class Wood:
    """.NET: Autodesk.Revit.DB.Visual.Wood"""
    def __init__(self, *args) -> None: ...
    TextureAngle: str
    TextureRealWorldOffsetZ: str
    TextureRealWorldOffsetY: str
    TextureRealWorldOffsetX: str
    TextureLinkTextureTransforms: str
    WoodThickness: str
    WoodAxialNoise: str
    WoodRadialNoise: str
    WoodColor2: str
    WoodColor1: str

class WoodPoreType:
    """.NET: Autodesk.Revit.DB.Visual.WoodPoreType"""
    def __init__(self, *args) -> None: ...
    ...
