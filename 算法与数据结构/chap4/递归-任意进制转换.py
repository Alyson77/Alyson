def toStr(n,base):
    convertString='0123456789ABCDEF'
    if n<base:
        return convertString[n]
    else:
        return toStr(n//base,base)+convertString[n%base] #string"+"到一起

print(toStr(1234,16))
print(toStr(20,2))
