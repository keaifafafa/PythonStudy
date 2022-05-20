"""
匿名函数
"""


# map：映射，所以最后返回的是地址,需要借助list(),tuple()等函数来解析
def my_func01(x):
    return x + 3


print(list(map(my_func01, [1, 2, 3, 4, 5])))
print(list(map(lambda x: x + 3, [1, 2, 3, 4, 5])))


# filter:过滤器
def my_func02(x):
    # 奇数才可以输出
    return x % 2 == 1


# 注意这里函数不需要写(),也就是第一个函数参数，然后其返回结果是boolean型
print(list(filter(my_func02, [1, 2, 3, 4, 5, 6])))
print(list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6])))
