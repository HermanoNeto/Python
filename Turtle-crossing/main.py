import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(player.walk, "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_Car()
    car_manager.move_Cars()

    for car in car_manager.all_cars:
        if player.distance(car)<20:
            scoreboard.game_Over()
            game_is_on = False

    if player.ycor()>280:
        player.finish()
        car_manager.next_level()
        scoreboard.level()

        
screen.exitonclick()
