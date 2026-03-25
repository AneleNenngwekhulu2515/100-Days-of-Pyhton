from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(100)

def move_backwards():
    tim.backward(100)

def counter_clockwise():
    tim.circle()



screen.listen()
screen.onkey(key="w", fun= move_forwards)
screen.onkey(key="s", fun= move_backwards)
screen.onkey(key="a", fun= counter_clockwise)
screen.exitonclick()