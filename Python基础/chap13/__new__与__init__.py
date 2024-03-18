class Person(object):
    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行，cls的id为{0}'.format(id(cls))) #5744
        obj=super().__new__(cls)
        print('创建对象id为{0}'.format(id(obj))) #9440
        return obj

    def __init__(self,name,age):
        print('__init__被调用执行，self的id为{0}'.format(id(self))) #9440
        self.name=name
        self.age=age

print('object类对象的id为{0}'.format(id(object))) #1744
print('Person类对象的id为{0}'.format(id(Person))) #5744

p1=Person('张三',20)
print('p1这个Person类的实例对象的id为{0}'.format(id(p1))) #9440

