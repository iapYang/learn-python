#!usr/bin/env/python3
import functools,time


def log(text):
    def decorator(func):
        # functools.wraps应该是改变函数名的
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log("execute")
def now():
    print('2018-04-08')


now()
print(now.__name__)


def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, time.time()))
    return fn


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


