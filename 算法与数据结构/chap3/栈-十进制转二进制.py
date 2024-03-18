from stack import Stack

def devideBy2(decNumber):
    remstack=Stack()
    while decNumber>0:
        rem=decNumber%2
        remstack.push(rem)
        decNumber=decNumber//2
    binString=''
    while not remstack.isEmpty():
        binString=binString+str(remstack.pop())
    return binString

print(devideBy2(35))


