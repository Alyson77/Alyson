from timeit import Timer
lst=list(range(100000))

def test1():
    global lst
    lst.pop(0)

t1=Timer('test1()','from __main__ import test1')
print(f'{t1.timeit(number=1000):.3f}seconds')