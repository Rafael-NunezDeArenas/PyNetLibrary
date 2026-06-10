# Auto-generated — Civil 26 — Autodesk.Civil.DataShortcuts

class DataShortcutEntityType:
    """.NET: Autodesk.Civil.DataShortcuts.DataShortcutEntityType"""
    def __init__(self, *args) -> None: ...
    ...

class DataShortcutKey(DisposableWrapper):
    """.NET: Autodesk.Civil.DataShortcuts.DataShortcutKey"""
    def __init__(self, *args) -> None: ...
    IsSourceDrawingExistent: bool
    SourceDrawing: str
    HandleHigh: int
    HandleLow: int
    Type: DataShortcutEntityType
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
