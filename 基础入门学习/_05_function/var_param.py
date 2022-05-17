# 可变参数
def my_func(a, b, *c):
    print(a)
    print(b)
    print(c)


# *c 是可变参数，会变成元组（多个参数）
my_func(1, 2, 3, 4, 5, 7, 9)

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def my_func02(a, b, *c, **d):
    print(a)
    print(b)
    print(c)
    print(d)


# ** 代表字典
my_func02(1, 2, 3, 4, 5, 6, name="fafa", age=22)
