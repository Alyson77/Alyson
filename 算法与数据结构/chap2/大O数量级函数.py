a=5
b=6
def fn(n):
    sum1=0
    sum2=0
    for i in range(n):
        for j in range(n):
            x=i*i
            y=j*j
            z=i*j
            sum1=sum1+x+y+z
    for k in range(n):
        w=a*k+45
        v=b*b
        sum2=sum2+w+v
    sum3=sum1+sum2
    return sum3
sum4=43+fn(2)
print(sum4)
