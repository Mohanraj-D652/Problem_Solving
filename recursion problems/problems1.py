def digit(n):
    if n == 0:
        return 0

    else:
        return 1 + digit(n // 10)
print(digit(353445))






