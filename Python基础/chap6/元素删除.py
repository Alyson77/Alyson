lst=[10,20,30,40,50,60,30]
lst.remove(30)
lst.pop(0)
lst.pop()
print(lst)

#切片操作
lst2=lst[1:3]
print(lst) #-->[20,40,50,60]
print(lst2) #-->[40,50]
lst[1:3]=[]
print(lst) #-->[20,60]


