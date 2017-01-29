# -*- coding: utf-8 -*-
import turtle

def draw_picture():
#调整画布属性
    window = turtle.Screen()
    window.bgcolor("red")
#写出要画的三个图形    
    draw_square()#这里draw只是符号函数代表下列过程，draw实际动作是在turtle库里定义的。因此不论draw是dddd还是1111都能画出图
    draw_circle()
    draw_triangle()
    
    window.exitonclick()
    
def draw_square():
#调整方块属性
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    
#方块四边循环
    time = 1
    while time < 5:
        brad.forward(100)
        brad.right(90)
        time = time + 1
    
def draw_circle():
#调整圆的属性
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
#调整三角熟悉
    fido = turtle.Turtle()
    fido.shape("arrow")
    fido.color("brown")

#三角三边循环  
    time = 0
    while(time < 3):
        fido.forward(60)
        fido.left(120)
        time = time + 1
    
draw_picture()