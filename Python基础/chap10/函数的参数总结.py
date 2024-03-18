def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)

fun(10,20,30)
lst=[11,22,33]
fun(*lst)

fun(a=100,c=200,b=300)
dic={'a':111,'c':222,'b':333}
fun(**dic)

def fun2(a,b,*,c,d): #从*之后的参数，函数调用时只能采用关键字实参传递
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)

fun2(1,2,c=3,d=4)

#函数定义时的形参顺序问题
def fun3(a,b,*,c,d,**args):
    pass

def fun4(*args1,**args2):
    pass

def fun5(a,b=10,*args1,**args2):
    pass