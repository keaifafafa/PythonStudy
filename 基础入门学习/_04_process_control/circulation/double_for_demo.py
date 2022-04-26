# 双层循环遍历
my_list = [[100, 200, 300], [210, 220, 230], [310, 320, 330]]


# 使用普通for循环【推荐使用这种】
def func01():
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            my_list[i][j] = my_list[i][j] + 1


# 使用for each + 普通for循环【这种虽然也可以但是for each 循环通常只做遍历用，因为每都是生成新的对象】
def func02():
    for item in my_list:
        for j in range(len(my_list)):
            item[j] = item[j] + 1


func02()
print(my_list)
