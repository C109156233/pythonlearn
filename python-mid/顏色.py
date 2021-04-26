# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:09:37 2021

@author: linnn
"""

f={"蘋果":"紅色","香蕉":"黃色","葡萄":"紫色","藍莓":"藍色","橘子":"橘色"}
print("dict_keys(['蘋果','香蕉','葡萄','藍莓','橘子'])")
ff=input("請輸入水果:")
print("{}是".format(ff),f.get(ff))