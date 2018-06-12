#!usr/bin/env/python3
# -*- coding: utf-8 -*-
# created_at: 2018/6/12 下午12:49

__author__ = 'IAPYANG'

import json
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
