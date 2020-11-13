#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# while循环实现100以内的奇数和(不满足循环条件退出循环)
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)