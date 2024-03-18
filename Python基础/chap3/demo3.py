a,b=10,20
print('交换之前：',a,b)
a,b=b,a #直接美美交换
print('交换之后：',a,b)

#比较运算符
a=10
b=10
print(a is b)

lst1=[11,22,33]
lst2=[11,22,33]
print(lst1==lst2)
print(lst1 is lst2)
print(id(lst1),id(lst2))

#布尔运算符
a=1
b=2
c=False
print(a==1 and b==1)
print(a==1 or b==1)
print(not c)

#in、not in
s='helloworld'
print('w' in s)
print('k' in s)
print('h' not in s)

#位运算 按二进制算的，可在excel表格里表示出来
print('——————————位运算——————————')
print(4&8) #同1则1，否则为0
print(4|8) #同0则0，否则为1
print(4<<1) #左移位1位为乘2倍
print(4>>1) #右移位1位为除以2



