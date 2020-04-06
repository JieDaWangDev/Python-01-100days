#!/usr/bin/env python3
# -*- coding: utf-8-*-
# ******************************
# @File    : flag.py
# @Author  : Lenovo
# @Time    : 2020/4/6 14:49
# @SW      : PyCharm
# ******************************
import turtle

'''
绘制背景
'''


def draw_rect(x, y, width, height):
    turtle.goto(x, y)
    turtle.pencolor('red')
    turtle.fillcolor('red')
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()


def draw_star(x, y, radius):
    turtle.setpos(x, y)
    pos1 = turtle.pos()
    turtle.circle(-radius, 72)
    pos2 = turtle.pos()
    turtle.circle(-radius, 72)
    pos3 = turtle.pos()
    turtle.circle(-radius, 72)
    pos4 = turtle.pos()
    turtle.circle(-radius, 72)
    pos5 = turtle.pos()
    turtle.color('yellow', 'yellow')
    turtle.begin_fill()
    turtle.goto(pos3)
    turtle.goto(pos1)
    turtle.goto(pos4)
    turtle.goto(pos2)
    turtle.goto(pos5)
    turtle.end_fill()


if __name__ == '__main__':
    turtle.speed(5)
    turtle.penup()
    start_x, start_y = -320, 260
    flag_w, flag_h = 660, 440
    draw_rect(start_x, start_y, flag_w, flag_h)
    pice = 22
    center_x, center_y = start_x + 5 * pice, start_y - 5 * pice
    turtle.goto(center_x, center_y)
    turtle.left(90)
    turtle.forward(3 * pice)
    turtle.right(90)
    draw_star(center_x, center_y, pice * 3)
    print(turtle.towards(center_x, center_y) - turtle.heading())
    # draw the small star
    turtle.goto(start_x + 10 * pice, start_y - pice * 2)
    turtle.left(turtle.towards(center_x, center_y) - turtle.heading())
    turtle.forward(pice)
    turtle.right(90)
    draw_star(turtle.xcor(), turtle.ycor(), pice)
    # draw the second star
    turtle.goto(start_x + pice * 12, start_y - pice * 4)
    turtle.left(turtle.towards(center_x, center_y) - turtle.heading())
    turtle.forward(pice)
    turtle.right(90)
    draw_star(turtle.xcor(), turtle.ycor(), pice)
    # draw the third
    turtle.goto(start_x + pice * 12, start_y - 7 * pice)
    turtle.left(turtle.towards(center_x, center_y) - turtle.heading())
    turtle.forward(pice)
    turtle.right(90)
    draw_star(turtle.xcor(), turtle.ycor(), pice)
    # draw the final
    turtle.goto(start_x + pice * 10, start_y  - 9 * pice)
    turtle.left(turtle.towards(center_x, center_y) - turtle.heading())
    turtle.forward(pice)
    turtle.right(90)
    draw_star(turtle.xcor(), turtle.ycor(), pice)
    turtle.ht()
    # 显示绘画窗口
    turtle.mainloop()
