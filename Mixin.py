# Mixin案例
class Person():
    name = "xiaojia"
    age = 18
    def eat(self):
        print("eating")
    def drink(self):
        print("drinking")
    def sleep(self):
        print("sleeping")
class Teachar(Person):
    def work(self):
        print("working")
class Student(Person):
    def study(self):
        print("studying")
class Tutor(Teachar,Student):#助教
    pass
t=Tutor()

print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)



print(" * " * 20)
class TeacharMixin():
    def work(self):
        print("work")
class StudentMixin():
    def study(self):
        print("study")
class TutorMixin(Person,TeacharMixin,StudentMixin):
    pass

tt=TutorMixin()
print(TutorMixin.__mro__)
print(tt.__dict__)
print(TutorMixin.__dict__)