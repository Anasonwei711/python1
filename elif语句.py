score = 85
#记得按判断优先性质来规划从上到下的判断顺序，否则输出第一个结果正确，后续语句全部忽略
if score >= 90:
    print 'excellent'
elif score >= 80:
    print 'good'
elif score >= 60:
    print 'passed'
else:
    print 'failed'