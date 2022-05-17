# 打印金字塔
# 层数
level = 5
# 双层循环
for i in range(level):
    for j in range(i + 1):
        print("*", end="")
    print()
# 换行
print()
# 单层循环
for i in range(level):
    # 因为下标从 0 开始，所以需要 i + 1
    print("*" * (i + 1))
