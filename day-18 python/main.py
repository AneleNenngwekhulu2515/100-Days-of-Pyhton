from turtle import Turtle, Screen

tim = Turtle()
tim.color("chocolate")


# for _ in range(10):
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)

#many shape pattern

for _ in range(3):
    tim.forward(100)
    tim.right(120)

for _ in range(4):
    tim.color("deeppink")
    tim.forward(100)
    tim.right(90)

for _ in range(5):
    tim.color("green")
    tim.forward(100)
    tim.right(72)

for _ in range(6):
    tim.color("red")
    tim.forward(100)
    tim.right(60)

for _ in range(7):
    tim.color("blue")
    tim.forward(100)
    tim.right(51)

for _ in range(8):
    tim.color("yellow")
    tim.forward(100)
    tim.right(45)











screen = Screen()
screen.exitonclick()