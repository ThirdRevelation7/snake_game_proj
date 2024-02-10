from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def snake_direction():
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


screen = Screen()
screen.setup(width=600, height=610)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
snake_direction()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.08)

    snake.move()

    #Detects collision with food and adds segment
    if snake.head.distance(food) < 15:
        food.refresh_location()
        snake.extend()
        scoreboard.increase_score()

    #Detects collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset_snake()

    #Detects collision with any segment in snake body
    for segment in snake.snake_segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()
