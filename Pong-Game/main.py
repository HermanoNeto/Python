from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle(x_pos=350)
l_paddle=Paddle(x_pos=-350)

ball=Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.Up,"Up")
screen.onkeypress(r_paddle.Down,"Down")

screen.onkeypress(l_paddle.Up,"w")
screen.onkeypress(l_paddle.Down,"s")


game_on=True
while game_on:
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 45 and ball.xcor() > 340 or ball.distance(l_paddle) < 45 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()




screen.exitonclick()
