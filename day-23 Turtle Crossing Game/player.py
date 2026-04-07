from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")

    def move(self):
        # STARTING_POSITION
        self.forward(MOVE_DISTANCE)
        if self.ycor() > FINISH_LINE_Y:
            print("You are at the finish line ")
            # STARTING_POSITION


