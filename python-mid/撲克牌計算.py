# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 17:10:04 2021

@author: linnn
"""


L=[]

for i in range(5):
  a=(input(":"))  
  if a=='A':
    a=1
  if a=='J':
    a=11
  if a=='Q':
    a=12
  if a=='K':
    a=13
  L.append(int(a))
print(sum(L))