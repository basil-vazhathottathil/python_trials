'''
Design and implement a Python program using the Turtle graphics module to create a simple house with the following requirements:
House Structure: The house should have a square base, a triangular roof, and a rectangular door.
Use of Colors:
    The house body (walls) should be brown (RGB: (150, 75, 0)).
    The roof should be red (RGB: (200, 0, 0)).
    The door should be dark brown (RGB: (100, 50, 0)).
Use of Turtle Functions:
    Move the turtle to different positions to draw the house.
    Use begin_fill() and end_fill() to fill each shape with color.
Use RGB color mode to define custom colors.

'''

import turtle

t=turtle.Turtle()
turtle.colormode(255)

def base(t):
    t.penup()
    t.goto(-100,-100)
    t.pendown()
    t.color(150, 75, 0)
    t.begin_fill()
    for _ in range(4):
        t.forward(200)
        t.right(90)
    t.end_fill()

def triangle(t):
    t.left(60)
    t.color(200, 0, 0)
    t.begin_fill()
    for _ in range(3):
        t.forward(200)
        t.right(120)
    t.end_fill()

def door(t):
    t.right(60)
    t.penup()
    t.goto(-30,-200)
    t.pendown()

    t.color(100, 50, 0)
    t.begin_fill()
    t.forward(60)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(100)
    t.end_fill()

def main(t):
    base(t)
    triangle(t)
    door(t)


main(t)
turtle.done()