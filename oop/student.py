#!usr/bin/env/python3
# -*- coding: utf-8 -*-

__author__ = 'IAPYANG'


class Student(object):

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def print_score(self):
        print('%s: %s' % (self._name, self._score))

    def get_grade(self):
        if self._score >= 90:
            return 'A'
        elif self._score >= 60:
            return 'B'
        else:
            return 'C'

