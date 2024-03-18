#求1-100所有偶数和
a=1
sum=0
while a<=100:
    if a%2==0: #也可以改写成 if not bool(a%2):
        sum+=a
    a+=1
print('1~100所有偶数和为：',sum)