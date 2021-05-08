import os

class Classroom:
    def __init__(self,name):
        self.name=name
        self.student=[]

class Student:
    def __init__(self,sid,name,gh):
        self.sid=sid
        self.name=name
        self.gh=gh
st=open(os.getcwd()+"/test2.csv")
s=st.readline()
IC=Classroom("智商一乙")
