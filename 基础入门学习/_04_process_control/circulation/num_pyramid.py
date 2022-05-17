# 打印数字金字塔
# 思路正序+逆序打印数字
level = int(input("请输入金字塔的层数：\n"))

for i in range(level):
    # 打印空格
    for t in range(level - i - 1):
        print(" ", end="")
    j = 0
    # 正序打印
    while j < i + 1:
        print(j + 1, end="")
        j += 1
    # 逆序打印
    while j > 1:
        print(j - 1, end="")
        j -= 1
    # 换行
    print()
