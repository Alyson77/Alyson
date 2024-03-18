score=int(input('请输入一个成绩：'))
if score>=90 and score<=100: #可改写成 if 90<=score<=100:
    print('A级')
elif 60<=score<=89:
    print('B级')
elif score>=0 and score<=59:
    print('C级')
else:
    print('对不起，该成绩无效')
