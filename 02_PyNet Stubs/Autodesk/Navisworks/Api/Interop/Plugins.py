# Auto-generated — Navisworks 24 — Autodesk.Navisworks.Api.Interop.Plugins

class LegacyManager:
    """.NET: Autodesk.Navisworks.Api.Interop.Plugins.LegacyManager"""
    def __init__(self, *args) -> None: ...
    Plugins: Collection
    @staticmethod
    def LoadPlugins(attribLoading: Attribute) -> int: ...

class LegacyPlugin:
    """.NET: Autodesk.Navisworks.Api.Interop.Plugins.LegacyPlugin"""
    def __init__(self, *args) -> None: ...
    PluginInterface: IPlugin
    DataDir: str
    AssemblyPrefix: str

class ModelDataPlugin(Plugin):
    """.NET: Autodesk.Navisworks.Api.Interop.Plugins.ModelDataPlugin"""
    def __init__(self, *args) -> None: ...
    PluginRecord: PluginRecord
    DeveloperId: str
    Name: str
    Id: str
    def ImportData(self, m: LcOpModel, filename: str) -> None: ...

class ModelDataPluginRecord(PluginRecord):
    """.NET: Autodesk.Navisworks.Api.Interop.Plugins.ModelDataPluginRecord"""
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
