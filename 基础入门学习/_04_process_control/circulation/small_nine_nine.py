# 小九九
for i in range(1, 10):
    for j in range(1, i + 1):
        #  end=""代表不换行
        print(i, "*", j, "=", i * j, "\t", end="")
    # 换行
    print()
