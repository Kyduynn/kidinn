# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 18:29:15 2024

@author: Dell
"""

print("Kiểm tra tính hợp lệ của ngày tháng năm")
y = float(input("Nhập năm: "))
m = float(input("Nhập tháng: "))
if m<1 and m>12:
    print("Không hợp lệ")
    d = float(input("Nhập ngày:"))
if d<1 and d>31:
    print("Không hợp lệ")
    
if y%4 == 0 and y%100 != 0 or y%400 == 0:
    print("Nay là năm nhuận.")
    if m==2:
        print("Tháng này có 29 ngày")
        if d>29:
            print("Không hợp lệ")
else:
    print("Năm này không là năm nhuận.")
    if m==2:
        print("Tháng này có 28 ngày")
        if d>28:
            print("Không hợp lệ")
        elif m==1 or m==3 or m==7 or m==8 or m==10 or m==12:
            print("Tháng này có 31 ngày")
        elif m==4 or m==6 or m==9 or m==11:
            print("Tháng này có 30 ngày")
            if d>30:
                print("Không hợp lệ")