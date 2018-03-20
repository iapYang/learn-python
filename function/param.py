def power(x, n=2):
    result = 1
    while n > 0:
        n = n - 1
        result = result * x
    return result
