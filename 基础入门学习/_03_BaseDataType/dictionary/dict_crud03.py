my_dict = dict((("name", "Alan"), ("age", 22), ("sex", "female")))
# 通过键获取值
print(my_dict.get("name"))

# 通过值获取键
keys = my_dict.keys()
print("keys = ", keys)
# 转成列表
key_list = list(keys)
print("key_list = ", key_list)

# 获取所有值
values = my_dict.values()
print("value = ", values)
# 转成列表
values_list = list(values)
print("values_list = ", values_list)

# 可以将键和值 构建为双值子序列
print("my_dict.items() = ", my_dict.items())
kv = list(my_dict.items())
print("kv = ", kv)

# 根据值来寻找键
# 思路：
# 1、其实就是先将 键的结果集合 和 值列表集合转成列表，
# 2、因为他们的下标是一一对应的，所以求出值的下标，也就可以获得Key的相应下标
index = values_list.index(22)
print("key = ", key_list[index])
