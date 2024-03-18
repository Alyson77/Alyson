s={1,2,3,4,4,5,5,6,6,6}
print(s) #-->{1, 2, 3, 4, 5, 6} 集合元素不允许重复

s1=set(range(6))
print(s1,type(s1))

s2=set([1,2,3,3,3])
print(s2,type(s2))

s3=set((1,2,3,3,3,65))
print(s3,type(s3)) #-->{65, 1, 2, 3} 集合元素是无序的

s4=set('Python')
print(s4,type(s4))

s5=set({11,22,33,44,55})
print(s5,type(s5))

s6=set()
print(type(s6)) #s6={}是空字典