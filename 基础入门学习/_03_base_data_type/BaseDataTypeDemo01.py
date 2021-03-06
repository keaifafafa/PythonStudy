# 基本数据类型
"""
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

等号（=）用来给变量赋值。

等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：
"""
counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串
print(counter)
print(miles)
print(name)

# 多个变量赋值
a = b = c = 1
print(a, b, c)

# 您也可以为多个对象指定多个变量
a, b, c = 1, 2, "runoob"
print(a)
print(b)
print(c)
