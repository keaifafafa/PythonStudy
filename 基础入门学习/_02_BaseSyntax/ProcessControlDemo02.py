# 循环遍历【函数命名用小写，多个词中间用"_",如果在开头加"_"则表示是私有的函数】
def list_all(num):
    while num > 0:
        print(num)
        num -= 1
    return


# 主函数
def main():
    list_all(10)
    return


if __name__ == '__main__':
    main()
