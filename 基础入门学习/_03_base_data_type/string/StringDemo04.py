string = 'Life is short, I love something'
# 方式一
# 先找到下标
index = string.index("so")
print(index)
# 然后截取目标下标以前的，并进行拼接操作
newStr = string[: index] + "python"
print(newStr)

# 方式二：调用replace
print(string.replace('something', 'python'))

