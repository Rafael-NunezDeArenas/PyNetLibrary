# encoding: utf-8
# module Autodesk.Navisworks.Api.DocumentParts calls itself DocumentParts
# from Autodesk.Navisworks.Api, Version=19.0.1374.1, Culture=neutral, PublicKeyToken=d85e58fa5af9b484
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DocumentCurrentComments(object):
    """ Stores the Current Comments information contained in a Autodesk.Navisworks.Api.DocumentDocument. """
    def ChangeSource(self, sourceOwner, sourceComments, activeCommentIndex=None):
        """
        ChangeSource(self: DocumentCurrentComments, sourceOwner: str, sourceComments: CommentCollection)
            Changes the Current Autodesk.Navisworks.Api.CommentCollectionComments.
        Typically called when the focus changes from one Comment Source to an other.
        
            sourceOwner: Internal string representing the owner of the comments.
            sourceComments: The Comments.
        ChangeSource(self: DocumentCurrentComments, sourceOwner: str, sourceComments: CommentCollection, activeCommentIndex: int)
            Changes the Current Autodesk.Navisworks.Api.CommentCollectionComments.
        Typically called when the focus changes from one Comment Source to an other.
        
            sourceOwner: Internal string representing the owner of the comments.
            sourceComments: The Comments.
            activeCommentIndex: The Comment to select.
        """
        pass

    def ClearSource(self):
        """
        ClearSource(self: DocumentCurrentComments)
            Sets situation that there is no owner, comments are cleared and editing prevented.
        """
        pass

    def CopyFrom(self, comments):
        """
        CopyFrom(self: DocumentCurrentComments, comments: CommentCollection)
            Copies the Autodesk.Navisworks.Api.CommentCollectionCommentCollection from comments.
        """
        pass

    def CreateCopy(self):
        """
        CreateCopy(self: DocumentCurrentComments) -> CommentCollection
        
            Creates a copy of the Autodesk.Navisworks.Api.CommentCollectionCommentCollection associated with this object.
        """
        pass

    def ToCommentCollection(self):
        """
        ToCommentCollection(self: DocumentCurrentComments) -> CommentCollection
        
            Explicit form of conversion operator returning Autodesk.Navisworks.Api.DocumentParts.DocumentCurrentComments.Value.
        """
        pass

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Internal string representing the owner of the comments.

Get: Owner(self: DocumentCurrentComments) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value of the current Autodesk.Navisworks.Api.CommentCollectionCommentsCollection within the Document.

Get: Value(self: DocumentCurrentComments) -> CommentCollection

"""


    Changed = None
    Changing = None


class DocumentCurrentMeasurement(object):
    """ The current measurement state in a Document """
    def AddRedlinesToCurrentSavedViewpoint(self):
        """
        AddRedlinesToCurrentSavedViewpoint(self: DocumentCurrentMeasurement)
            Converts the measurement to redlines. Then adds the redlines to the current saved viewpoint.
        If there is no current saved viewpoint, then one is created.
        """
        pass

    CanConvertToRedlines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if the measurement can be converted to redlines

Get: CanConvertToRedlines(self: DocumentCurrentMeasurement) -> bool

"""

    Difference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the difference

Get: Difference(self: DocumentCurrentMeasurement) -> Vector3D

"""

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the end point

Get: EndPoint(self: DocumentCurrentMeasurement) -> Point3D

"""

    FirstPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the first point

Get: FirstPoint(self: DocumentCurrentMeasurement) -> Point3D

"""

    HasDifference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if the difference is available

Get: HasDifference(self: DocumentCurrentMeasurement) -> bool

"""

    HasEndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if the end point is available

Get: HasEndPoint(self: DocumentCurrentMeasurement) -> bool

"""

    HasFirstPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if the first point is available

Get: HasFirstPoint(self: DocumentCurrentMeasurement) -> bool

"""

    HasMeasurement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if the MeasurementValue and MeasurementType are available

Get: HasMeasurement(self: DocumentCurrentMeasurement) -> bool

"""

    MeasurementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the measurement type

Get: MeasurementType(self: DocumentCurrentMeasurement) -> MeasurementType

"""

    MeasurementValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the measurement value

Get: MeasurementValue(self: DocumentCurrentMeasurement) -> float

"""

    Tool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the measurement tool in use

Get: Tool(self: DocumentCurrentMeasurement) -> Tool

"""

    ToolMeasurementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the tool measurement type

Get: ToolMeasurementType(self: DocumentCurrentMeasurement) -> MeasurementType

"""



class DocumentCurrentSearch(object):
    """ The current search in a Document """
    def Clear(self):
        """
        Clear(self: DocumentCurrentSearch)
            Clears the current search
        """
        pass

    def CopyFrom(self, search):
        """
        CopyFrom(self: DocumentCurrentSearch, search: Search)
            Copies the Autodesk.Navisworks.Api.SearchSearch from search
        """
        pass

    def CreateCopy(self):
        """
        CreateCopy(self: DocumentCurrentSearch) -> Search
        
            Creates a copy of the Autodesk.Navisworks.Api.SearchSearch associated with this object
        """
        pass

    def ToSearch(self):
        """
        ToSearch(self: DocumentCurrentSearch) -> Search
        
            Explicit form of conversion operator returning Autodesk.Navisworks.Api.DocumentParts.DocumentCurrentSearch.Value
        """
        pass

    IsClear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true when there is no selection or search conditions in the search

Get: IsClear(self: DocumentCurrentSearch) -> bool

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value of the current Autodesk.Navisworks.Api.Searchsearch within the document

Get: Value(self: DocumentCurrentSearch) -> Search

"""


    Changed = None
    Changing = None


class DocumentCurrentSelection(object):
    """ The current selection in a Document """
    def Add(self, item):
        """
        Add(self: DocumentCurrentSelection, item: ModelItem)
            Adds a Autodesk.Navisworks.Api.ModelItemModelItem to the Autodesk.Navisworks.Api.SelectionSelection
        
            item: The Autodesk.Navisworks.Api.ModelItemModelItem we wish to add to the selection
        """
        pass

    def AddRange(self, range):
        """ AddRange(self: DocumentCurrentSelection, range: IEnumerable[ModelItem]) """
        pass

    def Clear(self):
        """
        Clear(self: DocumentCurrentSelection)
            Removes all entries from
        """
        pass

    def CopyFrom(self, *__args):
        """
        CopyFrom(self: DocumentCurrentSelection, from: IEnumerable[ModelItem])CopyFrom(self: DocumentCurrentSelection, from: ModelItemCollection)
            Copies the Autodesk.Navisworks.Api.ModelItemModelItems from a Autodesk.Navisworks.Api.ModelItemCollectionModelItemCollection and replaces the list of entries held 
        in 
             Autodesk.Navisworks.Api.DocumentParts.DocumentCurrentSelection.SelectedItemsSelectedItems
        
        
            from: The Autodesk.Navisworks.Api.ModelItemModelItems to reference for this operation
        CopyFrom(self: DocumentCurrentSelection, selectionSources: SelectionSourceCollection)
            Updates the SelectionSources in Autodesk.Navisworks.Api.SelectionSelection from selectionSources and
        replaces the list of entries held in 
             Autodesk.Navisworks.Api.DocumentParts.DocumentCurrentSelection.SelectedItemsSelectedItems
        
        CopyFrom(self: DocumentCurrentSelection, selection: Selection)
            Copies the Autodesk.Navisworks.Api.SelectionSelection from selection and replaces the list of entries held 
        in 
             Autodesk.Navisworks.Api.DocumentParts.DocumentCurrentSelection.SelectedItemsSelectedItems
        """
        pass

    def CreateCopy(self):
        """
        CreateCopy(self: DocumentCurrentSelection) -> Selection
        
            Creates a copy of the Autodesk.Navisworks.Api.SelectionSelection associated with this object
        """
        pass

    def Remove(self, item):
        """
        Remove(self: DocumentCurrentSelection, item: ModelItem)
            Removes a Autodesk.Navisworks.Api.ModelItemModelItem from the Autodesk.Navisworks.Api.SelectionSelection
        
            item: The Autodesk.Navisworks.Api.ModelItemModelItems we wish to remove from the selection
        """
        pass

    def SelectAll(self):
        """
        SelectAll(self: DocumentCurrentSelection)
            Selects all the Autodesk.Navisworks.Api.ModelItemModelItems in the current document
        """
        pass

    def ToSelection(self):
        """
        ToSelection(self: DocumentCurrentSelection) -> Selection
        
            Explicit form of conversion operator returning Autodesk.Navisworks.Api.DocumentParts.DocumentCurrentSelection.Value
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true when there are no Autodesk.Navisworks.Api.ModelItemModelItems in the selection

Get: IsEmpty(self: DocumentCurrentSelection) -> bool

"""

    SelectedItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Collection of instances of Autodesk.Navisworks.Api.ModelItemModelItem in this Selection

Get: SelectedItems(self: DocumentCurrentSelection) -> ModelItemCollection

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value of the current Autodesk.Navisworks.Api.Selectionselection within the document

Get: Value(self: DocumentCurrentSelection) -> Selection

"""


    Changed = None
    Changing = None


class DocumentCurrentViewpoint(object):
    """ The Current Viewpoint in a Document """
    def CopyFrom(self, viewpoint):
        """
        CopyFrom(self: DocumentCurrentViewpoint, viewpoint: Viewpoint)
            Copies the Autodesk.Navisworks.Api.ViewpointViewpoint from viewpoint int the one in the Document
        """
        pass

    def CreateCopy(self):
        """
        CreateCopy(self: DocumentCurrentViewpoint) -> Viewpoint
        
            Creates a copy of the Autodesk.Navisworks.Api.ViewpointViewpoint associated with this object
        """
        pass

    def ToViewpoint(self):
        """
        ToViewpoint(self: DocumentCurrentViewpoint) -> Viewpoint
        
            Explicit form of conversion operator returning Autodesk.Navisworks.Api.DocumentParts.DocumentCurrentViewpoint.Value
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value of the current Autodesk.Navisworks.Api.ViewpointViewpoint within the document

Get: Value(self: DocumentCurrentViewpoint) -> Viewpoint

"""


    Changed = None
    Changing = None


class DocumentDatabase(object, IDisposable):
    """ The embedded database in a Document """
    def BeginTransaction(self, action):
        """
        BeginTransaction(self: DocumentDatabase, action: DatabaseChangedAction) -> NavisworksTransaction
        
            Begin a transaction.
        
            action: Determines which action should do after commit transaction, Autodesk.Navisworks.Api.Data.DatabaseChangedActionDatabaseChangedAction
            Returns: If success return Autodesk.Navisworks.Api.Data.NavisworksTransactionNavisworksTransaction, if failed, return null
        """
        pass

    def Dispose(self):
        """ Dispose(self: DocumentDatabase) """
        pass

    def EnableTableUndoable(self, tableName):
        """
        EnableTableUndoable(self: DocumentDatabase, tableName: str)
            Enable table to undoable or redoable.
        """
        pass

    def ToNavisworksConnection(self):
        """
        ToNavisworksConnection(self: DocumentDatabase) -> NavisworksConnection
        
            Explicit form of conversion operator returning Autodesk.Navisworks.Api.DocumentParts.DocumentDatabase.Value
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

    ExistLiveTransaction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If is in a transaction.

Get: ExistLiveTransaction(self: DocumentDatabase) -> bool

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value of the Autodesk.Navisworks.Api.Data.NavisworksConnectionNavisworksConnection of embedded database in the document

Get: Value(self: DocumentDatabase) -> NavisworksConnection

"""


    Changed = None
    Changing = None
    Loaded = None
    TransactionBeginning = None
    TransactionBegun = None
    TransactionCommitting = None
    TransactionRollingBack = None
    Unloading = None


class DocumentGrids(object):
    """ Stores the Grids information contained in a Document. """
    def SetSystemLockedLevel(self, system, level):
        """
        SetSystemLockedLevel(self: DocumentGrids, system: GridSystem, level: GridLevel)
            Sets the LockedLevel for a particular System.
        """
        pass

    ActiveSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The GridSystem that will be rendered.

Get: ActiveSystem(self: DocumentGrids) -> GridSystem

Set: ActiveSystem(self: DocumentGrids) = value
"""

    RenderMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The GridSystem that will be rendered.

Get: RenderMode(self: DocumentGrids) -> GridsRenderMode

Set: RenderMode(self: DocumentGrids) = value
"""

    Systems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The collection of all GridSystems within the Document.

Get: Systems(self: DocumentGrids) -> GridSystemCollection

"""


    Changed = None
    Changing = None


class DocumentHyperlinks(object):
    """ Stores the Hyperlinks information contained in a Document. """
    def DeleteHyperlinks(self, modelItem):
        """
        DeleteHyperlinks(self: DocumentHyperlinks, modelItem: ModelItem)
            Deletes all hyperlinks from a ModelItem.
        """
        pass

    def GetHyperlinks(self, modelItem):
        """
        GetHyperlinks(self: DocumentHyperlinks, modelItem: ModelItem) -> HyperlinkCollection
        
            Gets hyperlinks for a ModelItem.
        """
        pass

    def ResetAllHyperlinks(self):
        """
        ResetAllHyperlinks(self: DocumentHyperlinks)
            Resets hyperlinks on all ModelItems.
        """
        pass

    def ResetHyperlinks(self, modelItem):
        """
        ResetHyperlinks(self: DocumentHyperlinks, modelItem: ModelItem)
            Resets hyperlinks on a ModelItem back to their original state.
        """
        pass

    def SetHyperlinks(self, modelItem, links):
        """
        SetHyperlinks(self: DocumentHyperlinks, modelItem: ModelItem, links: HyperlinkCollection)
            Sets hyperlinks for a ModelItem from a list of hyperlinks.
        """
        pass

    Changed = None
    Changing = None


class DocumentInfoPart(object):
    """ The DocumentInfo stored in a Document """
    def AddCopy(self, *__args):
        """
        AddCopy(self: DocumentInfoPart, parent: GroupItem, item: SavedItem)
            Adds a copy of item to the end of the specified parent group contained by DocumentInfo.
        
            parent: The parent group to add to. RootItem or null to add directly to Value
        AddCopy(self: DocumentInfoPart, item: SavedItem)
            Adds a copy of item to the end of Value.
        """
        pass

    def AddUniqueCopy(self, item, sourceFileName):
        """
        AddUniqueCopy(self: DocumentInfoPart, item: SavedItem, sourceFileName: str)
            Adds an unique copy of item to the end of Value
        
            sourceFileName: If the parent group have the same name, will add it to item name
        """
        pass

    def CreateCopy(self):
        """
        CreateCopy(self: DocumentInfoPart) -> DocumentInfo
        
            Creates a copy of Autodesk.Navisworks.Api.DocumentParts.DocumentInfoPart.Value
        """
        pass

    def EditDisplayName(self, item, newDisplayName):
        """
        EditDisplayName(self: DocumentInfoPart, item: SavedItem, newDisplayName: str)
            Edit item and update it's DisplayName
        """
        pass

    def InsertCopy(self, *__args):
        """
        InsertCopy(self: DocumentInfoPart, parent: GroupItem, index: int, item: SavedItem)
            Inserts a copy of item into the specified parent group contained by DocumentInfo.
        
            parent: The parent group to insert into. RootItem or null to insert directly into Value
        InsertCopy(self: DocumentInfoPart, index: int, item: SavedItem)
            Inserts a copy of item into Value.
        """
        pass

    def InsertUniqueCopy(self, parent, index, item, sourceFileName):
        """
        InsertUniqueCopy(self: DocumentInfoPart, parent: GroupItem, index: int, item: SavedItem, sourceFileName: str)
            Inserts a copy of item into the specified parent group contained by DocumentInfo. If have same sheet, will reset id and rename
        
            parent: The parent group to insert into. RootItem or null to insert directly into Value
            sourceFileName: If the parent group have the same name, will add it to item name
        """
        pass

    def Move(self, *__args):
        """
        Move(self: DocumentInfoPart, oldParent: GroupItem, oldIndex: int, newParent: GroupItem, newIndex: int)
            Moves item at oldIndex in OldParent to newIndex in newParent
        
            oldParent: The parent group to move the item from.
            newParent: The parent group to move to.
        If newParent is equal to oldParent, the item will be moved within the same SavedItemCollection.
        Move(self: DocumentInfoPart, oldIndex: int, newIndex: int)
            Move sheet from oldIndex to new position in collection.
        
            oldIndex: The sheet in this position to move
            newIndex: The moved sheet place in this position
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: DocumentInfoPart, parent: GroupItem, item: SavedItem) -> bool
        
            Removes specified item from the specified parent group contained by DocumentInfo.
        
            parent: The parent group to remove from. null to remove directly from DocumentInfo
            Returns: false if item not found in DocumentInfo
        Remove(self: DocumentInfoPart, item: SavedItem) -> bool
        
            Removes specified item from DocumentInfo.
            Returns: false if item not found in DocumentInfo
        """
        pass

    def RemoveAt(self, *__args):
        """
        RemoveAt(self: DocumentInfoPart, parent: GroupItem, index: int)
            Removes item from the specified parent group contained by DocumentInfo.
        
            parent: The parent group to remove from. RootItem or null to remove directly from DocumentInfo
        RemoveAt(self: DocumentInfoPart, index: int)
            Removes item at the specified index from DocumentInfo.
        """
        pass

    def ReplaceWithCopy(self, *__args):
        """
        ReplaceWithCopy(self: DocumentInfoPart, parent: GroupItem, index: int, item: SavedItem)
            Replaces item from the specified parent group with a copy of item
        
            parent: The parent group to insert into. RootItem or null to insert directly into Value
        ReplaceWithCopy(self: DocumentInfoPart, index: int, item: SavedItem)
            Replaces item at given index within DocumentInfo with a copy of item
        """
        pass

    def ToDocumentInfo(self):
        """
        ToDocumentInfo(self: DocumentInfoPart) -> DocumentInfo
        
            Explicit form of conversion operator returning Autodesk.Navisworks.Api.DocumentParts.DocumentInfoPart.Value
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value of the current Autodesk.Navisworks.Api.DocumentInfoDocumentInfo within the document

Get: Value(self: DocumentInfoPart) -> DocumentInfo

"""


    Changed = None
    Changing = None


class DocumentModels(object, IList[Model], ICollection[Model], IEnumerable[Model], IEnumerable):
    """ Stores the collection of Models contained in a Document """
    def Contains(self, item):
        """
        Contains(self: DocumentModels, item: Model) -> bool
        
            Determines whether the collection contains a specific value.
        
            item: The Model to locate in the collection.
            Returns: true if item is found in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, *__args):
        """
        CopyTo(self: DocumentModels, to: ICollection[Model])CopyTo(self: DocumentModels, array: Array[Model], arrayIndex: int)
            Copies the elements of the System.Collections.Generic.ICollection to an System.Array, starting at a particular System.Array index.
        
            array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.Generic.ICollection. The System.Array must have zero-based indexing.
            arrayIndex: The zero-based index in array at which copying begins.
        """
        pass

    def CreateCollection(self):
        """
        CreateCollection(self: DocumentModels) -> ModelItemCollection
        
            Returns an empty collection associated with this Document
        """
        pass

    def CreateCollectionFromRootItems(self):
        """
        CreateCollectionFromRootItems(self: DocumentModels) -> ModelItemCollection
        
            Returns a snapshot collection containing the RootItem from each Autodesk.Navisworks.Api.Model
        """
        pass

    def CreateIndexPath(self, item):
        """
        CreateIndexPath(self: DocumentModels, item: ModelItem) -> Collection[int]
        
            Returns a collection of indices that defines a path from the root item through its
        descendants to the specified item.
        """
        pass

    def CreatePathId(self, item):
        """
        CreatePathId(self: DocumentModels, item: ModelItem) -> ModelItemPathId
        
            Return the path identifier that defines a path from the root item through its
        descendants to the specified item, and the model index this item belongs to.
        """
        pass

    def FindIdForModelItem(self, item):
        """
        FindIdForModelItem(self: DocumentModels, item: ModelItem) -> UInt64
        
            Returns numeric ID for a given model item.
            Returns: ID for model item, or 0 if no ID.
        """
        pass

    def FindModelItemsById(self, modelIndex, id):
        """
        FindModelItemsById(self: DocumentModels, modelIndex: int, id: UInt64) -> ModelItemCollection
        
            Returns collection of model items that have a given numeric ID.
            Returns: Model item collection containing requested items (if any).
        """
        pass

    def GetAllHiddenAtModelState(self):
        """
        GetAllHiddenAtModelState(self: DocumentModels) -> ModelItemCollection
        
            Gets the hidden status as defined by the constituent models.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: DocumentModels) -> IEnumerator[Model]
        
            Returns an enumerator that can iterate through the collection.
            Returns: An System.Collections.IEnumeratorIEnumerator that can be used to iterate through the collection.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: DocumentModels, item: Model) -> int
        
            Determines the index of a specific item in the DocumentModels.
        """
        pass

    def InternalAdd(self, model):
        """ InternalAdd(self: DocumentModels, model: Model) """
        pass

    def InternalClear(self):
        """ InternalClear(self: DocumentModels) """
        pass

    def InternalGetEnumerator(self):
        """ InternalGetEnumerator(self: DocumentModels) -> IEnumerator """
        pass

    def InternalInsert(self, index, item):
        """ InternalInsert(self: DocumentModels, index: int, item: Model) """
        pass

    def InternalRemove(self, item):
        """ InternalRemove(self: DocumentModels, item: Model) -> bool """
        pass

    def InternalRemoveAt(self, index):
        """ InternalRemoveAt(self: DocumentModels, index: int) """
        pass

    def IsFrozen(self, items):
        """ IsFrozen(self: DocumentModels, items: IEnumerable[ModelItem]) -> bool """
        pass

    def IsHidden(self, items):
        """ IsHidden(self: DocumentModels, items: IEnumerable[ModelItem]) -> bool """
        pass

    def IsRequired(self, items):
        """ IsRequired(self: DocumentModels, items: IEnumerable[ModelItem]) -> bool """
        pass

    def OverridePermanentColor(self, items, color):
        """ OverridePermanentColor(self: DocumentModels, items: IEnumerable[ModelItem], color: Color) """
        pass

    def OverridePermanentTransform(self, items, transform, updateModelTransform):
        """ OverridePermanentTransform(self: DocumentModels, items: IEnumerable[ModelItem], transform: Transform3D, updateModelTransform: bool) """
        pass

    def OverridePermanentTransparency(self, items, transparency):
        """ OverridePermanentTransparency(self: DocumentModels, items: IEnumerable[ModelItem], transparency: float) """
        pass

    def OverrideTemporaryColor(self, items, color):
        """ OverrideTemporaryColor(self: DocumentModels, items: IEnumerable[ModelItem], color: Color) """
        pass

    def OverrideTemporaryTransparency(self, items, transparency):
        """ OverrideTemporaryTransparency(self: DocumentModels, items: IEnumerable[ModelItem], transparency: float) """
        pass

    def ResetAllFrozen(self):
        """
        ResetAllFrozen(self: DocumentModels)
            Clears the IsFrozen property on all items in the models.
        """
        pass

    def ResetAllHidden(self):
        """
        ResetAllHidden(self: DocumentModels)
            Clears the IsHidden property on all items in the models.
        """
        pass

    def ResetAllHiddenToModelState(self):
        """
        ResetAllHiddenToModelState(self: DocumentModels)
            Resets the hidden status to that defined in the constituent models.
        """
        pass

    def ResetAllPermanentMaterials(self):
        """
        ResetAllPermanentMaterials(self: DocumentModels)
            Resets permanent material properties (color and transparency) of 
        all Autodesk.Navisworks.Api.ModelGeometryModelGeometry in the models.
        """
        pass

    def ResetAllPermanentTransforms(self):
        """
        ResetAllPermanentTransforms(self: DocumentModels)
            Reset incremental transforms for all model items contained in the entire model.
        """
        pass

    def ResetAllRequired(self):
        """
        ResetAllRequired(self: DocumentModels)
            Clears the IsRequired property on all items in the models.
        """
        pass

    def ResetAllTemporaryMaterials(self):
        """
        ResetAllTemporaryMaterials(self: DocumentModels)
            Resets temporary material properties (color and transparency) of 
        all Autodesk.Navisworks.Api.ModelGeometryModelGeometry in the models.
        """
        pass

    def ResetPermanentMaterials(self, items):
        """ ResetPermanentMaterials(self: DocumentModels, items: IEnumerable[ModelItem]) """
        pass

    def ResetPermanentTransform(self, items):
        """ ResetPermanentTransform(self: DocumentModels, items: IEnumerable[ModelItem]) """
        pass

    def ResetTemporaryMaterials(self, items):
        """ ResetTemporaryMaterials(self: DocumentModels, items: IEnumerable[ModelItem]) """
        pass

    def ResolveIndexPath(self, path):
        """ ResolveIndexPath(self: DocumentModels, path: IEnumerable[int]) -> ModelItem """
        pass

    def ResolvePathId(self, pathId):
        """
        ResolvePathId(self: DocumentModels, pathId: ModelItemPathId) -> ModelItem
        
            Returns the saved item referenced by a model index and a path identifier that
        define a path from the root item through its descendants to the specified item.
            Returns: null if source cannot be resolved
        """
        pass

    def SetFrozen(self, items, value):
        """ SetFrozen(self: DocumentModels, items: IEnumerable[ModelItem], value: bool) """
        pass

    def SetHidden(self, items, value):
        """ SetHidden(self: DocumentModels, items: IEnumerable[ModelItem], value: bool) """
        pass

    def SetModelUnitsAndTransform(self, model, units, transform, transformReflected):
        """
        SetModelUnitsAndTransform(self: DocumentModels, model: Model, units: Units, transform: Transform3D, transformReflected: bool)
            Sets the model units and transform.
        """
        pass

    def SetRequired(self, items, value):
        """ SetRequired(self: DocumentModels, items: IEnumerable[ModelItem], value: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[Model], item: Model) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements contained in the collection.

Get: Count(self: DocumentModels) -> int

"""

    First = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the first Autodesk.Navisworks.Api.ModelModel in the collection, returns null if the collection is empty

Get: First(self: DocumentModels) -> Model

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the collection is read-only.

Get: IsReadOnly(self: DocumentModels) -> bool

"""

    RootItemDescendants = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """All descendants of RootItems (excluding the RootItems themselves).

Get: RootItemDescendants(self: DocumentModels) -> ModelItemEnumerableCollection

"""

    RootItemDescendantsAndSelf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """All descendants of RootItems (including the RootItems themselves).

Get: RootItemDescendantsAndSelf(self: DocumentModels) -> ModelItemEnumerableCollection

"""

    RootItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The RootItem from each model

Get: RootItems(self: DocumentModels) -> ModelItemEnumerableCollection

"""


    CollectionChanged = None
    CollectionChanging = None
    ModelGeometryMaterialChanged = None
    ModelItemPropertiesChanged = None


class DocumentSavedViewpoints(object):
    """ The saved viewpoints stored in a Autodesk.Navisworks.Api.DocumentDocument. """
    def AddComment(self, item, comment):
        """
        AddComment(self: DocumentSavedViewpoints, item: SavedItem, comment: Comment)
            Edit item and add Comment to item's Comments
        """
        pass

    def AddCopy(self, *__args):
        """
        AddCopy(self: DocumentSavedViewpoints, parent: GroupItem, item: SavedItem)
            Adds a copy of item to the end of the specified parent group contained by SavedViewpoints.
        
            parent: The parent group to add to. RootItem or null to add directly to Value
        AddCopy(self: DocumentSavedViewpoints, item: SavedItem)
            Adds a copy of item to the end of Value.
        """
        pass

    def CaptureRuntimeOverrides(self):
        """
        CaptureRuntimeOverrides(self: DocumentSavedViewpoints) -> SavedViewpoint
        
            Creates a view that captures current runtime overrides.
        """
        pass

    def Clear(self):
        """
        Clear(self: DocumentSavedViewpoints)
            Removes all items in Value
        """
        pass

    def CopyFrom(self, value):
        """
        CopyFrom(self: DocumentSavedViewpoints, value: SavedItemCollection)
            Copies the Autodesk.Navisworks.Api.SelectionSavedViewpoints from value and 
        replaces the list of entries held in 
             Autodesk.Navisworks.Api.DocumentParts.DocumentSavedViewpoints.Value.
        
        CopyFrom(self: DocumentSavedViewpoints, value: IEnumerable[SavedItem])
        """
        pass

    def CreateCopy(self):
        """
        CreateCopy(self: DocumentSavedViewpoints) -> Collection[SavedItem]
        
            Creates a copy of the Autodesk.Navisworks.Api.SavedViewpointSavedViewpoints associated with this object
        """
        pass

    def CreateIndexPath(self, item):
        """
        CreateIndexPath(self: DocumentSavedViewpoints, item: SavedItem) -> Collection[int]
        
            Returns a collection of indices that defines a path from the root item through its
        descendents to the specified item.
        """
        pass

    def CreateReference(self, item):
        """
        CreateReference(self: DocumentSavedViewpoints, item: SavedItem) -> SavedItemReference
        
            Returns a reference to a saved item.
        """
        pass

    def EditComments(self, item, newComments):
        """
        EditComments(self: DocumentSavedViewpoints, item: SavedItem, newComments: CommentCollection)
            Edit item and update it's Comments
        """
        pass

    def EditDisplayName(self, item, newDisplayName):
        """
        EditDisplayName(self: DocumentSavedViewpoints, item: SavedItem, newDisplayName: str)
            Edit item and update it's DisplayName
        """
        pass

    def InsertCopy(self, *__args):
        """
        InsertCopy(self: DocumentSavedViewpoints, parent: GroupItem, index: int, item: SavedItem)
            Inserts a copy of item into the specified parent group contained by SavedViewpoints.
        
            parent: The parent group to insert into. RootItem or null to insert directly into Value
        InsertCopy(self: DocumentSavedViewpoints, index: int, item: SavedItem)
            Inserts a copy of item into Value.
        """
        pass

    def Move(self, *__args):
        """
        Move(self: DocumentSavedViewpoints, oldParent: GroupItem, oldIndex: int, newParent: GroupItem, newIndex: int)
            Moves item at oldIndex in OldParent to newIndex in newParent
        
            oldParent: The parent group to move the item from. RootItem or null to remove directly from Value
            newParent: The parent group to move to. RootItem or null to move directly into Value. 
        If newParent is equal to oldParent, the item will be moved within the same SavedItemCollection.
        Move(self: DocumentSavedViewpoints, oldIndex: int, newIndex: int)
            Moves item from oldIndex to newIndex within Value
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: DocumentSavedViewpoints, parent: GroupItem, item: SavedItem) -> bool
        
            Removes specified item from the specified parent group contained by SavedViewpoints.
        
            parent: The parent group to remove from. RootItem or null to remove directly from Value
            Returns: false if item not found in Value
        Remove(self: DocumentSavedViewpoints, item: SavedItem) -> bool
        
            Removes specified item from Value.
            Returns: false if item not found in Value
        """
        pass

    def RemoveAt(self, *__args):
        """
        RemoveAt(self: DocumentSavedViewpoints, parent: GroupItem, index: int)
            Removes item from the specified parent group contained by SavedViewpoints.
        
            parent: The parent group to remove from. RootItem or null to remove directly from Value
        RemoveAt(self: DocumentSavedViewpoints, index: int)
            Removes item at the specified index from Value.
        """
        pass

    def ReplaceFromCurrentView(self, savedViewpoint):
        """
        ReplaceFromCurrentView(self: DocumentSavedViewpoints, savedViewpoint: SavedViewpoint)
            Replaces the SavedViewpoint within Value with an updated copy.
        Viewpoint, Redlines and visibility are updated to those in the current View.
        """
        pass

    def ReplaceWithCopy(self, *__args):
        """
        ReplaceWithCopy(self: DocumentSavedViewpoints, parent: GroupItem, index: int, item: SavedItem)
            Replaces item from the specified parent group with a copy of item
        
            parent: The parent group to insert into. RootItem or null to insert directly into Value
        ReplaceWithCopy(self: DocumentSavedViewpoints, index: int, item: SavedItem)
            Replaces item at given index within Value with a copy of item
        """
        pass

    def ResolveGuid(self, value):
        """
        ResolveGuid(self: DocumentSavedViewpoints, value: Guid) -> SavedItem
        
            Returns the saved item referenced by a guid.
        """
        pass

    def ResolveIndexPath(self, path):
        """ ResolveIndexPath(self: DocumentSavedViewpoints, path: IEnumerable[int]) -> SavedItem """
        pass

    def ResolveReference(self, reference):
        """
        ResolveReference(self: DocumentSavedViewpoints, reference: SavedItemReference) -> SavedItem
        
            Returns the saved item referenced by a SavedItemReference.
        """
        pass

    def ToSavedItemCollection(self):
        """
        ToSavedItemCollection(self: DocumentSavedViewpoints) -> SavedItemCollection
        
            Explicit form of conversion operator returning Autodesk.Navisworks.Api.DocumentParts.DocumentSavedViewpoints.Value
        """
        pass

    CurrentSavedViewpoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current item as displayed in the GUI. Must exist in Autodesk.Navisworks.Api.DocumentParts.DocumentSavedViewpoints.Value or be null.

Get: CurrentSavedViewpoint(self: DocumentSavedViewpoints) -> SavedItem

Set: CurrentSavedViewpoint(self: DocumentSavedViewpoints) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The internal identifier for this type of document part.

Get: Id(self: DocumentSavedViewpoints) -> str

"""

    RootItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Autodesk.Navisworks.Api.DocumentParts.DocumentSavedViewpoints.Value as the children of a Autodesk.Navisworks.Api.FolderItem

Get: RootItem(self: DocumentSavedViewpoints) -> FolderItem

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The collection of SavedViewpoints stored in the Document

Get: Value(self: DocumentSavedViewpoints) -> SavedItemCollection

"""


    Changed = None
    Changing = None
    CurrentSavedViewpointChanged = None


class DocumentSelectionSets(object):
    """ The SelectionSets stored in a Document """
    def AddComment(self, item, comment):
        """
        AddComment(self: DocumentSelectionSets, item: SavedItem, comment: Comment)
            Edit item and add Comment to item's Comments
        """
        pass

    def AddCopy(self, *__args):
        """
        AddCopy(self: DocumentSelectionSets, parent: GroupItem, item: SavedItem)
            Adds a copy of item to the end of the specified parent group contained by SelectionSets.
        
            parent: The parent group to add to. RootItem or null to add directly to Value
        AddCopy(self: DocumentSelectionSets, item: SavedItem)
            Adds a copy of item to the end of Value.
        """
        pass

    def Clear(self):
        """
        Clear(self: DocumentSelectionSets)
            Removes all items in Value
        """
        pass

    def CopyFrom(self, value):
        """
        CopyFrom(self: DocumentSelectionSets, value: SavedItemCollection)
            Copies the Autodesk.Navisworks.Api.SelectionSelectionSets from value and 
        replaces the list of entries held in Autodesk.Navisworks.Api.DocumentParts.DocumentSelectionSets.Value.
        CopyFrom(self: DocumentSelectionSets, value: IEnumerable[SavedItem])
        """
        pass

    def CreateCopy(self):
        """
        CreateCopy(self: DocumentSelectionSets) -> Collection[SavedItem]
        
            Creates a copy of the Autodesk.Navisworks.Api.SelectionSetSelectionSets associated with this object
        """
        pass

    def CreateIndexPath(self, item):
        """
        CreateIndexPath(self: DocumentSelectionSets, item: SavedItem) -> Collection[int]
        
            Returns a collection of indices that defines a path from the root item through its
        descendents to the specified item.
        """
        pass

    def CreateReference(self, item):
        """
        CreateReference(self: DocumentSelectionSets, item: SavedItem) -> SavedItemReference
        
            Returns a reference to a saved item.
        """
        pass

    def CreateSelectionSource(self, item):
        """
        CreateSelectionSource(self: DocumentSelectionSets, item: SavedItem) -> SelectionSource
        
            Returns a selection source that refers to the selection defined by a Selection Set
        or folder of Selection Sets.
        """
        pass

    def EditComments(self, item, newComments):
        """
        EditComments(self: DocumentSelectionSets, item: SavedItem, newComments: CommentCollection)
            Edit item and update it's Comments
        """
        pass

    def EditDisplayName(self, item, newDisplayName):
        """
        EditDisplayName(self: DocumentSelectionSets, item: SavedItem, newDisplayName: str)
            Edit item and update it's DisplayName
        """
        pass

    def InsertCopy(self, *__args):
        """
        InsertCopy(self: DocumentSelectionSets, parent: GroupItem, index: int, item: SavedItem)
            Inserts a copy of item into the specified parent group contained by SelectionSets.
        
            parent: The parent group to insert into. RootItem or null to insert directly into Value
        InsertCopy(self: DocumentSelectionSets, index: int, item: SavedItem)
            Inserts a copy of item into Value.
        """
        pass

    def Move(self, *__args):
        """
        Move(self: DocumentSelectionSets, oldParent: GroupItem, oldIndex: int, newParent: GroupItem, newIndex: int)
            Moves item at oldIndex in OldParent to newIndex in newParent
        
            oldParent: The parent group to move the item from. RootItem or null to remove directly from Value
            newParent: The parent group to move to. RootItem or null to move directly into Value. 
        If newParent is equal to oldParent, the item will be moved within the same SavedItemCollection.
        Move(self: DocumentSelectionSets, oldIndex: int, newIndex: int)
            Moves item from oldIndex to newIndex within Value
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: DocumentSelectionSets, parent: GroupItem, item: SavedItem) -> bool
        
            Removes specified item from the specified parent group contained by SelectionSets.
        
            parent: The parent group to remove from. RootItem or null to remove directly from Value
            Returns: false if item not found in Value
        Remove(self: DocumentSelectionSets, item: SavedItem) -> bool
        
            Removes specified item from Value.
            Returns: false if item not found in Value
        """
        pass

    def RemoveAt(self, *__args):
        """
        RemoveAt(self: DocumentSelectionSets, parent: GroupItem, index: int)
            Removes item from the specified parent group contained by SelectionSets.
        
            parent: The parent group to remove from. RootItem or null to remove directly from Value
        RemoveAt(self: DocumentSelectionSets, index: int)
            Removes item at the specified index from Value.
        """
        pass

    def ReplaceWithCopy(self, *__args):
        """
        ReplaceWithCopy(self: DocumentSelectionSets, parent: GroupItem, index: int, item: SavedItem)
            Replaces item from the specified parent group with a copy of item
        
            parent: The parent group to insert into. RootItem or null to insert directly into Value
        ReplaceWithCopy(self: DocumentSelectionSets, index: int, item: SavedItem)
            Replaces item at given index within Value with a copy of item
        """
        pass

    def ResolveGuid(self, value):
        """
        ResolveGuid(self: DocumentSelectionSets, value: Guid) -> SavedItem
        
            Returns the saved item referenced by a guid.
        """
        pass

    def ResolveIndexPath(self, path):
        """ ResolveIndexPath(self: DocumentSelectionSets, path: IEnumerable[int]) -> SavedItem """
        pass

    def ResolveReference(self, reference):
        """
        ResolveReference(self: DocumentSelectionSets, reference: SavedItemReference) -> SavedItem
        
            Returns the saved item referenced by a SavedItemReference.
        """
        pass

    def ResolveSelectionSource(self, source):
        """
        ResolveSelectionSource(self: DocumentSelectionSets, source: SelectionSource) -> SavedItem
        
            Returns the saved item referenced by a SelectionSource
            Returns: null if source cannot be resolved
        """
        pass

    def ToSavedItemCollection(self):
        """
        ToSavedItemCollection(self: DocumentSelectionSets) -> SavedItemCollection
        
            Explicit form of conversion operator returning Autodesk.Navisworks.Api.DocumentParts.DocumentSelectionSets.Value
        """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The internal identifier for this type of document part.

Get: Id(self: DocumentSelectionSets) -> str

"""

    RootItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Autodesk.Navisworks.Api.DocumentParts.DocumentSelectionSets.Value as the children of a Autodesk.Navisworks.Api.FolderItem

Get: RootItem(self: DocumentSelectionSets) -> FolderItem

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The collection of SelectionSets stored in the Document

Get: Value(self: DocumentSelectionSets) -> SavedItemCollection

"""


    Changed = None
    Changing = None


class DocumentTool(object):
    """ The active tool in a Document """
    def Set(self, tool):
        """
        Set(self: DocumentTool, tool: Tool)
            Explicit method that sets Autodesk.Navisworks.Api.DocumentParts.DocumentTool.Value
        """
        pass

    def SetCustomToolPlugin(self, toolPlugin):
        """
        SetCustomToolPlugin(self: DocumentTool, toolPlugin: ToolPlugin)
            Sets the current Tool to a custom ToolPlugin.
        
            toolPlugin: Loaded ToolPlugin
        """
        pass

    def ToTool(self):
        """
        ToTool(self: DocumentTool) -> Tool
        
            Explicit form of conversion operator returning Autodesk.Navisworks.Api.DocumentParts.DocumentTool.Value
        """
        pass

    CustomToolPluginId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For the case where Autodesk.Navisworks.Api.DocumentParts.DocumentTool.Value is CustomToolPlugin,
this will return the the passed in ToolPlugin identifier.

Get: CustomToolPluginId(self: DocumentTool) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value of the active Autodesk.Navisworks.Api.ToolTool within the document
Attempts to set Autodesk.Navisworks.Api.DocumentParts.DocumentTool.Value to CustomToolPlugin will be ignored.

Get: Value(self: DocumentTool) -> Tool

Set: Value(self: DocumentTool) = value
"""


    Changed = None


class IDocumentClash:
    """ Discoverable Document Part for Clash Detective """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IDocumentTakeoff:
    """ Discoverable Document Part for Takeoff """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IDocumentTimeliner:
    """ Discoverable Document Part for Timeliner """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ModelItemPathId(object):
    """
    Represent a combined id with model index and the path identifier.
    
    ModelItemPathId()
    """
    ModelIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The model index

Get: ModelIndex(self: ModelItemPathId) -> int

Set: ModelIndex(self: ModelItemPathId) = value
"""

    PathId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The path identifier

Get: PathId(self: ModelItemPathId) -> str

Set: PathId(self: ModelItemPathId) = value
"""



