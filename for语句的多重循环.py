# -*- coding: utf-8 -*-
#100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。
for x in range(1,10):#not [range(1,10)]
    for y in range(0,10):
        if x < y:
            print x * 10 + y