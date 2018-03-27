#!/usr/bin/env python3

from collections import Iterable, Iterator

isinstance([], Iterable)
isinstance((x for x in range(10)), Iterator)

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# Iterable可迭代对象，即可使用for循环，可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# Python的for循环本质上就是通过不断调用next()函数实现的
