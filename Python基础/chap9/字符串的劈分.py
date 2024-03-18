s1='hello world Python'
lst=s1.split()
print(lst)

s2='hello|world|Python'
lst1=s2.split(sep='|')
print(lst1)
lst2=s2.split(sep='*') #字符串里查不到'*'，无处可分
print(lst2)

s3='hello|world|Python|aaa|bbb|ccc'
lst4=s3.split(sep='|',maxsplit=3) #最大分3次就不分了
print(lst4)

s4='aaa|bbb|ccc|ddd'
lst5=s4.rsplit(sep='|',maxsplit=1)
print(lst5)


