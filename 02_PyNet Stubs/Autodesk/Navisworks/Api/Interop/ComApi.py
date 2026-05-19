# encoding: utf-8
# module Autodesk.Navisworks.Api.Interop.ComApi calls itself ComApi
# from Autodesk.Navisworks.Interop.ComApi, Version=19.0.1374.1, Culture=neutral, PublicKeyToken=d85e58fa5af9b484
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class InwBase:
    # no doc
    def Copy(self):
        """ Copy(self: InwBase) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwBase, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwBase) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwBase, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwBase) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwBase) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwBase) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwBase) -> int

Set: nwLock(self: InwBase) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwBase) -> bool

Set: nwOwn(self: InwBase) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwBase) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwBase) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwBase) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwBase) -> str

"""



class InwClashPlugin:
    # no doc
    def iBeginTest(self, data):
        """ iBeginTest(self: InwClashPlugin) -> object """
        pass

    def iEndTest(self, data):
        """ iEndTest(self: InwClashPlugin) -> object """
        pass

    def iGetIgnoreDescription(self, description):
        """ iGetIgnoreDescription(self: InwClashPlugin) -> (bool, str) """
        pass

    def iIgnore(self, frag1, frag2, p_state):
        """ iIgnore(self: InwClashPlugin, frag1: InwOaFragment, frag2: InwOaFragment, p_state: InwOpState) -> bool """
        pass

    def InitialisePlugin(self, capbits, ver):
        """ InitialisePlugin(self: InwClashPlugin) -> (int, int) """
        pass

    def iXtension(self, vIn):
        """ iXtension(self: InwClashPlugin, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InwPlugin_Site(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwPlugin_Site) -> object """
        pass

    def GetApplication(self):
        """ GetApplication(self: InwPlugin_Site) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwPlugin_Site, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwPlugin_Site) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwPlugin_Site, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwPlugin_Site) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwPlugin_Site) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwPlugin_Site) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwPlugin_Site) -> int

Set: nwLock(self: InwPlugin_Site) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwPlugin_Site) -> bool

Set: nwOwn(self: InwPlugin_Site) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwPlugin_Site) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwPlugin_Site) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwPlugin_Site) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwPlugin_Site) -> str

"""



class InwClashPlugin_Site(InwPlugin_Site, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwClashPlugin_Site) -> object """
        pass

    def GetApplication(self):
        """ GetApplication(self: InwClashPlugin_Site) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwClashPlugin_Site, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwClashPlugin_Site) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwClashPlugin_Site, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwClashPlugin_Site) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwClashPlugin_Site) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwClashPlugin_Site) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwClashPlugin_Site) -> int

Set: nwLock(self: InwClashPlugin_Site) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwClashPlugin_Site) -> bool

Set: nwOwn(self: InwClashPlugin_Site) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwClashPlugin_Site) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwClashPlugin_Site) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwClashPlugin_Site) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwClashPlugin_Site) -> str

"""



class InwCollBase(IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwCollBase, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwCollBase) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwCollBase) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwCollBase, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwCollBase) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwCollBase, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwCollBase) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwCollBase, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwCollBase) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwCollBase) -> bool

"""



class InwClashTestsColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwClashTestsColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwClashTestsColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwClashTestsColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwClashTestsColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwClashTestsColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwClashTestsColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwClashTestsColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwClashTestsColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwClashTestsColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwClashTestsColl) -> bool

"""



class InwClippingPlaneColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwClippingPlaneColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwClippingPlaneColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwClippingPlaneColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwClippingPlaneColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwClippingPlaneColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwClippingPlaneColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwClippingPlaneColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwClippingPlaneColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwClippingPlaneColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwClippingPlaneColl) -> bool

"""



class InwClippingPlaneColl2(InwClippingPlaneColl, InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwClippingPlaneColl2, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwClippingPlaneColl2) """
        pass

    def CreatePlane(self, ndx):
        """ CreatePlane(self: InwClippingPlaneColl2, ndx: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwClippingPlaneColl2) -> IEnumerator """
        pass

    def GetRange(self):
        """ GetRange(self: InwClippingPlaneColl2) -> InwLBox3f """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwClippingPlaneColl2, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwClippingPlaneColl2) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwClippingPlaneColl2, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwClippingPlaneColl2) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwClippingPlaneColl2, ndx: int, p_newVal: object) """
        pass

    def SetRange(self, range):
        """ SetRange(self: InwClippingPlaneColl2, range: InwLBox3f) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwClippingPlaneColl2) -> int

"""

    CurrentPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPlane(self: InwClippingPlaneColl2) -> int

Set: CurrentPlane(self: InwClippingPlaneColl2) = value
"""

    Linked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Linked(self: InwClippingPlaneColl2) -> bool

Set: Linked(self: InwClippingPlaneColl2) = value
"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwClippingPlaneColl2) -> bool

"""



class InwCommentsColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwCommentsColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwCommentsColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwCommentsColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwCommentsColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwCommentsColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwCommentsColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwCommentsColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwCommentsColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwCommentsColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwCommentsColl) -> bool

"""



class InwControl:
    # no doc
    def AnimationCommand(self, cmd):
        """ AnimationCommand(self: InwControl, cmd: nwEAnimationCmd) -> nwEAnimCmdFlags """
        pass

    def AppendFile(self, file_name):
        """ AppendFile(self: InwControl, file_name: str) """
        pass

    def PickPixel(self, x, y, width, Flags, pos1, pos2, pos3):
        """ PickPixel(self: InwControl, x: int, y: int, width: int, Flags: nwEPickFlags) -> (InwOaFragment, object, object, object) """
        pass

    def SaveFile(self, file_name):
        """ SaveFile(self: InwControl, file_name: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwControl, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    HighlightSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighlightSelection(self: InwControl) -> bool

Set: HighlightSelection(self: InwControl) = value
"""

    LocalisationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalisationCode(self: InwControl) -> str

Set: LocalisationCode(self: InwControl) = value
"""

    NavigationMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NavigationMode(self: InwControl) -> nwENavigationMode

Set: NavigationMode(self: InwControl) = value
"""

    SecurityCertificate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecurityCertificate(self: InwControl) -> str

Set: SecurityCertificate(self: InwControl) = value
"""

    SelectionBehaviour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionBehaviour(self: InwControl) -> nwESelectionBehaviour

Set: SelectionBehaviour(self: InwControl) = value
"""

    ShowProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowProgress(self: InwControl) -> bool

Set: ShowProgress(self: InwControl) = value
"""

    SRC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SRC(self: InwControl) -> str

Set: SRC(self: InwControl) = value
"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: InwControl) -> InwOpState

"""

    UserModeSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserModeSelection(self: InwControl) -> bool

Set: UserModeSelection(self: InwControl) = value
"""

    _State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: _State(self: InwControl) -> str

Set: _State(self: InwControl) = value
"""



class InwControl2(InwControl):
    # no doc
    def AnimationCommand(self, cmd):
        """ AnimationCommand(self: InwControl2, cmd: nwEAnimationCmd) -> nwEAnimCmdFlags """
        pass

    def AppendFile(self, file_name):
        """ AppendFile(self: InwControl2, file_name: str) """
        pass

    def PickPixel(self, x, y, width, Flags, pos1, pos2, pos3):
        """ PickPixel(self: InwControl2, x: int, y: int, width: int, Flags: nwEPickFlags) -> (InwOaFragment, object, object, object) """
        pass

    def SaveFile(self, file_name):
        """ SaveFile(self: InwControl2, file_name: str) """
        pass

    def SyncAppendFile(self, file_name):
        """ SyncAppendFile(self: InwControl2, file_name: str) """
        pass

    def SyncSRC(self, file_name):
        """ SyncSRC(self: InwControl2, file_name: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwControl2, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    APIState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: APIState(self: InwControl2) -> InwOpState

"""

    AutoSetFocusMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSetFocusMode(self: InwControl2) -> bool

Set: AutoSetFocusMode(self: InwControl2) = value
"""

    HighlightSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighlightSelection(self: InwControl2) -> bool

Set: HighlightSelection(self: InwControl2) = value
"""

    LocalisationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalisationCode(self: InwControl2) -> str

Set: LocalisationCode(self: InwControl2) = value
"""

    NavigationMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NavigationMode(self: InwControl2) -> nwENavigationMode

Set: NavigationMode(self: InwControl2) = value
"""

    SecurityCertificate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecurityCertificate(self: InwControl2) -> str

Set: SecurityCertificate(self: InwControl2) = value
"""

    SelectionBehaviour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionBehaviour(self: InwControl2) -> nwESelectionBehaviour

Set: SelectionBehaviour(self: InwControl2) = value
"""

    ShowProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowProgress(self: InwControl2) -> bool

Set: ShowProgress(self: InwControl2) = value
"""

    SRC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SRC(self: InwControl2) -> str

Set: SRC(self: InwControl2) = value
"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: InwControl2) -> InwOpState

"""

    UserModeSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserModeSelection(self: InwControl2) -> bool

Set: UserModeSelection(self: InwControl2) = value
"""

    _State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: _State(self: InwControl2) -> str

Set: _State(self: InwControl2) = value
"""



class InwControl3(InwControl2, InwControl):
    # no doc
    def AnimationCommand(self, cmd):
        """ AnimationCommand(self: InwControl3, cmd: nwEAnimationCmd) -> nwEAnimCmdFlags """
        pass

    def AppendFile(self, file_name):
        """ AppendFile(self: InwControl3, file_name: str) """
        pass

    def AppendFile_As(self, file_name, file_type):
        """ AppendFile_As(self: InwControl3, file_name: str, file_type: nwEFileAsType) """
        pass

    def PickPixel(self, x, y, width, Flags, pos1, pos2, pos3):
        """ PickPixel(self: InwControl3, x: int, y: int, width: int, Flags: nwEPickFlags) -> (InwOaFragment, object, object, object) """
        pass

    def SaveFile(self, file_name):
        """ SaveFile(self: InwControl3, file_name: str) """
        pass

    def SaveFile_As(self, file_name, file_type):
        """ SaveFile_As(self: InwControl3, file_name: str, file_type: nwEFileAsType) """
        pass

    def SRC_As(self, file_name, file_type):
        """ SRC_As(self: InwControl3, file_name: str, file_type: nwEFileAsType) """
        pass

    def SyncAppendFile(self, file_name):
        """ SyncAppendFile(self: InwControl3, file_name: str) """
        pass

    def SyncAppendFile_As(self, file_name, file_type):
        """ SyncAppendFile_As(self: InwControl3, file_name: str, file_type: nwEFileAsType) """
        pass

    def SyncSRC(self, file_name):
        """ SyncSRC(self: InwControl3, file_name: str) """
        pass

    def SyncSRC_As(self, file_name, file_type):
        """ SyncSRC_As(self: InwControl3, file_name: str, file_type: nwEFileAsType) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwControl3, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    APIState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: APIState(self: InwControl3) -> InwOpState

"""

    AutoSetFocusMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSetFocusMode(self: InwControl3) -> bool

Set: AutoSetFocusMode(self: InwControl3) = value
"""

    HighlightSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighlightSelection(self: InwControl3) -> bool

Set: HighlightSelection(self: InwControl3) = value
"""

    LocalisationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalisationCode(self: InwControl3) -> str

Set: LocalisationCode(self: InwControl3) = value
"""

    NavigationMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NavigationMode(self: InwControl3) -> nwENavigationMode

Set: NavigationMode(self: InwControl3) = value
"""

    SecurityCertificate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecurityCertificate(self: InwControl3) -> str

Set: SecurityCertificate(self: InwControl3) = value
"""

    SelectionBehaviour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionBehaviour(self: InwControl3) -> nwESelectionBehaviour

Set: SelectionBehaviour(self: InwControl3) = value
"""

    ShowProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowProgress(self: InwControl3) -> bool

Set: ShowProgress(self: InwControl3) = value
"""

    SRC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SRC(self: InwControl3) -> str

Set: SRC(self: InwControl3) = value
"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: InwControl3) -> InwOpState

"""

    UserModeSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserModeSelection(self: InwControl3) -> bool

Set: UserModeSelection(self: InwControl3) = value
"""

    _State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: _State(self: InwControl3) -> str

Set: _State(self: InwControl3) = value
"""



class InwControl4(InwControl3, InwControl2, InwControl):
    # no doc
    def AnimationCommand(self, cmd):
        """ AnimationCommand(self: InwControl4, cmd: nwEAnimationCmd) -> nwEAnimCmdFlags """
        pass

    def AppendFile(self, file_name):
        """ AppendFile(self: InwControl4, file_name: str) """
        pass

    def AppendFile_As(self, file_name, file_type):
        """ AppendFile_As(self: InwControl4, file_name: str, file_type: nwEFileAsType) """
        pass

    def PickPixel(self, x, y, width, Flags, pos1, pos2, pos3):
        """ PickPixel(self: InwControl4, x: int, y: int, width: int, Flags: nwEPickFlags) -> (InwOaFragment, object, object, object) """
        pass

    def SaveFile(self, file_name):
        """ SaveFile(self: InwControl4, file_name: str) """
        pass

    def SaveFile_As(self, file_name, file_type):
        """ SaveFile_As(self: InwControl4, file_name: str, file_type: nwEFileAsType) """
        pass

    def SRC_As(self, file_name, file_type):
        """ SRC_As(self: InwControl4, file_name: str, file_type: nwEFileAsType) """
        pass

    def SyncAppendFile(self, file_name):
        """ SyncAppendFile(self: InwControl4, file_name: str) """
        pass

    def SyncAppendFile_As(self, file_name, file_type):
        """ SyncAppendFile_As(self: InwControl4, file_name: str, file_type: nwEFileAsType) """
        pass

    def SyncSRC(self, file_name):
        """ SyncSRC(self: InwControl4, file_name: str) """
        pass

    def SyncSRC_As(self, file_name, file_type):
        """ SyncSRC_As(self: InwControl4, file_name: str, file_type: nwEFileAsType) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwControl4, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    APIState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: APIState(self: InwControl4) -> InwOpState

"""

    AutoSetFocusMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSetFocusMode(self: InwControl4) -> bool

Set: AutoSetFocusMode(self: InwControl4) = value
"""

    ForceEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForceEvents(self: InwControl4) -> bool

Set: ForceEvents(self: InwControl4) = value
"""

    HighlightSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighlightSelection(self: InwControl4) -> bool

Set: HighlightSelection(self: InwControl4) = value
"""

    LocalisationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalisationCode(self: InwControl4) -> str

Set: LocalisationCode(self: InwControl4) = value
"""

    NavigationMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NavigationMode(self: InwControl4) -> nwENavigationMode

Set: NavigationMode(self: InwControl4) = value
"""

    SecurityCertificate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecurityCertificate(self: InwControl4) -> str

Set: SecurityCertificate(self: InwControl4) = value
"""

    SelectionBehaviour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionBehaviour(self: InwControl4) -> nwESelectionBehaviour

Set: SelectionBehaviour(self: InwControl4) = value
"""

    ShowProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowProgress(self: InwControl4) -> bool

Set: ShowProgress(self: InwControl4) = value
"""

    SRC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SRC(self: InwControl4) -> str

Set: SRC(self: InwControl4) = value
"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: InwControl4) -> InwOpState

"""

    UserModeSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserModeSelection(self: InwControl4) -> bool

Set: UserModeSelection(self: InwControl4) = value
"""

    _State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: _State(self: InwControl4) -> str

Set: _State(self: InwControl4) = value
"""



class InwControl5(InwControl4, InwControl3, InwControl2, InwControl):
    # no doc
    def AnimationCommand(self, cmd):
        """ AnimationCommand(self: InwControl5, cmd: nwEAnimationCmd) -> nwEAnimCmdFlags """
        pass

    def AppendFile(self, file_name):
        """ AppendFile(self: InwControl5, file_name: str) """
        pass

    def AppendFile_As(self, file_name, file_type):
        """ AppendFile_As(self: InwControl5, file_name: str, file_type: nwEFileAsType) """
        pass

    def PickPixel(self, x, y, width, Flags, pos1, pos2, pos3):
        """ PickPixel(self: InwControl5, x: int, y: int, width: int, Flags: nwEPickFlags) -> (InwOaFragment, object, object, object) """
        pass

    def SaveFile(self, file_name):
        """ SaveFile(self: InwControl5, file_name: str) """
        pass

    def SaveFile_As(self, file_name, file_type):
        """ SaveFile_As(self: InwControl5, file_name: str, file_type: nwEFileAsType) """
        pass

    def SRC_As(self, file_name, file_type):
        """ SRC_As(self: InwControl5, file_name: str, file_type: nwEFileAsType) """
        pass

    def SyncAppendFile(self, file_name):
        """ SyncAppendFile(self: InwControl5, file_name: str) """
        pass

    def SyncAppendFile_As(self, file_name, file_type):
        """ SyncAppendFile_As(self: InwControl5, file_name: str, file_type: nwEFileAsType) """
        pass

    def SyncSRC(self, file_name):
        """ SyncSRC(self: InwControl5, file_name: str) """
        pass

    def SyncSRC_As(self, file_name, file_type):
        """ SyncSRC_As(self: InwControl5, file_name: str, file_type: nwEFileAsType) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwControl5, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    APIState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: APIState(self: InwControl5) -> InwOpState

"""

    AutoSetFocusMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSetFocusMode(self: InwControl5) -> bool

Set: AutoSetFocusMode(self: InwControl5) = value
"""

    ForceEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForceEvents(self: InwControl5) -> bool

Set: ForceEvents(self: InwControl5) = value
"""

    HighlightSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighlightSelection(self: InwControl5) -> bool

Set: HighlightSelection(self: InwControl5) = value
"""

    LocalisationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalisationCode(self: InwControl5) -> str

Set: LocalisationCode(self: InwControl5) = value
"""

    NavigationMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NavigationMode(self: InwControl5) -> nwENavigationMode

Set: NavigationMode(self: InwControl5) = value
"""

    ProgressMsg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProgressMsg(self: InwControl5) -> str

Set: ProgressMsg(self: InwControl5) = value
"""

    SecurityCertificate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecurityCertificate(self: InwControl5) -> str

Set: SecurityCertificate(self: InwControl5) = value
"""

    SelectionBehaviour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionBehaviour(self: InwControl5) -> nwESelectionBehaviour

Set: SelectionBehaviour(self: InwControl5) = value
"""

    ShowProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowProgress(self: InwControl5) -> bool

Set: ShowProgress(self: InwControl5) = value
"""

    SRC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SRC(self: InwControl5) -> str

Set: SRC(self: InwControl5) = value
"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: InwControl5) -> InwOpState

"""

    UserModeSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserModeSelection(self: InwControl5) -> bool

Set: UserModeSelection(self: InwControl5) = value
"""

    _State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: _State(self: InwControl5) -> str

Set: _State(self: InwControl5) = value
"""



class InwExportPlugin:
    # no doc
    def iBeginContext(self, p_state):
        """ iBeginContext(self: InwExportPlugin, p_state: InwOpState) """
        pass

    def iCanExport(self, p_state, reason):
        """ iCanExport(self: InwExportPlugin, p_state: InwOpState, reason: int) -> bool """
        pass

    def iDialog(self, p_state, reason):
        """ iDialog(self: InwExportPlugin, p_state: InwOpState, reason: int) -> bool """
        pass

    def iEndContext(self, p_state):
        """ iEndContext(self: InwExportPlugin, p_state: InwOpState) """
        pass

    def iExport(self, p_state, reason, filename, Progress):
        """ iExport(self: InwExportPlugin, p_state: InwOpState, reason: int, filename: str, Progress: InwOpProgress) -> nwEExportStatus """
        pass

    def iGetFormatName(self):
        """ iGetFormatName(self: InwExportPlugin) -> str """
        pass

    def iGetFormatSuffix(self):
        """ iGetFormatSuffix(self: InwExportPlugin) -> str """
        pass

    def iGetUserString(self):
        """ iGetUserString(self: InwExportPlugin) -> str """
        pass

    def iHelpExport(self):
        """ iHelpExport(self: InwExportPlugin) -> bool """
        pass

    def InitialisePlugin(self, capbits, ver):
        """ InitialisePlugin(self: InwExportPlugin) -> (int, int) """
        pass

    def iXtension(self, vIn):
        """ iXtension(self: InwExportPlugin, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InwExportPlugin_Site(InwPlugin_Site, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwExportPlugin_Site) -> object """
        pass

    def GetApplication(self):
        """ GetApplication(self: InwExportPlugin_Site) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwExportPlugin_Site, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwExportPlugin_Site) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwExportPlugin_Site, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwExportPlugin_Site) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwExportPlugin_Site) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwExportPlugin_Site) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwExportPlugin_Site) -> int

Set: nwLock(self: InwExportPlugin_Site) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwExportPlugin_Site) -> bool

Set: nwOwn(self: InwExportPlugin_Site) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwExportPlugin_Site) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwExportPlugin_Site) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwExportPlugin_Site) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwExportPlugin_Site) -> str

"""



class InwGlobalProperties(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwGlobalProperties) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwGlobalProperties, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwGlobalProperties) """
        pass

    def SetSmartTagsOpts(self, pI):
        """ SetSmartTagsOpts(self: InwGlobalProperties, pI: InwSmartTagsOpts) """
        pass

    def URLsCategories(self):
        """ URLsCategories(self: InwGlobalProperties) -> InwURLCategoriesColl """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwGlobalProperties, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwGlobalProperties) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwGlobalProperties) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwGlobalProperties) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwGlobalProperties) -> int

Set: nwLock(self: InwGlobalProperties) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwGlobalProperties) -> bool

Set: nwOwn(self: InwGlobalProperties) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwGlobalProperties) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwGlobalProperties) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwGlobalProperties) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwGlobalProperties) -> str

"""

    URLs3dMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLs3dMode(self: InwGlobalProperties) -> bool

Set: URLs3dMode(self: InwGlobalProperties) = value
"""

    URLsAntiCollisionMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsAntiCollisionMode(self: InwGlobalProperties) -> bool

Set: URLsAntiCollisionMode(self: InwGlobalProperties) = value
"""

    URLsCullRadiusM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsCullRadiusM(self: InwGlobalProperties) -> float

Set: URLsCullRadiusM(self: InwGlobalProperties) = value
"""

    URLsLeaderX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsLeaderX(self: InwGlobalProperties) -> int

Set: URLsLeaderX(self: InwGlobalProperties) = value
"""

    URLsLeaderY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsLeaderY(self: InwGlobalProperties) -> int

Set: URLsLeaderY(self: InwGlobalProperties) = value
"""

    URLsMaxIcons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsMaxIcons(self: InwGlobalProperties) -> int

Set: URLsMaxIcons(self: InwGlobalProperties) = value
"""

    URLsShowContextMenu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsShowContextMenu(self: InwGlobalProperties) -> bool

Set: URLsShowContextMenu(self: InwGlobalProperties) = value
"""



class InwGlobalProperties2(InwGlobalProperties, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwGlobalProperties2) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwGlobalProperties2, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwGlobalProperties2) """
        pass

    def SetSmartTagsOpts(self, pI):
        """ SetSmartTagsOpts(self: InwGlobalProperties2, pI: InwSmartTagsOpts) """
        pass

    def URLsCategories(self):
        """ URLsCategories(self: InwGlobalProperties2) -> InwURLCategoriesColl """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwGlobalProperties2, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    HighlightSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighlightSelection(self: InwGlobalProperties2) -> bool

Set: HighlightSelection(self: InwGlobalProperties2) = value
"""

    HighlightSelectionColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighlightSelectionColor(self: InwGlobalProperties2) -> InwLVec3f

Set: HighlightSelectionColor(self: InwGlobalProperties2) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwGlobalProperties2) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwGlobalProperties2) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwGlobalProperties2) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwGlobalProperties2) -> int

Set: nwLock(self: InwGlobalProperties2) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwGlobalProperties2) -> bool

Set: nwOwn(self: InwGlobalProperties2) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwGlobalProperties2) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwGlobalProperties2) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwGlobalProperties2) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwGlobalProperties2) -> str

"""

    URLs3dMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLs3dMode(self: InwGlobalProperties2) -> bool

Set: URLs3dMode(self: InwGlobalProperties2) = value
"""

    URLsAntiCollisionMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsAntiCollisionMode(self: InwGlobalProperties2) -> bool

Set: URLsAntiCollisionMode(self: InwGlobalProperties2) = value
"""

    URLsCullRadiusM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsCullRadiusM(self: InwGlobalProperties2) -> float

Set: URLsCullRadiusM(self: InwGlobalProperties2) = value
"""

    URLsLeaderX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsLeaderX(self: InwGlobalProperties2) -> int

Set: URLsLeaderX(self: InwGlobalProperties2) = value
"""

    URLsLeaderY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsLeaderY(self: InwGlobalProperties2) -> int

Set: URLsLeaderY(self: InwGlobalProperties2) = value
"""

    URLsMaxIcons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsMaxIcons(self: InwGlobalProperties2) -> int

Set: URLsMaxIcons(self: InwGlobalProperties2) = value
"""

    URLsShowContextMenu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsShowContextMenu(self: InwGlobalProperties2) -> bool

Set: URLsShowContextMenu(self: InwGlobalProperties2) = value
"""



class InwGUIAttribute(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwGUIAttribute) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwGUIAttribute, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwGUIAttribute) """
        pass

    def Properties(self):
        """ Properties(self: InwGUIAttribute) -> InwOaPropertyColl """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwGUIAttribute, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwGUIAttribute) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwGUIAttribute) -> str

"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwGUIAttribute) -> str

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwGUIAttribute) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwGUIAttribute) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwGUIAttribute) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwGUIAttribute) -> int

Set: nwLock(self: InwGUIAttribute) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwGUIAttribute) -> bool

Set: nwOwn(self: InwGUIAttribute) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwGUIAttribute) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwGUIAttribute) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwGUIAttribute) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwGUIAttribute) -> str

"""



class InwGUIAttribute2(InwGUIAttribute, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwGUIAttribute2) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwGUIAttribute2, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwGUIAttribute2) """
        pass

    def Properties(self):
        """ Properties(self: InwGUIAttribute2) -> InwOaPropertyColl """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwGUIAttribute2, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwGUIAttribute2) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwGUIAttribute2) -> str

"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwGUIAttribute2) -> str

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwGUIAttribute2) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwGUIAttribute2) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwGUIAttribute2) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwGUIAttribute2) -> int

Set: nwLock(self: InwGUIAttribute2) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwGUIAttribute2) -> bool

Set: nwOwn(self: InwGUIAttribute2) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwGUIAttribute2) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwGUIAttribute2) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwGUIAttribute2) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwGUIAttribute2) -> str

"""

    UserDefined = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserDefined(self: InwGUIAttribute2) -> bool

"""



class InwGUIAttributesColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwGUIAttributesColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwGUIAttributesColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwGUIAttributesColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwGUIAttributesColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwGUIAttributesColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwGUIAttributesColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwGUIAttributesColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwGUIAttributesColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwGUIAttributesColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwGUIAttributesColl) -> bool

"""



class InwGUIPropertyNode(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwGUIPropertyNode) -> object """
        pass

    def GUIAttributes(self):
        """ GUIAttributes(self: InwGUIPropertyNode) -> InwGUIAttributesColl """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwGUIPropertyNode, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwGUIPropertyNode) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwGUIPropertyNode, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwGUIPropertyNode) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwGUIPropertyNode) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwGUIPropertyNode) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwGUIPropertyNode) -> int

Set: nwLock(self: InwGUIPropertyNode) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwGUIPropertyNode) -> bool

Set: nwOwn(self: InwGUIPropertyNode) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwGUIPropertyNode) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwGUIPropertyNode) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwGUIPropertyNode) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwGUIPropertyNode) -> str

"""



class InwGUIPropertyNode2(InwGUIPropertyNode, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwGUIPropertyNode2) -> object """
        pass

    def GUIAttributes(self):
        """ GUIAttributes(self: InwGUIPropertyNode2) -> InwGUIAttributesColl """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwGUIPropertyNode2, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwGUIPropertyNode2) """
        pass

    def RemoveUserDefined(self, ndx):
        """ RemoveUserDefined(self: InwGUIPropertyNode2, ndx: int) """
        pass

    def SetUserDefined(self, ndx, user_name, internal_name, props):
        """ SetUserDefined(self: InwGUIPropertyNode2, ndx: int, user_name: str, internal_name: str, props: InwOaPropertyVec) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwGUIPropertyNode2, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwGUIPropertyNode2) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwGUIPropertyNode2) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwGUIPropertyNode2) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwGUIPropertyNode2) -> int

Set: nwLock(self: InwGUIPropertyNode2) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwGUIPropertyNode2) -> bool

Set: nwOwn(self: InwGUIPropertyNode2) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwGUIPropertyNode2) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwGUIPropertyNode2) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwGUIPropertyNode2) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwGUIPropertyNode2) -> str

"""



class InwLBaseVec3f(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwLBaseVec3f) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwLBaseVec3f, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwLBaseVec3f) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwLBaseVec3f, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    data1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: data1(self: InwLBaseVec3f) -> float

Set: data1(self: InwLBaseVec3f) = value
"""

    data2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: data2(self: InwLBaseVec3f) -> float

Set: data2(self: InwLBaseVec3f) = value
"""

    data3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: data3(self: InwLBaseVec3f) -> float

Set: data3(self: InwLBaseVec3f) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwLBaseVec3f) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwLBaseVec3f) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwLBaseVec3f) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwLBaseVec3f) -> int

Set: nwLock(self: InwLBaseVec3f) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwLBaseVec3f) -> bool

Set: nwOwn(self: InwLBaseVec3f) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwLBaseVec3f) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwLBaseVec3f) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwLBaseVec3f) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwLBaseVec3f) -> str

"""



class InwLBox3f(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwLBox3f) -> object """
        pass

    def Equals(self, arg):
        """ Equals(self: InwLBox3f, arg: InwLBox3f) -> bool """
        pass

    def MakeEmpty(self):
        """ MakeEmpty(self: InwLBox3f) """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwLBox3f, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwLBox3f) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwLBox3f, vIn: object) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEmpty(self: InwLBox3f) -> bool

"""

    max_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: max_pos(self: InwLBox3f) -> InwLPos3f

Set: max_pos(self: InwLBox3f) = value
"""

    min_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: min_pos(self: InwLBox3f) -> InwLPos3f

Set: min_pos(self: InwLBox3f) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwLBox3f) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwLBox3f) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwLBox3f) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwLBox3f) -> int

Set: nwLock(self: InwLBox3f) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwLBox3f) -> bool

Set: nwOwn(self: InwLBox3f) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwLBox3f) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwLBox3f) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwLBox3f) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwLBox3f) -> str

"""



class InwLightsColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwLightsColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwLightsColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwLightsColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwLightsColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwLightsColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwLightsColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwLightsColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwLightsColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwLightsColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwLightsColl) -> bool

"""



class InwLPlane3f(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwLPlane3f) -> object """
        pass

    def distance(self):
        """ distance(self: InwLPlane3f) -> int """
        pass

    def GetNormal(self):
        """ GetNormal(self: InwLPlane3f) -> InwLUnitVec3f """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwLPlane3f, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwLPlane3f) """
        pass

    def SetValue(self, unit_vec, distance):
        """ SetValue(self: InwLPlane3f, unit_vec: InwLUnitVec3f, distance: float) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwLPlane3f, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwLPlane3f) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwLPlane3f) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwLPlane3f) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwLPlane3f) -> int

Set: nwLock(self: InwLPlane3f) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwLPlane3f) -> bool

Set: nwOwn(self: InwLPlane3f) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwLPlane3f) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwLPlane3f) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwLPlane3f) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwLPlane3f) -> str

"""



class InwLPlane3f2(InwLPlane3f, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwLPlane3f2) -> object """
        pass

    def distance(self):
        """ distance(self: InwLPlane3f2) -> int """
        pass

    def DistanceEx(self):
        """ DistanceEx(self: InwLPlane3f2) -> float """
        pass

    def GetNormal(self):
        """ GetNormal(self: InwLPlane3f2) -> InwLUnitVec3f """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwLPlane3f2, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwLPlane3f2) """
        pass

    def SetValue(self, unit_vec, distance):
        """ SetValue(self: InwLPlane3f2, unit_vec: InwLUnitVec3f, distance: float) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwLPlane3f2, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwLPlane3f2) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwLPlane3f2) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwLPlane3f2) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwLPlane3f2) -> int

Set: nwLock(self: InwLPlane3f2) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwLPlane3f2) -> bool

Set: nwOwn(self: InwLPlane3f2) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwLPlane3f2) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwLPlane3f2) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwLPlane3f2) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwLPlane3f2) -> str

"""



class InwLPos3f(InwLBaseVec3f, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwLPos3f) -> object """
        pass

    def Equals(self, arg):
        """ Equals(self: InwLPos3f, arg: InwLPos3f) -> bool """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwLPos3f, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwLPos3f) """
        pass

    def SetValue(self, d1, d2, d3):
        """ SetValue(self: InwLPos3f, d1: float, d2: float, d3: float) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwLPos3f, vIn: object) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    data1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: data1(self: InwLPos3f) -> float

Set: data1(self: InwLPos3f) = value
"""

    data2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: data2(self: InwLPos3f) -> float

Set: data2(self: InwLPos3f) = value
"""

    data3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: data3(self: InwLPos3f) -> float

Set: data3(self: InwLPos3f) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwLPos3f) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwLPos3f) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwLPos3f) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwLPos3f) -> int

Set: nwLock(self: InwLPos3f) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwLPos3f) -> bool

Set: nwOwn(self: InwLPos3f) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwLPos3f) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwLPos3f) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwLPos3f) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwLPos3f) -> str

"""



class InwLPos3fColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwLPos3fColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwLPos3fColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwLPos3fColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwLPos3fColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwLPos3fColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwLPos3fColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwLPos3fColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwLPos3fColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwLPos3fColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwLPos3fColl) -> bool

"""



class InwLRotation3f(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwLRotation3f) -> object """
        pass

    def GetAxis(self):
        """ GetAxis(self: InwLRotation3f) -> InwLUnitVec3f """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwLRotation3f, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwLRotation3f) """
        pass

    def SetValue(self, axis, angle):
        """ SetValue(self: InwLRotation3f, axis: InwLUnitVec3f, angle: float) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwLRotation3f, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: angle(self: InwLRotation3f) -> float

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwLRotation3f) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwLRotation3f) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwLRotation3f) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwLRotation3f) -> int

Set: nwLock(self: InwLRotation3f) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwLRotation3f) -> bool

Set: nwOwn(self: InwLRotation3f) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwLRotation3f) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwLRotation3f) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwLRotation3f) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwLRotation3f) -> str

"""



class InwLRotation3f2(InwLRotation3f, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwLRotation3f2) -> object """
        pass

    def GetAxis(self):
        """ GetAxis(self: InwLRotation3f2) -> InwLUnitVec3f """
        pass

    def Mult(self, Rotation):
        """ Mult(self: InwLRotation3f2, Rotation: InwLRotation3f) -> InwLRotation3f """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwLRotation3f2, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwLRotation3f2) """
        pass

    def SetValue(self, axis, angle):
        """ SetValue(self: InwLRotation3f2, axis: InwLUnitVec3f, angle: float) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwLRotation3f2, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: angle(self: InwLRotation3f2) -> float

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwLRotation3f2) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwLRotation3f2) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwLRotation3f2) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwLRotation3f2) -> int

Set: nwLock(self: InwLRotation3f2) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwLRotation3f2) -> bool

Set: nwOwn(self: InwLRotation3f2) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwLRotation3f2) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwLRotation3f2) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwLRotation3f2) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwLRotation3f2) -> str

"""



class InwLTransform3f(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwLTransform3f) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwLTransform3f, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwLTransform3f) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwLTransform3f, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Matrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Matrix(self: InwLTransform3f) -> object

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwLTransform3f) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwLTransform3f) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwLTransform3f) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwLTransform3f) -> int

Set: nwLock(self: InwLTransform3f) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwLTransform3f) -> bool

Set: nwOwn(self: InwLTransform3f) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwLTransform3f) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwLTransform3f) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwLTransform3f) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwLTransform3f) -> str

"""



class InwLTransform3f2(InwLTransform3f, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwLTransform3f2) -> object """
        pass

    def Equals(self, tran):
        """ Equals(self: InwLTransform3f2, tran: InwLTransform3f) -> bool """
        pass

    def GetLinear(self):
        """ GetLinear(self: InwLTransform3f2) -> object """
        pass

    def GetTranslation(self):
        """ GetTranslation(self: InwLTransform3f2) -> InwLVec3f """
        pass

    def MakeIdentity(self):
        """ MakeIdentity(self: InwLTransform3f2) """
        pass

    def MakeLinear(self, mat):
        """ MakeLinear(self: InwLTransform3f2, mat: object) """
        pass

    def MakeRotation(self, rot):
        """ MakeRotation(self: InwLTransform3f2, rot: InwLRotation3f) """
        pass

    def MakeScale(self, scale):
        """ MakeScale(self: InwLTransform3f2, scale: InwLVec3f) """
        pass

    def MakeTranslation(self, trans):
        """ MakeTranslation(self: InwLTransform3f2, trans: InwLVec3f) """
        pass

    def MakeTransRot(self, rot, trans):
        """ MakeTransRot(self: InwLTransform3f2, rot: InwLRotation3f, trans: InwLVec3f) """
        pass

    def MakeUniformScale(self, scale):
        """ MakeUniformScale(self: InwLTransform3f2, scale: float) """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwLTransform3f2, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwLTransform3f2) """
        pass

    def SetMatrix(self, Matrix):
        """ SetMatrix(self: InwLTransform3f2, Matrix: object) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwLTransform3f2, vIn: object) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsAffine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAffine(self: InwLTransform3f2) -> bool

"""

    IsIdentity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsIdentity(self: InwLTransform3f2) -> bool

"""

    IsLinear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLinear(self: InwLTransform3f2) -> bool

"""

    IsRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRotation(self: InwLTransform3f2) -> bool

"""

    IsTranslation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTranslation(self: InwLTransform3f2) -> bool

"""

    IsUniformScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUniformScale(self: InwLTransform3f2) -> bool

"""

    IsVecTransformed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVecTransformed(self: InwLTransform3f2) -> bool

"""

    Matrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Matrix(self: InwLTransform3f2) -> object

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwLTransform3f2) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwLTransform3f2) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwLTransform3f2) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwLTransform3f2) -> int

Set: nwLock(self: InwLTransform3f2) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwLTransform3f2) -> bool

Set: nwOwn(self: InwLTransform3f2) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwLTransform3f2) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwLTransform3f2) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwLTransform3f2) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwLTransform3f2) -> str

"""



class InwLTransform3f3(InwLTransform3f2, InwLTransform3f, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwLTransform3f3) -> object """
        pass

    def Equals(self, tran):
        """ Equals(self: InwLTransform3f3, tran: InwLTransform3f) -> bool """
        pass

    def factor(self, scale, scaleOrientation, Rotation, trans):
        """ factor(self: InwLTransform3f3, scale: InwLVec3f, scaleOrientation: InwLRotation3f, Rotation: InwLRotation3f, trans: InwLVec3f) """
        pass

    def GetLinear(self):
        """ GetLinear(self: InwLTransform3f3) -> object """
        pass

    def GetTranslation(self):
        """ GetTranslation(self: InwLTransform3f3) -> InwLVec3f """
        pass

    def MakeIdentity(self):
        """ MakeIdentity(self: InwLTransform3f3) """
        pass

    def MakeLinear(self, mat):
        """ MakeLinear(self: InwLTransform3f3, mat: object) """
        pass

    def MakeRotation(self, rot):
        """ MakeRotation(self: InwLTransform3f3, rot: InwLRotation3f) """
        pass

    def MakeScale(self, scale):
        """ MakeScale(self: InwLTransform3f3, scale: InwLVec3f) """
        pass

    def MakeTranslation(self, trans):
        """ MakeTranslation(self: InwLTransform3f3, trans: InwLVec3f) """
        pass

    def MakeTransRot(self, rot, trans):
        """ MakeTransRot(self: InwLTransform3f3, rot: InwLRotation3f, trans: InwLVec3f) """
        pass

    def MakeUniformScale(self, scale):
        """ MakeUniformScale(self: InwLTransform3f3, scale: float) """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwLTransform3f3, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwLTransform3f3) """
        pass

    def SetMatrix(self, Matrix):
        """ SetMatrix(self: InwLTransform3f3, Matrix: object) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwLTransform3f3, vIn: object) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsAffine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAffine(self: InwLTransform3f3) -> bool

"""

    IsIdentity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsIdentity(self: InwLTransform3f3) -> bool

"""

    IsLinear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLinear(self: InwLTransform3f3) -> bool

"""

    IsRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRotation(self: InwLTransform3f3) -> bool

"""

    IsTranslation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTranslation(self: InwLTransform3f3) -> bool

"""

    IsUniformScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUniformScale(self: InwLTransform3f3) -> bool

"""

    IsVecTransformed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVecTransformed(self: InwLTransform3f3) -> bool

"""

    Matrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Matrix(self: InwLTransform3f3) -> object

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwLTransform3f3) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwLTransform3f3) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwLTransform3f3) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwLTransform3f3) -> int

Set: nwLock(self: InwLTransform3f3) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwLTransform3f3) -> bool

Set: nwOwn(self: InwLTransform3f3) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwLTransform3f3) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwLTransform3f3) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwLTransform3f3) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwLTransform3f3) -> str

"""



class InwLUnitVec3f(InwLBaseVec3f, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwLUnitVec3f) -> object """
        pass

    def Equals(self, arg):
        """ Equals(self: InwLUnitVec3f, arg: InwLUnitVec3f) -> bool """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwLUnitVec3f, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwLUnitVec3f) """
        pass

    def SetValue(self, d1, d2, d3):
        """ SetValue(self: InwLUnitVec3f, d1: float, d2: float, d3: float) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwLUnitVec3f, vIn: object) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    data1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: data1(self: InwLUnitVec3f) -> float

Set: data1(self: InwLUnitVec3f) = value
"""

    data2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: data2(self: InwLUnitVec3f) -> float

Set: data2(self: InwLUnitVec3f) = value
"""

    data3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: data3(self: InwLUnitVec3f) -> float

Set: data3(self: InwLUnitVec3f) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwLUnitVec3f) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwLUnitVec3f) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwLUnitVec3f) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwLUnitVec3f) -> int

Set: nwLock(self: InwLUnitVec3f) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwLUnitVec3f) -> bool

Set: nwOwn(self: InwLUnitVec3f) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwLUnitVec3f) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwLUnitVec3f) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwLUnitVec3f) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwLUnitVec3f) -> str

"""



class InwLVec3f(InwLBaseVec3f, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwLVec3f) -> object """
        pass

    def Equals(self, arg):
        """ Equals(self: InwLVec3f, arg: InwLVec3f) -> bool """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwLVec3f, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwLVec3f) """
        pass

    def SetValue(self, d1, d2, d3):
        """ SetValue(self: InwLVec3f, d1: float, d2: float, d3: float) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwLVec3f, vIn: object) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    data1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: data1(self: InwLVec3f) -> float

Set: data1(self: InwLVec3f) = value
"""

    data2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: data2(self: InwLVec3f) -> float

Set: data2(self: InwLVec3f) = value
"""

    data3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: data3(self: InwLVec3f) -> float

Set: data3(self: InwLVec3f) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwLVec3f) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwLVec3f) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwLVec3f) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwLVec3f) -> int

Set: nwLock(self: InwLVec3f) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwLVec3f) -> bool

Set: nwOwn(self: InwLVec3f) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwLVec3f) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwLVec3f) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwLVec3f) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwLVec3f) -> str

"""



class InwNodeAttributesColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwNodeAttributesColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwNodeAttributesColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwNodeAttributesColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwNodeAttributesColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwNodeAttributesColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwNodeAttributesColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwNodeAttributesColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwNodeAttributesColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwNodeAttributesColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwNodeAttributesColl) -> bool

"""



class InwNodeFragsColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwNodeFragsColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwNodeFragsColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwNodeFragsColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwNodeFragsColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwNodeFragsColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwNodeFragsColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwNodeFragsColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwNodeFragsColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwNodeFragsColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwNodeFragsColl) -> bool

"""



class InwNodeNodesColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwNodeNodesColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwNodeNodesColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwNodeNodesColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwNodeNodesColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwNodeNodesColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwNodeNodesColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwNodeNodesColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwNodeNodesColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwNodeNodesColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwNodeNodesColl) -> bool

"""



class InwNvCamera(InwBase):
    # no doc
    def AlignUp(self, up):
        """ AlignUp(self: InwNvCamera, up: InwLVec3f) """
        pass

    def Copy(self):
        """ Copy(self: InwNvCamera) -> object """
        pass

    def GetUpVector(self):
        """ GetUpVector(self: InwNvCamera) -> InwLVec3f """
        pass

    def GetViewDir(self):
        """ GetViewDir(self: InwNvCamera) -> InwLVec3f """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwNvCamera, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwNvCamera) """
        pass

    def PointAt(self, pos):
        """ PointAt(self: InwNvCamera, pos: InwLPos3f) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwNvCamera, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AspectRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AspectRatio(self: InwNvCamera) -> float

Set: AspectRatio(self: InwNvCamera) = value
"""

    HeightField = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeightField(self: InwNvCamera) -> float

Set: HeightField(self: InwNvCamera) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwNvCamera) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwNvCamera) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwNvCamera) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwNvCamera) -> int

Set: nwLock(self: InwNvCamera) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwNvCamera) -> bool

Set: nwOwn(self: InwNvCamera) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwNvCamera) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwNvCamera) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwNvCamera) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwNvCamera) -> str

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: InwNvCamera) -> InwLPos3f

Set: Position(self: InwNvCamera) = value
"""

    Projection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Projection(self: InwNvCamera) -> nwEProjection

Set: Projection(self: InwNvCamera) = value
"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rotation(self: InwNvCamera) -> InwLRotation3f

Set: Rotation(self: InwNvCamera) = value
"""



class InwNvViewer(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwNvViewer) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwNvViewer, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwNvViewer) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwNvViewer, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AutoCrouch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCrouch(self: InwNvViewer) -> bool

Set: AutoCrouch(self: InwNvViewer) = value
"""

    CameraMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CameraMode(self: InwNvViewer) -> nwECameraMode

Set: CameraMode(self: InwNvViewer) = value
"""

    CollisionDetection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CollisionDetection(self: InwNvViewer) -> bool

Set: CollisionDetection(self: InwNvViewer) = value
"""

    Gravity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Gravity(self: InwNvViewer) -> bool

Set: Gravity(self: InwNvViewer) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwNvViewer) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwNvViewer) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwNvViewer) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwNvViewer) -> int

Set: nwLock(self: InwNvViewer) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwNvViewer) -> bool

Set: nwOwn(self: InwNvViewer) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwNvViewer) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwNvViewer) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwNvViewer) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwNvViewer) -> str

"""



class InwNvViewPoint(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwNvViewPoint) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwNvViewPoint, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwNvViewPoint) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwNvViewPoint, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AngularSpeed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngularSpeed(self: InwNvViewPoint) -> float

Set: AngularSpeed(self: InwNvViewPoint) = value
"""

    Camera = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Camera(self: InwNvViewPoint) -> InwNvCamera

Set: Camera(self: InwNvViewPoint) = value
"""

    FocalDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FocalDistance(self: InwNvViewPoint) -> float

Set: FocalDistance(self: InwNvViewPoint) = value
"""

    Lighting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lighting(self: InwNvViewPoint) -> nwELighting

Set: Lighting(self: InwNvViewPoint) = value
"""

    LinearSpeed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinearSpeed(self: InwNvViewPoint) -> float

Set: LinearSpeed(self: InwNvViewPoint) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwNvViewPoint) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwNvViewPoint) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwNvViewPoint) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwNvViewPoint) -> int

Set: nwLock(self: InwNvViewPoint) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwNvViewPoint) -> bool

Set: nwOwn(self: InwNvViewPoint) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwNvViewPoint) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwNvViewPoint) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwNvViewPoint) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwNvViewPoint) -> str

"""

    Paradigm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Paradigm(self: InwNvViewPoint) -> nwEParadigm

Set: Paradigm(self: InwNvViewPoint) = value
"""

    RenderStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderStyle(self: InwNvViewPoint) -> nwERenderStyle

Set: RenderStyle(self: InwNvViewPoint) = value
"""

    WorldUpVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WorldUpVector(self: InwNvViewPoint) -> InwLUnitVec3f

Set: WorldUpVector(self: InwNvViewPoint) = value
"""



class InwNvViewPoint2(InwNvViewPoint, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwNvViewPoint2) -> object """
        pass

    def IsParadigmCollisionDetectionAllowed(self):
        """ IsParadigmCollisionDetectionAllowed(self: InwNvViewPoint2) -> bool """
        pass

    def IsParadigmGravityAllowed(self):
        """ IsParadigmGravityAllowed(self: InwNvViewPoint2) -> bool """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwNvViewPoint2, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwNvViewPoint2) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwNvViewPoint2, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AngularSpeed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngularSpeed(self: InwNvViewPoint2) -> float

Set: AngularSpeed(self: InwNvViewPoint2) = value
"""

    Camera = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Camera(self: InwNvViewPoint2) -> InwNvCamera

Set: Camera(self: InwNvViewPoint2) = value
"""

    FocalDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FocalDistance(self: InwNvViewPoint2) -> float

Set: FocalDistance(self: InwNvViewPoint2) = value
"""

    Lighting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lighting(self: InwNvViewPoint2) -> nwELighting

Set: Lighting(self: InwNvViewPoint2) = value
"""

    LinearSpeed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinearSpeed(self: InwNvViewPoint2) -> float

Set: LinearSpeed(self: InwNvViewPoint2) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwNvViewPoint2) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwNvViewPoint2) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwNvViewPoint2) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwNvViewPoint2) -> int

Set: nwLock(self: InwNvViewPoint2) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwNvViewPoint2) -> bool

Set: nwOwn(self: InwNvViewPoint2) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwNvViewPoint2) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwNvViewPoint2) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwNvViewPoint2) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwNvViewPoint2) -> str

"""

    Paradigm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Paradigm(self: InwNvViewPoint2) -> nwEParadigm

Set: Paradigm(self: InwNvViewPoint2) = value
"""

    RenderStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderStyle(self: InwNvViewPoint2) -> nwERenderStyle

Set: RenderStyle(self: InwNvViewPoint2) = value
"""

    Viewer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Viewer(self: InwNvViewPoint2) -> InwNvViewer

Set: Viewer(self: InwNvViewPoint2) = value
"""

    WorldUpVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WorldUpVector(self: InwNvViewPoint2) -> InwLUnitVec3f

Set: WorldUpVector(self: InwNvViewPoint2) = value
"""



class InwOaSceneBase(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaSceneBase) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaSceneBase, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaSceneBase) """
        pass

    def Rename(self, class_name, class_username):
        """ Rename(self: InwOaSceneBase, class_name: str, class_username: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaSceneBase, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwOaSceneBase) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwOaSceneBase) -> str

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaSceneBase) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaSceneBase) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaSceneBase) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaSceneBase) -> int

Set: nwLock(self: InwOaSceneBase) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaSceneBase) -> bool

Set: nwOwn(self: InwOaSceneBase) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaSceneBase) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaSceneBase) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaSceneBase) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaSceneBase) -> str

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwOaSceneBase) -> str

Set: UserName(self: InwOaSceneBase) = value
"""



class InwOaAttribute(InwOaSceneBase, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaAttribute) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaAttribute, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaAttribute) """
        pass

    def Rename(self, class_name, class_username):
        """ Rename(self: InwOaAttribute, class_name: str, class_username: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaAttribute, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwOaAttribute) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwOaAttribute) -> str

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaAttribute) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaAttribute) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaAttribute) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaAttribute) -> int

Set: nwLock(self: InwOaAttribute) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaAttribute) -> bool

Set: nwOwn(self: InwOaAttribute) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaAttribute) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaAttribute) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaAttribute) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaAttribute) -> str

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwOaAttribute) -> str

Set: UserName(self: InwOaAttribute) = value
"""



class InwOaBinaryAttribute(InwOaAttribute, InwOaSceneBase, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaBinaryAttribute) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaBinaryAttribute, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaBinaryAttribute) """
        pass

    def Rename(self, class_name, class_username):
        """ Rename(self: InwOaBinaryAttribute, class_name: str, class_username: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaBinaryAttribute, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ArrayData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArrayData(self: InwOaBinaryAttribute) -> object

"""

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwOaBinaryAttribute) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwOaBinaryAttribute) -> str

"""

    NumBytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumBytes(self: InwOaBinaryAttribute) -> int

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaBinaryAttribute) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaBinaryAttribute) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaBinaryAttribute) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaBinaryAttribute) -> int

Set: nwLock(self: InwOaBinaryAttribute) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaBinaryAttribute) -> bool

Set: nwOwn(self: InwOaBinaryAttribute) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaBinaryAttribute) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaBinaryAttribute) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaBinaryAttribute) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaBinaryAttribute) -> str

"""

    RawData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RawData(self: InwOaBinaryAttribute) -> int

"""

    StringByteData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StringByteData(self: InwOaBinaryAttribute) -> str

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwOaBinaryAttribute) -> str

Set: UserName(self: InwOaBinaryAttribute) = value
"""



class InwOaClipPlane(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaClipPlane) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaClipPlane, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaClipPlane) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaClipPlane, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Alignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Alignment(self: InwOaClipPlane) -> nwEClipPlaneAlignment

Set: Alignment(self: InwOaClipPlane) = value
"""

    BaseDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseDistance(self: InwOaClipPlane) -> float

Set: BaseDistance(self: InwOaClipPlane) = value
"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: InwOaClipPlane) -> bool

Set: Enabled(self: InwOaClipPlane) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaClipPlane) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaClipPlane) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaClipPlane) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaClipPlane) -> int

Set: nwLock(self: InwOaClipPlane) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaClipPlane) -> bool

Set: nwOwn(self: InwOaClipPlane) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaClipPlane) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaClipPlane) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaClipPlane) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaClipPlane) -> str

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: InwOaClipPlane) -> InwLPlane3f

Set: Plane(self: InwOaClipPlane) = value
"""



class InwOaCommonLight(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaCommonLight) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaCommonLight, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaCommonLight) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaCommonLight, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AmbientColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AmbientColor(self: InwOaCommonLight) -> InwLVec3f

Set: AmbientColor(self: InwOaCommonLight) = value
"""

    DiffuseColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiffuseColor(self: InwOaCommonLight) -> InwLVec3f

Set: DiffuseColor(self: InwOaCommonLight) = value
"""

    IsEye = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEye(self: InwOaCommonLight) -> bool

Set: IsEye(self: InwOaCommonLight) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaCommonLight) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaCommonLight) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaCommonLight) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaCommonLight) -> int

Set: nwLock(self: InwOaCommonLight) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaCommonLight) -> bool

Set: nwOwn(self: InwOaCommonLight) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaCommonLight) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaCommonLight) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaCommonLight) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaCommonLight) -> str

"""

    SpecularColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecularColor(self: InwOaCommonLight) -> InwLVec3f

Set: SpecularColor(self: InwOaCommonLight) = value
"""



class InwOaDistantLight(InwOaCommonLight, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaDistantLight) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaDistantLight, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaDistantLight) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaDistantLight, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AmbientColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AmbientColor(self: InwOaDistantLight) -> InwLVec3f

Set: AmbientColor(self: InwOaDistantLight) = value
"""

    DiffuseColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiffuseColor(self: InwOaDistantLight) -> InwLVec3f

Set: DiffuseColor(self: InwOaDistantLight) = value
"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: InwOaDistantLight) -> InwLUnitVec3f

Set: Direction(self: InwOaDistantLight) = value
"""

    IsEye = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEye(self: InwOaDistantLight) -> bool

Set: IsEye(self: InwOaDistantLight) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaDistantLight) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaDistantLight) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaDistantLight) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaDistantLight) -> int

Set: nwLock(self: InwOaDistantLight) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaDistantLight) -> bool

Set: nwOwn(self: InwOaDistantLight) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaDistantLight) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaDistantLight) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaDistantLight) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaDistantLight) -> str

"""

    SpecularColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecularColor(self: InwOaDistantLight) -> InwLVec3f

Set: SpecularColor(self: InwOaDistantLight) = value
"""



class InwOaFragment(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaFragment) -> object """
        pass

    def GetLocalBox(self):
        """ GetLocalBox(self: InwOaFragment) -> InwLBox3f """
        pass

    def GetLocalToWorldMatrix(self):
        """ GetLocalToWorldMatrix(self: InwOaFragment) -> InwLTransform3f """
        pass

    def GetWorldBox(self):
        """ GetWorldBox(self: InwOaFragment) -> InwLBox3f """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaFragment, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaFragment) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaFragment, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Appearance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Appearance(self: InwOaFragment) -> object

"""

    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: InwOaFragment) -> object

"""

    IsTransformReverses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTransformReverses(self: InwOaFragment) -> bool

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaFragment) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaFragment) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaFragment) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaFragment) -> int

Set: nwLock(self: InwOaFragment) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaFragment) -> bool

Set: nwOwn(self: InwOaFragment) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaFragment) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaFragment) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaFragment) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaFragment) -> str

"""

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: path(self: InwOaFragment) -> InwOaPath

"""



class InwOaFragment2(InwOaFragment, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaFragment2) -> object """
        pass

    def GetLocalBox(self):
        """ GetLocalBox(self: InwOaFragment2) -> InwLBox3f """
        pass

    def GetLocalToWorldMatrix(self):
        """ GetLocalToWorldMatrix(self: InwOaFragment2) -> InwLTransform3f """
        pass

    def GetWorldBox(self):
        """ GetWorldBox(self: InwOaFragment2) -> InwLBox3f """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaFragment2, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaFragment2) """
        pass

    def SetLocalToWorldMatrix(self, Matrix, reverses, dynamic):
        """ SetLocalToWorldMatrix(self: InwOaFragment2, Matrix: InwLTransform3f, reverses: bool, dynamic: bool) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaFragment2, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Appearance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Appearance(self: InwOaFragment2) -> object

"""

    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: InwOaFragment2) -> object

"""

    IsTransformReverses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTransformReverses(self: InwOaFragment2) -> bool

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaFragment2) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaFragment2) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaFragment2) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaFragment2) -> int

Set: nwLock(self: InwOaFragment2) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaFragment2) -> bool

Set: nwOwn(self: InwOaFragment2) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaFragment2) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaFragment2) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaFragment2) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaFragment2) -> str

"""

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: path(self: InwOaFragment2) -> InwOaPath

"""



class InwOaFragment3(InwOaFragment2, InwOaFragment, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaFragment3) -> object """
        pass

    def GenerateSimplePrimitives(self, bits, cb):
        """ GenerateSimplePrimitives(self: InwOaFragment3, bits: nwEVertexProperty, cb: InwSimplePrimitivesCB) """
        pass

    def GetLocalBox(self):
        """ GetLocalBox(self: InwOaFragment3) -> InwLBox3f """
        pass

    def GetLocalToWorldMatrix(self):
        """ GetLocalToWorldMatrix(self: InwOaFragment3) -> InwLTransform3f """
        pass

    def GetWorldBox(self):
        """ GetWorldBox(self: InwOaFragment3) -> InwLBox3f """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaFragment3, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaFragment3) """
        pass

    def SetLocalToWorldMatrix(self, Matrix, reverses, dynamic):
        """ SetLocalToWorldMatrix(self: InwOaFragment3, Matrix: InwLTransform3f, reverses: bool, dynamic: bool) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaFragment3, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Appearance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Appearance(self: InwOaFragment3) -> object

"""

    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: InwOaFragment3) -> object

"""

    IsTransformReverses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTransformReverses(self: InwOaFragment3) -> bool

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaFragment3) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaFragment3) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaFragment3) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaFragment3) -> int

Set: nwLock(self: InwOaFragment3) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaFragment3) -> bool

Set: nwOwn(self: InwOaFragment3) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaFragment3) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaFragment3) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaFragment3) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaFragment3) -> str

"""

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: path(self: InwOaFragment3) -> InwOaPath

"""

    UserOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserOffset(self: InwOaFragment3) -> InwLVec3f

"""

    VertexProps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VertexProps(self: InwOaFragment3) -> nwEVertexProperty

"""



class InwOaNode(InwOaSceneBase, InwBase):
    # no doc
    def Attributes(self):
        """ Attributes(self: InwOaNode) -> InwNodeAttributesColl """
        pass

    def Copy(self):
        """ Copy(self: InwOaNode) -> object """
        pass

    def Fragments(self):
        """ Fragments(self: InwOaNode) -> InwNodeFragsColl """
        pass

    def GetBoundingBox(self, ignore_hidden, apply_xform):
        """ GetBoundingBox(self: InwOaNode, ignore_hidden: bool, apply_xform: bool) -> InwLBox3f """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaNode, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaNode) """
        pass

    def Rename(self, class_name, class_username):
        """ Rename(self: InwOaNode, class_name: str, class_username: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaNode, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwOaNode) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwOaNode) -> str

"""

    IsGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGeometry(self: InwOaNode) -> bool

"""

    IsGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGroup(self: InwOaNode) -> bool

"""

    IsInsert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInsert(self: InwOaNode) -> bool

"""

    IsLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLayer(self: InwOaNode) -> bool

"""

    IsOverrideHide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideHide(self: InwOaNode) -> bool

"""

    IsOverrideMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideMaterial(self: InwOaNode) -> bool

"""

    IsOverrideShow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideShow(self: InwOaNode) -> bool

"""

    IsOverrideTwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideTwoSided(self: InwOaNode) -> bool

"""

    IsPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPartition(self: InwOaNode) -> bool

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaNode) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaNode) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaNode) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaNode) -> int

Set: nwLock(self: InwOaNode) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaNode) -> bool

Set: nwOwn(self: InwOaNode) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaNode) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaNode) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaNode) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaNode) -> str

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwOaNode) -> str

Set: UserName(self: InwOaNode) = value
"""



class InwOaGeometry(InwOaNode, InwOaSceneBase, InwBase):
    # no doc
    def Attributes(self):
        """ Attributes(self: InwOaGeometry) -> InwNodeAttributesColl """
        pass

    def Copy(self):
        """ Copy(self: InwOaGeometry) -> object """
        pass

    def Fragments(self):
        """ Fragments(self: InwOaGeometry) -> InwNodeFragsColl """
        pass

    def GetBoundingBox(self, ignore_hidden, apply_xform):
        """ GetBoundingBox(self: InwOaGeometry, ignore_hidden: bool, apply_xform: bool) -> InwLBox3f """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaGeometry, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaGeometry) """
        pass

    def Rename(self, class_name, class_username):
        """ Rename(self: InwOaGeometry, class_name: str, class_username: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaGeometry, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwOaGeometry) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwOaGeometry) -> str

"""

    IsGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGeometry(self: InwOaGeometry) -> bool

"""

    IsGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGroup(self: InwOaGeometry) -> bool

"""

    IsInsert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInsert(self: InwOaGeometry) -> bool

"""

    IsLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLayer(self: InwOaGeometry) -> bool

"""

    IsOverrideHide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideHide(self: InwOaGeometry) -> bool

"""

    IsOverrideMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideMaterial(self: InwOaGeometry) -> bool

"""

    IsOverrideShow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideShow(self: InwOaGeometry) -> bool

"""

    IsOverrideTwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideTwoSided(self: InwOaGeometry) -> bool

"""

    IsPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPartition(self: InwOaGeometry) -> bool

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaGeometry) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaGeometry) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaGeometry) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaGeometry) -> int

Set: nwLock(self: InwOaGeometry) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaGeometry) -> bool

Set: nwOwn(self: InwOaGeometry) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaGeometry) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaGeometry) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaGeometry) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaGeometry) -> str

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwOaGeometry) -> str

Set: UserName(self: InwOaGeometry) = value
"""



class InwOaGroup(InwOaNode, InwOaSceneBase, InwBase):
    # no doc
    def Attributes(self):
        """ Attributes(self: InwOaGroup) -> InwNodeAttributesColl """
        pass

    def Children(self):
        """ Children(self: InwOaGroup) -> InwNodeNodesColl """
        pass

    def Copy(self):
        """ Copy(self: InwOaGroup) -> object """
        pass

    def Fragments(self):
        """ Fragments(self: InwOaGroup) -> InwNodeFragsColl """
        pass

    def GetBoundingBox(self, ignore_hidden, apply_xform):
        """ GetBoundingBox(self: InwOaGroup, ignore_hidden: bool, apply_xform: bool) -> InwLBox3f """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaGroup, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaGroup) """
        pass

    def Rename(self, class_name, class_username):
        """ Rename(self: InwOaGroup, class_name: str, class_username: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaGroup, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwOaGroup) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwOaGroup) -> str

"""

    IsGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGeometry(self: InwOaGroup) -> bool

"""

    IsGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGroup(self: InwOaGroup) -> bool

"""

    IsInsert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInsert(self: InwOaGroup) -> bool

"""

    IsLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLayer(self: InwOaGroup) -> bool

"""

    IsOverrideHide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideHide(self: InwOaGroup) -> bool

"""

    IsOverrideMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideMaterial(self: InwOaGroup) -> bool

"""

    IsOverrideShow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideShow(self: InwOaGroup) -> bool

"""

    IsOverrideTwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideTwoSided(self: InwOaGroup) -> bool

"""

    IsPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPartition(self: InwOaGroup) -> bool

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaGroup) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaGroup) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaGroup) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaGroup) -> int

Set: nwLock(self: InwOaGroup) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaGroup) -> bool

Set: nwOwn(self: InwOaGroup) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaGroup) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaGroup) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaGroup) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaGroup) -> str

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwOaGroup) -> str

Set: UserName(self: InwOaGroup) = value
"""



class InwOaMaterial(InwOaAttribute, InwOaSceneBase, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaMaterial) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaMaterial, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaMaterial) """
        pass

    def Rename(self, class_name, class_username):
        """ Rename(self: InwOaMaterial, class_name: str, class_username: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaMaterial, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AmbientColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AmbientColor(self: InwOaMaterial) -> InwLVec3f

Set: AmbientColor(self: InwOaMaterial) = value
"""

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwOaMaterial) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwOaMaterial) -> str

"""

    DiffuseColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiffuseColor(self: InwOaMaterial) -> InwLVec3f

Set: DiffuseColor(self: InwOaMaterial) = value
"""

    EmissiveColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EmissiveColor(self: InwOaMaterial) -> InwLVec3f

Set: EmissiveColor(self: InwOaMaterial) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaMaterial) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaMaterial) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaMaterial) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaMaterial) -> int

Set: nwLock(self: InwOaMaterial) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaMaterial) -> bool

Set: nwOwn(self: InwOaMaterial) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaMaterial) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaMaterial) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaMaterial) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaMaterial) -> str

"""

    Shininess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shininess(self: InwOaMaterial) -> float

Set: Shininess(self: InwOaMaterial) = value
"""

    SpecularColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecularColor(self: InwOaMaterial) -> InwLVec3f

Set: SpecularColor(self: InwOaMaterial) = value
"""

    transparency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: transparency(self: InwOaMaterial) -> float

Set: transparency(self: InwOaMaterial) = value
"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwOaMaterial) -> str

Set: UserName(self: InwOaMaterial) = value
"""



class InwOaNameAttribute(InwOaAttribute, InwOaSceneBase, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaNameAttribute) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaNameAttribute, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaNameAttribute) """
        pass

    def Rename(self, class_name, class_username):
        """ Rename(self: InwOaNameAttribute, class_name: str, class_username: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaNameAttribute, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwOaNameAttribute) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwOaNameAttribute) -> str

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaNameAttribute) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaNameAttribute) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaNameAttribute) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaNameAttribute) -> int

Set: nwLock(self: InwOaNameAttribute) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaNameAttribute) -> bool

Set: nwOwn(self: InwOaNameAttribute) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaNameAttribute) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaNameAttribute) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaNameAttribute) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaNameAttribute) -> str

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwOaNameAttribute) -> str

Set: UserName(self: InwOaNameAttribute) = value
"""



class InwOaNat64Attribute(InwOaAttribute, InwOaSceneBase, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaNat64Attribute) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaNat64Attribute, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaNat64Attribute) """
        pass

    def Rename(self, class_name, class_username):
        """ Rename(self: InwOaNat64Attribute, class_name: str, class_username: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaNat64Attribute, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwOaNat64Attribute) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwOaNat64Attribute) -> str

"""

    Nat64Hex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Nat64Hex(self: InwOaNat64Attribute) -> str

Set: Nat64Hex(self: InwOaNat64Attribute) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaNat64Attribute) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaNat64Attribute) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaNat64Attribute) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaNat64Attribute) -> int

Set: nwLock(self: InwOaNat64Attribute) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaNat64Attribute) -> bool

Set: nwOwn(self: InwOaNat64Attribute) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaNat64Attribute) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaNat64Attribute) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaNat64Attribute) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaNat64Attribute) -> str

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwOaNat64Attribute) -> str

Set: UserName(self: InwOaNat64Attribute) = value
"""



class InwOaPartition(InwOaGroup, InwOaNode, InwOaSceneBase, InwBase):
    # no doc
    def Attributes(self):
        """ Attributes(self: InwOaPartition) -> InwNodeAttributesColl """
        pass

    def Children(self):
        """ Children(self: InwOaPartition) -> InwNodeNodesColl """
        pass

    def Copy(self):
        """ Copy(self: InwOaPartition) -> object """
        pass

    def Fragments(self):
        """ Fragments(self: InwOaPartition) -> InwNodeFragsColl """
        pass

    def GetBoundingBox(self, ignore_hidden, apply_xform):
        """ GetBoundingBox(self: InwOaPartition, ignore_hidden: bool, apply_xform: bool) -> InwLBox3f """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaPartition, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaPartition) """
        pass

    def Rename(self, class_name, class_username):
        """ Rename(self: InwOaPartition, class_name: str, class_username: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaPartition, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwOaPartition) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwOaPartition) -> str

"""

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: filename(self: InwOaPartition) -> str

"""

    IsGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGeometry(self: InwOaPartition) -> bool

"""

    IsGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGroup(self: InwOaPartition) -> bool

"""

    IsInsert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInsert(self: InwOaPartition) -> bool

"""

    IsLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLayer(self: InwOaPartition) -> bool

"""

    IsOverrideHide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideHide(self: InwOaPartition) -> bool

"""

    IsOverrideMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideMaterial(self: InwOaPartition) -> bool

"""

    IsOverrideShow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideShow(self: InwOaPartition) -> bool

"""

    IsOverrideTwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideTwoSided(self: InwOaPartition) -> bool

"""

    IsPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPartition(self: InwOaPartition) -> bool

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaPartition) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaPartition) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaPartition) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaPartition) -> int

Set: nwLock(self: InwOaPartition) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaPartition) -> bool

Set: nwOwn(self: InwOaPartition) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaPartition) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaPartition) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaPartition) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaPartition) -> str

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwOaPartition) -> str

Set: UserName(self: InwOaPartition) = value
"""



class InwOaPartition2(InwOaPartition, InwOaGroup, InwOaNode, InwOaSceneBase, InwBase):
    # no doc
    def Attributes(self):
        """ Attributes(self: InwOaPartition2) -> InwNodeAttributesColl """
        pass

    def Children(self):
        """ Children(self: InwOaPartition2) -> InwNodeNodesColl """
        pass

    def Copy(self):
        """ Copy(self: InwOaPartition2) -> object """
        pass

    def Fragments(self):
        """ Fragments(self: InwOaPartition2) -> InwNodeFragsColl """
        pass

    def GetBoundingBox(self, ignore_hidden, apply_xform):
        """ GetBoundingBox(self: InwOaPartition2, ignore_hidden: bool, apply_xform: bool) -> InwLBox3f """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaPartition2, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaPartition2) """
        pass

    def Rename(self, class_name, class_username):
        """ Rename(self: InwOaPartition2, class_name: str, class_username: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaPartition2, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AngularUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngularUnits(self: InwOaPartition2) -> nwEAngularUnits

"""

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwOaPartition2) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwOaPartition2) -> str

"""

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: filename(self: InwOaPartition2) -> str

"""

    IsGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGeometry(self: InwOaPartition2) -> bool

"""

    IsGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGroup(self: InwOaPartition2) -> bool

"""

    IsInsert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInsert(self: InwOaPartition2) -> bool

"""

    IsLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLayer(self: InwOaPartition2) -> bool

"""

    IsOverrideHide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideHide(self: InwOaPartition2) -> bool

"""

    IsOverrideMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideMaterial(self: InwOaPartition2) -> bool

"""

    IsOverrideShow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideShow(self: InwOaPartition2) -> bool

"""

    IsOverrideTwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideTwoSided(self: InwOaPartition2) -> bool

"""

    IsPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPartition(self: InwOaPartition2) -> bool

"""

    LinearUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinearUnits(self: InwOaPartition2) -> nwELinearUnits

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaPartition2) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaPartition2) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaPartition2) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaPartition2) -> int

Set: nwLock(self: InwOaPartition2) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaPartition2) -> bool

Set: nwOwn(self: InwOaPartition2) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaPartition2) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaPartition2) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaPartition2) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaPartition2) -> str

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwOaPartition2) -> str

Set: UserName(self: InwOaPartition2) = value
"""



class InwOaPartition3(InwOaPartition2, InwOaPartition, InwOaGroup, InwOaNode, InwOaSceneBase, InwBase):
    # no doc
    def Attributes(self):
        """ Attributes(self: InwOaPartition3) -> InwNodeAttributesColl """
        pass

    def Children(self):
        """ Children(self: InwOaPartition3) -> InwNodeNodesColl """
        pass

    def Copy(self):
        """ Copy(self: InwOaPartition3) -> object """
        pass

    def Fragments(self):
        """ Fragments(self: InwOaPartition3) -> InwNodeFragsColl """
        pass

    def GetBoundingBox(self, ignore_hidden, apply_xform):
        """ GetBoundingBox(self: InwOaPartition3, ignore_hidden: bool, apply_xform: bool) -> InwLBox3f """
        pass

    def GetNorthVector(self):
        """ GetNorthVector(self: InwOaPartition3) -> InwLUnitVec3f """
        pass

    def GetUpVector(self):
        """ GetUpVector(self: InwOaPartition3) -> InwLUnitVec3f """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaPartition3, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaPartition3) """
        pass

    def Rename(self, class_name, class_username):
        """ Rename(self: InwOaPartition3, class_name: str, class_username: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaPartition3, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AngularUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngularUnits(self: InwOaPartition3) -> nwEAngularUnits

"""

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwOaPartition3) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwOaPartition3) -> str

"""

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: filename(self: InwOaPartition3) -> str

"""

    IsGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGeometry(self: InwOaPartition3) -> bool

"""

    IsGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGroup(self: InwOaPartition3) -> bool

"""

    IsInsert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInsert(self: InwOaPartition3) -> bool

"""

    IsLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLayer(self: InwOaPartition3) -> bool

"""

    IsOverrideHide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideHide(self: InwOaPartition3) -> bool

"""

    IsOverrideMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideMaterial(self: InwOaPartition3) -> bool

"""

    IsOverrideShow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideShow(self: InwOaPartition3) -> bool

"""

    IsOverrideTwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverrideTwoSided(self: InwOaPartition3) -> bool

"""

    IsPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPartition(self: InwOaPartition3) -> bool

"""

    LinearUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinearUnits(self: InwOaPartition3) -> nwELinearUnits

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaPartition3) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaPartition3) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaPartition3) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaPartition3) -> int

Set: nwLock(self: InwOaPartition3) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaPartition3) -> bool

Set: nwOwn(self: InwOaPartition3) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaPartition3) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaPartition3) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaPartition3) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaPartition3) -> str

"""

    SourceFilename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceFilename(self: InwOaPartition3) -> str

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwOaPartition3) -> str

Set: UserName(self: InwOaPartition3) = value
"""



class InwOaPath(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaPath) -> object """
        pass

    def Fragments(self):
        """ Fragments(self: InwOaPath) -> InwNodeFragsColl """
        pass

    def Nodes(self):
        """ Nodes(self: InwOaPath) -> InwPathNodesColl """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaPath, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaPath) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaPath, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ArrayData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArrayData(self: InwOaPath) -> object

Set: ArrayData(self: InwOaPath) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaPath) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaPath) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaPath) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaPath) -> int

Set: nwLock(self: InwOaPath) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaPath) -> bool

Set: nwOwn(self: InwOaPath) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaPath) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaPath) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaPath) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaPath) -> str

"""

    Serialise = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Serialise(self: InwOaPath) -> str

Set: Serialise(self: InwOaPath) = value
"""



class InwOaPath2(InwOaPath, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaPath2) -> object """
        pass

    def FindAttribute(self, class_name, b_forward, node):
        """ FindAttribute(self: InwOaPath2, class_name: str, b_forward: bool) -> (InwOaAttribute, object) """
        pass

    def Fragments(self):
        """ Fragments(self: InwOaPath2) -> InwNodeFragsColl """
        pass

    def Nodes(self):
        """ Nodes(self: InwOaPath2) -> InwPathNodesColl """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaPath2, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaPath2) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaPath2, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ArrayData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArrayData(self: InwOaPath2) -> object

Set: ArrayData(self: InwOaPath2) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaPath2) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaPath2) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaPath2) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaPath2) -> int

Set: nwLock(self: InwOaPath2) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaPath2) -> bool

Set: nwOwn(self: InwOaPath2) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaPath2) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaPath2) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaPath2) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaPath2) -> str

"""

    Serialise = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Serialise(self: InwOaPath2) -> str

Set: Serialise(self: InwOaPath2) = value
"""



class InwOaPath3(InwOaPath2, InwOaPath, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaPath3) -> object """
        pass

    def FindAttribute(self, class_name, b_forward, node):
        """ FindAttribute(self: InwOaPath3, class_name: str, b_forward: bool) -> (InwOaAttribute, object) """
        pass

    def Fragments(self):
        """ Fragments(self: InwOaPath3) -> InwNodeFragsColl """
        pass

    def GetBoundingBox(self):
        """ GetBoundingBox(self: InwOaPath3) -> InwLBox3f """
        pass

    def GetNextInstance(self):
        """ GetNextInstance(self: InwOaPath3) -> InwOaPath """
        pass

    def Nodes(self):
        """ Nodes(self: InwOaPath3) -> InwPathNodesColl """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaPath3, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaPath3) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaPath3, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ArrayData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArrayData(self: InwOaPath3) -> object

Set: ArrayData(self: InwOaPath3) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaPath3) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaPath3) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaPath3) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaPath3) -> int

Set: nwLock(self: InwOaPath3) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaPath3) -> bool

Set: nwOwn(self: InwOaPath3) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaPath3) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaPath3) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaPath3) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaPath3) -> str

"""

    Serialise = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Serialise(self: InwOaPath3) -> str

Set: Serialise(self: InwOaPath3) = value
"""



class InwOaPointLight(InwOaCommonLight, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaPointLight) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaPointLight, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaPointLight) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaPointLight, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AmbientColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AmbientColor(self: InwOaPointLight) -> InwLVec3f

Set: AmbientColor(self: InwOaPointLight) = value
"""

    Attenuation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attenuation(self: InwOaPointLight) -> InwLVec3f

Set: Attenuation(self: InwOaPointLight) = value
"""

    DiffuseColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiffuseColor(self: InwOaPointLight) -> InwLVec3f

Set: DiffuseColor(self: InwOaPointLight) = value
"""

    IsEye = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEye(self: InwOaPointLight) -> bool

Set: IsEye(self: InwOaPointLight) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaPointLight) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaPointLight) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaPointLight) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaPointLight) -> int

Set: nwLock(self: InwOaPointLight) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaPointLight) -> bool

Set: nwOwn(self: InwOaPointLight) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaPointLight) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaPointLight) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaPointLight) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaPointLight) -> str

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: InwOaPointLight) -> InwLPos3f

Set: Position(self: InwOaPointLight) = value
"""

    SpecularColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecularColor(self: InwOaPointLight) -> InwLVec3f

Set: SpecularColor(self: InwOaPointLight) = value
"""



class InwOaProperty(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaProperty) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaProperty, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaProperty) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaProperty, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwOaProperty) -> str

Set: name(self: InwOaProperty) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaProperty) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaProperty) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaProperty) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaProperty) -> int

Set: nwLock(self: InwOaProperty) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaProperty) -> bool

Set: nwOwn(self: InwOaProperty) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaProperty) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaProperty) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaProperty) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaProperty) -> str

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwOaProperty) -> str

Set: UserName(self: InwOaProperty) = value
"""

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: value(self: InwOaProperty) -> object

Set: value(self: InwOaProperty) = value
"""



class InwOaPropertyAttribute(InwOaNameAttribute, InwOaAttribute, InwOaSceneBase, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaPropertyAttribute) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaPropertyAttribute, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaPropertyAttribute) """
        pass

    def Properties(self):
        """ Properties(self: InwOaPropertyAttribute) -> InwOaPropertyColl """
        pass

    def Rename(self, class_name, class_username):
        """ Rename(self: InwOaPropertyAttribute, class_name: str, class_username: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaPropertyAttribute, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwOaPropertyAttribute) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwOaPropertyAttribute) -> str

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaPropertyAttribute) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaPropertyAttribute) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaPropertyAttribute) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaPropertyAttribute) -> int

Set: nwLock(self: InwOaPropertyAttribute) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaPropertyAttribute) -> bool

Set: nwOwn(self: InwOaPropertyAttribute) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaPropertyAttribute) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaPropertyAttribute) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaPropertyAttribute) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaPropertyAttribute) -> str

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwOaPropertyAttribute) -> str

Set: UserName(self: InwOaPropertyAttribute) = value
"""



class InwOaPropertyColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwOaPropertyColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwOaPropertyColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwOaPropertyColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwOaPropertyColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwOaPropertyColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwOaPropertyColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwOaPropertyColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwOaPropertyColl, ndx: int, p_newVal: object) """
        pass

    def Sort(self):
        """ Sort(self: InwOaPropertyColl) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwOaPropertyColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwOaPropertyColl) -> bool

"""



class InwOaPropertyVec(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaPropertyVec) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaPropertyVec, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaPropertyVec) """
        pass

    def Properties(self):
        """ Properties(self: InwOaPropertyVec) -> InwOaPropertyColl """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaPropertyVec, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaPropertyVec) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaPropertyVec) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaPropertyVec) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaPropertyVec) -> int

Set: nwLock(self: InwOaPropertyVec) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaPropertyVec) -> bool

Set: nwOwn(self: InwOaPropertyVec) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaPropertyVec) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaPropertyVec) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaPropertyVec) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaPropertyVec) -> str

"""



class InwOaPublishAttribute(InwOaAttribute, InwOaSceneBase, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaPublishAttribute) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaPublishAttribute, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaPublishAttribute) """
        pass

    def Rename(self, class_name, class_username):
        """ Rename(self: InwOaPublishAttribute, class_name: str, class_username: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaPublishAttribute, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Author = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Author(self: InwOaPublishAttribute) -> str

Set: Author(self: InwOaPublishAttribute) = value
"""

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwOaPublishAttribute) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwOaPublishAttribute) -> str

"""

    Comments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comments(self: InwOaPublishAttribute) -> str

Set: Comments(self: InwOaPublishAttribute) = value
"""

    Copyright = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Copyright(self: InwOaPublishAttribute) -> str

Set: Copyright(self: InwOaPublishAttribute) = value
"""

    ExpiryDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpiryDate(self: InwOaPublishAttribute) -> object

Set: ExpiryDate(self: InwOaPublishAttribute) = value
"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flags(self: InwOaPublishAttribute) -> nwEPublishFlags

Set: Flags(self: InwOaPublishAttribute) = value
"""

    Keywords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keywords(self: InwOaPublishAttribute) -> str

Set: Keywords(self: InwOaPublishAttribute) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaPublishAttribute) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaPublishAttribute) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaPublishAttribute) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaPublishAttribute) -> int

Set: nwLock(self: InwOaPublishAttribute) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaPublishAttribute) -> bool

Set: nwOwn(self: InwOaPublishAttribute) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaPublishAttribute) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaPublishAttribute) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaPublishAttribute) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaPublishAttribute) -> str

"""

    Password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Password(self: InwOaPublishAttribute) -> str

Set: Password(self: InwOaPublishAttribute) = value
"""

    PublishDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PublishDate(self: InwOaPublishAttribute) -> object

Set: PublishDate(self: InwOaPublishAttribute) = value
"""

    PublishedFor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PublishedFor(self: InwOaPublishAttribute) -> str

Set: PublishedFor(self: InwOaPublishAttribute) = value
"""

    Publisher = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Publisher(self: InwOaPublishAttribute) -> str

Set: Publisher(self: InwOaPublishAttribute) = value
"""

    Subject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Subject(self: InwOaPublishAttribute) -> str

Set: Subject(self: InwOaPublishAttribute) = value
"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Title(self: InwOaPublishAttribute) -> str

Set: Title(self: InwOaPublishAttribute) = value
"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwOaPublishAttribute) -> str

Set: UserName(self: InwOaPublishAttribute) = value
"""



class InwOaSpotLight(InwOaCommonLight, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaSpotLight) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaSpotLight, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaSpotLight) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaSpotLight, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AmbientColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AmbientColor(self: InwOaSpotLight) -> InwLVec3f

Set: AmbientColor(self: InwOaSpotLight) = value
"""

    Attenuation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attenuation(self: InwOaSpotLight) -> InwLVec3f

Set: Attenuation(self: InwOaSpotLight) = value
"""

    CutoffAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutoffAngle(self: InwOaSpotLight) -> float

Set: CutoffAngle(self: InwOaSpotLight) = value
"""

    DiffuseColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiffuseColor(self: InwOaSpotLight) -> InwLVec3f

Set: DiffuseColor(self: InwOaSpotLight) = value
"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: InwOaSpotLight) -> InwLUnitVec3f

Set: Direction(self: InwOaSpotLight) = value
"""

    DropOffRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DropOffRate(self: InwOaSpotLight) -> float

Set: DropOffRate(self: InwOaSpotLight) = value
"""

    IsEye = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEye(self: InwOaSpotLight) -> bool

Set: IsEye(self: InwOaSpotLight) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaSpotLight) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaSpotLight) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaSpotLight) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaSpotLight) -> int

Set: nwLock(self: InwOaSpotLight) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaSpotLight) -> bool

Set: nwOwn(self: InwOaSpotLight) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaSpotLight) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaSpotLight) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaSpotLight) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaSpotLight) -> str

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: InwOaSpotLight) -> InwLPos3f

Set: Position(self: InwOaSpotLight) = value
"""

    SpecularColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecularColor(self: InwOaSpotLight) -> InwLVec3f

Set: SpecularColor(self: InwOaSpotLight) = value
"""



class InwOaTextAttribute(InwOaNameAttribute, InwOaAttribute, InwOaSceneBase, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaTextAttribute) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaTextAttribute, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaTextAttribute) """
        pass

    def Rename(self, class_name, class_username):
        """ Rename(self: InwOaTextAttribute, class_name: str, class_username: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaTextAttribute, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwOaTextAttribute) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwOaTextAttribute) -> str

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaTextAttribute) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaTextAttribute) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaTextAttribute) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaTextAttribute) -> int

Set: nwLock(self: InwOaTextAttribute) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaTextAttribute) -> bool

Set: nwOwn(self: InwOaTextAttribute) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaTextAttribute) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaTextAttribute) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaTextAttribute) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaTextAttribute) -> str

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: InwOaTextAttribute) -> str

Set: Text(self: InwOaTextAttribute) = value
"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwOaTextAttribute) -> str

Set: UserName(self: InwOaTextAttribute) = value
"""



class InwOaTransform(InwOaAttribute, InwOaSceneBase, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaTransform) -> object """
        pass

    def GetTransform(self):
        """ GetTransform(self: InwOaTransform) -> InwLTransform3f """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaTransform, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaTransform) """
        pass

    def Rename(self, class_name, class_username):
        """ Rename(self: InwOaTransform, class_name: str, class_username: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaTransform, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwOaTransform) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwOaTransform) -> str

"""

    IsReverses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReverses(self: InwOaTransform) -> bool

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaTransform) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaTransform) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaTransform) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaTransform) -> int

Set: nwLock(self: InwOaTransform) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaTransform) -> bool

Set: nwOwn(self: InwOaTransform) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaTransform) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaTransform) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaTransform) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaTransform) -> str

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwOaTransform) -> str

Set: UserName(self: InwOaTransform) = value
"""



class InwOaURLAttribute(InwOaNameAttribute, InwOaAttribute, InwOaSceneBase, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOaURLAttribute) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOaURLAttribute, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOaURLAttribute) """
        pass

    def Rename(self, class_name, class_username):
        """ Rename(self: InwOaURLAttribute, class_name: str, class_username: str) """
        pass

    def URLs(self):
        """ URLs(self: InwOaURLAttribute) -> InwURLColl """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOaURLAttribute, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: InwOaURLAttribute) -> str

"""

    ClassUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassUserName(self: InwOaURLAttribute) -> str

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOaURLAttribute) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOaURLAttribute) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOaURLAttribute) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOaURLAttribute) -> int

Set: nwLock(self: InwOaURLAttribute) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOaURLAttribute) -> bool

Set: nwOwn(self: InwOaURLAttribute) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOaURLAttribute) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOaURLAttribute) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOaURLAttribute) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOaURLAttribute) -> str

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwOaURLAttribute) -> str

Set: UserName(self: InwOaURLAttribute) = value
"""



class InwOclClashTest(InwBase):
    # no doc
    def ClearResults(self):
        """ ClearResults(self: InwOclClashTest) """
        pass

    def Copy(self):
        """ Copy(self: InwOclClashTest) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOclClashTest, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOclClashTest) """
        pass

    def RemoveResolved(self):
        """ RemoveResolved(self: InwOclClashTest) """
        pass

    def results(self):
        """ results(self: InwOclClashTest) -> InwTestResultsColl """
        pass

    def RunTest(self, test_ndx, ovProgress):
        """ RunTest(self: InwOclClashTest, test_ndx: int, ovProgress: object) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOclClashTest, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AbsTouchTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AbsTouchTolerance(self: InwOclClashTest) -> float

Set: AbsTouchTolerance(self: InwOclClashTest) = value
"""

    ClashesIgnored = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClashesIgnored(self: InwOclClashTest) -> int

"""

    IgnoreRuleFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IgnoreRuleFlags(self: InwOclClashTest) -> nwEClashIgnore

Set: IgnoreRuleFlags(self: InwOclClashTest) = value
"""

    IntersectionMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IntersectionMethod(self: InwOclClashTest) -> nwEClashTestIntersectionMethod

Set: IntersectionMethod(self: InwOclClashTest) = value
"""

    IsRelTouchTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRelTouchTolerance(self: InwOclClashTest) -> bool

Set: IsRelTouchTolerance(self: InwOclClashTest) = value
"""

    Modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Modified(self: InwOclClashTest) -> bool

"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwOclClashTest) -> str

Set: name(self: InwOclClashTest) = value
"""

    NumNewResults = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumNewResults(self: InwOclClashTest) -> int

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOclClashTest) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOclClashTest) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOclClashTest) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOclClashTest) -> int

Set: nwLock(self: InwOclClashTest) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOclClashTest) -> bool

Set: nwOwn(self: InwOclClashTest) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOclClashTest) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOclClashTest) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOclClashTest) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOclClashTest) -> str

"""

    RelTouchTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelTouchTolerance(self: InwOclClashTest) -> float

Set: RelTouchTolerance(self: InwOclClashTest) = value
"""

    Selection1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selection1(self: InwOclClashTest) -> InwOpSelection

Set: Selection1(self: InwOclClashTest) = value
"""

    Selection2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selection2(self: InwOclClashTest) -> InwOpSelection

Set: Selection2(self: InwOclClashTest) = value
"""

    SelfIntersect1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelfIntersect1(self: InwOclClashTest) -> bool

Set: SelfIntersect1(self: InwOclClashTest) = value
"""

    SelfIntersect2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelfIntersect2(self: InwOclClashTest) -> bool

Set: SelfIntersect2(self: InwOclClashTest) = value
"""

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: status(self: InwOclClashTest) -> nwEClashTestStatus

Set: status(self: InwOclClashTest) = value
"""

    Tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tolerance(self: InwOclClashTest) -> float

Set: Tolerance(self: InwOclClashTest) = value
"""

    ToleranceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToleranceType(self: InwOclClashTest) -> nwEClashTestToleranceType

Set: ToleranceType(self: InwOclClashTest) = value
"""



class InwOclClashTest2(InwOclClashTest, InwBase):
    # no doc
    def ClearResults(self):
        """ ClearResults(self: InwOclClashTest2) """
        pass

    def Copy(self):
        """ Copy(self: InwOclClashTest2) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOclClashTest2, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOclClashTest2) """
        pass

    def RemoveResolved(self):
        """ RemoveResolved(self: InwOclClashTest2) """
        pass

    def results(self):
        """ results(self: InwOclClashTest2) -> InwTestResultsColl """
        pass

    def RunTest(self, test_ndx, ovProgress):
        """ RunTest(self: InwOclClashTest2, test_ndx: int, ovProgress: object) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOclClashTest2, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AbsTouchTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AbsTouchTolerance(self: InwOclClashTest2) -> float

Set: AbsTouchTolerance(self: InwOclClashTest2) = value
"""

    ClashesIgnored = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClashesIgnored(self: InwOclClashTest2) -> int

"""

    CustomTestName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomTestName(self: InwOclClashTest2) -> str

Set: CustomTestName(self: InwOclClashTest2) = value
"""

    IgnoreRuleFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IgnoreRuleFlags(self: InwOclClashTest2) -> nwEClashIgnore

Set: IgnoreRuleFlags(self: InwOclClashTest2) = value
"""

    IntersectionMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IntersectionMethod(self: InwOclClashTest2) -> nwEClashTestIntersectionMethod

Set: IntersectionMethod(self: InwOclClashTest2) = value
"""

    IsRelTouchTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRelTouchTolerance(self: InwOclClashTest2) -> bool

Set: IsRelTouchTolerance(self: InwOclClashTest2) = value
"""

    Modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Modified(self: InwOclClashTest2) -> bool

"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwOclClashTest2) -> str

Set: name(self: InwOclClashTest2) = value
"""

    NumNewResults = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumNewResults(self: InwOclClashTest2) -> int

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOclClashTest2) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOclClashTest2) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOclClashTest2) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOclClashTest2) -> int

Set: nwLock(self: InwOclClashTest2) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOclClashTest2) -> bool

Set: nwOwn(self: InwOclClashTest2) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOclClashTest2) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOclClashTest2) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOclClashTest2) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOclClashTest2) -> str

"""

    RelTouchTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelTouchTolerance(self: InwOclClashTest2) -> float

Set: RelTouchTolerance(self: InwOclClashTest2) = value
"""

    Selection1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selection1(self: InwOclClashTest2) -> InwOpSelection

Set: Selection1(self: InwOclClashTest2) = value
"""

    Selection2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selection2(self: InwOclClashTest2) -> InwOpSelection

Set: Selection2(self: InwOclClashTest2) = value
"""

    SelfIntersect1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelfIntersect1(self: InwOclClashTest2) -> bool

Set: SelfIntersect1(self: InwOclClashTest2) = value
"""

    SelfIntersect2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelfIntersect2(self: InwOclClashTest2) -> bool

Set: SelfIntersect2(self: InwOclClashTest2) = value
"""

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: status(self: InwOclClashTest2) -> nwEClashTestStatus

Set: status(self: InwOclClashTest2) = value
"""

    TestType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TestType(self: InwOclClashTest2) -> nwEClashTestType

Set: TestType(self: InwOclClashTest2) = value
"""

    Tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tolerance(self: InwOclClashTest2) -> float

Set: Tolerance(self: InwOclClashTest2) = value
"""

    ToleranceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToleranceType(self: InwOclClashTest2) -> nwEClashTestToleranceType

Set: ToleranceType(self: InwOclClashTest2) = value
"""



class InwOclTestResult(InwBase):
    # no doc
    def Comments(self):
        """ Comments(self: InwOclTestResult) -> InwCommentsColl """
        pass

    def Copy(self):
        """ Copy(self: InwOclTestResult) -> object """
        pass

    def CreatePicture(self, anonview, ovNumPasses, ovWidth, ovHeight, ovFlags):
        """ CreatePicture(self: InwOclTestResult, anonview: InwOpAnonView, ovNumPasses: object, ovWidth: object, ovHeight: object, ovFlags: object) -> object """
        pass

    def GetClashCenter(self):
        """ GetClashCenter(self: InwOclTestResult) -> InwLPos3f """
        pass

    def GetSuitableViewPoint(self):
        """ GetSuitableViewPoint(self: InwOclTestResult) -> InwNvViewPoint """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOclTestResult, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOclTestResult) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOclTestResult, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ApprovedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApprovedBy(self: InwOclTestResult) -> str

Set: ApprovedBy(self: InwOclTestResult) = value
"""

    ApprovedTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApprovedTime(self: InwOclTestResult) -> object

Set: ApprovedTime(self: InwOclTestResult) = value
"""

    Bound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bound(self: InwOclTestResult) -> InwLBox3f

"""

    CreatedTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedTime(self: InwOclTestResult) -> object

Set: CreatedTime(self: InwOclTestResult) = value
"""

    distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: distance(self: InwOclTestResult) -> float

"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwOclTestResult) -> str

Set: name(self: InwOclTestResult) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOclTestResult) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOclTestResult) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOclTestResult) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOclTestResult) -> int

Set: nwLock(self: InwOclTestResult) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOclTestResult) -> bool

Set: nwOwn(self: InwOclTestResult) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOclTestResult) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOclTestResult) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOclTestResult) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOclTestResult) -> str

"""

    Path1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path1(self: InwOclTestResult) -> InwOaPath

"""

    Path2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path2(self: InwOclTestResult) -> InwOaPath

"""

    Pt1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pt1(self: InwOclTestResult) -> InwLPos3f

"""

    Pt2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pt2(self: InwOclTestResult) -> InwLPos3f

"""

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: status(self: InwOclTestResult) -> nwETestResultStatus

Set: status(self: InwOclTestResult) = value
"""

    ViewPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewPoint(self: InwOclTestResult) -> InwNvViewPoint

Set: ViewPoint(self: InwOclTestResult) = value
"""



class InwOclTestResult2(InwOclTestResult, InwBase):
    # no doc
    def Comments(self):
        """ Comments(self: InwOclTestResult2) -> InwCommentsColl """
        pass

    def Copy(self):
        """ Copy(self: InwOclTestResult2) -> object """
        pass

    def CreatePicture(self, anonview, ovNumPasses, ovWidth, ovHeight, ovFlags):
        """ CreatePicture(self: InwOclTestResult2, anonview: InwOpAnonView, ovNumPasses: object, ovWidth: object, ovHeight: object, ovFlags: object) -> object """
        pass

    def GetClashCenter(self):
        """ GetClashCenter(self: InwOclTestResult2) -> InwLPos3f """
        pass

    def GetSuitableViewPoint(self):
        """ GetSuitableViewPoint(self: InwOclTestResult2) -> InwNvViewPoint """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOclTestResult2, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOclTestResult2) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOclTestResult2, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ApprovedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApprovedBy(self: InwOclTestResult2) -> str

Set: ApprovedBy(self: InwOclTestResult2) = value
"""

    ApprovedTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApprovedTime(self: InwOclTestResult2) -> object

Set: ApprovedTime(self: InwOclTestResult2) = value
"""

    AssignedTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssignedTo(self: InwOclTestResult2) -> str

Set: AssignedTo(self: InwOclTestResult2) = value
"""

    Bound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bound(self: InwOclTestResult2) -> InwLBox3f

"""

    CreatedTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedTime(self: InwOclTestResult2) -> object

Set: CreatedTime(self: InwOclTestResult2) = value
"""

    distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: distance(self: InwOclTestResult2) -> float

"""

    GroupPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupPath(self: InwOclTestResult2) -> str

"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwOclTestResult2) -> str

Set: name(self: InwOclTestResult2) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOclTestResult2) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOclTestResult2) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOclTestResult2) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOclTestResult2) -> int

Set: nwLock(self: InwOclTestResult2) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOclTestResult2) -> bool

Set: nwOwn(self: InwOclTestResult2) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOclTestResult2) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOclTestResult2) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOclTestResult2) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOclTestResult2) -> str

"""

    Path1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path1(self: InwOclTestResult2) -> InwOaPath

"""

    Path2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path2(self: InwOclTestResult2) -> InwOaPath

"""

    Pt1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pt1(self: InwOclTestResult2) -> InwLPos3f

"""

    Pt2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pt2(self: InwOclTestResult2) -> InwLPos3f

"""

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: status(self: InwOclTestResult2) -> nwETestResultStatus

Set: status(self: InwOclTestResult2) = value
"""

    ViewPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewPoint(self: InwOclTestResult2) -> InwNvViewPoint

Set: ViewPoint(self: InwOclTestResult2) = value
"""



class InwOpSavedView(InwBase):
    # no doc
    def Comments(self):
        """ Comments(self: InwOpSavedView) -> InwCommentsColl """
        pass

    def Copy(self):
        """ Copy(self: InwOpSavedView) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpSavedView, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpSavedView) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpSavedView, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwOpSavedView) -> str

Set: name(self: InwOpSavedView) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpSavedView) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpSavedView) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpSavedView) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpSavedView) -> int

Set: nwLock(self: InwOpSavedView) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpSavedView) -> bool

Set: nwOwn(self: InwOpSavedView) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpSavedView) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpSavedView) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpSavedView) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpSavedView) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: InwOpSavedView) -> nwESavedViewType

"""



class InwOpGroupView(InwOpSavedView, InwBase):
    # no doc
    def Comments(self):
        """ Comments(self: InwOpGroupView) -> InwCommentsColl """
        pass

    def Copy(self):
        """ Copy(self: InwOpGroupView) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpGroupView, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpGroupView) """
        pass

    def SavedViews(self):
        """ SavedViews(self: InwOpGroupView) -> InwSavedViewsColl """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpGroupView, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwOpGroupView) -> str

Set: name(self: InwOpGroupView) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpGroupView) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpGroupView) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpGroupView) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpGroupView) -> int

Set: nwLock(self: InwOpGroupView) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpGroupView) -> bool

Set: nwOwn(self: InwOpGroupView) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpGroupView) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpGroupView) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpGroupView) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpGroupView) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: InwOpGroupView) -> nwESavedViewType

"""



class InwOpAnimView(InwOpGroupView, InwOpSavedView, InwBase):
    # no doc
    def Comments(self):
        """ Comments(self: InwOpAnimView) -> InwCommentsColl """
        pass

    def Copy(self):
        """ Copy(self: InwOpAnimView) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpAnimView, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpAnimView) """
        pass

    def SavedViews(self):
        """ SavedViews(self: InwOpAnimView) -> InwSavedViewsColl """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpAnimView, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Looped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Looped(self: InwOpAnimView) -> bool

Set: Looped(self: InwOpAnimView) = value
"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwOpAnimView) -> str

Set: name(self: InwOpAnimView) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpAnimView) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpAnimView) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpAnimView) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpAnimView) -> int

Set: nwLock(self: InwOpAnimView) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpAnimView) -> bool

Set: nwOwn(self: InwOpAnimView) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpAnimView) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpAnimView) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpAnimView) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpAnimView) -> str

"""

    Smoothing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Smoothing(self: InwOpAnimView) -> nwEAnimSmoothing

Set: Smoothing(self: InwOpAnimView) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: InwOpAnimView) -> nwESavedViewType

"""



class InwOpAnonView(InwBase):
    # no doc
    def ClippingPlanes(self):
        """ ClippingPlanes(self: InwOpAnonView) -> InwClippingPlaneColl """
        pass

    def Copy(self):
        """ Copy(self: InwOpAnonView) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpAnonView, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpAnonView) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpAnonView, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpAnonView) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpAnonView) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpAnonView) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpAnonView) -> int

Set: nwLock(self: InwOpAnonView) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpAnonView) -> bool

Set: nwOwn(self: InwOpAnonView) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpAnonView) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpAnonView) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpAnonView) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpAnonView) -> str

"""

    ViewPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewPoint(self: InwOpAnonView) -> InwNvViewPoint

Set: ViewPoint(self: InwOpAnonView) = value
"""



class InwOpClashElement(InwBase):
    # no doc
    def ClearResults(self):
        """ ClearResults(self: InwOpClashElement) """
        pass

    def Copy(self):
        """ Copy(self: InwOpClashElement) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpClashElement, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpClashElement) """
        pass

    def RemoveResolved(self):
        """ RemoveResolved(self: InwOpClashElement) """
        pass

    def RunAllTests(self, ovProgress):
        """ RunAllTests(self: InwOpClashElement, ovProgress: object) """
        pass

    def Tests(self):
        """ Tests(self: InwOpClashElement) -> InwClashTestsColl """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpClashElement, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpClashElement) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpClashElement) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpClashElement) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpClashElement) -> int

Set: nwLock(self: InwOpClashElement) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpClashElement) -> bool

Set: nwOwn(self: InwOpClashElement) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpClashElement) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpClashElement) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpClashElement) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpClashElement) -> str

"""



class InwOpComment(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOpComment) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpComment, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpComment) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpComment, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Body(self: InwOpComment) -> str

Set: Body(self: InwOpComment) = value
"""

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Date(self: InwOpComment) -> object

Set: Date(self: InwOpComment) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpComment) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpComment) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpComment) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpComment) -> int

Set: nwLock(self: InwOpComment) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpComment) -> bool

Set: nwOwn(self: InwOpComment) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpComment) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpComment) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpComment) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpComment) -> str

"""

    User = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: User(self: InwOpComment) -> str

Set: User(self: InwOpComment) = value
"""



class InwOpComment2(InwOpComment, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOpComment2) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpComment2, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpComment2) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpComment2, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Body(self: InwOpComment2) -> str

Set: Body(self: InwOpComment2) = value
"""

    CommentID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommentID(self: InwOpComment2) -> int

Set: CommentID(self: InwOpComment2) = value
"""

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Date(self: InwOpComment2) -> object

Set: Date(self: InwOpComment2) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpComment2) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpComment2) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpComment2) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpComment2) -> int

Set: nwLock(self: InwOpComment2) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpComment2) -> bool

Set: nwOwn(self: InwOpComment2) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpComment2) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpComment2) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpComment2) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpComment2) -> str

"""

    User = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: User(self: InwOpComment2) -> str

Set: User(self: InwOpComment2) = value
"""



class InwOpComment3(InwOpComment2, InwOpComment, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOpComment3) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpComment3, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpComment3) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpComment3, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Body(self: InwOpComment3) -> str

Set: Body(self: InwOpComment3) = value
"""

    CommentID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommentID(self: InwOpComment3) -> int

Set: CommentID(self: InwOpComment3) = value
"""

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Date(self: InwOpComment3) -> object

Set: Date(self: InwOpComment3) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpComment3) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpComment3) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpComment3) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpComment3) -> int

Set: nwLock(self: InwOpComment3) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpComment3) -> bool

Set: nwOwn(self: InwOpComment3) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpComment3) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpComment3) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpComment3) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpComment3) -> str

"""

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: status(self: InwOpComment3) -> nwECommentStatus

Set: status(self: InwOpComment3) = value
"""

    User = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: User(self: InwOpComment3) -> str

Set: User(self: InwOpComment3) = value
"""



class InwOpCutView(InwOpSavedView, InwBase):
    # no doc
    def Comments(self):
        """ Comments(self: InwOpCutView) -> InwCommentsColl """
        pass

    def Copy(self):
        """ Copy(self: InwOpCutView) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpCutView, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpCutView) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpCutView, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwOpCutView) -> str

Set: name(self: InwOpCutView) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpCutView) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpCutView) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpCutView) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpCutView) -> int

Set: nwLock(self: InwOpCutView) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpCutView) -> bool

Set: nwOwn(self: InwOpCutView) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpCutView) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpCutView) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpCutView) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpCutView) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: InwOpCutView) -> nwESavedViewType

"""



class InwOpFind(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOpFind) -> object """
        pass

    def Find(self, first, match_data):
        """ Find(self: InwOpFind) -> (InwOaPath, bool, object) """
        pass

    def FindAll(self):
        """ FindAll(self: InwOpFind) -> InwOpSelection """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpFind, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpFind) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpFind, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    FindSpec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FindSpec(self: InwOpFind) -> InwOpFindSpec

Set: FindSpec(self: InwOpFind) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpFind) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpFind) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpFind) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpFind) -> int

Set: nwLock(self: InwOpFind) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpFind) -> bool

Set: nwOwn(self: InwOpFind) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpFind) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpFind) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpFind) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpFind) -> str

"""



class InwOpFindCondition(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOpFindCondition) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpFindCondition, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpFindCondition) """
        pass

    def SetAttributeNames(self, internal_name, user_name):
        """ SetAttributeNames(self: InwOpFindCondition, internal_name: str, user_name: object) """
        pass

    def SetPropertyNames(self, internal_name, user_name):
        """ SetPropertyNames(self: InwOpFindCondition, internal_name: str, user_name: object) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpFindCondition, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AttributeInternalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttributeInternalName(self: InwOpFindCondition) -> str

"""

    AttributeUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttributeUserName(self: InwOpFindCondition) -> str

"""

    Condition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Condition(self: InwOpFindCondition) -> nwEFindCondition

Set: Condition(self: InwOpFindCondition) = value
"""

    NegateCondition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NegateCondition(self: InwOpFindCondition) -> bool

Set: NegateCondition(self: InwOpFindCondition) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpFindCondition) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpFindCondition) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpFindCondition) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpFindCondition) -> int

Set: nwLock(self: InwOpFindCondition) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpFindCondition) -> bool

Set: nwOwn(self: InwOpFindCondition) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpFindCondition) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpFindCondition) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpFindCondition) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpFindCondition) -> str

"""

    PropertyInternalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyInternalName(self: InwOpFindCondition) -> str

"""

    PropertyUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyUserName(self: InwOpFindCondition) -> str

"""

    StartGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartGroup(self: InwOpFindCondition) -> bool

Set: StartGroup(self: InwOpFindCondition) = value
"""

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: value(self: InwOpFindCondition) -> object

Set: value(self: InwOpFindCondition) = value
"""

    ValueCaseSensitive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueCaseSensitive(self: InwOpFindCondition) -> bool

Set: ValueCaseSensitive(self: InwOpFindCondition) = value
"""



class InwOpFindConditionsColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwOpFindConditionsColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwOpFindConditionsColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwOpFindConditionsColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwOpFindConditionsColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwOpFindConditionsColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwOpFindConditionsColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwOpFindConditionsColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwOpFindConditionsColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwOpFindConditionsColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwOpFindConditionsColl) -> bool

"""



class InwOpFindSpec(InwBase):
    # no doc
    def Conditions(self):
        """ Conditions(self: InwOpFindSpec) -> InwOpFindConditionsColl """
        pass

    def Copy(self):
        """ Copy(self: InwOpFindSpec) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpFindSpec, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpFindSpec) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpFindSpec, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpFindSpec) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpFindSpec) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpFindSpec) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpFindSpec) -> int

Set: nwLock(self: InwOpFindSpec) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpFindSpec) -> bool

Set: nwOwn(self: InwOpFindSpec) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpFindSpec) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpFindSpec) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpFindSpec) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpFindSpec) -> str

"""

    ResultDisjoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResultDisjoint(self: InwOpFindSpec) -> bool

Set: ResultDisjoint(self: InwOpFindSpec) = value
"""

    SearchMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SearchMode(self: InwOpFindSpec) -> nwESearchMode

Set: SearchMode(self: InwOpFindSpec) = value
"""

    selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: selection(self: InwOpFindSpec) -> InwOpSelection

Set: selection(self: InwOpFindSpec) = value
"""



class InwOpFolderView(InwOpGroupView, InwOpSavedView, InwBase):
    # no doc
    def Comments(self):
        """ Comments(self: InwOpFolderView) -> InwCommentsColl """
        pass

    def Copy(self):
        """ Copy(self: InwOpFolderView) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpFolderView, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpFolderView) """
        pass

    def SavedViews(self):
        """ SavedViews(self: InwOpFolderView) -> InwSavedViewsColl """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpFolderView, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwOpFolderView) -> str

Set: name(self: InwOpFolderView) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpFolderView) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpFolderView) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpFolderView) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpFolderView) -> int

Set: nwLock(self: InwOpFolderView) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpFolderView) -> bool

Set: nwOwn(self: InwOpFolderView) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpFolderView) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpFolderView) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpFolderView) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpFolderView) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: InwOpFolderView) -> nwESavedViewType

"""



class InwOpInternalPlugin(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOpInternalPlugin) -> object """
        pass

    def GetParameterData(self, ndx):
        """ GetParameterData(self: InwOpInternalPlugin, ndx: int) -> object """
        pass

    def GetParameterId(self, ndx):
        """ GetParameterId(self: InwOpInternalPlugin, ndx: int) -> str """
        pass

    def GetParameterName(self, ndx):
        """ GetParameterName(self: InwOpInternalPlugin, ndx: int) -> str """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpInternalPlugin, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpInternalPlugin) """
        pass

    def SetParameterData(self, ndx, data):
        """ SetParameterData(self: InwOpInternalPlugin, ndx: int, data: object) -> bool """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpInternalPlugin, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    InternalDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalDisplayName(self: InwOpInternalPlugin) -> str

"""

    InternalObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalObjectName(self: InwOpInternalPlugin) -> str

"""

    NumParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumParameters(self: InwOpInternalPlugin) -> int

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpInternalPlugin) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpInternalPlugin) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpInternalPlugin) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpInternalPlugin) -> int

Set: nwLock(self: InwOpInternalPlugin) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpInternalPlugin) -> bool

Set: nwOwn(self: InwOpInternalPlugin) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpInternalPlugin) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpInternalPlugin) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpInternalPlugin) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpInternalPlugin) -> str

"""



class InwOpProgress(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOpProgress) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpProgress, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpProgress) """
        pass

    def Progress(self, fraction_done):
        """ Progress(self: InwOpProgress, fraction_done: float) -> bool """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpProgress, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpProgress) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpProgress) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpProgress) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpProgress) -> int

Set: nwLock(self: InwOpProgress) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpProgress) -> bool

Set: nwOwn(self: InwOpProgress) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpProgress) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpProgress) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpProgress) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpProgress) -> str

"""



class InwOpSelection(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOpSelection) -> object """
        pass

    def Invert(self):
        """ Invert(self: InwOpSelection) """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpSelection, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpSelection) """
        pass

    def Paths(self):
        """ Paths(self: InwOpSelection) -> InwSelectionPathsColl """
        pass

    def SelectAll(self):
        """ SelectAll(self: InwOpSelection) """
        pass

    def SelectNone(self):
        """ SelectNone(self: InwOpSelection) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpSelection, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpSelection) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpSelection) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpSelection) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpSelection) -> int

Set: nwLock(self: InwOpSelection) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpSelection) -> bool

Set: nwOwn(self: InwOpSelection) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpSelection) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpSelection) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpSelection) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpSelection) -> str

"""



class InwOpSelection2(InwOpSelection, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOpSelection2) -> object """
        pass

    def IntersectContents(self, sel):
        """ IntersectContents(self: InwOpSelection2, sel: InwOpSelection) """
        pass

    def IntersectSelection(self, sel):
        """ IntersectSelection(self: InwOpSelection2, sel: InwOpSelection) """
        pass

    def Invert(self):
        """ Invert(self: InwOpSelection2) """
        pass

    def IsAllSelected(self):
        """ IsAllSelected(self: InwOpSelection2) -> bool """
        pass

    def IsAnyContained(self, sel):
        """ IsAnyContained(self: InwOpSelection2, sel: InwOpSelection) -> bool """
        pass

    def IsContentsIntersected(self, sel):
        """ IsContentsIntersected(self: InwOpSelection2, sel: InwOpSelection) -> bool """
        pass

    def IsDisjoint(self):
        """ IsDisjoint(self: InwOpSelection2) -> bool """
        pass

    def IsNoneSelected(self):
        """ IsNoneSelected(self: InwOpSelection2) -> bool """
        pass

    def IsPathContained(self, path):
        """ IsPathContained(self: InwOpSelection2, path: InwOaPath) -> bool """
        pass

    def IsPathSelected(self, path):
        """ IsPathSelected(self: InwOpSelection2, path: InwOaPath) -> bool """
        pass

    def IsSelectionContained(self, sel):
        """ IsSelectionContained(self: InwOpSelection2, sel: InwOpSelection) -> bool """
        pass

    def IsSelectionSelected(self, sel):
        """ IsSelectionSelected(self: InwOpSelection2, sel: InwOpSelection) -> bool """
        pass

    def IsTailContained(self, tail):
        """ IsTailContained(self: InwOpSelection2, tail: InwOaNode) -> bool """
        pass

    def IsTailSelected(self, tail):
        """ IsTailSelected(self: InwOpSelection2, tail: InwOaNode) -> bool """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpSelection2, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpSelection2) """
        pass

    def Paths(self):
        """ Paths(self: InwOpSelection2) -> InwSelectionPathsColl """
        pass

    def SelectAll(self):
        """ SelectAll(self: InwOpSelection2) """
        pass

    def SelectNone(self):
        """ SelectNone(self: InwOpSelection2) """
        pass

    def SubtractContents(self, sel):
        """ SubtractContents(self: InwOpSelection2, sel: InwOpSelection) """
        pass

    def SubtractSelection(self, sel):
        """ SubtractSelection(self: InwOpSelection2, sel: InwOpSelection) """
        pass

    def UniteContents(self, sel):
        """ UniteContents(self: InwOpSelection2, sel: InwOpSelection) """
        pass

    def UniteSelection(self, sel):
        """ UniteSelection(self: InwOpSelection2, sel: InwOpSelection) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpSelection2, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpSelection2) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpSelection2) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpSelection2) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpSelection2) -> int

Set: nwLock(self: InwOpSelection2) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpSelection2) -> bool

Set: nwOwn(self: InwOpSelection2) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpSelection2) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpSelection2) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpSelection2) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpSelection2) -> str

"""



class InwOpSelectionSet(InwBase):
    # no doc
    def Comments(self):
        """ Comments(self: InwOpSelectionSet) -> InwCommentsColl """
        pass

    def Copy(self):
        """ Copy(self: InwOpSelectionSet) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpSelectionSet, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpSelectionSet) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpSelectionSet, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Author = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Author(self: InwOpSelectionSet) -> str

Set: Author(self: InwOpSelectionSet) = value
"""

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Date(self: InwOpSelectionSet) -> object

Set: Date(self: InwOpSelectionSet) = value
"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwOpSelectionSet) -> str

Set: name(self: InwOpSelectionSet) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpSelectionSet) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpSelectionSet) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpSelectionSet) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpSelectionSet) -> int

Set: nwLock(self: InwOpSelectionSet) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpSelectionSet) -> bool

Set: nwOwn(self: InwOpSelectionSet) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpSelectionSet) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpSelectionSet) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpSelectionSet) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpSelectionSet) -> str

"""

    selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: selection(self: InwOpSelectionSet) -> InwOpSelection

Set: selection(self: InwOpSelectionSet) = value
"""



class InwOpSelectionSet2(InwOpSelectionSet, InwBase):
    # no doc
    def Comments(self):
        """ Comments(self: InwOpSelectionSet2) -> InwCommentsColl """
        pass

    def Copy(self):
        """ Copy(self: InwOpSelectionSet2) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpSelectionSet2, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpSelectionSet2) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpSelectionSet2, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Author = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Author(self: InwOpSelectionSet2) -> str

Set: Author(self: InwOpSelectionSet2) = value
"""

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Date(self: InwOpSelectionSet2) -> object

Set: Date(self: InwOpSelectionSet2) = value
"""

    ImplicitFindSpec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImplicitFindSpec(self: InwOpSelectionSet2) -> InwOpFindSpec

Set: ImplicitFindSpec(self: InwOpSelectionSet2) = value
"""

    IsImplicit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsImplicit(self: InwOpSelectionSet2) -> bool

"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwOpSelectionSet2) -> str

Set: name(self: InwOpSelectionSet2) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpSelectionSet2) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpSelectionSet2) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpSelectionSet2) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpSelectionSet2) -> int

Set: nwLock(self: InwOpSelectionSet2) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpSelectionSet2) -> bool

Set: nwOwn(self: InwOpSelectionSet2) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpSelectionSet2) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpSelectionSet2) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpSelectionSet2) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpSelectionSet2) -> str

"""

    selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: selection(self: InwOpSelectionSet2) -> InwOpSelection

Set: selection(self: InwOpSelectionSet2) = value
"""



class InwOpSelectionTreeInterface:
    # no doc
    def iCreateHandle(self, path):
        """ iCreateHandle(self: InwOpSelectionTreeInterface, path: InwUInt32Vector) -> int """
        pass

    def iDestroyHandle(self, path, user_handle):
        """ iDestroyHandle(self: InwOpSelectionTreeInterface, path: InwUInt32Vector, user_handle: int) """
        pass

    def iGetIcon(self, path, user_handle):
        """ iGetIcon(self: InwOpSelectionTreeInterface, path: InwUInt32Vector, user_handle: int) -> nwESelTreeIcon """
        pass

    def iGetName(self, path, user_handle):
        """ iGetName(self: InwOpSelectionTreeInterface, path: InwUInt32Vector, user_handle: int) -> str """
        pass

    def iGetNumChildren(self, path, user_handle):
        """ iGetNumChildren(self: InwOpSelectionTreeInterface, path: InwUInt32Vector, user_handle: int) -> int """
        pass

    def iGetNumRootChildren(self):
        """ iGetNumRootChildren(self: InwOpSelectionTreeInterface) -> int """
        pass

    def iGetSelectedIcon(self, path, user_handle):
        """ iGetSelectedIcon(self: InwOpSelectionTreeInterface, path: InwUInt32Vector, user_handle: int) -> nwESelTreeIcon """
        pass

    def iGetSelection(self, path, user_handle, selection):
        """ iGetSelection(self: InwOpSelectionTreeInterface, path: InwUInt32Vector, user_handle: int, selection: InwOpSelection) """
        pass

    def iGetTextColor(self, path, user_handle, txt_color):
        """ iGetTextColor(self: InwOpSelectionTreeInterface, path: InwUInt32Vector, user_handle: int, txt_color: InwLVec3f) """
        pass

    def iGetTextFormat(self, path, user_handle):
        """ iGetTextFormat(self: InwOpSelectionTreeInterface, path: InwUInt32Vector, user_handle: int) -> nwESelTreeTextFormat """
        pass

    def iOnBeginContextMenu(self, path, user_handle):
        """ iOnBeginContextMenu(self: InwOpSelectionTreeInterface, path: InwUInt32Vector, user_handle: int) """
        pass

    def iOnCollapsed(self, path, user_handle):
        """ iOnCollapsed(self: InwOpSelectionTreeInterface, path: InwUInt32Vector, user_handle: int) """
        pass

    def iOnEndContextMenu(self, path, user_handle):
        """ iOnEndContextMenu(self: InwOpSelectionTreeInterface, path: InwUInt32Vector, user_handle: int) """
        pass

    def iOnLButtonDown(self, path, user_handle, is_selected, is_shift, is_ctrl):
        """ iOnLButtonDown(self: InwOpSelectionTreeInterface, path: InwUInt32Vector, user_handle: int, is_selected: bool, is_shift: bool, is_ctrl: bool) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InwOpState(InwBase):
    # no doc
    def ApplyView(self, view):
        """ ApplyView(self: InwOpState, view: InwOpView) """
        pass

    def BeginEdit(self, name):
        """ BeginEdit(self: InwOpState, name: str) """
        pass

    def Copy(self):
        """ Copy(self: InwOpState) -> object """
        pass

    def CreatePicture(self, anonview, ovNumPasses, vWidth, ovHeight):
        """ CreatePicture(self: InwOpState, anonview: InwOpAnonView, ovNumPasses: object, vWidth: object, ovHeight: object) -> object """
        pass

    def CreatePlugin(self, progid):
        """ CreatePlugin(self: InwOpState, progid: str) -> int """
        pass

    def EndEdit(self):
        """ EndEdit(self: InwOpState) """
        pass

    def GetBoundingBox(self):
        """ GetBoundingBox(self: InwOpState) -> InwLBox3f """
        pass

    def GetEnum(self, sName):
        """ GetEnum(self: InwOpState, sName: str) -> int """
        pass

    def HiddenItemsResetAll(self):
        """ HiddenItemsResetAll(self: InwOpState) """
        pass

    def NdxArray2Node(self, fullpath):
        """ NdxArray2Node(self: InwOpState, fullpath: object) -> InwOaNode """
        pass

    def NdxArray2SavedView(self, fullpath):
        """ NdxArray2SavedView(self: InwOpState, fullpath: object) -> InwOpSavedView """
        pass

    def Node2NdxArray(self, pI):
        """ Node2NdxArray(self: InwOpState, pI: InwOaNode) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpState, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpState) """
        pass

    def ObjectFactory(self, eType, ovReserved1, ovReserved2):
        """ ObjectFactory(self: InwOpState, eType: nwEObjectType, ovReserved1: object, ovReserved2: object) -> object """
        pass

    def OverrideColor(self, selection, color):
        """ OverrideColor(self: InwOpState, selection: InwOpSelection, color: InwLVec3f) """
        pass

    def OverrideReset(self, selection):
        """ OverrideReset(self: InwOpState, selection: InwOpSelection) """
        pass

    def OverrideResetAll(self):
        """ OverrideResetAll(self: InwOpState) """
        pass

    def OverrideTransparency(self, selection, transparency):
        """ OverrideTransparency(self: InwOpState, selection: InwOpSelection, transparency: float) """
        pass

    def Plugins(self):
        """ Plugins(self: InwOpState) -> InwPluginsColl """
        pass

    def RequiredItemsResetAll(self):
        """ RequiredItemsResetAll(self: InwOpState) """
        pass

    def SavedView2NdxArray(self, pI):
        """ SavedView2NdxArray(self: InwOpState, pI: InwOpSavedView) -> object """
        pass

    def SavedViews(self):
        """ SavedViews(self: InwOpState) -> InwSavedViewsColl """
        pass

    def SceneLights(self):
        """ SceneLights(self: InwOpState) -> InwLightsColl """
        pass

    def SeekSelection(self, results, cb, ovStartSelection):
        """ SeekSelection(self: InwOpState, results: InwOpSelection, cb: InwSeekSelection, ovStartSelection: object) """
        pass

    def SelectionSets(self):
        """ SelectionSets(self: InwOpState) -> InwSelectionSetColl """
        pass

    def StopMovement(self):
        """ StopMovement(self: InwOpState) """
        pass

    def ViewAll(self):
        """ ViewAll(self: InwOpState) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpState, vIn: object) -> object """
        pass

    def ZoomInCurViewOnCurSel(self):
        """ ZoomInCurViewOnCurSel(self: InwOpState) """
        pass

    def ZoomInCurViewOnSel(self, selection):
        """ ZoomInCurViewOnSel(self: InwOpState, selection: InwOpSelection) """
        pass

    def ZoomInViewOnSel(self, selection, anonview):
        """ ZoomInViewOnSel(self: InwOpState, selection: InwOpSelection, anonview: InwOpAnonView) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AreaCullThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaCullThreshold(self: InwOpState) -> float

Set: AreaCullThreshold(self: InwOpState) = value
"""

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColor(self: InwOpState) -> InwLVec3f

Set: BackgroundColor(self: InwOpState) = value
"""

    CurrentAnimation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAnimation(self: InwOpState) -> InwOpAnimView

Set: CurrentAnimation(self: InwOpState) = value
"""

    CurrentPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPartition(self: InwOpState) -> InwOaPartition

"""

    CurrentPlanView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPlanView(self: InwOpState) -> InwOpAnonView

Set: CurrentPlanView(self: InwOpState) = value
"""

    CurrentSectionView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSectionView(self: InwOpState) -> InwOpAnonView

Set: CurrentSectionView(self: InwOpState) = value
"""

    CurrentSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSelection(self: InwOpState) -> InwOpSelection

Set: CurrentSelection(self: InwOpState) = value
"""

    CurrentView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentView(self: InwOpState) -> InwOpAnonView

Set: CurrentView(self: InwOpState) = value
"""

    EventsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventsEnabled(self: InwOpState) -> bool

Set: EventsEnabled(self: InwOpState) = value
"""

    FrameRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameRate(self: InwOpState) -> int

Set: FrameRate(self: InwOpState) = value
"""

    GlobalAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalAmbient(self: InwOpState) -> InwLVec3f

Set: GlobalAmbient(self: InwOpState) = value
"""

    HeadlightAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightAmbient(self: InwOpState) -> float

Set: HeadlightAmbient(self: InwOpState) = value
"""

    HeadlightIntensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightIntensity(self: InwOpState) -> float

Set: HeadlightIntensity(self: InwOpState) = value
"""

    MaxNearDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxNearDistance(self: InwOpState) -> float

Set: MaxNearDistance(self: InwOpState) = value
"""

    MinFarDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinFarDistance(self: InwOpState) -> float

Set: MinFarDistance(self: InwOpState) = value
"""

    NumTriangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumTriangles(self: InwOpState) -> int

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpState) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpState) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpState) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpState) -> int

Set: nwLock(self: InwOpState) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpState) -> bool

Set: nwOwn(self: InwOpState) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpState) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpState) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpState) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpState) -> str

"""

    TwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TwoSided(self: InwOpState) -> bool

Set: TwoSided(self: InwOpState) = value
"""



class InwOpState2(InwOpState, InwBase):
    # no doc
    def ApplyView(self, view):
        """ ApplyView(self: InwOpState2, view: InwOpView) """
        pass

    def BeginEdit(self, name):
        """ BeginEdit(self: InwOpState2, name: str) """
        pass

    def Copy(self):
        """ Copy(self: InwOpState2) -> object """
        pass

    def CreatePicture(self, anonview, ovNumPasses, vWidth, ovHeight):
        """ CreatePicture(self: InwOpState2, anonview: InwOpAnonView, ovNumPasses: object, vWidth: object, ovHeight: object) -> object """
        pass

    def CreatePlugin(self, progid):
        """ CreatePlugin(self: InwOpState2, progid: str) -> int """
        pass

    def EndEdit(self):
        """ EndEdit(self: InwOpState2) """
        pass

    def GetBoundingBox(self):
        """ GetBoundingBox(self: InwOpState2) -> InwLBox3f """
        pass

    def GetEnum(self, sName):
        """ GetEnum(self: InwOpState2, sName: str) -> int """
        pass

    def HiddenItemsResetAll(self):
        """ HiddenItemsResetAll(self: InwOpState2) """
        pass

    def NdxArray2Node(self, fullpath):
        """ NdxArray2Node(self: InwOpState2, fullpath: object) -> InwOaNode """
        pass

    def NdxArray2SavedView(self, fullpath):
        """ NdxArray2SavedView(self: InwOpState2, fullpath: object) -> InwOpSavedView """
        pass

    def Node2NdxArray(self, pI):
        """ Node2NdxArray(self: InwOpState2, pI: InwOaNode) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpState2, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpState2) """
        pass

    def ObjectFactory(self, eType, ovReserved1, ovReserved2):
        """ ObjectFactory(self: InwOpState2, eType: nwEObjectType, ovReserved1: object, ovReserved2: object) -> object """
        pass

    def OverrideColor(self, selection, color):
        """ OverrideColor(self: InwOpState2, selection: InwOpSelection, color: InwLVec3f) """
        pass

    def OverrideReset(self, selection):
        """ OverrideReset(self: InwOpState2, selection: InwOpSelection) """
        pass

    def OverrideResetAll(self):
        """ OverrideResetAll(self: InwOpState2) """
        pass

    def OverrideTransform(self, selection, transform):
        """ OverrideTransform(self: InwOpState2, selection: InwOpSelection, transform: InwLTransform3f) """
        pass

    def OverrideTransformReset(self, selection):
        """ OverrideTransformReset(self: InwOpState2, selection: InwOpSelection) """
        pass

    def OverrideTransformResetAll(self):
        """ OverrideTransformResetAll(self: InwOpState2) """
        pass

    def OverrideTransparency(self, selection, transparency):
        """ OverrideTransparency(self: InwOpState2, selection: InwOpSelection, transparency: float) """
        pass

    def Plugins(self):
        """ Plugins(self: InwOpState2) -> InwPluginsColl """
        pass

    def RequiredItemsResetAll(self):
        """ RequiredItemsResetAll(self: InwOpState2) """
        pass

    def SavedView2NdxArray(self, pI):
        """ SavedView2NdxArray(self: InwOpState2, pI: InwOpSavedView) -> object """
        pass

    def SavedViews(self):
        """ SavedViews(self: InwOpState2) -> InwSavedViewsColl """
        pass

    def SceneLights(self):
        """ SceneLights(self: InwOpState2) -> InwLightsColl """
        pass

    def SeekSelection(self, results, cb, ovStartSelection):
        """ SeekSelection(self: InwOpState2, results: InwOpSelection, cb: InwSeekSelection, ovStartSelection: object) """
        pass

    def SelectionSets(self):
        """ SelectionSets(self: InwOpState2) -> InwSelectionSetColl """
        pass

    def StopMovement(self):
        """ StopMovement(self: InwOpState2) """
        pass

    def ViewAll(self):
        """ ViewAll(self: InwOpState2) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpState2, vIn: object) -> object """
        pass

    def ZoomInCurViewOnCurSel(self):
        """ ZoomInCurViewOnCurSel(self: InwOpState2) """
        pass

    def ZoomInCurViewOnSel(self, selection):
        """ ZoomInCurViewOnSel(self: InwOpState2, selection: InwOpSelection) """
        pass

    def ZoomInViewOnSel(self, selection, anonview):
        """ ZoomInViewOnSel(self: InwOpState2, selection: InwOpSelection, anonview: InwOpAnonView) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AreaCullThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaCullThreshold(self: InwOpState2) -> float

Set: AreaCullThreshold(self: InwOpState2) = value
"""

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColor(self: InwOpState2) -> InwLVec3f

Set: BackgroundColor(self: InwOpState2) = value
"""

    CurrentAnimation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAnimation(self: InwOpState2) -> InwOpAnimView

Set: CurrentAnimation(self: InwOpState2) = value
"""

    CurrentPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPartition(self: InwOpState2) -> InwOaPartition

"""

    CurrentPlanView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPlanView(self: InwOpState2) -> InwOpAnonView

Set: CurrentPlanView(self: InwOpState2) = value
"""

    CurrentSectionView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSectionView(self: InwOpState2) -> InwOpAnonView

Set: CurrentSectionView(self: InwOpState2) = value
"""

    CurrentSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSelection(self: InwOpState2) -> InwOpSelection

Set: CurrentSelection(self: InwOpState2) = value
"""

    CurrentView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentView(self: InwOpState2) -> InwOpAnonView

Set: CurrentView(self: InwOpState2) = value
"""

    EventsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventsEnabled(self: InwOpState2) -> bool

Set: EventsEnabled(self: InwOpState2) = value
"""

    FrameRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameRate(self: InwOpState2) -> int

Set: FrameRate(self: InwOpState2) = value
"""

    GlobalAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalAmbient(self: InwOpState2) -> InwLVec3f

Set: GlobalAmbient(self: InwOpState2) = value
"""

    HeadlightAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightAmbient(self: InwOpState2) -> float

Set: HeadlightAmbient(self: InwOpState2) = value
"""

    HeadlightIntensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightIntensity(self: InwOpState2) -> float

Set: HeadlightIntensity(self: InwOpState2) = value
"""

    MaxNearDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxNearDistance(self: InwOpState2) -> float

Set: MaxNearDistance(self: InwOpState2) = value
"""

    MinFarDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinFarDistance(self: InwOpState2) -> float

Set: MinFarDistance(self: InwOpState2) = value
"""

    NumTriangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumTriangles(self: InwOpState2) -> int

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpState2) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpState2) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpState2) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpState2) -> int

Set: nwLock(self: InwOpState2) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpState2) -> bool

Set: nwOwn(self: InwOpState2) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpState2) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpState2) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpState2) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpState2) -> str

"""

    TwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TwoSided(self: InwOpState2) -> bool

Set: TwoSided(self: InwOpState2) = value
"""



class InwOpState3(InwOpState2, InwOpState, InwBase):
    # no doc
    def ApplyView(self, view):
        """ ApplyView(self: InwOpState3, view: InwOpView) """
        pass

    def BeginEdit(self, name):
        """ BeginEdit(self: InwOpState3, name: str) """
        pass

    def Copy(self):
        """ Copy(self: InwOpState3) -> object """
        pass

    def CreatePicture(self, anonview, ovNumPasses, vWidth, ovHeight):
        """ CreatePicture(self: InwOpState3, anonview: InwOpAnonView, ovNumPasses: object, vWidth: object, ovHeight: object) -> object """
        pass

    def CreatePlugin(self, progid):
        """ CreatePlugin(self: InwOpState3, progid: str) -> int """
        pass

    def DeleteSelectedFiles(self):
        """ DeleteSelectedFiles(self: InwOpState3) """
        pass

    def EndEdit(self):
        """ EndEdit(self: InwOpState3) """
        pass

    def GetAttributeProperties(self, p_attribute):
        """ GetAttributeProperties(self: InwOpState3, p_attribute: InwOaAttribute) -> InwOaPropertyVec """
        pass

    def GetBoundingBox(self):
        """ GetBoundingBox(self: InwOpState3) -> InwLBox3f """
        pass

    def GetEnum(self, sName):
        """ GetEnum(self: InwOpState3, sName: str) -> int """
        pass

    def GetGUIPropertyNode(self, p_path, b_show_internal):
        """ GetGUIPropertyNode(self: InwOpState3, p_path: InwOaPath, b_show_internal: bool) -> InwGUIPropertyNode """
        pass

    def GetMeasureDiff(self):
        """ GetMeasureDiff(self: InwOpState3) -> InwLVec3f """
        pass

    def GetMeasureEndPos(self):
        """ GetMeasureEndPos(self: InwOpState3) -> InwLPos3f """
        pass

    def GetMeasureFirstPos(self):
        """ GetMeasureFirstPos(self: InwOpState3) -> InwLPos3f """
        pass

    def GetMeasureValue(self):
        """ GetMeasureValue(self: InwOpState3) -> float """
        pass

    def GetOverrideURL(self, p_path, include_model):
        """ GetOverrideURL(self: InwOpState3, p_path: InwOaPath, include_model: object) -> InwURLOverride """
        pass

    def GlobalProperties(self):
        """ GlobalProperties(self: InwOpState3) -> InwGlobalProperties """
        pass

    def HiddenItemsResetAll(self):
        """ HiddenItemsResetAll(self: InwOpState3) """
        pass

    def IsComposite(self, group):
        """ IsComposite(self: InwOpState3, group: InwOaGroup) -> bool """
        pass

    def NdxArray2Node(self, fullpath):
        """ NdxArray2Node(self: InwOpState3, fullpath: object) -> InwOaNode """
        pass

    def NdxArray2SavedView(self, fullpath):
        """ NdxArray2SavedView(self: InwOpState3, fullpath: object) -> InwOpSavedView """
        pass

    def Node2NdxArray(self, pI):
        """ Node2NdxArray(self: InwOpState3, pI: InwOaNode) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpState3, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpState3) """
        pass

    def ObjectFactory(self, eType, ovReserved1, ovReserved2):
        """ ObjectFactory(self: InwOpState3, eType: nwEObjectType, ovReserved1: object, ovReserved2: object) -> object """
        pass

    def OverrideColor(self, selection, color):
        """ OverrideColor(self: InwOpState3, selection: InwOpSelection, color: InwLVec3f) """
        pass

    def OverrideReset(self, selection):
        """ OverrideReset(self: InwOpState3, selection: InwOpSelection) """
        pass

    def OverrideResetAll(self):
        """ OverrideResetAll(self: InwOpState3) """
        pass

    def OverrideTransform(self, selection, transform):
        """ OverrideTransform(self: InwOpState3, selection: InwOpSelection, transform: InwLTransform3f) """
        pass

    def OverrideTransformReset(self, selection):
        """ OverrideTransformReset(self: InwOpState3, selection: InwOpSelection) """
        pass

    def OverrideTransformResetAll(self):
        """ OverrideTransformResetAll(self: InwOpState3) """
        pass

    def OverrideTransparency(self, selection, transparency):
        """ OverrideTransparency(self: InwOpState3, selection: InwOpSelection, transparency: float) """
        pass

    def OverrideURLReset(self, selection):
        """ OverrideURLReset(self: InwOpState3, selection: InwOpSelection) """
        pass

    def OverrideURLResetAll(self):
        """ OverrideURLResetAll(self: InwOpState3) """
        pass

    def Plugins(self):
        """ Plugins(self: InwOpState3) -> InwPluginsColl """
        pass

    def RequiredItemsResetAll(self):
        """ RequiredItemsResetAll(self: InwOpState3) """
        pass

    def SavedView2NdxArray(self, pI):
        """ SavedView2NdxArray(self: InwOpState3, pI: InwOpSavedView) -> object """
        pass

    def SavedViews(self):
        """ SavedViews(self: InwOpState3) -> InwSavedViewsColl """
        pass

    def SceneLights(self):
        """ SceneLights(self: InwOpState3) -> InwLightsColl """
        pass

    def SeekSelection(self, results, cb, ovStartSelection):
        """ SeekSelection(self: InwOpState3, results: InwOpSelection, cb: InwSeekSelection, ovStartSelection: object) """
        pass

    def SelectionSets(self):
        """ SelectionSets(self: InwOpState3) -> InwSelectionSetColl """
        pass

    def SetOverrideURL(self, selection, pI):
        """ SetOverrideURL(self: InwOpState3, selection: InwOpSelection, pI: InwURLOverride) """
        pass

    def StdName(self, Type, user_name):
        """ StdName(self: InwOpState3, Type: nwEStdName, user_name: bool) -> str """
        pass

    def StopMovement(self):
        """ StopMovement(self: InwOpState3) """
        pass

    def ViewAll(self):
        """ ViewAll(self: InwOpState3) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpState3, vIn: object) -> object """
        pass

    def ZoomInCurViewOnCurSel(self):
        """ ZoomInCurViewOnCurSel(self: InwOpState3) """
        pass

    def ZoomInCurViewOnSel(self, selection):
        """ ZoomInCurViewOnSel(self: InwOpState3, selection: InwOpSelection) """
        pass

    def ZoomInViewOnSel(self, selection, anonview):
        """ ZoomInViewOnSel(self: InwOpState3, selection: InwOpSelection, anonview: InwOpAnonView) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AreaCullThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaCullThreshold(self: InwOpState3) -> float

Set: AreaCullThreshold(self: InwOpState3) = value
"""

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColor(self: InwOpState3) -> InwLVec3f

Set: BackgroundColor(self: InwOpState3) = value
"""

    CurrentAnimation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAnimation(self: InwOpState3) -> InwOpAnimView

Set: CurrentAnimation(self: InwOpState3) = value
"""

    CurrentFindSpec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentFindSpec(self: InwOpState3) -> InwOpFindSpec

Set: CurrentFindSpec(self: InwOpState3) = value
"""

    CurrentPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPartition(self: InwOpState3) -> InwOaPartition

"""

    CurrentPlanView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPlanView(self: InwOpState3) -> InwOpAnonView

Set: CurrentPlanView(self: InwOpState3) = value
"""

    CurrentSectionView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSectionView(self: InwOpState3) -> InwOpAnonView

Set: CurrentSectionView(self: InwOpState3) = value
"""

    CurrentSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSelection(self: InwOpState3) -> InwOpSelection

Set: CurrentSelection(self: InwOpState3) = value
"""

    CurrentView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentView(self: InwOpState3) -> InwOpAnonView

Set: CurrentView(self: InwOpState3) = value
"""

    EventsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventsEnabled(self: InwOpState3) -> bool

Set: EventsEnabled(self: InwOpState3) = value
"""

    FrameRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameRate(self: InwOpState3) -> int

Set: FrameRate(self: InwOpState3) = value
"""

    GlobalAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalAmbient(self: InwOpState3) -> InwLVec3f

Set: GlobalAmbient(self: InwOpState3) = value
"""

    HeadlightAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightAmbient(self: InwOpState3) -> float

Set: HeadlightAmbient(self: InwOpState3) = value
"""

    HeadlightIntensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightIntensity(self: InwOpState3) -> float

Set: HeadlightIntensity(self: InwOpState3) = value
"""

    MaxNearDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxNearDistance(self: InwOpState3) -> float

Set: MaxNearDistance(self: InwOpState3) = value
"""

    MinFarDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinFarDistance(self: InwOpState3) -> float

Set: MinFarDistance(self: InwOpState3) = value
"""

    NumTriangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumTriangles(self: InwOpState3) -> int

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpState3) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpState3) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpState3) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpState3) -> int

Set: nwLock(self: InwOpState3) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpState3) -> bool

Set: nwOwn(self: InwOpState3) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpState3) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpState3) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpState3) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpState3) -> str

"""

    SmartTagsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmartTagsEnabled(self: InwOpState3) -> bool

Set: SmartTagsEnabled(self: InwOpState3) = value
"""

    TwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TwoSided(self: InwOpState3) -> bool

Set: TwoSided(self: InwOpState3) = value
"""

    URLsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsEnabled(self: InwOpState3) -> bool

Set: URLsEnabled(self: InwOpState3) = value
"""



class InwOpState4(InwOpState3, InwOpState2, InwOpState, InwBase):
    # no doc
    def ApplyView(self, view):
        """ ApplyView(self: InwOpState4, view: InwOpView) """
        pass

    def BeginEdit(self, name):
        """ BeginEdit(self: InwOpState4, name: str) """
        pass

    def Copy(self):
        """ Copy(self: InwOpState4) -> object """
        pass

    def CreatePicture(self, anonview, ovNumPasses, vWidth, ovHeight):
        """ CreatePicture(self: InwOpState4, anonview: InwOpAnonView, ovNumPasses: object, vWidth: object, ovHeight: object) -> object """
        pass

    def CreatePlugin(self, progid):
        """ CreatePlugin(self: InwOpState4, progid: str) -> int """
        pass

    def DeleteSelectedFiles(self):
        """ DeleteSelectedFiles(self: InwOpState4) """
        pass

    def DriveIOPlugin(self, internal_name, filename, opts):
        """ DriveIOPlugin(self: InwOpState4, internal_name: str, filename: str, opts: InwOaPropertyVec) -> nwEExportStatus """
        pass

    def EndEdit(self):
        """ EndEdit(self: InwOpState4) """
        pass

    def GetAttributeProperties(self, p_attribute):
        """ GetAttributeProperties(self: InwOpState4, p_attribute: InwOaAttribute) -> InwOaPropertyVec """
        pass

    def GetBoundingBox(self):
        """ GetBoundingBox(self: InwOpState4) -> InwLBox3f """
        pass

    def GetEnum(self, sName):
        """ GetEnum(self: InwOpState4, sName: str) -> int """
        pass

    def GetFirstInstanceOfNode(self, node):
        """ GetFirstInstanceOfNode(self: InwOpState4, node: InwOaNode) -> InwOaPath """
        pass

    def GetGUIPropertyNode(self, p_path, b_show_internal):
        """ GetGUIPropertyNode(self: InwOpState4, p_path: InwOaPath, b_show_internal: bool) -> InwGUIPropertyNode """
        pass

    def GetIOPluginOptions(self, internal_name):
        """ GetIOPluginOptions(self: InwOpState4, internal_name: str) -> InwOaPropertyVec """
        pass

    def GetMeasureDiff(self):
        """ GetMeasureDiff(self: InwOpState4) -> InwLVec3f """
        pass

    def GetMeasureEndPos(self):
        """ GetMeasureEndPos(self: InwOpState4) -> InwLPos3f """
        pass

    def GetMeasureFirstPos(self):
        """ GetMeasureFirstPos(self: InwOpState4) -> InwLPos3f """
        pass

    def GetMeasureValue(self):
        """ GetMeasureValue(self: InwOpState4) -> float """
        pass

    def GetOverrideURL(self, p_path, include_model):
        """ GetOverrideURL(self: InwOpState4, p_path: InwOaPath, include_model: object) -> InwURLOverride """
        pass

    def GlobalProperties(self):
        """ GlobalProperties(self: InwOpState4) -> InwGlobalProperties """
        pass

    def HiddenItemsResetAll(self):
        """ HiddenItemsResetAll(self: InwOpState4) """
        pass

    def IsComposite(self, group):
        """ IsComposite(self: InwOpState4, group: InwOaGroup) -> bool """
        pass

    def NdxArray2Node(self, fullpath):
        """ NdxArray2Node(self: InwOpState4, fullpath: object) -> InwOaNode """
        pass

    def NdxArray2SavedView(self, fullpath):
        """ NdxArray2SavedView(self: InwOpState4, fullpath: object) -> InwOpSavedView """
        pass

    def Node2NdxArray(self, pI):
        """ Node2NdxArray(self: InwOpState4, pI: InwOaNode) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpState4, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpState4) """
        pass

    def ObjectFactory(self, eType, ovReserved1, ovReserved2):
        """ ObjectFactory(self: InwOpState4, eType: nwEObjectType, ovReserved1: object, ovReserved2: object) -> object """
        pass

    def OverrideColor(self, selection, color):
        """ OverrideColor(self: InwOpState4, selection: InwOpSelection, color: InwLVec3f) """
        pass

    def OverrideReset(self, selection):
        """ OverrideReset(self: InwOpState4, selection: InwOpSelection) """
        pass

    def OverrideResetAll(self):
        """ OverrideResetAll(self: InwOpState4) """
        pass

    def OverrideTransform(self, selection, transform):
        """ OverrideTransform(self: InwOpState4, selection: InwOpSelection, transform: InwLTransform3f) """
        pass

    def OverrideTransformReset(self, selection):
        """ OverrideTransformReset(self: InwOpState4, selection: InwOpSelection) """
        pass

    def OverrideTransformResetAll(self):
        """ OverrideTransformResetAll(self: InwOpState4) """
        pass

    def OverrideTransparency(self, selection, transparency):
        """ OverrideTransparency(self: InwOpState4, selection: InwOpSelection, transparency: float) """
        pass

    def OverrideURLReset(self, selection):
        """ OverrideURLReset(self: InwOpState4, selection: InwOpSelection) """
        pass

    def OverrideURLResetAll(self):
        """ OverrideURLResetAll(self: InwOpState4) """
        pass

    def Plugins(self):
        """ Plugins(self: InwOpState4) -> InwPluginsColl """
        pass

    def RequiredItemsResetAll(self):
        """ RequiredItemsResetAll(self: InwOpState4) """
        pass

    def SavedView2NdxArray(self, pI):
        """ SavedView2NdxArray(self: InwOpState4, pI: InwOpSavedView) -> object """
        pass

    def SavedViews(self):
        """ SavedViews(self: InwOpState4) -> InwSavedViewsColl """
        pass

    def SceneLights(self):
        """ SceneLights(self: InwOpState4) -> InwLightsColl """
        pass

    def SeekSelection(self, results, cb, ovStartSelection):
        """ SeekSelection(self: InwOpState4, results: InwOpSelection, cb: InwSeekSelection, ovStartSelection: object) """
        pass

    def SelectionSets(self):
        """ SelectionSets(self: InwOpState4) -> InwSelectionSetColl """
        pass

    def SetOverrideURL(self, selection, pI):
        """ SetOverrideURL(self: InwOpState4, selection: InwOpSelection, pI: InwURLOverride) """
        pass

    def SmartTagText(self, path):
        """ SmartTagText(self: InwOpState4, path: InwOaPath) -> str """
        pass

    def StdName(self, Type, user_name):
        """ StdName(self: InwOpState4, Type: nwEStdName, user_name: bool) -> str """
        pass

    def StopMovement(self):
        """ StopMovement(self: InwOpState4) """
        pass

    def ViewAll(self):
        """ ViewAll(self: InwOpState4) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpState4, vIn: object) -> object """
        pass

    def ZoomInCurViewOnBoundingBox(self, box, factor):
        """ ZoomInCurViewOnBoundingBox(self: InwOpState4, box: InwLBox3f, factor: float) """
        pass

    def ZoomInCurViewOnCurSel(self):
        """ ZoomInCurViewOnCurSel(self: InwOpState4) """
        pass

    def ZoomInCurViewOnSel(self, selection):
        """ ZoomInCurViewOnSel(self: InwOpState4, selection: InwOpSelection) """
        pass

    def ZoomInViewOnSel(self, selection, anonview):
        """ ZoomInViewOnSel(self: InwOpState4, selection: InwOpSelection, anonview: InwOpAnonView) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AreaCullThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaCullThreshold(self: InwOpState4) -> float

Set: AreaCullThreshold(self: InwOpState4) = value
"""

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColor(self: InwOpState4) -> InwLVec3f

Set: BackgroundColor(self: InwOpState4) = value
"""

    CurrentAnimation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAnimation(self: InwOpState4) -> InwOpAnimView

Set: CurrentAnimation(self: InwOpState4) = value
"""

    CurrentFindSpec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentFindSpec(self: InwOpState4) -> InwOpFindSpec

Set: CurrentFindSpec(self: InwOpState4) = value
"""

    CurrentPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPartition(self: InwOpState4) -> InwOaPartition

"""

    CurrentPlanView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPlanView(self: InwOpState4) -> InwOpAnonView

Set: CurrentPlanView(self: InwOpState4) = value
"""

    CurrentSectionView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSectionView(self: InwOpState4) -> InwOpAnonView

Set: CurrentSectionView(self: InwOpState4) = value
"""

    CurrentSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSelection(self: InwOpState4) -> InwOpSelection

Set: CurrentSelection(self: InwOpState4) = value
"""

    CurrentView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentView(self: InwOpState4) -> InwOpAnonView

Set: CurrentView(self: InwOpState4) = value
"""

    EventsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventsEnabled(self: InwOpState4) -> bool

Set: EventsEnabled(self: InwOpState4) = value
"""

    FrameRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameRate(self: InwOpState4) -> int

Set: FrameRate(self: InwOpState4) = value
"""

    GlobalAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalAmbient(self: InwOpState4) -> InwLVec3f

Set: GlobalAmbient(self: InwOpState4) = value
"""

    HeadlightAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightAmbient(self: InwOpState4) -> float

Set: HeadlightAmbient(self: InwOpState4) = value
"""

    HeadlightIntensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightIntensity(self: InwOpState4) -> float

Set: HeadlightIntensity(self: InwOpState4) = value
"""

    MaxNearDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxNearDistance(self: InwOpState4) -> float

Set: MaxNearDistance(self: InwOpState4) = value
"""

    MinFarDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinFarDistance(self: InwOpState4) -> float

Set: MinFarDistance(self: InwOpState4) = value
"""

    NumTriangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumTriangles(self: InwOpState4) -> int

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpState4) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpState4) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpState4) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpState4) -> int

Set: nwLock(self: InwOpState4) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpState4) -> bool

Set: nwOwn(self: InwOpState4) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpState4) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpState4) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpState4) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpState4) -> str

"""

    SmartTagsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmartTagsEnabled(self: InwOpState4) -> bool

Set: SmartTagsEnabled(self: InwOpState4) = value
"""

    TwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TwoSided(self: InwOpState4) -> bool

Set: TwoSided(self: InwOpState4) = value
"""

    URLsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsEnabled(self: InwOpState4) -> bool

Set: URLsEnabled(self: InwOpState4) = value
"""



class InwOpState5(InwOpState4, InwOpState3, InwOpState2, InwOpState, InwBase):
    # no doc
    def ApplyView(self, view):
        """ ApplyView(self: InwOpState5, view: InwOpView) """
        pass

    def BeginEdit(self, name):
        """ BeginEdit(self: InwOpState5, name: str) """
        pass

    def CheckLicense(self, name):
        """ CheckLicense(self: InwOpState5, name: str) -> bool """
        pass

    def Copy(self):
        """ Copy(self: InwOpState5) -> object """
        pass

    def CreatePicture(self, anonview, ovNumPasses, vWidth, ovHeight):
        """ CreatePicture(self: InwOpState5, anonview: InwOpAnonView, ovNumPasses: object, vWidth: object, ovHeight: object) -> object """
        pass

    def CreatePlugin(self, progid):
        """ CreatePlugin(self: InwOpState5, progid: str) -> int """
        pass

    def DeleteSelectedFiles(self):
        """ DeleteSelectedFiles(self: InwOpState5) """
        pass

    def DriveIOPlugin(self, internal_name, filename, opts):
        """ DriveIOPlugin(self: InwOpState5, internal_name: str, filename: str, opts: InwOaPropertyVec) -> nwEExportStatus """
        pass

    def EndEdit(self):
        """ EndEdit(self: InwOpState5) """
        pass

    def GetAttributeProperties(self, p_attribute):
        """ GetAttributeProperties(self: InwOpState5, p_attribute: InwOaAttribute) -> InwOaPropertyVec """
        pass

    def GetBoundingBox(self):
        """ GetBoundingBox(self: InwOpState5) -> InwLBox3f """
        pass

    def GetEnum(self, sName):
        """ GetEnum(self: InwOpState5, sName: str) -> int """
        pass

    def GetFirstInstanceOfNode(self, node):
        """ GetFirstInstanceOfNode(self: InwOpState5, node: InwOaNode) -> InwOaPath """
        pass

    def GetGUIPropertyNode(self, p_path, b_show_internal):
        """ GetGUIPropertyNode(self: InwOpState5, p_path: InwOaPath, b_show_internal: bool) -> InwGUIPropertyNode """
        pass

    def GetIOPluginOptions(self, internal_name):
        """ GetIOPluginOptions(self: InwOpState5, internal_name: str) -> InwOaPropertyVec """
        pass

    def GetMeasureDiff(self):
        """ GetMeasureDiff(self: InwOpState5) -> InwLVec3f """
        pass

    def GetMeasureEndPos(self):
        """ GetMeasureEndPos(self: InwOpState5) -> InwLPos3f """
        pass

    def GetMeasureFirstPos(self):
        """ GetMeasureFirstPos(self: InwOpState5) -> InwLPos3f """
        pass

    def GetMeasureValue(self):
        """ GetMeasureValue(self: InwOpState5) -> float """
        pass

    def GetOverrideURL(self, p_path, include_model):
        """ GetOverrideURL(self: InwOpState5, p_path: InwOaPath, include_model: object) -> InwURLOverride """
        pass

    def GlobalProperties(self):
        """ GlobalProperties(self: InwOpState5) -> InwGlobalProperties """
        pass

    def HiddenItemsResetAll(self):
        """ HiddenItemsResetAll(self: InwOpState5) """
        pass

    def IsComposite(self, group):
        """ IsComposite(self: InwOpState5, group: InwOaGroup) -> bool """
        pass

    def NdxArray2Node(self, fullpath):
        """ NdxArray2Node(self: InwOpState5, fullpath: object) -> InwOaNode """
        pass

    def NdxArray2SavedView(self, fullpath):
        """ NdxArray2SavedView(self: InwOpState5, fullpath: object) -> InwOpSavedView """
        pass

    def Node2NdxArray(self, pI):
        """ Node2NdxArray(self: InwOpState5, pI: InwOaNode) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpState5, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpState5) """
        pass

    def ObjectFactory(self, eType, ovReserved1, ovReserved2):
        """ ObjectFactory(self: InwOpState5, eType: nwEObjectType, ovReserved1: object, ovReserved2: object) -> object """
        pass

    def OverrideColor(self, selection, color):
        """ OverrideColor(self: InwOpState5, selection: InwOpSelection, color: InwLVec3f) """
        pass

    def OverrideReset(self, selection):
        """ OverrideReset(self: InwOpState5, selection: InwOpSelection) """
        pass

    def OverrideResetAll(self):
        """ OverrideResetAll(self: InwOpState5) """
        pass

    def OverrideTransform(self, selection, transform):
        """ OverrideTransform(self: InwOpState5, selection: InwOpSelection, transform: InwLTransform3f) """
        pass

    def OverrideTransformReset(self, selection):
        """ OverrideTransformReset(self: InwOpState5, selection: InwOpSelection) """
        pass

    def OverrideTransformResetAll(self):
        """ OverrideTransformResetAll(self: InwOpState5) """
        pass

    def OverrideTransparency(self, selection, transparency):
        """ OverrideTransparency(self: InwOpState5, selection: InwOpSelection, transparency: float) """
        pass

    def OverrideURLReset(self, selection):
        """ OverrideURLReset(self: InwOpState5, selection: InwOpSelection) """
        pass

    def OverrideURLResetAll(self):
        """ OverrideURLResetAll(self: InwOpState5) """
        pass

    def Plugins(self):
        """ Plugins(self: InwOpState5) -> InwPluginsColl """
        pass

    def RequiredItemsResetAll(self):
        """ RequiredItemsResetAll(self: InwOpState5) """
        pass

    def SavedView2NdxArray(self, pI):
        """ SavedView2NdxArray(self: InwOpState5, pI: InwOpSavedView) -> object """
        pass

    def SavedViews(self):
        """ SavedViews(self: InwOpState5) -> InwSavedViewsColl """
        pass

    def SceneLights(self):
        """ SceneLights(self: InwOpState5) -> InwLightsColl """
        pass

    def SeekSelection(self, results, cb, ovStartSelection):
        """ SeekSelection(self: InwOpState5, results: InwOpSelection, cb: InwSeekSelection, ovStartSelection: object) """
        pass

    def SelectionSets(self):
        """ SelectionSets(self: InwOpState5) -> InwSelectionSetColl """
        pass

    def SetOverrideURL(self, selection, pI):
        """ SetOverrideURL(self: InwOpState5, selection: InwOpSelection, pI: InwURLOverride) """
        pass

    def SmartTagText(self, path):
        """ SmartTagText(self: InwOpState5, path: InwOaPath) -> str """
        pass

    def StdName(self, Type, user_name):
        """ StdName(self: InwOpState5, Type: nwEStdName, user_name: bool) -> str """
        pass

    def StopMovement(self):
        """ StopMovement(self: InwOpState5) """
        pass

    def ViewAll(self):
        """ ViewAll(self: InwOpState5) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpState5, vIn: object) -> object """
        pass

    def ZoomInCurViewOnBoundingBox(self, box, factor):
        """ ZoomInCurViewOnBoundingBox(self: InwOpState5, box: InwLBox3f, factor: float) """
        pass

    def ZoomInCurViewOnCurSel(self):
        """ ZoomInCurViewOnCurSel(self: InwOpState5) """
        pass

    def ZoomInCurViewOnSel(self, selection):
        """ ZoomInCurViewOnSel(self: InwOpState5, selection: InwOpSelection) """
        pass

    def ZoomInViewOnSel(self, selection, anonview):
        """ ZoomInViewOnSel(self: InwOpState5, selection: InwOpSelection, anonview: InwOpAnonView) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AreaCullThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaCullThreshold(self: InwOpState5) -> float

Set: AreaCullThreshold(self: InwOpState5) = value
"""

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColor(self: InwOpState5) -> InwLVec3f

Set: BackgroundColor(self: InwOpState5) = value
"""

    CurrentAnimation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAnimation(self: InwOpState5) -> InwOpAnimView

Set: CurrentAnimation(self: InwOpState5) = value
"""

    CurrentFindSpec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentFindSpec(self: InwOpState5) -> InwOpFindSpec

Set: CurrentFindSpec(self: InwOpState5) = value
"""

    CurrentPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPartition(self: InwOpState5) -> InwOaPartition

"""

    CurrentPlanView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPlanView(self: InwOpState5) -> InwOpAnonView

Set: CurrentPlanView(self: InwOpState5) = value
"""

    CurrentSectionView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSectionView(self: InwOpState5) -> InwOpAnonView

Set: CurrentSectionView(self: InwOpState5) = value
"""

    CurrentSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSelection(self: InwOpState5) -> InwOpSelection

Set: CurrentSelection(self: InwOpState5) = value
"""

    CurrentView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentView(self: InwOpState5) -> InwOpAnonView

Set: CurrentView(self: InwOpState5) = value
"""

    EventsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventsEnabled(self: InwOpState5) -> bool

Set: EventsEnabled(self: InwOpState5) = value
"""

    FrameRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameRate(self: InwOpState5) -> int

Set: FrameRate(self: InwOpState5) = value
"""

    GlobalAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalAmbient(self: InwOpState5) -> InwLVec3f

Set: GlobalAmbient(self: InwOpState5) = value
"""

    HeadlightAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightAmbient(self: InwOpState5) -> float

Set: HeadlightAmbient(self: InwOpState5) = value
"""

    HeadlightIntensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightIntensity(self: InwOpState5) -> float

Set: HeadlightIntensity(self: InwOpState5) = value
"""

    MaxNearDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxNearDistance(self: InwOpState5) -> float

Set: MaxNearDistance(self: InwOpState5) = value
"""

    MinFarDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinFarDistance(self: InwOpState5) -> float

Set: MinFarDistance(self: InwOpState5) = value
"""

    NumTriangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumTriangles(self: InwOpState5) -> int

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpState5) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpState5) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpState5) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpState5) -> int

Set: nwLock(self: InwOpState5) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpState5) -> bool

Set: nwOwn(self: InwOpState5) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpState5) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpState5) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpState5) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpState5) -> str

"""

    SmartTagsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmartTagsEnabled(self: InwOpState5) -> bool

Set: SmartTagsEnabled(self: InwOpState5) = value
"""

    TwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TwoSided(self: InwOpState5) -> bool

Set: TwoSided(self: InwOpState5) = value
"""

    URLsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsEnabled(self: InwOpState5) -> bool

Set: URLsEnabled(self: InwOpState5) = value
"""



class InwOpState6(InwOpState5, InwOpState4, InwOpState3, InwOpState2, InwOpState, InwBase):
    # no doc
    def ApplyView(self, view):
        """ ApplyView(self: InwOpState6, view: InwOpView) """
        pass

    def BeginEdit(self, name):
        """ BeginEdit(self: InwOpState6, name: str) """
        pass

    def CheckLicense(self, name):
        """ CheckLicense(self: InwOpState6, name: str) -> bool """
        pass

    def Copy(self):
        """ Copy(self: InwOpState6) -> object """
        pass

    def CreatePicture(self, anonview, ovNumPasses, vWidth, ovHeight):
        """ CreatePicture(self: InwOpState6, anonview: InwOpAnonView, ovNumPasses: object, vWidth: object, ovHeight: object) -> object """
        pass

    def CreatePlugin(self, progid):
        """ CreatePlugin(self: InwOpState6, progid: str) -> int """
        pass

    def DeleteSelectedFiles(self):
        """ DeleteSelectedFiles(self: InwOpState6) """
        pass

    def DriveIOPlugin(self, internal_name, filename, opts):
        """ DriveIOPlugin(self: InwOpState6, internal_name: str, filename: str, opts: InwOaPropertyVec) -> nwEExportStatus """
        pass

    def EndEdit(self):
        """ EndEdit(self: InwOpState6) """
        pass

    def EndInteractive(self):
        """ EndInteractive(self: InwOpState6) """
        pass

    def GetAttributeProperties(self, p_attribute):
        """ GetAttributeProperties(self: InwOpState6, p_attribute: InwOaAttribute) -> InwOaPropertyVec """
        pass

    def GetBoundingBox(self):
        """ GetBoundingBox(self: InwOpState6) -> InwLBox3f """
        pass

    def GetCurrentFilename(self):
        """ GetCurrentFilename(self: InwOpState6) -> str """
        pass

    def GetEnum(self, sName):
        """ GetEnum(self: InwOpState6, sName: str) -> int """
        pass

    def GetFirstInstanceOfNode(self, node):
        """ GetFirstInstanceOfNode(self: InwOpState6, node: InwOaNode) -> InwOaPath """
        pass

    def GetGUIPropertyNode(self, p_path, b_show_internal):
        """ GetGUIPropertyNode(self: InwOpState6, p_path: InwOaPath, b_show_internal: bool) -> InwGUIPropertyNode """
        pass

    def GetIOPluginOptions(self, internal_name):
        """ GetIOPluginOptions(self: InwOpState6, internal_name: str) -> InwOaPropertyVec """
        pass

    def GetMeasureDiff(self):
        """ GetMeasureDiff(self: InwOpState6) -> InwLVec3f """
        pass

    def GetMeasureEndPos(self):
        """ GetMeasureEndPos(self: InwOpState6) -> InwLPos3f """
        pass

    def GetMeasureFirstPos(self):
        """ GetMeasureFirstPos(self: InwOpState6) -> InwLPos3f """
        pass

    def GetMeasureValue(self):
        """ GetMeasureValue(self: InwOpState6) -> float """
        pass

    def GetOverrideURL(self, p_path, include_model):
        """ GetOverrideURL(self: InwOpState6, p_path: InwOaPath, include_model: object) -> InwURLOverride """
        pass

    def GlobalProperties(self):
        """ GlobalProperties(self: InwOpState6) -> InwGlobalProperties """
        pass

    def HiddenItemsResetAll(self):
        """ HiddenItemsResetAll(self: InwOpState6) """
        pass

    def IsComposite(self, group):
        """ IsComposite(self: InwOpState6, group: InwOaGroup) -> bool """
        pass

    def NdxArray2Node(self, fullpath):
        """ NdxArray2Node(self: InwOpState6, fullpath: object) -> InwOaNode """
        pass

    def NdxArray2SavedView(self, fullpath):
        """ NdxArray2SavedView(self: InwOpState6, fullpath: object) -> InwOpSavedView """
        pass

    def Node2NdxArray(self, pI):
        """ Node2NdxArray(self: InwOpState6, pI: InwOaNode) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpState6, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpState6) """
        pass

    def ObjectFactory(self, eType, ovReserved1, ovReserved2):
        """ ObjectFactory(self: InwOpState6, eType: nwEObjectType, ovReserved1: object, ovReserved2: object) -> object """
        pass

    def OverrideColor(self, selection, color):
        """ OverrideColor(self: InwOpState6, selection: InwOpSelection, color: InwLVec3f) """
        pass

    def OverrideReset(self, selection):
        """ OverrideReset(self: InwOpState6, selection: InwOpSelection) """
        pass

    def OverrideResetAll(self):
        """ OverrideResetAll(self: InwOpState6) """
        pass

    def OverrideTransform(self, selection, transform):
        """ OverrideTransform(self: InwOpState6, selection: InwOpSelection, transform: InwLTransform3f) """
        pass

    def OverrideTransformReset(self, selection):
        """ OverrideTransformReset(self: InwOpState6, selection: InwOpSelection) """
        pass

    def OverrideTransformResetAll(self):
        """ OverrideTransformResetAll(self: InwOpState6) """
        pass

    def OverrideTransparency(self, selection, transparency):
        """ OverrideTransparency(self: InwOpState6, selection: InwOpSelection, transparency: float) """
        pass

    def OverrideURLReset(self, selection):
        """ OverrideURLReset(self: InwOpState6, selection: InwOpSelection) """
        pass

    def OverrideURLResetAll(self):
        """ OverrideURLResetAll(self: InwOpState6) """
        pass

    def Plugins(self):
        """ Plugins(self: InwOpState6) -> InwPluginsColl """
        pass

    def RequiredItemsResetAll(self):
        """ RequiredItemsResetAll(self: InwOpState6) """
        pass

    def SavedView2NdxArray(self, pI):
        """ SavedView2NdxArray(self: InwOpState6, pI: InwOpSavedView) -> object """
        pass

    def SavedViews(self):
        """ SavedViews(self: InwOpState6) -> InwSavedViewsColl """
        pass

    def SceneLights(self):
        """ SceneLights(self: InwOpState6) -> InwLightsColl """
        pass

    def SeekSelection(self, results, cb, ovStartSelection):
        """ SeekSelection(self: InwOpState6, results: InwOpSelection, cb: InwSeekSelection, ovStartSelection: object) """
        pass

    def SelectionSets(self):
        """ SelectionSets(self: InwOpState6) -> InwSelectionSetColl """
        pass

    def SetOverrideURL(self, selection, pI):
        """ SetOverrideURL(self: InwOpState6, selection: InwOpSelection, pI: InwURLOverride) """
        pass

    def SmartTagText(self, path):
        """ SmartTagText(self: InwOpState6, path: InwOaPath) -> str """
        pass

    def StartInteractive(self):
        """ StartInteractive(self: InwOpState6) """
        pass

    def StdName(self, Type, user_name):
        """ StdName(self: InwOpState6, Type: nwEStdName, user_name: bool) -> str """
        pass

    def StopMovement(self):
        """ StopMovement(self: InwOpState6) """
        pass

    def ViewAll(self):
        """ ViewAll(self: InwOpState6) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpState6, vIn: object) -> object """
        pass

    def ZoomInCurViewOnBoundingBox(self, box, factor):
        """ ZoomInCurViewOnBoundingBox(self: InwOpState6, box: InwLBox3f, factor: float) """
        pass

    def ZoomInCurViewOnCurSel(self):
        """ ZoomInCurViewOnCurSel(self: InwOpState6) """
        pass

    def ZoomInCurViewOnSel(self, selection):
        """ ZoomInCurViewOnSel(self: InwOpState6, selection: InwOpSelection) """
        pass

    def ZoomInViewOnSel(self, selection, anonview):
        """ ZoomInViewOnSel(self: InwOpState6, selection: InwOpSelection, anonview: InwOpAnonView) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AreaCullThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaCullThreshold(self: InwOpState6) -> float

Set: AreaCullThreshold(self: InwOpState6) = value
"""

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColor(self: InwOpState6) -> InwLVec3f

Set: BackgroundColor(self: InwOpState6) = value
"""

    CurrentAnimation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAnimation(self: InwOpState6) -> InwOpAnimView

Set: CurrentAnimation(self: InwOpState6) = value
"""

    CurrentFindSpec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentFindSpec(self: InwOpState6) -> InwOpFindSpec

Set: CurrentFindSpec(self: InwOpState6) = value
"""

    CurrentPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPartition(self: InwOpState6) -> InwOaPartition

"""

    CurrentPlanView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPlanView(self: InwOpState6) -> InwOpAnonView

Set: CurrentPlanView(self: InwOpState6) = value
"""

    CurrentSectionView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSectionView(self: InwOpState6) -> InwOpAnonView

Set: CurrentSectionView(self: InwOpState6) = value
"""

    CurrentSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSelection(self: InwOpState6) -> InwOpSelection

Set: CurrentSelection(self: InwOpState6) = value
"""

    CurrentView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentView(self: InwOpState6) -> InwOpAnonView

Set: CurrentView(self: InwOpState6) = value
"""

    EventsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventsEnabled(self: InwOpState6) -> bool

Set: EventsEnabled(self: InwOpState6) = value
"""

    FrameRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameRate(self: InwOpState6) -> int

Set: FrameRate(self: InwOpState6) = value
"""

    GlobalAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalAmbient(self: InwOpState6) -> InwLVec3f

Set: GlobalAmbient(self: InwOpState6) = value
"""

    HeadlightAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightAmbient(self: InwOpState6) -> float

Set: HeadlightAmbient(self: InwOpState6) = value
"""

    HeadlightIntensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightIntensity(self: InwOpState6) -> float

Set: HeadlightIntensity(self: InwOpState6) = value
"""

    MaxNearDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxNearDistance(self: InwOpState6) -> float

Set: MaxNearDistance(self: InwOpState6) = value
"""

    MinFarDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinFarDistance(self: InwOpState6) -> float

Set: MinFarDistance(self: InwOpState6) = value
"""

    NumTriangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumTriangles(self: InwOpState6) -> int

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpState6) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpState6) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpState6) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpState6) -> int

Set: nwLock(self: InwOpState6) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpState6) -> bool

Set: nwOwn(self: InwOpState6) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpState6) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpState6) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpState6) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpState6) -> str

"""

    SmartTagsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmartTagsEnabled(self: InwOpState6) -> bool

Set: SmartTagsEnabled(self: InwOpState6) = value
"""

    TwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TwoSided(self: InwOpState6) -> bool

Set: TwoSided(self: InwOpState6) = value
"""

    URLsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsEnabled(self: InwOpState6) -> bool

Set: URLsEnabled(self: InwOpState6) = value
"""



class InwOpState7(InwOpState6, InwOpState5, InwOpState4, InwOpState3, InwOpState2, InwOpState, InwBase):
    # no doc
    def ApplyView(self, view):
        """ ApplyView(self: InwOpState7, view: InwOpView) """
        pass

    def BeginEdit(self, name):
        """ BeginEdit(self: InwOpState7, name: str) """
        pass

    def CheckLicense(self, name):
        """ CheckLicense(self: InwOpState7, name: str) -> bool """
        pass

    def Copy(self):
        """ Copy(self: InwOpState7) -> object """
        pass

    def CreatePicture(self, anonview, ovNumPasses, vWidth, ovHeight):
        """ CreatePicture(self: InwOpState7, anonview: InwOpAnonView, ovNumPasses: object, vWidth: object, ovHeight: object) -> object """
        pass

    def CreatePlugin(self, progid):
        """ CreatePlugin(self: InwOpState7, progid: str) -> int """
        pass

    def DeleteSelectedFiles(self):
        """ DeleteSelectedFiles(self: InwOpState7) """
        pass

    def DriveIOPlugin(self, internal_name, filename, opts):
        """ DriveIOPlugin(self: InwOpState7, internal_name: str, filename: str, opts: InwOaPropertyVec) -> nwEExportStatus """
        pass

    def EndEdit(self):
        """ EndEdit(self: InwOpState7) """
        pass

    def EndInteractive(self):
        """ EndInteractive(self: InwOpState7) """
        pass

    def GetAttributeProperties(self, p_attribute):
        """ GetAttributeProperties(self: InwOpState7, p_attribute: InwOaAttribute) -> InwOaPropertyVec """
        pass

    def GetBoundingBox(self):
        """ GetBoundingBox(self: InwOpState7) -> InwLBox3f """
        pass

    def GetCurrentFilename(self):
        """ GetCurrentFilename(self: InwOpState7) -> str """
        pass

    def GetEnum(self, sName):
        """ GetEnum(self: InwOpState7, sName: str) -> int """
        pass

    def GetFirstInstanceOfNode(self, node):
        """ GetFirstInstanceOfNode(self: InwOpState7, node: InwOaNode) -> InwOaPath """
        pass

    def GetGUIPropertyNode(self, p_path, b_show_internal):
        """ GetGUIPropertyNode(self: InwOpState7, p_path: InwOaPath, b_show_internal: bool) -> InwGUIPropertyNode """
        pass

    def GetIOPluginOptions(self, internal_name):
        """ GetIOPluginOptions(self: InwOpState7, internal_name: str) -> InwOaPropertyVec """
        pass

    def GetMeasureDiff(self):
        """ GetMeasureDiff(self: InwOpState7) -> InwLVec3f """
        pass

    def GetMeasureEndPos(self):
        """ GetMeasureEndPos(self: InwOpState7) -> InwLPos3f """
        pass

    def GetMeasureFirstPos(self):
        """ GetMeasureFirstPos(self: InwOpState7) -> InwLPos3f """
        pass

    def GetMeasureValue(self):
        """ GetMeasureValue(self: InwOpState7) -> float """
        pass

    def GetOverrideURL(self, p_path, include_model):
        """ GetOverrideURL(self: InwOpState7, p_path: InwOaPath, include_model: object) -> InwURLOverride """
        pass

    def GlobalProperties(self):
        """ GlobalProperties(self: InwOpState7) -> InwGlobalProperties """
        pass

    def HiddenItemsResetAll(self):
        """ HiddenItemsResetAll(self: InwOpState7) """
        pass

    def IsComposite(self, group):
        """ IsComposite(self: InwOpState7, group: InwOaGroup) -> bool """
        pass

    def LoadedFileFromNdx(self, ndx):
        """ LoadedFileFromNdx(self: InwOpState7, ndx: int) -> InwOaPartition """
        pass

    def LoadedFileFromPath(self, path):
        """ LoadedFileFromPath(self: InwOpState7, path: InwOaPath) -> InwOaPartition """
        pass

    def NdxArray2Node(self, fullpath):
        """ NdxArray2Node(self: InwOpState7, fullpath: object) -> InwOaNode """
        pass

    def NdxArray2SavedView(self, fullpath):
        """ NdxArray2SavedView(self: InwOpState7, fullpath: object) -> InwOpSavedView """
        pass

    def Node2NdxArray(self, pI):
        """ Node2NdxArray(self: InwOpState7, pI: InwOaNode) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpState7, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpState7) """
        pass

    def ObjectFactory(self, eType, ovReserved1, ovReserved2):
        """ ObjectFactory(self: InwOpState7, eType: nwEObjectType, ovReserved1: object, ovReserved2: object) -> object """
        pass

    def OverrideColor(self, selection, color):
        """ OverrideColor(self: InwOpState7, selection: InwOpSelection, color: InwLVec3f) """
        pass

    def OverrideReset(self, selection):
        """ OverrideReset(self: InwOpState7, selection: InwOpSelection) """
        pass

    def OverrideResetAll(self):
        """ OverrideResetAll(self: InwOpState7) """
        pass

    def OverrideTransform(self, selection, transform):
        """ OverrideTransform(self: InwOpState7, selection: InwOpSelection, transform: InwLTransform3f) """
        pass

    def OverrideTransformReset(self, selection):
        """ OverrideTransformReset(self: InwOpState7, selection: InwOpSelection) """
        pass

    def OverrideTransformResetAll(self):
        """ OverrideTransformResetAll(self: InwOpState7) """
        pass

    def OverrideTransparency(self, selection, transparency):
        """ OverrideTransparency(self: InwOpState7, selection: InwOpSelection, transparency: float) """
        pass

    def OverrideURLReset(self, selection):
        """ OverrideURLReset(self: InwOpState7, selection: InwOpSelection) """
        pass

    def OverrideURLResetAll(self):
        """ OverrideURLResetAll(self: InwOpState7) """
        pass

    def Plugins(self):
        """ Plugins(self: InwOpState7) -> InwPluginsColl """
        pass

    def RequiredItemsResetAll(self):
        """ RequiredItemsResetAll(self: InwOpState7) """
        pass

    def SavedView2NdxArray(self, pI):
        """ SavedView2NdxArray(self: InwOpState7, pI: InwOpSavedView) -> object """
        pass

    def SavedViews(self):
        """ SavedViews(self: InwOpState7) -> InwSavedViewsColl """
        pass

    def SceneLights(self):
        """ SceneLights(self: InwOpState7) -> InwLightsColl """
        pass

    def SeekSelection(self, results, cb, ovStartSelection):
        """ SeekSelection(self: InwOpState7, results: InwOpSelection, cb: InwSeekSelection, ovStartSelection: object) """
        pass

    def SelectionSets(self):
        """ SelectionSets(self: InwOpState7) -> InwSelectionSetColl """
        pass

    def SetOverrideURL(self, selection, pI):
        """ SetOverrideURL(self: InwOpState7, selection: InwOpSelection, pI: InwURLOverride) """
        pass

    def SmartTagText(self, path):
        """ SmartTagText(self: InwOpState7, path: InwOaPath) -> str """
        pass

    def StartInteractive(self):
        """ StartInteractive(self: InwOpState7) """
        pass

    def StdName(self, Type, user_name):
        """ StdName(self: InwOpState7, Type: nwEStdName, user_name: bool) -> str """
        pass

    def StopMovement(self):
        """ StopMovement(self: InwOpState7) """
        pass

    def ViewAll(self):
        """ ViewAll(self: InwOpState7) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpState7, vIn: object) -> object """
        pass

    def ZoomInCurViewOnBoundingBox(self, box, factor):
        """ ZoomInCurViewOnBoundingBox(self: InwOpState7, box: InwLBox3f, factor: float) """
        pass

    def ZoomInCurViewOnCurSel(self):
        """ ZoomInCurViewOnCurSel(self: InwOpState7) """
        pass

    def ZoomInCurViewOnSel(self, selection):
        """ ZoomInCurViewOnSel(self: InwOpState7, selection: InwOpSelection) """
        pass

    def ZoomInViewOnSel(self, selection, anonview):
        """ ZoomInViewOnSel(self: InwOpState7, selection: InwOpSelection, anonview: InwOpAnonView) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AreaCullThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaCullThreshold(self: InwOpState7) -> float

Set: AreaCullThreshold(self: InwOpState7) = value
"""

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColor(self: InwOpState7) -> InwLVec3f

Set: BackgroundColor(self: InwOpState7) = value
"""

    CurrentAnimation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAnimation(self: InwOpState7) -> InwOpAnimView

Set: CurrentAnimation(self: InwOpState7) = value
"""

    CurrentFindSpec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentFindSpec(self: InwOpState7) -> InwOpFindSpec

Set: CurrentFindSpec(self: InwOpState7) = value
"""

    CurrentPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPartition(self: InwOpState7) -> InwOaPartition

"""

    CurrentPlanView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPlanView(self: InwOpState7) -> InwOpAnonView

Set: CurrentPlanView(self: InwOpState7) = value
"""

    CurrentSectionView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSectionView(self: InwOpState7) -> InwOpAnonView

Set: CurrentSectionView(self: InwOpState7) = value
"""

    CurrentSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSelection(self: InwOpState7) -> InwOpSelection

Set: CurrentSelection(self: InwOpState7) = value
"""

    CurrentView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentView(self: InwOpState7) -> InwOpAnonView

Set: CurrentView(self: InwOpState7) = value
"""

    EventsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventsEnabled(self: InwOpState7) -> bool

Set: EventsEnabled(self: InwOpState7) = value
"""

    FrameRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameRate(self: InwOpState7) -> int

Set: FrameRate(self: InwOpState7) = value
"""

    GlobalAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalAmbient(self: InwOpState7) -> InwLVec3f

Set: GlobalAmbient(self: InwOpState7) = value
"""

    HeadlightAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightAmbient(self: InwOpState7) -> float

Set: HeadlightAmbient(self: InwOpState7) = value
"""

    HeadlightIntensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightIntensity(self: InwOpState7) -> float

Set: HeadlightIntensity(self: InwOpState7) = value
"""

    LoadedFileCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadedFileCount(self: InwOpState7) -> int

"""

    MaxNearDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxNearDistance(self: InwOpState7) -> float

Set: MaxNearDistance(self: InwOpState7) = value
"""

    MinFarDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinFarDistance(self: InwOpState7) -> float

Set: MinFarDistance(self: InwOpState7) = value
"""

    NumTriangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumTriangles(self: InwOpState7) -> int

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpState7) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpState7) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpState7) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpState7) -> int

Set: nwLock(self: InwOpState7) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpState7) -> bool

Set: nwOwn(self: InwOpState7) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpState7) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpState7) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpState7) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpState7) -> str

"""

    SmartTagsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmartTagsEnabled(self: InwOpState7) -> bool

Set: SmartTagsEnabled(self: InwOpState7) = value
"""

    TwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TwoSided(self: InwOpState7) -> bool

Set: TwoSided(self: InwOpState7) = value
"""

    URLsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsEnabled(self: InwOpState7) -> bool

Set: URLsEnabled(self: InwOpState7) = value
"""



class InwOpState8(InwOpState7, InwOpState6, InwOpState5, InwOpState4, InwOpState3, InwOpState2, InwOpState, InwBase):
    # no doc
    def ApplyView(self, view):
        """ ApplyView(self: InwOpState8, view: InwOpView) """
        pass

    def BeginEdit(self, name):
        """ BeginEdit(self: InwOpState8, name: str) """
        pass

    def CheckLicense(self, name):
        """ CheckLicense(self: InwOpState8, name: str) -> bool """
        pass

    def Copy(self):
        """ Copy(self: InwOpState8) -> object """
        pass

    def CreatePicture(self, anonview, ovNumPasses, vWidth, ovHeight):
        """ CreatePicture(self: InwOpState8, anonview: InwOpAnonView, ovNumPasses: object, vWidth: object, ovHeight: object) -> object """
        pass

    def CreatePlugin(self, progid):
        """ CreatePlugin(self: InwOpState8, progid: str) -> int """
        pass

    def DeleteSelectedFiles(self):
        """ DeleteSelectedFiles(self: InwOpState8) """
        pass

    def DriveIOPlugin(self, internal_name, filename, opts):
        """ DriveIOPlugin(self: InwOpState8, internal_name: str, filename: str, opts: InwOaPropertyVec) -> nwEExportStatus """
        pass

    def EndEdit(self):
        """ EndEdit(self: InwOpState8) """
        pass

    def EndInteractive(self):
        """ EndInteractive(self: InwOpState8) """
        pass

    def FileVersion(self, filename):
        """ FileVersion(self: InwOpState8, filename: str) -> int """
        pass

    def GetAttributeProperties(self, p_attribute):
        """ GetAttributeProperties(self: InwOpState8, p_attribute: InwOaAttribute) -> InwOaPropertyVec """
        pass

    def GetBoundingBox(self):
        """ GetBoundingBox(self: InwOpState8) -> InwLBox3f """
        pass

    def GetCurrentFilename(self):
        """ GetCurrentFilename(self: InwOpState8) -> str """
        pass

    def GetEnum(self, sName):
        """ GetEnum(self: InwOpState8, sName: str) -> int """
        pass

    def GetFirstInstanceOfNode(self, node):
        """ GetFirstInstanceOfNode(self: InwOpState8, node: InwOaNode) -> InwOaPath """
        pass

    def GetGUIPropertyNode(self, p_path, b_show_internal):
        """ GetGUIPropertyNode(self: InwOpState8, p_path: InwOaPath, b_show_internal: bool) -> InwGUIPropertyNode """
        pass

    def GetIOPluginOptions(self, internal_name):
        """ GetIOPluginOptions(self: InwOpState8, internal_name: str) -> InwOaPropertyVec """
        pass

    def GetMeasureDiff(self):
        """ GetMeasureDiff(self: InwOpState8) -> InwLVec3f """
        pass

    def GetMeasureEndPos(self):
        """ GetMeasureEndPos(self: InwOpState8) -> InwLPos3f """
        pass

    def GetMeasureFirstPos(self):
        """ GetMeasureFirstPos(self: InwOpState8) -> InwLPos3f """
        pass

    def GetMeasureValue(self):
        """ GetMeasureValue(self: InwOpState8) -> float """
        pass

    def GetOverrideURL(self, p_path, include_model):
        """ GetOverrideURL(self: InwOpState8, p_path: InwOaPath, include_model: object) -> InwURLOverride """
        pass

    def GlobalProperties(self):
        """ GlobalProperties(self: InwOpState8) -> InwGlobalProperties """
        pass

    def HiddenItemsResetAll(self):
        """ HiddenItemsResetAll(self: InwOpState8) """
        pass

    def IsComposite(self, group):
        """ IsComposite(self: InwOpState8, group: InwOaGroup) -> bool """
        pass

    def LoadedFileFromNdx(self, ndx):
        """ LoadedFileFromNdx(self: InwOpState8, ndx: int) -> InwOaPartition """
        pass

    def LoadedFileFromPath(self, path):
        """ LoadedFileFromPath(self: InwOpState8, path: InwOaPath) -> InwOaPartition """
        pass

    def NdxArray2Node(self, fullpath):
        """ NdxArray2Node(self: InwOpState8, fullpath: object) -> InwOaNode """
        pass

    def NdxArray2SavedView(self, fullpath):
        """ NdxArray2SavedView(self: InwOpState8, fullpath: object) -> InwOpSavedView """
        pass

    def Node2NdxArray(self, pI):
        """ Node2NdxArray(self: InwOpState8, pI: InwOaNode) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpState8, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpState8) """
        pass

    def ObjectFactory(self, eType, ovReserved1, ovReserved2):
        """ ObjectFactory(self: InwOpState8, eType: nwEObjectType, ovReserved1: object, ovReserved2: object) -> object """
        pass

    def OverrideColor(self, selection, color):
        """ OverrideColor(self: InwOpState8, selection: InwOpSelection, color: InwLVec3f) """
        pass

    def OverrideReset(self, selection):
        """ OverrideReset(self: InwOpState8, selection: InwOpSelection) """
        pass

    def OverrideResetAll(self):
        """ OverrideResetAll(self: InwOpState8) """
        pass

    def OverrideTransform(self, selection, transform):
        """ OverrideTransform(self: InwOpState8, selection: InwOpSelection, transform: InwLTransform3f) """
        pass

    def OverrideTransformReset(self, selection):
        """ OverrideTransformReset(self: InwOpState8, selection: InwOpSelection) """
        pass

    def OverrideTransformResetAll(self):
        """ OverrideTransformResetAll(self: InwOpState8) """
        pass

    def OverrideTransparency(self, selection, transparency):
        """ OverrideTransparency(self: InwOpState8, selection: InwOpSelection, transparency: float) """
        pass

    def OverrideURLReset(self, selection):
        """ OverrideURLReset(self: InwOpState8, selection: InwOpSelection) """
        pass

    def OverrideURLResetAll(self):
        """ OverrideURLResetAll(self: InwOpState8) """
        pass

    def Plugins(self):
        """ Plugins(self: InwOpState8) -> InwPluginsColl """
        pass

    def RequiredItemsResetAll(self):
        """ RequiredItemsResetAll(self: InwOpState8) """
        pass

    def SavedView2NdxArray(self, pI):
        """ SavedView2NdxArray(self: InwOpState8, pI: InwOpSavedView) -> object """
        pass

    def SavedViews(self):
        """ SavedViews(self: InwOpState8) -> InwSavedViewsColl """
        pass

    def SceneLights(self):
        """ SceneLights(self: InwOpState8) -> InwLightsColl """
        pass

    def SeekSelection(self, results, cb, ovStartSelection):
        """ SeekSelection(self: InwOpState8, results: InwOpSelection, cb: InwSeekSelection, ovStartSelection: object) """
        pass

    def SelectionSets(self):
        """ SelectionSets(self: InwOpState8) -> InwSelectionSetColl """
        pass

    def SelectionSetsEx(self):
        """ SelectionSetsEx(self: InwOpState8) -> InwSelectionSetExColl """
        pass

    def SetOverrideURL(self, selection, pI):
        """ SetOverrideURL(self: InwOpState8, selection: InwOpSelection, pI: InwURLOverride) """
        pass

    def SmartTagText(self, path):
        """ SmartTagText(self: InwOpState8, path: InwOaPath) -> str """
        pass

    def StartInteractive(self):
        """ StartInteractive(self: InwOpState8) """
        pass

    def StdName(self, Type, user_name):
        """ StdName(self: InwOpState8, Type: nwEStdName, user_name: bool) -> str """
        pass

    def StopMovement(self):
        """ StopMovement(self: InwOpState8) """
        pass

    def ViewAll(self):
        """ ViewAll(self: InwOpState8) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpState8, vIn: object) -> object """
        pass

    def ZoomInCurViewOnBoundingBox(self, box, factor):
        """ ZoomInCurViewOnBoundingBox(self: InwOpState8, box: InwLBox3f, factor: float) """
        pass

    def ZoomInCurViewOnCurSel(self):
        """ ZoomInCurViewOnCurSel(self: InwOpState8) """
        pass

    def ZoomInCurViewOnSel(self, selection):
        """ ZoomInCurViewOnSel(self: InwOpState8, selection: InwOpSelection) """
        pass

    def ZoomInViewOnSel(self, selection, anonview):
        """ ZoomInViewOnSel(self: InwOpState8, selection: InwOpSelection, anonview: InwOpAnonView) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AreaCullThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaCullThreshold(self: InwOpState8) -> float

Set: AreaCullThreshold(self: InwOpState8) = value
"""

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColor(self: InwOpState8) -> InwLVec3f

Set: BackgroundColor(self: InwOpState8) = value
"""

    CurrentAnimation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAnimation(self: InwOpState8) -> InwOpAnimView

Set: CurrentAnimation(self: InwOpState8) = value
"""

    CurrentFindSpec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentFindSpec(self: InwOpState8) -> InwOpFindSpec

Set: CurrentFindSpec(self: InwOpState8) = value
"""

    CurrentPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPartition(self: InwOpState8) -> InwOaPartition

"""

    CurrentPlanView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPlanView(self: InwOpState8) -> InwOpAnonView

Set: CurrentPlanView(self: InwOpState8) = value
"""

    CurrentSectionView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSectionView(self: InwOpState8) -> InwOpAnonView

Set: CurrentSectionView(self: InwOpState8) = value
"""

    CurrentSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSelection(self: InwOpState8) -> InwOpSelection

Set: CurrentSelection(self: InwOpState8) = value
"""

    CurrentView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentView(self: InwOpState8) -> InwOpAnonView

Set: CurrentView(self: InwOpState8) = value
"""

    EventsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventsEnabled(self: InwOpState8) -> bool

Set: EventsEnabled(self: InwOpState8) = value
"""

    FrameRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameRate(self: InwOpState8) -> int

Set: FrameRate(self: InwOpState8) = value
"""

    GlobalAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalAmbient(self: InwOpState8) -> InwLVec3f

Set: GlobalAmbient(self: InwOpState8) = value
"""

    HeadlightAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightAmbient(self: InwOpState8) -> float

Set: HeadlightAmbient(self: InwOpState8) = value
"""

    HeadlightIntensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightIntensity(self: InwOpState8) -> float

Set: HeadlightIntensity(self: InwOpState8) = value
"""

    LoadedFileCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadedFileCount(self: InwOpState8) -> int

"""

    MaxNearDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxNearDistance(self: InwOpState8) -> float

Set: MaxNearDistance(self: InwOpState8) = value
"""

    MinFarDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinFarDistance(self: InwOpState8) -> float

Set: MinFarDistance(self: InwOpState8) = value
"""

    NumTriangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumTriangles(self: InwOpState8) -> int

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpState8) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpState8) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpState8) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpState8) -> int

Set: nwLock(self: InwOpState8) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpState8) -> bool

Set: nwOwn(self: InwOpState8) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpState8) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpState8) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpState8) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpState8) -> str

"""

    SmartTagsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmartTagsEnabled(self: InwOpState8) -> bool

Set: SmartTagsEnabled(self: InwOpState8) = value
"""

    TwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TwoSided(self: InwOpState8) -> bool

Set: TwoSided(self: InwOpState8) = value
"""

    URLsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsEnabled(self: InwOpState8) -> bool

Set: URLsEnabled(self: InwOpState8) = value
"""



class InwOpState9(InwOpState8, InwOpState7, InwOpState6, InwOpState5, InwOpState4, InwOpState3, InwOpState2, InwOpState, InwBase):
    # no doc
    def ApplyView(self, view):
        """ ApplyView(self: InwOpState9, view: InwOpView) """
        pass

    def BeginEdit(self, name):
        """ BeginEdit(self: InwOpState9, name: str) """
        pass

    def CheckLicense(self, name):
        """ CheckLicense(self: InwOpState9, name: str) -> bool """
        pass

    def Copy(self):
        """ Copy(self: InwOpState9) -> object """
        pass

    def CreatePicture(self, anonview, ovNumPasses, vWidth, ovHeight):
        """ CreatePicture(self: InwOpState9, anonview: InwOpAnonView, ovNumPasses: object, vWidth: object, ovHeight: object) -> object """
        pass

    def CreatePlugin(self, progid):
        """ CreatePlugin(self: InwOpState9, progid: str) -> int """
        pass

    def DeleteSelectedFiles(self):
        """ DeleteSelectedFiles(self: InwOpState9) """
        pass

    def DriveIOPlugin(self, internal_name, filename, opts):
        """ DriveIOPlugin(self: InwOpState9, internal_name: str, filename: str, opts: InwOaPropertyVec) -> nwEExportStatus """
        pass

    def EndEdit(self):
        """ EndEdit(self: InwOpState9) """
        pass

    def EndInteractive(self):
        """ EndInteractive(self: InwOpState9) """
        pass

    def FileVersion(self, filename):
        """ FileVersion(self: InwOpState9, filename: str) -> int """
        pass

    def GetAttributeProperties(self, p_attribute):
        """ GetAttributeProperties(self: InwOpState9, p_attribute: InwOaAttribute) -> InwOaPropertyVec """
        pass

    def GetBoundingBox(self):
        """ GetBoundingBox(self: InwOpState9) -> InwLBox3f """
        pass

    def GetCurrentFilename(self):
        """ GetCurrentFilename(self: InwOpState9) -> str """
        pass

    def GetEnum(self, sName):
        """ GetEnum(self: InwOpState9, sName: str) -> int """
        pass

    def GetFirstInstanceOfNode(self, node):
        """ GetFirstInstanceOfNode(self: InwOpState9, node: InwOaNode) -> InwOaPath """
        pass

    def GetGUIPropertyNode(self, p_path, b_show_internal):
        """ GetGUIPropertyNode(self: InwOpState9, p_path: InwOaPath, b_show_internal: bool) -> InwGUIPropertyNode """
        pass

    def GetIOPluginOptions(self, internal_name):
        """ GetIOPluginOptions(self: InwOpState9, internal_name: str) -> InwOaPropertyVec """
        pass

    def GetMeasureDiff(self):
        """ GetMeasureDiff(self: InwOpState9) -> InwLVec3f """
        pass

    def GetMeasureEndPos(self):
        """ GetMeasureEndPos(self: InwOpState9) -> InwLPos3f """
        pass

    def GetMeasureFirstPos(self):
        """ GetMeasureFirstPos(self: InwOpState9) -> InwLPos3f """
        pass

    def GetMeasureValue(self):
        """ GetMeasureValue(self: InwOpState9) -> float """
        pass

    def GetOverrideURL(self, p_path, include_model):
        """ GetOverrideURL(self: InwOpState9, p_path: InwOaPath, include_model: object) -> InwURLOverride """
        pass

    def GetProductInfo(self):
        """ GetProductInfo(self: InwOpState9) -> str """
        pass

    def GlobalProperties(self):
        """ GlobalProperties(self: InwOpState9) -> InwGlobalProperties """
        pass

    def HiddenItemsResetAll(self):
        """ HiddenItemsResetAll(self: InwOpState9) """
        pass

    def IsComposite(self, group):
        """ IsComposite(self: InwOpState9, group: InwOaGroup) -> bool """
        pass

    def LoadedFileFromNdx(self, ndx):
        """ LoadedFileFromNdx(self: InwOpState9, ndx: int) -> InwOaPartition """
        pass

    def LoadedFileFromPath(self, path):
        """ LoadedFileFromPath(self: InwOpState9, path: InwOaPath) -> InwOaPartition """
        pass

    def NdxArray2Node(self, fullpath):
        """ NdxArray2Node(self: InwOpState9, fullpath: object) -> InwOaNode """
        pass

    def NdxArray2SavedView(self, fullpath):
        """ NdxArray2SavedView(self: InwOpState9, fullpath: object) -> InwOpSavedView """
        pass

    def Node2NdxArray(self, pI):
        """ Node2NdxArray(self: InwOpState9, pI: InwOaNode) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpState9, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpState9) """
        pass

    def ObjectFactory(self, eType, ovReserved1, ovReserved2):
        """ ObjectFactory(self: InwOpState9, eType: nwEObjectType, ovReserved1: object, ovReserved2: object) -> object """
        pass

    def OverrideColor(self, selection, color):
        """ OverrideColor(self: InwOpState9, selection: InwOpSelection, color: InwLVec3f) """
        pass

    def OverrideReset(self, selection):
        """ OverrideReset(self: InwOpState9, selection: InwOpSelection) """
        pass

    def OverrideResetAll(self):
        """ OverrideResetAll(self: InwOpState9) """
        pass

    def OverrideTransform(self, selection, transform):
        """ OverrideTransform(self: InwOpState9, selection: InwOpSelection, transform: InwLTransform3f) """
        pass

    def OverrideTransformReset(self, selection):
        """ OverrideTransformReset(self: InwOpState9, selection: InwOpSelection) """
        pass

    def OverrideTransformResetAll(self):
        """ OverrideTransformResetAll(self: InwOpState9) """
        pass

    def OverrideTransparency(self, selection, transparency):
        """ OverrideTransparency(self: InwOpState9, selection: InwOpSelection, transparency: float) """
        pass

    def OverrideURLReset(self, selection):
        """ OverrideURLReset(self: InwOpState9, selection: InwOpSelection) """
        pass

    def OverrideURLResetAll(self):
        """ OverrideURLResetAll(self: InwOpState9) """
        pass

    def Plugins(self):
        """ Plugins(self: InwOpState9) -> InwPluginsColl """
        pass

    def RequiredItemsResetAll(self):
        """ RequiredItemsResetAll(self: InwOpState9) """
        pass

    def SavedView2NdxArray(self, pI):
        """ SavedView2NdxArray(self: InwOpState9, pI: InwOpSavedView) -> object """
        pass

    def SavedViews(self):
        """ SavedViews(self: InwOpState9) -> InwSavedViewsColl """
        pass

    def SceneLights(self):
        """ SceneLights(self: InwOpState9) -> InwLightsColl """
        pass

    def SeekSelection(self, results, cb, ovStartSelection):
        """ SeekSelection(self: InwOpState9, results: InwOpSelection, cb: InwSeekSelection, ovStartSelection: object) """
        pass

    def SelectionSets(self):
        """ SelectionSets(self: InwOpState9) -> InwSelectionSetColl """
        pass

    def SelectionSetsEx(self):
        """ SelectionSetsEx(self: InwOpState9) -> InwSelectionSetExColl """
        pass

    def SetOverrideURL(self, selection, pI):
        """ SetOverrideURL(self: InwOpState9, selection: InwOpSelection, pI: InwURLOverride) """
        pass

    def SmartTagText(self, path):
        """ SmartTagText(self: InwOpState9, path: InwOaPath) -> str """
        pass

    def StartInteractive(self):
        """ StartInteractive(self: InwOpState9) """
        pass

    def StdName(self, Type, user_name):
        """ StdName(self: InwOpState9, Type: nwEStdName, user_name: bool) -> str """
        pass

    def StopMovement(self):
        """ StopMovement(self: InwOpState9) """
        pass

    def ViewAll(self):
        """ ViewAll(self: InwOpState9) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpState9, vIn: object) -> object """
        pass

    def ZoomInCurViewOnBoundingBox(self, box, factor):
        """ ZoomInCurViewOnBoundingBox(self: InwOpState9, box: InwLBox3f, factor: float) """
        pass

    def ZoomInCurViewOnCurSel(self):
        """ ZoomInCurViewOnCurSel(self: InwOpState9) """
        pass

    def ZoomInCurViewOnSel(self, selection):
        """ ZoomInCurViewOnSel(self: InwOpState9, selection: InwOpSelection) """
        pass

    def ZoomInViewOnSel(self, selection, anonview):
        """ ZoomInViewOnSel(self: InwOpState9, selection: InwOpSelection, anonview: InwOpAnonView) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AreaCullThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaCullThreshold(self: InwOpState9) -> float

Set: AreaCullThreshold(self: InwOpState9) = value
"""

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColor(self: InwOpState9) -> InwLVec3f

Set: BackgroundColor(self: InwOpState9) = value
"""

    CurrentAnimation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAnimation(self: InwOpState9) -> InwOpAnimView

Set: CurrentAnimation(self: InwOpState9) = value
"""

    CurrentFindSpec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentFindSpec(self: InwOpState9) -> InwOpFindSpec

Set: CurrentFindSpec(self: InwOpState9) = value
"""

    CurrentPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPartition(self: InwOpState9) -> InwOaPartition

"""

    CurrentPlanView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPlanView(self: InwOpState9) -> InwOpAnonView

Set: CurrentPlanView(self: InwOpState9) = value
"""

    CurrentSectionView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSectionView(self: InwOpState9) -> InwOpAnonView

Set: CurrentSectionView(self: InwOpState9) = value
"""

    CurrentSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSelection(self: InwOpState9) -> InwOpSelection

Set: CurrentSelection(self: InwOpState9) = value
"""

    CurrentView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentView(self: InwOpState9) -> InwOpAnonView

Set: CurrentView(self: InwOpState9) = value
"""

    EventsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventsEnabled(self: InwOpState9) -> bool

Set: EventsEnabled(self: InwOpState9) = value
"""

    FrameRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameRate(self: InwOpState9) -> int

Set: FrameRate(self: InwOpState9) = value
"""

    GlobalAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalAmbient(self: InwOpState9) -> InwLVec3f

Set: GlobalAmbient(self: InwOpState9) = value
"""

    HeadlightAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightAmbient(self: InwOpState9) -> float

Set: HeadlightAmbient(self: InwOpState9) = value
"""

    HeadlightIntensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightIntensity(self: InwOpState9) -> float

Set: HeadlightIntensity(self: InwOpState9) = value
"""

    LoadedFileCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadedFileCount(self: InwOpState9) -> int

"""

    MaxNearDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxNearDistance(self: InwOpState9) -> float

Set: MaxNearDistance(self: InwOpState9) = value
"""

    MinFarDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinFarDistance(self: InwOpState9) -> float

Set: MinFarDistance(self: InwOpState9) = value
"""

    NumTriangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumTriangles(self: InwOpState9) -> int

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpState9) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpState9) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpState9) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpState9) -> int

Set: nwLock(self: InwOpState9) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpState9) -> bool

Set: nwOwn(self: InwOpState9) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpState9) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpState9) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpState9) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpState9) -> str

"""

    SmartTagsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmartTagsEnabled(self: InwOpState9) -> bool

Set: SmartTagsEnabled(self: InwOpState9) = value
"""

    TwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TwoSided(self: InwOpState9) -> bool

Set: TwoSided(self: InwOpState9) = value
"""

    URLsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsEnabled(self: InwOpState9) -> bool

Set: URLsEnabled(self: InwOpState9) = value
"""



class InwOpState10(InwOpState9, InwOpState8, InwOpState7, InwOpState6, InwOpState5, InwOpState4, InwOpState3, InwOpState2, InwOpState, InwBase):
    # no doc
    def ApplyView(self, view):
        """ ApplyView(self: InwOpState10, view: InwOpView) """
        pass

    def BeginEdit(self, name):
        """ BeginEdit(self: InwOpState10, name: str) """
        pass

    def CheckLicense(self, name):
        """ CheckLicense(self: InwOpState10, name: str) -> bool """
        pass

    def Copy(self):
        """ Copy(self: InwOpState10) -> object """
        pass

    def CreatePicture(self, anonview, ovNumPasses, vWidth, ovHeight):
        """ CreatePicture(self: InwOpState10, anonview: InwOpAnonView, ovNumPasses: object, vWidth: object, ovHeight: object) -> object """
        pass

    def CreatePlugin(self, progid):
        """ CreatePlugin(self: InwOpState10, progid: str) -> int """
        pass

    def DeleteSelectedFiles(self):
        """ DeleteSelectedFiles(self: InwOpState10) """
        pass

    def DriveIOPlugin(self, internal_name, filename, opts):
        """ DriveIOPlugin(self: InwOpState10, internal_name: str, filename: str, opts: InwOaPropertyVec) -> nwEExportStatus """
        pass

    def EndEdit(self):
        """ EndEdit(self: InwOpState10) """
        pass

    def EndInteractive(self):
        """ EndInteractive(self: InwOpState10) """
        pass

    def FileVersion(self, filename):
        """ FileVersion(self: InwOpState10, filename: str) -> int """
        pass

    def GetAttributeProperties(self, p_attribute):
        """ GetAttributeProperties(self: InwOpState10, p_attribute: InwOaAttribute) -> InwOaPropertyVec """
        pass

    def GetBoundingBox(self):
        """ GetBoundingBox(self: InwOpState10) -> InwLBox3f """
        pass

    def GetCurrentFilename(self):
        """ GetCurrentFilename(self: InwOpState10) -> str """
        pass

    def GetEnum(self, sName):
        """ GetEnum(self: InwOpState10, sName: str) -> int """
        pass

    def GetFirstInstanceOfNode(self, node):
        """ GetFirstInstanceOfNode(self: InwOpState10, node: InwOaNode) -> InwOaPath """
        pass

    def GetGUIPropertyNode(self, p_path, b_show_internal):
        """ GetGUIPropertyNode(self: InwOpState10, p_path: InwOaPath, b_show_internal: bool) -> InwGUIPropertyNode """
        pass

    def GetIOPluginOptions(self, internal_name):
        """ GetIOPluginOptions(self: InwOpState10, internal_name: str) -> InwOaPropertyVec """
        pass

    def GetMeasureDiff(self):
        """ GetMeasureDiff(self: InwOpState10) -> InwLVec3f """
        pass

    def GetMeasureEndPos(self):
        """ GetMeasureEndPos(self: InwOpState10) -> InwLPos3f """
        pass

    def GetMeasureFirstPos(self):
        """ GetMeasureFirstPos(self: InwOpState10) -> InwLPos3f """
        pass

    def GetMeasureValue(self):
        """ GetMeasureValue(self: InwOpState10) -> float """
        pass

    def GetOverrideURL(self, p_path, include_model):
        """ GetOverrideURL(self: InwOpState10, p_path: InwOaPath, include_model: object) -> InwURLOverride """
        pass

    def GetProductInfo(self):
        """ GetProductInfo(self: InwOpState10) -> str """
        pass

    def GlobalProperties(self):
        """ GlobalProperties(self: InwOpState10) -> InwGlobalProperties """
        pass

    def HiddenItemsResetAll(self):
        """ HiddenItemsResetAll(self: InwOpState10) """
        pass

    def IsComposite(self, group):
        """ IsComposite(self: InwOpState10, group: InwOaGroup) -> bool """
        pass

    def LoadedFileFromNdx(self, ndx):
        """ LoadedFileFromNdx(self: InwOpState10, ndx: int) -> InwOaPartition """
        pass

    def LoadedFileFromPath(self, path):
        """ LoadedFileFromPath(self: InwOpState10, path: InwOaPath) -> InwOaPartition """
        pass

    def NdxArray2Node(self, fullpath):
        """ NdxArray2Node(self: InwOpState10, fullpath: object) -> InwOaNode """
        pass

    def NdxArray2SavedView(self, fullpath):
        """ NdxArray2SavedView(self: InwOpState10, fullpath: object) -> InwOpSavedView """
        pass

    def Node2NdxArray(self, pI):
        """ Node2NdxArray(self: InwOpState10, pI: InwOaNode) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpState10, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpState10) """
        pass

    def ObjectFactory(self, eType, ovReserved1, ovReserved2):
        """ ObjectFactory(self: InwOpState10, eType: nwEObjectType, ovReserved1: object, ovReserved2: object) -> object """
        pass

    def OverrideColor(self, selection, color):
        """ OverrideColor(self: InwOpState10, selection: InwOpSelection, color: InwLVec3f) """
        pass

    def OverrideReset(self, selection):
        """ OverrideReset(self: InwOpState10, selection: InwOpSelection) """
        pass

    def OverrideResetAll(self):
        """ OverrideResetAll(self: InwOpState10) """
        pass

    def OverrideTransform(self, selection, transform):
        """ OverrideTransform(self: InwOpState10, selection: InwOpSelection, transform: InwLTransform3f) """
        pass

    def OverrideTransformReset(self, selection):
        """ OverrideTransformReset(self: InwOpState10, selection: InwOpSelection) """
        pass

    def OverrideTransformResetAll(self):
        """ OverrideTransformResetAll(self: InwOpState10) """
        pass

    def OverrideTransparency(self, selection, transparency):
        """ OverrideTransparency(self: InwOpState10, selection: InwOpSelection, transparency: float) """
        pass

    def OverrideURLReset(self, selection):
        """ OverrideURLReset(self: InwOpState10, selection: InwOpSelection) """
        pass

    def OverrideURLResetAll(self):
        """ OverrideURLResetAll(self: InwOpState10) """
        pass

    def Plugins(self):
        """ Plugins(self: InwOpState10) -> InwPluginsColl """
        pass

    def PtrEquals(self, i1, i2):
        """ PtrEquals(self: InwOpState10, i1: InwBase, i2: InwBase) -> bool """
        pass

    def RequiredItemsResetAll(self):
        """ RequiredItemsResetAll(self: InwOpState10) """
        pass

    def SavedView2NdxArray(self, pI):
        """ SavedView2NdxArray(self: InwOpState10, pI: InwOpSavedView) -> object """
        pass

    def SavedViews(self):
        """ SavedViews(self: InwOpState10) -> InwSavedViewsColl """
        pass

    def SceneLights(self):
        """ SceneLights(self: InwOpState10) -> InwLightsColl """
        pass

    def SeekSelection(self, results, cb, ovStartSelection):
        """ SeekSelection(self: InwOpState10, results: InwOpSelection, cb: InwSeekSelection, ovStartSelection: object) """
        pass

    def SelectionSets(self):
        """ SelectionSets(self: InwOpState10) -> InwSelectionSetColl """
        pass

    def SelectionSetsEx(self):
        """ SelectionSetsEx(self: InwOpState10) -> InwSelectionSetExColl """
        pass

    def SetOverrideURL(self, selection, pI):
        """ SetOverrideURL(self: InwOpState10, selection: InwOpSelection, pI: InwURLOverride) """
        pass

    def SmartTagText(self, path):
        """ SmartTagText(self: InwOpState10, path: InwOaPath) -> str """
        pass

    def StartInteractive(self):
        """ StartInteractive(self: InwOpState10) """
        pass

    def StdName(self, Type, user_name):
        """ StdName(self: InwOpState10, Type: nwEStdName, user_name: bool) -> str """
        pass

    def StopMovement(self):
        """ StopMovement(self: InwOpState10) """
        pass

    def ViewAll(self):
        """ ViewAll(self: InwOpState10) """
        pass

    def X64PtrLongs(self, i1, high, low):
        """ X64PtrLongs(self: InwOpState10, i1: InwBase) -> (int, int) """
        pass

    def X64PtrVar(self, i1, pointer):
        """ X64PtrVar(self: InwOpState10, i1: InwBase) -> object """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpState10, vIn: object) -> object """
        pass

    def ZoomInCurViewOnBoundingBox(self, box, factor):
        """ ZoomInCurViewOnBoundingBox(self: InwOpState10, box: InwLBox3f, factor: float) """
        pass

    def ZoomInCurViewOnCurSel(self):
        """ ZoomInCurViewOnCurSel(self: InwOpState10) """
        pass

    def ZoomInCurViewOnSel(self, selection):
        """ ZoomInCurViewOnSel(self: InwOpState10, selection: InwOpSelection) """
        pass

    def ZoomInViewOnSel(self, selection, anonview):
        """ ZoomInViewOnSel(self: InwOpState10, selection: InwOpSelection, anonview: InwOpAnonView) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AreaCullThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaCullThreshold(self: InwOpState10) -> float

Set: AreaCullThreshold(self: InwOpState10) = value
"""

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColor(self: InwOpState10) -> InwLVec3f

Set: BackgroundColor(self: InwOpState10) = value
"""

    CurrentAnimation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAnimation(self: InwOpState10) -> InwOpAnimView

Set: CurrentAnimation(self: InwOpState10) = value
"""

    CurrentFindSpec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentFindSpec(self: InwOpState10) -> InwOpFindSpec

Set: CurrentFindSpec(self: InwOpState10) = value
"""

    CurrentPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPartition(self: InwOpState10) -> InwOaPartition

"""

    CurrentPlanView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPlanView(self: InwOpState10) -> InwOpAnonView

Set: CurrentPlanView(self: InwOpState10) = value
"""

    CurrentSectionView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSectionView(self: InwOpState10) -> InwOpAnonView

Set: CurrentSectionView(self: InwOpState10) = value
"""

    CurrentSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSelection(self: InwOpState10) -> InwOpSelection

Set: CurrentSelection(self: InwOpState10) = value
"""

    CurrentView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentView(self: InwOpState10) -> InwOpAnonView

Set: CurrentView(self: InwOpState10) = value
"""

    EventsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventsEnabled(self: InwOpState10) -> bool

Set: EventsEnabled(self: InwOpState10) = value
"""

    FrameRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameRate(self: InwOpState10) -> int

Set: FrameRate(self: InwOpState10) = value
"""

    GlobalAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalAmbient(self: InwOpState10) -> InwLVec3f

Set: GlobalAmbient(self: InwOpState10) = value
"""

    HeadlightAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightAmbient(self: InwOpState10) -> float

Set: HeadlightAmbient(self: InwOpState10) = value
"""

    HeadlightIntensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightIntensity(self: InwOpState10) -> float

Set: HeadlightIntensity(self: InwOpState10) = value
"""

    LoadedFileCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadedFileCount(self: InwOpState10) -> int

"""

    MaxNearDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxNearDistance(self: InwOpState10) -> float

Set: MaxNearDistance(self: InwOpState10) = value
"""

    MinFarDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinFarDistance(self: InwOpState10) -> float

Set: MinFarDistance(self: InwOpState10) = value
"""

    NumTriangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumTriangles(self: InwOpState10) -> int

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpState10) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpState10) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpState10) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpState10) -> int

Set: nwLock(self: InwOpState10) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpState10) -> bool

Set: nwOwn(self: InwOpState10) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpState10) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpState10) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpState10) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpState10) -> str

"""

    SmartTagsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmartTagsEnabled(self: InwOpState10) -> bool

Set: SmartTagsEnabled(self: InwOpState10) = value
"""

    TwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TwoSided(self: InwOpState10) -> bool

Set: TwoSided(self: InwOpState10) = value
"""

    URLsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsEnabled(self: InwOpState10) -> bool

Set: URLsEnabled(self: InwOpState10) = value
"""



class InwOpState11(InwOpState10, InwOpState9, InwOpState8, InwOpState7, InwOpState6, InwOpState5, InwOpState4, InwOpState3, InwOpState2, InwOpState, InwBase):
    # no doc
    def ApplyView(self, view):
        """ ApplyView(self: InwOpState11, view: InwOpView) """
        pass

    def BeginEdit(self, name):
        """ BeginEdit(self: InwOpState11, name: str) """
        pass

    def CheckLicense(self, name):
        """ CheckLicense(self: InwOpState11, name: str) -> bool """
        pass

    def Copy(self):
        """ Copy(self: InwOpState11) -> object """
        pass

    def CreatePicture(self, anonview, ovNumPasses, vWidth, ovHeight):
        """ CreatePicture(self: InwOpState11, anonview: InwOpAnonView, ovNumPasses: object, vWidth: object, ovHeight: object) -> object """
        pass

    def CreatePlugin(self, progid):
        """ CreatePlugin(self: InwOpState11, progid: str) -> int """
        pass

    def DeleteSelectedFiles(self):
        """ DeleteSelectedFiles(self: InwOpState11) """
        pass

    def DriveIOPlugin(self, internal_name, filename, opts):
        """ DriveIOPlugin(self: InwOpState11, internal_name: str, filename: str, opts: InwOaPropertyVec) -> nwEExportStatus """
        pass

    def EndEdit(self):
        """ EndEdit(self: InwOpState11) """
        pass

    def EndInteractive(self):
        """ EndInteractive(self: InwOpState11) """
        pass

    def FileVersion(self, filename):
        """ FileVersion(self: InwOpState11, filename: str) -> int """
        pass

    def GetAttributeProperties(self, p_attribute):
        """ GetAttributeProperties(self: InwOpState11, p_attribute: InwOaAttribute) -> InwOaPropertyVec """
        pass

    def GetBoundingBox(self):
        """ GetBoundingBox(self: InwOpState11) -> InwLBox3f """
        pass

    def GetCurrentFilename(self):
        """ GetCurrentFilename(self: InwOpState11) -> str """
        pass

    def GetEnum(self, sName):
        """ GetEnum(self: InwOpState11, sName: str) -> int """
        pass

    def GetFirstInstanceOfNode(self, node):
        """ GetFirstInstanceOfNode(self: InwOpState11, node: InwOaNode) -> InwOaPath """
        pass

    def GetGUIPropertyNode(self, p_path, b_show_internal):
        """ GetGUIPropertyNode(self: InwOpState11, p_path: InwOaPath, b_show_internal: bool) -> InwGUIPropertyNode """
        pass

    def GetIOPluginOptions(self, internal_name):
        """ GetIOPluginOptions(self: InwOpState11, internal_name: str) -> InwOaPropertyVec """
        pass

    def GetMeasureDiff(self):
        """ GetMeasureDiff(self: InwOpState11) -> InwLVec3f """
        pass

    def GetMeasureEndPos(self):
        """ GetMeasureEndPos(self: InwOpState11) -> InwLPos3f """
        pass

    def GetMeasureFirstPos(self):
        """ GetMeasureFirstPos(self: InwOpState11) -> InwLPos3f """
        pass

    def GetMeasureValue(self):
        """ GetMeasureValue(self: InwOpState11) -> float """
        pass

    def GetOverrideURL(self, p_path, include_model):
        """ GetOverrideURL(self: InwOpState11, p_path: InwOaPath, include_model: object) -> InwURLOverride """
        pass

    def GetProductInfo(self):
        """ GetProductInfo(self: InwOpState11) -> str """
        pass

    def GlobalProperties(self):
        """ GlobalProperties(self: InwOpState11) -> InwGlobalProperties """
        pass

    def HiddenItemsResetAll(self):
        """ HiddenItemsResetAll(self: InwOpState11) """
        pass

    def IsComposite(self, group):
        """ IsComposite(self: InwOpState11, group: InwOaGroup) -> bool """
        pass

    def LoadedFileFromNdx(self, ndx):
        """ LoadedFileFromNdx(self: InwOpState11, ndx: int) -> InwOaPartition """
        pass

    def LoadedFileFromPath(self, path):
        """ LoadedFileFromPath(self: InwOpState11, path: InwOaPath) -> InwOaPartition """
        pass

    def NdxArray2Node(self, fullpath):
        """ NdxArray2Node(self: InwOpState11, fullpath: object) -> InwOaNode """
        pass

    def NdxArray2SavedView(self, fullpath):
        """ NdxArray2SavedView(self: InwOpState11, fullpath: object) -> InwOpSavedView """
        pass

    def Node2NdxArray(self, pI):
        """ Node2NdxArray(self: InwOpState11, pI: InwOaNode) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpState11, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpState11) """
        pass

    def ObjectFactory(self, eType, ovReserved1, ovReserved2):
        """ ObjectFactory(self: InwOpState11, eType: nwEObjectType, ovReserved1: object, ovReserved2: object) -> object """
        pass

    def OverrideColor(self, selection, color):
        """ OverrideColor(self: InwOpState11, selection: InwOpSelection, color: InwLVec3f) """
        pass

    def OverrideReset(self, selection):
        """ OverrideReset(self: InwOpState11, selection: InwOpSelection) """
        pass

    def OverrideResetAll(self):
        """ OverrideResetAll(self: InwOpState11) """
        pass

    def OverrideTransform(self, selection, transform):
        """ OverrideTransform(self: InwOpState11, selection: InwOpSelection, transform: InwLTransform3f) """
        pass

    def OverrideTransformEx(self, selection, transform, overrideFileTransform):
        """ OverrideTransformEx(self: InwOpState11, selection: InwOpSelection, transform: InwLTransform3f, overrideFileTransform: bool) """
        pass

    def OverrideTransformReset(self, selection):
        """ OverrideTransformReset(self: InwOpState11, selection: InwOpSelection) """
        pass

    def OverrideTransformResetAll(self):
        """ OverrideTransformResetAll(self: InwOpState11) """
        pass

    def OverrideTransparency(self, selection, transparency):
        """ OverrideTransparency(self: InwOpState11, selection: InwOpSelection, transparency: float) """
        pass

    def OverrideURLReset(self, selection):
        """ OverrideURLReset(self: InwOpState11, selection: InwOpSelection) """
        pass

    def OverrideURLResetAll(self):
        """ OverrideURLResetAll(self: InwOpState11) """
        pass

    def Plugins(self):
        """ Plugins(self: InwOpState11) -> InwPluginsColl """
        pass

    def PtrEquals(self, i1, i2):
        """ PtrEquals(self: InwOpState11, i1: InwBase, i2: InwBase) -> bool """
        pass

    def RequiredItemsResetAll(self):
        """ RequiredItemsResetAll(self: InwOpState11) """
        pass

    def SavedView2NdxArray(self, pI):
        """ SavedView2NdxArray(self: InwOpState11, pI: InwOpSavedView) -> object """
        pass

    def SavedViews(self):
        """ SavedViews(self: InwOpState11) -> InwSavedViewsColl """
        pass

    def SceneLights(self):
        """ SceneLights(self: InwOpState11) -> InwLightsColl """
        pass

    def SeekSelection(self, results, cb, ovStartSelection):
        """ SeekSelection(self: InwOpState11, results: InwOpSelection, cb: InwSeekSelection, ovStartSelection: object) """
        pass

    def SelectionSets(self):
        """ SelectionSets(self: InwOpState11) -> InwSelectionSetColl """
        pass

    def SelectionSetsEx(self):
        """ SelectionSetsEx(self: InwOpState11) -> InwSelectionSetExColl """
        pass

    def SetOverrideURL(self, selection, pI):
        """ SetOverrideURL(self: InwOpState11, selection: InwOpSelection, pI: InwURLOverride) """
        pass

    def SmartTagText(self, path):
        """ SmartTagText(self: InwOpState11, path: InwOaPath) -> str """
        pass

    def StartInteractive(self):
        """ StartInteractive(self: InwOpState11) """
        pass

    def StdName(self, Type, user_name):
        """ StdName(self: InwOpState11, Type: nwEStdName, user_name: bool) -> str """
        pass

    def StopMovement(self):
        """ StopMovement(self: InwOpState11) """
        pass

    def ViewAll(self):
        """ ViewAll(self: InwOpState11) """
        pass

    def X64PtrLongs(self, i1, high, low):
        """ X64PtrLongs(self: InwOpState11, i1: InwBase) -> (int, int) """
        pass

    def X64PtrVar(self, i1, pointer):
        """ X64PtrVar(self: InwOpState11, i1: InwBase) -> object """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpState11, vIn: object) -> object """
        pass

    def ZoomInCurViewOnBoundingBox(self, box, factor):
        """ ZoomInCurViewOnBoundingBox(self: InwOpState11, box: InwLBox3f, factor: float) """
        pass

    def ZoomInCurViewOnCurSel(self):
        """ ZoomInCurViewOnCurSel(self: InwOpState11) """
        pass

    def ZoomInCurViewOnSel(self, selection):
        """ ZoomInCurViewOnSel(self: InwOpState11, selection: InwOpSelection) """
        pass

    def ZoomInViewOnSel(self, selection, anonview):
        """ ZoomInViewOnSel(self: InwOpState11, selection: InwOpSelection, anonview: InwOpAnonView) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AreaCullThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaCullThreshold(self: InwOpState11) -> float

Set: AreaCullThreshold(self: InwOpState11) = value
"""

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColor(self: InwOpState11) -> InwLVec3f

Set: BackgroundColor(self: InwOpState11) = value
"""

    CurrentAnimation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAnimation(self: InwOpState11) -> InwOpAnimView

Set: CurrentAnimation(self: InwOpState11) = value
"""

    CurrentFindSpec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentFindSpec(self: InwOpState11) -> InwOpFindSpec

Set: CurrentFindSpec(self: InwOpState11) = value
"""

    CurrentPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPartition(self: InwOpState11) -> InwOaPartition

"""

    CurrentPlanView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPlanView(self: InwOpState11) -> InwOpAnonView

Set: CurrentPlanView(self: InwOpState11) = value
"""

    CurrentSectionView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSectionView(self: InwOpState11) -> InwOpAnonView

Set: CurrentSectionView(self: InwOpState11) = value
"""

    CurrentSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSelection(self: InwOpState11) -> InwOpSelection

Set: CurrentSelection(self: InwOpState11) = value
"""

    CurrentView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentView(self: InwOpState11) -> InwOpAnonView

Set: CurrentView(self: InwOpState11) = value
"""

    EventsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventsEnabled(self: InwOpState11) -> bool

Set: EventsEnabled(self: InwOpState11) = value
"""

    FrameRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameRate(self: InwOpState11) -> int

Set: FrameRate(self: InwOpState11) = value
"""

    GlobalAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalAmbient(self: InwOpState11) -> InwLVec3f

Set: GlobalAmbient(self: InwOpState11) = value
"""

    HeadlightAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightAmbient(self: InwOpState11) -> float

Set: HeadlightAmbient(self: InwOpState11) = value
"""

    HeadlightIntensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightIntensity(self: InwOpState11) -> float

Set: HeadlightIntensity(self: InwOpState11) = value
"""

    LoadedFileCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadedFileCount(self: InwOpState11) -> int

"""

    MaxNearDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxNearDistance(self: InwOpState11) -> float

Set: MaxNearDistance(self: InwOpState11) = value
"""

    MinFarDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinFarDistance(self: InwOpState11) -> float

Set: MinFarDistance(self: InwOpState11) = value
"""

    NumTriangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumTriangles(self: InwOpState11) -> int

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpState11) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpState11) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpState11) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpState11) -> int

Set: nwLock(self: InwOpState11) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpState11) -> bool

Set: nwOwn(self: InwOpState11) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpState11) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpState11) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpState11) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpState11) -> str

"""

    SmartTagsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmartTagsEnabled(self: InwOpState11) -> bool

Set: SmartTagsEnabled(self: InwOpState11) = value
"""

    TwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TwoSided(self: InwOpState11) -> bool

Set: TwoSided(self: InwOpState11) = value
"""

    URLsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsEnabled(self: InwOpState11) -> bool

Set: URLsEnabled(self: InwOpState11) = value
"""



class InwOpUserFindSpec(InwBase):
    # no doc
    def Conditions(self):
        """ Conditions(self: InwOpUserFindSpec) -> InwOpFindConditionsColl """
        pass

    def Copy(self):
        """ Copy(self: InwOpUserFindSpec) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpUserFindSpec, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpUserFindSpec) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpUserFindSpec, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Continued = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Continued(self: InwOpUserFindSpec) -> bool

Set: Continued(self: InwOpUserFindSpec) = value
"""

    ExplicitIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExplicitIcon(self: InwOpUserFindSpec) -> nwESelTreeIcon

Set: ExplicitIcon(self: InwOpUserFindSpec) = value
"""

    ExplicitName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExplicitName(self: InwOpUserFindSpec) -> str

Set: ExplicitName(self: InwOpUserFindSpec) = value
"""

    ExplicitTextFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExplicitTextFormat(self: InwOpUserFindSpec) -> nwESelTreeTextFormat

Set: ExplicitTextFormat(self: InwOpUserFindSpec) = value
"""

    GroupMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupMode(self: InwOpUserFindSpec) -> nwESelTreeGroupMode

Set: GroupMode(self: InwOpUserFindSpec) = value
"""

    IconMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IconMode(self: InwOpUserFindSpec) -> nwESelTreeIconMode

Set: IconMode(self: InwOpUserFindSpec) = value
"""

    NameMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NameMode(self: InwOpUserFindSpec) -> nwESelTreeNameMode

Set: NameMode(self: InwOpUserFindSpec) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpUserFindSpec) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpUserFindSpec) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpUserFindSpec) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpUserFindSpec) -> int

Set: nwLock(self: InwOpUserFindSpec) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpUserFindSpec) -> bool

Set: nwOwn(self: InwOpUserFindSpec) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpUserFindSpec) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpUserFindSpec) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpUserFindSpec) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpUserFindSpec) -> str

"""

    SearchMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SearchMode(self: InwOpUserFindSpec) -> nwESearchMode

Set: SearchMode(self: InwOpUserFindSpec) = value
"""

    SelectionDisjoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionDisjoint(self: InwOpUserFindSpec) -> bool

Set: SelectionDisjoint(self: InwOpUserFindSpec) = value
"""

    SelectionSubPaths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionSubPaths(self: InwOpUserFindSpec) -> bool

Set: SelectionSubPaths(self: InwOpUserFindSpec) = value
"""

    TextFormatMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextFormatMode(self: InwOpUserFindSpec) -> nwESelTreeTextFormatMode

Set: TextFormatMode(self: InwOpUserFindSpec) = value
"""



class InwOpUserFindSpecsColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwOpUserFindSpecsColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwOpUserFindSpecsColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwOpUserFindSpecsColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwOpUserFindSpecsColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwOpUserFindSpecsColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwOpUserFindSpecsColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwOpUserFindSpecsColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwOpUserFindSpecsColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwOpUserFindSpecsColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwOpUserFindSpecsColl) -> bool

"""



class InwOpUserSelectionTreePlugin(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOpUserSelectionTreePlugin) -> object """
        pass

    def GetTreeSpec(self):
        """ GetTreeSpec(self: InwOpUserSelectionTreePlugin) -> InwOpUserSelectionTreeSpec """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpUserSelectionTreePlugin, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpUserSelectionTreePlugin) """
        pass

    def SaveFileToAppSpecDir(self):
        """ SaveFileToAppSpecDir(self: InwOpUserSelectionTreePlugin) """
        pass

    def SetTreeSpec(self, spec):
        """ SetTreeSpec(self: InwOpUserSelectionTreePlugin, spec: InwOpUserSelectionTreeSpec) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpUserSelectionTreePlugin, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwOpUserSelectionTreePlugin) -> str

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpUserSelectionTreePlugin) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpUserSelectionTreePlugin) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpUserSelectionTreePlugin) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpUserSelectionTreePlugin) -> int

Set: nwLock(self: InwOpUserSelectionTreePlugin) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpUserSelectionTreePlugin) -> bool

Set: nwOwn(self: InwOpUserSelectionTreePlugin) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpUserSelectionTreePlugin) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpUserSelectionTreePlugin) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpUserSelectionTreePlugin) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpUserSelectionTreePlugin) -> str

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: InwOpUserSelectionTreePlugin) -> int

"""



class InwOpUserSelectionTreeSpec(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwOpUserSelectionTreeSpec) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpUserSelectionTreeSpec, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpUserSelectionTreeSpec) """
        pass

    def SaveToFile(self, filename):
        """ SaveToFile(self: InwOpUserSelectionTreeSpec, filename: str) """
        pass

    def UserFindSpecs(self):
        """ UserFindSpecs(self: InwOpUserSelectionTreeSpec) -> InwOpUserFindSpecsColl """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpUserSelectionTreeSpec, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Bottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bottom(self: InwOpUserSelectionTreeSpec) -> nwESelTreeBottom

Set: Bottom(self: InwOpUserSelectionTreeSpec) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpUserSelectionTreeSpec) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpUserSelectionTreeSpec) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpUserSelectionTreeSpec) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpUserSelectionTreeSpec) -> int

Set: nwLock(self: InwOpUserSelectionTreeSpec) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpUserSelectionTreeSpec) -> bool

Set: nwOwn(self: InwOpUserSelectionTreeSpec) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpUserSelectionTreeSpec) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpUserSelectionTreeSpec) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpUserSelectionTreeSpec) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpUserSelectionTreeSpec) -> str

"""

    Top = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Top(self: InwOpUserSelectionTreeSpec) -> nwESelTreeTop

Set: Top(self: InwOpUserSelectionTreeSpec) = value
"""

    UserString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserString(self: InwOpUserSelectionTreeSpec) -> str

Set: UserString(self: InwOpUserSelectionTreeSpec) = value
"""



class InwOpView(InwOpSavedView, InwBase):
    # no doc
    def Comments(self):
        """ Comments(self: InwOpView) -> InwCommentsColl """
        pass

    def Copy(self):
        """ Copy(self: InwOpView) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpView, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpView) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpView, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    anonview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: anonview(self: InwOpView) -> InwOpAnonView

Set: anonview(self: InwOpView) = value
"""

    ApplyHideAttribs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyHideAttribs(self: InwOpView) -> bool

Set: ApplyHideAttribs(self: InwOpView) = value
"""

    ApplyMaterialAttribs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyMaterialAttribs(self: InwOpView) -> bool

Set: ApplyMaterialAttribs(self: InwOpView) = value
"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwOpView) -> str

Set: name(self: InwOpView) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpView) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpView) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpView) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpView) -> int

Set: nwLock(self: InwOpView) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpView) -> bool

Set: nwOwn(self: InwOpView) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpView) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpView) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpView) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpView) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: InwOpView) -> nwESavedViewType

"""



class InwOpView2(InwOpView, InwOpSavedView, InwBase):
    # no doc
    def Comments(self):
        """ Comments(self: InwOpView2) -> InwCommentsColl """
        pass

    def Copy(self):
        """ Copy(self: InwOpView2) -> object """
        pass

    def FindTagIDFromCommentID(self, comment_id):
        """ FindTagIDFromCommentID(self: InwOpView2, comment_id: int) -> int """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwOpView2, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwOpView2) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwOpView2, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    anonview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: anonview(self: InwOpView2) -> InwOpAnonView

Set: anonview(self: InwOpView2) = value
"""

    ApplyHideAttribs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyHideAttribs(self: InwOpView2) -> bool

Set: ApplyHideAttribs(self: InwOpView2) = value
"""

    ApplyMaterialAttribs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyMaterialAttribs(self: InwOpView2) -> bool

Set: ApplyMaterialAttribs(self: InwOpView2) = value
"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwOpView2) -> str

Set: name(self: InwOpView2) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwOpView2) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwOpView2) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwOpView2) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwOpView2) -> int

Set: nwLock(self: InwOpView2) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwOpView2) -> bool

Set: nwOwn(self: InwOpView2) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwOpView2) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwOpView2) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwOpView2) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwOpView2) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: InwOpView2) -> nwESavedViewType

"""



class InwPathNodesColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwPathNodesColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwPathNodesColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwPathNodesColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwPathNodesColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwPathNodesColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwPathNodesColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwPathNodesColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwPathNodesColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwPathNodesColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwPathNodesColl) -> bool

"""



class InwPlugin:
    # no doc
    def AdviseSite(self, plugin_site):
        """ AdviseSite(self: InwPlugin, plugin_site: InwPlugin_Site) """
        pass

    def iActivate(self):
        """ iActivate(self: InwPlugin) -> bool """
        pass

    def iAppInitialising(self):
        """ iAppInitialising(self: InwPlugin) """
        pass

    def iAppTerminating(self):
        """ iAppTerminating(self: InwPlugin) """
        pass

    def iDeactivate(self):
        """ iDeactivate(self: InwPlugin) -> bool """
        pass

    def iDoCustomOption(self):
        """ iDoCustomOption(self: InwPlugin) """
        pass

    def iGetDisplayName(self):
        """ iGetDisplayName(self: InwPlugin) -> str """
        pass

    def iGetNumParameters(self):
        """ iGetNumParameters(self: InwPlugin) -> int """
        pass

    def iGetParameter(self, ndx, pData):
        """ iGetParameter(self: InwPlugin, ndx: int) -> (str, object) """
        pass

    def iSetParameter(self, ndx, newVal):
        """ iSetParameter(self: InwPlugin, ndx: int, newVal: object) -> bool """
        pass

    def iXtension(self, vIn):
        """ iXtension(self: InwPlugin, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwPlugin) -> str

"""



class InwPluginLicense:
    # no doc
    def iGetModuleName(self):
        """ iGetModuleName(self: InwPluginLicense) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InwPluginsColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwPluginsColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwPluginsColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwPluginsColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwPluginsColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwPluginsColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwPluginsColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwPluginsColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwPluginsColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwPluginsColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwPluginsColl) -> bool

"""



class InwPropertyPlugin:
    # no doc
    def iCanTake(self, attrib, path, State):
        """ iCanTake(self: InwPropertyPlugin, attrib: InwOaAttribute, path: InwOaPath, State: InwOpState) -> nwECanTake """
        pass

    def iClassUserName(self, attrib, path, State):
        """ iClassUserName(self: InwPropertyPlugin, attrib: InwOaAttribute, path: InwOaPath, State: InwOpState) -> str """
        pass

    def iContentsProperties(self, attrib, path, State, bShowSheet, display_props):
        """ iContentsProperties(self: InwPropertyPlugin, attrib: InwOaAttribute, path: InwOaPath, State: InwOpState, display_props: InwOaPropertyColl) -> bool """
        pass

    def iContentsText(self, attrib, path, State, bShowSheet):
        """ iContentsText(self: InwPropertyPlugin, attrib: InwOaAttribute, path: InwOaPath, State: InwOpState) -> (str, bool) """
        pass

    def InitialisePlugin(self, capbits, ver):
        """ InitialisePlugin(self: InwPropertyPlugin) -> (int, int) """
        pass

    def iXtension(self, vIn):
        """ iXtension(self: InwPropertyPlugin, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InwPropertyPlugin2:
    # no doc
    def iCanAdd(self, path, State):
        """ iCanAdd(self: InwPropertyPlugin2, path: InwOaPath, State: InwOpState) -> bool """
        pass

    def iGetClassName(self):
        """ iGetClassName(self: InwPropertyPlugin2) -> str """
        pass

    def iGetClassUserName(self):
        """ iGetClassUserName(self: InwPropertyPlugin2) -> str """
        pass

    def iName(self, attrib, path, State):
        """ iName(self: InwPropertyPlugin2, attrib: InwOaAttribute, path: InwOaPath, State: InwOpState) -> str """
        pass

    def InitialisePlugin(self, capbits, ver):
        """ InitialisePlugin(self: InwPropertyPlugin2) -> (int, int) """
        pass

    def iProps(self, display_props, attrib, path, State):
        """ iProps(self: InwPropertyPlugin2, display_props: InwOaPropertyColl, attrib: InwOaAttribute, path: InwOaPath, State: InwOpState) """
        pass

    def iXtension(self, vIn):
        """ iXtension(self: InwPropertyPlugin2, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InwPropertyPlugin2_Site(InwPlugin_Site, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwPropertyPlugin2_Site) -> object """
        pass

    def GetApplication(self):
        """ GetApplication(self: InwPropertyPlugin2_Site) -> object """
        pass

    def NotifyChange(self, State, ov_path, ov_attrib_class_name):
        """ NotifyChange(self: InwPropertyPlugin2_Site, State: InwOpState, ov_path: object, ov_attrib_class_name: object) """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwPropertyPlugin2_Site, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwPropertyPlugin2_Site) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwPropertyPlugin2_Site, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwPropertyPlugin2_Site) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwPropertyPlugin2_Site) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwPropertyPlugin2_Site) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwPropertyPlugin2_Site) -> int

Set: nwLock(self: InwPropertyPlugin2_Site) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwPropertyPlugin2_Site) -> bool

Set: nwOwn(self: InwPropertyPlugin2_Site) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwPropertyPlugin2_Site) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwPropertyPlugin2_Site) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwPropertyPlugin2_Site) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwPropertyPlugin2_Site) -> str

"""



class InwPropertyPlugin_Site(InwPlugin_Site, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwPropertyPlugin_Site) -> object """
        pass

    def GetApplication(self):
        """ GetApplication(self: InwPropertyPlugin_Site) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwPropertyPlugin_Site, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwPropertyPlugin_Site) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwPropertyPlugin_Site, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwPropertyPlugin_Site) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwPropertyPlugin_Site) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwPropertyPlugin_Site) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwPropertyPlugin_Site) -> int

Set: nwLock(self: InwPropertyPlugin_Site) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwPropertyPlugin_Site) -> bool

Set: nwOwn(self: InwPropertyPlugin_Site) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwPropertyPlugin_Site) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwPropertyPlugin_Site) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwPropertyPlugin_Site) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwPropertyPlugin_Site) -> str

"""



class InwSavedViewsColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwSavedViewsColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwSavedViewsColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwSavedViewsColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwSavedViewsColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwSavedViewsColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwSavedViewsColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwSavedViewsColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwSavedViewsColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwSavedViewsColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwSavedViewsColl) -> bool

"""



class InwScriptParser:
    # no doc
    def AddObject(self, sName, pIunk):
        """ AddObject(self: InwScriptParser, sName: str, pIunk: object) """
        pass

    def CreateEngine(self, engine_name):
        """ CreateEngine(self: InwScriptParser, engine_name: str) """
        pass

    def GetScriptDispatch(self, sName):
        """ GetScriptDispatch(self: InwScriptParser, sName: str) -> object """
        pass

    def LoadScript(self, script):
        """ LoadScript(self: InwScriptParser, script: str) """
        pass

    def Run(self):
        """ Run(self: InwScriptParser) """
        pass

    def Stop(self):
        """ Stop(self: InwScriptParser) """
        pass

    def ThreadSafeKill(self):
        """ ThreadSafeKill(self: InwScriptParser) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InwSeekSelection:
    # no doc
    def SelectNode(self, node, path, Add, finished):
        """ SelectNode(self: InwSeekSelection, node: InwOaNode, path: InwOaPath) -> (bool, bool) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InwSelectionPathsColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwSelectionPathsColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwSelectionPathsColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwSelectionPathsColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwSelectionPathsColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwSelectionPathsColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwSelectionPathsColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwSelectionPathsColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwSelectionPathsColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwSelectionPathsColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwSelectionPathsColl) -> bool

"""



class InwSelectionSetColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwSelectionSetColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwSelectionSetColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwSelectionSetColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwSelectionSetColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwSelectionSetColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwSelectionSetColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwSelectionSetColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwSelectionSetColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwSelectionSetColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwSelectionSetColl) -> bool

"""



class InwSelectionSetExColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwSelectionSetExColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwSelectionSetExColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwSelectionSetExColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwSelectionSetExColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwSelectionSetExColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwSelectionSetExColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwSelectionSetExColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwSelectionSetExColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwSelectionSetExColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwSelectionSetExColl) -> bool

"""



class InwSelectionSetFolder(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwSelectionSetFolder) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwSelectionSetFolder, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwSelectionSetFolder) """
        pass

    def SelectionSets(self):
        """ SelectionSets(self: InwSelectionSetFolder) -> InwSelectionSetExColl """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwSelectionSetFolder, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwSelectionSetFolder) -> str

Set: name(self: InwSelectionSetFolder) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwSelectionSetFolder) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwSelectionSetFolder) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwSelectionSetFolder) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwSelectionSetFolder) -> int

Set: nwLock(self: InwSelectionSetFolder) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwSelectionSetFolder) -> bool

Set: nwOwn(self: InwSelectionSetFolder) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwSelectionSetFolder) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwSelectionSetFolder) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwSelectionSetFolder) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwSelectionSetFolder) -> str

"""



class InwSelectionTreePlugin:
    # no doc
    def iCreateInterface(self, State):
        """ iCreateInterface(self: InwSelectionTreePlugin, State: InwOpState) -> InwOpSelectionTreeInterface """
        pass

    def iGetUserString(self):
        """ iGetUserString(self: InwSelectionTreePlugin) -> str """
        pass

    def InitialisePlugin(self, capbits, ver):
        """ InitialisePlugin(self: InwSelectionTreePlugin) -> (int, int) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InwSelectionTreePlugin_Site(InwPlugin_Site, InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwSelectionTreePlugin_Site) -> object """
        pass

    def GetApplication(self):
        """ GetApplication(self: InwSelectionTreePlugin_Site) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwSelectionTreePlugin_Site, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwSelectionTreePlugin_Site) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwSelectionTreePlugin_Site, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwSelectionTreePlugin_Site) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwSelectionTreePlugin_Site) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwSelectionTreePlugin_Site) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwSelectionTreePlugin_Site) -> int

Set: nwLock(self: InwSelectionTreePlugin_Site) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwSelectionTreePlugin_Site) -> bool

Set: nwOwn(self: InwSelectionTreePlugin_Site) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwSelectionTreePlugin_Site) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwSelectionTreePlugin_Site) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwSelectionTreePlugin_Site) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwSelectionTreePlugin_Site) -> str

"""



class InwSimplePrimitivesCB:
    # no doc
    def Line(self, v1, v2):
        """ Line(self: InwSimplePrimitivesCB, v1: InwSimpleVertex, v2: InwSimpleVertex) """
        pass

    def Point(self, v1):
        """ Point(self: InwSimplePrimitivesCB, v1: InwSimpleVertex) """
        pass

    def SnapPoint(self, v1):
        """ SnapPoint(self: InwSimplePrimitivesCB, v1: InwSimpleVertex) """
        pass

    def Triangle(self, v1, v2, v3):
        """ Triangle(self: InwSimplePrimitivesCB, v1: InwSimpleVertex, v2: InwSimpleVertex, v3: InwSimpleVertex) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InwSimpleVertex(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwSimpleVertex) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwSimpleVertex, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwSimpleVertex) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwSimpleVertex, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: color(self: InwSimpleVertex) -> object

"""

    coord = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: coord(self: InwSimpleVertex) -> object

"""

    normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: normal(self: InwSimpleVertex) -> object

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwSimpleVertex) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwSimpleVertex) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwSimpleVertex) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwSimpleVertex) -> int

Set: nwLock(self: InwSimpleVertex) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwSimpleVertex) -> bool

Set: nwOwn(self: InwSimpleVertex) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwSimpleVertex) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwSimpleVertex) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwSimpleVertex) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwSimpleVertex) -> str

"""

    tex_coord = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: tex_coord(self: InwSimpleVertex) -> object

"""



class InwSmartTagsOpts(InwBase):
    # no doc
    def Conditions(self):
        """ Conditions(self: InwSmartTagsOpts) -> InwOpFindConditionsColl """
        pass

    def Copy(self):
        """ Copy(self: InwSmartTagsOpts) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwSmartTagsOpts, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwSmartTagsOpts) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwSmartTagsOpts, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwSmartTagsOpts) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwSmartTagsOpts) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwSmartTagsOpts) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwSmartTagsOpts) -> int

Set: nwLock(self: InwSmartTagsOpts) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwSmartTagsOpts) -> bool

Set: nwOwn(self: InwSmartTagsOpts) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwSmartTagsOpts) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwSmartTagsOpts) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwSmartTagsOpts) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwSmartTagsOpts) -> str

"""



class InwTestResultsColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwTestResultsColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwTestResultsColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwTestResultsColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwTestResultsColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwTestResultsColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwTestResultsColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwTestResultsColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwTestResultsColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwTestResultsColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwTestResultsColl) -> bool

"""



class InwUInt32Vector(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwUInt32Vector) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwUInt32Vector, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwUInt32Vector) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwUInt32Vector, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ArrayData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArrayData(self: InwUInt32Vector) -> object

Set: ArrayData(self: InwUInt32Vector) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwUInt32Vector) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwUInt32Vector) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwUInt32Vector) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwUInt32Vector) -> int

Set: nwLock(self: InwUInt32Vector) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwUInt32Vector) -> bool

Set: nwOwn(self: InwUInt32Vector) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwUInt32Vector) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwUInt32Vector) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwUInt32Vector) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwUInt32Vector) -> str

"""



class InwUResource:
    # no doc
    def AddStrings(self, directory, primary_locale_code, secondaryy_locale_code):
        """ AddStrings(self: InwUResource, directory: str, primary_locale_code: object, secondaryy_locale_code: object) """
        pass

    def FindString(self, string_name, default_string):
        """ FindString(self: InwUResource, string_name: str, default_string: str) -> str """
        pass

    def HasString(self, string_name):
        """ HasString(self: InwUResource, string_name: str) -> bool """
        pass

    def MakeTempFileName(self, prefix, extension, directoy):
        """ MakeTempFileName(self: InwUResource, prefix: str, extension: str, directoy: object) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CurPrimaryLocaleCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurPrimaryLocaleCode(self: InwUResource) -> str

"""

    CurSecondaryLocaleCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurSecondaryLocaleCode(self: InwUResource) -> str

"""



class InwUResource2(InwUResource):
    # no doc
    def AddStrings(self, directory, primary_locale_code, secondaryy_locale_code):
        """ AddStrings(self: InwUResource2, directory: str, primary_locale_code: object, secondaryy_locale_code: object) """
        pass

    def CleanAutoDeleteDir(self):
        """ CleanAutoDeleteDir(self: InwUResource2) """
        pass

    def FindString(self, string_name, default_string):
        """ FindString(self: InwUResource2, string_name: str, default_string: str) -> str """
        pass

    def HasString(self, string_name):
        """ HasString(self: InwUResource2, string_name: str) -> bool """
        pass

    def MakeTempFileName(self, prefix, extension, directoy):
        """ MakeTempFileName(self: InwUResource2, prefix: str, extension: str, directoy: object) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CurPrimaryLocaleCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurPrimaryLocaleCode(self: InwUResource2) -> str

"""

    CurSecondaryLocaleCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurSecondaryLocaleCode(self: InwUResource2) -> str

"""



class InwURL(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwURL) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwURL, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwURL) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwURL, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwURL) -> str

Set: name(self: InwURL) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwURL) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwURL) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwURL) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwURL) -> int

Set: nwLock(self: InwURL) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwURL) -> bool

Set: nwOwn(self: InwURL) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwURL) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwURL) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwURL) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwURL) -> str

"""

    URL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URL(self: InwURL) -> str

Set: URL(self: InwURL) = value
"""



class InwURL2(InwURL, InwBase):
    # no doc
    def AttachmentPoints(self):
        """ AttachmentPoints(self: InwURL2) -> InwLPos3fColl """
        pass

    def Copy(self):
        """ Copy(self: InwURL2) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwURL2, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwURL2) """
        pass

    def SetCategory(self, user_name, internal_name):
        """ SetCategory(self: InwURL2, user_name: str, internal_name: str) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwURL2, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CategoryInternalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CategoryInternalName(self: InwURL2) -> str

"""

    CategoryUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CategoryUserName(self: InwURL2) -> str

"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: InwURL2) -> str

Set: name(self: InwURL2) = value
"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwURL2) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwURL2) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwURL2) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwURL2) -> int

Set: nwLock(self: InwURL2) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwURL2) -> bool

Set: nwOwn(self: InwURL2) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwURL2) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwURL2) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwURL2) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwURL2) -> str

"""

    URL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URL(self: InwURL2) -> str

Set: URL(self: InwURL2) = value
"""



class InwURLCategoriesColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwURLCategoriesColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwURLCategoriesColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwURLCategoriesColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwURLCategoriesColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwURLCategoriesColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwURLCategoriesColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwURLCategoriesColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwURLCategoriesColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwURLCategoriesColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwURLCategoriesColl) -> bool

"""



class InwURLCategory(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwURLCategory) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwURLCategory, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwURLCategory) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwURLCategory, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DisplayType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayType(self: InwURLCategory) -> nwEURLDisplayType

Set: DisplayType(self: InwURLCategory) = value
"""

    InternalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalName(self: InwURLCategory) -> str

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwURLCategory) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwURLCategory) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwURLCategory) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwURLCategory) -> int

Set: nwLock(self: InwURLCategory) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwURLCategory) -> bool

Set: nwOwn(self: InwURLCategory) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwURLCategory) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwURLCategory) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwURLCategory) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwURLCategory) -> str

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: InwURLCategory) -> str

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: InwURLCategory) -> bool

Set: Visible(self: InwURLCategory) = value
"""



class InwURLColl(InwCollBase, IEnumerable):
    # no doc
    def Add(self, p_newVal):
        """ Add(self: InwURLColl, p_newVal: object) """
        pass

    def Clear(self):
        """ Clear(self: InwURLColl) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InwURLColl) -> IEnumerator """
        pass

    def Insert(self, ndx, p_newVal):
        """ Insert(self: InwURLColl, ndx: int, p_newVal: object) """
        pass

    def Last(self):
        """ Last(self: InwURLColl) -> object """
        pass

    def Remove(self, ndx):
        """ Remove(self: InwURLColl, ndx: int) """
        pass

    def RemoveLast(self):
        """ RemoveLast(self: InwURLColl) """
        pass

    def Replace(self, ndx, p_newVal):
        """ Replace(self: InwURLColl, ndx: int, p_newVal: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: InwURLColl) -> int

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: InwURLColl) -> bool

"""



class InwURLOverride(InwBase):
    # no doc
    def Copy(self):
        """ Copy(self: InwURLOverride) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: InwURLOverride, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: InwURLOverride) """
        pass

    def URLs(self):
        """ URLs(self: InwURLOverride) -> InwURLColl """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: InwURLOverride, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: InwURLOverride) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: InwURLOverride) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: InwURLOverride) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: InwURLOverride) -> int

Set: nwLock(self: InwURLOverride) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: InwURLOverride) -> bool

Set: nwOwn(self: InwURLOverride) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: InwURLOverride) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: InwURLOverride) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: InwURLOverride) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: InwURLOverride) -> str

"""



class InwUtilityObject:
    # no doc
    def GetEnum(self, sName):
        """ GetEnum(self: InwUtilityObject, sName: str) -> int """
        pass

    def ObjectFactory(self, eType, ovReserved1, ovReserved2):
        """ ObjectFactory(self: InwUtilityObject, eType: nwEUtilObjType, ovReserved1: object, ovReserved2: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InwX64:
    # no doc
    def X64Init(self, pointer, lock):
        """ X64Init(self: InwX64, pointer: Int64, lock: Int64) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    X64Lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X64Lock(self: InwX64) -> Int64

Set: X64Lock(self: InwX64) = value
"""

    X64Ptr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X64Ptr(self: InwX64) -> Int64

"""



class InwX64State:
    # no doc
    def X64CreatePlugin(self, progid):
        """ X64CreatePlugin(self: InwX64State, progid: str) -> Int64 """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _InwControlEvents_Event:
    # no doc
# Error generating skeleton for function add_OnCertificateDownload: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnContextMenu: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnContextMenuEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnEnableContextMenuCmd: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnEnableContextMenuCmdEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnEnableUserNavMode: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnEnableUserNavModeEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnFileDownload: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnFileError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnFileOpen: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnKeyDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnKeyDownEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnKeyUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnKeyUpEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnLButtonDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnLButtonUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnMButtonDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnMButtonUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnMouseMove: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnMouseWheel: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnNavModeChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnOutOfMemory: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnProgressError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnProgressPublished: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnSecurityChecked: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnSecurityError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnUserContextMenuCmd: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnXRefResolve: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnCertificateDownload: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnContextMenu: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnContextMenuEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnEnableContextMenuCmd: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnEnableContextMenuCmdEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnEnableUserNavMode: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnEnableUserNavModeEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnFileDownload: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnFileError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnFileOpen: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnKeyDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnKeyDownEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnKeyUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnKeyUpEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnLButtonDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnLButtonUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnMButtonDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnMButtonUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnMouseMove: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnMouseWheel: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnNavModeChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnOutOfMemory: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnProgressError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnProgressPublished: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnSecurityChecked: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnSecurityError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnUserContextMenuCmd: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnXRefResolve: sequence item 1: expected string, NoneType found

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    OnCertificateDownload = None
    OnContextMenu = None
    OnContextMenuEx = None
    OnEnableContextMenuCmd = None
    OnEnableContextMenuCmdEx = None
    OnEnableUserNavMode = None
    OnEnableUserNavModeEx = None
    OnFileDownload = None
    OnFileError = None
    OnFileOpen = None
    OnKeyDown = None
    OnKeyDownEx = None
    OnKeyUp = None
    OnKeyUpEx = None
    OnLButtonDown = None
    OnLButtonUp = None
    OnMButtonDown = None
    OnMButtonUp = None
    OnMouseMove = None
    OnMouseWheel = None
    OnNavModeChanged = None
    OnOutOfMemory = None
    OnProgressError = None
    OnProgressPublished = None
    OnSecurityChecked = None
    OnSecurityError = None
    OnUserContextMenuCmd = None
    OnXRefResolve = None


class nwControlMDI(InwControl5, InwControl4, InwControl3, InwControl2, InwControl, _InwControlEvents_Event):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class nwControlMDIClass(__ComObject, InwControl5, InwControl4, InwControl3, InwControl2, InwControl, nwControlMDI, _InwControlEvents_Event):
    """ nwControlMDIClass() """
# Error generating skeleton for function add_OnCertificateDownload: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnContextMenu: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnContextMenuEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnEnableContextMenuCmd: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnEnableContextMenuCmdEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnEnableUserNavMode: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnEnableUserNavModeEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnFileDownload: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnFileError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnFileOpen: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnKeyDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnKeyDownEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnKeyUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnKeyUpEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnLButtonDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnLButtonUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnMButtonDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnMButtonUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnMouseMove: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnMouseWheel: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnNavModeChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnOutOfMemory: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnProgressError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnProgressPublished: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnSecurityChecked: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnSecurityError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnUserContextMenuCmd: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnXRefResolve: sequence item 1: expected string, NoneType found

    def AnimationCommand(self, cmd):
        """ AnimationCommand(self: nwControlMDIClass, cmd: nwEAnimationCmd) -> nwEAnimCmdFlags """
        pass

    def AppendFile(self, file_name):
        """ AppendFile(self: nwControlMDIClass, file_name: str) """
        pass

    def AppendFile_As(self, file_name, file_type):
        """ AppendFile_As(self: nwControlMDIClass, file_name: str, file_type: nwEFileAsType) """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A 
             value of lse is usually appropriate. ue to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the 
             remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def PickPixel(self, x, y, width, Flags, pos1, pos2, pos3):
        """ PickPixel(self: nwControlMDIClass, x: int, y: int, width: int, Flags: nwEPickFlags) -> (InwOaFragment, object, object, object) """
        pass

# Error generating skeleton for function remove_OnCertificateDownload: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnContextMenu: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnContextMenuEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnEnableContextMenuCmd: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnEnableContextMenuCmdEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnEnableUserNavMode: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnEnableUserNavModeEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnFileDownload: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnFileError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnFileOpen: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnKeyDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnKeyDownEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnKeyUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnKeyUpEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnLButtonDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnLButtonUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnMButtonDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnMButtonUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnMouseMove: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnMouseWheel: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnNavModeChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnOutOfMemory: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnProgressError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnProgressPublished: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnSecurityChecked: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnSecurityError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnUserContextMenuCmd: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnXRefResolve: sequence item 1: expected string, NoneType found

    def SaveFile(self, file_name):
        """ SaveFile(self: nwControlMDIClass, file_name: str) """
        pass

    def SaveFile_As(self, file_name, file_type):
        """ SaveFile_As(self: nwControlMDIClass, file_name: str, file_type: nwEFileAsType) """
        pass

    def SRC_As(self, file_name, file_type):
        """ SRC_As(self: nwControlMDIClass, file_name: str, file_type: nwEFileAsType) """
        pass

    def SyncAppendFile(self, file_name):
        """ SyncAppendFile(self: nwControlMDIClass, file_name: str) """
        pass

    def SyncAppendFile_As(self, file_name, file_type):
        """ SyncAppendFile_As(self: nwControlMDIClass, file_name: str, file_type: nwEFileAsType) """
        pass

    def SyncSRC(self, file_name):
        """ SyncSRC(self: nwControlMDIClass, file_name: str) """
        pass

    def SyncSRC_As(self, file_name, file_type):
        """ SyncSRC_As(self: nwControlMDIClass, file_name: str, file_type: nwEFileAsType) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: nwControlMDIClass, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    APIState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: APIState(self: nwControlMDIClass) -> InwOpState

"""

    AutoSetFocusMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSetFocusMode(self: nwControlMDIClass) -> bool

Set: AutoSetFocusMode(self: nwControlMDIClass) = value
"""

    ForceEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForceEvents(self: nwControlMDIClass) -> bool

Set: ForceEvents(self: nwControlMDIClass) = value
"""

    HighlightSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighlightSelection(self: nwControlMDIClass) -> bool

Set: HighlightSelection(self: nwControlMDIClass) = value
"""

    LocalisationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalisationCode(self: nwControlMDIClass) -> str

Set: LocalisationCode(self: nwControlMDIClass) = value
"""

    NavigationMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NavigationMode(self: nwControlMDIClass) -> nwENavigationMode

Set: NavigationMode(self: nwControlMDIClass) = value
"""

    ProgressMsg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProgressMsg(self: nwControlMDIClass) -> str

Set: ProgressMsg(self: nwControlMDIClass) = value
"""

    SecurityCertificate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecurityCertificate(self: nwControlMDIClass) -> str

Set: SecurityCertificate(self: nwControlMDIClass) = value
"""

    SelectionBehaviour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionBehaviour(self: nwControlMDIClass) -> nwESelectionBehaviour

Set: SelectionBehaviour(self: nwControlMDIClass) = value
"""

    ShowProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowProgress(self: nwControlMDIClass) -> bool

Set: ShowProgress(self: nwControlMDIClass) = value
"""

    SRC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SRC(self: nwControlMDIClass) -> str

Set: SRC(self: nwControlMDIClass) = value
"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: nwControlMDIClass) -> InwOpState

"""

    UserModeSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserModeSelection(self: nwControlMDIClass) -> bool

Set: UserModeSelection(self: nwControlMDIClass) = value
"""

    _State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: _State(self: nwControlMDIClass) -> str

Set: _State(self: nwControlMDIClass) = value
"""


    OnCertificateDownload = None
    OnContextMenu = None
    OnContextMenuEx = None
    OnEnableContextMenuCmd = None
    OnEnableContextMenuCmdEx = None
    OnEnableUserNavMode = None
    OnEnableUserNavModeEx = None
    OnFileDownload = None
    OnFileError = None
    OnFileOpen = None
    OnKeyDown = None
    OnKeyDownEx = None
    OnKeyUp = None
    OnKeyUpEx = None
    OnLButtonDown = None
    OnLButtonUp = None
    OnMButtonDown = None
    OnMButtonUp = None
    OnMouseMove = None
    OnMouseWheel = None
    OnNavModeChanged = None
    OnOutOfMemory = None
    OnProgressError = None
    OnProgressPublished = None
    OnSecurityChecked = None
    OnSecurityError = None
    OnUserContextMenuCmd = None
    OnXRefResolve = None


class nwControlProp:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class nwControlPropClass(__ComObject, nwControlProp):
    """ nwControlPropClass() """
    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A 
             value of lse is usually appropriate. ue to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the 
             remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class nwControlSDI(InwControl5, InwControl4, InwControl3, InwControl2, InwControl, _InwControlEvents_Event):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class nwControlSDIClass(__ComObject, InwControl5, InwControl4, InwControl3, InwControl2, InwControl, nwControlSDI, _InwControlEvents_Event):
    """ nwControlSDIClass() """
# Error generating skeleton for function add_OnCertificateDownload: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnContextMenu: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnContextMenuEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnEnableContextMenuCmd: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnEnableContextMenuCmdEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnEnableUserNavMode: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnEnableUserNavModeEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnFileDownload: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnFileError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnFileOpen: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnKeyDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnKeyDownEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnKeyUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnKeyUpEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnLButtonDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnLButtonUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnMButtonDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnMButtonUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnMouseMove: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnMouseWheel: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnNavModeChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnOutOfMemory: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnProgressError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnProgressPublished: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnSecurityChecked: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnSecurityError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnUserContextMenuCmd: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnXRefResolve: sequence item 1: expected string, NoneType found

    def AnimationCommand(self, cmd):
        """ AnimationCommand(self: nwControlSDIClass, cmd: nwEAnimationCmd) -> nwEAnimCmdFlags """
        pass

    def AppendFile(self, file_name):
        """ AppendFile(self: nwControlSDIClass, file_name: str) """
        pass

    def AppendFile_As(self, file_name, file_type):
        """ AppendFile_As(self: nwControlSDIClass, file_name: str, file_type: nwEFileAsType) """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A 
             value of lse is usually appropriate. ue to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the 
             remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def PickPixel(self, x, y, width, Flags, pos1, pos2, pos3):
        """ PickPixel(self: nwControlSDIClass, x: int, y: int, width: int, Flags: nwEPickFlags) -> (InwOaFragment, object, object, object) """
        pass

# Error generating skeleton for function remove_OnCertificateDownload: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnContextMenu: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnContextMenuEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnEnableContextMenuCmd: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnEnableContextMenuCmdEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnEnableUserNavMode: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnEnableUserNavModeEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnFileDownload: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnFileError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnFileOpen: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnKeyDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnKeyDownEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnKeyUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnKeyUpEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnLButtonDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnLButtonUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnMButtonDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnMButtonUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnMouseMove: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnMouseWheel: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnNavModeChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnOutOfMemory: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnProgressError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnProgressPublished: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnSecurityChecked: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnSecurityError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnUserContextMenuCmd: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnXRefResolve: sequence item 1: expected string, NoneType found

    def SaveFile(self, file_name):
        """ SaveFile(self: nwControlSDIClass, file_name: str) """
        pass

    def SaveFile_As(self, file_name, file_type):
        """ SaveFile_As(self: nwControlSDIClass, file_name: str, file_type: nwEFileAsType) """
        pass

    def SRC_As(self, file_name, file_type):
        """ SRC_As(self: nwControlSDIClass, file_name: str, file_type: nwEFileAsType) """
        pass

    def SyncAppendFile(self, file_name):
        """ SyncAppendFile(self: nwControlSDIClass, file_name: str) """
        pass

    def SyncAppendFile_As(self, file_name, file_type):
        """ SyncAppendFile_As(self: nwControlSDIClass, file_name: str, file_type: nwEFileAsType) """
        pass

    def SyncSRC(self, file_name):
        """ SyncSRC(self: nwControlSDIClass, file_name: str) """
        pass

    def SyncSRC_As(self, file_name, file_type):
        """ SyncSRC_As(self: nwControlSDIClass, file_name: str, file_type: nwEFileAsType) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: nwControlSDIClass, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    APIState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: APIState(self: nwControlSDIClass) -> InwOpState

"""

    AutoSetFocusMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSetFocusMode(self: nwControlSDIClass) -> bool

Set: AutoSetFocusMode(self: nwControlSDIClass) = value
"""

    ForceEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForceEvents(self: nwControlSDIClass) -> bool

Set: ForceEvents(self: nwControlSDIClass) = value
"""

    HighlightSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighlightSelection(self: nwControlSDIClass) -> bool

Set: HighlightSelection(self: nwControlSDIClass) = value
"""

    LocalisationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalisationCode(self: nwControlSDIClass) -> str

Set: LocalisationCode(self: nwControlSDIClass) = value
"""

    NavigationMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NavigationMode(self: nwControlSDIClass) -> nwENavigationMode

Set: NavigationMode(self: nwControlSDIClass) = value
"""

    ProgressMsg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProgressMsg(self: nwControlSDIClass) -> str

Set: ProgressMsg(self: nwControlSDIClass) = value
"""

    SecurityCertificate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecurityCertificate(self: nwControlSDIClass) -> str

Set: SecurityCertificate(self: nwControlSDIClass) = value
"""

    SelectionBehaviour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionBehaviour(self: nwControlSDIClass) -> nwESelectionBehaviour

Set: SelectionBehaviour(self: nwControlSDIClass) = value
"""

    ShowProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowProgress(self: nwControlSDIClass) -> bool

Set: ShowProgress(self: nwControlSDIClass) = value
"""

    SRC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SRC(self: nwControlSDIClass) -> str

Set: SRC(self: nwControlSDIClass) = value
"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: nwControlSDIClass) -> InwOpState

"""

    UserModeSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserModeSelection(self: nwControlSDIClass) -> bool

Set: UserModeSelection(self: nwControlSDIClass) = value
"""

    _State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: _State(self: nwControlSDIClass) -> str

Set: _State(self: nwControlSDIClass) = value
"""


    OnCertificateDownload = None
    OnContextMenu = None
    OnContextMenuEx = None
    OnEnableContextMenuCmd = None
    OnEnableContextMenuCmdEx = None
    OnEnableUserNavMode = None
    OnEnableUserNavModeEx = None
    OnFileDownload = None
    OnFileError = None
    OnFileOpen = None
    OnKeyDown = None
    OnKeyDownEx = None
    OnKeyUp = None
    OnKeyUpEx = None
    OnLButtonDown = None
    OnLButtonUp = None
    OnMButtonDown = None
    OnMButtonUp = None
    OnMouseMove = None
    OnMouseWheel = None
    OnNavModeChanged = None
    OnOutOfMemory = None
    OnProgressError = None
    OnProgressPublished = None
    OnSecurityChecked = None
    OnSecurityError = None
    OnUserContextMenuCmd = None
    OnXRefResolve = None


class nwEAngularUnits(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEAngularUnits, values: eAngularUnits_DEGREES (0), eAngularUnits_RADIANS (1) """
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

    eAngularUnits_DEGREES = None
    eAngularUnits_RADIANS = None
    value__ = None


class nwEAnimationCmd(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEAnimationCmd, values: eCmd_Erase (9), eCmd_FForward (8), eCmd_Pause (4), eCmd_Play (6), eCmd_Record (3), eCmd_ReversePlay (2), eCmd_Rewind (0), eCmd_StepBack (1), eCmd_StepForward (7), eCmd_Stop (5), eCmd_UpdateErase (19), eCmd_UpdateFForward (18), eCmd_UpdatePause (14), eCmd_UpdatePlay (16), eCmd_UpdateRecord (13), eCmd_UpdateReversePlay (12), eCmd_UpdateRewind (10), eCmd_UpdateStepBack (11), eCmd_UpdateStepForward (17), eCmd_UpdateStop (15) """
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

    eCmd_Erase = None
    eCmd_FForward = None
    eCmd_Pause = None
    eCmd_Play = None
    eCmd_Record = None
    eCmd_ReversePlay = None
    eCmd_Rewind = None
    eCmd_StepBack = None
    eCmd_StepForward = None
    eCmd_Stop = None
    eCmd_UpdateErase = None
    eCmd_UpdateFForward = None
    eCmd_UpdatePause = None
    eCmd_UpdatePlay = None
    eCmd_UpdateRecord = None
    eCmd_UpdateReversePlay = None
    eCmd_UpdateRewind = None
    eCmd_UpdateStepBack = None
    eCmd_UpdateStepForward = None
    eCmd_UpdateStop = None
    value__ = None


class nwEAnimCmdFlags(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEAnimCmdFlags, values: eAnim_Disabled (2), eAnim_Enabled (1), eAnim_StatusChecked (4), eAnim_StatusNone (16), eAnim_StatusUnchecked (8) """
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

    eAnim_Disabled = None
    eAnim_Enabled = None
    eAnim_StatusChecked = None
    eAnim_StatusNone = None
    eAnim_StatusUnchecked = None
    value__ = None


class nwEAnimSmoothing(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEAnimSmoothing, values: eAnimSmoothing_NONE (0), eAnimSmoothing_SPLINE (2), eAnimSmoothing_SYNC (1) """
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

    eAnimSmoothing_NONE = None
    eAnimSmoothing_SPLINE = None
    eAnimSmoothing_SYNC = None
    value__ = None


class nwECameraMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwECameraMode, values: eCameraMode_FirstPerson (0), eCameraMode_ThirdPerson (1) """
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

    eCameraMode_FirstPerson = None
    eCameraMode_ThirdPerson = None
    value__ = None


class nwECanTake(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwECanTake, values: eCanTake_CONTENTS_PROPERTIES (2), eCanTake_CONTENTS_TEXT (1), eCanTake_DEFAULT (0) """
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

    eCanTake_CONTENTS_PROPERTIES = None
    eCanTake_CONTENTS_TEXT = None
    eCanTake_DEFAULT = None
    value__ = None


class nwECaps(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwECaps, values: eCap_BACKGROUND (32), eCap_CACHE_IN_FILE (256), eCap_CLASH_IGNORE (1), eCap_CLASH_IGNORE_SLOW (2), eCap_COMMENT_BOUNDS (4), eCap_COMMENT_IMAGELIST (1), eCap_COMMENT_POSITION (2), eCap_CUSTOM_OPTION (536870912), eCap_DONT_CACHE (512), eCap_EXPORT_CONTEXT_ITEM (4), eCap_EXPORT_DIALOG (512), eCap_EXPORT_EXPLICIT (2), eCap_EXPORT_HELP (1024), eCap_EXPORT_PROGRESS (1), eCap_EXPORT_TO_FILE (128), eCap_EXPORT_TOOL (256), eCap_EXTERNAL_CACHE (128), eCap_IGNORE_LOAD_ERROR (33554432), eCap_INITIAL_VIEW (2048), eCap_LOAD (1), eCap_LOAD_PROGRESS (4), eCap_NO_DELAY (268435456), eCap_NO_USER_PARAMS (1073741824), eCap_OPTIONAL_PLUGIN (67108864), eCap_POLICY_BACKGROUND (1), eCap_POLICY_LIGHTS (2), eCap_POLICY_PRIORITY (4), eCap_PROPERTY_NAME (1), eCap_PROPERTY_TEXT (2), eCap_PROPERTY2_ADD (2), eCap_PROPERTY2_CLASS (1), eCap_PROPERTY2_NAME (4), eCap_PROPERTY2_PROPS (8), eCap_PROPERTY2_REPLACE (16), eCap_RENDER (64), eCap_REQUIRED_PLUGIN (16777216), eCap_RESOLVE_XREFS (16), eCap_SAVE (2), eCap_SAVE_PROGRESS (8), eCap_SCENE_XREFS (1024) """
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

    eCap_BACKGROUND = None
    eCap_CACHE_IN_FILE = None
    eCap_CLASH_IGNORE = None
    eCap_CLASH_IGNORE_SLOW = None
    eCap_COMMENT_BOUNDS = None
    eCap_COMMENT_IMAGELIST = None
    eCap_COMMENT_POSITION = None
    eCap_CUSTOM_OPTION = None
    eCap_DONT_CACHE = None
    eCap_EXPORT_CONTEXT_ITEM = None
    eCap_EXPORT_DIALOG = None
    eCap_EXPORT_EXPLICIT = None
    eCap_EXPORT_HELP = None
    eCap_EXPORT_PROGRESS = None
    eCap_EXPORT_TOOL = None
    eCap_EXPORT_TO_FILE = None
    eCap_EXTERNAL_CACHE = None
    eCap_IGNORE_LOAD_ERROR = None
    eCap_INITIAL_VIEW = None
    eCap_LOAD = None
    eCap_LOAD_PROGRESS = None
    eCap_NO_DELAY = None
    eCap_NO_USER_PARAMS = None
    eCap_OPTIONAL_PLUGIN = None
    eCap_POLICY_BACKGROUND = None
    eCap_POLICY_LIGHTS = None
    eCap_POLICY_PRIORITY = None
    eCap_PROPERTY2_ADD = None
    eCap_PROPERTY2_CLASS = None
    eCap_PROPERTY2_NAME = None
    eCap_PROPERTY2_PROPS = None
    eCap_PROPERTY2_REPLACE = None
    eCap_PROPERTY_NAME = None
    eCap_PROPERTY_TEXT = None
    eCap_RENDER = None
    eCap_REQUIRED_PLUGIN = None
    eCap_RESOLVE_XREFS = None
    eCap_SAVE = None
    eCap_SAVE_PROGRESS = None
    eCap_SCENE_XREFS = None
    value__ = None


class nwEClashIgnore(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEClashIgnore, values: eIgnore_CUSTOM_01 (16), eIgnore_CUSTOM_02 (32), eIgnore_CUSTOM_03 (64), eIgnore_CUSTOM_04 (128), eIgnore_CUSTOM_05 (256), eIgnore_CUSTOM_06 (512), eIgnore_CUSTOM_07 (1024), eIgnore_CUSTOM_08 (2048), eIgnore_CUSTOM_09 (4096), eIgnore_CUSTOM_10 (8192), eIgnore_GROUP (8), eIgnore_LAYER (2), eIgnore_NONE (0), eIgnore_PARTITION (4) """
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

    eIgnore_CUSTOM_01 = None
    eIgnore_CUSTOM_02 = None
    eIgnore_CUSTOM_03 = None
    eIgnore_CUSTOM_04 = None
    eIgnore_CUSTOM_05 = None
    eIgnore_CUSTOM_06 = None
    eIgnore_CUSTOM_07 = None
    eIgnore_CUSTOM_08 = None
    eIgnore_CUSTOM_09 = None
    eIgnore_CUSTOM_10 = None
    eIgnore_GROUP = None
    eIgnore_LAYER = None
    eIgnore_NONE = None
    eIgnore_PARTITION = None
    value__ = None


class nwEClashTestIntersectionMethod(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEClashTestIntersectionMethod, values: eMETHOD_FACET (0), eMETHOD_FACET_TOUCH (1), eMETHOD_MESH (2) """
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

    eMETHOD_FACET = None
    eMETHOD_FACET_TOUCH = None
    eMETHOD_MESH = None
    value__ = None


class nwEClashTestStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEClashTestStatus, values: eClashTestStatus_NEW (0), eClashTestStatus_NUM (4), eClashTestStatus_OK (3), eClashTestStatus_OLD (1), eClashTestStatus_PARTIAL (2) """
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

    eClashTestStatus_NEW = None
    eClashTestStatus_NUM = None
    eClashTestStatus_OK = None
    eClashTestStatus_OLD = None
    eClashTestStatus_PARTIAL = None
    value__ = None


class nwEClashTestToleranceType(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEClashTestToleranceType, values: eTOLERANCE_CLEARANCE (1), eTOLERANCE_HARD (0), eTOLERANCE_NUM (2) """
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

    eTOLERANCE_CLEARANCE = None
    eTOLERANCE_HARD = None
    eTOLERANCE_NUM = None
    value__ = None


class nwEClashTestType(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEClashTestType, values: eClashTestType_CLEARANCE (2), eClashTestType_CUSTOM (4), eClashTestType_DUPLICATE (3), eClashTestType_HARD (0), eClashTestType_HARD_CONSERVATIVE (1) """
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

    eClashTestType_CLEARANCE = None
    eClashTestType_CUSTOM = None
    eClashTestType_DUPLICATE = None
    eClashTestType_HARD = None
    eClashTestType_HARD_CONSERVATIVE = None
    value__ = None


class nwEClipPlaneAlignment(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEClipPlaneAlignment, values: eAlignment_BACK (2), eAlignment_BOTTOM (7), eAlignment_FRONT (3), eAlignment_LEFT (4), eAlignment_NONE (0), eAlignment_RIGHT (5), eAlignment_TOP (6), eAlignment_VIEW (1) """
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

    eAlignment_BACK = None
    eAlignment_BOTTOM = None
    eAlignment_FRONT = None
    eAlignment_LEFT = None
    eAlignment_NONE = None
    eAlignment_RIGHT = None
    eAlignment_TOP = None
    eAlignment_VIEW = None
    value__ = None


class nwECommentStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwECommentStatus, values: eCommentStatus_ACTIVE (1), eCommentStatus_APPROVED (2), eCommentStatus_NEW (0), eCommentStatus_RESOLVED (3) """
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

    eCommentStatus_ACTIVE = None
    eCommentStatus_APPROVED = None
    eCommentStatus_NEW = None
    eCommentStatus_RESOLVED = None
    value__ = None


class nwEExportStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEExportStatus, values: eExport_CANCELED (5), eExport_CANT_OPEN (1), eExport_FAIL (3), eExport_NA (6), eExport_NO_ROOM (2), eExport_OK (0), eExport_UNIMPLEMENTED (4) """
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

    eExport_CANCELED = None
    eExport_CANT_OPEN = None
    eExport_FAIL = None
    eExport_NA = None
    eExport_NO_ROOM = None
    eExport_OK = None
    eExport_UNIMPLEMENTED = None
    value__ = None


class nwEFileAction(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEFileAction, values: eFileAction_CERTIFICATE_FAIL_DOWNLOAD (5), eFileAction_CERTIFICATE_FAIL_FILENAME (6), eFileAction_FAIL_BAD_VERSION (11), eFileAction_FAIL_CANCELED (13), eFileAction_FAIL_DOWNLOAD (1), eFileAction_FAIL_FILE_CORRUPT (9), eFileAction_FAIL_FILENAME (3), eFileAction_FAIL_FREE_VIEWER_OLD_FILE (14), eFileAction_FAIL_OPEN (4), eFileAction_FAIL_SECURITY (0), eFileAction_FAIL_STILL_DOWNLOADING (2), eFileAction_FAIL_UNIMPLEMENTED (12), eFileAction_FAIL_UNSUPPORTED (10), eFileAction_SAVE_FAILED (8), eFileAction_SAVE_REFUSED (7) """
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

    eFileAction_CERTIFICATE_FAIL_DOWNLOAD = None
    eFileAction_CERTIFICATE_FAIL_FILENAME = None
    eFileAction_FAIL_BAD_VERSION = None
    eFileAction_FAIL_CANCELED = None
    eFileAction_FAIL_DOWNLOAD = None
    eFileAction_FAIL_FILENAME = None
    eFileAction_FAIL_FILE_CORRUPT = None
    eFileAction_FAIL_FREE_VIEWER_OLD_FILE = None
    eFileAction_FAIL_OPEN = None
    eFileAction_FAIL_SECURITY = None
    eFileAction_FAIL_STILL_DOWNLOADING = None
    eFileAction_FAIL_UNIMPLEMENTED = None
    eFileAction_FAIL_UNSUPPORTED = None
    eFileAction_SAVE_FAILED = None
    eFileAction_SAVE_REFUSED = None
    value__ = None


class nwEFileAsType(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEFileAsType, values: eFileType_AUTO (0), eFileType_NWC (1), eFileType_NWD (2), eFileType_NWF (3) """
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

    eFileType_AUTO = None
    eFileType_NWC = None
    eFileType_NWD = None
    eFileType_NWF = None
    value__ = None


class nwEFindCondition(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEFindCondition, values: eFind_CONTAINS (12), eFind_EQUAL (6), eFind_FIND_NEVER (0), eFind_GE (10), eFind_GT (11), eFind_HAS_ATTRIB (1), eFind_HAS_NO_ATTRIB (2), eFind_HAS_NO_PROP (4), eFind_HAS_PROP (3), eFind_LE (9), eFind_LT (8), eFind_NOT_EQUAL (7), eFind_SAME_TYPE (5), eFind_WILDCARD (13), eFind_WITHIN_DAY (14), eFind_WITHIN_WEEK (15) """
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

    eFind_CONTAINS = None
    eFind_EQUAL = None
    eFind_FIND_NEVER = None
    eFind_GE = None
    eFind_GT = None
    eFind_HAS_ATTRIB = None
    eFind_HAS_NO_ATTRIB = None
    eFind_HAS_NO_PROP = None
    eFind_HAS_PROP = None
    eFind_LE = None
    eFind_LT = None
    eFind_NOT_EQUAL = None
    eFind_SAME_TYPE = None
    eFind_WILDCARD = None
    eFind_WITHIN_DAY = None
    eFind_WITHIN_WEEK = None
    value__ = None


class nwELighting(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwELighting, values: eLighting_FULL_LIGHTING (3), eLighting_HEAD_LIGHTING (2), eLighting_NO_LIGHTING (0), eLighting_NUM_LIGHTING (4), eLighting_USER_LIGHTING (1) """
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

    eLighting_FULL_LIGHTING = None
    eLighting_HEAD_LIGHTING = None
    eLighting_NO_LIGHTING = None
    eLighting_NUM_LIGHTING = None
    eLighting_USER_LIGHTING = None
    value__ = None


class nwELinearUnits(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwELinearUnits, values: eLinearUnits_CENTIMETRES (1), eLinearUnits_FEET (3), eLinearUnits_INCHES (4), eLinearUnits_METRES (0), eLinearUnits_MILLIMETRES (2) """
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

    eLinearUnits_CENTIMETRES = None
    eLinearUnits_FEET = None
    eLinearUnits_INCHES = None
    eLinearUnits_METRES = None
    eLinearUnits_MILLIMETRES = None
    value__ = None


class nwENavigationMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwENavigationMode, values: eNavigationMode_ADV_SELECT_BOX (100), eNavigationMode_AUTOCAM_CENTER (509), eNavigationMode_AUTOCAM_LOOK_AROUND (507), eNavigationMode_AUTOCAM_LOOK_AT (506), eNavigationMode_AUTOCAM_ORBIT (503), eNavigationMode_AUTOCAM_ORBIT_CONSTRAINED (505), eNavigationMode_AUTOCAM_ORBIT_FREE (504), eNavigationMode_AUTOCAM_PAN (500), eNavigationMode_AUTOCAM_WALK (508), eNavigationMode_AUTOCAM_ZOOM (501), eNavigationMode_AUTOCAM_ZOOM_WINDOW (502), eNavigationMode_Custom (5), eNavigationMode_MEASURE_ACCUMULATIVE_POINTS (303), eNavigationMode_MEASURE_ANGLE (304), eNavigationMode_MEASURE_AREA (305), eNavigationMode_MEASURE_POINT_STRING (302), eNavigationMode_MEASURE_POINT_TO_MANY_POINTS (301), eNavigationMode_MEASURE_POINT_TO_POINT (300), eNavigationMode_NONE (-1), eNavigationMode_Normal (0), eNavigationMode_REDLINE_ARROW (208), eNavigationMode_REDLINE_CLOUD (203), eNavigationMode_REDLINE_ELLIPSE (202), eNavigationMode_REDLINE_ERASE (207), eNavigationMode_REDLINE_LINE (201), eNavigationMode_REDLINE_LINESTRING (204), eNavigationMode_REDLINE_PEN (200), eNavigationMode_REDLINE_TAG (205), eNavigationMode_REDLINE_TEXT (206), eNavigationMode_Select (1), eNavigationMode_User1 (2), eNavigationMode_User2 (3), eNavigationMode_User3 (4), eNavigationMode_WHEEL_2D (406), eNavigationMode_WHEEL_FULL_NAVIGATION (402), eNavigationMode_WHEEL_MINI_FULL_NAVIGATION (405), eNavigationMode_WHEEL_MINI_TOUR_BUILDING (404), eNavigationMode_WHEEL_MINI_VIEW_OBJECT (403), eNavigationMode_WHEEL_TOUR_BUILDING (401), eNavigationMode_WHEEL_VIEW_OBJECT (400) """
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

    eNavigationMode_ADV_SELECT_BOX = None
    eNavigationMode_AUTOCAM_CENTER = None
    eNavigationMode_AUTOCAM_LOOK_AROUND = None
    eNavigationMode_AUTOCAM_LOOK_AT = None
    eNavigationMode_AUTOCAM_ORBIT = None
    eNavigationMode_AUTOCAM_ORBIT_CONSTRAINED = None
    eNavigationMode_AUTOCAM_ORBIT_FREE = None
    eNavigationMode_AUTOCAM_PAN = None
    eNavigationMode_AUTOCAM_WALK = None
    eNavigationMode_AUTOCAM_ZOOM = None
    eNavigationMode_AUTOCAM_ZOOM_WINDOW = None
    eNavigationMode_Custom = None
    eNavigationMode_MEASURE_ACCUMULATIVE_POINTS = None
    eNavigationMode_MEASURE_ANGLE = None
    eNavigationMode_MEASURE_AREA = None
    eNavigationMode_MEASURE_POINT_STRING = None
    eNavigationMode_MEASURE_POINT_TO_MANY_POINTS = None
    eNavigationMode_MEASURE_POINT_TO_POINT = None
    eNavigationMode_NONE = None
    eNavigationMode_Normal = None
    eNavigationMode_REDLINE_ARROW = None
    eNavigationMode_REDLINE_CLOUD = None
    eNavigationMode_REDLINE_ELLIPSE = None
    eNavigationMode_REDLINE_ERASE = None
    eNavigationMode_REDLINE_LINE = None
    eNavigationMode_REDLINE_LINESTRING = None
    eNavigationMode_REDLINE_PEN = None
    eNavigationMode_REDLINE_TAG = None
    eNavigationMode_REDLINE_TEXT = None
    eNavigationMode_Select = None
    eNavigationMode_User1 = None
    eNavigationMode_User2 = None
    eNavigationMode_User3 = None
    eNavigationMode_WHEEL_2D = None
    eNavigationMode_WHEEL_FULL_NAVIGATION = None
    eNavigationMode_WHEEL_MINI_FULL_NAVIGATION = None
    eNavigationMode_WHEEL_MINI_TOUR_BUILDING = None
    eNavigationMode_WHEEL_MINI_VIEW_OBJECT = None
    eNavigationMode_WHEEL_TOUR_BUILDING = None
    eNavigationMode_WHEEL_VIEW_OBJECT = None
    value__ = None


class nwEObjectType(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEObjectType, values: eObjectType_nwLBox3f (1), eObjectType_nwLPlane3f (15), eObjectType_nwLPos3f (2), eObjectType_nwLRotation3f (12), eObjectType_nwLTransform3f (24), eObjectType_nwLUnitVec3f (14), eObjectType_nwLVec3f (3), eObjectType_nwNvCamera (5), eObjectType_nwNvViewPoint (4), eObjectType_nwOaClipPlane (13), eObjectType_nwOaDistantLight (23), eObjectType_nwOaMaterial (29), eObjectType_nwOaNameAttribute (26), eObjectType_nwOaNat64Attribute (25), eObjectType_nwOaPath (17), eObjectType_nwOaPointLight (22), eObjectType_nwOaProperty (20), eObjectType_nwOaPropertyAttribute (30), eObjectType_nwOaPropertyVec (39), eObjectType_nwOaPublishAttribute (40), eObjectType_nwOaSpotLight (21), eObjectType_nwOaTextAttribute (27), eObjectType_nwOaURLAttribute (28), eObjectType_nwOclClashTest (19), eObjectType_nwOpAnimView (6), eObjectType_nwOpAnonView (7), eObjectType_nwOpComment (8), eObjectType_nwOpCutView (9), eObjectType_nwOpFind (31), eObjectType_nwOpFindCondition (32), eObjectType_nwOpFindSpec (33), eObjectType_nwOpFolderView (10), eObjectType_nwOpSelection (18), eObjectType_nwOpSelectionSet (16), eObjectType_nwOpSelectionSetFolder (41), eObjectType_nwOpUserFindSpec (35), eObjectType_nwOpUserSelectionTreeSpec (34), eObjectType_nwOpView (11), eObjectType_nwSmartTagsOpts (38), eObjectType_nwURL (36), eObjectType_nwURLOverride (37), eObjectType_Reserved (0) """
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

    eObjectType_nwLBox3f = None
    eObjectType_nwLPlane3f = None
    eObjectType_nwLPos3f = None
    eObjectType_nwLRotation3f = None
    eObjectType_nwLTransform3f = None
    eObjectType_nwLUnitVec3f = None
    eObjectType_nwLVec3f = None
    eObjectType_nwNvCamera = None
    eObjectType_nwNvViewPoint = None
    eObjectType_nwOaClipPlane = None
    eObjectType_nwOaDistantLight = None
    eObjectType_nwOaMaterial = None
    eObjectType_nwOaNameAttribute = None
    eObjectType_nwOaNat64Attribute = None
    eObjectType_nwOaPath = None
    eObjectType_nwOaPointLight = None
    eObjectType_nwOaProperty = None
    eObjectType_nwOaPropertyAttribute = None
    eObjectType_nwOaPropertyVec = None
    eObjectType_nwOaPublishAttribute = None
    eObjectType_nwOaSpotLight = None
    eObjectType_nwOaTextAttribute = None
    eObjectType_nwOaURLAttribute = None
    eObjectType_nwOclClashTest = None
    eObjectType_nwOpAnimView = None
    eObjectType_nwOpAnonView = None
    eObjectType_nwOpComment = None
    eObjectType_nwOpCutView = None
    eObjectType_nwOpFind = None
    eObjectType_nwOpFindCondition = None
    eObjectType_nwOpFindSpec = None
    eObjectType_nwOpFolderView = None
    eObjectType_nwOpSelection = None
    eObjectType_nwOpSelectionSet = None
    eObjectType_nwOpSelectionSetFolder = None
    eObjectType_nwOpUserFindSpec = None
    eObjectType_nwOpUserSelectionTreeSpec = None
    eObjectType_nwOpView = None
    eObjectType_nwSmartTagsOpts = None
    eObjectType_nwURL = None
    eObjectType_nwURLOverride = None
    eObjectType_Reserved = None
    value__ = None


class nwEParadigm(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEParadigm, values: eParadigm_APPLICATION (6), eParadigm_EXAMINE (2), eParadigm_FIXED (0), eParadigm_FLY (4), eParadigm_NUM_PARADIGMS (13), eParadigm_ORBIT_WORLD (11), eParadigm_PAN_LOCAL (8), eParadigm_PAN_WORLD (9), eParadigm_SWIVEL (1), eParadigm_SWIVEL_WORLD (10), eParadigm_TURNTABLE (5), eParadigm_WALK (3), eParadigm_ZOOM (7), eParadigm_ZOOM_BOX (12) """
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

    eParadigm_APPLICATION = None
    eParadigm_EXAMINE = None
    eParadigm_FIXED = None
    eParadigm_FLY = None
    eParadigm_NUM_PARADIGMS = None
    eParadigm_ORBIT_WORLD = None
    eParadigm_PAN_LOCAL = None
    eParadigm_PAN_WORLD = None
    eParadigm_SWIVEL = None
    eParadigm_SWIVEL_WORLD = None
    eParadigm_TURNTABLE = None
    eParadigm_WALK = None
    eParadigm_ZOOM = None
    eParadigm_ZOOM_BOX = None
    value__ = None


class nwEPickFlags(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEPickFlags, values: ePickFlag_CENTER (8192), ePickFlag_CENTER_EXACT_SURFACE (16384), ePickFlag_DISTANCE (512), ePickFlag_EDGE (7), ePickFlag_EDGE_0_1 (1), ePickFlag_EDGE_1_2 (2), ePickFlag_EDGE_2_0 (4), ePickFlag_LINE_VERTEX (196608), ePickFlag_LINE_VERTEX_0 (65536), ePickFlag_LINE_VERTEX_1 (131072), ePickFlag_NEAR_THRESHOLD (4096), ePickFlag_NONE (0), ePickFlag_POINT (256), ePickFlag_VERTEX (112), ePickFlag_VERTEX_0 (16), ePickFlag_VERTEX_1 (32), ePickFlag_VERTEX_2 (64) """
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

    ePickFlag_CENTER = None
    ePickFlag_CENTER_EXACT_SURFACE = None
    ePickFlag_DISTANCE = None
    ePickFlag_EDGE = None
    ePickFlag_EDGE_0_1 = None
    ePickFlag_EDGE_1_2 = None
    ePickFlag_EDGE_2_0 = None
    ePickFlag_LINE_VERTEX = None
    ePickFlag_LINE_VERTEX_0 = None
    ePickFlag_LINE_VERTEX_1 = None
    ePickFlag_NEAR_THRESHOLD = None
    ePickFlag_NONE = None
    ePickFlag_POINT = None
    ePickFlag_VERTEX = None
    ePickFlag_VERTEX_0 = None
    ePickFlag_VERTEX_1 = None
    ePickFlag_VERTEX_2 = None
    value__ = None


class nwEProjection(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEProjection, values: eProjection_ORTHOGRAPHIC (1), eProjection_PERSPECTIVE (0) """
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

    eProjection_ORTHOGRAPHIC = None
    eProjection_PERSPECTIVE = None
    value__ = None


class nwEPublishFlags(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEPublishFlags, values: ePublishFlag_ALLOW_RESAVE (64), ePublishFlag_DISPLAY_AT_PASSWORD (128), ePublishFlag_DISPLAY_ON_OPEN (2), ePublishFlag_EMBED_DATABASE (512), ePublishFlag_EMBED_TEXTURES (256), ePublishFlag_EXPIRES (16), ePublishFlag_NEW (4), ePublishFlag_PASSWORD (1), ePublishFlag_PREVENT_PROPS (1024), ePublishFlag_RESAVED (32) """
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

    ePublishFlag_ALLOW_RESAVE = None
    ePublishFlag_DISPLAY_AT_PASSWORD = None
    ePublishFlag_DISPLAY_ON_OPEN = None
    ePublishFlag_EMBED_DATABASE = None
    ePublishFlag_EMBED_TEXTURES = None
    ePublishFlag_EXPIRES = None
    ePublishFlag_NEW = None
    ePublishFlag_PASSWORD = None
    ePublishFlag_PREVENT_PROPS = None
    ePublishFlag_RESAVED = None
    value__ = None


class nwERenderStyle(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwERenderStyle, values: eRenderStyle_FULL_RENDER (0), eRenderStyle_HLINE_RENDER (4), eRenderStyle_NUM_RENDER (5), eRenderStyle_PREVIEW_RENDER (1), eRenderStyle_SHADED_RENDER (2), eRenderStyle_WIRE_RENDER (3) """
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

    eRenderStyle_FULL_RENDER = None
    eRenderStyle_HLINE_RENDER = None
    eRenderStyle_NUM_RENDER = None
    eRenderStyle_PREVIEW_RENDER = None
    eRenderStyle_SHADED_RENDER = None
    eRenderStyle_WIRE_RENDER = None
    value__ = None


class nwESavedViewType(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwESavedViewType, values: eSavedViewType_Anim (1), eSavedViewType_Cut (2), eSavedViewType_Folder (4), eSavedViewType_View (0) """
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

    eSavedViewType_Anim = None
    eSavedViewType_Cut = None
    eSavedViewType_Folder = None
    eSavedViewType_View = None
    value__ = None


class nwESearchMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwESearchMode, values: eSearchMode_ALL_PATHS (3), eSearchMode_BELOW_SELECTED_PATHS (2), eSearchMode_SELECTED_PATHS (1) """
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

    eSearchMode_ALL_PATHS = None
    eSearchMode_BELOW_SELECTED_PATHS = None
    eSearchMode_SELECTED_PATHS = None
    value__ = None


class nwESecurityAction(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwESecurityAction, values: eSecurityAction_EXPIRED (3), eSecurityAction_FAILED (6), eSecurityAction_NO_LICENSE (5), eSecurityAction_NONE_LEFT (2), eSecurityAction_NONE_SUIT (7), eSecurityAction_OK (0) """
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

    eSecurityAction_EXPIRED = None
    eSecurityAction_FAILED = None
    eSecurityAction_NONE_LEFT = None
    eSecurityAction_NONE_SUIT = None
    eSecurityAction_NO_LICENSE = None
    eSecurityAction_OK = None
    value__ = None


class nwESelectionBehaviour(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwESelectionBehaviour, values: eSelectionBehaviour_BY_LAYER (1), eSelectionBehaviour_BY_MODEL (0), eSelectionBehaviour_FIRST_OBJECT (2), eSelectionBehaviour_GEOMETRY (4), eSelectionBehaviour_LAST_COMPOSITE (7), eSelectionBehaviour_LAST_UNIQUE (3), eSelectionBehaviour_NO_SELECTION_CHANGE (6), eSelectionBehaviour_UNIQUE_EQUIVALENT_GEOMETRY (5) """
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

    eSelectionBehaviour_BY_LAYER = None
    eSelectionBehaviour_BY_MODEL = None
    eSelectionBehaviour_FIRST_OBJECT = None
    eSelectionBehaviour_GEOMETRY = None
    eSelectionBehaviour_LAST_COMPOSITE = None
    eSelectionBehaviour_LAST_UNIQUE = None
    eSelectionBehaviour_NO_SELECTION_CHANGE = None
    eSelectionBehaviour_UNIQUE_EQUIVALENT_GEOMETRY = None
    value__ = None


class nwESelTreeBottom(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwESelTreeBottom, values: eSelTreeBottom_BELOW_LAYER (3), eSelTreeBottom_GEOMETRY (6), eSelTreeBottom_LAYER_PLUS (2), eSelTreeBottom_MODEL_PLUS (1), eSelTreeBottom_NONE (0), eSelTreeBottom_TAIL (4), eSelTreeBottom_TAIL_PLUS (5) """
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

    eSelTreeBottom_BELOW_LAYER = None
    eSelTreeBottom_GEOMETRY = None
    eSelTreeBottom_LAYER_PLUS = None
    eSelTreeBottom_MODEL_PLUS = None
    eSelTreeBottom_NONE = None
    eSelTreeBottom_TAIL = None
    eSelTreeBottom_TAIL_PLUS = None
    value__ = None


class nwESelTreeGroupMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwESelTreeGroupMode, values: eSelTreeGroupMode_ALL (0), eSelTreeGroupMode_NAME (1), eSelTreeGroupMode_NONE (2) """
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

    eSelTreeGroupMode_ALL = None
    eSelTreeGroupMode_NAME = None
    eSelTreeGroupMode_NONE = None
    value__ = None


class nwESelTreeIcon(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwESelTreeIcon, values: nwESelTreeIcon_COLLECTION__REQUIRED (27), nwESelTreeIcon_COLLECTION_HIDDEN (15), nwESelTreeIcon_COLLECTION_NORMAL (3), nwESelTreeIcon_COMPOSITE_HIDDEN (17), nwESelTreeIcon_COMPOSITE_NORMAL (5), nwESelTreeIcon_COMPOSITE_REQUIRED (29), nwESelTreeIcon_FIND_SET_HIDDEN (22), nwESelTreeIcon_FIND_SET_NORMAL (10), nwESelTreeIcon_FIND_SET_REQUIRED (34), nwESelTreeIcon_GEOMETRY_HIDDEN (20), nwESelTreeIcon_GEOMETRY_NORMAL (8), nwESelTreeIcon_GEOMETRY_REQUIRED (32), nwESelTreeIcon_GROUP_HIDDEN (16), nwESelTreeIcon_GROUP_NORMAL (4), nwESelTreeIcon_GROUP_REQUIRED (28), nwESelTreeIcon_INSERT_GEOMETRY_HIDDEN (19), nwESelTreeIcon_INSERT_GEOMETRY_NORMAL (7), nwESelTreeIcon_INSERT_GEOMETRY_REQUIRED (31), nwESelTreeIcon_INSERT_GROUP_HIDDEN (18), nwESelTreeIcon_INSERT_GROUP_NORMAL (6), nwESelTreeIcon_INSERT_GROUP_REQUIRED (30), nwESelTreeIcon_LAYER_HIDDEN (14), nwESelTreeIcon_LAYER_NORMAL (2), nwESelTreeIcon_LAYER_REQUIRED (26), nwESelTreeIcon_MODEL_HIDDEN (13), nwESelTreeIcon_MODEL_NORMAL (1), nwESelTreeIcon_MODEL_REQUIRED (25), nwESelTreeIcon_SELECTION_SET_HIDDEN (21), nwESelTreeIcon_SELECTION_SET_NORMAL (9), nwESelTreeIcon_SELECTION_SET_REQUIRED (33), nwESelTreeIcon_UNKNOWN_HIDDEN (12), nwESelTreeIcon_UNKNOWN_NORMAL (0), nwESelTreeIcon_UNKNOWN_REQUIRED (24), nwESelTreeIcon_ZONE_SET_HIDDEN (23), nwESelTreeIcon_ZONE_SET_NORMAL (11), nwESelTreeIcon_ZONE_SET_REQUIRED (35) """
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

    nwESelTreeIcon_COLLECTION_HIDDEN = None
    nwESelTreeIcon_COLLECTION_NORMAL = None
    nwESelTreeIcon_COLLECTION__REQUIRED = None
    nwESelTreeIcon_COMPOSITE_HIDDEN = None
    nwESelTreeIcon_COMPOSITE_NORMAL = None
    nwESelTreeIcon_COMPOSITE_REQUIRED = None
    nwESelTreeIcon_FIND_SET_HIDDEN = None
    nwESelTreeIcon_FIND_SET_NORMAL = None
    nwESelTreeIcon_FIND_SET_REQUIRED = None
    nwESelTreeIcon_GEOMETRY_HIDDEN = None
    nwESelTreeIcon_GEOMETRY_NORMAL = None
    nwESelTreeIcon_GEOMETRY_REQUIRED = None
    nwESelTreeIcon_GROUP_HIDDEN = None
    nwESelTreeIcon_GROUP_NORMAL = None
    nwESelTreeIcon_GROUP_REQUIRED = None
    nwESelTreeIcon_INSERT_GEOMETRY_HIDDEN = None
    nwESelTreeIcon_INSERT_GEOMETRY_NORMAL = None
    nwESelTreeIcon_INSERT_GEOMETRY_REQUIRED = None
    nwESelTreeIcon_INSERT_GROUP_HIDDEN = None
    nwESelTreeIcon_INSERT_GROUP_NORMAL = None
    nwESelTreeIcon_INSERT_GROUP_REQUIRED = None
    nwESelTreeIcon_LAYER_HIDDEN = None
    nwESelTreeIcon_LAYER_NORMAL = None
    nwESelTreeIcon_LAYER_REQUIRED = None
    nwESelTreeIcon_MODEL_HIDDEN = None
    nwESelTreeIcon_MODEL_NORMAL = None
    nwESelTreeIcon_MODEL_REQUIRED = None
    nwESelTreeIcon_SELECTION_SET_HIDDEN = None
    nwESelTreeIcon_SELECTION_SET_NORMAL = None
    nwESelTreeIcon_SELECTION_SET_REQUIRED = None
    nwESelTreeIcon_UNKNOWN_HIDDEN = None
    nwESelTreeIcon_UNKNOWN_NORMAL = None
    nwESelTreeIcon_UNKNOWN_REQUIRED = None
    nwESelTreeIcon_ZONE_SET_HIDDEN = None
    nwESelTreeIcon_ZONE_SET_NORMAL = None
    nwESelTreeIcon_ZONE_SET_REQUIRED = None
    value__ = None


class nwESelTreeIconMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwESelTreeIconMode, values: nwESelTreeIconMode_EXPLICIT (0), nwESelTreeIconMode_STANDARD (1) """
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

    nwESelTreeIconMode_EXPLICIT = None
    nwESelTreeIconMode_STANDARD = None
    value__ = None


class nwESelTreeNameMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwESelTreeNameMode, values: eSelTreeNameMode_EXPLICIT (0), eSelTreeNameMode_STANDARD (2), eSelTreeNameMode_VALUE (1) """
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

    eSelTreeNameMode_EXPLICIT = None
    eSelTreeNameMode_STANDARD = None
    eSelTreeNameMode_VALUE = None
    value__ = None


class nwESelTreeTextFormat(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwESelTreeTextFormat, values: eSelTreeTxtFmt_BOLD (1), eSelTreeTxtFmt_NORMAL (0) """
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

    eSelTreeTxtFmt_BOLD = None
    eSelTreeTxtFmt_NORMAL = None
    value__ = None


class nwESelTreeTextFormatMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwESelTreeTextFormatMode, values: nwESelTreeTextFormatMode_EXPLICIT (0), nwESelTreeTextFormatMode_STANDARD (1) """
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

    nwESelTreeTextFormatMode_EXPLICIT = None
    nwESelTreeTextFormatMode_STANDARD = None
    value__ = None


class nwESelTreeTop(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwESelTreeTop, values: eSelTreeTop_MODEL (1), eSelTreeTop_MODEL_LAYER (2), eSelTreeTop_NONE (0) """
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

    eSelTreeTop_MODEL = None
    eSelTreeTop_MODEL_LAYER = None
    eSelTreeTop_NONE = None
    value__ = None


class nwEStdName(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEStdName, values: eStdName_CLASS_MATERIAL (4), eStdName_CLASS_NAME (2), eStdName_CLASS_NODE (3), eStdName_CLASS_TRANSFORM (5), eStdName_CLASS_URL (6), eStdName_CLASS_USER_NAME (1), eStdName_CLASS_XREF (7), eStdName_PARTITION_FILENAME (9), eStdName_TEXT_TEXT (8), eStdName_USER_NAME (0) """
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

    eStdName_CLASS_MATERIAL = None
    eStdName_CLASS_NAME = None
    eStdName_CLASS_NODE = None
    eStdName_CLASS_TRANSFORM = None
    eStdName_CLASS_URL = None
    eStdName_CLASS_USER_NAME = None
    eStdName_CLASS_XREF = None
    eStdName_PARTITION_FILENAME = None
    eStdName_TEXT_TEXT = None
    eStdName_USER_NAME = None
    value__ = None


class nwETestResultStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwETestResultStatus, values: eTestResultStatus_ACTIVE (1), eTestResultStatus_APPROVED (2), eTestResultStatus_NEW (0), eTestResultStatus_NUM (5), eTestResultStatus_RESOLVED (3), eTestResultStatus_REVIEWED (4), eTestResultStatus_UNMERGED (256) """
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

    eTestResultStatus_ACTIVE = None
    eTestResultStatus_APPROVED = None
    eTestResultStatus_NEW = None
    eTestResultStatus_NUM = None
    eTestResultStatus_RESOLVED = None
    eTestResultStatus_REVIEWED = None
    eTestResultStatus_UNMERGED = None
    value__ = None


class nwEURLDisplayType(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEURLDisplayType, values: eURLDisplayType_ICON (1), eURLDisplayType_TEXT (0) """
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

    eURLDisplayType_ICON = None
    eURLDisplayType_TEXT = None
    value__ = None


class nwEUtilObjType(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEUtilObjType, values: eUtilObjType_nwUResource (1), eUtilObjType_Reserved (0) """
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

    eUtilObjType_nwUResource = None
    eUtilObjType_Reserved = None
    value__ = None


class nwEVertexProperty(Enum, IComparable, IFormattable, IConvertible):
    """ enum nwEVertexProperty, values: eCOLOR (2), eNONE (0), eNORMAL (1), eTEX_COORD (4) """
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

    eCOLOR = None
    eNONE = None
    eNORMAL = None
    eTEX_COORD = None
    value__ = None


class _InwOpStateEvents_Event:
    # no doc
# Error generating skeleton for function add_OnCurrentAnimationChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnCurrentSceneChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnCurrentSceneChanging: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnCurrentSelectionChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnCurrentViewChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnCustomChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnPlanViewChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnSavedViewsChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnSectionViewChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnCurrentAnimationChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnCurrentSceneChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnCurrentSceneChanging: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnCurrentSelectionChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnCurrentViewChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnCustomChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnPlanViewChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnSavedViewsChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnSectionViewChanged: sequence item 1: expected string, NoneType found

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    OnCurrentAnimationChanged = None
    OnCurrentSceneChanged = None
    OnCurrentSceneChanging = None
    OnCurrentSelectionChanged = None
    OnCurrentViewChanged = None
    OnCustomChanged = None
    OnPlanViewChanged = None
    OnSavedViewsChanged = None
    OnSectionViewChanged = None


class nwOpState(InwOpState11, InwOpState10, InwOpState9, InwOpState8, InwOpState7, InwOpState6, InwOpState5, InwOpState4, InwOpState3, InwOpState2, InwOpState, InwBase, _InwOpStateEvents_Event):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class nwOpStateClass(__ComObject, InwOpState11, InwOpState10, InwOpState9, InwOpState8, InwOpState7, InwOpState6, InwOpState5, InwOpState4, InwOpState3, InwOpState2, InwOpState, InwBase, nwOpState, _InwOpStateEvents_Event):
    """ nwOpStateClass() """
# Error generating skeleton for function add_OnCurrentAnimationChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnCurrentSceneChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnCurrentSceneChanging: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnCurrentSelectionChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnCurrentViewChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnCustomChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnPlanViewChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnSavedViewsChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnSectionViewChanged: sequence item 1: expected string, NoneType found

    def ApplyView(self, view):
        """ ApplyView(self: nwOpStateClass, view: InwOpView) """
        pass

    def BeginEdit(self, name):
        """ BeginEdit(self: nwOpStateClass, name: str) """
        pass

    def CheckLicense(self, name):
        """ CheckLicense(self: nwOpStateClass, name: str) -> bool """
        pass

    def Copy(self):
        """ Copy(self: nwOpStateClass) -> object """
        pass

    def CreatePicture(self, anonview, ovNumPasses, vWidth, ovHeight):
        """ CreatePicture(self: nwOpStateClass, anonview: InwOpAnonView, ovNumPasses: object, vWidth: object, ovHeight: object) -> object """
        pass

    def CreatePlugin(self, progid):
        """ CreatePlugin(self: nwOpStateClass, progid: str) -> int """
        pass

    def DeleteSelectedFiles(self):
        """ DeleteSelectedFiles(self: nwOpStateClass) """
        pass

    def DriveIOPlugin(self, internal_name, filename, opts):
        """ DriveIOPlugin(self: nwOpStateClass, internal_name: str, filename: str, opts: InwOaPropertyVec) -> nwEExportStatus """
        pass

    def EndEdit(self):
        """ EndEdit(self: nwOpStateClass) """
        pass

    def EndInteractive(self):
        """ EndInteractive(self: nwOpStateClass) """
        pass

    def FileVersion(self, filename):
        """ FileVersion(self: nwOpStateClass, filename: str) -> int """
        pass

    def GetAttributeProperties(self, p_attribute):
        """ GetAttributeProperties(self: nwOpStateClass, p_attribute: InwOaAttribute) -> InwOaPropertyVec """
        pass

    def GetBoundingBox(self):
        """ GetBoundingBox(self: nwOpStateClass) -> InwLBox3f """
        pass

    def GetCurrentFilename(self):
        """ GetCurrentFilename(self: nwOpStateClass) -> str """
        pass

    def GetEnum(self, sName):
        """ GetEnum(self: nwOpStateClass, sName: str) -> int """
        pass

    def GetFirstInstanceOfNode(self, node):
        """ GetFirstInstanceOfNode(self: nwOpStateClass, node: InwOaNode) -> InwOaPath """
        pass

    def GetGUIPropertyNode(self, p_path, b_show_internal):
        """ GetGUIPropertyNode(self: nwOpStateClass, p_path: InwOaPath, b_show_internal: bool) -> InwGUIPropertyNode """
        pass

    def GetIOPluginOptions(self, internal_name):
        """ GetIOPluginOptions(self: nwOpStateClass, internal_name: str) -> InwOaPropertyVec """
        pass

    def GetMeasureDiff(self):
        """ GetMeasureDiff(self: nwOpStateClass) -> InwLVec3f """
        pass

    def GetMeasureEndPos(self):
        """ GetMeasureEndPos(self: nwOpStateClass) -> InwLPos3f """
        pass

    def GetMeasureFirstPos(self):
        """ GetMeasureFirstPos(self: nwOpStateClass) -> InwLPos3f """
        pass

    def GetMeasureValue(self):
        """ GetMeasureValue(self: nwOpStateClass) -> float """
        pass

    def GetOverrideURL(self, p_path, include_model):
        """ GetOverrideURL(self: nwOpStateClass, p_path: InwOaPath, include_model: object) -> InwURLOverride """
        pass

    def GetProductInfo(self):
        """ GetProductInfo(self: nwOpStateClass) -> str """
        pass

    def GlobalProperties(self):
        """ GlobalProperties(self: nwOpStateClass) -> InwGlobalProperties """
        pass

    def HiddenItemsResetAll(self):
        """ HiddenItemsResetAll(self: nwOpStateClass) """
        pass

    def IsComposite(self, group):
        """ IsComposite(self: nwOpStateClass, group: InwOaGroup) -> bool """
        pass

    def LoadedFileFromNdx(self, ndx):
        """ LoadedFileFromNdx(self: nwOpStateClass, ndx: int) -> InwOaPartition """
        pass

    def LoadedFileFromPath(self, path):
        """ LoadedFileFromPath(self: nwOpStateClass, path: InwOaPath) -> InwOaPartition """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A 
             value of lse is usually appropriate. ue to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the 
             remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def NdxArray2Node(self, fullpath):
        """ NdxArray2Node(self: nwOpStateClass, fullpath: object) -> InwOaNode """
        pass

    def NdxArray2SavedView(self, fullpath):
        """ NdxArray2SavedView(self: nwOpStateClass, fullpath: object) -> InwOpSavedView """
        pass

    def Node2NdxArray(self, pI):
        """ Node2NdxArray(self: nwOpStateClass, pI: InwOaNode) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: nwOpStateClass, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: nwOpStateClass) """
        pass

    def ObjectFactory(self, eType, ovReserved1, ovReserved2):
        """ ObjectFactory(self: nwOpStateClass, eType: nwEObjectType, ovReserved1: object, ovReserved2: object) -> object """
        pass

    def OverrideColor(self, selection, color):
        """ OverrideColor(self: nwOpStateClass, selection: InwOpSelection, color: InwLVec3f) """
        pass

    def OverrideReset(self, selection):
        """ OverrideReset(self: nwOpStateClass, selection: InwOpSelection) """
        pass

    def OverrideResetAll(self):
        """ OverrideResetAll(self: nwOpStateClass) """
        pass

    def OverrideTransform(self, selection, transform):
        """ OverrideTransform(self: nwOpStateClass, selection: InwOpSelection, transform: InwLTransform3f) """
        pass

    def OverrideTransformEx(self, selection, transform, overrideFileTransform):
        """ OverrideTransformEx(self: nwOpStateClass, selection: InwOpSelection, transform: InwLTransform3f, overrideFileTransform: bool) """
        pass

    def OverrideTransformReset(self, selection):
        """ OverrideTransformReset(self: nwOpStateClass, selection: InwOpSelection) """
        pass

    def OverrideTransformResetAll(self):
        """ OverrideTransformResetAll(self: nwOpStateClass) """
        pass

    def OverrideTransparency(self, selection, transparency):
        """ OverrideTransparency(self: nwOpStateClass, selection: InwOpSelection, transparency: float) """
        pass

    def OverrideURLReset(self, selection):
        """ OverrideURLReset(self: nwOpStateClass, selection: InwOpSelection) """
        pass

    def OverrideURLResetAll(self):
        """ OverrideURLResetAll(self: nwOpStateClass) """
        pass

    def Plugins(self):
        """ Plugins(self: nwOpStateClass) -> InwPluginsColl """
        pass

    def PtrEquals(self, i1, i2):
        """ PtrEquals(self: nwOpStateClass, i1: InwBase, i2: InwBase) -> bool """
        pass

# Error generating skeleton for function remove_OnCurrentAnimationChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnCurrentSceneChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnCurrentSceneChanging: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnCurrentSelectionChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnCurrentViewChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnCustomChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnPlanViewChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnSavedViewsChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnSectionViewChanged: sequence item 1: expected string, NoneType found

    def RequiredItemsResetAll(self):
        """ RequiredItemsResetAll(self: nwOpStateClass) """
        pass

    def SavedView2NdxArray(self, pI):
        """ SavedView2NdxArray(self: nwOpStateClass, pI: InwOpSavedView) -> object """
        pass

    def SavedViews(self):
        """ SavedViews(self: nwOpStateClass) -> InwSavedViewsColl """
        pass

    def SceneLights(self):
        """ SceneLights(self: nwOpStateClass) -> InwLightsColl """
        pass

    def SeekSelection(self, results, cb, ovStartSelection):
        """ SeekSelection(self: nwOpStateClass, results: InwOpSelection, cb: InwSeekSelection, ovStartSelection: object) """
        pass

    def SelectionSets(self):
        """ SelectionSets(self: nwOpStateClass) -> InwSelectionSetColl """
        pass

    def SelectionSetsEx(self):
        """ SelectionSetsEx(self: nwOpStateClass) -> InwSelectionSetExColl """
        pass

    def SetOverrideURL(self, selection, pI):
        """ SetOverrideURL(self: nwOpStateClass, selection: InwOpSelection, pI: InwURLOverride) """
        pass

    def SmartTagText(self, path):
        """ SmartTagText(self: nwOpStateClass, path: InwOaPath) -> str """
        pass

    def StartInteractive(self):
        """ StartInteractive(self: nwOpStateClass) """
        pass

    def StdName(self, Type, user_name):
        """ StdName(self: nwOpStateClass, Type: nwEStdName, user_name: bool) -> str """
        pass

    def StopMovement(self):
        """ StopMovement(self: nwOpStateClass) """
        pass

    def ViewAll(self):
        """ ViewAll(self: nwOpStateClass) """
        pass

    def X64PtrLongs(self, i1, high, low):
        """ X64PtrLongs(self: nwOpStateClass, i1: InwBase) -> (int, int) """
        pass

    def X64PtrVar(self, i1, pointer):
        """ X64PtrVar(self: nwOpStateClass, i1: InwBase) -> object """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: nwOpStateClass, vIn: object) -> object """
        pass

    def ZoomInCurViewOnBoundingBox(self, box, factor):
        """ ZoomInCurViewOnBoundingBox(self: nwOpStateClass, box: InwLBox3f, factor: float) """
        pass

    def ZoomInCurViewOnCurSel(self):
        """ ZoomInCurViewOnCurSel(self: nwOpStateClass) """
        pass

    def ZoomInCurViewOnSel(self, selection):
        """ ZoomInCurViewOnSel(self: nwOpStateClass, selection: InwOpSelection) """
        pass

    def ZoomInViewOnSel(self, selection, anonview):
        """ ZoomInViewOnSel(self: nwOpStateClass, selection: InwOpSelection, anonview: InwOpAnonView) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AreaCullThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaCullThreshold(self: nwOpStateClass) -> float

Set: AreaCullThreshold(self: nwOpStateClass) = value
"""

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColor(self: nwOpStateClass) -> InwLVec3f

Set: BackgroundColor(self: nwOpStateClass) = value
"""

    CurrentAnimation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAnimation(self: nwOpStateClass) -> InwOpAnimView

Set: CurrentAnimation(self: nwOpStateClass) = value
"""

    CurrentFindSpec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentFindSpec(self: nwOpStateClass) -> InwOpFindSpec

Set: CurrentFindSpec(self: nwOpStateClass) = value
"""

    CurrentPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPartition(self: nwOpStateClass) -> InwOaPartition

"""

    CurrentPlanView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPlanView(self: nwOpStateClass) -> InwOpAnonView

Set: CurrentPlanView(self: nwOpStateClass) = value
"""

    CurrentSectionView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSectionView(self: nwOpStateClass) -> InwOpAnonView

Set: CurrentSectionView(self: nwOpStateClass) = value
"""

    CurrentSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSelection(self: nwOpStateClass) -> InwOpSelection

Set: CurrentSelection(self: nwOpStateClass) = value
"""

    CurrentView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentView(self: nwOpStateClass) -> InwOpAnonView

Set: CurrentView(self: nwOpStateClass) = value
"""

    EventsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventsEnabled(self: nwOpStateClass) -> bool

Set: EventsEnabled(self: nwOpStateClass) = value
"""

    FrameRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameRate(self: nwOpStateClass) -> int

Set: FrameRate(self: nwOpStateClass) = value
"""

    GlobalAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalAmbient(self: nwOpStateClass) -> InwLVec3f

Set: GlobalAmbient(self: nwOpStateClass) = value
"""

    HeadlightAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightAmbient(self: nwOpStateClass) -> float

Set: HeadlightAmbient(self: nwOpStateClass) = value
"""

    HeadlightIntensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightIntensity(self: nwOpStateClass) -> float

Set: HeadlightIntensity(self: nwOpStateClass) = value
"""

    LoadedFileCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadedFileCount(self: nwOpStateClass) -> int

"""

    MaxNearDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxNearDistance(self: nwOpStateClass) -> float

Set: MaxNearDistance(self: nwOpStateClass) = value
"""

    MinFarDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinFarDistance(self: nwOpStateClass) -> float

Set: MinFarDistance(self: nwOpStateClass) = value
"""

    NumTriangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumTriangles(self: nwOpStateClass) -> int

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: nwOpStateClass) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: nwOpStateClass) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: nwOpStateClass) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: nwOpStateClass) -> int

Set: nwLock(self: nwOpStateClass) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: nwOpStateClass) -> bool

Set: nwOwn(self: nwOpStateClass) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: nwOpStateClass) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: nwOpStateClass) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: nwOpStateClass) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: nwOpStateClass) -> str

"""

    SmartTagsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmartTagsEnabled(self: nwOpStateClass) -> bool

Set: SmartTagsEnabled(self: nwOpStateClass) = value
"""

    TwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TwoSided(self: nwOpStateClass) -> bool

Set: TwoSided(self: nwOpStateClass) = value
"""

    URLsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsEnabled(self: nwOpStateClass) -> bool

Set: URLsEnabled(self: nwOpStateClass) = value
"""


    OnCurrentAnimationChanged = None
    OnCurrentSceneChanged = None
    OnCurrentSceneChanging = None
    OnCurrentSelectionChanged = None
    OnCurrentViewChanged = None
    OnCustomChanged = None
    OnPlanViewChanged = None
    OnSavedViewsChanged = None
    OnSectionViewChanged = None


class _InwScriptParserEvents_Event:
    # no doc
# Error generating skeleton for function add_OnScriptError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnScriptError: sequence item 1: expected string, NoneType found

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    OnScriptError = None


class nwScriptParser(InwScriptParser, _InwScriptParserEvents_Event):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class nwScriptParserClass(__ComObject, InwScriptParser, nwScriptParser, _InwScriptParserEvents_Event):
    """ nwScriptParserClass() """
    def AddObject(self, sName, pIunk):
        """ AddObject(self: nwScriptParserClass, sName: str, pIunk: object) """
        pass

# Error generating skeleton for function add_OnScriptError: sequence item 1: expected string, NoneType found

    def CreateEngine(self, engine_name):
        """ CreateEngine(self: nwScriptParserClass, engine_name: str) """
        pass

    def GetScriptDispatch(self, sName):
        """ GetScriptDispatch(self: nwScriptParserClass, sName: str) -> object """
        pass

    def LoadScript(self, script):
        """ LoadScript(self: nwScriptParserClass, script: str) """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A 
             value of lse is usually appropriate. ue to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the 
             remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

# Error generating skeleton for function remove_OnScriptError: sequence item 1: expected string, NoneType found

    def Run(self):
        """ Run(self: nwScriptParserClass) """
        pass

    def Stop(self):
        """ Stop(self: nwScriptParserClass) """
        pass

    def ThreadSafeKill(self):
        """ ThreadSafeKill(self: nwScriptParserClass) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    OnScriptError = None


class nwUtilityObject(InwUtilityObject):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class nwUtilityObjectClass(__ComObject, InwUtilityObject, nwUtilityObject):
    """ nwUtilityObjectClass() """
    def GetEnum(self, sName):
        """ GetEnum(self: nwUtilityObjectClass, sName: str) -> int """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A 
             value of lse is usually appropriate. ue to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the 
             remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def ObjectFactory(self, eType, ovReserved1, ovReserved2):
        """ ObjectFactory(self: nwUtilityObjectClass, eType: nwEUtilObjType, ovReserved1: object, ovReserved2: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class nwVerIndependentControl(InwControl5, InwControl4, InwControl3, InwControl2, InwControl, _InwControlEvents_Event):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class nwVerIndependentControlClass(__ComObject, InwControl5, InwControl4, InwControl3, InwControl2, InwControl, nwVerIndependentControl, _InwControlEvents_Event):
    # no doc
# Error generating skeleton for function add_OnCertificateDownload: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnContextMenu: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnContextMenuEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnEnableContextMenuCmd: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnEnableContextMenuCmdEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnEnableUserNavMode: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnEnableUserNavModeEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnFileDownload: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnFileError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnFileOpen: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnKeyDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnKeyDownEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnKeyUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnKeyUpEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnLButtonDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnLButtonUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnMButtonDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnMButtonUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnMouseMove: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnMouseWheel: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnNavModeChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnOutOfMemory: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnProgressError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnProgressPublished: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnSecurityChecked: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnSecurityError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnUserContextMenuCmd: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnXRefResolve: sequence item 1: expected string, NoneType found

    def AnimationCommand(self, cmd):
        """ AnimationCommand(self: nwVerIndependentControlClass, cmd: nwEAnimationCmd) -> nwEAnimCmdFlags """
        pass

    def AppendFile(self, file_name):
        """ AppendFile(self: nwVerIndependentControlClass, file_name: str) """
        pass

    def AppendFile_As(self, file_name, file_type):
        """ AppendFile_As(self: nwVerIndependentControlClass, file_name: str, file_type: nwEFileAsType) """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A 
             value of lse is usually appropriate. ue to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the 
             remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def PickPixel(self, x, y, width, Flags, pos1, pos2, pos3):
        """ PickPixel(self: nwVerIndependentControlClass, x: int, y: int, width: int, Flags: nwEPickFlags) -> (InwOaFragment, object, object, object) """
        pass

# Error generating skeleton for function remove_OnCertificateDownload: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnContextMenu: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnContextMenuEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnEnableContextMenuCmd: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnEnableContextMenuCmdEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnEnableUserNavMode: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnEnableUserNavModeEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnFileDownload: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnFileError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnFileOpen: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnKeyDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnKeyDownEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnKeyUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnKeyUpEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnLButtonDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnLButtonUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnMButtonDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnMButtonUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnMouseMove: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnMouseWheel: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnNavModeChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnOutOfMemory: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnProgressError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnProgressPublished: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnSecurityChecked: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnSecurityError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnUserContextMenuCmd: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnXRefResolve: sequence item 1: expected string, NoneType found

    def SaveFile(self, file_name):
        """ SaveFile(self: nwVerIndependentControlClass, file_name: str) """
        pass

    def SaveFile_As(self, file_name, file_type):
        """ SaveFile_As(self: nwVerIndependentControlClass, file_name: str, file_type: nwEFileAsType) """
        pass

    def SRC_As(self, file_name, file_type):
        """ SRC_As(self: nwVerIndependentControlClass, file_name: str, file_type: nwEFileAsType) """
        pass

    def SyncAppendFile(self, file_name):
        """ SyncAppendFile(self: nwVerIndependentControlClass, file_name: str) """
        pass

    def SyncAppendFile_As(self, file_name, file_type):
        """ SyncAppendFile_As(self: nwVerIndependentControlClass, file_name: str, file_type: nwEFileAsType) """
        pass

    def SyncSRC(self, file_name):
        """ SyncSRC(self: nwVerIndependentControlClass, file_name: str) """
        pass

    def SyncSRC_As(self, file_name, file_type):
        """ SyncSRC_As(self: nwVerIndependentControlClass, file_name: str, file_type: nwEFileAsType) """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: nwVerIndependentControlClass, vIn: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    APIState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: APIState(self: nwVerIndependentControlClass) -> InwOpState

"""

    AutoSetFocusMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSetFocusMode(self: nwVerIndependentControlClass) -> bool

Set: AutoSetFocusMode(self: nwVerIndependentControlClass) = value
"""

    ForceEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForceEvents(self: nwVerIndependentControlClass) -> bool

Set: ForceEvents(self: nwVerIndependentControlClass) = value
"""

    HighlightSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighlightSelection(self: nwVerIndependentControlClass) -> bool

Set: HighlightSelection(self: nwVerIndependentControlClass) = value
"""

    LocalisationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalisationCode(self: nwVerIndependentControlClass) -> str

Set: LocalisationCode(self: nwVerIndependentControlClass) = value
"""

    NavigationMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NavigationMode(self: nwVerIndependentControlClass) -> nwENavigationMode

Set: NavigationMode(self: nwVerIndependentControlClass) = value
"""

    ProgressMsg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProgressMsg(self: nwVerIndependentControlClass) -> str

Set: ProgressMsg(self: nwVerIndependentControlClass) = value
"""

    SecurityCertificate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecurityCertificate(self: nwVerIndependentControlClass) -> str

Set: SecurityCertificate(self: nwVerIndependentControlClass) = value
"""

    SelectionBehaviour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionBehaviour(self: nwVerIndependentControlClass) -> nwESelectionBehaviour

Set: SelectionBehaviour(self: nwVerIndependentControlClass) = value
"""

    ShowProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowProgress(self: nwVerIndependentControlClass) -> bool

Set: ShowProgress(self: nwVerIndependentControlClass) = value
"""

    SRC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SRC(self: nwVerIndependentControlClass) -> str

Set: SRC(self: nwVerIndependentControlClass) = value
"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: nwVerIndependentControlClass) -> InwOpState

"""

    UserModeSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserModeSelection(self: nwVerIndependentControlClass) -> bool

Set: UserModeSelection(self: nwVerIndependentControlClass) = value
"""

    _State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: _State(self: nwVerIndependentControlClass) -> str

Set: _State(self: nwVerIndependentControlClass) = value
"""


    OnCertificateDownload = None
    OnContextMenu = None
    OnContextMenuEx = None
    OnEnableContextMenuCmd = None
    OnEnableContextMenuCmdEx = None
    OnEnableUserNavMode = None
    OnEnableUserNavModeEx = None
    OnFileDownload = None
    OnFileError = None
    OnFileOpen = None
    OnKeyDown = None
    OnKeyDownEx = None
    OnKeyUp = None
    OnKeyUpEx = None
    OnLButtonDown = None
    OnLButtonUp = None
    OnMButtonDown = None
    OnMButtonUp = None
    OnMouseMove = None
    OnMouseWheel = None
    OnNavModeChanged = None
    OnOutOfMemory = None
    OnProgressError = None
    OnProgressPublished = None
    OnSecurityChecked = None
    OnSecurityError = None
    OnUserContextMenuCmd = None
    OnXRefResolve = None


class nwVerIndependentScriptParser(InwScriptParser, _InwScriptParserEvents_Event):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class nwVerIndependentScriptParserClass(__ComObject, InwScriptParser, nwVerIndependentScriptParser, _InwScriptParserEvents_Event):
    # no doc
    def AddObject(self, sName, pIunk):
        """ AddObject(self: nwVerIndependentScriptParserClass, sName: str, pIunk: object) """
        pass

# Error generating skeleton for function add_OnScriptError: sequence item 1: expected string, NoneType found

    def CreateEngine(self, engine_name):
        """ CreateEngine(self: nwVerIndependentScriptParserClass, engine_name: str) """
        pass

    def GetScriptDispatch(self, sName):
        """ GetScriptDispatch(self: nwVerIndependentScriptParserClass, sName: str) -> object """
        pass

    def LoadScript(self, script):
        """ LoadScript(self: nwVerIndependentScriptParserClass, script: str) """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A 
             value of lse is usually appropriate. ue to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the 
             remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

# Error generating skeleton for function remove_OnScriptError: sequence item 1: expected string, NoneType found

    def Run(self):
        """ Run(self: nwVerIndependentScriptParserClass) """
        pass

    def Stop(self):
        """ Stop(self: nwVerIndependentScriptParserClass) """
        pass

    def ThreadSafeKill(self):
        """ ThreadSafeKill(self: nwVerIndependentScriptParserClass) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    OnScriptError = None


class nwVerIndependentState(InwOpState11, InwOpState10, InwOpState9, InwOpState8, InwOpState7, InwOpState6, InwOpState5, InwOpState4, InwOpState3, InwOpState2, InwOpState, InwBase, _InwOpStateEvents_Event):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class nwVerIndependentStateClass(__ComObject, InwOpState11, InwOpState10, InwOpState9, InwOpState8, InwOpState7, InwOpState6, InwOpState5, InwOpState4, InwOpState3, InwOpState2, InwOpState, InwBase, nwVerIndependentState, _InwOpStateEvents_Event):
    # no doc
# Error generating skeleton for function add_OnCurrentAnimationChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnCurrentSceneChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnCurrentSceneChanging: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnCurrentSelectionChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnCurrentViewChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnCustomChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnPlanViewChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnSavedViewsChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function add_OnSectionViewChanged: sequence item 1: expected string, NoneType found

    def ApplyView(self, view):
        """ ApplyView(self: nwVerIndependentStateClass, view: InwOpView) """
        pass

    def BeginEdit(self, name):
        """ BeginEdit(self: nwVerIndependentStateClass, name: str) """
        pass

    def CheckLicense(self, name):
        """ CheckLicense(self: nwVerIndependentStateClass, name: str) -> bool """
        pass

    def Copy(self):
        """ Copy(self: nwVerIndependentStateClass) -> object """
        pass

    def CreatePicture(self, anonview, ovNumPasses, vWidth, ovHeight):
        """ CreatePicture(self: nwVerIndependentStateClass, anonview: InwOpAnonView, ovNumPasses: object, vWidth: object, ovHeight: object) -> object """
        pass

    def CreatePlugin(self, progid):
        """ CreatePlugin(self: nwVerIndependentStateClass, progid: str) -> int """
        pass

    def DeleteSelectedFiles(self):
        """ DeleteSelectedFiles(self: nwVerIndependentStateClass) """
        pass

    def DriveIOPlugin(self, internal_name, filename, opts):
        """ DriveIOPlugin(self: nwVerIndependentStateClass, internal_name: str, filename: str, opts: InwOaPropertyVec) -> nwEExportStatus """
        pass

    def EndEdit(self):
        """ EndEdit(self: nwVerIndependentStateClass) """
        pass

    def EndInteractive(self):
        """ EndInteractive(self: nwVerIndependentStateClass) """
        pass

    def FileVersion(self, filename):
        """ FileVersion(self: nwVerIndependentStateClass, filename: str) -> int """
        pass

    def GetAttributeProperties(self, p_attribute):
        """ GetAttributeProperties(self: nwVerIndependentStateClass, p_attribute: InwOaAttribute) -> InwOaPropertyVec """
        pass

    def GetBoundingBox(self):
        """ GetBoundingBox(self: nwVerIndependentStateClass) -> InwLBox3f """
        pass

    def GetCurrentFilename(self):
        """ GetCurrentFilename(self: nwVerIndependentStateClass) -> str """
        pass

    def GetEnum(self, sName):
        """ GetEnum(self: nwVerIndependentStateClass, sName: str) -> int """
        pass

    def GetFirstInstanceOfNode(self, node):
        """ GetFirstInstanceOfNode(self: nwVerIndependentStateClass, node: InwOaNode) -> InwOaPath """
        pass

    def GetGUIPropertyNode(self, p_path, b_show_internal):
        """ GetGUIPropertyNode(self: nwVerIndependentStateClass, p_path: InwOaPath, b_show_internal: bool) -> InwGUIPropertyNode """
        pass

    def GetIOPluginOptions(self, internal_name):
        """ GetIOPluginOptions(self: nwVerIndependentStateClass, internal_name: str) -> InwOaPropertyVec """
        pass

    def GetMeasureDiff(self):
        """ GetMeasureDiff(self: nwVerIndependentStateClass) -> InwLVec3f """
        pass

    def GetMeasureEndPos(self):
        """ GetMeasureEndPos(self: nwVerIndependentStateClass) -> InwLPos3f """
        pass

    def GetMeasureFirstPos(self):
        """ GetMeasureFirstPos(self: nwVerIndependentStateClass) -> InwLPos3f """
        pass

    def GetMeasureValue(self):
        """ GetMeasureValue(self: nwVerIndependentStateClass) -> float """
        pass

    def GetOverrideURL(self, p_path, include_model):
        """ GetOverrideURL(self: nwVerIndependentStateClass, p_path: InwOaPath, include_model: object) -> InwURLOverride """
        pass

    def GetProductInfo(self):
        """ GetProductInfo(self: nwVerIndependentStateClass) -> str """
        pass

    def GlobalProperties(self):
        """ GlobalProperties(self: nwVerIndependentStateClass) -> InwGlobalProperties """
        pass

    def HiddenItemsResetAll(self):
        """ HiddenItemsResetAll(self: nwVerIndependentStateClass) """
        pass

    def IsComposite(self, group):
        """ IsComposite(self: nwVerIndependentStateClass, group: InwOaGroup) -> bool """
        pass

    def LoadedFileFromNdx(self, ndx):
        """ LoadedFileFromNdx(self: nwVerIndependentStateClass, ndx: int) -> InwOaPartition """
        pass

    def LoadedFileFromPath(self, path):
        """ LoadedFileFromPath(self: nwVerIndependentStateClass, path: InwOaPath) -> InwOaPartition """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A 
             value of lse is usually appropriate. ue to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the 
             remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def NdxArray2Node(self, fullpath):
        """ NdxArray2Node(self: nwVerIndependentStateClass, fullpath: object) -> InwOaNode """
        pass

    def NdxArray2SavedView(self, fullpath):
        """ NdxArray2SavedView(self: nwVerIndependentStateClass, fullpath: object) -> InwOpSavedView """
        pass

    def Node2NdxArray(self, pI):
        """ Node2NdxArray(self: nwVerIndependentStateClass, pI: InwOaNode) -> object """
        pass

    def nwInit(self, nw_ptr, nw_lock):
        """ nwInit(self: nwVerIndependentStateClass, nw_ptr: int, nw_lock: int) """
        pass

    def nwInvalidate(self):
        """ nwInvalidate(self: nwVerIndependentStateClass) """
        pass

    def ObjectFactory(self, eType, ovReserved1, ovReserved2):
        """ ObjectFactory(self: nwVerIndependentStateClass, eType: nwEObjectType, ovReserved1: object, ovReserved2: object) -> object """
        pass

    def OverrideColor(self, selection, color):
        """ OverrideColor(self: nwVerIndependentStateClass, selection: InwOpSelection, color: InwLVec3f) """
        pass

    def OverrideReset(self, selection):
        """ OverrideReset(self: nwVerIndependentStateClass, selection: InwOpSelection) """
        pass

    def OverrideResetAll(self):
        """ OverrideResetAll(self: nwVerIndependentStateClass) """
        pass

    def OverrideTransform(self, selection, transform):
        """ OverrideTransform(self: nwVerIndependentStateClass, selection: InwOpSelection, transform: InwLTransform3f) """
        pass

    def OverrideTransformEx(self, selection, transform, overrideFileTransform):
        """ OverrideTransformEx(self: nwVerIndependentStateClass, selection: InwOpSelection, transform: InwLTransform3f, overrideFileTransform: bool) """
        pass

    def OverrideTransformReset(self, selection):
        """ OverrideTransformReset(self: nwVerIndependentStateClass, selection: InwOpSelection) """
        pass

    def OverrideTransformResetAll(self):
        """ OverrideTransformResetAll(self: nwVerIndependentStateClass) """
        pass

    def OverrideTransparency(self, selection, transparency):
        """ OverrideTransparency(self: nwVerIndependentStateClass, selection: InwOpSelection, transparency: float) """
        pass

    def OverrideURLReset(self, selection):
        """ OverrideURLReset(self: nwVerIndependentStateClass, selection: InwOpSelection) """
        pass

    def OverrideURLResetAll(self):
        """ OverrideURLResetAll(self: nwVerIndependentStateClass) """
        pass

    def Plugins(self):
        """ Plugins(self: nwVerIndependentStateClass) -> InwPluginsColl """
        pass

    def PtrEquals(self, i1, i2):
        """ PtrEquals(self: nwVerIndependentStateClass, i1: InwBase, i2: InwBase) -> bool """
        pass

# Error generating skeleton for function remove_OnCurrentAnimationChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnCurrentSceneChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnCurrentSceneChanging: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnCurrentSelectionChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnCurrentViewChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnCustomChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnPlanViewChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnSavedViewsChanged: sequence item 1: expected string, NoneType found

# Error generating skeleton for function remove_OnSectionViewChanged: sequence item 1: expected string, NoneType found

    def RequiredItemsResetAll(self):
        """ RequiredItemsResetAll(self: nwVerIndependentStateClass) """
        pass

    def SavedView2NdxArray(self, pI):
        """ SavedView2NdxArray(self: nwVerIndependentStateClass, pI: InwOpSavedView) -> object """
        pass

    def SavedViews(self):
        """ SavedViews(self: nwVerIndependentStateClass) -> InwSavedViewsColl """
        pass

    def SceneLights(self):
        """ SceneLights(self: nwVerIndependentStateClass) -> InwLightsColl """
        pass

    def SeekSelection(self, results, cb, ovStartSelection):
        """ SeekSelection(self: nwVerIndependentStateClass, results: InwOpSelection, cb: InwSeekSelection, ovStartSelection: object) """
        pass

    def SelectionSets(self):
        """ SelectionSets(self: nwVerIndependentStateClass) -> InwSelectionSetColl """
        pass

    def SelectionSetsEx(self):
        """ SelectionSetsEx(self: nwVerIndependentStateClass) -> InwSelectionSetExColl """
        pass

    def SetOverrideURL(self, selection, pI):
        """ SetOverrideURL(self: nwVerIndependentStateClass, selection: InwOpSelection, pI: InwURLOverride) """
        pass

    def SmartTagText(self, path):
        """ SmartTagText(self: nwVerIndependentStateClass, path: InwOaPath) -> str """
        pass

    def StartInteractive(self):
        """ StartInteractive(self: nwVerIndependentStateClass) """
        pass

    def StdName(self, Type, user_name):
        """ StdName(self: nwVerIndependentStateClass, Type: nwEStdName, user_name: bool) -> str """
        pass

    def StopMovement(self):
        """ StopMovement(self: nwVerIndependentStateClass) """
        pass

    def ViewAll(self):
        """ ViewAll(self: nwVerIndependentStateClass) """
        pass

    def X64PtrLongs(self, i1, high, low):
        """ X64PtrLongs(self: nwVerIndependentStateClass, i1: InwBase) -> (int, int) """
        pass

    def X64PtrVar(self, i1, pointer):
        """ X64PtrVar(self: nwVerIndependentStateClass, i1: InwBase) -> object """
        pass

    def Xtension(self, vIn):
        """ Xtension(self: nwVerIndependentStateClass, vIn: object) -> object """
        pass

    def ZoomInCurViewOnBoundingBox(self, box, factor):
        """ ZoomInCurViewOnBoundingBox(self: nwVerIndependentStateClass, box: InwLBox3f, factor: float) """
        pass

    def ZoomInCurViewOnCurSel(self):
        """ ZoomInCurViewOnCurSel(self: nwVerIndependentStateClass) """
        pass

    def ZoomInCurViewOnSel(self, selection):
        """ ZoomInCurViewOnSel(self: nwVerIndependentStateClass, selection: InwOpSelection) """
        pass

    def ZoomInViewOnSel(self, selection, anonview):
        """ ZoomInViewOnSel(self: nwVerIndependentStateClass, selection: InwOpSelection, anonview: InwOpAnonView) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AreaCullThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaCullThreshold(self: nwVerIndependentStateClass) -> float

Set: AreaCullThreshold(self: nwVerIndependentStateClass) = value
"""

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColor(self: nwVerIndependentStateClass) -> InwLVec3f

Set: BackgroundColor(self: nwVerIndependentStateClass) = value
"""

    CurrentAnimation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAnimation(self: nwVerIndependentStateClass) -> InwOpAnimView

Set: CurrentAnimation(self: nwVerIndependentStateClass) = value
"""

    CurrentFindSpec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentFindSpec(self: nwVerIndependentStateClass) -> InwOpFindSpec

Set: CurrentFindSpec(self: nwVerIndependentStateClass) = value
"""

    CurrentPartition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPartition(self: nwVerIndependentStateClass) -> InwOaPartition

"""

    CurrentPlanView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPlanView(self: nwVerIndependentStateClass) -> InwOpAnonView

Set: CurrentPlanView(self: nwVerIndependentStateClass) = value
"""

    CurrentSectionView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSectionView(self: nwVerIndependentStateClass) -> InwOpAnonView

Set: CurrentSectionView(self: nwVerIndependentStateClass) = value
"""

    CurrentSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSelection(self: nwVerIndependentStateClass) -> InwOpSelection

Set: CurrentSelection(self: nwVerIndependentStateClass) = value
"""

    CurrentView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentView(self: nwVerIndependentStateClass) -> InwOpAnonView

Set: CurrentView(self: nwVerIndependentStateClass) = value
"""

    EventsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventsEnabled(self: nwVerIndependentStateClass) -> bool

Set: EventsEnabled(self: nwVerIndependentStateClass) = value
"""

    FrameRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameRate(self: nwVerIndependentStateClass) -> int

Set: FrameRate(self: nwVerIndependentStateClass) = value
"""

    GlobalAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalAmbient(self: nwVerIndependentStateClass) -> InwLVec3f

Set: GlobalAmbient(self: nwVerIndependentStateClass) = value
"""

    HeadlightAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightAmbient(self: nwVerIndependentStateClass) -> float

Set: HeadlightAmbient(self: nwVerIndependentStateClass) = value
"""

    HeadlightIntensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightIntensity(self: nwVerIndependentStateClass) -> float

Set: HeadlightIntensity(self: nwVerIndependentStateClass) = value
"""

    LoadedFileCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadedFileCount(self: nwVerIndependentStateClass) -> int

"""

    MaxNearDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxNearDistance(self: nwVerIndependentStateClass) -> float

Set: MaxNearDistance(self: nwVerIndependentStateClass) = value
"""

    MinFarDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinFarDistance(self: nwVerIndependentStateClass) -> float

Set: MinFarDistance(self: nwVerIndependentStateClass) = value
"""

    NumTriangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumTriangles(self: nwVerIndependentStateClass) -> int

"""

    nwHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwHandle(self: nwVerIndependentStateClass) -> int

"""

    nwID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwID(self: nwVerIndependentStateClass) -> int

"""

    nwInvalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwInvalidated(self: nwVerIndependentStateClass) -> bool

"""

    nwLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwLock(self: nwVerIndependentStateClass) -> int

Set: nwLock(self: nwVerIndependentStateClass) = value
"""

    nwOwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwOwn(self: nwVerIndependentStateClass) -> bool

Set: nwOwn(self: nwVerIndependentStateClass) = value
"""

    nwProcess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwProcess(self: nwVerIndependentStateClass) -> int

"""

    nwReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwReadOnly(self: nwVerIndependentStateClass) -> bool

"""

    nwThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: nwThread(self: nwVerIndependentStateClass) -> int

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: nwVerIndependentStateClass) -> str

"""

    SmartTagsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmartTagsEnabled(self: nwVerIndependentStateClass) -> bool

Set: SmartTagsEnabled(self: nwVerIndependentStateClass) = value
"""

    TwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TwoSided(self: nwVerIndependentStateClass) -> bool

Set: TwoSided(self: nwVerIndependentStateClass) = value
"""

    URLsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URLsEnabled(self: nwVerIndependentStateClass) -> bool

Set: URLsEnabled(self: nwVerIndependentStateClass) = value
"""


    OnCurrentAnimationChanged = None
    OnCurrentSceneChanged = None
    OnCurrentSceneChanging = None
    OnCurrentSelectionChanged = None
    OnCurrentViewChanged = None
    OnCustomChanged = None
    OnPlanViewChanged = None
    OnSavedViewsChanged = None
    OnSectionViewChanged = None


class _InwControlEvents:
    # no doc
    def OnCertificateDownload(self):
        """ OnCertificateDownload(self: _InwControlEvents) """
        pass

    def OnContextMenu(self, x_coord, y_coord, bHandled):
        """ OnContextMenu(self: _InwControlEvents, x_coord: int, y_coord: int) -> bool """
        pass

    def OnContextMenuEx(self, x_coord, y_coord, bHandled):
        """ OnContextMenuEx(self: _InwControlEvents, x_coord: int, y_coord: int) -> object """
        pass

    def OnEnableContextMenuCmd(self, cmd_ndx, display_name, bEnable):
        """ OnEnableContextMenuCmd(self: _InwControlEvents, cmd_ndx: int) -> (str, bool) """
        pass

    def OnEnableContextMenuCmdEx(self, cmd_ndx, display_name, bEnable):
        """ OnEnableContextMenuCmdEx(self: _InwControlEvents, cmd_ndx: int) -> (object, object) """
        pass

    def OnEnableUserNavMode(self, mode, display_name, bEnable):
        """ OnEnableUserNavMode(self: _InwControlEvents, mode: int) -> (str, bool) """
        pass

    def OnEnableUserNavModeEx(self, mode, display_name, bEnable):
        """ OnEnableUserNavModeEx(self: _InwControlEvents, mode: int) -> (object, object) """
        pass

    def OnFileDownload(self):
        """ OnFileDownload(self: _InwControlEvents) """
        pass

    def OnFileError(self, file_error):
        """ OnFileError(self: _InwControlEvents, file_error: int) """
        pass

    def OnFileOpen(self):
        """ OnFileOpen(self: _InwControlEvents) """
        pass

    def OnKeyDown(self, key_code, key_data, bHandled):
        """ OnKeyDown(self: _InwControlEvents, key_code: int, key_data: int) -> bool """
        pass

    def OnKeyDownEx(self, key_code, key_data, bHandled):
        """ OnKeyDownEx(self: _InwControlEvents, key_code: int, key_data: int) -> object """
        pass

    def OnKeyUp(self, key_code, key_data, bHandled):
        """ OnKeyUp(self: _InwControlEvents, key_code: int, key_data: int) -> bool """
        pass

    def OnKeyUpEx(self, key_code, key_data, bHandled):
        """ OnKeyUpEx(self: _InwControlEvents, key_code: int, key_data: int) -> object """
        pass

    def OnLButtonDown(self, Flags, x_coord, y_coord):
        """ OnLButtonDown(self: _InwControlEvents, Flags: int, x_coord: int, y_coord: int) """
        pass

    def OnLButtonUp(self, Flags, x_coord, y_coord):
        """ OnLButtonUp(self: _InwControlEvents, Flags: int, x_coord: int, y_coord: int) """
        pass

    def OnMButtonDown(self, Flags, x_coord, y_coord):
        """ OnMButtonDown(self: _InwControlEvents, Flags: int, x_coord: int, y_coord: int) """
        pass

    def OnMButtonUp(self, Flags, x_coord, y_coord):
        """ OnMButtonUp(self: _InwControlEvents, Flags: int, x_coord: int, y_coord: int) """
        pass

    def OnMouseMove(self, Flags, x_coord, y_coord):
        """ OnMouseMove(self: _InwControlEvents, Flags: int, x_coord: int, y_coord: int) """
        pass

    def OnMouseWheel(self, Flags, delta, x_coord, y_coord):
        """ OnMouseWheel(self: _InwControlEvents, Flags: int, delta: int, x_coord: int, y_coord: int) """
        pass

    def OnNavModeChanged(self, mode):
        """ OnNavModeChanged(self: _InwControlEvents, mode: int) """
        pass

    def OnOutOfMemory(self):
        """ OnOutOfMemory(self: _InwControlEvents) """
        pass

    def OnProgressError(self, error_number, description, filename, bCancel, bHandled):
        """ OnProgressError(self: _InwControlEvents, error_number: int, description: str, filename: str) -> (bool, bool) """
        pass

    def OnProgressPublished(self, filename, pub_attrib, Password, bHandled):
        """ OnProgressPublished(self: _InwControlEvents, filename: str, pub_attrib: object) -> (str, bool) """
        pass

    def OnSecurityChecked(self):
        """ OnSecurityChecked(self: _InwControlEvents) """
        pass

    def OnSecurityError(self, security_error):
        """ OnSecurityError(self: _InwControlEvents, security_error: int) """
        pass

    def OnUserContextMenuCmd(self, cmd_ndx):
        """ OnUserContextMenuCmd(self: _InwControlEvents, cmd_ndx: int) """
        pass

    def OnXRefResolve(self, filename, resolved, bHandled):
        """ OnXRefResolve(self: _InwControlEvents, filename: str) -> (str, bool) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _InwControlEvents_OnCertificateDownloadEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnCertificateDownloadEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self):
        """ Invoke(self: _InwControlEvents_OnCertificateDownloadEventHandler) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnContextMenuEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnContextMenuEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, x_coord, y_coord, bHandled):
        """ Invoke(self: _InwControlEvents_OnContextMenuEventHandler, x_coord: int, y_coord: int) -> bool """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnContextMenuExEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnContextMenuExEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, x_coord, y_coord, bHandled):
        """ Invoke(self: _InwControlEvents_OnContextMenuExEventHandler, x_coord: int, y_coord: int) -> object """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnEnableContextMenuCmdEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnEnableContextMenuCmdEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, cmd_ndx, display_name, bEnable):
        """ Invoke(self: _InwControlEvents_OnEnableContextMenuCmdEventHandler, cmd_ndx: int) -> (str, bool) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnEnableContextMenuCmdExEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnEnableContextMenuCmdExEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, cmd_ndx, display_name, bEnable):
        """ Invoke(self: _InwControlEvents_OnEnableContextMenuCmdExEventHandler, cmd_ndx: int) -> (object, object) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnEnableUserNavModeEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnEnableUserNavModeEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, mode, display_name, bEnable):
        """ Invoke(self: _InwControlEvents_OnEnableUserNavModeEventHandler, mode: int) -> (str, bool) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnEnableUserNavModeExEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnEnableUserNavModeExEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, mode, display_name, bEnable):
        """ Invoke(self: _InwControlEvents_OnEnableUserNavModeExEventHandler, mode: int) -> (object, object) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnFileDownloadEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnFileDownloadEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self):
        """ Invoke(self: _InwControlEvents_OnFileDownloadEventHandler) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnFileErrorEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnFileErrorEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, file_error):
        """ Invoke(self: _InwControlEvents_OnFileErrorEventHandler, file_error: int) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnFileOpenEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnFileOpenEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self):
        """ Invoke(self: _InwControlEvents_OnFileOpenEventHandler) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnKeyDownEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnKeyDownEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, key_code, key_data, bHandled):
        """ Invoke(self: _InwControlEvents_OnKeyDownEventHandler, key_code: int, key_data: int) -> bool """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnKeyDownExEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnKeyDownExEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, key_code, key_data, bHandled):
        """ Invoke(self: _InwControlEvents_OnKeyDownExEventHandler, key_code: int, key_data: int) -> object """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnKeyUpEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnKeyUpEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, key_code, key_data, bHandled):
        """ Invoke(self: _InwControlEvents_OnKeyUpEventHandler, key_code: int, key_data: int) -> bool """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnKeyUpExEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnKeyUpExEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, key_code, key_data, bHandled):
        """ Invoke(self: _InwControlEvents_OnKeyUpExEventHandler, key_code: int, key_data: int) -> object """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnLButtonDownEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnLButtonDownEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, Flags, x_coord, y_coord):
        """ Invoke(self: _InwControlEvents_OnLButtonDownEventHandler, Flags: int, x_coord: int, y_coord: int) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnLButtonUpEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnLButtonUpEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, Flags, x_coord, y_coord):
        """ Invoke(self: _InwControlEvents_OnLButtonUpEventHandler, Flags: int, x_coord: int, y_coord: int) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnMButtonDownEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnMButtonDownEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, Flags, x_coord, y_coord):
        """ Invoke(self: _InwControlEvents_OnMButtonDownEventHandler, Flags: int, x_coord: int, y_coord: int) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnMButtonUpEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnMButtonUpEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, Flags, x_coord, y_coord):
        """ Invoke(self: _InwControlEvents_OnMButtonUpEventHandler, Flags: int, x_coord: int, y_coord: int) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnMouseMoveEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnMouseMoveEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, Flags, x_coord, y_coord):
        """ Invoke(self: _InwControlEvents_OnMouseMoveEventHandler, Flags: int, x_coord: int, y_coord: int) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnMouseWheelEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnMouseWheelEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, Flags, delta, x_coord, y_coord):
        """ Invoke(self: _InwControlEvents_OnMouseWheelEventHandler, Flags: int, delta: int, x_coord: int, y_coord: int) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnNavModeChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnNavModeChangedEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, mode):
        """ Invoke(self: _InwControlEvents_OnNavModeChangedEventHandler, mode: int) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnOutOfMemoryEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnOutOfMemoryEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self):
        """ Invoke(self: _InwControlEvents_OnOutOfMemoryEventHandler) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnProgressErrorEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnProgressErrorEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, error_number, description, filename, bCancel, bHandled):
        """ Invoke(self: _InwControlEvents_OnProgressErrorEventHandler, error_number: int, description: str, filename: str) -> (bool, bool) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnProgressPublishedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnProgressPublishedEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, filename, pub_attrib, Password, bHandled):
        """ Invoke(self: _InwControlEvents_OnProgressPublishedEventHandler, filename: str, pub_attrib: object) -> (str, bool) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnSecurityCheckedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnSecurityCheckedEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self):
        """ Invoke(self: _InwControlEvents_OnSecurityCheckedEventHandler) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnSecurityErrorEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnSecurityErrorEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, security_error):
        """ Invoke(self: _InwControlEvents_OnSecurityErrorEventHandler, security_error: int) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnUserContextMenuCmdEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnUserContextMenuCmdEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, cmd_ndx):
        """ Invoke(self: _InwControlEvents_OnUserContextMenuCmdEventHandler, cmd_ndx: int) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_OnXRefResolveEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwControlEvents_OnXRefResolveEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, filename, resolved, bHandled):
        """ Invoke(self: _InwControlEvents_OnXRefResolveEventHandler, filename: str) -> (str, bool) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwControlEvents_SinkHelper(object, _InwControlEvents):
    # no doc
    def OnCertificateDownload(self):
        """ OnCertificateDownload(self: _InwControlEvents_SinkHelper) """
        pass

# Error generating skeleton for function OnContextMenu: sequence item 1: expected string, NoneType found

# Error generating skeleton for function OnContextMenuEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function OnEnableContextMenuCmd: sequence item 1: expected string, NoneType found

# Error generating skeleton for function OnEnableContextMenuCmdEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function OnEnableUserNavMode: sequence item 1: expected string, NoneType found

# Error generating skeleton for function OnEnableUserNavModeEx: sequence item 1: expected string, NoneType found

    def OnFileDownload(self):
        """ OnFileDownload(self: _InwControlEvents_SinkHelper) """
        pass

# Error generating skeleton for function OnFileError: sequence item 1: expected string, NoneType found

    def OnFileOpen(self):
        """ OnFileOpen(self: _InwControlEvents_SinkHelper) """
        pass

# Error generating skeleton for function OnKeyDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function OnKeyDownEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function OnKeyUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function OnKeyUpEx: sequence item 1: expected string, NoneType found

# Error generating skeleton for function OnLButtonDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function OnLButtonUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function OnMButtonDown: sequence item 1: expected string, NoneType found

# Error generating skeleton for function OnMButtonUp: sequence item 1: expected string, NoneType found

# Error generating skeleton for function OnMouseMove: sequence item 1: expected string, NoneType found

# Error generating skeleton for function OnMouseWheel: sequence item 1: expected string, NoneType found

# Error generating skeleton for function OnNavModeChanged: sequence item 1: expected string, NoneType found

    def OnOutOfMemory(self):
        """ OnOutOfMemory(self: _InwControlEvents_SinkHelper) """
        pass

# Error generating skeleton for function OnProgressError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function OnProgressPublished: sequence item 1: expected string, NoneType found

    def OnSecurityChecked(self):
        """ OnSecurityChecked(self: _InwControlEvents_SinkHelper) """
        pass

# Error generating skeleton for function OnSecurityError: sequence item 1: expected string, NoneType found

# Error generating skeleton for function OnUserContextMenuCmd: sequence item 1: expected string, NoneType found

# Error generating skeleton for function OnXRefResolve: sequence item 1: expected string, NoneType found

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    m_dwCookie = None
    m_OnCertificateDownloadDelegate = None
    m_OnContextMenuDelegate = None
    m_OnContextMenuExDelegate = None
    m_OnEnableContextMenuCmdDelegate = None
    m_OnEnableContextMenuCmdExDelegate = None
    m_OnEnableUserNavModeDelegate = None
    m_OnEnableUserNavModeExDelegate = None
    m_OnFileDownloadDelegate = None
    m_OnFileErrorDelegate = None
    m_OnFileOpenDelegate = None
    m_OnKeyDownDelegate = None
    m_OnKeyDownExDelegate = None
    m_OnKeyUpDelegate = None
    m_OnKeyUpExDelegate = None
    m_OnLButtonDownDelegate = None
    m_OnLButtonUpDelegate = None
    m_OnMButtonDownDelegate = None
    m_OnMButtonUpDelegate = None
    m_OnMouseMoveDelegate = None
    m_OnMouseWheelDelegate = None
    m_OnNavModeChangedDelegate = None
    m_OnOutOfMemoryDelegate = None
    m_OnProgressErrorDelegate = None
    m_OnProgressPublishedDelegate = None
    m_OnSecurityCheckedDelegate = None
    m_OnSecurityErrorDelegate = None
    m_OnUserContextMenuCmdDelegate = None
    m_OnXRefResolveDelegate = None


class _InwOpStateEvents:
    # no doc
    def OnCurrentAnimationChanged(self):
        """ OnCurrentAnimationChanged(self: _InwOpStateEvents) """
        pass

    def OnCurrentSceneChanged(self):
        """ OnCurrentSceneChanged(self: _InwOpStateEvents) """
        pass

    def OnCurrentSceneChanging(self):
        """ OnCurrentSceneChanging(self: _InwOpStateEvents) """
        pass

    def OnCurrentSelectionChanged(self):
        """ OnCurrentSelectionChanged(self: _InwOpStateEvents) """
        pass

    def OnCurrentViewChanged(self):
        """ OnCurrentViewChanged(self: _InwOpStateEvents) """
        pass

    def OnCustomChanged(self, custom_name):
        """ OnCustomChanged(self: _InwOpStateEvents, custom_name: str) """
        pass

    def OnPlanViewChanged(self):
        """ OnPlanViewChanged(self: _InwOpStateEvents) """
        pass

    def OnSavedViewsChanged(self):
        """ OnSavedViewsChanged(self: _InwOpStateEvents) """
        pass

    def OnSectionViewChanged(self):
        """ OnSectionViewChanged(self: _InwOpStateEvents) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _InwOpStateEvents_OnCurrentAnimationChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwOpStateEvents_OnCurrentAnimationChangedEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self):
        """ Invoke(self: _InwOpStateEvents_OnCurrentAnimationChangedEventHandler) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwOpStateEvents_OnCurrentSceneChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwOpStateEvents_OnCurrentSceneChangedEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self):
        """ Invoke(self: _InwOpStateEvents_OnCurrentSceneChangedEventHandler) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwOpStateEvents_OnCurrentSceneChangingEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwOpStateEvents_OnCurrentSceneChangingEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self):
        """ Invoke(self: _InwOpStateEvents_OnCurrentSceneChangingEventHandler) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwOpStateEvents_OnCurrentSelectionChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwOpStateEvents_OnCurrentSelectionChangedEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self):
        """ Invoke(self: _InwOpStateEvents_OnCurrentSelectionChangedEventHandler) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwOpStateEvents_OnCurrentViewChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwOpStateEvents_OnCurrentViewChangedEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self):
        """ Invoke(self: _InwOpStateEvents_OnCurrentViewChangedEventHandler) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwOpStateEvents_OnCustomChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwOpStateEvents_OnCustomChangedEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, custom_name):
        """ Invoke(self: _InwOpStateEvents_OnCustomChangedEventHandler, custom_name: str) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwOpStateEvents_OnPlanViewChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwOpStateEvents_OnPlanViewChangedEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self):
        """ Invoke(self: _InwOpStateEvents_OnPlanViewChangedEventHandler) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwOpStateEvents_OnSavedViewsChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwOpStateEvents_OnSavedViewsChangedEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self):
        """ Invoke(self: _InwOpStateEvents_OnSavedViewsChangedEventHandler) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwOpStateEvents_OnSectionViewChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwOpStateEvents_OnSectionViewChangedEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self):
        """ Invoke(self: _InwOpStateEvents_OnSectionViewChangedEventHandler) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwOpStateEvents_SinkHelper(object, _InwOpStateEvents):
    # no doc
    def OnCurrentAnimationChanged(self):
        """ OnCurrentAnimationChanged(self: _InwOpStateEvents_SinkHelper) """
        pass

    def OnCurrentSceneChanged(self):
        """ OnCurrentSceneChanged(self: _InwOpStateEvents_SinkHelper) """
        pass

    def OnCurrentSceneChanging(self):
        """ OnCurrentSceneChanging(self: _InwOpStateEvents_SinkHelper) """
        pass

    def OnCurrentSelectionChanged(self):
        """ OnCurrentSelectionChanged(self: _InwOpStateEvents_SinkHelper) """
        pass

    def OnCurrentViewChanged(self):
        """ OnCurrentViewChanged(self: _InwOpStateEvents_SinkHelper) """
        pass

# Error generating skeleton for function OnCustomChanged: sequence item 1: expected string, NoneType found

    def OnPlanViewChanged(self):
        """ OnPlanViewChanged(self: _InwOpStateEvents_SinkHelper) """
        pass

    def OnSavedViewsChanged(self):
        """ OnSavedViewsChanged(self: _InwOpStateEvents_SinkHelper) """
        pass

    def OnSectionViewChanged(self):
        """ OnSectionViewChanged(self: _InwOpStateEvents_SinkHelper) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    m_dwCookie = None
    m_OnCurrentAnimationChangedDelegate = None
    m_OnCurrentSceneChangedDelegate = None
    m_OnCurrentSceneChangingDelegate = None
    m_OnCurrentSelectionChangedDelegate = None
    m_OnCurrentViewChangedDelegate = None
    m_OnCustomChangedDelegate = None
    m_OnPlanViewChangedDelegate = None
    m_OnSavedViewsChangedDelegate = None
    m_OnSectionViewChangedDelegate = None


class _InwScriptParserEvents:
    # no doc
    def OnScriptError(self, sSource, sDescription, sLine):
        """ OnScriptError(self: _InwScriptParserEvents, sSource: str, sDescription: str, sLine: str) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _InwScriptParserEvents_OnScriptErrorEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ _InwScriptParserEvents_OnScriptErrorEventHandler(: object, : UIntPtr) """
    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.  
         -or-  
         ll, if the method represented by the current delegate does not 
             require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sSource, sDescription, sLine):
        """ Invoke(self: _InwScriptParserEvents_OnScriptErrorEventHandler, sSource: str, sDescription: str, sLine: str) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its invocation list; otherwise, this instance with its original invocation 
             list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: sequence item 1: expected string, NoneType found

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class _InwScriptParserEvents_SinkHelper(object, _InwScriptParserEvents):
    # no doc
# Error generating skeleton for function OnScriptError: sequence item 1: expected string, NoneType found

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    m_dwCookie = None
    m_OnScriptErrorDelegate = None


