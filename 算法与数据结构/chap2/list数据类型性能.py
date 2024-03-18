def test1():
    l=[]
    for i in range(1000):
        l=l+[i]
def test2():
    l=[]
    for i in range(1000):
        l.append(i)
def test3():
    l=[i for i in range(1000)] #列表生成式
def test4():
    l=list(range(1000)) #range()转成列表
from timeit import Timer
t1=Timer('test1()','from __main__ import test1') #反复运行语句和安装语句
print('concat %f seconds'% t1.timeit(number=1000)) #%f为浮点数占位符
t2=Timer('test2()','from __main__ import test2')
print('append %f seconds'% t2.timeit(number=1000))
t3=Timer('test3()','from __main__ import test3')
print('comprehension %f seconds'% t3.timeit(number=1000))
t4=Timer('test4()','from __main__ import test4')
print('list range %f seconds'% t4.timeit(number=1000))


