from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

CREATE_OR_NOT=[0, 1]


class CarManager:
    
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
    
    def create_Car(self):
        random_chance = random.randint(1,6)

        if random_chance==1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            random_y=random.randint(-250, 250)
            new_car.goto(300, random_y)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)


    def move_Cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    
    def next_level(self):
        for car in self.all_cars:
            car.ht()
        self.all_cars=[]
        self.car_speed+=MOVE_INCREMENT

