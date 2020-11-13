#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('./././')
import math
from mfunc.args import my_sqrt

# 调用求一元二次两个解函数方法
x, y = my_sqrt(100, 100, 60, math.pi / 6)
print(x, y)

r = my_sqrt(100, 100, 60, math.pi / 6)
print(r) 
print(r[0],r[1]) # 根据索引获取元祖中的元素