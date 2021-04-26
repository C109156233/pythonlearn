# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 19:37:06 2021

@author: linnn
"""

listscore=[]
listsub=["國文","英文","微積分","體育","程式設計"]
c=int(input("國文:"))
e=int(input("英文:"))
m=int(input("微積分:"))
s=int(input("體育:"))
p=int(input("程式設計:"))
listscore.append(c)
listscore.append(e)
listscore.append(m)
listscore.append(s)
listscore.append(p)

ave=sum(listscore)/5

print("平均成績:%2d"%ave)
a_dict=dict(zip(listscore,listsub))
mx=max(listscore)
mn=min(listscore)

print("最高分科目:{}".format(mx),a_dict.get(95))
print("最低分科目:{}".format(mn),a_dict.get(55))