# def nPrint(message, n):
#     while n > 0:
#         print(message)
#         n -= 1


# nPrint('a', 4)

# def factorial(n):
#     return n * factorial(n - 1)

# factorial(3)

# def xfunction(n):
#     if n == 1:
#         return 1
#     else
#         return n + xfunction(n - 1)


# def xfunction(n):
#     if n == 1:
#         return 1
#     else:
#         return n + xfunction(n - 1)

# print(xfunction(4))

def f2(n, result):
    if n == 0:
        return 0
    else:
        return f2(n - 1, n + result)

print(f2(20, 10))