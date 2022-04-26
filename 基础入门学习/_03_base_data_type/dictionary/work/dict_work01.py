# 创建一个字典（dict）并进行增删改查操作
# 1、创建字典
my_dict = dict([
    ("Math", 96), ("English", 86),
    ("Chinese", 95.5), ("Biology", 86),
    ("Physics", None)
])
print(my_dict)
# 2、添加键值对
my_dict.update({"History": 88})
print(my_dict)
# 3、删除键值对
my_dict.pop("Physics")
print(my_dict)
# 4、将浮点数四舍五入取整
my_dict["Chinese"] = round(my_dict["Chinese"])
print(my_dict)
# 5、查询键"Math"的对应值
print(my_dict["Math"])
