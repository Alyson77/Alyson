#for 循环写一写
for i in range(3):
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确！')
        break
    else:
        print('密码错误！')
else:
    print('对不起，三次均不正确。')

#while循环写一写
'''
a=0
while a<3:
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确！')
        break
    else:
        print('密码错误！')
    a+=1
else:
    print('对不起，三次均不正确。')
    
'''

