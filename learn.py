def make_incrementor(n):
    answer = lambda x: x + n
    return answer

f = make_incrementor(42)
print(f(0))
f(0)
f(1)