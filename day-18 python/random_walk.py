from turtle import Turtle, Screen
import random

tim = Turtle()


colors = ["chocolate","seagreen", "black", "red", "green", "blue", "yellow", "purple"]

directions = [0,90,180,270]

for _ in range(200):
    tim.forward(30)
    tim.pensize(10)
    tim.color(random.choice(colors))
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()