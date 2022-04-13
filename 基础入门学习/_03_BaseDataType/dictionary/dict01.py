# 键值对类型【json】
# 创建方式一
my_dict1 = {'name': '丁佳杰', 'age': 20, 'hobby': 'sing'}
print(my_dict1)

# 创建方式二 注意一定是要双值子序列
# 要注意dict函数只能传入一个参数，所以需要第二个()来包裹最里面的三个()
my_dict2 = dict([('name', '丁佳杰'), ('age', 20), ('hobby', 'sing')])
print(my_dict2)

# 创建方式三 使用函数创建
# 注意键不用加引号，字符串值才需要加引号
my_dict3 = dict(name="佳杰", age=20, hobby='sing')
print(my_dict3)

# 键必须是不可变的类型，所以键不可以用列表，值无所谓【因为值没必要】
