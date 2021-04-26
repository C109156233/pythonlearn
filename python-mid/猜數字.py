# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 17:05:47 2021

@author: linnn
"""

a=list("1234")
b=list(input("PLZ :"))
A=0
B=0

for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            if i==j:
                A+=1
            else:
                B+=1

print(A,"A",B,"B")