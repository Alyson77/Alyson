class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)

stu1=Student('张三')
stu2=Student('李四')
stu3=Student('Amy')

s1=stu1+stu2
print(s1)
s2=stu2.__add__(stu1)
print(s2)
print(len(stu3))

