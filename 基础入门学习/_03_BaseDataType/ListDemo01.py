# List（列表）
# 语法：变量[头下标:尾下标]
# 索引值以 0 为开始值，-1 为从末尾的开始位置。
list = ['abcd', 786, 2.223, 'fafa', 70.2]
tinylist = [123, 'keaifa']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[0:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表
print("------------------")

# 与Python字符串不一样的是，列表中的元素是可以改变的：
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
print(a)
print("------------------")

"""
注意事项
1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的。
"""


# Python 列表截取可以接收第三个参数，参数作用是截取的步长，
# 以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
# 如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：
def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")
    return inputWords[-1::-1]


if __name__ == "__main__":
    # 注意要加空格，才有效果哦
    input = "i love u"
    rw = reverseWords(input)
    print(rw)
