# 基本数据类型

# 浮点型转整型【不会四舍五入，只会舍去】
f = 3.14
print(int(f))

# 整型转浮点型
a = 1
print(float(a))

# 复数
print(complex(a))
print(complex(1, 2))

# 数字0,空字符串、空列表、空元组、空字典、空集合、空None是False, 其余都是True
print(bool(0))
print(bool(""))
print(bool(0.3))
# 空元组
print(bool(()))
# 空列表
print(bool([]))
# 空字典
print(bool({}))
