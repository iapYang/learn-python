#!/usr/bin/env python3

L = [x * x for x in range(1, 11)]

g = (x * x for x in range(1, 11))

for n in g:
    print(n)


def fib(maxvalue):
    n, a, b = 0, 0, 1
    while n < maxvalue:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


f = fib(10)

for n in fib(6):
    print(n)


print('==================杨辉三角==================')


def triangles():
    n, start, _list = 0, 1, [1]

    while True:
        if n == 0:
            n += 1
            yield _list
        else:
            n += 1
            tmp_list = []
            for x, index in enumerate(range(n)):
                if index == 0:
                    tmp_list.append(1)
                elif index == n - 1:
                    tmp_list.append(1)
                else:
                    tmp_list.append(_list[index] + _list[index - 1])

            _list = tmp_list
            yield _list


# 测试
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
