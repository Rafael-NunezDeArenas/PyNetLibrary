# Auto-generated — Revit 2027 — Autodesk.Revit.UI.Events

class ApplicationClosingEventArgs(RevitAPIPreEventArgs):
    """.NET: Autodesk.Revit.UI.Events.ApplicationClosingEventArgs"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Cancellable: bool

class BeforeExecutedEventArgs(CommandEventArgs):
    """.NET: Autodesk.Revit.UI.Events.BeforeExecutedEventArgs"""
    def __init__(self, *args) -> None: ...
    UsingCommandData: bool
    CommandId: RevitCommandId
    ActiveDocument: Document
    Cancellable: bool
    Cancel: bool

class CanExecuteEventArgs(CommandEventArgs):
    """.NET: Autodesk.Revit.UI.Events.CanExecuteEventArgs"""
    def __init__(self, *args) -> None: ...
    IsChecked: bool
    CanExecute: bool
    CommandId: RevitCommandId
    ActiveDocument: Document
    Cancellable: bool
    Cancel: bool
    def GetSelectedCategoryIds(self, ) -> ICollection: ...

class ComboBoxCurrentChangedEventArgs(RibbonItemEventArgs):
    """.NET: Autodesk.Revit.UI.Events.ComboBoxCurrentChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    NewValue: ComboBoxMember
    OldValue: ComboBoxMember
    Application: UIApplication

class ComboBoxDropDownClosedEventArgs(RibbonItemEventArgs):
    """.NET: Autodesk.Revit.UI.Events.ComboBoxDropDownClosedEventArgs"""
    def __init__(self, *args) -> None: ...
    Application: UIApplication

class ComboBoxDropDownOpenedEventArgs(RibbonItemEventArgs):
    """.NET: Autodesk.Revit.UI.Events.ComboBoxDropDownOpenedEventArgs"""
    def __init__(self, *args) -> None: ...
    Application: UIApplication

class CommandEventArgs(RevitEventArgs):
    """.NET: Autodesk.Revit.UI.Events.CommandEventArgs"""
    def __init__(self, *args) -> None: ...
    CommandId: RevitCommandId
    ActiveDocument: Document
    Cancellable: bool
    Cancel: bool

class DialogBoxData(APIObject):
    """.NET: Autodesk.Revit.UI.Events.DialogBoxData"""
    def __init__(self, *args) -> None: ...
    HelpId: int
    IsReadOnly: bool
    def OverrideResult(self, result: int) -> bool: ...

class DialogBoxShowingEventArgs(RevitAPIPreEventArgs):
    """.NET: Autodesk.Revit.UI.Events.DialogBoxShowingEventArgs"""
    def __init__(self, *args) -> None: ...
    DialogId: str
    IsValidObject: bool
    Cancellable: bool
    def OverrideResult(self, resultCode: int) -> bool: ...

class DisplayingOptionsDialogEventArgs(RevitAPIPreEventArgs):
    """.NET: Autodesk.Revit.UI.Events.DisplayingOptionsDialogEventArgs"""
    def __init__(self, *args) -> None: ...
    PagesCount: int
    IsValidObject: bool
    Cancellable: bool
    def AddTab(self, newTabName: str, tabbedDialogExtension: TabbedDialogExtension) -> None: ...

class DockableFrameFocusChangedEventArgs(RevitAPISingleEventArgs):
    """.NET: Autodesk.Revit.UI.Events.DockableFrameFocusChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    PaneId: DockablePaneId
    FocusGained: bool
    IsValidObject: bool
    Cancellable: bool

class DockableFrameVisibilityChangedEventArgs(RevitAPISingleEventArgs):
    """.NET: Autodesk.Revit.UI.Events.DockableFrameVisibilityChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    PaneId: DockablePaneId
    DockableFrameShown: bool
    IsValidObject: bool
    Cancellable: bool

class ExecutedEventArgs(CommandEventArgs):
    """.NET: Autodesk.Revit.UI.Events.ExecutedEventArgs"""
    def __init__(self, *args) -> None: ...
    CommandId: RevitCommandId
    ActiveDocument: Document
    Cancellable: bool
    Cancel: bool
    def GetJournalData(self, ) -> IDictionary: ...
    def SetJournalData(self, data: IDictionary) -> None: ...

class FabricationPartBrowserChangedEventArgs(RevitAPISingleEventArgs):
    """.NET: Autodesk.Revit.UI.Events.FabricationPartBrowserChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    NumberOfSolutions: int
    ServiceId: int
    Operation: FabricationPartBrowserOperation
    IsValidObject: bool
    Cancellable: bool
    def GetAllSolutionsPartsTypeCounts(self, ) -> IDictionary: ...
    def GetCurrentSolutionPartTypeIds(self, ) -> ISet: ...
    def GetFabricationPartTypeIds(self, ) -> ISet: ...
    def GetFilteredSolutionsPartsTypeCounts(self, ) -> IDictionary: ...
    def GetRequiredFabricationPartTypeIds(self, ) -> ISet: ...

class FabricationPartBrowserOperation:
    """.NET: Autodesk.Revit.UI.Events.FabricationPartBrowserOperation"""
    def __init__(self, *args) -> None: ...
    ...

class FormulaEditingEventArgs(RevitAPIPreEventArgs):
    """.NET: Autodesk.Revit.UI.Events.FormulaEditingEventArgs"""
    def __init__(self, *args) -> None: ...
    Formula: str
    ParameterId: ElementId
    CurrentDocument: Document
    IsValidObject: bool
    Cancellable: bool
    def Apply(self, formula: str) -> None: ...

class IdlingEventArgs(RevitAPIPreEventArgs):
    """.NET: Autodesk.Revit.UI.Events.IdlingEventArgs"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Cancellable: bool
    def SetRaiseWithoutDelay(self, ) -> None: ...

class MacroUpdatedEventArgs(RevitAPISingleEventArgs):
    """.NET: Autodesk.Revit.UI.Events.MacroUpdatedEventArgs"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Cancellable: bool

class MessageBoxData(DialogBoxData):
    """.NET: Autodesk.Revit.UI.Events.MessageBoxData"""
    def __init__(self, *args) -> None: ...
    DialogType: int
    Message: str
    HelpId: int
    IsReadOnly: bool

class MessageBoxShowingEventArgs(DialogBoxShowingEventArgs):
    """.NET: Autodesk.Revit.UI.Events.MessageBoxShowingEventArgs"""
    def __init__(self, *args) -> None: ...
    DialogType: int
    Message: str
    DialogId: str
    IsValidObject: bool
    Cancellable: bool

class RibbonItemEventArgs(EventArgs):
    """.NET: Autodesk.Revit.UI.Events.RibbonItemEventArgs"""
    def __init__(self, *args) -> None: ...
    Application: UIApplication

class SelectionChangedEventArgs(RevitAPISingleEventArgs):
    """.NET: Autodesk.Revit.UI.Events.SelectionChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    IsValidObject: bool
    Cancellable: bool
    def GetDocument(self, ) -> Document: ...
    def GetReferences(self, ) -> IList: ...
    def GetSelectedElements(self, ) -> ISet: ...

class TaskDialogShowingEventArgs(DialogBoxShowingEventArgs):
    """.NET: Autodesk.Revit.UI.Events.TaskDialogShowingEventArgs"""
    def __init__(self, *args) -> None: ...
    Message: str
    DialogId: str
    IsValidObject: bool
    Cancellable: bool

class TextBoxEnterPressedEventArgs(RibbonItemEventArgs):
    """.NET: Autodesk.Revit.UI.Events.TextBoxEnterPressedEventArgs"""
    def __init__(self, *args) -> None: ...
    Application: UIApplication

class ThemeChangedEventArgs(RevitAPISingleEventArgs):
    """.NET: Autodesk.Revit.UI.Events.ThemeChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    ThemeChangedType: ThemeType
    IsValidObject: bool
    Cancellable: bool

class TransferredProjectStandardsEventArgs(RevitAPISingleEventArgs):
    """.NET: Autodesk.Revit.UI.Events.TransferredProjectStandardsEventArgs"""
    def __init__(self, *args) -> None: ...
    TargetDocument: Document
    SourceDocument: Document
    IsValidObject: bool
    Cancellable: bool
    def GetSelectedExternalItems(self, ) -> IDictionary: ...

class TransferringProjectStandardsEventArgs(RevitAPIPreDocEventArgs):
    """.NET: Autodesk.Revit.UI.Events.TransferringProjectStandardsEventArgs"""
    def __init__(self, *args) -> None: ...
    TargetDocument: Document
    SourceDocument: Document
    Document: Document
    IsValidObject: bool
    Cancellable: bool
    def GetExternalItems(self, ) -> IDictionary: ...
    def SetExternalItems(self, externalItems: IDictionary) -> None: ...

class ViewActivatedEventArgs(RevitAPIPostDocEventArgs):
    """.NET: Autodesk.Revit.UI.Events.ViewActivatedEventArgs"""
    def __init__(self, *args) -> None: ...
    PreviousActiveView: View
    CurrentActiveView: View
    Document: Document
    Status: RevitAPIEventStatus
    IsValidObject: bool
    Cancellable: bool

class ViewActivatingEventArgs(RevitAPIPreDocEventArgs):
    """.NET: Autodesk.Revit.UI.Events.ViewActivatingEventArgs"""
    def __init__(self, *args) -> None: ...
    CurrentActiveView: View
    NewActiveView: View
    Document: Document
    IsValidObject: bool
    Cancellable: bool
