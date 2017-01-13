#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import inspect

class DBModel(object):
    def __init__(self, **kwargs):
        pass

    def insert(self):
        raise NotImplementedError

    def save(self):
        raise NotImplementedError

class DatabaseFactory(object):
    @classmethod
    def create(cls, plugin_name='mongodb', **kwargs):
        '''
        create
        :param plugin_name:
        :param kwargs:
        :return: backend_plugin instance
        '''
        backend_plugin = None
        plugin_path = "libs.database.dbplugins.{0}".format(plugin_name)
        __import__(plugin_path)
        plugin_obj = sys.modules[plugin_path]
        plugin_classes = inspect.getmembers(plugin_obj, inspect.isclass)
        for class_name, class_obj in plugin_classes:
            if inspect.getmodule(class_obj).__name__.find(plugin_path) == 0:
                try:
                    backend_plugin = class_obj(**kwargs)
                except Exception as e:
                    raise Exception("Cannot create Backend: {0}".format(e))

        return backend_plugin