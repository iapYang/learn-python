#!usr/bin/env/python3


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f())


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


f1, f2, f3 = count()

f1()

f2()

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


def createCounter():
    s = [0]

    def counter():
        # 闭包内部无法修改外部变量的引用，用list做个小技巧
        s[0] += 1
        return s[0]
    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
