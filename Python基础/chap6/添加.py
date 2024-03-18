lst=[10,20,30]
print('原列表',lst,id(lst))
lst.append(100)
print('添加之后',lst,id(lst))
lst2=['hello','world']
#lst.append(lst2)
lst.extend(lst2)
print(lst) #-->[10, 20, 60, 30, 100, ['hello', 'world']]
lst.insert(2,60) #索引为2的元素新添加成了元素60
print(lst) #-->[10, 20, 60, 30, 100, 'hello', 'world']
lst3=['aaa','bbb','ccc']
lst[2:4]=lst3
print(lst) #-->[10, 20, 'aaa', 'bbb', 'ccc', 100, 'hello', 'world']