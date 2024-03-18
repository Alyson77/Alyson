t=('Python','world',98) #此处()可省略
print(t)
print(type(t))

t2=tuple(('Python','world',98))
print(t2)
print(type(t2))

t3=('hello',) #元组只有一个元素，要加小括号和逗号
# print(type('hello')) --> <class 'str'>
print(t3)
print(type(t3))

t4=()
t5=tuple()
print(t4)
print(t5)