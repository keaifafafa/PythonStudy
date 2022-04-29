# 质数与因子
for i in range(10, 15):
    # 用于判断的标志位
    flag = True
    # 要用 // 这样不会出现浮点数，算是python的一个特点。
    for j in range(2, (i // 2) + 1):
        # 可以整除,存在质数因子
        if i % j == 0:
            flag = False
            x = i // j
            print(i, "=", x, "*", j)
    if flag:
        print(i, "是一个质数\n")
    else:
        print(i, "不是一个质数\n")
