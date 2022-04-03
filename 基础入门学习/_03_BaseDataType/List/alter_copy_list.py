my_list = [1, 2, 3, 4, 5]
# 修改操作
my_list[2] = "Python"
print(my_list)

# 方式一：赋值
list1 = my_list
print(list1)

# 方式二：切片
list2 = my_list[::]
# 完整格式， 参数分别为 start : end : step
# list2 = my_list[0:4:1]
print(list2)

# 方式三：list函数，转为列表
list3 = list(my_list)
print(list3)

# 方式四：copy函数
list4 = my_list.copy()
print(list4)

# 查看四种创建方式的地址是否一致
print(id(my_list))
print(id(list1))
# 下面的都是创建了新的对象，开辟了新的内存空间
print(id(list2))
print(id(list3))
print(id(list4))
