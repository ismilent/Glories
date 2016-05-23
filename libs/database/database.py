#!/usr/bin/env python
#-*- coding: utf-8 -*-


class DBModel(object):
    def __init__(self, **kwargs):
        pass

    def insert(self):
        raise NotImplementedError

    def save(self):
        raise NotImplementedError