# 猜数小游戏
import random

# 生成一个随机数
target = random.randint(1, 100)
print(target)
count = 0
while True:
    num = int(input("请输入你的答案：\n"))
    count += 1
    if num == target:
        print("恭喜你猜对了，一共猜了", count, "次")
        # 结束
        break
    elif num > target:
        print("很遗憾，猜大了")
    elif num < target:
        print("很遗憾，猜小了")
