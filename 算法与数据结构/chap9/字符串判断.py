s1='hello,world'
s2='hello world'
s3='hello_world'
s4='张三_111_abc'
print(s1.isidentifier())
print(s2.isidentifier())
print(s3.isidentifier())
print(s4.isidentifier()) #字母（汉字）、数字、下划线算合法标识符

print('\t'.isspace())
print('张三'.isalpha()) #汉字算字母
print('123四'.isdecimal()) #'四'不算十进制数字
print('ⅡⅡⅡ'.isdecimal()) #罗马数字不算十进制数字
print('123四'.isnumeric()) #'四'算数字
print('ⅡⅡⅡ'.isnumeric()) #罗马数字算数字
print('abc!'.isalnum())