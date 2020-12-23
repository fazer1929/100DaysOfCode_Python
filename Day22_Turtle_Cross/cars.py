from turtle import Turtle
import random

colors = ["red","green","blue","purple","lightblue","green yellow",'salmon']

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=2.3,stretch_wid=1.4)
        self.color(random.choice(colors))
        self.penup()
        self.speed = random.randint(3,10)
        self.y = random.randint(-300,300)
        self.goto(380,self.y)
        self.move()

    def move(self):
        self.goto(self.xcor() - self.speed,self.ycor())
