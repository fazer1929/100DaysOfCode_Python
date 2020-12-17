from turtle import Turtle

class Snake():
    def __init__(self):
        self.snake_segments = []
        self.createSnake()
        self.head= self.snake_segments[0]
    
    def createSnake(self):
        starting_pos = [(0,0),(-20,0),(-40,0),(-60,0)]
        for start_pos in starting_pos:
            self.add_segment(start_pos)
    
    def add_segment(self,start_pos):
        turtle  = Turtle()
        turtle.shape('square')
        turtle.color("white")
        turtle.penup()
        turtle.goto(start_pos)
        self.snake_segments.append(turtle)
        
    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for i in range(len(self.snake_segments)-1,0,-1):
            new_y = self.snake_segments[i-1].ycor()
            new_x = self.snake_segments[i-1].xcor()
            self.snake_segments[i].goto(new_x, new_y)
        self.snake_segments[0].forward(12)

    def turnUp(self):
        if self.snake_segments[0].heading() != 270:
            self.snake_segments[0].setheading(90)

    def turnLeft(self):
        if self.snake_segments[0].heading() != 0:
            self.snake_segments[0].setheading(180)

    def turnDown(self):
        if self.snake_segments[0].heading() != 90:
            self.snake_segments[0].setheading(270)

    def turnRight(self):
        if self.snake_segments[0].heading() != 180:
            self.snake_segments[0].setheading(0)
    
    def checkWrap(self,x,y):
        if self.head.xcor() > int(x/2) :
            self.head.goto(-x//2,self.head.ycor())
        elif self.head.xcor() < -int(x/2) :
            self.head.goto(int(x/2),self.head.ycor())
        elif self.head.ycor() > int(y/2) :
            self.head.goto(self.head.xcor(),-y//2)
        elif self.head.ycor() < -int(y/2) :
            self.head.goto(self.head.xcor(),int(y/2))
