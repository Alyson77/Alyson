class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动')

car=Car('宝马X5')
car.start()
print(car.brand)

class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
stu.show()
print(stu.name)
#print(stu.__age) -->'Student' object has no attribute '__age'

print(dir(stu)) #查找Student大类的属性
print(stu._Student__age)