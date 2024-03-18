import time
start = time.time()

with open('3.1415.txt','r')as file:
    pi=file.read()
    date=input('请输入您要查询的日期：')
    result=pi.find(date)
    if result==-1:
        print('抱歉，您查询的日期不存在。')
    else:
        print('您查询的日期在pi的第',result,'位。')

end = time.time()
print('运行时间: %s 秒' % (end - start))

