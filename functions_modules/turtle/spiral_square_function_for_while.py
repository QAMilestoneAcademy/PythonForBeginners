# Python program to draw
# Spiral Square Outside In and Inside Out
# using Turtle Programming
import turtle
import time

s = turtle.Screen()
s.bgcolor("light green")
s.title("Spiral Square")
t = turtle.Turtle()
t.pen(pencolor="blue", fillcolor="yellow", pensize=10, speed=9)
# t.begin_fill()
# size=100
# while size<=300:
#     for i in range(0,10):
#         t.fd(size)
#         t.rt(90)
#         size=size+25
# t.end_fill()
# time.sleep(1)
#
def sqrfunc(size):
    for i in range(4):
        t.fd(size)
        t.left(90)
        size = size -5
sqrfunc(146)
t.pen(pencolor="green", fillcolor="red", pensize=5, speed=9)
sqrfunc(126)
t.pen(pencolor="red", fillcolor="purple", pensize=5, speed=9)
sqrfunc(106)
time.sleep(10)
