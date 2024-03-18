s='天涯共此时'
byte=s.encode(encoding='GBK') #编码 GBK一个中文占2个字符
print(byte)
print(byte.decode(encoding='GBK')) #解码

byte=s.encode(encoding='UTF-8') #编码 UTF-8一个中文占3个字符
print(byte)
print(byte.decode(encoding='UTF-8')) #解码