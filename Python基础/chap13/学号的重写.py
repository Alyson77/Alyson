class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age) #调用父类self.name和self.age的赋值
        self.stu_no=stu_no
    def info(self): #info()的重写
        super().info()
        print('学号为：',self.stu_no)

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear
    def info(self): #info()的重写
        super().info()
        print('教龄为：', self.teachofyear)

stu=Student('张三',20,'1001')
teacher=Teacher('李四',34,10)

stu.info()
teacher.info()


