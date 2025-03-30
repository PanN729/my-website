# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 19:27:05 2025

@author: PanN
"""

stu_num=input("请输入你的学号:")
first3=stu_num[0:3]
last3=stu_num[7:]
print(first3)
print(last3)
first3_float=float(first3)
last3_float=float(last3)
print(first3,"/", last3, "=", round(first3_float/last3_float,2)) 