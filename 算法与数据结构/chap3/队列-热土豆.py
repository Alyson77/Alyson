from queue import Queue

def HotPotato(namelist,num):
    simqueue=Queue()
    for name in namelist:
        simqueue.enqueue(name)
        while simqueue.size()>1:
            for i in range(num):
                simqueue.enqueue(simqueue.dequeue()) #完成一次传递
            simqueue.dequeue() #此时队首出列
        return simqueue.dequeue()

print(HotPotato(['Bill','David','Susan','Jane','Kent','Brand'],7))