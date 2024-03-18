fp=open('/chap1/text1.txt', 'a+')
print('Hello World',file=fp)
fp.close()

#注：1、file=fp 是重点；2、地址用“/”而不能用“\”

print('aaa','bbb','ccc')