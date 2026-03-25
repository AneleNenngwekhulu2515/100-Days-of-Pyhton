from turtle import *

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


tim.goto(x=-230, y=0)
tom.goto(x=-230, y=100)
sam.goto(x=-230, y=-100)
hank.goto(x=-230, y=-50)
rex.goto(x=-230, y=50)

screen.exitonclick()