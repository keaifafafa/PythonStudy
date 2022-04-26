# 字典的增删改查

my_dict = dict(("py", ("name", "Alan"), ("age", 22)))
# 增加元素
# 方式一
my_dict["hobby"] = "basketball"
print(my_dict)
# 方式二
my_dict2 = {"nation": "Han", "sex": "female"}
my_dict.update(my_dict2)
print(my_dict)

# 删除元素 返回删除键的值
res = my_dict.pop("nation")
print(res)
print(my_dict)

# 修改元素
# 方式一：和增加元素一样【如果存在相关键，则修改】
my_dict3 = {"sex": "male"}
my_dict.update(my_dict3)
print(my_dict)
# 方式二，直接赋值
my_dict["name"] = "Bob"
print(my_dict)

# 查找
print(my_dict["age"])

