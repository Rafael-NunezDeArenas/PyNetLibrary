# encoding: utf-8
# module Autodesk.Navisworks.Api.Automation calls itself Automation
# from Autodesk.Navisworks.Automation, Version=19.0.1374.1, Culture=neutral, PublicKeyToken=d85e58fa5af9b484
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AutomationDocumentFileException(Exception, ISerializable, _Exception):
    """
    Automation equivalent of DocumentFileException
    
    AutomationDocumentFileException(message: str, innerException: Exception)
    AutomationDocumentFileException(message: str)
    AutomationDocumentFileException()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, message: str)
        __new__(cls: type)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class AutomationException(Exception, ISerializable, _Exception):
    """
    Specific Exception that is thrown by the .NET Automation parts of the API when there is a general failure of Automation
    
    AutomationException(message: str, innerException: Exception)
    AutomationException(message: str)
    AutomationException()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, message: str)
        __new__(cls: type)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class NavisworksApplication(object, IDisposable):
    """
    Provides the same interface as Autodesk.Navisworks.Api.ApplicationParts.ApplicationAutomation but via Automation.
    Calls made via this class eventually call methods on Autodesk.Navisworks.Api.ApplicationParts.ApplicationAutomation.
    
    NavisworksApplication()
    """
    def AddPluginAssembly(self, fileName):
        """
        AddPluginAssembly(self: NavisworksApplication, fileName: str)
            Adds another assembly that plugins can be loaded from.
        Assembly is loaded using the LoadFrom context and can be outside the Application root.
        
            fileName: The file name of the assembly
        """
        pass

    def AppendFile(self, fileName):
        """
        AppendFile(self: NavisworksApplication, fileName: str)
            Appends a Navisworks supported files to the currently loaded file
        
            fileName: The file name including extension
        """
        pass

    def CreateCache(self, fileNameToCache):
        """
        CreateCache(self: NavisworksApplication, fileNameToCache: str)
            Creates a corresponding nwc file for specified file.
        """
        pass

    def DisableProgress(self):
        """
        DisableProgress(self: NavisworksApplication)
            Normal behavior is that Progress is displayed when performing long operations, even during Automated actions.
         Calling this method changes behaviour such that Progress is not 
             displayed in such cirmumstances.
        """
        pass

    def Dispose(self):
        """ Dispose(self: NavisworksApplication) """
        pass

    def EnableProgress(self):
        """
        EnableProgress(self: NavisworksApplication)
            Normal behavior is that Progress is displayed when performing long operations, even during Automated actions.
        This may have been overriden by using 
             Autodesk.Navisworks.Api.Automation.NavisworksApplication.DisableProgressDisableProgress,
        If so then calling this method will reinstate normal behavior.
        """
        pass

    def ExecuteAddInPlugin(self, pluginId, parameters):
        """
        ExecuteAddInPlugin(self: NavisworksApplication, pluginId: str, *parameters: Array[str]) -> int
        
            Executes an Addin Plugin whose full name is given by pluginId, passing in the paramaters given.
        
            pluginId: The full identifier for the plugin. This is formed as 
        PluginRecord::Name.PluginRecord::DeveloperId
            parameters: Optional parameters to pass to the plugin
        """
        pass

    @staticmethod
    def GetRunningInstance():
        """
        GetRunningInstance() -> NavisworksApplication
        
            Gets hold of currently running instance of the Application.
            Returns: The running Autodesk.Navisworks.Api.Automation.NavisworksApplicationNavisworksApplication.
        """
        pass

    def OpenFile(self, fileName, moreFiles):
        """
        OpenFile(self: NavisworksApplication, fileName: str, *moreFiles: Array[str])
            Loads one or more Navisworks supported files
        
            fileName: first file to load
        """
        pass

    def Print(self, printer=None, driver=None, port=None):
        """
        Print(self: NavisworksApplication, printer: str, driver: str, port: str)
            Sends the current View to the Printer
        
            printer: The name of the printer to print to
            driver: The name of the printer driver to use
            port: The name of the port the printer is connected to
        Print(self: NavisworksApplication, printer: str, driver: str)
            Sends the current View to the Printer
        
            printer: The name of the printer to print to
            driver: The name of the printer driver to use
        Print(self: NavisworksApplication, printer: str)
            Sends the current View to the Printer
        
            printer: The name of the printer to print to
        Print(self: NavisworksApplication)
            Sends the current View to the Printer
        """
        pass

    def SaveFile(self, fileName):
        """
        SaveFile(self: NavisworksApplication, fileName: str)
            Save the documents loaded using Autodesk.Navisworks.Api.Automation.NavisworksApplication.OpenFile(System.String,System.String[])OpenFile to a single Navisworks Document
        
            fileName: The file name including extension
        """
        pass

    def StayOpen(self):
        """
        StayOpen(self: NavisworksApplication)
            Normal behaviour is that the instance of Navisworks closes when the NavisworksApplication is Disposed or Finalized.
        """
        pass

    @staticmethod
    def TryGetRunningInstance():
        """
        TryGetRunningInstance() -> NavisworksApplication
        
            Gets hold of currently running instance of the Application.
            Returns: The running Autodesk.Navisworks.Api.Automation.NavisworksApplicationNavisworksApplication or null if there on failure.
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

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Controls whether the Navisworks application GUI is visible

Get: Visible(self: NavisworksApplication) -> bool

Set: Visible(self: NavisworksApplication) = value
"""



