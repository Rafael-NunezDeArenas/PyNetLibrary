# encoding: utf-8
# module Autodesk.Revit.DB.DirectContext3D calls itself DirectContext3D
# from RevitAPI, Version=22.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Camera(object, IDisposable):
    """
    A collection of camera settings for the current view.
    
    Camera(other: Camera)
    """
    def Dispose(self):
        """ Dispose(self: Camera) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Camera, disposing: bool) """
        pass

    def Transform(self, trf):
        """
        Transform(self: Camera, trf: Transform)
            Transforms the camera
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
    def __new__(self, other):
        """ __new__(cls: type, other: Camera) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    EyePosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Camera's position in the world

Get: EyePosition(self: Camera) -> XYZ

Set: EyePosition(self: Camera) = value
"""

    FarDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance to far clipping plane

Get: FarDistance(self: Camera) -> float

Set: FarDistance(self: Camera) = value
"""

    HorizontalExtent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Horizontal extent of the camera's view, measured at target distance.

Get: HorizontalExtent(self: Camera) -> float

Set: HorizontalExtent(self: Camera) = value
"""

    HorizontalOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Horizontal offset of the camera's view center from target, measured at target distance.

Get: HorizontalOffset(self: Camera) -> float

Set: HorizontalOffset(self: Camera) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: Camera) -> bool

"""

    NearDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance to near clipping plane

Get: NearDistance(self: Camera) -> float

Set: NearDistance(self: Camera) = value
"""

    ProjectionMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Projection method

Get: ProjectionMethod(self: Camera) -> ProjectionMethod

Set: ProjectionMethod(self: Camera) = value
"""

    TargetDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance from camera to its target

Get: TargetDistance(self: Camera) -> float

Set: TargetDistance(self: Camera) = value
"""

    UpDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Up direction of the camera

Get: UpDirection(self: Camera) -> XYZ

Set: UpDirection(self: Camera) = value
"""

    VerticalExtent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Vertical extent of the camera's view, measured at target distance.

Get: VerticalExtent(self: Camera) -> float

Set: VerticalExtent(self: Camera) = value
"""

    VerticalOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Vertical offset of the camera's view center from target, measured at target distance.

Get: VerticalOffset(self: Camera) -> float

Set: VerticalOffset(self: Camera) = value
"""

    ViewDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Direction that the camera is facing

Get: ViewDirection(self: Camera) -> XYZ

Set: ViewDirection(self: Camera) = value
"""



class ClipPlane(object, IDisposable):
    """
    A set of parameters representing a clip plane in DirectContext3D.
    
    ClipPlane(other: ClipPlane)
    """
    def Dispose(self):
        """ Dispose(self: ClipPlane) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ClipPlane, disposing: bool) """
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
    def __new__(self, other):
        """ __new__(cls: type, other: ClipPlane) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ClipPlane) -> bool

"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The plane's normal vector.

Get: Normal(self: ClipPlane) -> XYZ

Set: Normal(self: ClipPlane) = value
"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The plane's origin.

Get: Origin(self: ClipPlane) -> XYZ

Set: Origin(self: ClipPlane) = value
"""



class DirectContext3DDocumentUtils(object):
    """ The methods provided by this utility class support the use of DirectContext3D and storage of DirectContext3D handle elements in Revit documents. """
    @staticmethod
    def GetDirectContext3DHandleInstances(aDocument, handleCategory):
        """
        GetDirectContext3DHandleInstances(aDocument: Document, handleCategory: ElementId) -> ISet[ElementId]
        
            Returns all DirectContext3D handle instances of the given category in the 
             document.
        
        
            aDocument: The document.
            handleCategory: A category of DirectContext3D handles.
            Returns: The set of DirectContext3D handle instances of the given category.
        """
        pass

    @staticmethod
    def GetDirectContext3DHandleTypes(aDocument, handleCategory):
        """
        GetDirectContext3DHandleTypes(aDocument: Document, handleCategory: ElementId) -> ISet[ElementId]
        
            Returns all DirectContext3D handle types of the given category in the document.
        
            aDocument: The document.
            handleCategory: A category of DirectContext3D handles.
            Returns: The set of DirectContext3D handle types of the given category.
        """
        pass

    @staticmethod
    def IsADirectContext3DHandleCategory(categoryId):
        """
        IsADirectContext3DHandleCategory(categoryId: ElementId) -> bool
        
            Checks whether the provided category ID is one of the categories used by 
             DirectContext3D handle elements.
        
        
            categoryId: The category ID to check.
            Returns: True, if the category is valid for DirectContext3D handle elements, false 
             otherwise.
        """
        pass

    @staticmethod
    def IsADirectContext3DHandleInstance(aDocument, elementId):
        """
        IsADirectContext3DHandleInstance(aDocument: Document, elementId: ElementId) -> bool
        
            Checks whether the provided Element ID corresponds to a DirectContext3D handle 
             instance element.
        
        
            aDocument: The document.
            elementId: The ID of the element to check.
            Returns: True, if the element is a valid DirectContext3D handle instance, false 
             otherwise.
        """
        pass

    @staticmethod
    def IsADirectContext3DHandleType(aDocument, elementId):
        """
        IsADirectContext3DHandleType(aDocument: Document, elementId: ElementId) -> bool
        
            Checks whether the provided Element ID corresponds to a DirectContext3D handle 
             type element.
        
        
            aDocument: The document.
            elementId: The ID of the element to check.
            Returns: True, if the element is a valid DirectContext3D handle type, false otherwise.
        """
        pass

    __all__ = [
        'GetDirectContext3DHandleInstances',
        'GetDirectContext3DHandleTypes',
        'IsADirectContext3DHandleCategory',
        'IsADirectContext3DHandleInstance',
        'IsADirectContext3DHandleType',
    ]


class DirectContext3DHandleOverrides(object, IDisposable):
    """ A set of DirectContext3DHandleSettings that are stored by a view. """
    def Assign(self, other):
        """
        Assign(self: DirectContext3DHandleOverrides, other: DirectContext3DHandleOverrides)
            Assigns values of the source overrides to this object.
        
            other: The source overrides.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DirectContext3DHandleOverrides) """
        pass

    def GetDirectContext3DHandleSettings(self, aDoc, elementId):
        """
        GetDirectContext3DHandleSettings(self: DirectContext3DHandleOverrides, aDoc: Document, elementId: ElementId) -> DirectContext3DHandleSettings
        
            Gets override settings associated with a DirectContext3D handle instance or 
             type.
        
        
            aDoc: Document where elementId resides.
            elementId: Id of the overridden element.
            Returns: The override settings assigned to the handle element, if present, or a default 
             override settings if nothing was found.
        """
        pass

    def IsEqual(self, other):
        """
        IsEqual(self: DirectContext3DHandleOverrides, other: DirectContext3DHandleOverrides) -> bool
        
            Check if the contents of two overrides are equal.
        
            other: The overrides to be compared.
            Returns: True for equal, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DirectContext3DHandleOverrides, disposing: bool) """
        pass

    def SetDirectContext3DHandleSettings(self, aDoc, elementId, newSettings):
        """
        SetDirectContext3DHandleSettings(self: DirectContext3DHandleOverrides, aDoc: Document, elementId: ElementId, newSettings: DirectContext3DHandleSettings)
            Assigns override settings associated with a DirectContext3D handle instance or 
             type.
        
        
            aDoc: Document where elementId resides.
            elementId: Id of the element to be overridden.
            newSettings: The override settings to be assigned to the handle element.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: DirectContext3DHandleOverrides) -> bool

"""



class DirectContext3DHandleSettings(object, IDisposable):
    """
    Overriding settings applied to DirectContext3DHandles through the Visibility dialog.
    
    DirectContext3DHandleSettings(other: DirectContext3DHandleSettings)
    DirectContext3DHandleSettings(visibility: bool, transparency: int)
    DirectContext3DHandleSettings()
    """
    def Assign(self, other):
        """
        Assign(self: DirectContext3DHandleSettings, other: DirectContext3DHandleSettings)
            Assigns values of the source settings to this object.
        
            other: The source settings.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DirectContext3DHandleSettings) """
        pass

    def GetTransparency(self):
        """
        GetTransparency(self: DirectContext3DHandleSettings) -> int
        
            Gets the transparency value of the handle and the associated DirectContext3D 
             graphics.
        
            Returns: The transparency value (in percentage)
        """
        pass

    def IsEqual(self, other):
        """
        IsEqual(self: DirectContext3DHandleSettings, other: DirectContext3DHandleSettings) -> bool
        
            Check if the contents of two instances of settings are equal.
        
            other: The settings to be compared.
            Returns: True for equal, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DirectContext3DHandleSettings, disposing: bool) """
        pass

    def SetTransparency(self, transparency):
        """
        SetTransparency(self: DirectContext3DHandleSettings, transparency: int)
            Sets the transparency value of the handle and the associated DirectContext3D 
             graphics.
        
        
            transparency: The transparency value to apply (in percentage)
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
        __new__(cls: type, other: DirectContext3DHandleSettings)
        __new__(cls: type, visibility: bool, transparency: int)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: DirectContext3DHandleSettings) -> bool

"""

    Visibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Visibility of the handle and the associated DirectContext3D graphics.
   A value of true means that the graphics are visible.

Get: Visibility(self: DirectContext3DHandleSettings) -> bool

Set: Visibility(self: DirectContext3DHandleSettings) = value
"""



class DrawContext(object):
    """ A class that provides drawing functionality for use by Autodesk.Revit.DB.DirectContext3D.IDirectContext3DServer servers """
    @staticmethod
    def FlushBuffer(vertexBuffer, vertexCount, indexBuffer, indexCount, vertexFormat, effectInstance, primitiveType, start, primitiveCount):
        """
        FlushBuffer(vertexBuffer: VertexBuffer, vertexCount: int, indexBuffer: IndexBuffer, indexCount: int, vertexFormat: VertexFormat, effectInstance: EffectInstance, primitiveType: PrimitiveType, start: int, primitiveCount: int)
            Submits geometry for rendering.
        
            vertexBuffer: The vertex buffer that contains vertex data.
            vertexCount: The number of vertices in the vertex buffer.
            indexBuffer: The index buffer that contains indices into the vertex buffer.
            indexCount: The number of indices in the index buffer.
            vertexFormat: The format of the vertices in the vertex buffer.
            effectInstance: The effect instance to be used for drawing this piece of geometry.
            primitiveType: The type of geometry primitive used in the index buffer.
            start: The first index to use for drawing.
            primitiveCount: The number of primitives to draw.
        """
        pass

    @staticmethod
    def GetCamera():
        """
        GetCamera() -> Camera
        
            Gets the camera corresponding to the Revit view where rendering takes place.
            Returns: The camera.
        """
        pass

    @staticmethod
    def GetClipPlanes():
        """
        GetClipPlanes() -> IList[ClipPlane]
        
            Gets the clipping planes for the Revit view where rendering takes place.
           
             Clipping planes control the 3D extent of a view and can be set using Section 
             Box in Revit.
        
            Returns: The array of clipping planes, which is empty if none are set.
        """
        pass

    @staticmethod
    def GetClipRectangle():
        """
        GetClipRectangle() -> Rectangle
        
            Gets the clip rectangle for the Revit view where rendering takes place. The 
             clip rectangle
           is the area currently being redrawn, which may be smaller 
             than the view rectangle.
        
            Returns: The clip rectangle.
        """
        pass

    @staticmethod
    def GetOverrideColor(color):
        """
        GetOverrideColor() -> (bool, Color)
        
            Returns override color that will be applied to geometry during rendering.
        """
        pass

    @staticmethod
    def GetOverrideTransparency(transparency):
        """
        GetOverrideTransparency() -> (bool, float)
        
            Returns override transparency that will be applied to geometry during rendering.
        """
        pass

    @staticmethod
    def GetViewRectangle():
        """
        GetViewRectangle() -> Rectangle
        
            Gets the rectangle that represents the extent (in 2D) of the Revit view where 
             rendering takes place.
        
            Returns: The view rectangle.
        """
        pass

    @staticmethod
    def IsAvailable():
        """
        IsAvailable() -> bool
        
            Checks whether the facilities of this class are available for use in the 
             current scope.
        
            Returns: True if the DrawContext is available for rendering, false otherwise.
        """
        pass

    @staticmethod
    def IsInterrupted():
        """
        IsInterrupted() -> bool
        
            Checks whether the current rendering pass has been interrupted.
            Returns: True if the current rendering pass has been interrupted before its completion, 
             false otherwise.
        """
        pass

    @staticmethod
    def IsTransparentPass():
        """
        IsTransparentPass() -> bool
        
            Determines whether the current rendering pass is for transparent objects.
            Returns: True when the server should be submitting transparent objects for rendering, 
             false otherwise.
        """
        pass

    @staticmethod
    def SetWorldTransform(trf):
        """
        SetWorldTransform(trf: Transform)
            Sets the world transformation that will be applied to geometry during rendering.
        
            trf: The transformation matrix.
        """
        pass

    __all__ = [
        'FlushBuffer',
        'GetCamera',
        'GetClipPlanes',
        'GetClipRectangle',
        'GetOverrideColor',
        'GetOverrideTransparency',
        'GetViewRectangle',
        'IsAvailable',
        'IsInterrupted',
        'IsTransparentPass',
        'SetWorldTransform',
    ]


class EffectInstance(object, IDisposable):
    """
    An effect instance that controls the appearance of geometry.
    
    EffectInstance(vertexFormatBits: VertexFormatBits)
    """
    def Dispose(self):
        """ Dispose(self: EffectInstance) """
        pass

    def IsValid(self):
        """
        IsValid(self: EffectInstance) -> bool
        
            Tests whether the effect instance is valid for rendering.
            Returns: True if the effect instance is valid for rendering, false otherwise.
        """
        pass

    def MatchesFormat(self, vertexFormat):
        """
        MatchesFormat(self: EffectInstance, vertexFormat: VertexFormat) -> bool
        
            Tests whether the effect instance is appropriate for the given vertex format.
        
            vertexFormat: A vertex format.
            Returns: True if the effect instance is valid for use with the specified vertex format.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: EffectInstance, disposing: bool) """
        pass

    def SetAmbientColor(self, color):
        """
        SetAmbientColor(self: EffectInstance, color: Color)
            Sets the ambient color parameter of the effect instance.
        
            color: The ambient color value.
        """
        pass

    def SetColor(self, color):
        """
        SetColor(self: EffectInstance, color: Color)
            Sets the color parameter of the effect instance.
        
            color: The color value.
        """
        pass

    def SetDiffuseColor(self, color):
        """
        SetDiffuseColor(self: EffectInstance, color: Color)
            Sets the diffuse color parameter of the effect instance.
        
            color: The diffuse color value.
        """
        pass

    def SetEmissiveColor(self, color):
        """
        SetEmissiveColor(self: EffectInstance, color: Color)
            Sets the emissive color parameter of the effect instance.
        
            color: The emissive color value.
        """
        pass

    def SetGlossiness(self, glossiness):
        """
        SetGlossiness(self: EffectInstance, glossiness: float)
            Sets the glossiness parameter of the effect instance.
        
            glossiness: The glossiness value.
        """
        pass

    def SetSpecularColor(self, color):
        """
        SetSpecularColor(self: EffectInstance, color: Color)
            Sets the specular color parameter of the effect instance.
        
            color: The specular color value.
        """
        pass

    def SetTransparency(self, transparency):
        """
        SetTransparency(self: EffectInstance, transparency: float)
            Sets the transparency parameter of the effect instance.
        
            transparency: The transparency value.
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
    def __new__(self, vertexFormatBits):
        """ __new__(cls: type, vertexFormatBits: VertexFormatBits) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: EffectInstance) -> bool

"""



class IDirectContext3DServer(IExternalServer):
    """ The interface to be implemented by a server of the DirectContext3D external service. """
    def CanExecute(self, dBView):
        """
        CanExecute(self: IDirectContext3DServer, dBView: View) -> bool
        
            Can be used to allow the server to execute only in certain views.
        
            dBView: The view where rendering will occur.
            Returns: True if the server can be executed in the provided view, false otherwise.
        """
        pass

    def GetApplicationId(self):
        """
        GetApplicationId(self: IDirectContext3DServer) -> str
        
            Reports this server's application ID.
            Returns: The application ID.
        """
        pass

    def GetBoundingBox(self, dBView):
        """
        GetBoundingBox(self: IDirectContext3DServer, dBView: View) -> Outline
        
            Reports a bounding box of the geometry that this server submits for drawing.
        
            dBView: The view where rendering will occur. If this argument is ll, a view-independent 
             bounding box should be reported.
        
            Returns: The bounding box as an Outline.
        """
        pass

    def GetSourceId(self):
        """
        GetSourceId(self: IDirectContext3DServer) -> str
        
            Reports this server's source ID.
            Returns: The source ID.
        """
        pass

    def RenderScene(self, dBView, displayStyle):
        """
        RenderScene(self: IDirectContext3DServer, dBView: View, displayStyle: DisplayStyle)
            Performs rendering of the scene that the server creates.
        
            dBView: The view where rendering will occur.
            displayStyle: The display style of the view in which the submitted geometry will be drawn.
        """
        pass

    def UseInTransparentPass(self, dBView):
        """
        UseInTransparentPass(self: IDirectContext3DServer, dBView: View) -> bool
        
            Indicates whether this server will submit geometry during the rendering pass 
             for transparent geometry.
        
        
            dBView: The view where rendering will occur.
            Returns: True if the server needs to render transparent geometry, false otherwise.
        """
        pass

    def UsesHandles(self):
        """
        UsesHandles(self: IDirectContext3DServer) -> bool
        
            Tests whether this server uses DirectContext3D handle elements.
            Returns: True if the server needs to use DirectContext3D handle elements, false 
             otherwise.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IndexBuffer(object, IDisposable):
    """
    A buffer that stores vertex indices for rendering.
    
    IndexBuffer(sizeInShortInts: int)
    """
    def Dispose(self):
        """ Dispose(self: IndexBuffer) """
        pass

    def GetIndexStreamLine(self):
        """
        GetIndexStreamLine(self: IndexBuffer) -> IndexStreamLine
        
            Gets a stream that can be used to write 
             Autodesk.Revit.DB.DirectContext3D.IndexLine segment primitives into the buffer.
        
            Returns: The stream that can be used to write into this buffer.
        """
        pass

    def GetIndexStreamPoint(self):
        """
        GetIndexStreamPoint(self: IndexBuffer) -> IndexStreamPoint
        
            Gets a stream that can be used to write 
             Autodesk.Revit.DB.DirectContext3D.IndexPoint primitives into the buffer.
        
            Returns: The stream that can be used to write into this buffer.
        """
        pass

    def GetIndexStreamTriangle(self):
        """
        GetIndexStreamTriangle(self: IndexBuffer) -> IndexStreamTriangle
        
            Gets a stream that can be used to write 
             Autodesk.Revit.DB.DirectContext3D.IndexTriangle primitives into the buffer.
        
            Returns: The stream that can be used to write into this buffer.
        """
        pass

    def GetMappedHandle(self):
        """
        GetMappedHandle(self: IndexBuffer) -> IntPtr
        
            Gets a handle to the buffer's memory that has been mapped. Writing data to the 
             buffer using the handle is an alternative to using stream objects.
        
            Returns: The handle to the mapped memory or nullptr when the buffer is not mapped.
        """
        pass

    def IsValid(self):
        """
        IsValid(self: IndexBuffer) -> bool
        
            Tests whether the buffer is valid for rendering.
            Returns: True if the buffer is valid for rendering, false otherwise.
        """
        pass

    def Map(self, sizeInShortInts):
        """
        Map(self: IndexBuffer, sizeInShortInts: int)
            Maps a portion of the index buffer into memory, so that indices can be written 
             into it.
           see Autodesk.Revit.DB.DirectContext3D.IndexStream.
        
        
            sizeInShortInts: The size of the part of the buffer to be mapped, measured in short integers.
          
              Must be less than or equal to the size of the 
             Autodesk.Revit.DB.DirectContext3D.IndexBuffer
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: IndexBuffer, disposing: bool) """
        pass

    def Unmap(self):
        """
        Unmap(self: IndexBuffer)
            Unmaps the buffer so that it can be used for rendering.
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
    def __new__(self, sizeInShortInts):
        """ __new__(cls: type, sizeInShortInts: int) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: IndexBuffer) -> bool

"""



class IndexPrimitive(object, IDisposable):
    """ The base class for index buffer primitives. """
    def Dispose(self):
        """ Dispose(self: IndexPrimitive) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: IndexPrimitive, disposing: bool) """
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

Get: IsValidObject(self: IndexPrimitive) -> bool

"""



class IndexLine(IndexPrimitive, IDisposable):
    """
    A line segment primitive consisting of two indices.
    
    IndexLine(index0: int, index1: int)
    """
    def Dispose(self):
        """ Dispose(self: IndexPrimitive, A_0: bool) """
        pass

    @staticmethod
    def GetSizeInShortInts():
        """
        GetSizeInShortInts() -> int
        
            Gets the amount of storage that the primitive takes up in a buffer, measured in 
             short integers.
        
            Returns: The number of short integers occupied by the primitive.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: IndexPrimitive, disposing: bool) """
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
    def __new__(self, index0, index1):
        """ __new__(cls: type, index0: int, index1: int) """
        pass

    Index0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the line segment's first vertex.

Get: Index0(self: IndexLine) -> int

Set: Index0(self: IndexLine) = value
"""

    Index1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the line segment's second vertex.

Get: Index1(self: IndexLine) -> int

Set: Index1(self: IndexLine) = value
"""



class IndexPoint(IndexPrimitive, IDisposable):
    """
    A point primitive consisting of one index.
    
    IndexPoint(index: int)
    """
    def Dispose(self):
        """ Dispose(self: IndexPrimitive, A_0: bool) """
        pass

    @staticmethod
    def GetSizeInShortInts():
        """
        GetSizeInShortInts() -> int
        
            Gets the amount of storage that the primitive takes up in a buffer, measured in 
             short integers.
        
            Returns: The number of short integers occupied by the primitive.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: IndexPrimitive, disposing: bool) """
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
    def __new__(self, index):
        """ __new__(cls: type, index: int) """
        pass

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the point's vertex.

Get: Index(self: IndexPoint) -> int

Set: Index(self: IndexPoint) = value
"""



class IndexStream(object, IDisposable):
    """ The base class for DirectContext3D index streams, which are used to write vertex indices into buffers. """
    def Dispose(self):
        """ Dispose(self: IndexStream) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: IndexStream, disposing: bool) """
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

Get: IsValidObject(self: IndexStream) -> bool

"""



class IndexStreamLine(IndexStream, IDisposable):
    """
    A stream that can be used to write Autodesk.Revit.DB.DirectContext3D.IndexLine
       primitives into an Autodesk.Revit.DB.DirectContext3D.IndexBuffer
    """
    def AddLine(self, line):
        """
        AddLine(self: IndexStreamLine, line: IndexLine)
            Inserts a Autodesk.Revit.DB.DirectContext3D.IndexLine segment into the stream 
             and associated buffer.
        
        
            line: The line segment to be inserted.
        """
        pass

    def AddLines(self, lines):
        """ AddLines(self: IndexStreamLine, lines: IList[IndexLine]) """
        pass

    def Dispose(self):
        """ Dispose(self: IndexStream, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: IndexStream, disposing: bool) """
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


class IndexStreamPoint(IndexStream, IDisposable):
    """
    A stream that can be used to write Autodesk.Revit.DB.DirectContext3D.IndexPoint
       primitives into an Autodesk.Revit.DB.DirectContext3D.IndexBuffer
    """
    def AddPoint(self, point):
        """
        AddPoint(self: IndexStreamPoint, point: IndexPoint)
            Inserts a Autodesk.Revit.DB.DirectContext3D.IndexPoint into the stream and 
             associated buffer.
        
        
            point: The point to be inserted.
        """
        pass

    def AddPoints(self, points):
        """ AddPoints(self: IndexStreamPoint, points: IList[IndexPoint]) """
        pass

    def Dispose(self):
        """ Dispose(self: IndexStream, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: IndexStream, disposing: bool) """
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


class IndexStreamTriangle(IndexStream, IDisposable):
    """
    A stream that can be used to write Autodesk.Revit.DB.DirectContext3D.IndexTriangle
       primitives into an Autodesk.Revit.DB.DirectContext3D.IndexBuffer
    """
    def AddTriangle(self, triangle):
        """
        AddTriangle(self: IndexStreamTriangle, triangle: IndexTriangle)
            Inserts a Autodesk.Revit.DB.DirectContext3D.IndexTriangle into the stream and 
             associated buffer.
        
        
            triangle: The triangle to be inserted.
        """
        pass

    def AddTriangles(self, triangles):
        """ AddTriangles(self: IndexStreamTriangle, triangles: IList[IndexTriangle]) """
        pass

    def Dispose(self):
        """ Dispose(self: IndexStream, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: IndexStream, disposing: bool) """
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


class IndexTriangle(IndexPrimitive, IDisposable):
    """
    A triangle primitive consisting of three indices.
    
    IndexTriangle(index0: int, index1: int, index2: int)
    """
    def Dispose(self):
        """ Dispose(self: IndexPrimitive, A_0: bool) """
        pass

    @staticmethod
    def GetSizeInShortInts():
        """
        GetSizeInShortInts() -> int
        
            Gets the amount of storage that the primitive takes up in a buffer, measured in 
             short integers.
        
            Returns: The number of short integers occupied by the primitive.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: IndexPrimitive, disposing: bool) """
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
    def __new__(self, index0, index1, index2):
        """ __new__(cls: type, index0: int, index1: int, index2: int) """
        pass

    Index0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the triangle's first vertex.

Get: Index0(self: IndexTriangle) -> int

Set: Index0(self: IndexTriangle) = value
"""

    Index1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the triangle's second vertex.

Get: Index1(self: IndexTriangle) -> int

Set: Index1(self: IndexTriangle) = value
"""

    Index2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the triangle's third vertex.

Get: Index2(self: IndexTriangle) -> int

Set: Index2(self: IndexTriangle) = value
"""



class PrimitiveType(Enum, IComparable, IFormattable, IConvertible):
    """
    Type of geometry primitive represented as a number.
    
    enum PrimitiveType, values: LineList (1), PointList (2), TriangleList (0)
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

    LineList = None
    PointList = None
    TriangleList = None
    value__ = None


class ProjectionMethod(Enum, IComparable, IFormattable, IConvertible):
    """
    Projection method
    
    enum ProjectionMethod, values: Orthographic (0), Perspective (1)
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

    Orthographic = None
    Perspective = None
    value__ = None


class Vertex(object, IDisposable):
    """ The base class for DirectContext3D vertices. """
    def Dispose(self):
        """ Dispose(self: Vertex) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Vertex, disposing: bool) """
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

Get: IsValidObject(self: Vertex) -> bool

"""



class VertexBuffer(object, IDisposable):
    """
    A buffer that stores vertex data for rendering.
    
    VertexBuffer(sizeInFloats: int)
    """
    def Dispose(self):
        """ Dispose(self: VertexBuffer) """
        pass

    def GetMappedHandle(self):
        """
        GetMappedHandle(self: VertexBuffer) -> IntPtr
        
            Gets a handle to the buffer's memory that has been mapped. Writing data to the 
             buffer using the handle is an alternative to using stream objects.
        
            Returns: The handle to the mapped memory or nullptr when the buffer is not mapped.
        """
        pass

    def GetVertexStreamPosition(self):
        """
        GetVertexStreamPosition(self: VertexBuffer) -> VertexStreamPosition
        
            Gets a stream that can be used to write vertices of type 
             Autodesk.Revit.DB.DirectContext3D.VertexPosition into the buffer.
        
            Returns: The stream that can be used to write into this buffer.
        """
        pass

    def GetVertexStreamPositionColored(self):
        """
        GetVertexStreamPositionColored(self: VertexBuffer) -> VertexStreamPositionColored
        
            Gets a stream that can be used to write vertices of type 
             Autodesk.Revit.DB.DirectContext3D.VertexPositionColored into the buffer.
        
            Returns: The stream that can be used to write into this buffer.
        """
        pass

    def GetVertexStreamPositionNormal(self):
        """
        GetVertexStreamPositionNormal(self: VertexBuffer) -> VertexStreamPositionNormal
        
            Gets a stream that can be used to write vertices of type 
             Autodesk.Revit.DB.DirectContext3D.VertexPositionNormal into the buffer.
        
            Returns: The stream that can be used to write into this buffer.
        """
        pass

    def GetVertexStreamPositionNormalColored(self):
        """
        GetVertexStreamPositionNormalColored(self: VertexBuffer) -> VertexStreamPositionNormalColored
        
            Gets a stream that can be used to write vertices of type 
             Autodesk.Revit.DB.DirectContext3D.VertexPositionNormalColored into the buffer.
        
            Returns: The stream that can be used to write into this buffer.
        """
        pass

    def IsValid(self):
        """
        IsValid(self: VertexBuffer) -> bool
        
            Tests whether the buffer is valid for rendering.
            Returns: True if the buffer is valid for rendering, false otherwise.
        """
        pass

    def Map(self, sizeInFloats):
        """
        Map(self: VertexBuffer, sizeInFloats: int)
            Maps a portion of the buffer into memory, so that vertex data can be written 
             into it.
           (see Autodesk.Revit.DB.DirectContext3D.VertexStream).
        
        
            sizeInFloats: The size of the part of the buffer to be mapped, measured in floats.
           Must 
             be less than or equal to the size of the 
             Autodesk.Revit.DB.DirectContext3D.VertexBuffer
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: VertexBuffer, disposing: bool) """
        pass

    def Unmap(self):
        """
        Unmap(self: VertexBuffer)
            Unmaps the buffer, so that it can be used for rendering.
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
    def __new__(self, sizeInFloats):
        """ __new__(cls: type, sizeInFloats: int) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: VertexBuffer) -> bool

"""



class VertexFormat(object, IDisposable):
    """
    A specification of the format of vertex data contained in a piece of geometry.
    
    VertexFormat(vertexFormatBits: VertexFormatBits)
    """
    def Dispose(self):
        """ Dispose(self: VertexFormat) """
        pass

    def IsValid(self):
        """
        IsValid(self: VertexFormat) -> bool
        
            Tests whether the vertex format specification is valid for rendering.
            Returns: True if the vertex format specification is valid for rendering, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: VertexFormat, disposing: bool) """
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
    def __new__(self, vertexFormatBits):
        """ __new__(cls: type, vertexFormatBits: VertexFormatBits) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: VertexFormat) -> bool

"""



class VertexFormatBits(Enum, IComparable, IFormattable, IConvertible):
    """
    Vertex format (i.e., the type of data associated with a vertex) represented as a number.
    
    enum VertexFormatBits, values: Position (1), PositionColored (5), PositionNormal (3), PositionNormalColored (7)
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

    Position = None
    PositionColored = None
    PositionNormal = None
    PositionNormalColored = None
    value__ = None


class VertexPosition(Vertex, IDisposable):
    """
    A geometry vertex specified as a position in space.
    
    VertexPosition(position: XYZ)
    """
    def Dispose(self):
        """ Dispose(self: Vertex, A_0: bool) """
        pass

    @staticmethod
    def GetSizeInFloats():
        """
        GetSizeInFloats() -> int
        
            Gets the amount of storage that the vertex takes up in a buffer, measured in 
             floats.
        
            Returns: The number of floats occupied by one vertex of this type.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Vertex, disposing: bool) """
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
    def __new__(self, position):
        """ __new__(cls: type, position: XYZ) """
        pass

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The vertex's position.

Get: Position(self: VertexPosition) -> XYZ

Set: Position(self: VertexPosition) = value
"""



class VertexPositionColored(Vertex, IDisposable):
    """
    A geometry vertex specified as a position in space with a color.
    
    VertexPositionColored(position: XYZ, color: ColorWithTransparency)
    """
    def Dispose(self):
        """ Dispose(self: Vertex, A_0: bool) """
        pass

    def GetColor(self):
        """
        GetColor(self: VertexPositionColored) -> ColorWithTransparency
        
            Gets the vertex's color.
            Returns: The vertex's color.
        """
        pass

    @staticmethod
    def GetSizeInFloats():
        """
        GetSizeInFloats() -> int
        
            Gets the amount of storage that the vertex takes up in a buffer, measured in 
             floats.
        
            Returns: The number of floats occupied by one vertex of this type.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Vertex, disposing: bool) """
        pass

    def SetColor(self, color):
        """
        SetColor(self: VertexPositionColored, color: ColorWithTransparency)
            Sets the vertex's color.
        
            color: The vertex's color.
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
    def __new__(self, position, color):
        """ __new__(cls: type, position: XYZ, color: ColorWithTransparency) """
        pass

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The vertex's position.

Get: Position(self: VertexPositionColored) -> XYZ

Set: Position(self: VertexPositionColored) = value
"""



class VertexPositionNormal(Vertex, IDisposable):
    """
    A geometry vertex specified as a position in space with a normal vector.
    
    VertexPositionNormal(position: XYZ, normal: XYZ)
    """
    def Dispose(self):
        """ Dispose(self: Vertex, A_0: bool) """
        pass

    @staticmethod
    def GetSizeInFloats():
        """
        GetSizeInFloats() -> int
        
            Gets the amount of storage that the vertex takes up in a buffer, measured in 
             floats.
        
            Returns: The number of floats occupied by one vertex of this type.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Vertex, disposing: bool) """
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
    def __new__(self, position, normal):
        """ __new__(cls: type, position: XYZ, normal: XYZ) """
        pass

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The vertex's normal vector.

Get: Normal(self: VertexPositionNormal) -> XYZ

Set: Normal(self: VertexPositionNormal) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The vertex's position.

Get: Position(self: VertexPositionNormal) -> XYZ

Set: Position(self: VertexPositionNormal) = value
"""



class VertexPositionNormalColored(Vertex, IDisposable):
    """
    A geometry vertex specified as a position in space with a normal vector and a color.
    
    VertexPositionNormalColored(position: XYZ, normal: XYZ, color: ColorWithTransparency)
    """
    def Dispose(self):
        """ Dispose(self: Vertex, A_0: bool) """
        pass

    def GetColor(self):
        """
        GetColor(self: VertexPositionNormalColored) -> ColorWithTransparency
        
            Gets the vertex's color.
            Returns: The vertex's color.
        """
        pass

    @staticmethod
    def GetSizeInFloats():
        """
        GetSizeInFloats() -> int
        
            Gets the amount of storage that the vertex takes up in a buffer, measured in 
             floats.
        
            Returns: The number of floats occupied by one vertex of this type.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Vertex, disposing: bool) """
        pass

    def SetColor(self, color):
        """
        SetColor(self: VertexPositionNormalColored, color: ColorWithTransparency)
            Sets the vertex's color.
        
            color: The vertex's color.
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
    def __new__(self, position, normal, color):
        """ __new__(cls: type, position: XYZ, normal: XYZ, color: ColorWithTransparency) """
        pass

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The vertex's normal vector.

Get: Normal(self: VertexPositionNormalColored) -> XYZ

Set: Normal(self: VertexPositionNormalColored) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The vertex's position.

Get: Position(self: VertexPositionNormalColored) -> XYZ

Set: Position(self: VertexPositionNormalColored) = value
"""



class VertexStream(object, IDisposable):
    """ The base class for DirectContext3D vertex streams, which are used to write vertex data into buffers. """
    def Dispose(self):
        """ Dispose(self: VertexStream) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: VertexStream, disposing: bool) """
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

Get: IsValidObject(self: VertexStream) -> bool

"""



class VertexStreamPosition(VertexStream, IDisposable):
    """
    A stream that can be used to write vertices of type Autodesk.Revit.DB.DirectContext3D.VertexPosition
       into a buffer (see Autodesk.Revit.DB.DirectContext3D.VertexBuffer).
    """
    def AddVertex(self, vertex):
        """
        AddVertex(self: VertexStreamPosition, vertex: VertexPosition)
            Inserts a Autodesk.Revit.DB.DirectContext3D.VertexStreamPosition into the 
             stream and associated buffer.
        
        
            vertex: The vertex to be inserted.
        """
        pass

    def AddVertices(self, vertices):
        """ AddVertices(self: VertexStreamPosition, vertices: IList[VertexPosition]) """
        pass

    def Dispose(self):
        """ Dispose(self: VertexStream, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: VertexStream, disposing: bool) """
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


class VertexStreamPositionColored(VertexStream, IDisposable):
    """
    A stream that can be used to write vertices of type Autodesk.Revit.DB.DirectContext3D.VertexPositionColored
       into a buffer (see Autodesk.Revit.DB.DirectContext3D.VertexBuffer).
    """
    def AddVertex(self, vertex):
        """
        AddVertex(self: VertexStreamPositionColored, vertex: VertexPositionColored)
            Inserts a Autodesk.Revit.DB.DirectContext3D.VertexStreamPositionColored into 
             the stream and associated buffer.
        
        
            vertex: The vertex to be inserted.
        """
        pass

    def AddVertices(self, vertices):
        """ AddVertices(self: VertexStreamPositionColored, vertices: IList[VertexPositionColored]) """
        pass

    def Dispose(self):
        """ Dispose(self: VertexStream, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: VertexStream, disposing: bool) """
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


class VertexStreamPositionNormal(VertexStream, IDisposable):
    """
    A stream that can be used to write vertices of type Autodesk.Revit.DB.DirectContext3D.VertexPositionNormal
       into a buffer (see Autodesk.Revit.DB.DirectContext3D.VertexBuffer).
    """
    def AddVertex(self, vertex):
        """
        AddVertex(self: VertexStreamPositionNormal, vertex: VertexPositionNormal)
            Inserts a Autodesk.Revit.DB.DirectContext3D.VertexStreamPositionNormal into the 
             stream and associated buffer.
        
        
            vertex: The vertex to be inserted.
        """
        pass

    def AddVertices(self, vertices):
        """ AddVertices(self: VertexStreamPositionNormal, vertices: IList[VertexPositionNormal]) """
        pass

    def Dispose(self):
        """ Dispose(self: VertexStream, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: VertexStream, disposing: bool) """
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


class VertexStreamPositionNormalColored(VertexStream, IDisposable):
    """
    A stream that can be used to write vertices of type Autodesk.Revit.DB.DirectContext3D.VertexPositionNormalColored
       into a buffer (see Autodesk.Revit.DB.DirectContext3D.VertexBuffer).
    """
    def AddVertex(self, vertex):
        """
        AddVertex(self: VertexStreamPositionNormalColored, vertex: VertexPositionNormalColored)
            Inserts a Autodesk.Revit.DB.DirectContext3D.VertexStreamPositionNormalColored 
             into the stream and associated buffer.
        
        
            vertex: The vertex to be inserted.
        """
        pass

    def AddVertices(self, vertices):
        """ AddVertices(self: VertexStreamPositionNormalColored, vertices: IList[VertexPositionNormalColored]) """
        pass

    def Dispose(self):
        """ Dispose(self: VertexStream, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: VertexStream, disposing: bool) """
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


