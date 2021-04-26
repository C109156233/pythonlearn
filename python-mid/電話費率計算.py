# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 17:23:38 2021

@author: linnn
"""

m, n = map(int, input("請輸入月租費型式及通話時間為:").split())
if m==186:
    a=n*0.09
    if (a)>186:
        b=(a)*0.9
    if a>186*2:
        b=(a)*0.8
    print(round(b,1))
if m==386:
    a=n*0.08
    if (a)>386:
        b=(a)*0.8
    if a>386*2:
        b=(a)*0.7
    print(round(b,1))
if m==586:
    a=n*0.07
    if (a)>586:
        b=(a)*0.7
    if a>586*2:
        b=(a)*0.6
    print(round(b,1))
if m==986:
    a=n*0.06
    if (a)>986:
        b=(a)*0.6
    if a>986*2:
        b=(a)*0.5
    print(round(b,1))