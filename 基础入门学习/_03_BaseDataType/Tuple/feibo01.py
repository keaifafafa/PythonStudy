# 0 1 1 2 3 5 8 13

# 生成斐波那契数列
def fei_bo(n):
    if n < 2:
        return n
    # 使用动态规划
    dp_i = 0
    dp_i_1 = 1
    dp_i_2 = 0
    index = 2
    # 注意 n 是取不到的
    while index <= n:
        dp_i = dp_i_1 + dp_i_2
        dp_i_2 = dp_i_1
        dp_i_1 = dp_i
        index += 1
    return dp_i


# 调用函数
num = fei_bo(4)
print(num)
