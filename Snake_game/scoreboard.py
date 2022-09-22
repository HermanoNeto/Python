from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score=0
        self.color("white")
        self.penup()
        self.ht()
        self.goto(x=0,y=270)
        self.update_Scoreboard()


    def update_Scoreboard(self):
        self.clear()
        with open("data.txt") as file:
            self.high_score=file.read()
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", align="center", font=('Arial', 15, 'normal'))



    def reset_Score(self):
        if self.current_score > int(self.high_score):
            with open("data.txt", "w") as file:
                file.write(str(self.current_score))
        self.current_score=0
        self.update_Scoreboard()


    def score(self):
        self.current_score+=1
        self.update_Scoreboard()
