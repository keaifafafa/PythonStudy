# 格式化字符串
print("我叫%s，今年%d岁了!" % ("发发1", 21))
# 通过大括号
print("我叫{}，今年{}岁了!".format("发发2", 21))
# 通过关键字
print("我叫{name}，今年{age}岁了!".format(name="发发3", age=21))
# 通过索引 【类似第二种】
print("我叫{0}，今年{1}岁了!".format("发发4", 21))
# 通过list【类似数组】，然后可以参照第四种【用下标来定位list里的元素】
info = ["可爱发", 22]
print("我叫{0[0]}，今年{0[1]}岁了!".format(info))

# 保留n位小数【四舍五入】
print("{:.2f}".format(321.456787461))
# 做金额的千分隔符
print("{:,}".format(1234567890))
# 进制转换 b，d,o,x 二、十、八、十六进制
print("{:b}".format(17))
print("{:d}".format(17))
print("{:o}".format(17))
print("{:x}".format(17))
