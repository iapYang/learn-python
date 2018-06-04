#!usr/bin/env/python3
# -*- coding: utf-8 -*-
# created_at: 2018/5/29

__author__ = 'IAPYANG'

import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('END')
