"""
外部不能访问局部变量
内部可以访问外部变量
"""


def param_scope(*a):
    sumA = 0
    for i in a:
        sumA += i
    print(sumA)


param_scope(1, 2, 3)
# print(sumA)


# 在Python里 全局变量，不能在函数内部被赋值
# 但是可以使用global关键字解决此问题
sumA = 0


def param_scope02(*a):
    global sumA
    for i in a:
        # 不能被赋值 UnboundLocalError: local variable 'sumA' referenced before assignment
        # 但是可以赋值给别人即 b = sumA + i
        sumA = sumA + i
        # b = sumA + i
    print(sumA)


param_scope02(1, 2, 3)

# 当局部变量和全局变量同名时，局部会覆盖全局
sumA = 0


def param_scope03(*a):
    sumA = 10
    for i in a:
        # 不能被赋值 UnboundLocalError: local variable 'sumA' referenced before assignment
        # 但是可以赋值给别人即 b = sumA + i
        sumA = sumA + i
    print(sumA)


param_scope03(1, 2, 3)
