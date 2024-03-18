from stack import Stack
opens='([{'
closers=')]}'
def parChecker(symbolString):
    s=Stack()
    balanced=True
    index=0
    while index<len(symbolString) and balanced:
        symbol=symbolString[index]
        if symbol in'([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            elif opens.index(s.peek())==closers.index(symbol):
                s.pop()
            else:
                balanced = False
        index=index+1
    if balanced and s.isEmpty():
        return True
    else:
        return False
print(parChecker('{([])}'))
print(parChecker('{([]}'))

