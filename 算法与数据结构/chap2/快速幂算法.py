import time
start=time.time()
def pow(x,n):
    if n==0:
        return 1
    elif n==1:
        return x
    elif n%2==0:
        return pow(x * x,n//2) #x^n=(x²)^(n//2)
    else:
        return pow(x * x,n//2)* x #x^n=(x²)^(n//2)*x
print(pow(1111,2222))
end=time.time()
print(end-start)


