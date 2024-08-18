# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

distance = float(input("Nhập điểm trung bình GPA từ bàn phím: "))

if distance < 3.5:
    print("Học lực Kém")
elif distance <= 3.5 and distance < 5.0:
    print("Học lực Yếu")
elif distance < 7.0 and distance < 8.0:
    print("Học lực Khá")
elif distance <= 8.0 and distane < 9.0:
    print("Học lực Giỏi")
elif distance <= 9.0 and distance <= 10:
    print("Học lực Xuất Sắc")