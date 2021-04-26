# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:22:27 2021

@author: linnn
"""

k=float(input("請輸入路程公里數(km):"))

if k<=1.5:
    cost=75
else:
    kk=k-1.5
    if kk%0.25 ==0:
        cost=75+(kk/0.25)*5
    else:
        cost=75+((kk//0.25)+1)*5
           
print("所需車資為:",cost)