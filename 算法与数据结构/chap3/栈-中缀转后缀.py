from stack import Stack

def InfixToPostfix(infixexpr):
    prec={} #定义一个字典用于规定操作符的优先级
    prec['*']=3
    prec['/']=3
    prec['+']=2
    prec['-']=2
    prec['(']=1
    opStack=Stack() #定义一个栈用于储存
    postfixList=[] #定义一个列表,用于最后join后的后缀结果的输出
    tokenList=infixexpr.split( ) #把输入的中缀表达式split成单个元素
    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'or token in '0123456789':
            postfixList.append(token)
        elif token=='(': #直接压入opStack栈中,优先级操作符作用相当于括号
            opStack.push(token)
        elif token==')': #反复弹出opStack栈顶的操作符至postfixList，寻找与之匹配的'('
            topToken=opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken=opStack.pop()
        else: #操作符进opStack栈待定，先弹出opStack栈顶优先级比自己高的操作符至postfixList
            while (not opStack.isEmpty()) and (prec[opStack.peek()]>=prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty(): #次序反转，依次弹出opStack栈顶操作符至postfixList
        postfixList.append(opStack.pop())
    return ''.join(postfixList)

print(InfixToPostfix('( A * B ) - ( C / D ) + ( E * 2 )'))
