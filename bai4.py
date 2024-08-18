# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 18:12:14 2024

@author: Dell
"""

import math

print("Tính tiền taxi theo số km quãng đường đi được")
d = float(input("Nhập quãng đường đã đi:"))

if d==1:
    m = 20
    print("Tiền taxi của bạn là: ",m)
elif d>1 and d<=3:
    m = 13*d
    print("Tiền taxi của bạn là: ",m)
elif d>=4 and d<=8:
    m = 13*3 + (d-3)*12
    print("Tiền taxi của bạn là: ",m) 
else:
        m = 39 + 60 + (d-8)*10
        n = m*0.92
        print("Tiền taxi của bạn sau khi giảm: ",n)