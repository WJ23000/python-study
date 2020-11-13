#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('./././')
from mfunc.demo6args import my_power,add_end

# 测试传入多个参数
p1 = my_power(2)
p2 = my_power(2,4)
p3 = my_power(2,n=5)
print(p1, p2, p3)


# 测试默认值
s1 = add_end([1, 2, 3])
print(s1)