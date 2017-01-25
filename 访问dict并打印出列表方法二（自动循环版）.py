# -*- coding: utf-8 -*-
#访问dict-----方法二
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for (key, value) in d.items():#利用for循环语句
    print("%s: %s" % (key, value))