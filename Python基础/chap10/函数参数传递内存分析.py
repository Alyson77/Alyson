def fun(arg1,arg2):
    print('arg1=',arg1)
    print('arg2=',arg2)
    arg1=100
    arg2.append(10)
    print('arg1=', arg1,id(arg1))
    print('arg2=', arg2,id(arg2))

n1=11
n2=[22,33,44]
print(n1,id(n1))
print(n2,id(n2))
fun(n1,n2)
print(n1,id(n1)) #-->11,arg1=100与n1无关，n1只指向不可变的11
print(n2,id(n2)) #-->[22, 33, 44, 10],arg2.append(10)与n2有关，n2指向可变的列表，列表id不变