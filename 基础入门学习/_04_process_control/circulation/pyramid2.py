# 打印规则金字塔
level = 5
for i in range(level):
    # 打印空格
    for t in range((level - i)):
        print(" ", end="")
    # 打印 *
    for j in range((2 * i) + 1):
        print("*", end="")
    print()
