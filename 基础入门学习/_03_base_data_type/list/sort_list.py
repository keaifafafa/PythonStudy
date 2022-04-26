# 列表排序
my_list = [1, 6, 7, 8, 15, 3, 45, 32, 31, 23]
print("排序前", my_list)
# sort 会改变原列表
# my_list.sort()
# print("排序后", my_list)

# sorted不会改变原列表 会重新创建一个对象来存储排序后的
new_list = sorted(my_list)
print(new_list)
print(my_list)
