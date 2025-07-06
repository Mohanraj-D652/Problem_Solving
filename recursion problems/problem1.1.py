def digit(n):
    if n % 10 == n:
        if n % 10 == 5:
            return 1
 
    else:
        return 1 + digit(n // 10)
result = digit(53543)
print(result)
