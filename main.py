from turtle import *
import random
import time
from SNAKE import Snake
from FOOD import Food
from SCORE import Score

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("MY SNAKE GAME")

snake =Snake()

screen.listen()
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")

food = Food()
score = Score()

while True:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food)<15:
            snake.extend()
            food.refresh()
            score.add_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290:
        score.update_scoreboard()
        score.game_over()
        break
    elif snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.update_scoreboard()
        score.game_over()
        break
    else:
        for segments in snake.segments[1:]:
            if segments.distance(snake.head) < 15:
                score.update_scoreboard()
                score.game_over()
                break






screen.exitonclick()