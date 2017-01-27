# -*- coding: UTF-8 -*-  
import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on "+time.ctime())#显示程序运行时间
while(break_count < total_breaks):#开始进入循环
    time.sleep(3)#定时3秒
    webbrowser.open("http://www.bilibili.com/video/av8106278/")
    break_count = break_count + 1