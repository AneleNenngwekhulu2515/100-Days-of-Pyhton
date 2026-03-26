from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

t = Turtle(shape="square")
t.color("white")
s = Turtle(shape="square")
s.color("white")
p = Turtle(shape="square")
p.color("white")

t.goto(x=-1, y=0)
s.goto(x=-2, y=0)



screen.exitonclick()