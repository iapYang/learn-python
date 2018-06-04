#!usr/bin/env/python3
# -*- coding: utf-8 -*-
# created_at: 2018/5/28

__author__ = 'IAPYANG'

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

