my_list = [2, 5, 8, 9, 18]
# for 的增强循环,只能用于遍历操作
# 注意 i 是一个新的对象，更改其内容，不会改变原列表的内容
for i in my_list:
    print(i)
print("======================")
# 这种就可以进行更改原列表元素了
# range 是返回的意思， param1 = start ，param2 = end， param3 = step
for i in range(len(my_list)):
    print(my_list[i])
