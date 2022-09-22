import turtle
import pandas as pd

t=turtle.Turtle()
screen=turtle.Screen()
screen.title("U.S - States Game")


image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pd.read_csv("50_states.csv")

correct_states=0

states_list=states["state"].to_list()

guesses=[]

game_on=True
while game_on:
    state_answer = screen.textinput(title=f"{correct_states}/50 States Correct", prompt="What's another state name?").title()

    if state_answer=="Exit":
        missing_states=[state for state in states_list if not state in guesses]
        df= pd.DataFrame(missing_states, columns=["States to Learn"])
        df.to_csv("states_to_learn.csv")
        break

    if state_answer in states_list:
        guesses.append(state_answer)
        t.penup()
        t.ht()
        xy_pos=states[states.state == state_answer]
        t.goto(x=int(xy_pos.x),y=int(xy_pos.y))
        t.write(state_answer, align="center", font=("Arial", 7, "normal"))
        correct_states+=1
    if correct_states == 50:
        game_on=False

