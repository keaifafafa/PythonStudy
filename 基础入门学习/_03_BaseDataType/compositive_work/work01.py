"""
利用 Python中的方法和函数提取出给定列表[5,8,-7,4,6,2,-3,0]中的最大元素
删除最小元素,同时将负数的负号去除。
"""
my_list = [5, 8, -7, 4, 6, 2, -3, 0, -5]
# 先取出最大的元素
max_value = max(my_list)
print("最大值为：", max_value)
# 然后获取最小值
min_value = min(my_list)
# 将最小值移除
my_list.remove(min_value)
print("移除最小值后的结果：", my_list)
# 将负数的符号去掉
for i in range(len(my_list)):
    if my_list[i] < 0:
        # 取绝对值
        my_list[i] = abs(my_list[i])
print("将负号去掉的结果为：", my_list)
