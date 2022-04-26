my_tuple = ('hello', 1, 2, 3, "sss")
print(my_tuple)
print(my_tuple.count(1))
print(len(my_tuple))
print(my_tuple[::-1])
print(my_tuple[1:3:1])

# 需要注意 只能用sorted，因为元组不可变！！！
my_tuple1 = ("apple", "banana", "lemon", "milk", "cheese")
print(sorted(my_tuple1))
# print(my_tuple.sort())

# 元组解包
m = tuple(range(1, 10))
print("m = ", m)
# 注意 等号前面的变量数量 = m里的元素数量
A, B, C, D, E, F, G, H, I = m
print("A = ", A)
print("B = ", B)
print("C = ", C)
print("D = ", D)
