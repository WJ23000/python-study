#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

# 求绝对值自定义函数
def my_abs(value):
    if not isinstance(value,(int,float)): # 数据类型检查，对参数进行过滤
        raise TypeError('请传入数值类型数据')
    if value > 0:
        return value
    else:
        return -value # 负负得正
        
# 求一元二次方程两个解自定义函数并返回多个值
def my_sqrt(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny # 返回的是一个元祖

# 传入的参数添加默认值
def my_power(x, n=2): # 必选参数在前，默认参数在后
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 给传入的List设置默认值为None
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
        
# pass用来占位(暂时没想好做什么)
def nop(): 
    pass
