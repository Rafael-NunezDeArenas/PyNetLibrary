# encoding: utf-8
# module Autodesk.Navisworks.Api.Interop.Plugins calls itself Plugins
# from Autodesk.Navisworks.Api, Version=19.0.1374.1, Culture=neutral, PublicKeyToken=d85e58fa5af9b484
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class LegacyManager(object):
    # no doc
    @staticmethod
    def LoadPlugins(attribLoading):
        """ LoadPlugins(attribLoading: Attribute) -> int """
        pass

    Plugins = None


class LegacyPlugin(object):
    """ LegacyPlugin(assembly: Assembly, iPlugin: IPlugin, DataDir: str) """
    @staticmethod # known case of __new__
    def __new__(self, assembly, iPlugin, DataDir):
        """ __new__(cls: type, assembly: Assembly, iPlugin: IPlugin, DataDir: str) """
        pass

    AssemblyPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyPrefix(self: LegacyPlugin) -> str

"""

    DataDir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataDir(self: LegacyPlugin) -> str

"""

    PluginInterface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PluginInterface(self: LegacyPlugin) -> IPlugin

"""



