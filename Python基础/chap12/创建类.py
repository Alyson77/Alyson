class Student:
    native_pace='吉林' #类属性

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

print(id(Student)) #-->2443680376784
print(type(Student)) #--><class 'type'>
print(Student) #--><class '__main__.Student'>
