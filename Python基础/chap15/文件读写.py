file=open('a.txt','r')
print(file.readlines())
file.close() #-->['中国美丽\n']

file=open('b.txt','w')
file.write('hello world')
file.close() #-->新建了b.txt，打开是hello world

file=open('b.txt','a')
file.write('Python')
file.close() #-->b.txt变成了hello worldPython

src_file=open('c.jpg','rb')
target_file=open('copyc.jpg','wb')
target_file.write(src_file.read()) #边读边写
target_file.close()
src_file.close() #-->创建的copyc.jpg与c.jpg图片一样