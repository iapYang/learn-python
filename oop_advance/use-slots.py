#!usr/bin/env/python3
# -*- coding: utf-8 -*-

__author__ = 'IAPYANG'


class Student(object):
    # 用tuple定义允许绑定的属性名称
    # 限制实例的属性
    __slots__ = {'name', 'age'}


s = Student()
s.name = 'Michael'

print(s.name)


# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__，类似于上下文
