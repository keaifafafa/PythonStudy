# 统计一个字符串里的各数据类型的个数
intCount = charCount = otherCount = 0
string = input("请输入一个字符串\n")
for item in string:
    # 判断字符串是不是纯数字。
    # 注意，小数中有“.”，所以不算纯数字哦。复数有“-”，也不算纯数字
    if item.isdigit():
        intCount += 1
    # 判断字符串是否全部是“字母+中文”
    elif item.isalpha():
        charCount += 1
    # 为其他符号
    else:
        otherCount += 1
print(intCount, charCount, otherCount)
