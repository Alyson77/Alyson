class CPU():
    pass
class Disk():
    pass
class Computer():
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

cpu1=CPU()
cpu2=cpu1
print(cpu1)
print(cpu2)

disk=Disk()
computer=Computer(cpu1,disk)
print('--------------类的浅拷贝--------------')
#类的浅拷贝
import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk) #AAF0 AB50 AB20
print(computer2,computer2.cpu,computer2.disk) #A910 AB50 AB20

print('--------------深拷贝---------------')
#深拷贝
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)