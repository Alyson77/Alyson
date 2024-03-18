lst=[20,10,50,40,30]
print('排序前的列表',lst)
lst.sort()
print('排序后的列表',lst)
lst.sort(reverse=True)
print(lst)

print('-------使用内置函数sorted()--------')
lst=[20,10,50,40,30]
print('排序前的列表',lst)
new_lst=sorted(lst)
print(lst)
print(new_lst)
desc_lst=sorted(lst,reverse=True)
print(desc_lst)