def fun1(a,b):
    c=a+b
    print(c)
fun1(1,2)

def fun2(name):
    print(name)
name='AAA' #name为全局变量
fun2(name)

def fun3():
    global age
    age=22
    print(age)
fun3()


