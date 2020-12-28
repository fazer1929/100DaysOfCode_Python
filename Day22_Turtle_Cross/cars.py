from turtle import Turtle
import random

colors = ["red","green","blue","purple","lightblue","green yellow",'salmon']

class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.createCar(6)
        
        
    def createCar(self,lev=6):
        for i in range(0,lev):
            car= Turtle()
            car.shape('square')
            car.shapesize(stretch_len=2.3,stretch_wid=1.4)
            car.color(random.choice(colors))
            car.penup()
            car.speed = (random.random()+1) *5
            car.y = random.randint(-270,270)
            car.x = random.randint(400,500)
            car.goto(380,car.y)
            self.move()
            self.cars.append(car)
    
    def levelup(self):
        self.createCar(3)
        for car in self.cars:
            car.goto(410,car.ycor())    

    
    def move(self):
        for car in self.cars:
            if car.xcor()<-450:
                car.goto(410,car.ycor())    
            else:
                car.goto(car.xcor() - car.speed,car.ycor())
