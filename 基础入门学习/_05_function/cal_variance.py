"""
使用函数计算方差
"""


# 计算平均值
def avg(*ele):
    avgA = 0
    for i in ele:
        avgA += i
    return avgA / len(ele)


# 计算方差
def variance(*ele):
    # 计算均值
    avgA = avg(*ele)
    print("平均值：", avgA)
    res = 0
    for i in ele:
        res += (i - avgA) * (i - avgA)
    return res / len(ele)


# 调用函数
print("总体标准方差：", variance(1, 2, 3, 4, 5))
