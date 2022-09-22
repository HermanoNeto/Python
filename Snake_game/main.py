from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on=True
while game_on:
    screen.update()
    sleep(0.1)

    snake.move()


    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score()

    if snake.head.xcor()>295 or snake.head.xcor()<-300 or snake.head.ycor()>299 or snake.head.ycor()<-280:
        scoreboard.reset_Score()
        snake.reset()

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_Score()
            snake.reset()

screen.exitonclick()
