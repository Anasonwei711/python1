# -*- coding: utf-8 -*-
#set的特点
#1、et的内部结构和dict很像，唯一区别是不存储value
#2、set存储的元素和dict的key类似，必须是不变对象
#月份也可以用set表示，请设计一个set并判断用户输入的月份是否有效。
months = set(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
x1 = 'Feb'
x2 = 'Sun'

if x1 in months:
    print 'x1: ok'
else:
    print 'x1: error'

if x2 in months:
    print 'x2: ok'
else:
    print 'x2: error'