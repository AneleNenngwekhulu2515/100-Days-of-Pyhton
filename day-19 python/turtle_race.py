from turtle import *
import random

tim = Turtle(shape="turtle")
tim.penup()
tim.color("purple")

tom = Turtle(shape="turtle")
tom.penup()
tom.color("red")

sam =Turtle(shape="turtle")
sam.penup()
sam.color("green")

hank = Turtle(shape="turtle")
hank.color("blue")
hank.penup()

rex = Turtle(shape="turtle")
rex.color("pink")
rex.penup()

screen = Screen()


screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle do you think will win the race? Enter a color:  ")
y_positions = [0, 100, -100, 50, -50, 20]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=y_positions[turtle_index])


# tim.goto(x=-230, y=0)
# tom.goto(x=-230, y=100)
# sam.goto(x=-230, y=-100)
# hank.goto(x=-230, y=-50)
# rex.goto(x=-230, y=50)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)


screen.exitonclick()