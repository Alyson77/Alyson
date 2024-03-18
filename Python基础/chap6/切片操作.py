print('------step>0------')
lst=[10,20,30,40,50,60,70,80]
print(lst,id(lst))
lst2=lst[1:6:1]
print(lst2,id(lst2))
print(lst[1:6])
print(lst[1:6:2])
print(lst[:6:2])
print(lst[1::2])

print('------step<0------')
lst=[10,20,30,40,50,60,70,80]
print('原列表：',lst)
print(lst[::-1])
print(lst[7::-1])
print(lst[3::-1])
print(lst[6:0:-1])