# encoding: utf-8
# module Autodesk.Navisworks.Api.Plugins calls itself Plugins
# from Autodesk.Navisworks.Api, Version=19.0.1374.1, Culture=neutral, PublicKeyToken=d85e58fa5af9b484
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AddInLocation(Enum, IComparable, IFormattable, IConvertible):
    """
    Location of an Autodesk.Navisworks.Api.Plugins.AddInPluginAddInPlugin in the Navisworks menus system
    
    enum AddInLocation, values: AddIn (1), CurrentSelection2DContextMenu (6), CurrentSelectionContextMenu (5), Export (3), Help (4), Import (2), None (0)
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

    AddIn = None
    CurrentSelection2DContextMenu = None
    CurrentSelectionContextMenu = None
    Export = None
    Help = None
    Import = None
    None = None
    value__ = None


class Plugin(object):
    """ Base class for all plugins """
    def GetString(self, name):
        """
        GetString(self: Plugin, name: str) -> str
        
            Looks up a localizable string that is specific to this plugin
        
            name: The identifier of the string to lookup
            Returns: Returns localized string
        """
        pass

    def GetStringSafe(self, name):
        """
        GetStringSafe(self: Plugin, name: str) -> str
        
            Looks up a localizable string that is specific to this plugin
        
            name: The identifier of the string to lookup
            Returns: Returns localized string or value of 'name' if it cannot be found
        """
        pass

    def IsSelfEnabled(self, *args): #cannot find CLR method
        """
        IsSelfEnabled(self: Plugin) -> bool
        
            Called once to determines if the plugin is enabled.
        Only called if PluginRecord.SupportsIsSelfEnabled is true
        """
        pass

    def OnLoaded(self, *args): #cannot find CLR method
        """
        OnLoaded(self: Plugin)
            Called once immediately after the plugin has been loaded (created).
        Plugins are loaded on demand so this may be some time after application startup.
        Default implementation does 
             nothing.
        This is a good place to subscribe to API events.
        """
        pass

    def OnUnloading(self, *args): #cannot find CLR method
        """
        OnUnloading(self: Plugin)
            Called once just before the plugin is unloaded. If the plugin implements 
        System.IDisposableIDisposable, then
        Dispose will be called immediately after the plugin is unloaded.
        
             Plugins are typically unloaded at application shutdown or when the end user has disabled a plugin.
        Default implementation does nothing.
        This is a good place to unsubscribe from 
             API events.
        """
        pass

    def TryGetString(self, name):
        """
        TryGetString(self: Plugin, name: str) -> str
        
            Looks up a localizable string that is specific to this plugin
        
            name: The identifier of the string to lookup
            Returns: Returns localized string or Null if it cannot be found
        """
        pass

    DeveloperId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The 4 character ADN developer code or a GUID. The combination of this and Autodesk.Navisworks.Api.Plugins.Plugin.NameName should make the plugin unique

Get: DeveloperId(self: Plugin) -> str

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The full identifier for the plugin. This is formed as 
Autodesk.Navisworks.Api.Plugins.Plugin.NameName.Autodesk.Navisworks.Api.Plugins.Plugin.DeveloperIdDeveloperId

Get: Id(self: Plugin) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the Plugin. The combination of this and Autodesk.Navisworks.Api.Plugins.Plugin.DeveloperIdDeveloperId should make the plugin unique

Get: Name(self: Plugin) -> str

"""

    PluginRecord = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The PluginRecord that provides access to the attribute defined properties for this plugin.

Get: PluginRecord(self: Plugin) -> PluginRecord

"""



class AddInPlugin(Plugin):
    """
    A plugin that can be called either using the GUI, 
    Autodesk.Navisworks.Api.ApplicationParts.ApplicationAutomationApplicationAutomation
    or using the Automation .NET API
    """
    def CanExecute(self):
        """
        CanExecute(self: AddInPlugin) -> CommandState
        
            This is called to determine the state of plugin. 
        Primarily if Autodesk.Navisworks.Api.Plugins.AddInPlugin.Execute(System.String[])Execute can be called.
        """
        pass

    def Execute(self, parameters):
        """
        Execute(self: AddInPlugin, *parameters: Array[str]) -> int
        
            This method is called when the plugin is executed
        """
        pass

    def TryShowHelp(self):
        """
        TryShowHelp(self: AddInPlugin) -> bool
        
            Called to tell the plugin to display help
            Returns: Return true if you have handled this call
        """
        pass


class AddInPluginAttribute(Attribute, _Attribute):
    """
    Optional attribute for use with an Autodesk.Navisworks.Api.Plugins.AddInPluginAddInPlugin derived class.
    If this attribute is not used, the default location for an Autodesk.Navisworks.Api.Plugins.AddInPluginAddInPlugin is Autodesk.Navisworks.Api.Plugins.AddInLocationAddInLocation.AddIn
    
    AddInPluginAttribute(location: AddInLocation)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, location):
        """ __new__(cls: type, location: AddInLocation) """
        pass

    CallCanExecute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines the conditions in which CanExecuteCommand should be called.

Get: CallCanExecute(self: AddInPluginAttribute) -> CallCanExecute

Set: CallCanExecute(self: AddInPluginAttribute) = value
"""

    CanToggle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies if the command can toggle

Get: CanToggle(self: AddInPluginAttribute) -> bool

Set: CanToggle(self: AddInPluginAttribute) = value
"""

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The 16x16 icon to display for this command

Get: Icon(self: AddInPluginAttribute) -> str

Set: Icon(self: AddInPluginAttribute) = value
"""

    LargeIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The 32x32 icon to display for this command

Get: LargeIcon(self: AddInPluginAttribute) -> str

Set: LargeIcon(self: AddInPluginAttribute) = value
"""

    LoadForCanExecute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies if CanExecuteCommand should cause the Plugin to load

Get: LoadForCanExecute(self: AddInPluginAttribute) -> bool

Set: LoadForCanExecute(self: AddInPluginAttribute) = value
"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines where the plugin is displayed in Navisworks menus system

Get: Location(self: AddInPluginAttribute) -> AddInLocation

"""

    Shortcut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the keyboard shortcut for the command.

Get: Shortcut(self: AddInPluginAttribute) -> str

Set: Shortcut(self: AddInPluginAttribute) = value
"""

    ShortcutWindowTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Ids of the windows for which the shortcut is valid. 
Multiple Ids can be specified by separating with ";".
If Ids are specified the shortcut should be valid in all contexts.

Get: ShortcutWindowTypes(self: AddInPluginAttribute) -> str

Set: ShortcutWindowTypes(self: AddInPluginAttribute) = value
"""



class PluginRecord(object):
    """
    Metadata for a plugin that can be loaded into Navisworks. 
        """
    def FindInterfaceRecord(self, interfaceId):
        """
        FindInterfaceRecord(self: PluginRecord, interfaceId: str) -> InterfaceRecord
        
            Finds an Autodesk.Navisworks.Api.Plugins.InterfaceRecordInterfaceRecord
        
            interfaceId: The Autodesk.Navisworks.Api.Plugins.InterfaceRecord.IdId of the Autodesk.Navisworks.Api.Plugins.InterfaceRecordInterfaceRecord
            Returns: null if the Autodesk.Navisworks.Api.Plugins.InterfaceRecordInterfaceRecord cannot be found
        """
        pass

    def LoadPlugin(self):
        """
        LoadPlugin(self: PluginRecord) -> Plugin
        
            Returns the plugin, loads it if required
        """
        pass

    def TryLoadPlugin(self):
        """
        TryLoadPlugin(self: PluginRecord) -> Plugin
        
            Returns the plugin, loads it if required
            Returns: null if plugin failed to load
        """
        pass

    DeveloperId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the 4 character ADN developer code or a GUID. The combination of this and Autodesk.Navisworks.Api.Plugins.PluginRecord.NameName should make the plugin unique

Get: DeveloperId(self: PluginRecord) -> str

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Text to display in the Navisworks GUI.

Get: DisplayName(self: PluginRecord) -> str

"""

    ExtendedToolTip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extended Tooltip to display when the Plugin is highlighted in the Navisworks GUI

Get: ExtendedToolTip(self: PluginRecord) -> str

"""

    HasAttemptedCreate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if an attempt has been made to create the Plugin.

Get: HasAttemptedCreate(self: PluginRecord) -> bool

"""

    HasFailedCreate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if an attempt has been made to create the plugin, and it has failed.

Get: HasFailedCreate(self: PluginRecord) -> bool

"""

    HasFailedIsSelfEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Where Autodesk.Navisworks.Api.Plugins.PluginRecord.SupportsIsSelfEnabledSupportsIsSelfEnabled is true then the plugin 
will be created early and Autodesk.Navisworks.Api.Plugins.Plugin.IsSelfEnabledIsSelfEnabled
will be called to determine the result. 
Will return false if the plugin could not be created to make the call.

Get: HasFailedIsSelfEnabled(self: PluginRecord) -> bool

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The full identifier for the plugin. This is formed as 
Autodesk.Navisworks.Api.Plugins.PluginRecord.NameName.Autodesk.Navisworks.Api.Plugins.PluginRecord.DeveloperIdDeveloperId

Get: Id(self: PluginRecord) -> str

"""

    InterfaceRecords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a collection of Autodesk.Navisworks.Api.Plugins.InterfaceRecordInterfaceRecords that declare which interfaces we support

Get: InterfaceRecords(self: PluginRecord) -> ReadOnlyCollection[InterfaceRecord]

"""

    IsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether the Plugin is currently enabled for use or not.

Get: IsEnabled(self: PluginRecord) -> bool

"""

    IsLoaded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether the Plugin is currently loaded

Get: IsLoaded(self: PluginRecord) -> bool

"""

    LoadedPlugin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the plugin if loaded, otherwise null

Get: LoadedPlugin(self: PluginRecord) -> Plugin

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the Plugin. The combination of this and Autodesk.Navisworks.Api.Plugins.PluginRecord.DeveloperIdDeveloperId should make the plugin unique

Get: Name(self: PluginRecord) -> str

"""

    PluginOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets flags for how plugins run

Get: PluginOptions(self: PluginRecord) -> PluginOptions

"""

    SupportsIsSelfEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if Autodesk.Navisworks.Api.Plugins.Plugin.IsSelfEnabledIsSelfEnabled will be called.

Get: SupportsIsSelfEnabled(self: PluginRecord) -> bool

"""

    ToolTip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tooltip to display when the Plugin is highlighted in the Navisworks GUI

Get: ToolTip(self: PluginRecord) -> str

"""



class AddInPluginRecord(PluginRecord):
    """ Represents an Autodesk.Navisworks.Api.Plugins.AddInPluginAddInPlugin record in Navisworks """
    def CanExecute(self):
        """
        CanExecute(self: AddInPluginRecord) -> CommandState
        
            This is called to determine the state of plugin.
        Primarily if Autodesk.Navisworks.Api.Plugins.AddInPluginRecordExecute can be called.
        """
        pass

    def Execute(self, parameters):
        """
        Execute(self: AddInPluginRecord, *parameters: Array[str]) -> int
        
            Executes the plugin, loading it if needed
        """
        pass

    def LoadPlugin(self):
        """
        LoadPlugin(self: AddInPluginRecord) -> AddInPlugin
        
            Returns the plugin, loads it if required
        """
        pass

    def TryLoadPlugin(self):
        """
        TryLoadPlugin(self: AddInPluginRecord) -> AddInPlugin
        
            Returns the plugin, loads it if required
            Returns: null if plugin failed to load
        """
        pass

    CanToggle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies if the command can toggle

Get: CanToggle(self: AddInPluginRecord) -> bool

"""

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The 16x16 icon to be displayed for this command

Get: Icon(self: AddInPluginRecord) -> str

"""

    LargeIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The 32x32 icon to be displayed for this command

Get: LargeIcon(self: AddInPluginRecord) -> str

"""

    LoadedPlugin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the plugin if loaded, otherwise null

Get: LoadedPlugin(self: AddInPluginRecord) -> AddInPlugin

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Where the plugin is displayed in Navisworks menus system

Get: Location(self: AddInPluginRecord) -> AddInLocation

"""

    Shortcut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the keyboard shortcut for the command.

Get: Shortcut(self: AddInPluginRecord) -> str

"""

    ShortcutWindowTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Ids of the windows for which the shortcut is valid. 
Multiple Ids can be specified by separating with ";".
If Ids are specified the shortcut should be valid in all contexts.

Get: ShortcutWindowTypes(self: AddInPluginRecord) -> str

"""



class CallCanExecute(Enum, IComparable, IFormattable, IConvertible):
    """
    Determines logic used to determine if a command is Enabled
    
    enum CallCanExecute, values: Always (0), CurrentSelectionMultiple (3), CurrentSelectionSingle (2), DocumentNotClear (1)
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

    Always = None
    CurrentSelectionMultiple = None
    CurrentSelectionSingle = None
    DocumentNotClear = None
    value__ = None


class CommandAttribute(Attribute, _Attribute):
    """
    Defines a new command in the GUI system
    
    CommandAttribute(name: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass

    CallCanExecute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines the conditions in which CanExecuteCommand should be called.

Get: CallCanExecute(self: CommandAttribute) -> CallCanExecute

Set: CallCanExecute(self: CommandAttribute) = value
"""

    CanToggle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies if the command can toggle

Get: CanToggle(self: CommandAttribute) -> bool

Set: CanToggle(self: CommandAttribute) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The text to display for this command

Get: DisplayName(self: CommandAttribute) -> str

Set: DisplayName(self: CommandAttribute) = value
"""

    ExtendedToolTip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Extended Tooltip to display for this command

Get: ExtendedToolTip(self: CommandAttribute) -> str

Set: ExtendedToolTip(self: CommandAttribute) = value
"""

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The 16x16 icon to display for this command

Get: Icon(self: CommandAttribute) -> str

Set: Icon(self: CommandAttribute) = value
"""

    LargeIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The 32x32 icon to display for this command

Get: LargeIcon(self: CommandAttribute) -> str

Set: LargeIcon(self: CommandAttribute) = value
"""

    LoadForCanExecute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies if CanExecuteCommand should cause the Plugin to load

Get: LoadForCanExecute(self: CommandAttribute) -> bool

Set: LoadForCanExecute(self: CommandAttribute) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the command

Get: Name(self: CommandAttribute) -> str

"""

    Shortcut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the keyboard shortcut for the command.

Get: Shortcut(self: CommandAttribute) -> str

Set: Shortcut(self: CommandAttribute) = value
"""

    ShortcutWindowTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Ids of the windows for which the shortcut is valid. 
Multiple Ids can be specified by separating with ";".
If Ids are specified the shortcut should be valid in all contexts.

Get: ShortcutWindowTypes(self: CommandAttribute) -> str

Set: ShortcutWindowTypes(self: CommandAttribute) = value
"""

    ToolTip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Tooltip to display for this command

Get: ToolTip(self: CommandAttribute) -> str

Set: ToolTip(self: CommandAttribute) = value
"""



class CommandHandlerPlugin(Plugin):
    """ A plugin that can be used to add commands to the GUI """
    def CanExecuteCommand(self, name):
        """
        CanExecuteCommand(self: CommandHandlerPlugin, name: str) -> CommandState
        
            Called to determine if a command can be executed
        
            name: The name of the command
        """
        pass

    def CanExecuteRibbonTab(self, name):
        """
        CanExecuteRibbonTab(self: CommandHandlerPlugin, name: str) -> bool
        
            Called to determine if a ribbon tab can be executed
        
            name: The name of the ribbon tab
        """
        pass

    def ExecuteCommand(self, name, parameters):
        """
        ExecuteCommand(self: CommandHandlerPlugin, name: str, *parameters: Array[str]) -> int
        
            Called when a command is executed
        
            name: The name of the command
            parameters: Paramaters to be passed to the command
        """
        pass

    def TryShowCommandHelp(self, name):
        """
        TryShowCommandHelp(self: CommandHandlerPlugin, name: str) -> bool
        
            Called to tell the plugin to display help
        
            name: The name of the command
            Returns: Return true if you have handled this call
        """
        pass


class CommandHandlerPluginRecord(PluginRecord):
    """ Represents an Autodesk.Navisworks.Api.Plugins.CommandHandlerPluginCommandHandlerPlugin record in Navisworks """
    def CanExecuteCommand(self, commandId):
        """
        CanExecuteCommand(self: CommandHandlerPluginRecord, commandId: str) -> CommandState
        
            Calls CanExecuteCommand on the plugin
        
            commandId: The Id of the command
        """
        pass

    def CanExecuteRibbonTab(self, ribbonId):
        """
        CanExecuteRibbonTab(self: CommandHandlerPluginRecord, ribbonId: str) -> bool
        
            Calls CanExecuteRibbonTab on the plugin
        
            ribbonId: The Id of the ribbon tab
        """
        pass

    def ExecuteCommand(self, commandId, parameters):
        """
        ExecuteCommand(self: CommandHandlerPluginRecord, commandId: str, *parameters: Array[str]) -> int
        
            Calls ExecuteCommand on the plugin
        
            commandId: The Id of the command
            parameters: Paramaters to be passed to the command
        """
        pass

    def ExtractNameFromId(self, id):
        """
        ExtractNameFromId(self: CommandHandlerPluginRecord, id: str) -> str
        
            Helper to extract a name from a Id.
        """
        pass

    def LoadPlugin(self):
        """
        LoadPlugin(self: CommandHandlerPluginRecord) -> CommandHandlerPlugin
        
            Returns the plugin, loads it if required
        """
        pass

    def MakeIdFromName(self, name):
        """
        MakeIdFromName(self: CommandHandlerPluginRecord, name: str) -> str
        
            Helper to make an Id from a name
        """
        pass

    def ShowCommandHelp(self, commandId):
        """
        ShowCommandHelp(self: CommandHandlerPluginRecord, commandId: str) -> bool
        
            Calls TryShowCommandHelp on the plugin
        
            commandId: The Id of the command
        """
        pass

    def TryLoadPlugin(self):
        """
        TryLoadPlugin(self: CommandHandlerPluginRecord) -> CommandHandlerPlugin
        
            Returns the plugin, loads it if required
            Returns: null if plugin failed to load
        """
        pass

    def TryShowCommandHelp(self, commandId):
        """
        TryShowCommandHelp(self: CommandHandlerPluginRecord, commandId: str) -> bool
        
            Calls TryShowCommandHelp on the plugin
        
            commandId: The Id of the command
        """
        pass

    CommandRecords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Commands defined by this plugin

Get: CommandRecords(self: CommandHandlerPluginRecord) -> ReadOnlyCollection[CommandRecord]

"""

    LoadedPlugin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the plugin if loaded, otherwise null

Get: LoadedPlugin(self: CommandHandlerPluginRecord) -> CommandHandlerPlugin

"""

    RibbonLayoutRecords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Xaml files that define the layout of the RibbonTabs and Commands

Get: RibbonLayoutRecords(self: CommandHandlerPluginRecord) -> ReadOnlyCollection[RibbonLayoutRecord]

"""

    RibbonTabRecords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ribbon Tabs defined by this plugin

Get: RibbonTabRecords(self: CommandHandlerPluginRecord) -> ReadOnlyCollection[RibbonTabRecord]

"""

    ToolTipsRecords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ToolTips files that define tooltips for RibbonTabs and Commands

Get: ToolTipsRecords(self: CommandHandlerPluginRecord) -> ReadOnlyCollection[ToolTipsRecord]

"""



class CommandRecord(object):
    """ Represents the definition of a command in the GUI system """
    CanToggle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies if the command can toggle

Get: CanToggle(self: CommandRecord) -> bool

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The text to be displayed for this command

Get: DisplayName(self: CommandRecord) -> str

"""

    ExtendedToolTip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The extended tooltip to be displayed for this command

Get: ExtendedToolTip(self: CommandRecord) -> str

"""

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The 16x16 icon to be displayed for this command

Get: Icon(self: CommandRecord) -> str

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The full Id of the command. This is a combination of 
and Autodesk.Navisworks.Api.Plugins.Plugin.IdPlugin.Id

Get: Id(self: CommandRecord) -> str

"""

    LargeIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The 32x32 icon to be displayed for this command

Get: LargeIcon(self: CommandRecord) -> str

"""

    Shortcut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the keyboard shortcut for the command.

Get: Shortcut(self: CommandRecord) -> str

"""

    ShortcutWindowTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Ids of the windows for which the shortcut is valid. 
Multiple Ids can be specified by separating with ";".
If Ids are specified the shortcut should be valid in all contexts.

Get: ShortcutWindowTypes(self: CommandRecord) -> str

"""

    ToolTip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The tooltip to be displayed for this command

Get: ToolTip(self: CommandRecord) -> str

"""



class CommandState(object):
    """
    Represents the state of a command in the GUI
    
    CommandState(enabled: bool)
    CommandState()
    """
    @staticmethod # known case of __new__
    def __new__(self, enabled=None):
        """
        __new__(cls: type, enabled: bool)
        __new__(cls: type)
        """
        pass

    IsChecked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies if the command should be checked

Get: IsChecked(self: CommandState) -> bool

Set: IsChecked(self: CommandState) = value
"""

    IsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies if the command should be enabled

Get: IsEnabled(self: CommandState) -> bool

Set: IsEnabled(self: CommandState) = value
"""

    IsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies if the command should be visible

Get: IsVisible(self: CommandState) -> bool

Set: IsVisible(self: CommandState) = value
"""

    OverrideDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies if the display name for the command should be overridden

Get: OverrideDisplayName(self: CommandState) -> str

Set: OverrideDisplayName(self: CommandState) = value
"""



class CustomPlugin(Plugin):
    """
    A custom plugin is the most basic plugin that can be defined.
    It can be used when none of the specialized behaviour of other plugin tyes is required.
    """

class CustomPluginRecord(PluginRecord):
    """ Record representing a Autodesk.Navisworks.Api.Plugins.CustomPluginCustomPlugin """
    def LoadPlugin(self):
        """
        LoadPlugin(self: CustomPluginRecord) -> CustomPlugin
        
            Returns the plugin, loads it if required
        """
        pass

    def TryLoadPlugin(self):
        """
        TryLoadPlugin(self: CustomPluginRecord) -> CustomPlugin
        
            Returns the plugin, loads it if required
            Returns: null if plugin failed to load
        """
        pass

    LoadedPlugin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the plugin if loaded, otherwise null

Get: LoadedPlugin(self: CustomPluginRecord) -> CustomPlugin

"""



class DockPanePlugin(Plugin):
    """ A plugin that can be used to add a docking pane to the GUI. """
    def ActivatePane(self):
        """
        ActivatePane(self: DockPanePlugin)
            Activates the pane (i.e. makes it the window with keyboard focus), also making it
        visible first, if necessary.
        """
        pass

    def CreateControlPane(self):
        """
        CreateControlPane(self: DockPanePlugin) -> Control
        
            Called to tell the plugin to create it's pane. The pane will be resized as specified by the  
        Autodesk.Navisworks.Api.Plugins.DockPanePluginAttributeDockPanePluginAttribute.
        
             Should be overriden in conjunction with 
        Autodesk.Navisworks.Api.Plugins.DockPanePlugin.DestroyControlPane(System.Windows.Forms.Control)DestroyControlPane.
        
            Returns: A Control that contains the pane content
        """
        pass

    def CreateHWndPane(self, parent):
        """
        CreateHWndPane(self: DockPanePlugin, parent: IWin32Window) -> IWin32Window
        
            Called to tell the plugin to create it's pane. The pane will be resized as specified by the  
        Autodesk.Navisworks.Api.Plugins.DockPanePluginAttributeDockPanePluginAttribute.
        
             Should be overriden in conjunction with 
        Autodesk.Navisworks.Api.Plugins.DockPanePlugin.DestroyHWndPane(System.Windows.Forms.IWin32Window)DestroyHWndPane.
        
        
            parent: The pane should be created using this window as it's parent
            Returns: The handle of window that contains the pane content
        """
        pass

    def DestroyControlPane(self, pane):
        """
        DestroyControlPane(self: DockPanePlugin, pane: Control)
            Called to tell the plugin to destroy it's pane
        Should be overriden in conjunction with 
        Autodesk.Navisworks.Api.Plugins.DockPanePlugin.CreateControlPaneCreateControlPane.
        
            pane: The pane to destroy
        """
        pass

    def DestroyHWndPane(self, pane):
        """
        DestroyHWndPane(self: DockPanePlugin, pane: IWin32Window)
            Called to tell the plugin to destroy it's pane.
        Should be overriden in conjunction with 
        
             Autodesk.Navisworks.Api.Plugins.DockPanePlugin.CreateHWndPane(System.Windows.Forms.IWin32Window)CreateHWndPane.
        
        
            pane: The pane to destroy
        """
        pass

    def OnActivePaneChanged(self, isActive):
        """
        OnActivePaneChanged(self: DockPanePlugin, isActive: bool)
            Called when the active pane changes
        """
        pass

    def OnVisibleChanged(self):
        """
        OnVisibleChanged(self: DockPanePlugin)
            Called when the visibility of the pane changes
        """
        pass

    def TryShowHelp(self):
        """
        TryShowHelp(self: DockPanePlugin) -> bool
        
            Called to tell the plugin to display help
            Returns: Return true if you have handled this call
        """
        pass

    def TryShowHelpAtScreenPoint(self, x, y):
        """
        TryShowHelpAtScreenPoint(self: DockPanePlugin, x: int, y: int) -> bool
        
            Called to tell the plugin to display help at a screen point
            Returns: Return true if you have handled this call
        """
        pass

    def TryShowHelpForHighlight(self):
        """
        TryShowHelpForHighlight(self: DockPanePlugin) -> bool
        
            Called to tell the plugin to display help for highlight
            Returns: Return true if you have handled this call
        """
        pass

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The visibility of the pane

Get: Visible(self: DockPanePlugin) -> bool

Set: Visible(self: DockPanePlugin) = value
"""



class DockPanePluginAttribute(Attribute, _Attribute):
    """
    Optional attribute for use with an Autodesk.Navisworks.Api.Plugins.DockPanePluginDockPanePlugin derived class.
    If this attribute is not used, the default values are the same as using a Autodesk.Navisworks.Api.Plugins.DockPanePluginAttributeDockPanePluginAttribute(100,100)
    
    DockPanePluginAttribute(preferredWidth: int, preferredHeight: int)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, preferredWidth, preferredHeight):
        """ __new__(cls: type, preferredWidth: int, preferredHeight: int) """
        pass

    AutoScroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if scroll bars should appear when the pane gets bellow it's minimum size

Get: AutoScroll(self: DockPanePluginAttribute) -> bool

Set: AutoScroll(self: DockPanePluginAttribute) = value
"""

    FixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if the pane should be resizable

Get: FixedSize(self: DockPanePluginAttribute) -> bool

Set: FixedSize(self: DockPanePluginAttribute) = value
"""

    MinimumHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Minimum height of pane, 0 means no preference

Get: MinimumHeight(self: DockPanePluginAttribute) -> int

Set: MinimumHeight(self: DockPanePluginAttribute) = value
"""

    MinimumWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Minimum width of pane, 0 means no preference

Get: MinimumWidth(self: DockPanePluginAttribute) -> int

Set: MinimumWidth(self: DockPanePluginAttribute) = value
"""

    PreferredHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Preferred height of pane, 0 means no preference

Get: PreferredHeight(self: DockPanePluginAttribute) -> int

"""

    PreferredWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Preferred width of pane, 0 means no preference

Get: PreferredWidth(self: DockPanePluginAttribute) -> int

"""



class DockPanePluginRecord(PluginRecord):
    """ Represents an Autodesk.Navisworks.Api.Plugins.DockPanePluginDockPanePlugin record in Navisworks """
    def LoadPlugin(self):
        """
        LoadPlugin(self: DockPanePluginRecord) -> DockPanePlugin
        
            Returns the plugin, loads it if required
        """
        pass

    def TryLoadPlugin(self):
        """
        TryLoadPlugin(self: DockPanePluginRecord) -> DockPanePlugin
        
            Returns the plugin, loads it if required
            Returns: null if plugin failed to load
        """
        pass

    AutoScroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if scroll bars should appear when the pane gets bellow it's minimum size

Get: AutoScroll(self: DockPanePluginRecord) -> bool

"""

    FixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if the pane should be resizable

Get: FixedSize(self: DockPanePluginRecord) -> bool

"""

    LoadedPlugin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the plugin if loaded, otherwise null

Get: LoadedPlugin(self: DockPanePluginRecord) -> DockPanePlugin

"""

    MinimumHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Minimum height of pane, 0 means no preference

Get: MinimumHeight(self: DockPanePluginRecord) -> int

"""

    MinimumWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Minimum width of pane, 0 means no preference

Get: MinimumWidth(self: DockPanePluginRecord) -> int

"""

    PreferredHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Preferred height of pane, 0 means no preference

Get: PreferredHeight(self: DockPanePluginRecord) -> int

"""

    PreferredWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Preferred width of pane, 0 means no preference

Get: PreferredWidth(self: DockPanePluginRecord) -> int

"""



class EventWatcherPlugin(Plugin):
    """
    Differs fom other plugin types in that the plugin is not delay loaded. 
    A typical implementation will subscribe to some API events in 
    Autodesk.Navisworks.Api.Plugins.Plugin.OnLoadedOnLoaded and
    unsubscribe in Autodesk.Navisworks.Api.Plugins.Plugin.OnUnloadingOnUnloading.
    """
    def OnLoaded(self):
        """
        OnLoaded(self: EventWatcherPlugin)
            Called once immediately after the plugin has been loaded (created).
        Default implementation does nothing.
        This is a good place to subscribe to API events.
        """
        pass

    def OnUnloading(self):
        """
        OnUnloading(self: EventWatcherPlugin)
            Called once just before the plugin is unloaded. If the plugin implements 
        System.IDisposableIDisposable, then
        Dispose will be called immediately after the plugin is unloaded.
        
             Plugins are typically unloaded at application shutdown or when the end user has disabled a plugin.
        Default implementation does nothing.
        This is a good place to unsubscribe from 
             API events.
        """
        pass


class EventWatcherPluginRecord(PluginRecord):
    """ Record representing a Autodesk.Navisworks.Api.Plugins.EventWatcherPluginEventWatcherPlugin """
    def LoadPlugin(self):
        """
        LoadPlugin(self: EventWatcherPluginRecord) -> EventWatcherPlugin
        
            Returns the plugin, loads it if required
        """
        pass

    def TryLoadPlugin(self):
        """
        TryLoadPlugin(self: EventWatcherPluginRecord) -> EventWatcherPlugin
        
            Returns the plugin, loads it if required
            Returns: null if plugin failed to load
        """
        pass

    LoadedPlugin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the plugin if loaded, otherwise null

Get: LoadedPlugin(self: EventWatcherPluginRecord) -> EventWatcherPlugin

"""



class ExecuteDisabledException(InvalidOperationException, ISerializable, _Exception):
    """
    The exception that is thrown when you try to call Execute on a plugin who's CanExecute method states that it should be disabled.
    
    ExecuteDisabledException(message: str, innerException: Exception)
    ExecuteDisabledException(message: str)
    ExecuteDisabledException()
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


class FileMetadata(NativeHandle, IDisposable):
    """
    Metadata about a file or URI.
    
    FileMetadata()
    """
    def Dispose(self):
        """ Dispose(self: NativeHandle, A_0: bool) """
        pass

    def InternalCleanup(self, *args): #cannot find CLR method
        """ InternalCleanup(self: FileMetadata, queue: bool) """
        pass

    @staticmethod
    def InternalCreator(handleIn, ownership, parent):
        """ InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> FileMetadata """
        pass

    @staticmethod
    def InternalFactory(reserved):
        """ InternalFactory(reserved: NativeHandleInit) -> (NativeHandle, NativeHandleInit) """
        pass

    def InternalInit(self, *args): #cannot find CLR method
        """ InternalInit(self: NativeHandle, ptr: Void*, ownership: NativeHandleOwnership, source: NativeHandle) """
        pass

    def InternalIsReadOnlyByOwnership(self, *args): #cannot find CLR method
        """ InternalIsReadOnlyByOwnership(self: NativeHandle) -> bool """
        pass

    def InternalRC(self, *args): #cannot find CLR method
        """ InternalRC(self: NativeHandle) -> bool """
        pass

    def InternalWR(self, *args): #cannot find CLR method
        """ InternalWR(self: NativeHandle) -> Void* """
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
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, init: NativeHandleInit) -> NativeHandleInit
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    HasModificationTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is the ModificationTime property valid?

Get: HasModificationTime(self: FileMetadata) -> bool

"""

    HasRevisionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is the RevisionId property valid?

Get: HasRevisionId(self: FileMetadata) -> bool

"""

    HasSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is the Size property valid?

Get: HasSize(self: FileMetadata) -> bool

"""

    ModificationTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The modification time of the URI.

Get: ModificationTime(self: FileMetadata) -> DateTime

Set: ModificationTime(self: FileMetadata) = value
"""

    RevisionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The revision id of the URI.

Get: RevisionId(self: FileMetadata) -> str

Set: RevisionId(self: FileMetadata) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size in bytes of the URI.

Get: Size(self: FileMetadata) -> UInt64

Set: Size(self: FileMetadata) = value
"""



class FileProtocolHandle(object):
    """ A file handle opened via the Autodesk.Navisworks.Api.Plugins.FileProtocolPluginFileProtocolPlugin. """
    def Close(self):
        """
        Close(self: FileProtocolHandle) -> bool
        
            Closes an open file handle.
        """
        pass

    def Read(self, data, offset, count):
        """
        Read(self: FileProtocolHandle, offset: UInt64, count: UInt64) -> (bool, Array[Byte])
        
            Reads data from a file.
        """
        pass

    def Write(self, data, offset, count):
        """
        Write(self: FileProtocolHandle, data: Array[Byte], offset: UInt64, count: UInt64) -> bool
        
            Writes data to a file.
        """
        pass


class FileProtocolOpenMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Open mode for FileProtocolPlugin interface.
    
    enum FileProtocolOpenMode, values: Read (0), Write (1)
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

    Read = None
    value__ = None
    Write = None


class FileProtocolPlugin(Plugin):
    """ A plugin for implementing a custom file protocol. """
    def GetFile(self, uri, localPath, progress):
        """
        GetFile(self: FileProtocolPlugin, uri: Uri, localPath: str, progress: Progress) -> bool
        
            Downloads a remote URI to a local path.
        """
        pass

    def GetFileInfo(self, uri, info):
        """
        GetFileInfo(self: FileProtocolPlugin, uri: Uri, info: FileMetadata) -> bool
        
            Returns information about a URI.
        """
        pass

    def GetFileToCache(self, uri, progress, cachePath):
        """
        GetFileToCache(self: FileProtocolPlugin, uri: Uri, progress: Progress) -> (bool, str)
        
            Downloads a remote URI to the protocols internal cache.
        """
        pass

    def OpenFile(self, uri, mode):
        """
        OpenFile(self: FileProtocolPlugin, uri: Uri, mode: FileProtocolOpenMode) -> FileProtocolHandle
        
            Directly opens a URI.
        """
        pass

    def PutFile(self, localPath, uri, progress):
        """
        PutFile(self: FileProtocolPlugin, localPath: str, uri: Uri, progress: Progress) -> bool
        
            Uploads a file to a remote URI.
        """
        pass

    def TryGetDisplayName(self, uri, displayName):
        """
        TryGetDisplayName(self: FileProtocolPlugin, uri: Uri) -> (bool, str)
        
            Returns the normal display name for a given URI.
        """
        pass

    def TryGetVerboseDisplayName(self, uri, displayName):
        """
        TryGetVerboseDisplayName(self: FileProtocolPlugin, uri: Uri) -> (bool, str)
        
            Returns the verbose display name for a given URI.
        """
        pass

    def TryResolveAbsolute(self, originalParent, originalChild, resolvedParent, resolvedChild):
        """
        TryResolveAbsolute(self: FileProtocolPlugin, originalParent: str, originalChild: str, resolvedParent: str) -> (bool, str)
        
            Called to resolve an absolute URI.
        """
        pass

    def TryResolveRelative(self, resolvedParent, relativeChild, resolvedChild):
        """
        TryResolveRelative(self: FileProtocolPlugin, resolvedParent: str, relativeChild: str) -> (bool, str)
        
            Called to resolve an relative URI.
        """
        pass

    IsRemote = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Does this protocol access remote data?

Get: IsRemote(self: FileProtocolPlugin) -> bool

"""

    SupportedSchemes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of schemes that this protocol supports.

Get: SupportedSchemes(self: FileProtocolPlugin) -> IEnumerable[str]

"""

    SupportsDirectOpen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Does this protocol support direct opening of a file?

Get: SupportsDirectOpen(self: FileProtocolPlugin) -> bool

"""

    SupportsGetPut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Does this protocol support the GetFile and PutFile methods?

Get: SupportsGetPut(self: FileProtocolPlugin) -> bool

"""

    SupportsOwnCache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Does this protocol support it's own cache?

Get: SupportsOwnCache(self: FileProtocolPlugin) -> bool

"""



class FileProtocolPluginRecord(PluginRecord):
    """ Represents a Autodesk.Navisworks.Api.Plugins.FileProtocolPluginFileProtocolPlugin record in Navisworks """
    def LoadPlugin(self):
        """
        LoadPlugin(self: FileProtocolPluginRecord) -> FileProtocolPlugin
        
            Returns the plugin, loads it if required
        """
        pass

    def TryLoadPlugin(self):
        """
        TryLoadPlugin(self: FileProtocolPluginRecord) -> FileProtocolPlugin
        
            Returns the plugin, loads it if required
            Returns: null if plugin failed to load
        """
        pass

    LoadedPlugin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the plugin if loaded, otherwise null

Get: LoadedPlugin(self: FileProtocolPluginRecord) -> FileProtocolPlugin

"""



class InputPlugin(Plugin):
    """ A plugin that can respond to mouse and keyboard inputs. """
    def ContextMenu(self, view, x, y):
        """
        ContextMenu(self: InputPlugin, view: View, x: int, y: int) -> bool
        
            ContextMenu handler.
        """
        pass

    def GetCursor(self, view, modifier):
        """
        GetCursor(self: InputPlugin, view: View, modifier: KeyModifiers) -> Cursor
        
            GetCursor handler.
        """
        pass

    def GetHelpIdAtPoint(self, view, x, y):
        """
        GetHelpIdAtPoint(self: InputPlugin, view: View, x: int, y: int) -> HelpIdResult
        
            GetHelpIdAtPoint handler.
        """
        pass

    def GetHelpIdForHighlight(self, view):
        """
        GetHelpIdForHighlight(self: InputPlugin, view: View) -> HelpIdResult
        
            GetHelpIdForHighlight handler.
        """
        pass

    def GetTooltip(self, view, x, y):
        """
        GetTooltip(self: InputPlugin, view: View, x: int, y: int) -> TooltipResult
        
            GetTooltip handler
        """
        pass

    def KeyDown(self, view, modifier, key, timeOffset):
        """
        KeyDown(self: InputPlugin, view: View, modifier: KeyModifiers, key: UInt16, timeOffset: float) -> bool
        
            MouseLeave handler.
        """
        pass

    def KeyDrag(self, view, modifier, timeOffset):
        """
        KeyDrag(self: InputPlugin, view: View, modifier: KeyModifiers, timeOffset: float) -> bool
        
            KeyDrag  handler.
        """
        pass

    def KeyUp(self, view, modifier, key, timeOffset):
        """
        KeyUp(self: InputPlugin, view: View, modifier: KeyModifiers, key: UInt16, timeOffset: float) -> bool
        
            KeyUp handler.
        """
        pass

    def ModifierKeyDown(self, view, modifier, timeOffset):
        """
        ModifierKeyDown(self: InputPlugin, view: View, modifier: KeyModifiers, timeOffset: float) -> bool
        
            ModifierKeyDown handler.
        """
        pass

    def ModifierKeyUp(self, view, modifier, timeOffset):
        """
        ModifierKeyUp(self: InputPlugin, view: View, modifier: KeyModifiers, timeOffset: float) -> bool
        
            ModifierKeyUp handler.
        """
        pass

    def MouseDown(self, view, modifiers, button, x, y, timeOffset):
        """
        MouseDown(self: InputPlugin, view: View, modifiers: KeyModifiers, button: UInt16, x: int, y: int, timeOffset: float) -> bool
        
            Mouse down handler.
        """
        pass

    def MouseDrag(self, view, modifiers, x, y, timeOffset):
        """
        MouseDrag(self: InputPlugin, view: View, modifiers: KeyModifiers, x: int, y: int, timeOffset: float) -> bool
        
            Mouse drag handler.
        """
        pass

    def MouseLeave(self, view, timeOffset):
        """
        MouseLeave(self: InputPlugin, view: View, timeOffset: float) -> bool
        
            Mouse leave handler.
        """
        pass

    def MouseMove(self, view, modifiers, x, y, timeOffset):
        """
        MouseMove(self: InputPlugin, view: View, modifiers: KeyModifiers, x: int, y: int, timeOffset: float) -> bool
        
            Mouse move handler.
        """
        pass

    def MouseUp(self, view, modifiers, button, x, y, timeOffset):
        """
        MouseUp(self: InputPlugin, view: View, modifiers: KeyModifiers, button: UInt16, x: int, y: int, timeOffset: float) -> bool
        
            Mouse up handler.
        """
        pass

    def WheelDrag(self, view, modifier, x, y, wheel, len, timeOffset):
        """
        WheelDrag(self: InputPlugin, view: View, modifier: KeyModifiers, x: int, y: int, wheel: UInt16, len: float, timeOffset: float) -> bool
        
            WheelDrag handler.
        """
        pass


class InputPluginRecord(PluginRecord):
    """ Represents an Autodesk.Navisworks.Api.Plugins.InputPluginInputPlugin record in Navisworks """
    def LoadPlugin(self):
        """
        LoadPlugin(self: InputPluginRecord) -> InputPlugin
        
            Returns the plugin, loads it if required
        """
        pass

    def TryLoadPlugin(self):
        """
        TryLoadPlugin(self: InputPluginRecord) -> InputPlugin
        
            Returns the plugin, loads it if required
            Returns: null if plugin failed to load
        """
        pass

    LoadedPlugin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the plugin if loaded, otherwise null

Get: LoadedPlugin(self: InputPluginRecord) -> InputPlugin

"""



class InterfaceAttribute(Attribute, _Attribute):
    """
    Attribute that declares a plugin implements a particular interface or behaviours.
    
    InterfaceAttribute(name: str, developerId: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, developerId):
        """ __new__(cls: type, name: str, developerId: str) """
        pass

    DeveloperId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The 4 character ADN developer code or a GUID. The combination of this and Autodesk.Navisworks.Api.Plugins.InterfaceAttribute.NameName is used
to form and Id that identifies which interface is being supported.

Get: DeveloperId(self: InterfaceAttribute) -> str

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Optional additional information about the interface implementation

Get: DisplayName(self: InterfaceAttribute) -> str

Set: DisplayName(self: InterfaceAttribute) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the Inteface. The combination of this and Autodesk.Navisworks.Api.Plugins.InterfaceAttribute.DeveloperIdDeveloperId is used
to form an Id that identifies which interface is being supported.

Get: Name(self: InterfaceAttribute) -> str

"""

    UserData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Optional additional information about the interface implementation

Get: UserData(self: InterfaceAttribute) -> str

Set: UserData(self: InterfaceAttribute) = value
"""



class InterfaceRecord(object):
    """ Record that declares a plugin implements a particular interface or behaviour. """
    DeveloperId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The 4 character ADN developer code or a GUID. The combination of this and Autodesk.Navisworks.Api.Plugins.InterfaceRecord.NameName is used
to form Autodesk.Navisworks.Api.Plugins.InterfaceRecord.IdId that identifies which interface is being supported.

Get: DeveloperId(self: InterfaceRecord) -> str

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Optional additional information about the interface implementation

Get: DisplayName(self: InterfaceRecord) -> str

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The full identifier of the interface being supported. This is formed as 
Autodesk.Navisworks.Api.Plugins.InterfaceRecord.NameName.Autodesk.Navisworks.Api.Plugins.InterfaceRecord.DeveloperIdDeveloperId

Get: Id(self: InterfaceRecord) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the Inteface. The combination of this and Autodesk.Navisworks.Api.Plugins.InterfaceRecord.DeveloperIdDeveloperId is used
to form Autodesk.Navisworks.Api.Plugins.InterfaceRecord.IdId that identifies which interface is being supported.

Get: Name(self: InterfaceRecord) -> str

"""

    UserData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Optional additional information about the interface implementation

Get: UserData(self: InterfaceRecord) -> str

"""



class PluginAttribute(Attribute, _Attribute):
    """
    The standard attribute which must be applied to all plug-ins.
    
    PluginAttribute(name: str, developerId: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, developerId):
        """ __new__(cls: type, name: str, developerId: str) """
        pass

    DeveloperId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The 4 character ADN developer code or a GUID. The combination of this and Autodesk.Navisworks.Api.Plugins.PluginAttribute.NameName should make the plugin unique

Get: DeveloperId(self: PluginAttribute) -> str

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Text to display in the Navisworks GUI

Get: DisplayName(self: PluginAttribute) -> str

Set: DisplayName(self: PluginAttribute) = value
"""

    ExtendedToolTip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The extended tooltip to display when the Plugin is highlighted in the Navisworks GUI

Get: ExtendedToolTip(self: PluginAttribute) -> str

Set: ExtendedToolTip(self: PluginAttribute) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the Plugin. The combination of this and Autodesk.Navisworks.Api.Plugins.PluginAttribute.DeveloperIdDeveloperId should make the plugin unique

Get: Name(self: PluginAttribute) -> str

"""

    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Options that modify how a plugin behaves

Get: Options(self: PluginAttribute) -> PluginOptions

Set: Options(self: PluginAttribute) = value
"""

    SupportsIsSelfEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if Plugin.IsSelfEnabled will be called.

Get: SupportsIsSelfEnabled(self: PluginAttribute) -> bool

Set: SupportsIsSelfEnabled(self: PluginAttribute) = value
"""

    ToolTip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The tooltip to display when the Plugin is highlighted in the Navisworks GUI

Get: ToolTip(self: PluginAttribute) -> str

Set: ToolTip(self: PluginAttribute) = value
"""



class PluginLoadException(InvalidOperationException, ISerializable, _Exception):
    """
    The exception that is thrown when a plugin fails to load
    
    PluginLoadException(message: str, innerException: Exception)
    PluginLoadException(message: str)
    PluginLoadException()
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


class PluginOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Options that modify how a plugin behaves
    
    enum (flags) PluginOptions, values: None (0), SupportsControls (1)
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

    None = None
    SupportsControls = None
    value__ = None


class RenderPlugin(Plugin):
    """ A plugin that can perform custom rendering. """
    def MakeRenderBoundingBox(self, viewer):
        """
        MakeRenderBoundingBox(self: RenderPlugin, viewer: View) -> BoundingBox3D
        
            Should return bounding box of any additional model space geometry that will be rendered so that near/far clipping planes can be adjusted accordingly.
            Returns: Bounding box
        """
        pass

    def OverlayRender(self, view, graphics):
        """
        OverlayRender(self: RenderPlugin, view: View, graphics: Graphics)
            Override to allow custom drawing overlayed on main render.
        """
        pass

    def Render(self, view, graphics):
        """
        Render(self: RenderPlugin, view: View, graphics: Graphics)
            Override to allow custom drawing in main render.
        """
        pass


class RenderPluginRecord(PluginRecord):
    """ Represents an Autodesk.Navisworks.Api.Plugins.RenderPluginRenderPlugin record in Navisworks """
    def LoadPlugin(self):
        """
        LoadPlugin(self: RenderPluginRecord) -> RenderPlugin
        
            Returns the plugin, loads it if required
        """
        pass

    def TryLoadPlugin(self):
        """
        TryLoadPlugin(self: RenderPluginRecord) -> RenderPlugin
        
            Returns the plugin, loads it if required
            Returns: null if plugin failed to load
        """
        pass

    LoadedPlugin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the plugin if loaded, otherwise null

Get: LoadedPlugin(self: RenderPluginRecord) -> RenderPlugin

"""



class RibbonLayoutAttribute(Attribute, _Attribute):
    """
    Defines a new ribbon layout in the GUI system
    
    RibbonLayoutAttribute(xaml: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, xaml):
        """ __new__(cls: type, xaml: str) """
        pass

    Xaml = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Xaml file that specifies the Ribbon tab and commands

Get: Xaml(self: RibbonLayoutAttribute) -> str

"""



class RibbonLayoutRecord(object):
    """ Represents the definition of a ribbon layout in the GUI system """
    Xaml = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The path to the Xaml file that specifies the layout of ribbon and commands

Get: Xaml(self: RibbonLayoutRecord) -> str

"""



class RibbonTabAttribute(Attribute, _Attribute):
    """
    Defines a ribbon tab in the GUI system.
    
    RibbonTabAttribute(name: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass

    CallCanExecute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines the conditions in which CanExecuteRibbonTab should be called.

Get: CallCanExecute(self: RibbonTabAttribute) -> CallCanExecute

Set: CallCanExecute(self: RibbonTabAttribute) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The text to display for this Ribbon tab

Get: DisplayName(self: RibbonTabAttribute) -> str

Set: DisplayName(self: RibbonTabAttribute) = value
"""

    LoadForCanExecute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies if CanExecuteRibbonTab should cause the Plugin to load

Get: LoadForCanExecute(self: RibbonTabAttribute) -> bool

Set: LoadForCanExecute(self: RibbonTabAttribute) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the Ribbon tab

Get: Name(self: RibbonTabAttribute) -> str

"""



class RibbonTabRecord(object):
    """ Represents the definition of a ribbon tab in the GUI system. """
    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The text to be displayed for this Ribbon tab

Get: DisplayName(self: RibbonTabRecord) -> str

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The full Id of the ribbon tab. This is a combination of 
and Autodesk.Navisworks.Api.Plugins.Plugin.IdPlugin.Id

Get: Id(self: RibbonTabRecord) -> str

"""



class StringsAttribute(Attribute, _Attribute):
    """
    Attribute which causes a string localization file to be loaded for a particular plug-in.
    
    StringsAttribute(fileName: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fileName):
        """ __new__(cls: type, fileName: str) """
        pass

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The filename containing the strings.

Get: FileName(self: StringsAttribute) -> str

"""



class ToolPlugin(Plugin):
    """ A plugin that provides the behaviour of a custom tool. """
    def ContextMenu(self, view, x, y):
        """
        ContextMenu(self: ToolPlugin, view: View, x: int, y: int) -> bool
        
            ContextMenu handler.
        """
        pass

    def GetCursor(self, view, modifier):
        """
        GetCursor(self: ToolPlugin, view: View, modifier: KeyModifiers) -> Cursor
        
            GetCursor handler.
        """
        pass

    def GetHelpIdAtPoint(self, view, x, y):
        """
        GetHelpIdAtPoint(self: ToolPlugin, view: View, x: int, y: int) -> HelpIdResult
        
            GetHelpIdAtPoint handler.
        """
        pass

    def GetHelpIdForHighlight(self, view):
        """
        GetHelpIdForHighlight(self: ToolPlugin, view: View) -> HelpIdResult
        
            GetHelpIdForHighlight handler.
        """
        pass

    def GetTooltip(self, view, x, y):
        """
        GetTooltip(self: ToolPlugin, view: View, x: int, y: int) -> TooltipResult
        
            GetTooltip handler
        """
        pass

    def KeyDown(self, view, modifier, key, timeOffset):
        """
        KeyDown(self: ToolPlugin, view: View, modifier: KeyModifiers, key: UInt16, timeOffset: float) -> bool
        
            MouseLeave handler.
        """
        pass

    def KeyDrag(self, view, modifier, timeOffset):
        """
        KeyDrag(self: ToolPlugin, view: View, modifier: KeyModifiers, timeOffset: float) -> bool
        
            KeyDrag  handler.
        """
        pass

    def KeyUp(self, view, modifier, key, timeOffset):
        """
        KeyUp(self: ToolPlugin, view: View, modifier: KeyModifiers, key: UInt16, timeOffset: float) -> bool
        
            KeyUp handler.
        """
        pass

    def MakeRenderBoundingBox(self, viewer):
        """
        MakeRenderBoundingBox(self: ToolPlugin, viewer: View) -> BoundingBox3D
        
            Should return bounding box of any additional model space geometry that will be rendered so that near/far clipping planes can be adjusted accordingly.
            Returns: Bounding box
        """
        pass

    def ModifierKeyDown(self, view, modifier, timeOffset):
        """
        ModifierKeyDown(self: ToolPlugin, view: View, modifier: KeyModifiers, timeOffset: float) -> bool
        
            ModifierKeyDown handler.
        """
        pass

    def ModifierKeyUp(self, view, modifier, timeOffset):
        """
        ModifierKeyUp(self: ToolPlugin, view: View, modifier: KeyModifiers, timeOffset: float) -> bool
        
            ModifierKeyUp handler.
        """
        pass

    def MouseDown(self, view, modifiers, button, x, y, timeOffset):
        """
        MouseDown(self: ToolPlugin, view: View, modifiers: KeyModifiers, button: UInt16, x: int, y: int, timeOffset: float) -> bool
        
            Mouse down handler.
        """
        pass

    def MouseDrag(self, view, modifiers, x, y, timeOffset):
        """
        MouseDrag(self: ToolPlugin, view: View, modifiers: KeyModifiers, x: int, y: int, timeOffset: float) -> bool
        
            Mouse drag handler.
        """
        pass

    def MouseLeave(self, view, timeOffset):
        """
        MouseLeave(self: ToolPlugin, view: View, timeOffset: float) -> bool
        
            Mouse leave handler.
        """
        pass

    def MouseMove(self, view, modifiers, x, y, timeOffset):
        """
        MouseMove(self: ToolPlugin, view: View, modifiers: KeyModifiers, x: int, y: int, timeOffset: float) -> bool
        
            Mouse move handler.
        """
        pass

    def MouseUp(self, view, modifiers, button, x, y, timeOffset):
        """
        MouseUp(self: ToolPlugin, view: View, modifiers: KeyModifiers, button: UInt16, x: int, y: int, timeOffset: float) -> bool
        
            Mouse up handler.
        """
        pass

    def OverlayRender(self, view, graphics):
        """
        OverlayRender(self: ToolPlugin, view: View, graphics: Graphics)
            Override to allow custom drawing overlayed on main render.
        """
        pass

    def Render(self, view, graphics):
        """
        Render(self: ToolPlugin, view: View, graphics: Graphics)
            Override to allow custom drawing in main render.
        """
        pass

    def WheelDrag(self, view, modifier, x, y, wheel, len, timeOffset):
        """
        WheelDrag(self: ToolPlugin, view: View, modifier: KeyModifiers, x: int, y: int, wheel: UInt16, len: float, timeOffset: float) -> bool
        
            WheelDrag handler.
        """
        pass


class ToolPluginRecord(PluginRecord):
    """ Represents an Autodesk.Navisworks.Api.Plugins.ToolPluginToolPlugin record in Navisworks """
    def LoadPlugin(self):
        """
        LoadPlugin(self: ToolPluginRecord) -> ToolPlugin
        
            Returns the plugin, loads it if required
        """
        pass

    def TryLoadPlugin(self):
        """
        TryLoadPlugin(self: ToolPluginRecord) -> ToolPlugin
        
            Returns the plugin, loads it if required
            Returns: null if plugin failed to load
        """
        pass

    LoadedPlugin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the plugin if loaded, otherwise null

Get: LoadedPlugin(self: ToolPluginRecord) -> ToolPlugin

"""



class ToolTipsAttribute(Attribute, _Attribute):
    """
    Defines tooltips for ribbon tabs and commands in the GUI system.
    
    ToolTipsAttribute(xaml: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, xaml):
        """ __new__(cls: type, xaml: str) """
        pass

    Xaml = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The file that specifies the tooltips for Ribbon tab and commands

Get: Xaml(self: ToolTipsAttribute) -> str

"""



class ToolTipsRecord(object):
    """ Represents the definition of tooltips for ribbon tabs and commands in the GUI system. """
    Xaml = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The path to the file that specifies the tool tips for the ribbon and commands

Get: Xaml(self: ToolTipsRecord) -> str

"""



