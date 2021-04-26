# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 17:37:55 2021

@author: linnn
"""

m=int(input("請輸入月:"))
d=int(input("請輸入日:"))
s=(m*2+d)%3
if s==0:
    print("普通")
if s==1:
    print("吉")
if s==2:
    print("大吉")