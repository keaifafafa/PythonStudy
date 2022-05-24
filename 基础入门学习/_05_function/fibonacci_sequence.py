"""
递归解决斐波那契数列问题
1 1 2 3 5 8 ……
"""


def fibonacci(n):
    # python 要用or，不能用 ||
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
