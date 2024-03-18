def fun1(*args):
    print(args)
    print(args[0])

fun1(10)
fun1(20,30)
fun1(40,50,60)

def fun2(**args):
    print(args)

fun2(a=10)
fun2(a=20,b=30,c=40)

def fun3(*args,**args2): #**args放在**args2之前
    pass