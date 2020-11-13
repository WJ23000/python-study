#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 判断当前学习状况
score = input('请输入您的成绩：')
if score < 60:
    print('不及格')
elif score == 60: 
    print('及格')
elif score <= 75: 
    print('良')
elif score <= 90: 
    print('良好')
else:
    print('优秀')