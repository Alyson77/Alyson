s={10,20,30,40,50,60}
print(10 in s,100 in s)

s.remove(10)
print(s)
# s.remove(555) -->key error
s.discard(555) #没有555也不报错，
print(s)
s.pop() #删了谁是任意的，且不可指定参数
print(s)
s.clear()
print(s)

s.add(80)
print(s)
s.update({200,300,400})
print(s)
s.update([111])
s.update((222,333))
print(s)
