import time
start=time.time()
def sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
print(sum(1000000))
end=time.time()
print('time1:',end-start)
start2=time.time()
def sum2(n):
    sum2=(n*(n+1))/2
    return sum2
print(sum2(1000000))
end2=time.time()
print('time2:',end2-start2)


