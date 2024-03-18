class Animal(object):
    def eat(self):
        print('动物吃...')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class Person(object):
    def eat(self):
        print('人吃五谷杂粮')

def fun(obj): #定义一个函数
    obj.eat() #obj为后面的Cat()那些

fun(Dog()) #Dog为类对象，Dog()为实例对象
fun(Cat())
fun(Animal())
fun(Person())