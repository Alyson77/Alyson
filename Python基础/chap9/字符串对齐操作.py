s='hello,Python'
print(s.center(20,'*'))
print(s.ljust(20,'*'))
print(s.rjust(20,'*'))
print(s.rjust(20)) #默认添加的是空格
print(s.zfill(20)) #默认添加的是0

s2='-8910'
print(s2.zfill(8)) #'-'也占了一位，但0添加在'-'之后

