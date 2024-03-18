from stack import Stack

def devideByN(decNumber,base):
    digits='0123456789ABCDEF'
    remstack=Stack()
    while decNumber>0:
        rem=decNumber % base
        remstack.push(rem)
        decNumber=decNumber // base
    binString=''
    while not remstack.isEmpty():
        binString=binString+str(digits[remstack.pop()])
    return binString

print(devideByN(200,16))



