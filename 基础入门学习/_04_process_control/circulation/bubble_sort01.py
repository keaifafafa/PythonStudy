# 冒泡排序
my_list = [10, 22, 33, 45, 6, 7, 8, 9, 21]
length = len(my_list)
for i in range(length - 1):
    for j in range(length - i - 1):
        if my_list[j] > my_list[j + 1]:
            temp = my_list[j]
            my_list[j] = my_list[j + 1]
            my_list[j + 1] = temp
print(my_list)
