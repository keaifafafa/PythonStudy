# 通过键盘输入，来输出用户的出生日期区间


# 获取出生日期
def get_birthday(name, constellation):
    if constellation == 1:
        date = "1.20-2.18"
        # 注意格式化
        print("{}您好，您的出生日期在{}".format(name, date))
    elif constellation == 2:
        date = "2.19-3.20"
        print("{}您好，您的出生日期在{}".format(name, date))
    elif constellation == 3:
        date = "3.21-4.19"
        print("{}您好，您的出生日期在{}".format(name, date))
    elif constellation == 4:
        date = "4.20-5.20"
        print("{}您好，您的出生日期在{}".format(name, date))
    else:
        print("抱歉暂时无法找到相关信息")


# 循环输入
while True:
    # 名字
    name = input("请输入你的名字\n")
    # 星座
    constellation = input("请输入你的星座：水瓶座请输入1，双鱼座请输入2，"
                          "白羊座请输入3，金牛座请输入4, 退出程序请输入0\n")
    constellation = int(constellation)
    if constellation == 0:
        break
    get_birthday(name, constellation)
