# 计算收入

# 可以有默认参数比如 天数 和 利率
def com_salary(money, day=1, lilv=0.05):
    income = money * day * lilv
    print(income)


com_salary(10000)
com_salary(money=10000, day=10, lilv=0.08)
# 关键字参数可以换位置，因为有映射
com_salary(day=10, money=10000, lilv=0.08)


# 位置参数必须在关键字的前面,否则会报错
# com_salary(day=10, lilv=0.08,  10000)


