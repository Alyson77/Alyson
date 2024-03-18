import timeit
import random #生成随机数，用于检索列表或字典中任意的值是否存在

for i in range(100,10001,2000):
    t=timeit.Timer('random.randrange(%d) in x'%i,'from __main__ import random,x')
    x=list(range(i))
    list_time=t.timeit(number=1000) #检索列表中任意值，重复运行1000次
    x={j:None for j in range(i)}
    d_time=t.timeit(number=1000) #检索字典中任意值，重复运行1000次
    print('%d,%10.3f,%10.3f'%(i,list_time,d_time)) #%10.3f:按10字符域宽左对齐，保留3位小数的形式输出变量的值


