# Auto-generated — Revit 2027 — Autodesk.Revit.DB.ExternalData

class CoordinationModelElementProperty:
    """.NET: Autodesk.Revit.DB.ExternalData.CoordinationModelElementProperty"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Value: str
    Group: str
    Name: str
    def Dispose(self, ) -> None: ...

class CoordinationModelLinkData:
    """.NET: Autodesk.Revit.DB.ExternalData.CoordinationModelLinkData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    VersionLabel: str
    ViewName: str
    ModelName: str
    FileId: str
    ProjectId: str
    FileSize: float
    DisplayPath: str
    SourcePath: str
    def Dispose(self, ) -> None: ...
    def GetCategoryNames(self, ) -> IList: ...
    def GetPathType(self, ) -> CoordinationModelLinkPathType: ...

class CoordinationModelLinkOptions:
    """.NET: Autodesk.Revit.DB.ExternalData.CoordinationModelLinkOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Positioning: CoordinationModelPositioning
    def Dispose(self, ) -> None: ...

class CoordinationModelLinkPathType:
    """.NET: Autodesk.Revit.DB.ExternalData.CoordinationModelLinkPathType"""
    def __init__(self, *args) -> None: ...
    ...

class CoordinationModelLinkUtils:
    """.NET: Autodesk.Revit.DB.ExternalData.CoordinationModelLinkUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def ContainsCategory(document: Document, coordinationModelType: ElementType, categoryName: str) -> bool: ...
    @staticmethod
    def GetAllCoordinationModelInstanceIds(document: Document) -> ISet: ...
    @staticmethod
    def GetAllCoordinationModelTypeIds(document: Document) -> ISet: ...
    @staticmethod
    def GetAllPropertiesForReferenceInsideCoordinationModel(document: Document, coordinationModelInstance: Element, reference: Reference) -> IList: ...
    @staticmethod
    def GetCategoryForReferenceInsideCoordinationModel(document: Document, coordinationModelInstance: Element, reference: Reference) -> str: ...
    @staticmethod
    def GetColorOverride(document: Document, view: View, coordinationModelType: Element) -> Color: ...
    @staticmethod
    def GetColorOverrideForCategory(document: Document, view: View, coordinationModelType: ElementType, categoryName: str) -> Color: ...
    @staticmethod
    def GetCoordinationModelTypeData(document: Document, coordinationModelType: ElementType) -> CoordinationModelLinkData: ...
    @staticmethod
    def GetTransparencyOverride(document: Document, view: View, coordinationModelType: Element) -> int: ...
    @staticmethod
    def GetVisibilityOverride(document: Document, view: View, coordinationModelTypeOrInstance: Element) -> bool: ...
    @staticmethod
    def GetVisibilityOverrideForCategory(document: Document, view: View, coordinationModelType: ElementType, categoryName: str) -> bool: ...
    @staticmethod
    def GetVisibilityOverrideForReferenceInsideCoordinationModel(document: Document, view: View, coordinationModelInstance: Element, reference: Reference) -> bool: ...
    @staticmethod
    def IsCoordinationModelInstance(document: Document, element: Element) -> bool: ...
    @staticmethod
    def IsCoordinationModelType(document: Document, coordinationModelType: Element) -> bool: ...
    @staticmethod
    def Link3DViewFromAutodeskDocs(document: Document, accountId: str, projectId: str, fileId: str, viewName: str, linkOptions: CoordinationModelLinkOptions) -> Element: ...
    @staticmethod
    def LinkCoordinationModelFromLocalPath(document: Document, filePath: str, linkOptions: CoordinationModelLinkOptions) -> Element: ...
    @staticmethod
    def Reload(document: Document, coordinationModelType: ElementType) -> None: ...
    @staticmethod
    def ReloadAutodeskDocsCoordinationModelFrom(document: Document, coordinationModelType: ElementType, accountId: str, projectId: str, fileId: str, viewName: str) -> None: ...
    @staticmethod
    def ReloadLocalCoordinationModelFrom(document: Document, coordinationModelType: ElementType, filePath: str) -> None: ...
    @staticmethod
    def SetColorOverride(document: Document, view: View, coordinationModelType: Element, color: Color) -> None: ...
    @staticmethod
    def SetColorOverrideForCategory(document: Document, view: View, coordinationModelType: ElementType, categoryName: str, color: Color) -> None: ...
    @staticmethod
    def SetTransparencyOverride(document: Document, view: View, coordinationModelType: Element, transparency: int) -> None: ...
    @staticmethod
    def SetVisibilityOverride(document: Document, view: View, coordinationModelTypeOrInstance: Element, visible: bool) -> None: ...
    @staticmethod
    def SetVisibilityOverrideForCategory(document: Document, view: View, coordinationModelType: ElementType, categoryName: str, visible: bool) -> None: ...
    @staticmethod
    def SetVisibilityOverrideForReferenceInsideCoordinationModel(document: Document, view: View, coordinationModelInstance: Element, reference: Reference, visible: bool) -> None: ...
    @staticmethod
    def Unload(document: Document, coordinationModelType: ElementType) -> None: ...

class CoordinationModelPositioning:
    """.NET: Autodesk.Revit.DB.ExternalData.CoordinationModelPositioning"""
    def __init__(self, *args) -> None: ...
    ...

class ExtendedParameterElement(ParameterElement):
    """.NET: Autodesk.Revit.DB.ExternalData.ExtendedParameterElement"""
    def __init__(self, *args) -> None: ...
    LinkId: ElementId
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

class ExtendedPropertiesBindingType:
    """.NET: Autodesk.Revit.DB.ExternalData.ExtendedPropertiesBindingType"""
    def __init__(self, *args) -> None: ...
    ...

class ExtendedPropertiesBindings:
    """.NET: Autodesk.Revit.DB.ExternalData.ExtendedPropertiesBindings"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    BindingType: ExtendedPropertiesBindingType
    def AddCategories(self, categories: ICollection) -> None: ...
    def AddCategory(self, categoryId: ForgeTypeId) -> None: ...
    def Dispose(self, ) -> None: ...

class ExtendedPropertiesLink(Element):
    """.NET: Autodesk.Revit.DB.ExternalData.ExtendedPropertiesLink"""
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
    def Create(doc: Document, externalReference: ExternalResourceReference) -> LinkLoadResult: ...
    @staticmethod
    def CreateFromCloudDataset(doc: Document, datasetId: str) -> LinkLoadResult: ...
    def GetAllAssociatedPropertyIds(self, ) -> IList: ...
    def LoadFrom(self, externalReference: ExternalResourceReference) -> LinkLoadResult: ...
    def Reload(self, ) -> LinkLoadResult: ...

class ExtendedPropertiesLinkData:
    """.NET: Autodesk.Revit.DB.ExternalData.ExtendedPropertiesLinkData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Region: str
    ContainerName: str
    def AddParameterSchemaWithBindings(self, schemaId: ForgeTypeId, bindings: ExtendedPropertiesBindings) -> None: ...
    def AddValues(self, elementId: LinkElementId, values: ExtendedPropertiesLinkValues) -> bool: ...
    def Dispose(self, ) -> None: ...
    def HasSchema(self, schemaId: ForgeTypeId) -> bool: ...
    @staticmethod
    def IsValidContainerName(containerName: str) -> bool: ...

class ExtendedPropertiesLinkLoadContent(ExternalResourceLoadContent):
    """.NET: Autodesk.Revit.DB.ExternalData.ExtendedPropertiesLinkLoadContent"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    LoadStatus: ExternalResourceLoadStatus
    Version: str
    def SetExtendedPropertiesLinkData(self, data: ExtendedPropertiesLinkData) -> None: ...

class ExtendedPropertiesLinkValues:
    """.NET: Autodesk.Revit.DB.ExternalData.ExtendedPropertiesLinkValues"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def AddValue(self, schemaId: ForgeTypeId, value: str) -> bool: ...
    def Dispose(self, ) -> None: ...
