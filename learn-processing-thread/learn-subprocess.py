#!usr/bin/env/python3
# -*- coding: utf-8 -*-
# created_at: 2018/6/14 下午12:58

__author__ = 'IAPYANG'

import subprocess

website = 'www.python.org'
print('nslookup %s' % website)
r = subprocess.call(['nslookup', website])
print('Exit Codes:', r)
