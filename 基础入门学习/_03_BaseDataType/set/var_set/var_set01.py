# 可变集合【可进行增删改查】

# 集合中不可以有可变的数据类型，如 列表 或者 集合 等可变数据类型就不可以添加到其中

# 创建方式一
my_var_set = {1, False, "Python", (88, 99)}
# 无序的
print(my_var_set)

# 创建方式二
my_var_set2 = set([1, False, "Java", (77, 66)])
print(my_var_set2)

# 字符串
my_var_set3 = set("Python%%&34--")
print(my_var_set3)
