#coding:utf-8
#用来查阅保留字的，取名不能用
import keyword
print(keyword.kwlist)

name='Alyson'
print(name)
print('标识',id(name))
print('类型',type(name))
print('值',name)

#整数进制
print('十进制',20)
print('二进制',0b1010111) #0b开头
print('八进制',0o157) #0o开头
print('十六进制',0x16A) #0x开头

#浮点数decimal模块
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

#字符串的引号问题
str1='人生苦短，我用Python'
str2="人生苦短，我用Python"
str3='''人生苦短
我用Python'''
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))

#数据类型转换
name='Alyson'
age=22
print(name,type(name),age,type(age))
print('My name is '+name+', I am '+str(age)+' years old.')
a=0.5
b=True
print(str(a),str(b),type(str(a)),type(str(b)))

s1='98.0'
s2='10'
ff=True
i=5
print(float(s1),type(float(s1)),float(s2),type(float(s2)),float(ff),type(float(ff)),float(i),type(float(i)))

'''嘿嘿
我是多行注释
三引号之间
我可以换行'''