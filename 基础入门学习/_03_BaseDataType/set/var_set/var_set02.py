# 求并集
A = {1, 3, 5, 6, 7, 8, 9, 23, 45, 67}
B = {2, 4, 5, 6, 7, 8, 9, 233, 145, 67}
# 返回结果 是生成一个新的
# 方式一
C = A | B
# 方式二
C = A.union(B)
print(C)

# 求交集
# 方式一
D = A & B
# 方式二
D = A.intersection(B)
print(D)

# 求差集
# 求的是 A独有的一部分
E = A - B
E = A.difference(B)
print(E)

# 异或集 [两个集合减去交集的部分]
F = A ^ B
F = A.symmetric_difference(B)
# TODO 也可以使用 并集 - 交集
print(F)

my_set = {15}
# 新增方法【单个元素】 可类比 list中的 append
my_set.add(999)
print(my_set)
# 新增方法【一个集合】可类比 list中的 extends
my_set.update({55, 777, 888, 100})
print(my_set)

# 集合的删除
my_lang = {"Java", "Php", "VB", "C++", "Go", "C"}
# 如果删除不存在的就会报错
my_lang.remove("Php")
print(my_lang)
# 如果删除不存在的，就不会做任何处理
my_lang.discard("SSS")
print(my_lang)
# 注意pop是随机删除，每次运行删除的都不一样
s = my_lang.pop()
print(s)
