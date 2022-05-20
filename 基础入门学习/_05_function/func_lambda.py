"""
lambda表达式
类比Java中的Lambda即可
"""

# 参数自增
a = lambda x: x + 3
print(a(10))


# 自定义写法
def lam(x):
    return x + 3


print(lam(10))

# 计算俩个参数的乘积
b = lambda i, j: i * j;

print(b(2, 3))


# 自定义写法
def lam(i, j):
    return i * j


print(lam(2, 3))
