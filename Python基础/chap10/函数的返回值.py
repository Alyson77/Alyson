def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

lst=[10,29,34,23,44,53,55]
print(fun(lst))

def fun1():
    print('aaa')
fun1()

def fun2():
    return 'bbb'
res1=fun2()
print(res1)

def fun3():
    return 'aaa','bbb','ccc'
res2=fun3()
print(res2)