# Auto-generated — Revit 2027 — Autodesk.Revit.DB.Analysis

class AllowLargeGeometry:
    """.NET: Autodesk.Revit.DB.Analysis.AllowLargeGeometry"""
    def __init__(self, *args) -> None: ...
    ...

class AnalysisDisplayColorEntry:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayColorEntry"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Color: Color
    Value: float
    def Dispose(self, ) -> None: ...
    def HasValue(self, ) -> bool: ...
    def IsEqual(self, other: AnalysisDisplayColorEntry) -> bool: ...

class AnalysisDisplayColorSettings:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayColorSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ColorSettingsType: AnalysisDisplayStyleColorSettingsType
    MinColor: Color
    MaxColor: Color
    def AreIntermediateColorsValid(self, map: IList) -> bool: ...
    def Colors(self, ) -> int: ...
    def Dispose(self, ) -> None: ...
    def GetIntermediateColors(self, ) -> IList: ...
    def IsEqual(self, other: AnalysisDisplayColorSettings) -> bool: ...
    def SetIntermediateColors(self, map: IList) -> None: ...

class AnalysisDisplayColoredSurfaceSettings:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayColoredSurfaceSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Transparency: int
    GridLineWeight: int
    GridColor: Color
    ShowContourLines: bool
    ShowGridLines: bool
    def Dispose(self, ) -> None: ...
    def IsEqual(self, other: AnalysisDisplayColoredSurfaceSettings) -> bool: ...

class AnalysisDisplayDeformedShapeSettings:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayDeformedShapeSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Transparency: int
    GridLineWeight: int
    GridColor: Color
    Rounding: float
    TextLabelType: AnalysisDisplayStyleDeformedShapeTextLabelType
    TextTypeId: ElementId
    ShowContourLines: bool
    ShowGridLines: bool
    def Dispose(self, ) -> None: ...
    def IsEqual(self, other: AnalysisDisplayDeformedShapeSettings) -> bool: ...

class AnalysisDisplayDiagramSettings:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayDiagramSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    OutlineLineWeight: int
    OutlineColor: Color
    Transparency: int
    Rounding: float
    TextLabelType: AnalysisDisplayStyleDiagramTextLabelType
    FenceType: AnalysisDisplayStyleDiagramFenceType
    TextTypeId: ElementId
    def Dispose(self, ) -> None: ...
    def IsEqual(self, other: AnalysisDisplayDiagramSettings) -> bool: ...

class AnalysisDisplayLegend(Element):
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayLegend"""
    def __init__(self, *args) -> None: ...
    Height: float
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str

class AnalysisDisplayLegendSettings:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayLegendSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    NumberForScale: float
    ScaleHeight: int
    ColorRangeHeight: int
    ColorRangeWidth: int
    NumberOfSteps: int
    Rounding: float
    ShowDataDescription: bool
    ShowDataName: bool
    ShowUnits: bool
    ShowLegend: bool
    HeadingTextTypeId: ElementId
    TextTypeId: ElementId
    def Dispose(self, ) -> None: ...
    def IsEqual(self, other: AnalysisDisplayLegendSettings) -> bool: ...

class AnalysisDisplayMarkersAndTextSettings:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayMarkersAndTextSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Rounding: float
    MarkerSize: float
    TextLabelType: AnalysisDisplayStyleMarkerTextLabelType
    MarkerType: AnalysisDisplayStyleMarkerType
    TextTypeId: ElementId
    def Dispose(self, ) -> None: ...
    def IsEqual(self, other: AnalysisDisplayMarkersAndTextSettings) -> bool: ...

class AnalysisDisplayStyle(Element):
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayStyle"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    @staticmethod
    def CreateAnalysisDisplayStyle(document: Document, name: str, deformedShapeSettings: AnalysisDisplayDeformedShapeSettings, colorSettings: AnalysisDisplayColorSettings, legendSettings: AnalysisDisplayLegendSettings) -> AnalysisDisplayStyle: ...
    @staticmethod
    def FindByName(document: Document, name: str) -> ElementId: ...
    def GetColorSettings(self, ) -> AnalysisDisplayColorSettings: ...
    def GetColoredSurfaceSettings(self, ) -> AnalysisDisplayColoredSurfaceSettings: ...
    def GetDeformedShapeSettings(self, ) -> AnalysisDisplayDeformedShapeSettings: ...
    def GetDiagramSettings(self, ) -> AnalysisDisplayDiagramSettings: ...
    @staticmethod
    def GetElements(document: Document) -> ICollection: ...
    def GetLegendSettings(self, ) -> AnalysisDisplayLegendSettings: ...
    def GetMarkersAndTextSettings(self, ) -> AnalysisDisplayMarkersAndTextSettings: ...
    def GetVectorSettings(self, ) -> AnalysisDisplayVectorSettings: ...
    def HasColoredSurfaceSettings(self, ) -> bool: ...
    def HasDeformedShapeSettings(self, ) -> bool: ...
    def HasDiagramSettings(self, ) -> bool: ...
    def HasMarkersAndTextSettings(self, ) -> bool: ...
    def HasVectorSettings(self, ) -> bool: ...
    @staticmethod
    def IsNameUnique(document: Document, name: str, excludedElement: AnalysisDisplayStyle) -> bool: ...
    @staticmethod
    def IsTextTypeIdValid(textTypeId: ElementId, doc: Document) -> bool: ...
    def SetColorSettings(self, colorSettings: AnalysisDisplayColorSettings) -> None: ...
    def SetColoredSurfaceSettings(self, coloredSurfaceSettings: AnalysisDisplayColoredSurfaceSettings) -> None: ...
    def SetDeformedShapeSettings(self, deformedShapeSettings: AnalysisDisplayDeformedShapeSettings) -> None: ...
    def SetDiagramSettings(self, diagramSettings: AnalysisDisplayDiagramSettings) -> None: ...
    def SetLegendSettings(self, legendSettings: AnalysisDisplayLegendSettings) -> None: ...
    def SetMarkersAndTextSettings(self, markersAndTextSettings: AnalysisDisplayMarkersAndTextSettings) -> None: ...
    def SetName(self, name: str) -> None: ...
    def SetVectorSettings(self, vectorSettings: AnalysisDisplayVectorSettings) -> None: ...

class AnalysisDisplayStyleColorSettingsType:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayStyleColorSettingsType"""
    def __init__(self, *args) -> None: ...
    ...

class AnalysisDisplayStyleDeformedShapeTextLabelType:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayStyleDeformedShapeTextLabelType"""
    def __init__(self, *args) -> None: ...
    ...

class AnalysisDisplayStyleDiagramFenceType:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayStyleDiagramFenceType"""
    def __init__(self, *args) -> None: ...
    ...

class AnalysisDisplayStyleDiagramTextLabelType:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayStyleDiagramTextLabelType"""
    def __init__(self, *args) -> None: ...
    ...

class AnalysisDisplayStyleMarkerTextLabelType:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayStyleMarkerTextLabelType"""
    def __init__(self, *args) -> None: ...
    ...

class AnalysisDisplayStyleMarkerType:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayStyleMarkerType"""
    def __init__(self, *args) -> None: ...
    ...

class AnalysisDisplayStyleVectorArrowheadScale:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayStyleVectorArrowheadScale"""
    def __init__(self, *args) -> None: ...
    ...

class AnalysisDisplayStyleVectorOrientation:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayStyleVectorOrientation"""
    def __init__(self, *args) -> None: ...
    ...

class AnalysisDisplayStyleVectorPosition:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayStyleVectorPosition"""
    def __init__(self, *args) -> None: ...
    ...

class AnalysisDisplayStyleVectorTextType:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayStyleVectorTextType"""
    def __init__(self, *args) -> None: ...
    ...

class AnalysisDisplayVectorSettings:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisDisplayVectorSettings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ArrowLineWeight: int
    Rounding: float
    VectorOrientation: AnalysisDisplayStyleVectorOrientation
    VectorPosition: AnalysisDisplayStyleVectorPosition
    ArrowheadScale: AnalysisDisplayStyleVectorArrowheadScale
    VectorTextType: AnalysisDisplayStyleVectorTextType
    TextTypeId: ElementId
    def Dispose(self, ) -> None: ...
    def IsEqual(self, other: AnalysisDisplayVectorSettings) -> bool: ...

class AnalysisMode:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisMode"""
    def __init__(self, *args) -> None: ...
    ...

class AnalysisResultSchema:
    """.NET: Autodesk.Revit.DB.Analysis.AnalysisResultSchema"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Scale: float
    CurrentUnits: int
    IsVisible: bool
    AnalysisDisplayStyleId: ElementId
    Description: str
    Name: str
    def Dispose(self, ) -> None: ...
    def GetNumberOfUnits(self, ) -> int: ...
    def GetUnitsMultiplier(self, index: int) -> float: ...
    def GetUnitsName(self, index: int) -> str: ...
    def IsEqual(self, other: AnalysisResultSchema) -> bool: ...
    def SetUnits(self, names: IList, multipliers: IList) -> None: ...

class BuildingEnvelopeAnalyzer:
    """.NET: Autodesk.Revit.DB.Analysis.BuildingEnvelopeAnalyzer"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    @staticmethod
    def Create(document: Document, options: BuildingEnvelopeAnalyzerOptions) -> BuildingEnvelopeAnalyzer: ...
    def Dispose(self, ) -> None: ...
    def GetBoundingElements(self, ) -> IList: ...
    def GetBoundingElementsForSpaceVolume(self, spaceVolume: int) -> IList: ...
    def GetCenterPointsForConnectedGridCellsInSpaceVolume(self, spaceVolume: int) -> IList: ...

class BuildingEnvelopeAnalyzerOptions:
    """.NET: Autodesk.Revit.DB.Analysis.BuildingEnvelopeAnalyzerOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    GridCellSize: float
    OptimizeGridCellSize: bool
    AnalyzeEnclosedSpaceVolumes: bool
    def Dispose(self, ) -> None: ...

class BuildingOperatingDaySchedule(Element):
    """.NET: Autodesk.Revit.DB.Analysis.BuildingOperatingDaySchedule"""
    def __init__(self, *args) -> None: ...
    ScheduleName: str
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    @staticmethod
    def Create(document: Document, name: str) -> BuildingOperatingDaySchedule: ...
    def GetValueForHour(self, hour: int) -> float: ...
    def SetValueForHour(self, hour: int, usage: float) -> None: ...

class BuildingOperatingYearSchedule(Element):
    """.NET: Autodesk.Revit.DB.Analysis.BuildingOperatingYearSchedule"""
    def __init__(self, *args) -> None: ...
    ScheduleName: str
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    @staticmethod
    def Create(document: Document, daySchedule: BuildingOperatingDaySchedule, name: str) -> BuildingOperatingYearSchedule: ...
    def GetScheduleForDay(self, day: DateTime) -> BuildingOperatingDaySchedule: ...
    def SetScheduleForDay(self, day: DateTime, daySchedule: BuildingOperatingDaySchedule) -> None: ...

class ConceptualConstructionFloorSlabType:
    """.NET: Autodesk.Revit.DB.Analysis.ConceptualConstructionFloorSlabType"""
    def __init__(self, *args) -> None: ...
    ...

class ConceptualConstructionOpeningType:
    """.NET: Autodesk.Revit.DB.Analysis.ConceptualConstructionOpeningType"""
    def __init__(self, *args) -> None: ...
    ...

class ConceptualConstructionRoofType:
    """.NET: Autodesk.Revit.DB.Analysis.ConceptualConstructionRoofType"""
    def __init__(self, *args) -> None: ...
    ...

class ConceptualConstructionShadeType:
    """.NET: Autodesk.Revit.DB.Analysis.ConceptualConstructionShadeType"""
    def __init__(self, *args) -> None: ...
    ...

class ConceptualConstructionType(ElementType):
    """.NET: Autodesk.Revit.DB.Analysis.ConceptualConstructionType"""
    def __init__(self, *args) -> None: ...
    MassSurfaceSubCategoryId: ElementId
    MaterialId: ElementId
    FamilyName: str
    CanBeDeleted: bool
    CanBeRenamed: bool
    CanBeCopied: bool
    Name: str
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    @staticmethod
    def GetAllConceptualConstructionsForCategory(ccda: Document, massSubCategoryId: ElementId) -> ICollection: ...
    @staticmethod
    def GetFloorOrSlabConstructionType(ccda: Document, typeEnum: ConceptualConstructionFloorSlabType) -> ElementId: ...
    def GetGBSId(self, massSurfaceSubCategoryId: ElementId) -> int: ...
    @staticmethod
    def GetOpeningConstructionType(ccda: Document, typeEnum: ConceptualConstructionOpeningType) -> ElementId: ...
    @staticmethod
    def GetRoofConstructionType(ccda: Document, typeEnum: ConceptualConstructionRoofType) -> ElementId: ...
    @staticmethod
    def GetShadeConstructionType(ccda: Document, typeEnum: ConceptualConstructionShadeType) -> ElementId: ...
    @staticmethod
    def GetWallConstructionType(ccda: Document, typeEnum: ConceptualConstructionWallType) -> ElementId: ...
    @staticmethod
    def GetWindowOrSkylightConstructionType(ccda: Document, typeEnum: ConceptualConstructionWindowSkylightType) -> ElementId: ...
    @staticmethod
    def IsValidConceptualConstructionId(ccda: Document, constructionTypeId: ElementId) -> bool: ...
    @staticmethod
    def IsValidConceptualConstructionIdForCategory(ccda: Document, constructionTypeId: ElementId, massSubcategoryId: ElementId) -> bool: ...
    @staticmethod
    def IsValidSubcategoryForMassSurfaceDatas(massSubCategoryId: ElementId) -> bool: ...
    def IsValidSurfaceSubcategoryForConstruction(self, massSurfaceSubcategoryId: ElementId) -> bool: ...

class ConceptualConstructionWallType:
    """.NET: Autodesk.Revit.DB.Analysis.ConceptualConstructionWallType"""
    def __init__(self, *args) -> None: ...
    ...

class ConceptualConstructionWindowSkylightType:
    """.NET: Autodesk.Revit.DB.Analysis.ConceptualConstructionWindowSkylightType"""
    def __init__(self, *args) -> None: ...
    ...

class ConceptualSurfaceType(Element):
    """.NET: Autodesk.Revit.DB.Analysis.ConceptualSurfaceType"""
    def __init__(self, *args) -> None: ...
    DefaultConstructionTypeId: ElementId
    MassSubCategoryId: ElementId
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    @staticmethod
    def GetAllMassSubCategoryIds() -> IList: ...
    @staticmethod
    def GetByMassSubCategoryId(cda: Document, massSubCategoryId: ElementId) -> ConceptualSurfaceType: ...
    def GetConstructionTypeIds(self, ) -> ICollection: ...

class ConstructionType:
    """.NET: Autodesk.Revit.DB.Analysis.ConstructionType"""
    def __init__(self, *args) -> None: ...
    ...

class CriticalPathCollector:
    """.NET: Autodesk.Revit.DB.Analysis.CriticalPathCollector"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetCalculatedFlow(self, ) -> float: ...
    def GetCalculatedPressureDrop(self, ) -> float: ...
    def GetCriticalPathCollectorIterator(self, ) -> CriticalPathIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def ToNetworkSegmentIds(self, ) -> IList: ...

class CriticalPathIterator:
    """.NET: Autodesk.Revit.DB.Analysis.CriticalPathIterator"""
    def __init__(self, *args) -> None: ...
    Current: MEPNetworkSegmentId
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetCurrent(self, ) -> MEPNetworkSegmentId: ...
    def IsDone(self, ) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class EnergyAnalysisConstruction(Element):
    """.NET: Autodesk.Revit.DB.Analysis.EnergyAnalysisConstruction"""
    def __init__(self, *args) -> None: ...
    Roughness: int
    Absorptance: float
    ThermalMass: float
    ThermalResistance: float
    ThermalTransmittance: float
    HeatTransferCoefficient: float
    Description: str
    ConstructionName: str
    IsSchematic: bool
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    def GetMaterialIds(self, ) -> IList: ...

class EnergyAnalysisDetailModel(Element):
    """.NET: Autodesk.Revit.DB.Analysis.EnergyAnalysisDetailModel"""
    def __init__(self, *args) -> None: ...
    BuildingTypeId: ElementId
    ExportCategory: ElementId
    ExportMullions: bool
    SimplifyCurtainSystems: bool
    IncludeShadingSurfaces: bool
    Tier: EnergyAnalysisDetailModelTier
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    @staticmethod
    def Create(document: Document, options: EnergyAnalysisDetailModelOptions) -> EnergyAnalysisDetailModel: ...
    def GetAnalyticalOpenings(self, ) -> IList: ...
    def GetAnalyticalShadingSurfaces(self, ) -> IList: ...
    def GetAnalyticalSpaces(self, ) -> IList: ...
    def GetAnalyticalSurfaces(self, ) -> IList: ...
    @staticmethod
    def GetMainEnergyAnalysisDetailModel(document: Document) -> EnergyAnalysisDetailModel: ...
    def TransformModel(self, ) -> None: ...

class EnergyAnalysisDetailModelOptions:
    """.NET: Autodesk.Revit.DB.Analysis.EnergyAnalysisDetailModelOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ExportMullions: bool
    SimplifyCurtainSystems: bool
    IncludeShadingSurfaces: bool
    Tier: EnergyAnalysisDetailModelTier
    EnergyModelType: EnergyModelType
    def Dispose(self, ) -> None: ...

class EnergyAnalysisDetailModelTier:
    """.NET: Autodesk.Revit.DB.Analysis.EnergyAnalysisDetailModelTier"""
    def __init__(self, *args) -> None: ...
    ...

class EnergyAnalysisMaterial(Element):
    """.NET: Autodesk.Revit.DB.Analysis.EnergyAnalysisMaterial"""
    def __init__(self, *args) -> None: ...
    ThermalResistance: float
    SpecificHeatCapacity: float
    Density: float
    ThermalConductivity: float
    Thickness: float
    Description: str
    MaterialName: str
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str

class EnergyAnalysisOpening(Element):
    """.NET: Autodesk.Revit.DB.Analysis.EnergyAnalysisOpening"""
    def __init__(self, *args) -> None: ...
    OpeningId: str
    Corner: XYZ
    OpeningType: EnergyAnalysisOpeningType
    OriginatingElementName: str
    OriginatingElementDescription: str
    CADLinkUniqueId: str
    CADObjectUniqueId: str
    OriginatingElementId: LinkElementId
    OpeningName: str
    Type: gbXMLOpeningType
    Height: float
    Width: float
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    def GetAnalyticalSurface(self, ) -> EnergyAnalysisSurface: ...
    def GetConstruction(self, ) -> EnergyAnalysisConstruction: ...
    def GetPolyloops(self, ) -> IList: ...
    def GetWindowType(self, ) -> EnergyAnalysisWindowType: ...

class EnergyAnalysisOpeningType:
    """.NET: Autodesk.Revit.DB.Analysis.EnergyAnalysisOpeningType"""
    def __init__(self, *args) -> None: ...
    ...

class EnergyAnalysisSpace(Element):
    """.NET: Autodesk.Revit.DB.Analysis.EnergyAnalysisSpace"""
    def __init__(self, *args) -> None: ...
    Volume: float
    Area: float
    CADObjectUniqueId: str
    ComposedName: str
    Description: str
    Number: str
    SpaceName: str
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    def GetAnalyticalSurfaces(self, ) -> IList: ...
    def GetBoundary(self, ) -> IList: ...
    def GetClosedShell(self, ) -> IList: ...

class EnergyAnalysisSurface(Element):
    """.NET: Autodesk.Revit.DB.Analysis.EnergyAnalysisSurface"""
    def __init__(self, *args) -> None: ...
    SurfaceId: str
    Corner: XYZ
    Normal: XYZ
    SurfaceType: EnergyAnalysisSurfaceType
    OriginatingElementName: str
    OriginatingElementDescription: str
    CADLinkUniqueId: str
    CADObjectUniqueId: str
    OriginatingElementId: LinkElementId
    SurfaceName: str
    Type: gbXMLSurfaceType
    Tilt: float
    Azimuth: float
    Height: float
    Width: float
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    def GetAdjacentAnalyticalSpace(self, ) -> EnergyAnalysisSpace: ...
    def GetAnalyticalOpenings(self, ) -> IList: ...
    def GetAnalyticalSpace(self, ) -> EnergyAnalysisSpace: ...
    def GetConstruction(self, ) -> EnergyAnalysisConstruction: ...
    def GetPolyloops(self, ) -> IList: ...

class EnergyAnalysisSurfaceType:
    """.NET: Autodesk.Revit.DB.Analysis.EnergyAnalysisSurfaceType"""
    def __init__(self, *args) -> None: ...
    ...

class EnergyAnalysisWindowType(Element):
    """.NET: Autodesk.Revit.DB.Analysis.EnergyAnalysisWindowType"""
    def __init__(self, *args) -> None: ...
    Transmittance: float
    SolarHeatGainCoefficient: float
    ThermalTransmittance: float
    HeatTransferCoefficient: float
    Description: str
    WindowTypeName: str
    IsSchematic: bool
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    def GetSolarHeatGainCoefficientsForSolarIndicientAngles(self, ) -> IDictionary: ...

class EnergyAnalysisZone(Element):
    """.NET: Autodesk.Revit.DB.Analysis.EnergyAnalysisZone"""
    def __init__(self, *args) -> None: ...
    CADObjectUniqueId: str
    UseAirChangesPerHour: bool
    AirChangesPerHour: float
    UseOutsideAirPerArea: bool
    OutsideAirPerArea: float
    UseOutsideAirPerPerson: bool
    OutsideAirPerPerson: float
    DehumidificationSetPoint: float
    HumidificationSetPoint: float
    UseDehumidificationSetPoint: bool
    UseHumidificationSetPoint: bool
    CoolingAirTemperature: float
    HeatingAirTemperature: float
    CoolingSetPoint: float
    HeatingSetPoint: float
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str

class EnergyDataSettings(Element):
    """.NET: Autodesk.Revit.DB.Analysis.EnergyDataSettings"""
    def __init__(self, *args) -> None: ...
    AnalyticalSurfaceResolution: float
    AnalyticalSpaceResolution: float
    DividePerimeter: bool
    EnergyModel: bool
    BuildingType: gbXMLBuildingType
    CoreOffset: float
    IsExportMullionsEnabled: bool
    IsExportSimplifiedCurtainSystemsEnabled: bool
    IsExportShadingSurfacesEnabled: bool
    ReportsFolder: str
    AnalyticalGridCellSize: float
    BuildingEnvelopeDeterminationMethod: gbXMLExportBuildingEnvelope
    IncludeThermalProperties: bool
    UseAirChangesPerHour: bool
    UseCurrentViewOnly: bool
    UseOutsideAirPerArea: bool
    UseOutsideAirPerPerson: bool
    IsGlazingShaded: bool
    CreateAnalyticalModel: bool
    UseHeatingCredits: bool
    ExportDefaults: bool
    ServiceType: gbXMLServiceType
    BuildingTypeId: ElementId
    AnalysisType: AnalysisMode
    ProjectPhase: ElementId
    GroundPlane: ElementId
    ExportCategory: ElementId
    BuildingHVACSystem: gbXMLBuildingHVACSystem
    BuildingOperatingSchedule: gbXMLBuildingOperatingSchedule
    ProjectReportType: HVACLoadLoadsReportType
    BuildingConstructionClass: HVACLoadConstructionClass
    ExportComplexity: gbXMLExportComplexity
    OutsideAirChangesRatePerHour: float
    OutsideAirPerArea: float
    OutsideAirPerPerson: float
    SkylightWidth: float
    PercentageSkylights: float
    ShadeDepth: float
    SillHeight: float
    PercentageGlazing: float
    SliverSpaceTolerance: float
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    @staticmethod
    def CheckAnalysisType(analysisType: AnalysisMode) -> bool: ...
    @staticmethod
    def CheckBuildingConstructionClass(buildingConstructionClass: HVACLoadConstructionClass) -> bool: ...
    @staticmethod
    def CheckBuildingEnvelope(determinationMethod: gbXMLExportBuildingEnvelope) -> bool: ...
    @staticmethod
    def CheckBuildingHVACSystem(buildingHVACSystem: gbXMLBuildingHVACSystem) -> bool: ...
    @staticmethod
    def CheckBuildingOperatingSchedule(buildingOperatingSchedule: gbXMLBuildingOperatingSchedule) -> bool: ...
    @staticmethod
    def CheckBuildingType(buildingType: gbXMLBuildingType) -> bool: ...
    def CheckConstructionSetElement(self, constructionSetElementId: ElementId) -> bool: ...
    @staticmethod
    def CheckExportCategory(exportCategoryId: ElementId) -> bool: ...
    @staticmethod
    def CheckExportComplexity(exportComplexity: gbXMLExportComplexity) -> bool: ...
    @staticmethod
    def CheckGroundPlane(ccda: Document, groundPlaneId: ElementId) -> bool: ...
    def CheckProjectPhase(self, projectPhaseId: ElementId) -> bool: ...
    @staticmethod
    def CheckProjectReportType(projectReportType: HVACLoadLoadsReportType) -> bool: ...
    @staticmethod
    def CheckRangeOfPercentageGlazing(percentageGlazing: float) -> bool: ...
    @staticmethod
    def CheckRangeOfPercentageSkylights(percentageSkylights: float) -> bool: ...
    @staticmethod
    def CheckRangeOfShadeDepth(shadeDepth: float) -> bool: ...
    @staticmethod
    def CheckRangeOfSillHeight(sillHeight: float) -> bool: ...
    @staticmethod
    def CheckRangeOfSkylightWidth(skylightWidth: float) -> bool: ...
    @staticmethod
    def CheckRangeOfSliverSpaceTolerance(silverSpaceTolerance: float) -> bool: ...
    @staticmethod
    def CheckServiceType(serviceType: gbXMLServiceType) -> bool: ...
    @staticmethod
    def GetBuildingConstructionSetElementId(ccda: Document) -> ElementId: ...
    @staticmethod
    def GetEnergyDataSettings(doc: Document) -> EnergyDataSettings: ...
    @staticmethod
    def GetFromDocument(cda: Document) -> EnergyDataSettings: ...
    def GetReportsFolderParsed(self, ) -> str: ...
    @staticmethod
    def IsDocumentUsingEnergyDataAnalyticalModel(ccda: Document) -> bool: ...
    def SetReportsFolder(self, folderPath: str) -> None: ...

class EnergyModelType:
    """.NET: Autodesk.Revit.DB.Analysis.EnergyModelType"""
    def __init__(self, *args) -> None: ...
    ...

class FieldDomainPoints:
    """.NET: Autodesk.Revit.DB.Analysis.FieldDomainPoints"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class FieldDomainPointsByParameter(FieldDomainPoints):
    """.NET: Autodesk.Revit.DB.Analysis.FieldDomainPointsByParameter"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class FieldDomainPointsByUV(FieldDomainPoints):
    """.NET: Autodesk.Revit.DB.Analysis.FieldDomainPointsByUV"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def SetGridCoordinates(self, uCoordinates: ICollection, vCoordinates: ICollection) -> None: ...

class FieldDomainPointsByXYZ(FieldDomainPoints):
    """.NET: Autodesk.Revit.DB.Analysis.FieldDomainPointsByXYZ"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class FieldValues:
    """.NET: Autodesk.Revit.DB.Analysis.FieldValues"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class FlowConvergenceCharacteristic:
    """.NET: Autodesk.Revit.DB.Analysis.FlowConvergenceCharacteristic"""
    def __init__(self, *args) -> None: ...
    ...

class FlowPositionCharacteristic:
    """.NET: Autodesk.Revit.DB.Analysis.FlowPositionCharacteristic"""
    def __init__(self, *args) -> None: ...
    ...

class FlowTransitionCharacteristic:
    """.NET: Autodesk.Revit.DB.Analysis.FlowTransitionCharacteristic"""
    def __init__(self, *args) -> None: ...
    ...

class GenericZone(Element):
    """.NET: Autodesk.Revit.DB.Analysis.GenericZone"""
    def __init__(self, *args) -> None: ...
    Perimeter: float
    OccupiedVolume: float
    Volume: float
    OccupiedArea: float
    Area: float
    LevelOffset: float
    GeometricDefinition: ZoneGeometricDefinition
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    def AddSpaces(self, spaceIds: ISet) -> None: ...
    def ConvertSpaceBasedToSketchBased(self, typeId: ElementId) -> None: ...
    @staticmethod
    def CreateSketchBased(doc: Document, typeId: ElementId, name: str, domainData: GenericZoneDomainData, levelId: ElementId, curveLoops: IList) -> GenericZone: ...
    @staticmethod
    def CreateSpaceBased(doc: Document, typeId: ElementId, name: str, domainData: GenericZoneDomainData, levelId: ElementId, spaceIds: ISet) -> GenericZone: ...
    def GetBoundaries(self, ) -> IList: ...
    def GetDomainData(self, ) -> GenericZoneDomainData: ...
    def GetSketchId(self, ) -> ElementId: ...
    def GetSpaceIds(self, ) -> ISet: ...
    def RemoveSpaces(self, spaceIds: ISet) -> None: ...

class GenericZoneDomainData:
    """.NET: Autodesk.Revit.DB.Analysis.GenericZoneDomainData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class HVACLoadBuildingType(HVACLoadType):
    """.NET: Autodesk.Revit.DB.Analysis.HVACLoadBuildingType"""
    def __init__(self, *args) -> None: ...
    UnoccupiedCoolingSetPoint: float
    ClosingTime: str
    OpeningTime: str
    BuildingTypeName: str
    DehumidificationSetPoint: float
    HumidificationSetPoint: float
    CoolingSetPoint: float
    HeatingSetPoint: float
    OutdoorAirFlowStandard: OutdoorAirFlowStandard
    AirChangesPerHour: float
    OutdoorAirPerArea: float
    OutdoorAirPerPerson: float
    PlenumLighting: float
    PowerLoadDensity: float
    LightingLoadDensity: float
    LatentHeatGainPerPerson: float
    SensibleHeatGainPerPerson: float
    AreaPerPerson: float
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    @staticmethod
    def Create(document: Document, name: str) -> HVACLoadBuildingType: ...
    @staticmethod
    def IsNameUnique(document: Document, name: str) -> bool: ...
    @staticmethod
    def IsValidTime(hourMinute: str) -> bool: ...

class HVACLoadConstructionClass:
    """.NET: Autodesk.Revit.DB.Analysis.HVACLoadConstructionClass"""
    def __init__(self, *args) -> None: ...
    ...

class HVACLoadLoadsReportType:
    """.NET: Autodesk.Revit.DB.Analysis.HVACLoadLoadsReportType"""
    def __init__(self, *args) -> None: ...
    ...

class HVACLoadSpaceType(HVACLoadType):
    """.NET: Autodesk.Revit.DB.Analysis.HVACLoadSpaceType"""
    def __init__(self, *args) -> None: ...
    SpaceTypeName: str
    IsPlenum: bool
    DehumidificationSetPoint: float
    HumidificationSetPoint: float
    CoolingSetPoint: float
    HeatingSetPoint: float
    OutdoorAirFlowStandard: OutdoorAirFlowStandard
    AirChangesPerHour: float
    OutdoorAirPerArea: float
    OutdoorAirPerPerson: float
    PlenumLighting: float
    PowerLoadDensity: float
    LightingLoadDensity: float
    LatentHeatGainPerPerson: float
    SensibleHeatGainPerPerson: float
    AreaPerPerson: float
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    @staticmethod
    def Create(document: Document, name: str) -> HVACLoadSpaceType: ...
    @staticmethod
    def IsNameUnique(document: Document, name: str) -> bool: ...

class HVACLoadType(Element):
    """.NET: Autodesk.Revit.DB.Analysis.HVACLoadType"""
    def __init__(self, *args) -> None: ...
    DehumidificationSetPoint: float
    HumidificationSetPoint: float
    CoolingSetPoint: float
    HeatingSetPoint: float
    OutdoorAirFlowStandard: OutdoorAirFlowStandard
    AirChangesPerHour: float
    OutdoorAirPerArea: float
    OutdoorAirPerPerson: float
    PlenumLighting: float
    PowerLoadDensity: float
    LightingLoadDensity: float
    LatentHeatGainPerPerson: float
    SensibleHeatGainPerPerson: float
    AreaPerPerson: float
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str

class MEPAnalyticalModelData:
    """.NET: Autodesk.Revit.DB.Analysis.MEPAnalyticalModelData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetMEPAnalyticalModelData(pElement: Element) -> MEPAnalyticalModelData: ...
    def GetNodeById(self, nodeId: int) -> MEPAnalyticalNode: ...
    def GetNodeByIndex(self, index: int) -> MEPAnalyticalNode: ...
    def GetNumberOfNodes(self, ) -> int: ...
    def GetNumberOfSegments(self, ) -> int: ...
    def GetSegmentById(self, segmentId: int) -> MEPAnalyticalSegment: ...
    def GetSegmentByIndex(self, index: int) -> MEPAnalyticalSegment: ...
    def GetSegmentData(self, segmentId: int) -> MEPNetworkSegmentData: ...
    def IsValidNodeId(self, nodeId: int) -> bool: ...
    def IsValidSegmentId(self, segmentId: int) -> bool: ...

class MEPAnalyticalNode:
    """.NET: Autodesk.Revit.DB.Analysis.MEPAnalyticalNode"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Location: XYZ
    IsFlowBlocked: bool
    IsFocalNode: bool
    Id: int
    def Dispose(self, ) -> None: ...
    def IsSameNode(self, other: MEPAnalyticalNode) -> bool: ...

class MEPAnalyticalSegment:
    """.NET: Autodesk.Revit.DB.Analysis.MEPAnalyticalSegment"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Area: float
    Comments: str
    OverrideType: SegmentOverrideType
    DemandFlow: float
    RevitElementId: ElementId
    EndNode: int
    StartNode: int
    Id: int
    Roughness: float
    InnerDiameter: float
    SegmentType: MEPAnalyticalSegmentType
    DomainType: ConnectorDomainType
    def Dispose(self, ) -> None: ...
    def GetFlowCharacteristics(self, doc: Document) -> str: ...
    def GetFlowConvergenceCharacteristic(self, doc: Document, outPosition: FlowPositionCharacteristic) -> FlowConvergenceCharacteristic: ...
    def GetFlowTransitionCharacteristic(self, doc: Document) -> FlowTransitionCharacteristic: ...
    def GetLossCoefficientOverride(self, ) -> float: ...
    def GetNetworkSegmentId(self, ) -> MEPNetworkSegmentId: ...
    def GetPressureDropOverride(self, ) -> float: ...
    @staticmethod
    def GetSegment(subElem: Subelement) -> MEPAnalyticalSegment: ...
    def GetSubelement(self, pADoc: Document) -> Subelement: ...
    def IsSegmentOverridable(self, ) -> bool: ...
    def SetComments(self, analyticalModel: MEPAnalyticalModelData, newComments: str) -> None: ...
    def SetLossCoefficientOverride(self, analyticalModel: MEPAnalyticalModelData, lossCoefficient: float) -> None: ...
    def SetOverrideType(self, analyticalModel: MEPAnalyticalModelData, overrideType: SegmentOverrideType) -> None: ...
    def SetPressureDropOverride(self, analyticalModel: MEPAnalyticalModelData, pressureDrop: float) -> None: ...

class MEPAnalyticalSegmentType:
    """.NET: Autodesk.Revit.DB.Analysis.MEPAnalyticalSegmentType"""
    def __init__(self, *args) -> None: ...
    ...

class MEPNetworkIterator:
    """.NET: Autodesk.Revit.DB.Analysis.MEPNetworkIterator"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    CurrentElementId: ElementId
    SystemClassification: MEPSystemClassification
    SystemId: ElementId
    def Dispose(self, ) -> None: ...
    def End(self, ) -> bool: ...
    def GetAnalyticalModelData(self, ) -> MEPAnalyticalModelData: ...
    def GetAnalyticalNode(self, ) -> MEPAnalyticalNode: ...
    def GetAnalyticalSegment(self, ) -> MEPAnalyticalSegment: ...
    def GetOtherAnalyticalNode(self, ) -> MEPAnalyticalNode: ...
    def Next(self, ) -> None: ...
    def Start(self, ) -> None: ...

class MEPNetworkSegmentData:
    """.NET: Autodesk.Revit.DB.Analysis.MEPNetworkSegmentData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Coefficient: float
    PressureDrop: float
    VelocityPressure: float
    Velocity: float
    FrictionFactor: float
    RelativeRoughness: float
    ReynoldsNumber: float
    FlowState: PipeFlowState
    Flow: float
    SectionNumber: int
    IsCriticalPath: bool
    def Dispose(self, ) -> None: ...
    def GetDownstreamSegments(self, ) -> IList: ...
    def GetUpstreamSegments(self, ) -> IList: ...
    def IsValid(self, ) -> bool: ...

class MEPNetworkSegmentId:
    """.NET: Autodesk.Revit.DB.Analysis.MEPNetworkSegmentId"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    SegmentId: int
    ElementId: ElementId
    def Dispose(self, ) -> None: ...
    def IsValid(self, ) -> bool: ...

class MassLevelData(Element):
    """.NET: Autodesk.Revit.DB.Analysis.MassLevelData"""
    def __init__(self, *args) -> None: ...
    ConceptualConstructionIsByEnergyData: bool
    ConceptualConstructionId: ElementId
    MaterialId: ElementId
    OwningMassId: ElementId
    NLevelPerimeter: float
    NLevelFafArea: float
    NExteriorSurfaceArea: float
    NVolume: float
    StrUsage: str
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    def IsEmpty(self, ) -> bool: ...
    @staticmethod
    def IsMassFamilyInstance(document: Document, id: ElementId) -> bool: ...
    def IsValidConceptualConstructionTypeElement(self, id: ElementId) -> bool: ...

class OutdoorAirFlowStandard:
    """.NET: Autodesk.Revit.DB.Analysis.OutdoorAirFlowStandard"""
    def __init__(self, *args) -> None: ...
    ...

class PathOfTravel(Element):
    """.NET: Autodesk.Revit.DB.Analysis.PathOfTravel"""
    def __init__(self, *args) -> None: ...
    LineStyle: ElementId
    PathEnd: XYZ
    PathStart: XYZ
    PathMidpoint: XYZ
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    @staticmethod
    def Create(DBView: View, pathStart: XYZ, pathEnd: XYZ, resultStatus: PathOfTravelCalculationStatus) -> PathOfTravel: ...
    @staticmethod
    def CreateMapped(DBView: View, pathStarts: IList, pathEnds: IList, resultStatus: IList) -> IList: ...
    @staticmethod
    def CreateMultiple(DBView: View, pathStarts: IList, pathEnds: IList, resultStatus: IList) -> IList: ...
    @staticmethod
    def FindEndsOfShortestPaths(DBView: View, destinationPoints: IList, startPoints: IList) -> IList: ...
    @staticmethod
    def FindShortestPaths(DBView: View, destinationPoints: IList, startPoints: IList) -> IList: ...
    @staticmethod
    def FindStartsOfLongestPathsFromRooms(DBView: View, destinationPoints: IList) -> IList: ...
    def GetCurves(self, ) -> IList: ...
    def GetWaypoints(self, ) -> IList: ...
    def InsertWaypoint(self, waypoint: XYZ, index: int) -> None: ...
    @staticmethod
    def IsInRevealObstaclesMode(DBView: View) -> bool: ...
    def RemoveWaypoint(self, index: int) -> None: ...
    @staticmethod
    def SetRevealObstaclesMode(DBView: View, newState: bool) -> PathOfTravelCalculationStatus: ...
    def SetWaypoint(self, waypoint: XYZ, index: int) -> None: ...
    def Update(self, ) -> PathOfTravelCalculationStatus: ...
    @staticmethod
    def UpdateMultiple(adoc: Document, elementsToUpdate: IList, resultStatus: IList) -> int: ...

class PathOfTravelCalculationServerIds:
    """.NET: Autodesk.Revit.DB.Analysis.PathOfTravelCalculationServerIds"""
    def __init__(self, *args) -> None: ...
    DefaultPathOfTravelCalculationGUID: Guid

class PathOfTravelCalculationStatus:
    """.NET: Autodesk.Revit.DB.Analysis.PathOfTravelCalculationStatus"""
    def __init__(self, *args) -> None: ...
    ...

class Polyloop:
    """.NET: Autodesk.Revit.DB.Analysis.Polyloop"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Direction: XYZ
    Centroid: XYZ
    def ComputeArea(self, ) -> float: ...
    def Dispose(self, ) -> None: ...
    def GetPoints(self, ) -> IList: ...

class RouteAnalysisSettings(Element):
    """.NET: Autodesk.Revit.DB.Analysis.RouteAnalysisSettings"""
    def __init__(self, *args) -> None: ...
    MinimumLength: float
    AnalysisZoneTopOffset: float
    AnalysisZoneBottomOffset: float
    IgnoreImports: bool
    EnableIgnoredCategoryIds: bool
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    def GetExcludedCategoryIds(self, ) -> ICollection: ...
    def GetIgnoredCategoryIds(self, ) -> ICollection: ...
    @staticmethod
    def GetRouteAnalysisSettings(cda: Document) -> RouteAnalysisSettings: ...
    def IsLargeGeometryAllowed(self, ) -> bool: ...
    def SetIgnoredCategoryIds(self, categoryIds: ICollection) -> None: ...

class SegmentOverrideType:
    """.NET: Autodesk.Revit.DB.Analysis.SegmentOverrideType"""
    def __init__(self, *args) -> None: ...
    ...

class SizingCalculator:
    """.NET: Autodesk.Revit.DB.Analysis.SizingCalculator"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def CalculateSizeByFriction(self, flow: float, friction: float, sizingOptions: SizingOptions) -> None: ...
    def CalculateSizeByVelocity(self, flow: float, velocity: float, sizingOptions: SizingOptions) -> None: ...
    def Dispose(self, ) -> None: ...
    def EquivalentDiameter(self, eShape: ConnectorProfileType, widthOrDiameter: float, height: float) -> float: ...
    def Friction(self, flow: float, options: SizingOptions) -> float: ...
    def Velocity(self, flow: float, options: SizingOptions) -> float: ...

class SizingOptions:
    """.NET: Autodesk.Revit.DB.Analysis.SizingOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Diameter: float
    Width: float
    Area: float
    Height: float
    MaxSize: float
    MinSize: float
    Viscosity: float
    Density: float
    Roughness: float
    ProfileType: ConnectorProfileType
    DomainType: ConnectorDomainType
    def Dispose(self, ) -> None: ...
    def IsValid(self, ) -> bool: ...
    def SetEquivalentHeight(self, fixedWidth: float, availableSizes: ISet) -> None: ...
    def SetEquivalentWidth(self, fixedHeight: float, availableSizes: ISet) -> None: ...
    def SetNextAvailableSize(self, profileType: ConnectorProfileType, width: float, height: float, availableSizes: ISet) -> None: ...

class SpatialFieldManager(Element):
    """.NET: Autodesk.Revit.DB.Analysis.SpatialFieldManager"""
    def __init__(self, *args) -> None: ...
    LegendShowDescription: bool
    LegendShowConfigurationName: bool
    LegendTextTypeId: ElementId
    ResultsVisibleInView: bool
    UseRangeForAllMeasurements: bool
    CurrentMeasurement: int
    LegendPosition: XYZ
    NumberOfMeasurements: int
    AllowInteractiveSettings: bool
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    def AddSpatialFieldPrimitive(self, curve: Curve, trf: Transform) -> int: ...
    def Clear(self, ) -> None: ...
    @staticmethod
    def CreateSpatialFieldManager(view: View, numberOfMeasurements: int) -> SpatialFieldManager: ...
    def GetLegend(self, ) -> AnalysisDisplayLegend: ...
    def GetMaximum(self, resultIndex: int, rawValue: bool) -> float: ...
    def GetMinimum(self, resultIndex: int, rawValue: bool) -> float: ...
    def GetRegisteredResults(self, ) -> IList: ...
    def GetResultSchema(self, idx: int) -> AnalysisResultSchema: ...
    @staticmethod
    def GetSpatialFieldManager(view: View) -> SpatialFieldManager: ...
    def IsResultSchemaNameUnique(self, name: str, resultIndexToSkip: int) -> bool: ...
    @staticmethod
    def IsTextTypeIdValid(textTypeId: ElementId, doc: Document) -> bool: ...
    def RegisterResult(self, resultSchema: AnalysisResultSchema) -> int: ...
    def RemoveSpatialFieldPrimitive(self, idx: int) -> None: ...
    def SetMeasurementDescriptions(self, measurementDescriptions: IList) -> None: ...
    def SetMeasurementNames(self, measurementNames: IList) -> None: ...
    def SetResultSchema(self, idx: int, resultSchema: AnalysisResultSchema) -> None: ...
    def UpdateSpatialFieldPrimitive(self, idx: int, fieldDomainPoints: FieldDomainPoints, fieldValues: FieldValues, resultIndex: int) -> None: ...

class SpatialFieldPrimitiveHideMode:
    """.NET: Autodesk.Revit.DB.Analysis.SpatialFieldPrimitiveHideMode"""
    def __init__(self, *args) -> None: ...
    ...

class SystemsAnalysisOptions:
    """.NET: Autodesk.Revit.DB.Analysis.SystemsAnalysisOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    OutputFolder: str
    WeatherFile: str
    WorkflowFile: str
    def Dispose(self, ) -> None: ...

class SystemsAnalysisReportStyle:
    """.NET: Autodesk.Revit.DB.Analysis.SystemsAnalysisReportStyle"""
    def __init__(self, *args) -> None: ...
    ...

class ValueAtPoint(ValueAtPointBase):
    """.NET: Autodesk.Revit.DB.Analysis.ValueAtPoint"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class VectorAtPoint(ValueAtPointBase):
    """.NET: Autodesk.Revit.DB.Analysis.VectorAtPoint"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class ViewHVACLoadsReport(View):
    """.NET: Autodesk.Revit.DB.Analysis.ViewHVACLoadsReport"""
    def __init__(self, *args) -> None: ...
    ViewTemplateId: ElementId
    SunlightIntensity: int
    ShadowIntensity: int
    Discipline: ViewDiscipline
    DisplayStyle: DisplayStyle
    RevealConstraintsMode: bool
    TemporaryViewModes: TemporaryViewModes
    AnalysisDisplayStyleId: ElementId
    AreCoordinationModelHandlesHidden: bool
    ArePointCloudsHidden: bool
    AreImportCategoriesHidden: bool
    AreAnalyticalModelCategoriesHidden: bool
    AreAnnotationCategoriesHidden: bool
    AreModelCategoriesHidden: bool
    DetailLevel: ViewDetailLevel
    PartsVisibility: PartsVisibility
    Title: str
    IsAssemblyView: bool
    AssociatedAssemblyInstanceId: ElementId
    IsCallout: bool
    ViewPositionId: ElementId
    SunAndShadowSettings: SunAndShadowSettings
    SketchPlane: SketchPlane
    CropBoxVisible: bool
    CropBoxActive: bool
    GenLevel: Level
    IsTemplate: bool
    CanBePrinted: bool
    UpDirection: XYZ
    RightDirection: XYZ
    ViewDirection: XYZ
    Scale: int
    Origin: XYZ
    CropBox: BoundingBoxXYZ
    ViewType: ViewType
    Outline: BoundingBoxUV
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    @staticmethod
    def Create(document: Document, viewName: str) -> ViewHVACLoadsReport: ...
    def IsAnalysisCompleted(self, ) -> bool: ...
    def RunLoadsAnalysis(self, ) -> None: ...

class ViewSystemsAnalysisReport(View):
    """.NET: Autodesk.Revit.DB.Analysis.ViewSystemsAnalysisReport"""
    def __init__(self, *args) -> None: ...
    AnalysisDateAndTime: DateTime
    ReportStyle: SystemsAnalysisReportStyle
    SystemsAnalysisOutputFolder: str
    WeatherFile: str
    SystemsAnalysisWorkflowFile: str
    ViewTemplateId: ElementId
    SunlightIntensity: int
    ShadowIntensity: int
    Discipline: ViewDiscipline
    DisplayStyle: DisplayStyle
    RevealConstraintsMode: bool
    TemporaryViewModes: TemporaryViewModes
    AnalysisDisplayStyleId: ElementId
    AreCoordinationModelHandlesHidden: bool
    ArePointCloudsHidden: bool
    AreImportCategoriesHidden: bool
    AreAnalyticalModelCategoriesHidden: bool
    AreAnnotationCategoriesHidden: bool
    AreModelCategoriesHidden: bool
    DetailLevel: ViewDetailLevel
    PartsVisibility: PartsVisibility
    Title: str
    IsAssemblyView: bool
    AssociatedAssemblyInstanceId: ElementId
    IsCallout: bool
    ViewPositionId: ElementId
    SunAndShadowSettings: SunAndShadowSettings
    SketchPlane: SketchPlane
    CropBoxVisible: bool
    CropBoxActive: bool
    GenLevel: Level
    IsTemplate: bool
    CanBePrinted: bool
    UpDirection: XYZ
    RightDirection: XYZ
    ViewDirection: XYZ
    Scale: int
    Origin: XYZ
    CropBox: BoundingBoxXYZ
    ViewType: ViewType
    Outline: BoundingBoxUV
    IsValidObject: bool
    DemolishedPhaseId: ElementId
    CreatedPhaseId: ElementId
    OwnerViewId: ElementId
    ViewSpecific: bool
    AssemblyInstanceId: ElementId
    LevelId: ElementId
    UniqueId: str
    IsTransient: bool
    Id: ElementId
    GroupId: ElementId
    IsModifiable: bool
    VersionGuid: Guid
    WorksetId: WorksetId
    Pinned: bool
    BoundingBox: BoundingBoxXYZ
    Geometry: GeometryElement
    DesignOption: DesignOption
    Document: Document
    Location: Location
    ParametersMap: ParameterMap
    Parameters: ParameterSet
    Parameter: Parameter
    Parameter: Parameter
    Parameter: Parameter
    Category: Category
    Name: str
    @staticmethod
    def CancelSystemsAnalysis(document: Document, reportElement: ElementId) -> None: ...
    @staticmethod
    def Create(document: Document, viewName: str) -> ViewSystemsAnalysisReport: ...
    @staticmethod
    def GetLatestSystemsAnalysisReport(document: Document) -> ElementId: ...
    def GetReportContent(self, ) -> str: ...
    def IsAnalysisCompleted(self, ) -> bool: ...
    def RequestSystemsAnalysis(self, options: SystemsAnalysisOptions) -> None: ...

class ZoneGeometricDefinition:
    """.NET: Autodesk.Revit.DB.Analysis.ZoneGeometricDefinition"""
    def __init__(self, *args) -> None: ...
    ...

class gbXMLBuildingHVACSystem:
    """.NET: Autodesk.Revit.DB.Analysis.gbXMLBuildingHVACSystem"""
    def __init__(self, *args) -> None: ...
    ...

class gbXMLBuildingOperatingSchedule:
    """.NET: Autodesk.Revit.DB.Analysis.gbXMLBuildingOperatingSchedule"""
    def __init__(self, *args) -> None: ...
    ...

class gbXMLBuildingType:
    """.NET: Autodesk.Revit.DB.Analysis.gbXMLBuildingType"""
    def __init__(self, *args) -> None: ...
    ...

class gbXMLConditionType:
    """.NET: Autodesk.Revit.DB.Analysis.gbXMLConditionType"""
    def __init__(self, *args) -> None: ...
    ...

class gbXMLExportBuildingEnvelope:
    """.NET: Autodesk.Revit.DB.Analysis.gbXMLExportBuildingEnvelope"""
    def __init__(self, *args) -> None: ...
    ...

class gbXMLExportComplexity:
    """.NET: Autodesk.Revit.DB.Analysis.gbXMLExportComplexity"""
    def __init__(self, *args) -> None: ...
    ...

class gbXMLOpeningType:
    """.NET: Autodesk.Revit.DB.Analysis.gbXMLOpeningType"""
    def __init__(self, *args) -> None: ...
    ...

class gbXMLServiceType:
    """.NET: Autodesk.Revit.DB.Analysis.gbXMLServiceType"""
    def __init__(self, *args) -> None: ...
    ...

class gbXMLSpaceType:
    """.NET: Autodesk.Revit.DB.Analysis.gbXMLSpaceType"""
    def __init__(self, *args) -> None: ...
    ...

class gbXMLSurfaceType:
    """.NET: Autodesk.Revit.DB.Analysis.gbXMLSurfaceType"""
    def __init__(self, *args) -> None: ...
    ...
