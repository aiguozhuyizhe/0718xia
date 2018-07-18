#多继承的例子
#子类可以直接拥有父类的属性和方法，私有属性和方法除外
class Fish():
    def __init__(self,name):
        self.name = name
    def swim(self):
        print(" i am swimming")
class Bird():
    def __init__(self,name):
        self.name = name
    def Fly(self):
        print("i am flying")
class Person():
    def __init__(self,name):
        self.name =name
    def worked(self):
        print("i am woring")



class SuperMan(Person,Bird,Fish):
    def __init__(self,name):
        self.name = name
    pass
s=SuperMan("yueyue")
s.Fly()
s.swim()

#单继承例子
class Student(Person):
    def __init__(self, name):
        self.name = name


stu=Student("xiaojia")
stu.worked()