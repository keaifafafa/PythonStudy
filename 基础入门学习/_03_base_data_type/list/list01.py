# 创建列表
# 列表里可以进行套娃
my_list = [1, "python", "123", True, [1, 2, 3], "like"]
print(my_list)

# 将字符串转换成列表，即把字符串的每一个字符转换成了列表的元素【分割】
my_list2 = list("python")
print(my_list2)

# 将列表作为list函数的参数
my_list3 = list([1, 2, 3, "python"])
print(my_list3)

# 将元组作为list函数的参数【元组表示符为 () 】
my_list4 = list((1, 2, 3, "python"))
print(my_list4)

# 如何创建空列表？？？
empty_list1 = []
# 没有参数
empty_list2 = list()
# 参数是空字符串
empty_list3 = list()
# 参数是空列表
empty_list4 = list([])
# 参数是空元组
empty_list5 = list(())

# 打印
print(empty_list1)
print(empty_list2)
print(empty_list3)
print(empty_list4)
print(empty_list5)

# 计算长度
print(len("python"))

# 计数
print("vvvdfgdfgb".count("n"))


