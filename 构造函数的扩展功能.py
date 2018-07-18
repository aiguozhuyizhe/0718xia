class A():
    pass
class B(A):
    def __init__(self,name,adr):
        print("B")
        print(name)
        print("adr")
class C(B):
    def __init__(self,name,adr):#先初始化父类中的参数
        # C中想扩展B的构造函数后添加功能
        #方法1：
        #B.__init__(self,name)
        #方法2：
        #首先调用父类构造函数
        super(C, self).__init__(name,adr)
        #以下是添加的功能
        age = 18
        print("年龄是{0}".format(age))



c=C("xiaojia",adr="mingxi")