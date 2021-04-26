# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 15:33:02 2021

@author: linnn
"""
a=["rat","ox","tiger","rabbit","dragon","snake","horse","sheep","monkey","rooster","dog","pig"]
o=int(input(""))
ans=o%12
if ans==4:
    print(a[0])
if ans==5:
    print(a[1])
if ans==6:
    print(a[2])
if ans==7:
    print(a[3])
if ans==8:
    print(a[4])
if ans==9:
    print(a[5])
if ans==10:
    print(a[6])
if ans==11:
    print(a[7])
if ans==0:
    print(a[8])
if ans==1:
    print(a[9])
if ans==2:
    print(a[10])
if ans==3:
    print(a[11])