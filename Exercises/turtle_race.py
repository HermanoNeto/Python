from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "green", "blue", "purple", "orange"]
y_positions = [-100, -50, 0, 50, 100]

all_turtles = []

for turtle_n in range(0,5):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle_n])
    turtle.goto(x=-230,y=y_positions[turtle_n])

    all_turtles.append(turtle)

racing=True
while racing == True:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            racing=False
            winning_color=turtle.pencolor()
            print(f"The {winning_color} turtle won!")
            break

        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
