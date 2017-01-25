# -*- coding: utf-8 -*-
#求1+2+4+8+16+......前20项和，利用while true和break语句实现
sum = 0
x = 1
n = 1
#---------------while True是无限循环语句！
while True:
    sum = sum + x
    x = x * 2
    n = n + 1
#---------------下行是表示累加器结束语句！
    if n > 20:
        break
print sum