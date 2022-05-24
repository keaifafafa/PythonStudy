import sys

sys.path.append(r'E:\\编程学习\\Python\\PythonStudy\\基础入门学习\\_05_function\\import_function\\')

# 导入函数模块
import custom_func

custom_func.make_steak(5, "红酒")

# # 导入某个函数
# from custom_func import make_steak
#
# # 导入所有函数
# from custom_func import *
#
# # 给函数起个别名 这个时候就不可以再用原来的名字了
# from custom_func import make_steak as mk
#
# # 给模块起别名
# import custom_func as cf
