from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.shape("circle")
        self.penup()

        self.x_move = 0.2
        self.y_move = 0.2



    def move(self):
        x_pos=self.xcor()+self.x_move
        y_pos=self.ycor()+self.y_move
        self.goto(x=x_pos,y=y_pos)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1


    def reset(self):
        self.goto(x=0,y=0)
        self.bounce_x()



