from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.y_dir = 1
        self.x_dir=1
        self.speed = 8
        self.penup()
    
    def move(self):
        new_x  = self.xcor() + self.speed*self.x_dir
        new_y = self.ycor()+self.speed*self.y_dir
        self.goto(new_x,new_y )

    def bounce_y(self):
        self.y_dir = self.y_dir*-1
   
    def bounce_x(self):
        self.x_dir = self.x_dir*-1
        self.speed+=.4

    def reset(self):
        self.bounce_x()
        self.goto(0,0)
        self.speed=8
    