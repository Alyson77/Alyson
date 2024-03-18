# 获取指定的元素索引
lst=['hello','world',98,'hello']
print(lst.index('hello'))
# print(lst.index('Python')) -->报错，不存在
# print(lst.index('hello',1,3)) -->'world'和98里没有'hello'
print(lst.index('hello',1,4))

# 获取指定索引的元素
lst=['hello','world',98,'hello']
print(lst[1])
print(lst[-3])
#print(lst[4]) -->报错，不存在