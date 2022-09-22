from turtle import Turtle, position

STARTING_POSITIONS=((0,0),(-20,0),(-40,0))
MOVE_DISTANCE=20

UP=90
DOWN=270
LEFT=180
RIGHT=0



class Snake:

    def __init__(self):
        self.snake=[]
        self.create_Snake()
        self.head=self.snake[0]



    def create_Snake(self):
        """Create the segments of the snake"""
        for position in STARTING_POSITIONS:
            self.add_Segment(position)



    def add_Segment(self, position):
        snake_segment=Turtle(shape="square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.snake.append(snake_segment)



    def extend(self):
        self.add_Segment(self.snake[-1].position())


    def reset(self):
        for seg in self.snake:
            seg.goto(800,800)
        self.snake.clear()
        self.create_Snake()
        self.head=self.snake[0]


    def move(self):
        """Make the snake keep moving forward"""
        for seg_num in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(x=new_x,y=new_y)
        self.snake[0].forward(MOVE_DISTANCE)


    
    def up(self):
        """Set the heading of the snake to UP"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Set the heading of the snake to DOWN"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Set the heading of the snake to LEFT"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Set the heading of the snake to RIGHT"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
