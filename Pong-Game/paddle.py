from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self,x_pos):
        super().__init__()
        self.color("White")
        self.shape("square")
        self.penup() 
        self.goto(x=x_pos,y=0)
        self.setheading(90)
        self.shapesize(stretch_len=5)



    
    def Up(self):
        self.forward(20)

    def Down(self):
        self.backward(20)

        
        