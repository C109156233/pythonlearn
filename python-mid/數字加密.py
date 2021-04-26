# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:02:03 2021

@author: linnn
"""
list=[]
a ,b ,c ,d =map(int, input("請輸入一組四位數字:"))
list.append(a)
list.append(b)
list.append(c)
list.append(d)
list[0]=(c+7)%10
list[1]=(d+7)%10
list[2]=(a+7)%10
list[3]=(b+7)%10
print("輸出加密後數字為:%d %d %d %d"%(list[0],list[1],list[2],list[3]))