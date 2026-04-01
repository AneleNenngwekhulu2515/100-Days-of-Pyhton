from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


screen.listen()
screen.onkey(Paddle.go_up(), "Up")
screen.onkey(Paddle.go_down(), "Down")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()

