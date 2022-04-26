string = "less is more"
# 将字符串的第一个字符转换为大写
print(string.capitalize())

# 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
print(string.center(50, '*'))

# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
print(string.count('s', 0, len(string)))

# Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
bytes.decode("utf-8", )
