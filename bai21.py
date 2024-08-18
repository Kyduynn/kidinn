# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:45:56 2024

@author: Dell
"""

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
if a == 0 and b != 0:
    print("Phương trình có vô nghiệm")
elif a == 0 and b == 0:
    print("Phương trình có vô số nghiệm")
else:
    print("Nghiệm của phương trình là: ", -b/a)