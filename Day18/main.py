from turtle import Turtle,Screen
import random
import colorgram

colors_from_image = colorgram.extract('spot.jpg',30)
colors=[]
for color in  colors_from_image:
    colors.append((color.rgb.r,color.rgb.b,color.rgb.g))

jim = Turtle()
jim.speed(0)
screen = Screen()
screen.title("DAY18")
screen.colormode(255)
jim.hideturtle()
jim.penup()
jim.goto([-200,-200])
for i in range(10):
    for j in range(10):
        jim.color(random.choice(colors))
        jim.pendown()
        jim.dot(15)
        jim.penup()
        jim.setx(jim.xcor()+50)
    jim.setx(jim.xcor() -500)
    jim.sety(jim.ycor()+50)
screen.exitonclick()