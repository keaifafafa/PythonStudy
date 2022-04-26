#  求圆形的面积和周长

# 定义π
PI = 3.142
#  获取面积
def getArea(radius):
    return PI * (radius * radius)
# 获取周长
def getPerimeter(radius):
    return PI * (2 * radius)

radius = int(input("请输入半径:"))
# 调用方法
print("圆的面积为 %.6f" % getArea(radius))
print("圆的周长为 %.6f" % getPerimeter(radius))
