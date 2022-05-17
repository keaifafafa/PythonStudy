# 打印平行四边形
# 限制数
limit = 4
row = int(input("请输入平行四边形的高度：\n"))
# 双层循环
for i in range(row):
    for t in range(limit - i):
        print(" ", end="")
    for j in range(limit):
        print("*", end="")
    print()
# 换行
print("=========================================")
# 单层循环
for i in range(row):
    print(" " * (row - i - 1), "*" * limit)
