#!usr/bin/env/python3
# -*- coding: utf-8 -*-
# created_at: 2018/6/9 下午5:00

__author__ = 'IAPYANG'

from io import StringIO, BytesIO

f = StringIO()

f.write('hello')

f.write(' ')

f.write('world')

print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')

while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


f = BytesIO()
f.write('中文'.encode('utf-8'))

print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
