L = ['A', 'B', 'C', 'D']

# 如果开始索引为0可以省略
print(L[: 3])
print(L[1: 3])
print(L[-1])

L = list(range(1000))

# 每5个取一个
print(L[::5])

# 复制
print(L[:])

# tuple返回值也是tuple
print((0, 1, 2, 3, 4)[:3])

# 字符串也是一种list
print('ABCDEFG'[::2])


def trim(str):
    end = -1
    # 越界判断
    while end + len(str) >= 0 and str[end] == ' ':
        end -= 1

    start = 0
    # 越界判断
    while len(str) - start > 0 and str[start] == ' ':
        start += 1

    return str[start: (len(str) + end + 1)]


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
