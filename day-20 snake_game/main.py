from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_positions = [(0,0),(-20,0), (-40,0)]
segment = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segment.append(new_segment)

game_is_on = True

while game_is_on:
    for seg in segment:
        seg.forward(20)



# segment_1 = Turtle(shape="square")
# segment_1.color("white")
#
# segment_2 = Turtle(shape="square")
# segment_2.color("white")
#
# segment_3 = Turtle(shape="square")
# segment_3.color("white")
#
# segment_2.goto(x=-20, y=0)
# segment_3.goto(x=-40, y=0)



screen.exitonclick()