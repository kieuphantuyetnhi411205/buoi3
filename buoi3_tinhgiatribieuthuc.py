# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:18:28 2024

@author: KIEUNHI
"""

import math
a = float(input("Nhập vào số thực a: "))
b = float(input("Nhập vào số thực b: "))
# Tính
A = ( (math.sqrt(a)-math.sqrt(b) )/( pow(a,1/4)-pow(b,1/4) ) )-( (math.sqrt(a)+pow(a*b,1/4))/(pow(a,1/4)+pow(b,1/4) ) )
# In kết quả
print("Kết quả: ", round(A, 3))
