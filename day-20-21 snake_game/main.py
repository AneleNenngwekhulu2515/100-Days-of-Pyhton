from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #collision with food
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        print("you have eaten a fruit")
        scoreboard.increase_score()

    if snake.head.xcor()> 290 or snake.head.xcor()< -290 or snake.head.ycor()> 290 or snake.head.ycor()< -290:
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    #if head collides with tail , game over

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()






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