# encoding: utf-8
# module Autodesk.Navisworks.Api.ComApi calls itself ComApi
# from Autodesk.Navisworks.ComApi, Version=19.0.1374.1, Culture=neutral, PublicKeyToken=d85e58fa5af9b484
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ComApiBridge(object):
    """
    Provides access to the Navisworks COM API from the Navisworks .Net API together with support
    for interop between the two.
    """
    @staticmethod
    def ToInwOaPath(modelItem):
        """
        ToInwOaPath(modelItem: ModelItem) -> InwOaPath
        
            Helper for using COM Api from .NET Api.
        Translates from ModelItem to InwOaPath.
        """
        pass

    @staticmethod
    def ToInwOpAnonView(viewpoint):
        """
        ToInwOpAnonView(viewpoint: Viewpoint) -> InwOpAnonView
        
            Helper for using COM Api from .NET Api.
        Translates from Viewpoint to InwOpAnonView.
        Makes a copy of the underlying viewpoint.
        """
        pass

    @staticmethod
    def ToInwOpSelection(modelItemCollection):
        """
        ToInwOpSelection(modelItemCollection: ModelItemCollection) -> InwOpSelection
        
            Helper for using COM Api from .NET Api.
        Translates from ModelItemCollection to InwOpSelection.
        Makes a copy of the underlying selection.
        """
        pass

    @staticmethod
    def ToModelItem(path):
        """
        ToModelItem(path: InwOaPath) -> ModelItem
        
            Helper for using COM Api from .NET Api.
        Translates from InwOaPath to ModelItem.
        """
        pass

    @staticmethod
    def ToModelItemCollection(selection):
        """
        ToModelItemCollection(selection: InwOpSelection) -> ModelItemCollection
        
            Helper for using COM Api from .NET Api.
        Translates from InwOpSelection to ModelItemCollection.
        Makes a copy of the underlying selection.
        """
        pass

    @staticmethod
    def ToViewpoint(anonView):
        """
        ToViewpoint(anonView: InwOpAnonView) -> Viewpoint
        
            Helper for using COM Api from .NET Api.
        Translates from InwOpAnonView to Viewpoint.
        Makes a copy of the underlying viewpoint.
        """
        pass


