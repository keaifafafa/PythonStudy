all_list = [1, "word", {'like': 'python'}, True, [1, 2]]
# 切片操作【注意取值区间是左闭右开，最后是步长，-1表示反转】
# 从1到第3个【下标从 0 到 2】
print(all_list[:3])
# 步长为2
print(all_list[::2])
# 反转
print(all_list[::-1])
# 反正区取需要，倒转【下标从 3 到 2】
print(all_list[3:1:-1])

# list函数可以将元组【()】转为列表【[]】
my_list = list("Java")
print(my_list)
my_list.append("Php")
print(my_list)
my_list.append("True")
print(my_list)
my_list.append([1, 2, 5])
print(my_list)

#  extend可以看作是两个列表的合并，
#  但是append不会，他每次只能追加一个元素【一个整体】进来【不管这个元素里有多少个子元素】
my_list1 = [1, 3, 5, 7, 9]
s = [6, 8, 10]
my_list1.extend(s)
print(my_list1)
