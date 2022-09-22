from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.current_level=-1
        super().__init__()
        self.level()
        


    def game_Over(self):
        self.goto(x=0,y=0)
        self.clear()
        self.write(f"GAME OVER\nScore: {self.current_level}", align="center", font=FONT)



    def level(self):
        self.current_level+=1
        self.clear()
        self.penup()
        self.ht()
        self.goto(x=-220,y=260)
        self.write(f"Level: {self.current_level}", align="center", font=FONT)
