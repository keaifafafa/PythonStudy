# 简单菜单
my_menu = (('香辣鸡腿堡', '劲脆鸡腿堡', '新奥尔良堡'),
           ('薯条', '黄金鸡块', '鱿鱼圈'),
           ('奶茶', '可口可乐', '百事可乐'))

while True:
    # 这里不够完善，因为有一些无法转换成数字的字符串
    selection = int(input("请输入你的选择：1表示汉堡类，2表示薯条类，3表示可乐类，4表示退出\n"))
    if selection == 1:
        print(my_menu[selection - 1])
    elif selection == 2:
        print(my_menu[selection - 1])
    elif selection == 3:
        print(my_menu[selection - 1])
    elif selection == 4:
        print("谢谢惠顾，欢迎下次光临~")
        break
    else:
        print("暂不存在该商品，请重新输入")
