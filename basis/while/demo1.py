#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# while循环实现累加器(1+2+3+.....100)(不满足循环条件退出循环)
s = 0
i = 100
while i > 0:
    s = s + i
    i = i - 1
print(s)