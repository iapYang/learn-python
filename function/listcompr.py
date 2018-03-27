#!/usr/bin/env python3

L = list(range(1, 11))

A = [x * x for x in range(1, 11)]

B = [x * x for x in range(1, 11) if x % 2 == 0]

C = [m + n for m in 'ABC' for n in 'XYZ']

L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s, str)]


# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
