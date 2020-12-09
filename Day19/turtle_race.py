from turtle import Turtle,Screen
import random
import datetime
print(datetime.datetime.now())
screen = Screen()
# jim = Turtle()
screen.setup(width=1280,height=720)
turtles=[]
colors = ['red','orange','yellow','green','blue','indigo','violet']
user_input = screen.textinput(title="Make Your Bet", prompt="Which Color Turtle Would Win").lower()

for i in range(7):
    turtle = Turtle()
    turtle.shape('turtle')
    yt=  -300 + 100*i
    turtle.penup()
    turtle.color(colors[i])
    xt=-(screen.window_width()/2)+20
    turtle.goto(x=xt,y=yt)
    turtles.append(turtle)

if user_input:
    race_on=True
    
wincolor = "" 
while race_on:
    for turtle in turtles:
        if turtle.xcor() > screen.window_width()/2 -20:
            race_on=False
            wincolor = turtle.pencolor()
            break
        rand_distance = random.randint(4,25)
        turtle.forward(rand_distance)

if(wincolor == user_input):
    print(f"You've Won!!!. {wincolor.capitalize()} has won the race")
else:
    print(f"You've Lost!!!. {wincolor.capitalize()} has won the race")

screen.exitonclick()