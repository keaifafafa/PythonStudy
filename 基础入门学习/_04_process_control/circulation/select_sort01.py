# 选择排序
my_list = [10, 22, 33, 45, 6, 7, 8, 9, 21]
length = len(my_list)
for i in range(length - 1):
    for j in range(i, length):
        if my_list[i] > my_list[j]:
            temp = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = temp
print(my_list)
