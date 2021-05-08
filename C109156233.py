class Student:
    def __init__(self,nm,classes):
        self.nm=nm
        self.classes=classes

class City:
    def __init__(self,ct):
        self.ct=ct

class Area:
    def __init__(self,area):
        self.area=area

class School:
    def __init__(self,school):
        self.school=school

class Dpt:
    def __init__(self,dpt):
        self.dpt=dpt



lin=City("Kaohsiung")
lin.ct=Area("YanChao")
lin.ct.area=School("NKUST")
lin.ct.area.school=Dpt("IC")
lin.ct.area.school.dpt=Student("lin","Class B")