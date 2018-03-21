#!/usr/bin/env python3

from collections import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 4], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (3, 5), (6, 8)]:
    print(x, y)


def findMinAndMax(L):
    max = None
    min = None

    for value in L:
        if max is None:
            max = value
        elif max < value:
            max = value

        if min is None:
            min = value
        elif value < min:
            min = value

    return min, max


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
