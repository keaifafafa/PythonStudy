"""
使用四种方式：实现参数列表全部加3
"""
my_list = list(range(1, 11))


# print(my_list)

# 方式一：自定义函数
def auto_inc(num):
    num += 3
    return num


print(list(map(auto_inc, my_list)))

# 方式二：使用lambda
print(list(map(lambda x: x + 3, my_list)))

# 方式三：采用新元素追加
# 注意这里不可用元组，因为元组不可变
my_new_list = []
for i in range(1, 11):
    my_new_list.append(auto_inc(i))

print(my_new_list)

# 方式四：采用列表解析
a = lambda x: x + 3
my_new_list2 = []
print([my_new_list2.append(a(i)) for i in range(1, 11)])
print(my_new_list2)
