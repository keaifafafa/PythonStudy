# 键是不允许重复的，后面的会覆盖前面的
my_dict = {"vx": "112242", "vx": "2344432", "age": 22}
print(my_dict)
# 键必须是不可变类型的
# 元组不可变，所以其可以作为键
my_dict1 = {(1, 2, 3, 4, 5): "Tuple"}
print(my_dict1)
# 列表可变，所以其不可以作为键
my_dict2 = {[1, 2, 3, 4, 5]: "Tuple"}
# TypeError: unhashable type: 'list'
print(my_dict2)


