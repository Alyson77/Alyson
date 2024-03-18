num1=int(input('请输入整数1：'))
num2=int(input('请输入整数2：'))

'''如果是常规if else应该写成：

if num1>=num2:
    print(num1,'大于等于',num2)
if num1 < num2:
    print(num1, '小于', num2)
    
现在用条件表达式改写一下：'''

print(str(num1)+'大于等于'+str(num2) if num1>=num2 else str(num1)+'小于'+str(num2))


