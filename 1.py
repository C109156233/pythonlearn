class City:
    def __init__(self,name):
        self.name=name
        self.area=area
class Area:
    def __init__(self,namea):
        self.namea=namea
        self.school=school
class School:
    def __init__(self,names):
        self.names=names
        self.dpt=dpt
class Dpt:
    def __init__(self,named):
        self.named=named
        self.classes=classes
class Classes:
    def __init__(self,namec):
        self.namec=namec
        self.student=student



class Student:
    def __init__(self,name1):
        self.c=None
        self.a=None
        self.s=None
        self.d=None
        self.cs=None

lin=Student()
lin.c=City("高雄市")
lin.a=Area("燕巢區")
lin.s=School("高應大")
lin.d=Dpt("智慧商務系")
lin.cs=Classes("乙班")