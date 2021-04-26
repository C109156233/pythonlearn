# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 16:08:51 2021

@author: linnn
"""

dict1={}

n=int(input("請輸入n值:"))
for nm in range(n):  
    nm=str(input("請輸入人名:"))
    em=str(input("請輸入電子郵件:"))
    dict1[nm]=em
    n+=1
s=input("請輸入要查詢的人名:")
print("{}的電子郵件是:".format(s),dict1.get(s))





