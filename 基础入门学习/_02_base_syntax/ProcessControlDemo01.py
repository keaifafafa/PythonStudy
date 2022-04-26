# 获取等级的函数
def get_rank(score):
    if score >= 90:
        print("你的成绩等级为A")
    elif score >= 80:
        print("你的成绩等级为B")
    elif score >= 70:
        print("你的成绩等级为C")
    elif score >= 60:
        print("你的成绩等级为D")
    else:
        print("你的成绩等级为E")
    return


# 流程控制练习
score = input("请输入您的成绩：")
# 记得转型【input获得的是string类型】
score = int(score)
#  调用判断等级的函数
get_rank(score)
