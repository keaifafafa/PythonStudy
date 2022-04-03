# 创建列表
my_list = ['pen', 'paper', True, 10, False, 2.5, True]
# 列表转元组
my_tuple = tuple(my_list)
index = 0
# 遍历元组，来找到全部bool
while index < len(my_tuple):
    # 先判断类型,符合的就输出【包含截取】
    if isinstance(my_tuple[index], bool):
        # 截取相应的元素，并打印
        print(my_tuple[index])
    index += 1
