# Rectangle
# Fd 300 rt 90 fd 150 rt 90
# Fd 300 rt 90 fd 150 rt 90

import turtle
import time #introduce time module

for i in range(2):
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    i+=1
    time.sleep(2)

time.sleep(5)