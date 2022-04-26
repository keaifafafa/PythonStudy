import keyword

# 基础语法学习
# 查看所有关键字
print(keyword.kwlist)

# 行与缩进【注意 布尔值首字母要大写】
flag = False
if flag:
    print("True")
else:
    print("False")

# 多行语句
item_one = 1
item_two = 2
item_three = 3
total1 = item_one + \
         item_two + \
         item_three
print(total1)
# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \
total2 = ['item_one', 'item_two', 'item_three',
          'item_four', 'item_five']
print(total2)

# 数字(Number)类型
"""
    int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
    bool (布尔), 如 True。
    float (浮点数), 如 1.23、3E-2
    complex (复数), 如 1 + 2j、 1.1 + 2.2j
"""

