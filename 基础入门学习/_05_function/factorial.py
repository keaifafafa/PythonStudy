"""
递归实现n的阶乘
"""


def factorial(n):
    # 结束标志
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(6))
