class Student:
    native_place='吉林' #类属性
    def __init__(self, name, age): #初始化方法
        self.name=name #实例属性，将局部变量name值赋给实例属性
        self.age=age
    def eat(self): #实例方法
        print('学生在吃饭')
    @staticmethod #静态方法
    def method( ):
        print('静态方法，使用staticmethod修饰')
    @classmethod #类方法
    def cm(cls):
        print('类方法，使用classmethod修饰')

def drink():
    print('喝水')

#创建Student类的对象
stu1=Student('张三',20)
print(id(stu1))
print(type(stu1))
print(stu1)

print('-----------------------')
stu2=Student('李四',22)
stu2.eat()
print(stu2.name)
print(stu2.age)

print('-----------------------')
class Tanxl:
    def __init__(self,name,gender,weapon):
        self.name=name
        self.gender=gender
        self.weapon=weapon

    def say1(self):
        print('洛神：不可以么？')

    def say2(self):
        print('师师：可...可以。')

ls=Tanxl('洛神','女','巨阙')
sqy=Tanxl('师清漪','女','春雪')

print('洛神的性别是：',ls.gender)
print('师师的武器是：',sqy.weapon)
ls.say1()
Tanxl.say2(sqy)



