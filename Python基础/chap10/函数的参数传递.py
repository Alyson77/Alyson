def  calc(a,b):#a,b为形式参数，在函数的定义处
    c=a+b
    return c

res1=calc(10,20)
print(res1)

res2=calc(b=10,a=20) #10，20为实际参数的值，在函数的调用处
#'='左侧的a,b为关键字参数
print(res2)