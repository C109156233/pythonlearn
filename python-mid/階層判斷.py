# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 15:49:24 2021

@author: linnn
"""


m=int(input("請輸入M?"))
b=1
i=1
while(b<m):
    i=i+1
    b=b*i
print("超過M為",m,"的最小值為:",i)