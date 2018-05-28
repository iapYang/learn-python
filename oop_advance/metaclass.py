#!usr/bin/env/python3
# -*- coding: utf-8 -*-

__author__ = 'IAPYANG'


class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


h = Hello()

h.hello()

print(type(Hello))
print(type(h))


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(1)
print(L)

# metaclass
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000
