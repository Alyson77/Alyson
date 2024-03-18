answer=input('请问您是会员吗？请输入yes or no：')
money=float(input('请输入您的购物金额：'))
if answer=='yes':
    if money>=200:
        print('打8折，付款金额为：',money*0.8)
    elif money>=100:
        print('打9折，付款金额为：',money*0.9)
    else:
        print('不打折，付款金额为：',money)
if answer=='no':
    if money>=200:
        print('打8.5折，付款金额为：',money*0.85)
    elif money>=100:
        print('打9.5折，付款金额为：',money*0.95)
    else:
        print('不打折，付款金额为：',money)
