# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 15:06:18 2024

@author: KIEUNHI
"""

a = int(input("Nhập giờ: "))
b = int(input("Nhập phút: "))
c = int(input("Nhập giây: "))
# Tính tổng đổi ra giây
tong_giay = a*3600 + b*60 + c
print("Tổng đổi ra giây: ", tong_giay)