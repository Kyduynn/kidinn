# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:58:15 2024

@author: Dell
"""

print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm!")
        else:
            print("Phương trình vô nghiệm!")
    else:
        if c == 0:
            print("Phương trình có một nghiệm x = 0")
        else:
            x = -c / b
            print("Phương trình có nghiệm kép x1=x2 = ", x)

else:
    delta = b **2 - 4 *a *c
    if delta < 0:
        print("Phương trình vô nghiệm! ")
    elif delta == 0:
        x= -b / (2 * a)
        print("Phuong trình có 1 nghiệm x =",x)
    else:
        print("Phương trình có 2 nghiệm phân biệt!")
        x1= (-b + math.sqrt(delta)) / (2 * a)
        x2= (-b -math.sqrt(delta)) / (2 * a)
        print("x1 = ", x1)
        print("x2 = ", x2)