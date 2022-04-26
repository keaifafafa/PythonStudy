"""
流程语句条件判定标椎：
1、非零数字 和 非空对象 也为 True
2、0、空对象、None 都是 False
3、直接使用 True 和 False
4、使用 in
5、使用 is ，用来对比对象的地址
"""

# 0 代表 False 所以不会执行
if 0:
    print("000")
# 5 代表 True 所以会执行
if 5:
    print("555")
# "abc" 是非空的 所以也是 True
if "abc":
    print("abc")
# 空对象 所以为 False
if ():
    print("()")

# 使用in
my_list = [2, 3, 4]
if 2 in my_list:
    print("2在列表中")

# 使用is
# 先拷贝【深拷贝，会创建新的内存空间】
my_list2 = my_list.copy()
if my_list is my_list2:
    print("地址相同")
