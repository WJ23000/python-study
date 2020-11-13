#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用in判断key是否存在(如果key不存在，执行打印语句会报错)
list = {'大黑':25, '二黑':27, '三黑': 28}
pd = '大黑' in list
if pd:
    list['大黑'] = 18
    print(list['大黑'],list['二黑'])
else:
    print('当前属性不存在')