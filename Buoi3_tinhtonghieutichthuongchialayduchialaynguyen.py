# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 13:51:16 2024

@author: KIEUNHI
"""

# Nhập 2 số nguyên
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
# Tính tổng, hiệu, tích
tong = a + b
hieu = a - b
tich = a * b
# Tính thương
if b != 0:
    thuong = a / b
    # Làm tròn đến 2 chữ số sau dấu phẩy
    thuong_lam_tron_2 = round(thuong, 2) 
    # Làm tròn đến 3 chữ số sau dấu phẩy
    thuong_lam_tron_3 = round(thuong, 3) 
    chia_lay_du = a % b
    chia_lay_nguyen = a // b
else: 
    print("Không xác định")
# In ra kết quả
print("Tổng của a và b là: ", tong)
print("Hiệu của a và b là: ", hieu)
print("Tích của a và b là: ", tich)
print("Thương của a và b (làm tròn 2 chữ số) là: ", thuong_lam_tron_2)
print("Thương của a và b (làm tròn 3 chữ số) là: ", thuong_lam_tron_3)
print("Chia lấy dư của a và b là: ", chia_lay_du)
print("Chia lấy nguyên của a và b là: ", chia_lay_nguyen)
