"""haz una pelota rebotando"""

import turtle

t=turtle.Turtle()
t.shape("circle")
t.speed(0)
t.up()

x= -200
y= 100
vx= 3
vy= 0

while True:
    x += vx
    y += vy
    vy -= 0.50

    if y <  -150:
        y = -150
        vy = 10

    t.goto(x,y)

    if x > 200 or x < -200:
        vx*=-1