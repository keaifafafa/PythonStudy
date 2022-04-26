# 运用算数运算符实现将十进制数9转换成二进制【其实可以是任意进制】，并输出
target = int(input("请输入待转换数字："))
# 进制数，便于复用
scale = 2
# 定义空字符串用于存放结果
res = ""

# 只要商不为0 就会一直循环【while循环里的才是核心算法】
while target != 0:
    # 将每次获取的余树添加到res的尾部，即拼接，记得转成String类型
    res += str(target % scale)
    # 取商，便于下一次遍历使用
    target //= scale

# 输出结果，记得反转字符串
print(res[::-1])
