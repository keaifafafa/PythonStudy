# 反转操作
my_list1 = [1, "like", "love", "python", "**", True, False]
# 这种只是临时反转，不会改变原来的列表结构
print(my_list1[::-1])
print("原列表：", my_list1)
# 这种会改变原来的列表结构【而且没有返回值】
my_list1.reverse()
print(my_list1)

# 重复
print(my_list1 * 3)
# 拼接
my_list2 = [552, "java", "final"]
print(my_list1 + my_list2)

# 因为字符串不可修改，所以其没有reverse函数
