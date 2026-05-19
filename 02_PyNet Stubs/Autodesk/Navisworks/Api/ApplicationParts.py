# encoding: utf-8
# module Autodesk.Navisworks.Api.ApplicationParts calls itself ApplicationParts
# from Autodesk.Navisworks.Api, Version=19.0.1374.1, Culture=neutral, PublicKeyToken=d85e58fa5af9b484
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ApplicationAutomation(object):
    """
    Provides the same interface as Api.Automation.NavisworksApplication but within the current process.
    Calls made via NavisworksApplication or command line when automating eventually call methods
    on here.
    """
    def AddPluginAssembly(self, fileName):
        """
        AddPluginAssembly(self: ApplicationAutomation, fileName: str)
            Adds another assembly that plugins can be loaded from.
        Assembly is loaded using the LoadFrom context and can be used outside the Application root.
        """
        pass

    def AppendFile(self, fileName):
        """
        AppendFile(self: ApplicationAutomation, fileName: str)
            Appends the Navisworks supported file to the currently loaded document
        
            fileName: The file name including extension
        """
        pass

    def CreateCache(self, fileNameToCache):
        """
        CreateCache(self: ApplicationAutomation, fileNameToCache: str)
            Creates a corresponding nwc file for specified file.
        
            fileNameToCache: The file name, excluding extension, for the cache file
        """
        pass

    def DisableProgress(self):
        """
        DisableProgress(self: ApplicationAutomation)
            Normal behavior is that Progress is displayed when performing long operations, even during Automated actions.
        """
        pass

    def EnableProgress(self):
        """
        EnableProgress(self: ApplicationAutomation)
            Normal behavior is that Progress is displayed when performing long operations, even during Automated actions.
        """
        pass

    def ExecuteAddInPlugin(self, pluginId, parameters):
        """
        ExecuteAddInPlugin(self: ApplicationAutomation, pluginId: str, *parameters: Array[str]) -> int
        
            Executes an Addin Plugin whose full name is given by pluginId, passing in the paramaters given.
        
            pluginId: The full identifier for the plugin.
        This is formed as Autodesk.Navisworks.Api.Plugins.PluginRecord.NameName.Autodesk.Navisworks.Api.Plugins.PluginRecord.DeveloperIdDeveloperId
            parameters: Optional parameters to pass to the plugin
        """
        pass

    def GenerateThumbnail(self, width, height, fileName):
        """
        GenerateThumbnail(self: ApplicationAutomation, width: int, height: int, fileName: str)
            Generates a Thumbnail Image for this Document, and save it as a PNG image
        
            width: The width of the image
            height: The height of the image
            fileName: The file name of the saved image
        """
        pass

    def GenerateThumbnailByRayTrace(self, width, height, fileName):
        """
        GenerateThumbnailByRayTrace(self: ApplicationAutomation, width: int, height: int, fileName: str)
            Generates a thumbnail render by ray trace for this Document, and save it as a PNG image
        
            width: The width of the image
            height: The height of the image
            fileName: The file name of the saved image
        """
        pass

    def OpenFile(self, fileName, moreFiles):
        """
        OpenFile(self: ApplicationAutomation, fileName: str, *moreFiles: Array[str])
            Loads one or more Navisworks supported files
        
            fileName: First file to open
            moreFiles: Other files to open
        """
        pass

    def Print(self, printer=None, driver=None, port=None):
        """
        Print(self: ApplicationAutomation, printer: str, driver: str, port: str)
            Sends the current View to the Printer
        
            printer: The name of the printer to print to
            driver: The name of the printer driver to use
            port: The name of the port the printer is connected to
        Print(self: ApplicationAutomation, printer: str, driver: str)
            Sends the current View to the Printer
        
            printer: The name of the printer to print to
            driver: The name of the printer driver to use
        Print(self: ApplicationAutomation, printer: str)
            Sends the current View to the Printer
        
            printer: The name of the printer to print to
        Print(self: ApplicationAutomation)
            Sends the current View to the Printer
        """
        pass

    def SaveFile(self, fileName):
        """
        SaveFile(self: ApplicationAutomation, fileName: str)
            Save the documents loaded using Autodesk.Navisworks.Api.ApplicationParts.ApplicationAutomation.OpenFile(System.String,System.String[])OpenFile to a single Navisworks Document
        
            fileName: The file name including extension
        """
        pass


class ApplicationDragDrop(object):
    """ Represents Application level Drag & Drop. """
    def DecodeData(self, data, processId):
        """
        DecodeData(self: ApplicationDragDrop, data: IDataObject) -> (bool, int)
        
            Tries to decode the data passed in drag drop operations.
        If successful determines the source Process Id.
        """
        pass

    def DecodeDataWpf(self, data, processId):
        """
        DecodeDataWpf(self: ApplicationDragDrop, data: IDataObject) -> (bool, int)
        
            Tries to decode the data passed in drag drop operations.
        If successful determines the source Process Id.
        """
        pass

    Format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of the format used for Navisworks drag drop operations.
Currently is just a notification theat Current Selection has been dragged.

Get: Format(self: ApplicationDragDrop) -> str

Set: Format(self: ApplicationDragDrop) = value
"""



class ApplicationOptions(object):
    """ Represents Application level options """
    Grids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides access to Autodesk.Navisworks.Api.GridsOptionsGrids Options.

Get: Grids(self: ApplicationOptions) -> GridsOptions

"""

    Stereo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides access to Autodesk.Navisworks.Api.StereoOptionsStereo Options.

Get: Stereo(self: ApplicationOptions) -> StereoOptions

"""



class ApplicationPlugins(object):
    """ Provides information about the Autodesk.Navisworks.Api.Plugins.PluginPlugins available in the application runtime """
    def AddPluginAssembly(self, fileName):
        """
        AddPluginAssembly(self: ApplicationPlugins, fileName: str)
            Adds another assembly that plugins can be loaded from.
        Assembly is loaded using the LoadFrom context and can be used outside the Application root.
        """
        pass

    def ExecuteAddInPlugin(self, pluginId, parameters):
        """
        ExecuteAddInPlugin(self: ApplicationPlugins, pluginId: str, *parameters: Array[str]) -> int
        
            Executes an Addin Plugin whose full name is given by pluginId, passing in the paramaters given.
        
            pluginId: The full identifier for the plugin.
        This is formed as Autodesk.Navisworks.Api.Plugins.PluginRecord.NameName.Autodesk.Navisworks.Api.Plugins.PluginRecord.DeveloperIdDeveloperId
            parameters: Optional parameters to pass to the plugin
        """
        pass

    def FindInterfaces(self, interfaceId):
        """
        FindInterfaces(self: ApplicationPlugins, interfaceId: str) -> ReadOnlyCollection[PluginRecord]
        
            Returns a collection of Autodesk.Navisworks.Api.Plugins.PluginRecordPluginRecords that implement a particular interface
        
            interfaceId: The Autodesk.Navisworks.Api.Plugins.InterfaceRecord.IdId of the Autodesk.Navisworks.Api.Plugins.InterfaceRecordInterfaceRecord
            Returns: Collection if empty if no mathcing Autodesk.Navisworks.Api.Plugins.PluginRecordPluginRecordsare found
        """
        pass

    def FindPlugin(self, pluginId):
        """
        FindPlugin(self: ApplicationPlugins, pluginId: str) -> PluginRecord
        
            Searches for a Autodesk.Navisworks.Api.Plugins.PluginRecordPluginRecord by Id
        
            pluginId: The full identifier for the plugin.
        This is formed as Autodesk.Navisworks.Api.Plugins.PluginRecord.NameName.Autodesk.Navisworks.Api.Plugins.PluginRecord.DeveloperIdDeveloperId
            Returns: Returns the Autodesk.Navisworks.Api.Plugins.PluginRecordPluginRecord or Null if it cannot be found
        """
        pass

    PluginRecords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets collection of Autodesk.Navisworks.Api.Plugins.PluginRecordPluginRecords that describe the available plugins

Get: PluginRecords(self: ApplicationPlugins) -> ReadOnlyCollection[PluginRecord]

"""


    PluginRecordsChanged = None
    PluginRecordsChanging = None


class ApplicationResources(object):
    """ Provides access to Application Resources """
    def GetString(self, name):
        """
        GetString(self: ApplicationResources, name: str) -> str
        
            Looks up a localizable string
        
            name: The identifier of the string to lookup
            Returns: Returns localized string
        """
        pass

    def GetStringSafe(self, name):
        """
        GetStringSafe(self: ApplicationResources, name: str) -> str
        
            Looks up a localizable string
        
            name: The identifier of the string to lookup
            Returns: Returns localized string or value of 'name' if it cannot be found
        """
        pass

    def TryGetString(self, name):
        """
        TryGetString(self: ApplicationResources, name: str) -> str
        
            Looks up a localizable string
        
            name: The identifier of the string to lookup
            Returns: Returns localized string or Null if it cannot be found
        """
        pass


class ApplicationVersion(object):
    """ Provides information about the version of the currently running API and Runtime """
    ApiMajor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Major version number for the Navisworks API.
Changes when a non-backwards compatible change is made to a stable version of the API.
Always less than or equal to Autodesk.Navisworks.Api.ApplicationParts.ApplicationVersion.RuntimeMajor.

Get: ApiMajor(self: ApplicationVersion) -> int

"""

    ApiMinor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Minor version number for the Navisworks API.
Changes when there is a behavioral or minor change to a stable version of the API
that may have an impact on backwards compatibility.
Always less than or equal to Autodesk.Navisworks.Api.ApplicationParts.ApplicationVersion.RuntimeMinor.

Get: ApiMinor(self: ApplicationVersion) -> int

"""

    Build = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Build number for Api and Runtime. Changes on every build (and hence every release).

Get: Build(self: ApplicationVersion) -> int

"""

    IsApiStable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this version of the API stable ? If false, breaking changes may be made at any time and client
code must be recompiled for every build. Api will be unstable for alpha and early beta releases.

Get: IsApiStable(self: ApplicationVersion) -> bool

"""

    IsRuntimeBeta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this an alpha or beta version of the runtime ?

Get: IsRuntimeBeta(self: ApplicationVersion) -> bool

"""

    Runtime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the Navisworks runtime that is providing this implementation of the API. Will typically
be an installed Navisworks product.

Get: Runtime(self: ApplicationVersion) -> str

"""

    RuntimeLanguage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the language code corresponding to the one Navisworks is using.

Get: RuntimeLanguage(self: ApplicationVersion) -> str

"""

    RuntimeMajor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Major version number for the current Navisworks Runtime.
This changes with every major (annual) release of Navisworks products.

Get: RuntimeMajor(self: ApplicationVersion) -> int

"""

    RuntimeMinor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Minor version number for the current Navisworks Runtime.
This changes with every minor (service pack or subscription release) update of Navisworks products.

Get: RuntimeMinor(self: ApplicationVersion) -> int

"""

    RuntimeProductName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The complete product name for the Navisworks runtime that is providing
this implementation of the API.

Get: RuntimeProductName(self: ApplicationVersion) -> str

"""



class IApplicationBim360:
    """ Provides access to the BIM360 state of the application which is hosting the API. """
    def GetRestApi(self, accountInfo):
        """
        GetRestApi(self: IApplicationBim360, accountInfo: AccountInfo) -> object
        
            Rest Api access.
        """
        pass

    def GetRestApiV3(self, accountInfo):
        """
        GetRestApiV3(self: IApplicationBim360, accountInfo: AccountInfo) -> object
        
            Rest Api access.
        """
        pass

    def ParseBim360Uri(self, input):
        """
        ParseBim360Uri(self: IApplicationBim360, input: str) -> ResourceInfo
        
            Attempts to parse a string as a BIM 360 URI, and then determines resource information.
        """
        pass

    def TryParseBim360Uri(self, input, uriInfo):
        """
        TryParseBim360Uri(self: IApplicationBim360, input: str) -> (bool, ResourceInfo)
        
            Attempts to parse a string as a BIM 360 URI, and then determines resource information.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Accounts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gives access to all current Accounts.
Youu'll only get these once SignedIn.

Get: Accounts(self: IApplicationBim360) -> Collection[AccountInfo]

"""

    HasAnyBim360ModelOpen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if any BIM 360 Models are loaded.

Get: HasAnyBim360ModelOpen(self: IApplicationBim360) -> bool

"""

    IsSignedIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """BIM 360 SignIn support.

Get: IsSignedIn(self: IApplicationBim360) -> bool

"""


    RefreshBeginning = None
    RefreshComplete = None


class IApplicationGui:
    """ Provides access to the Gui of the application which is hosting the API. """
    def CheckServiceEntitlement(self, rawServiceUrl):
        """
        CheckServiceEntitlement(self: IApplicationGui, rawServiceUrl: str) -> bool
        
            Checks a particular service entitlement.
        """
        pass

    def GetDockPanePluginVisibility(self, pluginId):
        """
        GetDockPanePluginVisibility(self: IApplicationGui, pluginId: str) -> bool
        
            Called when a DockPanePlugin gets it's Visible property
        
            pluginId: The full identifier for the plugin.
        This is formed as Autodesk.Navisworks.Api.Plugins.PluginRecord.NameName.Autodesk.Navisworks.Api.Plugins.PluginRecord.DeveloperIdDeveloperId
        """
        pass

    def IsSignedIn(self):
        """
        IsSignedIn(self: IApplicationGui) -> bool
        
            Reports if there is an authenticated user.
            Returns: Sign In status.
        """
        pass

    def SetDockPanePluginActive(self, pluginId):
        """
        SetDockPanePluginActive(self: IApplicationGui, pluginId: str)
            Called when a DockPanePlugin activates the plugin pane.
        
            pluginId: The full identifier for the plugin.
        This is formed as Autodesk.Navisworks.Api.Plugins.PluginRecord.NameName.Autodesk.Navisworks.Api.Plugins.PluginRecord.DeveloperIdDeveloperId
        """
        pass

    def SetDockPanePluginVisibility(self, pluginId, visible):
        """
        SetDockPanePluginVisibility(self: IApplicationGui, pluginId: str, visible: bool)
            Called when a DockPanePlugin sets it's Visible property
        
            pluginId: The full identifier for the plugin.
        This is formed as Autodesk.Navisworks.Api.Plugins.PluginRecord.NameName.Autodesk.Navisworks.Api.Plugins.PluginRecord.DeveloperIdDeveloperId
            visible: The value to set
        """
        pass

    def SetRaiseIdle(self, raiseIdle):
        """ SetRaiseIdle(self: IApplicationGui, raiseIdle: Action[EventArgs]) """
        pass

    def SignIn(self):
        """
        SignIn(self: IApplicationGui) -> bool
        
            Authenticate with Autodesk ID. Popup generic sign-in UI in Navisworks to allow users to enter the credentials.
            Returns: true if authenticated or false if failed to authenticate.
        """
        pass

    def SignOut(self):
        """
        SignOut(self: IApplicationGui) -> bool
        
            Sign-out the current authenticated user.
            Returns: true if succeeded or false if failed.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    MainWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the main window of the application. Use as parent window for dialogs and message boxes.

Get: MainWindow(self: IApplicationGui) -> IWin32Window

"""

    ServerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sign In server type.

Get: ServerType(self: IApplicationGui) -> ServerType

"""

    SignInUserId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The internal user ID of the user currently logged in. The user ID will be null if no user is logged in.

Get: SignInUserId(self: IApplicationGui) -> str

"""

    SignInUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current authenticated user's Autodesk ID.

Get: SignInUserName(self: IApplicationGui) -> str

"""


    Closed = None
    Closing = None
    ServerTypeChanged = None
    SignedIn = None
    SignedOut = None
    SigningOut = None


