for i in 'Python':
    print(i)

for a in range(1,10,2):
    print(a)

for _ in range(3):
    print('520!')

#计算1~100偶数累加和
sum=0
for a in range(1,101):
    if not bool(a%2):
       sum+=a
print('1~100偶数和为：',sum)