import time
start = time.time()

month1 = [1, 3, 5, 7, 8, 10, 12]
month2 = [4, 6, 9, 11]
month3 = [2]
lst=[]
def fun1(a,b,c):
    lst1 = [a,b,c]
    lst2 = [str(i) for i in lst1]
    join1 = int(''.join(lst2))
    lst.append(join1)
def fun2():
    for month in range(1,13):
        if month==2 and year%4 == 0:
            for day in range(1, 30):
                fun1(year,month,day)
        elif month==2 and year%4 != 0:
            for day in range(1, 29):
                fun1(year,month,day)
        elif month in month1:
            for day in range(1, 32):
                fun1(year,month,day)
        else:
            for day in range(1, 31):
                fun1(year,month,day)

year=int(input('请输入您要查询的年份：'))
fun2()
with open('3.1415.txt','r')as file:
    pi=file.read()
    i=0
    for date in lst:
        result=pi.find(str(date))
        if result==-1:
            continue
        else:
            i+=1
            print('您查询的年份日期',date,'在pi的第',result,'位。')
    print('您查询的年份中共有',i,'个日期在pi中可以找到。')

end = time.time()
print('运行时间: %s 秒' % (end - start))
