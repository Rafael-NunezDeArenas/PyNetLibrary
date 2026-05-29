# Auto-generated — Navisworks 24 — Autodesk.Navisworks.Api.Plugins

class AddInLocation:
    """.NET: Autodesk.Navisworks.Api.Plugins.AddInLocation"""
    def __init__(self, *args) -> None: ...
    ...

class AddInPlugin(Plugin):
    """.NET: Autodesk.Navisworks.Api.Plugins.AddInPlugin"""
    def __init__(self, *args) -> None: ...
    PluginRecord: PluginRecord
    DeveloperId: str
    Name: str
    Id: str
    def CanExecute(self, ) -> CommandState: ...
    def Execute(self, parameters: list) -> int: ...
    def TryShowHelp(self, ) -> bool: ...

class AddInPluginAttribute(Attribute):
    """.NET: Autodesk.Navisworks.Api.Plugins.AddInPluginAttribute"""
    def __init__(self, *args) -> None: ...
    ShortcutWindowTypes: str
    Shortcut: str
    CallCanExecute: CallCanExecute
    LoadForCanExecute: bool
    CanToggle: bool
    LargeIcon: str
    Icon: str
    Location: AddInLocation
    TypeId: object

class AddInPluginRecord(PluginRecord):
    """.NET: Autodesk.Navisworks.Api.Plugins.AddInPluginRecord"""
    def __init__(self, *args) -> None: ...
    ShortcutWindowTypes: str
    Shortcut: str
    CanToggle: bool
    LargeIcon: str
    Icon: str
    Location: AddInLocation
    LoadedPlugin: AddInPlugin
    InterfaceRecords: ReadOnlyCollection
    SupportsIsSelfEnabled: bool
    HasFailedIsSelfEnabled: bool
    HasFailedCreate: bool
    HasAttemptedCreate: bool
    LoadedPlugin: Plugin
    IsLoaded: bool
    IsEnabled: bool
    ExtendedToolTip: str
    ToolTip: str
    DisplayName: str
    PluginOptions: PluginOptions
    DeveloperId: str
    Name: str
    Id: str
    def CanExecute(self, ) -> CommandState: ...
    def Execute(self, parameters: list) -> int: ...
    def LoadPlugin(self, ) -> AddInPlugin: ...
    def TryLoadPlugin(self, ) -> AddInPlugin: ...

class CallCanExecute:
    """.NET: Autodesk.Navisworks.Api.Plugins.CallCanExecute"""
    def __init__(self, *args) -> None: ...
    ...

class ClashResultActionPlugin(Plugin):
    """.NET: Autodesk.Navisworks.Api.Plugins.ClashResultActionPlugin"""
    def __init__(self, *args) -> None: ...
    PluginRecord: PluginRecord
    DeveloperId: str
    Name: str
    Id: str
    def BeginExecute(self, ) -> None: ...
    def CanExecute(self, item: SavedItem) -> bool: ...
    def EndExecute(self, ) -> None: ...
    def ExecuteAction(self, item: SavedItem) -> bool: ...
    def SupportsMultipleItems(self, ) -> bool: ...

class ClashResultActionPluginRecord(PluginRecord):
    """.NET: Autodesk.Navisworks.Api.Plugins.ClashResultActionPluginRecord"""
    def __init__(self, *args) -> None: ...
    LoadedPlugin: ClashResultActionPlugin
    InterfaceRecords: ReadOnlyCollection
    SupportsIsSelfEnabled: bool
    HasFailedIsSelfEnabled: bool
    HasFailedCreate: bool
    HasAttemptedCreate: bool
    LoadedPlugin: Plugin
    IsLoaded: bool
    IsEnabled: bool
    ExtendedToolTip: str
    ToolTip: str
    DisplayName: str
    PluginOptions: PluginOptions
    DeveloperId: str
    Name: str
    Id: str
    def LoadPlugin(self, ) -> ClashResultActionPlugin: ...
    def TryLoadPlugin(self, ) -> ClashResultActionPlugin: ...

class CommandAttribute(Attribute):
    """.NET: Autodesk.Navisworks.Api.Plugins.CommandAttribute"""
    def __init__(self, *args) -> None: ...
    ShortcutWindowTypes: str
    Shortcut: str
    CallCanExecute: CallCanExecute
    LoadForCanExecute: bool
    CanToggle: bool
    ExtendedToolTip: str
    ToolTip: str
    LargeIcon: str
    Icon: str
    DisplayName: str
    Name: str
    TypeId: object

class CommandHandlerPlugin(Plugin):
    """.NET: Autodesk.Navisworks.Api.Plugins.CommandHandlerPlugin"""
    def __init__(self, *args) -> None: ...
    PluginRecord: PluginRecord
    DeveloperId: str
    Name: str
    Id: str
    def CanExecuteCommand(self, name: str) -> CommandState: ...
    def CanExecuteRibbonTab(self, name: str) -> bool: ...
    def ExecuteCommand(self, name: str, parameters: list) -> int: ...
    def TryShowCommandHelp(self, name: str) -> bool: ...

class CommandHandlerPluginRecord(PluginRecord):
    """.NET: Autodesk.Navisworks.Api.Plugins.CommandHandlerPluginRecord"""
    def __init__(self, *args) -> None: ...
    ToolTipsRecords: ReadOnlyCollection
    RibbonLayoutRecords: ReadOnlyCollection
    CommandRecords: ReadOnlyCollection
    RibbonTabRecords: ReadOnlyCollection
    LoadedPlugin: CommandHandlerPlugin
    InterfaceRecords: ReadOnlyCollection
    SupportsIsSelfEnabled: bool
    HasFailedIsSelfEnabled: bool
    HasFailedCreate: bool
    HasAttemptedCreate: bool
    LoadedPlugin: Plugin
    IsLoaded: bool
    IsEnabled: bool
    ExtendedToolTip: str
    ToolTip: str
    DisplayName: str
    PluginOptions: PluginOptions
    DeveloperId: str
    Name: str
    Id: str
    def CanExecuteCommand(self, commandId: str) -> CommandState: ...
    def CanExecuteRibbonTab(self, ribbonId: str) -> bool: ...
    def ExecuteCommand(self, commandId: str, parameters: list) -> int: ...
    def ExtractNameFromId(self, id: str) -> str: ...
    def LoadPlugin(self, ) -> CommandHandlerPlugin: ...
    def MakeIdFromName(self, name: str) -> str: ...
    def ShowCommandHelp(self, commandId: str) -> bool: ...
    def TryLoadPlugin(self, ) -> CommandHandlerPlugin: ...
    def TryShowCommandHelp(self, commandId: str) -> bool: ...

class CommandRecord:
    """.NET: Autodesk.Navisworks.Api.Plugins.CommandRecord"""
    def __init__(self, *args) -> None: ...
    ShortcutWindowTypes: str
    Shortcut: str
    CanToggle: bool
    ExtendedToolTip: str
    ToolTip: str
    LargeIcon: str
    Icon: str
    DisplayName: str
    Id: str

class CommandState:
    """.NET: Autodesk.Navisworks.Api.Plugins.CommandState"""
    def __init__(self, *args) -> None: ...
    OverrideDisplayName: str
    IsVisible: bool
    IsChecked: bool
    IsEnabled: bool

class CustomPlugin(Plugin):
    """.NET: Autodesk.Navisworks.Api.Plugins.CustomPlugin"""
    def __init__(self, *args) -> None: ...
    PluginRecord: PluginRecord
    DeveloperId: str
    Name: str
    Id: str

class CustomPluginRecord(PluginRecord):
    """.NET: Autodesk.Navisworks.Api.Plugins.CustomPluginRecord"""
    def __init__(self, *args) -> None: ...
    LoadedPlugin: CustomPlugin
    InterfaceRecords: ReadOnlyCollection
    SupportsIsSelfEnabled: bool
    HasFailedIsSelfEnabled: bool
    HasFailedCreate: bool
    HasAttemptedCreate: bool
    LoadedPlugin: Plugin
    IsLoaded: bool
    IsEnabled: bool
    ExtendedToolTip: str
    ToolTip: str
    DisplayName: str
    PluginOptions: PluginOptions
    DeveloperId: str
    Name: str
    Id: str
    def LoadPlugin(self, ) -> CustomPlugin: ...
    def TryLoadPlugin(self, ) -> CustomPlugin: ...

class DockPanePlugin(Plugin):
    """.NET: Autodesk.Navisworks.Api.Plugins.DockPanePlugin"""
    def __init__(self, *args) -> None: ...
    Visible: bool
    PluginRecord: PluginRecord
    DeveloperId: str
    Name: str
    Id: str
    def ActivatePane(self, ) -> None: ...
    def CreateControlPane(self, ) -> Control: ...
    def CreateHWndPane(self, parent: IWin32Window) -> IWin32Window: ...
    def DestroyControlPane(self, pane: Control) -> None: ...
    def DestroyHWndPane(self, pane: IWin32Window) -> None: ...
    def OnActivePaneChanged(self, isActive: bool) -> None: ...
    def OnVisibleChanged(self, ) -> None: ...
    def TryShowHelp(self, ) -> bool: ...
    def TryShowHelpAtScreenPoint(self, x: int, y: int) -> bool: ...
    def TryShowHelpForHighlight(self, ) -> bool: ...

class DockPanePluginAttribute(Attribute):
    """.NET: Autodesk.Navisworks.Api.Plugins.DockPanePluginAttribute"""
    def __init__(self, *args) -> None: ...
    FixedSize: bool
    AutoScroll: bool
    MinimumHeight: int
    MinimumWidth: int
    PreferredHeight: int
    PreferredWidth: int
    TypeId: object

class DockPanePluginRecord(PluginRecord):
    """.NET: Autodesk.Navisworks.Api.Plugins.DockPanePluginRecord"""
    def __init__(self, *args) -> None: ...
    FixedSize: bool
    AutoScroll: bool
    MinimumHeight: int
    MinimumWidth: int
    PreferredHeight: int
    PreferredWidth: int
    LoadedPlugin: DockPanePlugin
    InterfaceRecords: ReadOnlyCollection
    SupportsIsSelfEnabled: bool
    HasFailedIsSelfEnabled: bool
    HasFailedCreate: bool
    HasAttemptedCreate: bool
    LoadedPlugin: Plugin
    IsLoaded: bool
    IsEnabled: bool
    ExtendedToolTip: str
    ToolTip: str
    DisplayName: str
    PluginOptions: PluginOptions
    DeveloperId: str
    Name: str
    Id: str
    def LoadPlugin(self, ) -> DockPanePlugin: ...
    def TryLoadPlugin(self, ) -> DockPanePlugin: ...

class EventWatcherPlugin(Plugin):
    """.NET: Autodesk.Navisworks.Api.Plugins.EventWatcherPlugin"""
    def __init__(self, *args) -> None: ...
    PluginRecord: PluginRecord
    DeveloperId: str
    Name: str
    Id: str
    def OnLoaded(self, ) -> None: ...
    def OnUnloading(self, ) -> None: ...

class EventWatcherPluginRecord(PluginRecord):
    """.NET: Autodesk.Navisworks.Api.Plugins.EventWatcherPluginRecord"""
    def __init__(self, *args) -> None: ...
    LoadedPlugin: EventWatcherPlugin
    InterfaceRecords: ReadOnlyCollection
    SupportsIsSelfEnabled: bool
    HasFailedIsSelfEnabled: bool
    HasFailedCreate: bool
    HasAttemptedCreate: bool
    LoadedPlugin: Plugin
    IsLoaded: bool
    IsEnabled: bool
    ExtendedToolTip: str
    ToolTip: str
    DisplayName: str
    PluginOptions: PluginOptions
    DeveloperId: str
    Name: str
    Id: str
    def LoadPlugin(self, ) -> EventWatcherPlugin: ...
    def TryLoadPlugin(self, ) -> EventWatcherPlugin: ...

class ExecuteDisabledException(InvalidOperationException):
    """.NET: Autodesk.Navisworks.Api.Plugins.ExecuteDisabledException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class FileMetadata(NativeHandle):
    """.NET: Autodesk.Navisworks.Api.Plugins.FileMetadata"""
    def __init__(self, *args) -> None: ...
    Size: int
    RevisionId: str
    ModificationTime: DateTime
    HasSize: bool
    HasRevisionId: bool
    HasModificationTime: bool
    IsDisposed: bool
    IsReadOnly: bool
    @staticmethod
    def InternalCreator(handleIn: IntPtr, ownership: NativeHandleOwnership, parent: NativeHandle) -> FileMetadata: ...
    @staticmethod
    def InternalFactory(reserved: NativeHandleInit) -> NativeHandle: ...

class FileProtocolHandle:
    """.NET: Autodesk.Navisworks.Api.Plugins.FileProtocolHandle"""
    def __init__(self, *args) -> None: ...
    def Close(self, ) -> bool: ...
    def Read(self, data: list, offset: int, count: int) -> bool: ...
    def Write(self, data: list, offset: int, count: int) -> bool: ...

class FileProtocolOpenMode:
    """.NET: Autodesk.Navisworks.Api.Plugins.FileProtocolOpenMode"""
    def __init__(self, *args) -> None: ...
    ...

class FileProtocolPlugin(Plugin):
    """.NET: Autodesk.Navisworks.Api.Plugins.FileProtocolPlugin"""
    def __init__(self, *args) -> None: ...
    IsRemote: bool
    SupportsOwnCache: bool
    SupportsDirectOpen: bool
    SupportsGetPut: bool
    SupportedSchemes: IEnumerable
    PluginRecord: PluginRecord
    DeveloperId: str
    Name: str
    Id: str
    def GetFile(self, uri: Uri, localPath: str, progress: Progress) -> bool: ...
    def GetFileInfo(self, uri: Uri, info: FileMetadata) -> bool: ...
    def GetFileToCache(self, uri: Uri, progress: Progress, cachePath: str) -> bool: ...
    def OpenFile(self, uri: Uri, mode: FileProtocolOpenMode) -> FileProtocolHandle: ...
    def PutFile(self, localPath: str, uri: Uri, progress: Progress) -> bool: ...
    def TryGetDisplayName(self, uri: Uri, displayName: str) -> bool: ...
    def TryGetMRUPath(self, logicalUri: Uri, mruPath: str) -> bool: ...
    def TryGetPhysicalPath(self, logicalUri: Uri, physicalPath: str) -> bool: ...
    def TryGetVerboseDisplayName(self, uri: Uri, displayName: str) -> bool: ...
    def TryResolveAbsolute(self, originalParent: str, originalChild: str, resolvedParent: str, resolvedChild: str) -> bool: ...
    def TryResolveRelative(self, resolvedParent: str, relativeChild: str, resolvedChild: str) -> bool: ...

class FileProtocolPluginRecord(PluginRecord):
    """.NET: Autodesk.Navisworks.Api.Plugins.FileProtocolPluginRecord"""
    def __init__(self, *args) -> None: ...
    LoadedPlugin: FileProtocolPlugin
    InterfaceRecords: ReadOnlyCollection
    SupportsIsSelfEnabled: bool
    HasFailedIsSelfEnabled: bool
    HasFailedCreate: bool
    HasAttemptedCreate: bool
    LoadedPlugin: Plugin
    IsLoaded: bool
    IsEnabled: bool
    ExtendedToolTip: str
    ToolTip: str
    DisplayName: str
    PluginOptions: PluginOptions
    DeveloperId: str
    Name: str
    Id: str
    def LoadPlugin(self, ) -> FileProtocolPlugin: ...
    def TryLoadPlugin(self, ) -> FileProtocolPlugin: ...

class HomeScreenError:
    """.NET: Autodesk.Navisworks.Api.Plugins.HomeScreenError"""
    def __init__(self, *args) -> None: ...
    HttpStatusCode: int
    ErrorStatus: HomeScreenErrorStatus

class HomeScreenErrorStatus:
    """.NET: Autodesk.Navisworks.Api.Plugins.HomeScreenErrorStatus"""
    def __init__(self, *args) -> None: ...
    ...

class HomeScreenExtensionPlugin(Plugin):
    """.NET: Autodesk.Navisworks.Api.Plugins.HomeScreenExtensionPlugin"""
    def __init__(self, *args) -> None: ...
    HostObject: object
    HostObjectName: str
    FrameUrl: Uri
    PluginRecord: PluginRecord
    DeveloperId: str
    Name: str
    Id: str
    def GetErrorHtml(self, error: HomeScreenError) -> str: ...
    def GetHostObjectOrigins(self, ) -> list: ...
    def SetHostObjectOrigins(self, hostObjectOrigins: list) -> None: ...

class HomeScreenExtensionPluginRecord(PluginRecord):
    """.NET: Autodesk.Navisworks.Api.Plugins.HomeScreenExtensionPluginRecord"""
    def __init__(self, *args) -> None: ...
    InterfaceRecords: ReadOnlyCollection
    SupportsIsSelfEnabled: bool
    HasFailedIsSelfEnabled: bool
    HasFailedCreate: bool
    HasAttemptedCreate: bool
    LoadedPlugin: Plugin
    IsLoaded: bool
    IsEnabled: bool
    ExtendedToolTip: str
    ToolTip: str
    DisplayName: str
    PluginOptions: PluginOptions
    DeveloperId: str
    Name: str
    Id: str
    def LoadPlugin(self, ) -> HomeScreenExtensionPlugin: ...

class InputPlugin(Plugin):
    """.NET: Autodesk.Navisworks.Api.Plugins.InputPlugin"""
    def __init__(self, *args) -> None: ...
    PluginRecord: PluginRecord
    DeveloperId: str
    Name: str
    Id: str
    def ContextMenu(self, view: View, x: int, y: int) -> bool: ...
    def GetCursor(self, view: View, modifier: KeyModifiers) -> Cursor: ...
    def GetHelpIdAtPoint(self, view: View, x: int, y: int) -> HelpIdResult: ...
    def GetHelpIdForHighlight(self, view: View) -> HelpIdResult: ...
    def GetTooltip(self, view: View, x: int, y: int) -> TooltipResult: ...
    def KeyDown(self, view: View, modifier: KeyModifiers, key: int, timeOffset: float) -> bool: ...
    def KeyDrag(self, view: View, modifier: KeyModifiers, timeOffset: float) -> bool: ...
    def KeyUp(self, view: View, modifier: KeyModifiers, key: int, timeOffset: float) -> bool: ...
    def ModifierKeyDown(self, view: View, modifier: KeyModifiers, timeOffset: float) -> bool: ...
    def ModifierKeyUp(self, view: View, modifier: KeyModifiers, timeOffset: float) -> bool: ...
    def MouseDown(self, view: View, modifiers: KeyModifiers, button: int, x: int, y: int, timeOffset: float) -> bool: ...
    def MouseDrag(self, view: View, modifiers: KeyModifiers, x: int, y: int, timeOffset: float) -> bool: ...
    def MouseLeave(self, view: View, timeOffset: float) -> bool: ...
    def MouseMove(self, view: View, modifiers: KeyModifiers, x: int, y: int, timeOffset: float) -> bool: ...
    def MouseUp(self, view: View, modifiers: KeyModifiers, button: int, x: int, y: int, timeOffset: float) -> bool: ...
    def WheelDrag(self, view: View, modifier: KeyModifiers, x: int, y: int, wheel: int, len: float, timeOffset: float) -> bool: ...

class InputPluginRecord(PluginRecord):
    """.NET: Autodesk.Navisworks.Api.Plugins.InputPluginRecord"""
    def __init__(self, *args) -> None: ...
    LoadedPlugin: InputPlugin
    InterfaceRecords: ReadOnlyCollection
    SupportsIsSelfEnabled: bool
    HasFailedIsSelfEnabled: bool
    HasFailedCreate: bool
    HasAttemptedCreate: bool
    LoadedPlugin: Plugin
    IsLoaded: bool
    IsEnabled: bool
    ExtendedToolTip: str
    ToolTip: str
    DisplayName: str
    PluginOptions: PluginOptions
    DeveloperId: str
    Name: str
    Id: str
    def LoadPlugin(self, ) -> InputPlugin: ...
    def TryLoadPlugin(self, ) -> InputPlugin: ...

class InterfaceAttribute(Attribute):
    """.NET: Autodesk.Navisworks.Api.Plugins.InterfaceAttribute"""
    def __init__(self, *args) -> None: ...
    UserData: str
    DisplayName: str
    DeveloperId: str
    Name: str
    TypeId: object

class InterfaceRecord:
    """.NET: Autodesk.Navisworks.Api.Plugins.InterfaceRecord"""
    def __init__(self, *args) -> None: ...
    UserData: str
    DisplayName: str
    DeveloperId: str
    Name: str
    Id: str

class Plugin:
    """.NET: Autodesk.Navisworks.Api.Plugins.Plugin"""
    def __init__(self, *args) -> None: ...
    PluginRecord: PluginRecord
    DeveloperId: str
    Name: str
    Id: str
    def GetString(self, name: str) -> str: ...
    def GetStringSafe(self, name: str) -> str: ...
    def TryGetString(self, name: str) -> str: ...

class PluginAttribute(Attribute):
    """.NET: Autodesk.Navisworks.Api.Plugins.PluginAttribute"""
    def __init__(self, *args) -> None: ...
    SupportsIsSelfEnabled: bool
    Options: PluginOptions
    ExtendedToolTip: str
    ToolTip: str
    DisplayName: str
    DeveloperId: str
    Name: str
    TypeId: object

class PluginLoadException(InvalidOperationException):
    """.NET: Autodesk.Navisworks.Api.Plugins.PluginLoadException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class PluginOptions:
    """.NET: Autodesk.Navisworks.Api.Plugins.PluginOptions"""
    def __init__(self, *args) -> None: ...
    ...

class PluginRecord:
    """.NET: Autodesk.Navisworks.Api.Plugins.PluginRecord"""
    def __init__(self, *args) -> None: ...
    InterfaceRecords: ReadOnlyCollection
    SupportsIsSelfEnabled: bool
    HasFailedIsSelfEnabled: bool
    HasFailedCreate: bool
    HasAttemptedCreate: bool
    LoadedPlugin: Plugin
    IsLoaded: bool
    IsEnabled: bool
    ExtendedToolTip: str
    ToolTip: str
    DisplayName: str
    PluginOptions: PluginOptions
    DeveloperId: str
    Name: str
    Id: str
    def FindInterfaceRecord(self, interfaceId: str) -> InterfaceRecord: ...
    def LoadPlugin(self, ) -> Plugin: ...
    def TryLoadPlugin(self, ) -> Plugin: ...

class RenderPlugin(Plugin):
    """.NET: Autodesk.Navisworks.Api.Plugins.RenderPlugin"""
    def __init__(self, *args) -> None: ...
    PluginRecord: PluginRecord
    DeveloperId: str
    Name: str
    Id: str
    def MakeRenderBoundingBox(self, viewer: View) -> BoundingBox3D: ...
    def OverlayRender(self, view: View, graphics: Graphics) -> None: ...
    def Render(self, view: View, graphics: Graphics) -> None: ...

class RenderPluginRecord(PluginRecord):
    """.NET: Autodesk.Navisworks.Api.Plugins.RenderPluginRecord"""
    def __init__(self, *args) -> None: ...
    LoadedPlugin: RenderPlugin
    InterfaceRecords: ReadOnlyCollection
    SupportsIsSelfEnabled: bool
    HasFailedIsSelfEnabled: bool
    HasFailedCreate: bool
    HasAttemptedCreate: bool
    LoadedPlugin: Plugin
    IsLoaded: bool
    IsEnabled: bool
    ExtendedToolTip: str
    ToolTip: str
    DisplayName: str
    PluginOptions: PluginOptions
    DeveloperId: str
    Name: str
    Id: str
    def LoadPlugin(self, ) -> RenderPlugin: ...
    def TryLoadPlugin(self, ) -> RenderPlugin: ...

class RibbonLayoutAttribute(Attribute):
    """.NET: Autodesk.Navisworks.Api.Plugins.RibbonLayoutAttribute"""
    def __init__(self, *args) -> None: ...
    Xaml: str
    TypeId: object

class RibbonLayoutRecord:
    """.NET: Autodesk.Navisworks.Api.Plugins.RibbonLayoutRecord"""
    def __init__(self, *args) -> None: ...
    Xaml: str

class RibbonTabAttribute(Attribute):
    """.NET: Autodesk.Navisworks.Api.Plugins.RibbonTabAttribute"""
    def __init__(self, *args) -> None: ...
    CallCanExecute: CallCanExecute
    LoadForCanExecute: bool
    DisplayName: str
    Name: str
    TypeId: object

class RibbonTabRecord:
    """.NET: Autodesk.Navisworks.Api.Plugins.RibbonTabRecord"""
    def __init__(self, *args) -> None: ...
    DisplayName: str
    Id: str

class StringsAttribute(Attribute):
    """.NET: Autodesk.Navisworks.Api.Plugins.StringsAttribute"""
    def __init__(self, *args) -> None: ...
    FileName: str
    TypeId: object

class ToolPlugin(Plugin):
    """.NET: Autodesk.Navisworks.Api.Plugins.ToolPlugin"""
    def __init__(self, *args) -> None: ...
    PluginRecord: PluginRecord
    DeveloperId: str
    Name: str
    Id: str
    def ContextMenu(self, view: View, x: int, y: int) -> bool: ...
    def GetCursor(self, view: View, modifier: KeyModifiers) -> Cursor: ...
    def GetHelpIdAtPoint(self, view: View, x: int, y: int) -> HelpIdResult: ...
    def GetHelpIdForHighlight(self, view: View) -> HelpIdResult: ...
    def GetTooltip(self, view: View, x: int, y: int) -> TooltipResult: ...
    def KeyDown(self, view: View, modifier: KeyModifiers, key: int, timeOffset: float) -> bool: ...
    def KeyDrag(self, view: View, modifier: KeyModifiers, timeOffset: float) -> bool: ...
    def KeyUp(self, view: View, modifier: KeyModifiers, key: int, timeOffset: float) -> bool: ...
    def MakeRenderBoundingBox(self, viewer: View) -> BoundingBox3D: ...
    def ModifierKeyDown(self, view: View, modifier: KeyModifiers, timeOffset: float) -> bool: ...
    def ModifierKeyUp(self, view: View, modifier: KeyModifiers, timeOffset: float) -> bool: ...
    def MouseDown(self, view: View, modifiers: KeyModifiers, button: int, x: int, y: int, timeOffset: float) -> bool: ...
    def MouseDrag(self, view: View, modifiers: KeyModifiers, x: int, y: int, timeOffset: float) -> bool: ...
    def MouseLeave(self, view: View, timeOffset: float) -> bool: ...
    def MouseMove(self, view: View, modifiers: KeyModifiers, x: int, y: int, timeOffset: float) -> bool: ...
    def MouseUp(self, view: View, modifiers: KeyModifiers, button: int, x: int, y: int, timeOffset: float) -> bool: ...
    def OverlayRender(self, view: View, graphics: Graphics) -> None: ...
    def Render(self, view: View, graphics: Graphics) -> None: ...
    def WheelDrag(self, view: View, modifier: KeyModifiers, x: int, y: int, wheel: int, len: float, timeOffset: float) -> bool: ...

class ToolPluginRecord(PluginRecord):
    """.NET: Autodesk.Navisworks.Api.Plugins.ToolPluginRecord"""
    def __init__(self, *args) -> None: ...
    LoadedPlugin: ToolPlugin
    InterfaceRecords: ReadOnlyCollection
    SupportsIsSelfEnabled: bool
    HasFailedIsSelfEnabled: bool
    HasFailedCreate: bool
    HasAttemptedCreate: bool
    LoadedPlugin: Plugin
    IsLoaded: bool
    IsEnabled: bool
    ExtendedToolTip: str
    ToolTip: str
    DisplayName: str
    PluginOptions: PluginOptions
    DeveloperId: str
    Name: str
    Id: str
    def LoadPlugin(self, ) -> ToolPlugin: ...
    def TryLoadPlugin(self, ) -> ToolPlugin: ...

class ToolTipsAttribute(Attribute):
    """.NET: Autodesk.Navisworks.Api.Plugins.ToolTipsAttribute"""
    def __init__(self, *args) -> None: ...
    Xaml: str
    TypeId: object

class ToolTipsRecord:
    """.NET: Autodesk.Navisworks.Api.Plugins.ToolTipsRecord"""
    def __init__(self, *args) -> None: ...
    Xaml: str
