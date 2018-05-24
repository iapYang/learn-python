#!usr/bin/env/python3
# -*- coding: utf-8 -*-

__author__ = 'IAPYANG'


class Student(object):
    def __init__(self, name, score):
        self._name = name
        self._score = score

    # 用于限制属性类型
    @property
    def score(self):
        return self._score

    def __str__(self):
        return 'Student Object name: %s' % self._name

    __repr__ = __str__


d = Student('IAPYANG', 98)

print(d)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


for n in Fib():
    print(n)

f = Fib()

print(f[100])


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)
print(Chain().users('michael').repos)
