from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.color("white")
        self.penup()
        self.goto(0,-290)
        
    def move(self):
        self.goto(self.xcor(),self.ycor()+5)
        
    def reset(self):
        self.goto(0,-290)
