s='hello,python'
a=s.upper()
print(a,id(a))
print(s,id(s))
b=s.lower()
print(b,id(b)) #转换之后会产生新的字符串
print(b==s)
print(b is s)

s2='hello,Python'
print(s2.swapcase())
print(s2.capitalize())
print(s2.title())
