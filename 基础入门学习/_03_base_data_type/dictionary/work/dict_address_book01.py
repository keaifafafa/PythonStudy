# 实现基于字典的简单通讯录功能

my_friends = dict([("小明", "001, 广州"), ("小红", "002, 深圳"), ("小刘", "003, 上海")])

while True:
    selection = input("请对好友的通讯录进行操作，"
                      "0：退出程序，"
                      "1：添加好友信息，"
                      "2：删除好友信息，"
                      "3：修改好友信息，"
                      "4：查询好友信息\n")
    selection = int(selection)
    if selection == 0:
        print("程序退出")
        break
    if selection == 1:
        print("增添前：", my_friends)
        name = input("请输入新增姓名：")
        address = input("请输入新增地址：")
        my_friends.update({name: address})
        print("增添后：", my_friends)
    elif selection == 2:
        name = input("请输入要删除的姓名:")
        print(my_friends.pop(name, "该用户不存在~"))
    elif selection == 3:
        print("修改前：", my_friends)
        name = input("请输入需要修改人的姓名：")
        address = input("请输入修改地址：")
        my_friends.update({name: address})
        print("修改后：", my_friends)
    elif selection == 4:
        name = input("请输入需要查询的姓名：")
        # 这里建议使用get函数，这样就不用手动去解决不存在的异常的
        print(my_friends.get(name, "该好友不存在！"))
    else:
        print("此操作不存在！")
