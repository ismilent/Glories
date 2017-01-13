import sys
import inspect

class Plugin(object):
    '''
    create object instance and return
    '''
    @classmethod
    def load(cls, plugin_name=None, **kwargs):
        if not plugin_name:
            raise Exception('Need plugin name')
        plugin_instance = None
        plugin_path = 'plugins.{0}'.format(plugin_name)
        try:
            __import__(plugin_path)
        except ImportError:
            raise Exception('Cant load plugin')

        plugin_obj = sys.modules[plugin_path]
        plugin_classes = inspect.getmembers(plugin_obj, inspect.isclass)
        for plugin_name, class_obj in plugin_classes:
            if inspect.getmodule(class_obj).__name__.find(plugin_path) == 0 :
                for member in inspect.getmembers(class_obj, inspect.ismethod):
                    if 'run' in member:
                        try:
                            plugin_instance = class_obj(**kwargs)
                        except Exception as e:
                            raise Exception('Can not load plugin')

        print plugin_instance
        return plugin_instance