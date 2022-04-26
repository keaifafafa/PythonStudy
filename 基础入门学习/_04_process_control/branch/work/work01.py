score = input("请输入成绩：")
score = int(score)
if score >= 90:
    print("等级为A")
elif score >= 80:
    print("等级为B")
elif score >= 70:
    print("等级为C")
elif score >= 60:
    print("等级为D")
elif score < 60:
    print("等级为E")
