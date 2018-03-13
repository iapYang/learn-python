age = 12
if age >= 18:
    print('your age is', age)
    print('adult')
elif age > 6:
    print('your age is', age)
    print('teenager')
else:
    print('your age is', age)
    print('adult')

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = ""

if x:
    print('x is true!')


s = input('birth year: ')
birth = int(s)

if birth < 2000:
    print('00前')
else:
    print('00后')

weight = 80.5
height = 1.75
BMI = weight / (height * height)

if BMI < 18.5:
    print('过轻')
elif BMI < 25:
    print('正常')
elif BMI < 28:
    print('过重')
elif BMI < 32:
    print('肥胖')
else:
    print('严重肥胖')
