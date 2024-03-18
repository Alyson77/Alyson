# a.txt:中国
       #美丽
file=open('a.txt','r')
print(file.read()) #-->中国
                   #   美丽
print(file.read(2)) #-->中国
print(file.readline())#-->中国
print(file.readlines()) #-->中国
                        #   美丽
file=open('d.txt','a')
file.write('hello')
lst=['java','go','Python']
file.writelines(lst)
file.close()

file=open('b.txt','r')
file.seek(2) #一个汉字占2个字符，一个字母占1个字符
print(file.read()) #-->llo worldPython
print(file.tell()) #17
file.close()

file=open('e.txt','a')
file.write('hello')
file.flush()
file.write('world')
file.close()