from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("chocolate")

for _ in range(10):
    tim.penup()
    tim.forward(10)
    tim.pendown()
    tim.forward(10)








screen = Screen()
screen.exitonclick()