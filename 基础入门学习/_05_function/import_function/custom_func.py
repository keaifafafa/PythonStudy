"""
自定义函数
"""


def add(x):
    x += 3
    return x


def make_steak(price, *order):
    print("制作一个%d分熟的牛排" % price, "再来点", end="")
    for item in order:
        print(item, end="")


# make_steak(7, "红酒", "薯条", "披萨")
