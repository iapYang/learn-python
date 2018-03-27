#!/usr/bin/env python3

from collections import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 4], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (3, 5), (6, 8)]:
    print(x, y)


def find_max_and_min(l):
    max_value = None
    min_value = None

    for values in l:
        if max_value is None:
            max_value = values
        elif max_value < values:
            max_value = values

        if min_value is None:
            min_value = values
        elif values < min_value:
            min_value = values

    return min_value, max_value


# 测试
if find_max_and_min([]) != (None, None):
    print('测试失败!')
elif find_max_and_min([7]) != (7, 7):
    print('测试失败!')
elif find_max_and_min([7, 1]) != (1, 7):
    print('测试失败!')
elif find_max_and_min([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
