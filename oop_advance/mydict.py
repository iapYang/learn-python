#!usr/bin/env/python3
# -*- coding: utf-8 -*-
# created_at: 2018/6/4

__author__ = 'IAPYANG'


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


