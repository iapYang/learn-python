#!usr/bin/env/python3
# -*- coding: utf-8 -*-
# created_at: 2018/6/9
import os

__author__ = 'IAPYANG'

with open(os.path.dirname(__file__) + '/text', 'r') as f:
    for line in f.readlines():
        print(line.strip())


# f = open('/Users/michael/test.jpg', 'rb')
# open('/Users/michael/gbk.txt', 'r', encoding='gbk')
# open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
# with open('/Users/michael/test.txt', 'w') as f:
