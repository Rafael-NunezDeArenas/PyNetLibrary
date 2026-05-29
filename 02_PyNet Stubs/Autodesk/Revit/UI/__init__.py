# Auto-generated — Revit 2027 — Autodesk.Revit.UI

class AddInCommandBinding:
    """.NET: Autodesk.Revit.UI.AddInCommandBinding"""
    def __init__(self, *args) -> None: ...
    RevitCommandId: RevitCommandId

class ButtonData(RibbonItemData):
    """.NET: Autodesk.Revit.UI.ButtonData"""
    def __init__(self, *args) -> None: ...
    Image: ImageSource
    LargeImage: ImageSource
    Text: str
    ToolTipImage: ImageSource
    LongDescription: str
    IsValidObject: bool
    ToolTip: str
    Name: str

class ColorSelectionDialog:
    """.NET: Autodesk.Revit.UI.ColorSelectionDialog"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    OriginalColor: Color
    SelectedColor: Color
    def Dispose(self, ) -> None: ...
    def Show(self, ) -> ItemSelectionDialogResult: ...

class ComboBox(RibbonItem):
    """.NET: Autodesk.Revit.UI.ComboBox"""
    def __init__(self, *args) -> None: ...
    Image: ImageSource
    Current: ComboBoxMember
    ItemType: RibbonItemType
    Visible: bool
    Enabled: bool
    ToolTipImage: ImageSource
    LongDescription: str
    ToolTip: str
    ItemText: str
    Name: str
    def AddItem(self, memberData: ComboBoxMemberData) -> ComboBoxMember: ...
    def AddItems(self, memberData: IList) -> IList: ...
    def AddSeparator(self, ) -> None: ...
    def GetItems(self, ) -> IList: ...

class ComboBoxData(RibbonItemData):
    """.NET: Autodesk.Revit.UI.ComboBoxData"""
    def __init__(self, *args) -> None: ...
    Image: ImageSource
    ToolTipImage: ImageSource
    LongDescription: str
    IsValidObject: bool
    ToolTip: str
    Name: str

class ComboBoxMember(RibbonItem):
    """.NET: Autodesk.Revit.UI.ComboBoxMember"""
    def __init__(self, *args) -> None: ...
    GroupName: str
    Image: ImageSource
    ItemType: RibbonItemType
    Visible: bool
    Enabled: bool
    ToolTipImage: ImageSource
    LongDescription: str
    ToolTip: str
    ItemText: str
    Name: str

class ComboBoxMemberData(RibbonItemData):
    """.NET: Autodesk.Revit.UI.ComboBoxMemberData"""
    def __init__(self, *args) -> None: ...
    GroupName: str
    Image: ImageSource
    Text: str
    ToolTipImage: ImageSource
    LongDescription: str
    IsValidObject: bool
    ToolTip: str
    Name: str

class CommandMenuItem(MenuItem):
    """.NET: Autodesk.Revit.UI.CommandMenuItem"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def SetAvailabilityClassName(self, availabilityClassName: str) -> None: ...
    def SetToolTip(self, toolTip: str) -> None: ...

class ContextMenu:
    """.NET: Autodesk.Revit.UI.ContextMenu"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def AddItem(self, menuItem: MenuItem) -> None: ...
    def Dispose(self, ) -> None: ...

class ContextualHelp:
    """.NET: Autodesk.Revit.UI.ContextualHelp"""
    def __init__(self, *args) -> None: ...
    HelpTopicUrl: str
    HelpPath: str
    HelpType: ContextualHelpType
    def Launch(self, ) -> None: ...

class ContextualHelpType:
    """.NET: Autodesk.Revit.UI.ContextualHelpType"""
    def __init__(self, *args) -> None: ...
    ...

class DockPosition:
    """.NET: Autodesk.Revit.UI.DockPosition"""
    def __init__(self, *args) -> None: ...
    ...

class DockablePane:
    """.NET: Autodesk.Revit.UI.DockablePane"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Id: DockablePaneId
    def Dispose(self, ) -> None: ...
    def GetTitle(self, ) -> str: ...
    def Hide(self, ) -> None: ...
    def IsShown(self, ) -> bool: ...
    @staticmethod
    def PaneExists(id: DockablePaneId) -> bool: ...
    @staticmethod
    def PaneIsBuiltIn(id: DockablePaneId) -> bool: ...
    @staticmethod
    def PaneIsRegistered(id: DockablePaneId) -> bool: ...
    def SetTitle(self, title: str) -> None: ...
    def Show(self, ) -> None: ...

class DockablePaneId(GuidEnum):
    """.NET: Autodesk.Revit.UI.DockablePaneId"""
    def __init__(self, *args) -> None: ...
    Guid: Guid

class DockablePaneProviderData:
    """.NET: Autodesk.Revit.UI.DockablePaneProviderData"""
    def __init__(self, *args) -> None: ...
    VisibleByDefault: bool
    EditorInteraction: EditorInteraction
    ContextualHelp: ContextualHelp
    InitialState: DockablePaneState
    FrameworkElementCreator: IFrameworkElementCreator
    FrameworkElement: FrameworkElement
    def GetFrameworkElement(self, ) -> FrameworkElement: ...

class DockablePaneState:
    """.NET: Autodesk.Revit.UI.DockablePaneState"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    MinimumHeight: int
    MinimumWidth: int
    TabBehind: DockablePaneId
    FloatingRectangle: Rectangle
    DockPosition: DockPosition
    def Dispose(self, ) -> None: ...
    def SetFloatingRectangle(self, rect: Rectangle) -> None: ...

class DockablePanes:
    """.NET: Autodesk.Revit.UI.DockablePanes"""
    def __init__(self, *args) -> None: ...
    ...

class DoubleClickAction:
    """.NET: Autodesk.Revit.UI.DoubleClickAction"""
    def __init__(self, *args) -> None: ...
    ...

class DoubleClickOptions:
    """.NET: Autodesk.Revit.UI.DoubleClickOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...
    def GetAction(self, target: DoubleClickTarget) -> DoubleClickAction: ...
    @staticmethod
    def GetDoubleClickOptions() -> DoubleClickOptions: ...
    def IsSupportedAction(self, target: DoubleClickTarget, action: DoubleClickAction) -> bool: ...
    def SetAction(self, target: DoubleClickTarget, action: DoubleClickAction) -> None: ...

class DoubleClickTarget:
    """.NET: Autodesk.Revit.UI.DoubleClickTarget"""
    def __init__(self, *args) -> None: ...
    ...

class EditorInteraction:
    """.NET: Autodesk.Revit.UI.EditorInteraction"""
    def __init__(self, *args) -> None: ...
    InteractionType: EditorInteractionType

class EditorInteractionType:
    """.NET: Autodesk.Revit.UI.EditorInteractionType"""
    def __init__(self, *args) -> None: ...
    ...

class ExternalApplicationArray(APIObject):
    """.NET: Autodesk.Revit.UI.ExternalApplicationArray"""
    def __init__(self, *args) -> None: ...
    Item: IExternalApplication
    IsEmpty: bool
    Size: int
    IsReadOnly: bool
    def Append(self, item: IExternalApplication) -> None: ...
    def Clear(self, ) -> None: ...
    def ForwardIterator(self, ) -> ExternalApplicationArrayIterator: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, item: IExternalApplication, index: int) -> None: ...
    def ReverseIterator(self, ) -> ExternalApplicationArrayIterator: ...

class ExternalApplicationArrayIterator(APIObject):
    """.NET: Autodesk.Revit.UI.ExternalApplicationArrayIterator"""
    def __init__(self, *args) -> None: ...
    Current: object
    IsReadOnly: bool
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ExternalCommandData(APIObject):
    """.NET: Autodesk.Revit.UI.ExternalCommandData"""
    def __init__(self, *args) -> None: ...
    JournalData: IDictionary
    View: View
    Application: UIApplication
    IsReadOnly: bool

class ExternalCommandsData:
    """.NET: Autodesk.Revit.UI.ExternalCommandsData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    AvailabilityClassName: str
    AssemblyName: str
    ClassName: str
    def Dispose(self, ) -> None: ...

class ExternalDataManagerCommand:
    """.NET: Autodesk.Revit.UI.ExternalDataManagerCommand"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Executable: bool
    SupportMultiItems: bool
    Tooltip: str
    Name: str
    Id: ExternalDataManagerCommandId
    def Dispose(self, ) -> None: ...
    @staticmethod
    def RegisterCommand(command: ExternalDataManagerCommand) -> None: ...

class ExternalDataManagerCommandId(GuidEnum):
    """.NET: Autodesk.Revit.UI.ExternalDataManagerCommandId"""
    def __init__(self, *args) -> None: ...
    Guid: Guid

class ExternalDataManagerCommands:
    """.NET: Autodesk.Revit.UI.ExternalDataManagerCommands"""
    def __init__(self, *args) -> None: ...
    ...

class ExternalDataManagerDataItem:
    """.NET: Autodesk.Revit.UI.ExternalDataManagerDataItem"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Version: str
    Count: int
    PathType: str
    Path: str
    Resolution: str
    Size: int
    ReferenceType: str
    Status: LinkedFileStatus
    Name: str
    def Dispose(self, ) -> None: ...
    def GetId(self, ) -> ExternalDataManagerDataItemId: ...
    def SetId(self, id: ExternalDataManagerDataItemId) -> None: ...

class ExternalDataManagerDataItemId:
    """.NET: Autodesk.Revit.UI.ExternalDataManagerDataItemId"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Id: int
    def Dispose(self, ) -> None: ...

class ExternalDataManagerTool:
    """.NET: Autodesk.Revit.UI.ExternalDataManagerTool"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    CommandId: ExternalDataManagerCommandId
    def Dispose(self, ) -> None: ...
    def GetChildCommandIds(self, ) -> IList: ...
    def SetChildCommandIds(self, childCommandIds: IList) -> None: ...

class ExternalEvent:
    """.NET: Autodesk.Revit.UI.ExternalEvent"""
    def __init__(self, *args) -> None: ...
    IsPending: bool
    @staticmethod
    def Create(handler: IExternalEventHandler) -> ExternalEvent: ...
    @staticmethod
    def CreateJournalable(handler: IExternalEventHandler) -> ExternalEvent: ...
    def Dispose(self, ) -> None: ...
    def Raise(self, ) -> ExternalEventRequest: ...

class ExternalEventRequest:
    """.NET: Autodesk.Revit.UI.ExternalEventRequest"""
    def __init__(self, *args) -> None: ...
    ...

class FaceBasedPlacementType:
    """.NET: Autodesk.Revit.UI.FaceBasedPlacementType"""
    def __init__(self, *args) -> None: ...
    ...

class FamilyInstancePlacingArgs:
    """.NET: Autodesk.Revit.UI.FamilyInstancePlacingArgs"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    TooltipMessage: str
    StatusMessage: str
    IsBanned: bool
    ActiveView: View
    def Dispose(self, ) -> None: ...

class FileDialog:
    """.NET: Autodesk.Revit.UI.FileDialog"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    DefaultFilterEntry: str
    Title: str
    Filter: str
    def Dispose(self, ) -> None: ...
    def GetSelectedModelPath(self, ) -> ModelPath: ...
    @staticmethod
    def IsValidFilterString(filterString: str) -> bool: ...
    def Show(self, ) -> ItemSelectionDialogResult: ...

class FileOpenDialog(FileDialog):
    """.NET: Autodesk.Revit.UI.FileOpenDialog"""
    def __init__(self, *args) -> None: ...
    ShowPreview: bool
    IsValidObject: bool
    DefaultFilterEntry: str
    Title: str
    Filter: str

class FileSaveDialog(FileDialog):
    """.NET: Autodesk.Revit.UI.FileSaveDialog"""
    def __init__(self, *args) -> None: ...
    InitialFileName: str
    IsValidObject: bool
    DefaultFilterEntry: str
    Title: str
    Filter: str

class FilterDialog:
    """.NET: Autodesk.Revit.UI.FilterDialog"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    NewFilterName: str
    FilterToSelect: ElementId
    NewFilterId: ElementId
    def Dispose(self, ) -> None: ...
    def Show(self, ) -> None: ...

class IContextMenuCreator:
    """.NET: Autodesk.Revit.UI.IContextMenuCreator"""
    def __init__(self, *args) -> None: ...
    def BuildContextMenu(self, menu: ContextMenu) -> None: ...

class IControllableDropHandler:
    """.NET: Autodesk.Revit.UI.IControllableDropHandler"""
    def __init__(self, *args) -> None: ...
    def CanExecute(self, document: UIDocument, data: object, dropViewId: ElementId) -> bool: ...

class IDockablePaneProvider:
    """.NET: Autodesk.Revit.UI.IDockablePaneProvider"""
    def __init__(self, *args) -> None: ...
    def SetupDockablePane(self, data: DockablePaneProviderData) -> None: ...

class IDropHandler:
    """.NET: Autodesk.Revit.UI.IDropHandler"""
    def __init__(self, *args) -> None: ...
    def Execute(self, document: UIDocument, data: object) -> None: ...

class IExternalApplication:
    """.NET: Autodesk.Revit.UI.IExternalApplication"""
    def __init__(self, *args) -> None: ...
    def OnShutdown(self, application: UIControlledApplication) -> Result: ...
    def OnStartup(self, application: UIControlledApplication) -> Result: ...

class IExternalCommand:
    """.NET: Autodesk.Revit.UI.IExternalCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, commandData: ExternalCommandData, message: str, elements: ElementSet) -> Result: ...

class IExternalCommandAvailability:
    """.NET: Autodesk.Revit.UI.IExternalCommandAvailability"""
    def __init__(self, *args) -> None: ...
    def IsCommandAvailable(self, applicationData: UIApplication, selectedCategories: CategorySet) -> bool: ...

class IExternalDataManagerServer:
    """.NET: Autodesk.Revit.UI.IExternalDataManagerServer"""
    def __init__(self, *args) -> None: ...
    def GetCommandsForAdd(self, ) -> IList: ...
    def GetContentTools(self, document: Document) -> IList: ...
    def GetData(self, document: Document) -> IList: ...
    def GetPreviewImage(self, document: Document, dataId: ExternalDataManagerDataItemId) -> IntPtr: ...
    def GetPreviewImageFile(self, document: Document, dataId: ExternalDataManagerDataItemId) -> str: ...
    def GetTitle(self, ) -> str: ...
    def IsCommandEnabled(self, document: Document, commandId: ExternalDataManagerCommandId, dataIds: IList) -> bool: ...
    def IsEnabledInFamilyDocuments(self, ) -> bool: ...
    def OnCommand(self, document: Document, commandId: ExternalDataManagerCommandId, dataIds: IList) -> None: ...

class IExternalEventHandler:
    """.NET: Autodesk.Revit.UI.IExternalEventHandler"""
    def __init__(self, *args) -> None: ...
    def Execute(self, app: UIApplication) -> None: ...
    def GetName(self, ) -> str: ...

class IExternalResourceUIServer:
    """.NET: Autodesk.Revit.UI.IExternalResourceUIServer"""
    def __init__(self, *args) -> None: ...
    def GetDBServerId(self, ) -> Guid: ...
    def HandleBrowseResult(self, resultType: ExternalResourceUIBrowseResultType, browsingItemPath: str) -> None: ...
    def HandleLoadResourceResults(self, document: Document, loadData: IList) -> None: ...

class IFCExternalServiceUIData:
    """.NET: Autodesk.Revit.UI.IFCExternalServiceUIData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Document: Document
    IsReset: bool
    ParamId: ElementId
    SelectedIFCItem: str
    def Dispose(self, ) -> None: ...
    def GetParentHwnd(self, ) -> IntPtr: ...
    def GetRevitElementIds(self, ) -> IList: ...

class IFrameworkElementCreator:
    """.NET: Autodesk.Revit.UI.IFrameworkElementCreator"""
    def __init__(self, *args) -> None: ...
    def CreateFrameworkElement(self, ) -> FrameworkElement: ...

class IIFCEntityTreeUIServer:
    """.NET: Autodesk.Revit.UI.IIFCEntityTreeUIServer"""
    def __init__(self, *args) -> None: ...
    def ShowDialog(self, data: IFCExternalServiceUIData) -> bool: ...

class IRevisionsOnSheetUIServer:
    """.NET: Autodesk.Revit.UI.IRevisionsOnSheetUIServer"""
    def __init__(self, *args) -> None: ...
    def ShowDialog(self, data: RevisionsOnSheetUIServiceData) -> bool: ...

class ITemporaryGraphicsHandler:
    """.NET: Autodesk.Revit.UI.ITemporaryGraphicsHandler"""
    def __init__(self, *args) -> None: ...
    def OnClick(self, data: TemporaryGraphicsCommandData) -> None: ...

class ItemData:
    """.NET: Autodesk.Revit.UI.ItemData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ToolTip: str
    Name: str
    def Dispose(self, ) -> None: ...

class ItemSelectionDialogResult:
    """.NET: Autodesk.Revit.UI.ItemSelectionDialogResult"""
    def __init__(self, *args) -> None: ...
    ...

class MenuItem:
    """.NET: Autodesk.Revit.UI.MenuItem"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class PostableCommand:
    """.NET: Autodesk.Revit.UI.PostableCommand"""
    def __init__(self, *args) -> None: ...
    ...

class PreviewControl(UserControl):
    """.NET: Autodesk.Revit.UI.PreviewControl"""
    def __init__(self, *args) -> None: ...
    ScrollbarVisibility: ScrollbarVisibility
    UIView: UIView
    ViewId: ElementId
    Content: object
    HasContent: bool
    ContentTemplate: DataTemplate
    ContentTemplateSelector: DataTemplateSelector
    ContentStringFormat: str
    BorderBrush: Brush
    BorderThickness: Thickness
    Background: Brush
    Foreground: Brush
    FontFamily: FontFamily
    FontSize: float
    FontStretch: FontStretch
    FontStyle: FontStyle
    FontWeight: FontWeight
    HorizontalContentAlignment: HorizontalAlignment
    VerticalContentAlignment: VerticalAlignment
    TabIndex: int
    IsTabStop: bool
    Padding: Thickness
    Template: ControlTemplate
    Style: Style
    OverridesDefaultStyle: bool
    UseLayoutRounding: bool
    Triggers: TriggerCollection
    TemplatedParent: DependencyObject
    Resources: ResourceDictionary
    DataContext: object
    BindingGroup: BindingGroup
    Language: XmlLanguage
    Name: str
    Tag: object
    InputScope: InputScope
    ActualWidth: float
    ActualHeight: float
    LayoutTransform: Transform
    Width: float
    MinWidth: float
    MaxWidth: float
    Height: float
    MinHeight: float
    MaxHeight: float
    FlowDirection: FlowDirection
    Margin: Thickness
    HorizontalAlignment: HorizontalAlignment
    VerticalAlignment: VerticalAlignment
    FocusVisualStyle: Style
    Cursor: Cursor
    ForceCursor: bool
    IsInitialized: bool
    IsLoaded: bool
    ToolTip: object
    ContextMenu: ContextMenu
    Parent: DependencyObject
    HasAnimatedProperties: bool
    InputBindings: InputBindingCollection
    CommandBindings: CommandBindingCollection
    AllowDrop: bool
    DesiredSize: Size
    IsMeasureValid: bool
    IsArrangeValid: bool
    RenderSize: Size
    RenderTransform: Transform
    RenderTransformOrigin: Point
    IsMouseDirectlyOver: bool
    IsMouseOver: bool
    IsStylusOver: bool
    IsKeyboardFocusWithin: bool
    IsMouseCaptured: bool
    IsMouseCaptureWithin: bool
    IsStylusDirectlyOver: bool
    IsStylusCaptured: bool
    IsStylusCaptureWithin: bool
    IsKeyboardFocused: bool
    IsInputMethodEnabled: bool
    Opacity: float
    OpacityMask: Brush
    BitmapEffect: BitmapEffect
    Effect: Effect
    BitmapEffectInput: BitmapEffectInput
    CacheMode: CacheMode
    Uid: str
    Visibility: Visibility
    ClipToBounds: bool
    Clip: Geometry
    SnapsToDevicePixels: bool
    IsFocused: bool
    IsEnabled: bool
    IsHitTestVisible: bool
    IsVisible: bool
    Focusable: bool
    PersistId: int
    IsManipulationEnabled: bool
    AreAnyTouchesOver: bool
    AreAnyTouchesDirectlyOver: bool
    AreAnyTouchesCapturedWithin: bool
    AreAnyTouchesCaptured: bool
    TouchesCaptured: IEnumerable
    TouchesCapturedWithin: IEnumerable
    TouchesOver: IEnumerable
    TouchesDirectlyOver: IEnumerable
    DependencyObjectType: DependencyObjectType
    IsSealed: bool
    Dispatcher: Dispatcher
    def Dispose(self, ) -> None: ...

class ProjectBrowserOptions:
    """.NET: Autodesk.Revit.UI.ProjectBrowserOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    AutoExpandSheetViewsOnViewPlacement: bool
    ShowViewPlacementOnSheetStatusIcons: bool
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetProjectBrowserOptions() -> ProjectBrowserOptions: ...

class PromptForFamilyInstancePlacementOptions:
    """.NET: Autodesk.Revit.UI.PromptForFamilyInstancePlacementOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    FaceBasedPlacementType: FaceBasedPlacementType
    SketchGalleryOptions: SketchGalleryOptions
    PlaceAirTerminalOnDuct: bool
    def Dispose(self, ) -> None: ...

class PulldownButton(RibbonButton):
    """.NET: Autodesk.Revit.UI.PulldownButton"""
    def __init__(self, *args) -> None: ...
    IsEnabledByContext: bool
    Image: ImageSource
    LargeImage: ImageSource
    ItemType: RibbonItemType
    Visible: bool
    Enabled: bool
    ToolTipImage: ImageSource
    LongDescription: str
    ToolTip: str
    ItemText: str
    Name: str
    def AddPushButton(self, buttonData: PushButtonData) -> PushButton: ...
    def AddSeparator(self, ) -> None: ...
    def GetItems(self, ) -> IList: ...

class PulldownButtonData(ButtonData):
    """.NET: Autodesk.Revit.UI.PulldownButtonData"""
    def __init__(self, *args) -> None: ...
    Image: ImageSource
    LargeImage: ImageSource
    Text: str
    ToolTipImage: ImageSource
    LongDescription: str
    IsValidObject: bool
    ToolTip: str
    Name: str

class PushButton(RibbonButton):
    """.NET: Autodesk.Revit.UI.PushButton"""
    def __init__(self, *args) -> None: ...
    AvailabilityClassName: str
    ClassName: str
    AssemblyName: str
    IsEnabledByContext: bool
    Image: ImageSource
    LargeImage: ImageSource
    ItemType: RibbonItemType
    Visible: bool
    Enabled: bool
    ToolTipImage: ImageSource
    LongDescription: str
    ToolTip: str
    ItemText: str
    Name: str

class PushButtonData(ButtonData):
    """.NET: Autodesk.Revit.UI.PushButtonData"""
    def __init__(self, *args) -> None: ...
    AvailabilityClassName: str
    AssemblyName: str
    ClassName: str
    Image: ImageSource
    LargeImage: ImageSource
    Text: str
    ToolTipImage: ImageSource
    LongDescription: str
    IsValidObject: bool
    ToolTip: str
    Name: str

class RadioButtonGroup(RibbonItem):
    """.NET: Autodesk.Revit.UI.RadioButtonGroup"""
    def __init__(self, *args) -> None: ...
    Current: ToggleButton
    ItemType: RibbonItemType
    Visible: bool
    Enabled: bool
    ToolTipImage: ImageSource
    LongDescription: str
    ToolTip: str
    ItemText: str
    Name: str
    def AddItem(self, buttonData: ToggleButtonData) -> ToggleButton: ...
    def AddItems(self, buttonData: IList) -> IList: ...
    def GetItems(self, ) -> IList: ...

class RadioButtonGroupData(RibbonItemData):
    """.NET: Autodesk.Revit.UI.RadioButtonGroupData"""
    def __init__(self, *args) -> None: ...
    ToolTipImage: ImageSource
    LongDescription: str
    IsValidObject: bool
    ToolTip: str
    Name: str

class Result:
    """.NET: Autodesk.Revit.UI.Result"""
    def __init__(self, *args) -> None: ...
    ...

class RevisionsOnSheetUIServiceData:
    """.NET: Autodesk.Revit.UI.RevisionsOnSheetUIServiceData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Document: Document
    IsReset: bool
    ParamId: ElementId
    def Dispose(self, ) -> None: ...
    def GetParentHwnd(self, ) -> IntPtr: ...
    def GetRevitElementIds(self, ) -> IList: ...

class RevitCommandId:
    """.NET: Autodesk.Revit.UI.RevitCommandId"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    HasBinding: bool
    CanHaveBinding: bool
    Id: int
    Name: str
    def Dispose(self, ) -> None: ...
    @staticmethod
    def LookupCommandId(name: str) -> RevitCommandId: ...
    @staticmethod
    def LookupPostableCommandId(postableCommand: PostableCommand) -> RevitCommandId: ...

class RevitLinkUIUtils:
    """.NET: Autodesk.Revit.UI.RevitLinkUIUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def ReportLinkLoadResults(doc: Document, loadResults: IDictionary) -> None: ...

class RibbonButton(RibbonItem):
    """.NET: Autodesk.Revit.UI.RibbonButton"""
    def __init__(self, *args) -> None: ...
    IsEnabledByContext: bool
    Image: ImageSource
    LargeImage: ImageSource
    ItemType: RibbonItemType
    Visible: bool
    Enabled: bool
    ToolTipImage: ImageSource
    LongDescription: str
    ToolTip: str
    ItemText: str
    Name: str

class RibbonButtonOptions:
    """.NET: Autodesk.Revit.UI.RibbonButtonOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    def Dispose(self, ) -> None: ...

class RibbonItem:
    """.NET: Autodesk.Revit.UI.RibbonItem"""
    def __init__(self, *args) -> None: ...
    ItemType: RibbonItemType
    Visible: bool
    Enabled: bool
    ToolTipImage: ImageSource
    LongDescription: str
    ToolTip: str
    ItemText: str
    Name: str
    def Equals(self, obj: object) -> bool: ...
    def GetContextualHelp(self, ) -> ContextualHelp: ...
    def SetContextualHelp(self, contextualHelp: ContextualHelp) -> None: ...

class RibbonItemData(ItemData):
    """.NET: Autodesk.Revit.UI.RibbonItemData"""
    def __init__(self, *args) -> None: ...
    ToolTipImage: ImageSource
    LongDescription: str
    IsValidObject: bool
    ToolTip: str
    Name: str
    def GetContextualHelp(self, ) -> ContextualHelp: ...
    def SetContextualHelp(self, contextualHelp: ContextualHelp) -> None: ...

class RibbonItemType:
    """.NET: Autodesk.Revit.UI.RibbonItemType"""
    def __init__(self, *args) -> None: ...
    ...

class RibbonPanel:
    """.NET: Autodesk.Revit.UI.RibbonPanel"""
    def __init__(self, *args) -> None: ...
    Enabled: bool
    Visible: bool
    Title: str
    Name: str
    def AddItem(self, itemData: RibbonItemData) -> RibbonItem: ...
    def AddSeparator(self, ) -> None: ...
    def AddSlideOut(self, ) -> None: ...
    def AddStackedItems(self, item1: RibbonItemData, item2: RibbonItemData, item3: RibbonItemData) -> IList: ...
    def Equals(self, obj: object) -> bool: ...
    def GetItems(self, ) -> IList: ...

class ScrollbarVisibility:
    """.NET: Autodesk.Revit.UI.ScrollbarVisibility"""
    def __init__(self, *args) -> None: ...
    ...

class SelectionUIOptions:
    """.NET: Autodesk.Revit.UI.SelectionUIOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ActivateControlsAndDimensionsOnMultiSelect: bool
    SelectPinned: bool
    DragOnSelection: bool
    SelectUnderlay: bool
    SelectLinks: bool
    SelectFaces: bool
    def Dispose(self, ) -> None: ...
    @staticmethod
    def ElementSelectsAsPinned(document: Document, element: Element) -> bool: ...
    @staticmethod
    def GetSelectionUIOptions() -> SelectionUIOptions: ...

class SeparatorItem(MenuItem):
    """.NET: Autodesk.Revit.UI.SeparatorItem"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class SizingUIUtils:
    """.NET: Autodesk.Revit.UI.SizingUIUtils"""
    def __init__(self, *args) -> None: ...
    ...

class SketchGalleryOptions:
    """.NET: Autodesk.Revit.UI.SketchGalleryOptions"""
    def __init__(self, *args) -> None: ...
    ...

class SplitButton(PulldownButton):
    """.NET: Autodesk.Revit.UI.SplitButton"""
    def __init__(self, *args) -> None: ...
    CurrentButton: PushButton
    IsSynchronizedWithCurrentItem: bool
    IsEnabledByContext: bool
    Image: ImageSource
    LargeImage: ImageSource
    ItemType: RibbonItemType
    Visible: bool
    Enabled: bool
    ToolTipImage: ImageSource
    LongDescription: str
    ToolTip: str
    ItemText: str
    Name: str

class SplitButtonData(PulldownButtonData):
    """.NET: Autodesk.Revit.UI.SplitButtonData"""
    def __init__(self, *args) -> None: ...
    Image: ImageSource
    LargeImage: ImageSource
    Text: str
    ToolTipImage: ImageSource
    LongDescription: str
    IsValidObject: bool
    ToolTip: str
    Name: str

class SubMenuItem(MenuItem):
    """.NET: Autodesk.Revit.UI.SubMenuItem"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool

class Tab:
    """.NET: Autodesk.Revit.UI.Tab"""
    def __init__(self, *args) -> None: ...
    ...

class TabbedDialogAction:
    """.NET: Autodesk.Revit.UI.TabbedDialogAction"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, ) -> None: ...

class TabbedDialogExtension:
    """.NET: Autodesk.Revit.UI.TabbedDialogExtension"""
    def __init__(self, *args) -> None: ...
    OnRestoreDefaultsAction: TabbedDialogAction
    OnCancelAction: TabbedDialogAction
    OnOKAction: TabbedDialogAction
    Control: UserControl
    def GetContextualHelp(self, ) -> ContextualHelp: ...
    def SetContextualHelp(self, contextualHelp: ContextualHelp) -> None: ...

class TableViewUIUtils:
    """.NET: Autodesk.Revit.UI.TableViewUIUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def TestCellAndPromptToEditTypeParameter(tableView: TableView, sectionType: SectionType, row: int, column: int) -> bool: ...

class TaskDialog(APIObject):
    """.NET: Autodesk.Revit.UI.TaskDialog"""
    def __init__(self, *args) -> None: ...
    EnableMarqueeProgressBar: bool
    TitleAutoPrefix: bool
    CommonButtons: TaskDialogCommonButtons
    MainIcon: TaskDialogIcon
    DefaultButton: TaskDialogResult
    AllowCancellation: bool
    FooterText: str
    ExtraCheckBoxText: str
    VerificationText: str
    ExpandedContent: str
    MainContent: str
    Id: str
    MainInstruction: str
    Title: str
    IsReadOnly: bool
    def AddCommandLink(self, id: TaskDialogCommandLinkId, mainContent: str, supportingContent: str) -> None: ...
    def EnableDoNotShowAgain(self, dialogId: str, enableDoNotShow: bool, doNotShowText: str) -> None: ...
    @staticmethod
    def Show(title: str, mainInstruction: str, buttons: TaskDialogCommonButtons, defaultButton: TaskDialogResult) -> TaskDialogResult: ...
    def WasExtraCheckBoxChecked(self, ) -> bool: ...
    def WasVerificationChecked(self, ) -> bool: ...

class TaskDialogCommandLinkId:
    """.NET: Autodesk.Revit.UI.TaskDialogCommandLinkId"""
    def __init__(self, *args) -> None: ...
    ...

class TaskDialogCommonButtons:
    """.NET: Autodesk.Revit.UI.TaskDialogCommonButtons"""
    def __init__(self, *args) -> None: ...
    ...

class TaskDialogIcon:
    """.NET: Autodesk.Revit.UI.TaskDialogIcon"""
    def __init__(self, *args) -> None: ...
    ...

class TaskDialogResult:
    """.NET: Autodesk.Revit.UI.TaskDialogResult"""
    def __init__(self, *args) -> None: ...
    ...

class TemporaryGraphicsCommandData:
    """.NET: Autodesk.Revit.UI.TemporaryGraphicsCommandData"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Index: int
    Document: Document
    def Dispose(self, ) -> None: ...

class TextBox(RibbonItem):
    """.NET: Autodesk.Revit.UI.TextBox"""
    def __init__(self, *args) -> None: ...
    Width: float
    ShowImageAsButton: bool
    Image: ImageSource
    Value: object
    SelectTextOnFocus: bool
    PromptText: str
    ItemType: RibbonItemType
    Visible: bool
    Enabled: bool
    ToolTipImage: ImageSource
    LongDescription: str
    ToolTip: str
    ItemText: str
    Name: str

class TextBoxData(RibbonItemData):
    """.NET: Autodesk.Revit.UI.TextBoxData"""
    def __init__(self, *args) -> None: ...
    Image: ImageSource
    ToolTipImage: ImageSource
    LongDescription: str
    IsValidObject: bool
    ToolTip: str
    Name: str

class TextEditorOptions:
    """.NET: Autodesk.Revit.UI.TextEditorOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ShowOpaqueBackground: bool
    ShowBorder: bool
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetTextEditorOptions() -> TextEditorOptions: ...

class ThemeType:
    """.NET: Autodesk.Revit.UI.ThemeType"""
    def __init__(self, *args) -> None: ...
    ...

class ThinLinesOptions:
    """.NET: Autodesk.Revit.UI.ThinLinesOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    AreThinLinesEnabled: bool
    def Dispose(self, ) -> None: ...

class ToggleButton(PushButton):
    """.NET: Autodesk.Revit.UI.ToggleButton"""
    def __init__(self, *args) -> None: ...
    AvailabilityClassName: str
    ClassName: str
    AssemblyName: str
    IsEnabledByContext: bool
    Image: ImageSource
    LargeImage: ImageSource
    ItemType: RibbonItemType
    Visible: bool
    Enabled: bool
    ToolTipImage: ImageSource
    LongDescription: str
    ToolTip: str
    ItemText: str
    Name: str

class ToggleButtonData(PushButtonData):
    """.NET: Autodesk.Revit.UI.ToggleButtonData"""
    def __init__(self, *args) -> None: ...
    AvailabilityClassName: str
    AssemblyName: str
    ClassName: str
    Image: ImageSource
    LargeImage: ImageSource
    Text: str
    ToolTipImage: ImageSource
    LongDescription: str
    IsValidObject: bool
    ToolTip: str
    Name: str

class UIApplication:
    """.NET: Autodesk.Revit.UI.UIApplication"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    IsViewerModeActive: bool
    Application: Application
    MainWindowHandle: IntPtr
    ProductIsRS: bool
    ActiveAddInId: AddInId
    LoadedApplications: ExternalApplicationArray
    DrawingAreaExtents: Rectangle
    MainWindowExtents: Rectangle
    ActiveUIDocument: UIDocument
    def CanPostCommand(self, commandId: RevitCommandId) -> bool: ...
    def CreateAddInCommandBinding(self, revitCommandId: RevitCommandId) -> AddInCommandBinding: ...
    def CreateRibbonPanel(self, tab: Tab, panelName: str) -> RibbonPanel: ...
    def CreateRibbonTab(self, tabName: str) -> None: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def DoDragDrop(dropData: object, handler: IDropHandler) -> None: ...
    def GetDockablePane(self, id: DockablePaneId) -> DockablePane: ...
    def GetRibbonPanels(self, tabName: str) -> List: ...
    def LoadAddIn(self, fileName: str) -> None: ...
    def LoadPackageContents(self, packageContentsPath: str) -> None: ...
    def OpenAndActivateDocument(self, modelPath: ModelPath, openOptions: OpenOptions, detachAndPrompt: bool, openFromCloudCallback: IOpenFromCloudCallback) -> UIDocument: ...
    def PostCommand(self, commandId: RevitCommandId) -> None: ...
    def RegisterContextMenu(self, fullClassName: str, creator: IContextMenuCreator) -> None: ...
    def RegisterDockablePane(self, id: DockablePaneId, title: str, provider: IDockablePaneProvider) -> None: ...
    def RemoveAddInCommandBinding(self, revitCommandId: RevitCommandId) -> None: ...

class UIControlledApplication:
    """.NET: Autodesk.Revit.UI.UIControlledApplication"""
    def __init__(self, *args) -> None: ...
    MainWindowHandle: IntPtr
    ProductIsRS: bool
    ActiveAddInId: AddInId
    LoadedApplications: ExternalApplicationArray
    IsViewerModeActive: bool
    IsLateAddinLoading: bool
    ControlledApplication: ControlledApplication
    def CreateAddInCommandBinding(self, revitCommandId: RevitCommandId) -> AddInCommandBinding: ...
    def CreateRibbonPanel(self, tab: Tab, panelName: str) -> RibbonPanel: ...
    def CreateRibbonTab(self, tabName: str) -> None: ...
    def GetDockablePane(self, id: DockablePaneId) -> DockablePane: ...
    def GetRibbonPanels(self, tabName: str) -> List: ...
    def LoadAddIn(self, fileName: str) -> None: ...
    def LoadPackageContents(self, packageContentsPath: str) -> None: ...
    def RegisterContextMenu(self, fullClassName: str, creator: IContextMenuCreator) -> None: ...
    def RegisterDockablePane(self, id: DockablePaneId, title: str, provider: IDockablePaneProvider) -> None: ...
    def RemoveAddInCommandBinding(self, revitCommandId: RevitCommandId) -> None: ...

class UIDocument:
    """.NET: Autodesk.Revit.UI.UIDocument"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ActiveGraphicalView: View
    Application: UIApplication
    Document: Document
    ActiveView: View
    Selection: Selection
    def CanPlaceElementType(self, elementType: ElementType) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetOpenUIViews(self, ) -> IList: ...
    def GetPlacementTypes(self, familySymbol: FamilySymbol, pDBView: View) -> IList: ...
    @staticmethod
    def GetRevitUIFamilyLoadOptions() -> IFamilyLoadOptions: ...
    def GetSketchGalleryOptions(self, familySymbol: FamilySymbol) -> IList: ...
    def PostRequestForElementTypePlacement(self, elementType: ElementType) -> None: ...
    def PromptForFamilyInstancePlacement(self, familySymbol: FamilySymbol, options: PromptForFamilyInstancePlacementOptions) -> None: ...
    def PromptToMatchElementType(self, elementType: ElementType) -> None: ...
    def PromptToPlaceElementTypeOnLegendView(self, elementType: ElementType) -> None: ...
    def PromptToPlaceViewOnSheet(self, view: View, allowReplaceExistingSheetViewport: bool) -> None: ...
    def RefreshActiveView(self, ) -> None: ...
    def RequestViewChange(self, view: View) -> None: ...
    def SaveAndClose(self, ) -> bool: ...
    def SaveAs(self, options: UISaveAsOptions) -> None: ...
    def ShowElements(self, elementIds: ICollection) -> None: ...
    def UpdateAllOpenViews(self, ) -> None: ...

class UIFabricationUtils:
    """.NET: Autodesk.Revit.UI.UIFabricationUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetOpenConnectorIndicatorAwayColor() -> Color: ...
    @staticmethod
    def GetOpenConnectorIndicatorPlanColor() -> Color: ...
    @staticmethod
    def GetOpenConnectorIndicatorTowardsColor() -> Color: ...
    @staticmethod
    def SetOpenConnectorIndicatorAwayColor(color: Color) -> None: ...
    @staticmethod
    def SetOpenConnectorIndicatorPlanColor(color: Color) -> None: ...
    @staticmethod
    def SetOpenConnectorIndicatorTowardsColor(color: Color) -> None: ...

class UISaveAsOptions:
    """.NET: Autodesk.Revit.UI.UISaveAsOptions"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ShowOverwriteWarning: bool
    def Dispose(self, ) -> None: ...

class UITheme:
    """.NET: Autodesk.Revit.UI.UITheme"""
    def __init__(self, *args) -> None: ...
    ...

class UIThemeManager:
    """.NET: Autodesk.Revit.UI.UIThemeManager"""
    def __init__(self, *args) -> None: ...
    CurrentCanvasTheme: UITheme
    FollowSystemColorTheme: bool
    CurrentTheme: UITheme
    @staticmethod
    def GetThemeName(frameTheme: UITheme) -> str: ...

class UIView:
    """.NET: Autodesk.Revit.UI.UIView"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    ViewId: ElementId
    def Close(self, ) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetWindowRectangle(self, ) -> Rectangle: ...
    def GetZoomCorners(self, ) -> IList: ...
    def Zoom(self, zoomFactor: float) -> None: ...
    def ZoomAndCenterRectangle(self, viewCorner1: XYZ, viewCorner2: XYZ) -> None: ...
    def ZoomSheetSize(self, ) -> None: ...
    def ZoomToFit(self, ) -> None: ...
