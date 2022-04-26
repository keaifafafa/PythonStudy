# 进一步区分 append 和 extend

my_list = [1, 2, 3, 4, 5]
my_list.append("python")
print(my_list)
my_list.extend("python")
print(my_list)

# 插入
my_list2 = [1, 2, 3, 4, 5]
my_list2.insert(2, "Python")
print(my_list2)
my_list2.insert(-2, "Python")
print(my_list2)

my_list3 = ["red", "yellow", "purple", "black", "green"]
# remove元素  无返回值
# my_list3.remove("black")
my_list3.remove(my_list3[2])

# 移除元素【弹出元素】，按照下标来的，返回值为删除元素
# my_list3.pop(3)
print(my_list3)
