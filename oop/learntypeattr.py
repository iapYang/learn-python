#!usr/bin/env/python3
# -*- coding: utf-8 -*-

__author__ = 'IAPYANG'

from animal import Animal
from myobj import MyObject
import types

# 基本类型都可以用type()判断
print(type(123))
print(type('str'))
print(type(None))

# 如果一个变量指向函数或者类，也可以用type()判断：
print(type(abs))
a = Animal()
print(type(a))

print(type(123) == type(456))


def fn():
    pass


print(type(fn) == types.FunctionType)

# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print('判断类型', isinstance([1, 2, 4], (list, tuple)))

print(dir('ABC'))

obj = MyObject()

print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))

setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))

print(getattr(obj, 'z', 404))

print(hasattr(obj, 'power'))

fn = getattr(obj, 'power')

print(fn())
