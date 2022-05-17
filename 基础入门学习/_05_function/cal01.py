"""
注意事项：
* 代表多个参数
不带* 说明是一个元组
带两个* 说明是字典， name = "黎明"
"""


# 方式一
def avg01(*a):
    # * 代表多个参数
    def he01(b):
        sumA = 0
        for i in b:
            sumA += i
        return sumA

    return he01(a) / len(a)


print(avg01(1, 2, 3, 4, 5))


# 方式二
def avg02(*a):
    # * 代表多个参数
    def he02(*b):
        sumA = 0
        for i in b:
            sumA += i
        return sumA

    # 这里写 *a 是因为he里面的形参就是带*的，即多个参数
    return he02(*a) / len(a)


print(avg02(1, 2, 3, 4, 5))


# 方式三
def he03(*b):
    sumA = 0
    for i in b:
        sumA += i
    return sumA


def avg03(*a):
    return he03(*a) / len(a)


# 调用
print(avg03(1, 2, 3, 4, 5))


# 方式四
def he04(b):
    sumA = 0
    for i in b:
        sumA += i
    return sumA


def avg04(*a):
    return he03(a) / len(a)


# 调用
print(avg03(1, 2, 3, 4, 5))
