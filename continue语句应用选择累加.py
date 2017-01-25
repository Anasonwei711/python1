# -*- coding: utf-8 -*-
#对已有的计算 0 - 100 的while循环进行改造，通过增加 continue 语句，使得只计算奇数的和
sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x % 2 == 0:#x除以2余数为0
        continue#不继续循环，开始下一个循环
    sum = sum + x
print sum