list = [110, 'dog', 'cat', 120, 'apple']
# 先插入空列表
list.insert(list.index('dog') + 1, [])
# 删除apple
list.remove('apple')
# 分别找出两个数字，并扩大10倍
index1 = list.index(110)
index2 = list.index(120)
list[index1] = list[index1] * 10
list[index2] = list[index2] * 10
print(list)
