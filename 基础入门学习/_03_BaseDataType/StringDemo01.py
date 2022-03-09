# 标准数据类型
"""
Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

"""

# 1、数字
"""
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
"""
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
a = 111
print(isinstance(a, int))
print("------------------")
# 2、String（字符串）
# 语法：变量[头下标:尾下标]
# 索引值以 0 为开始值，-1 为从末尾的开始位置。
string = "KeAiFa"
print(string)  # 输出字符串
print(string[0:-1])  # 输出第一个到倒数第二个的所有字符
print(string[0])  # 输出字符串第一个字符
print(string[2:5])  # 输出从第三个开始到第五个的字符
print(string[2:])  # 输出从第三个开始的后的所有字符
print(string * 2)  # 输出字符串两次，也可以写成 print (2 * str)
print(string + "TEST")  # 连接字符串
print("------------------")

# Python 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
print("keai\nfa")
print(r"keai\nfa")

"""
字符串注意事项：
1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2、字符串可以用+运算符连接在一起，用*运算符重复。
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变。
"""
