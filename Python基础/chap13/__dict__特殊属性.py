class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age

x=C('Mary',20)
print(x.__dict__)
print(C.__dict__)
print(x.__class__) #对象所属类
print(C.__bases__)
print(C.__base__)
print(C.__mro__) #查看类的层次结构
print(A.__subclasses__()) #查看子类的列表