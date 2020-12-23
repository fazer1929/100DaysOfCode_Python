from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
pad = Paddle((360,0))
pad2 = Paddle((-360,0))
ball = Ball()
screen.listen()
screen.onkeypress(pad.go_up,"Up")
screen.onkeypress(pad.go_down,"Down")
screen.onkeypress(pad2.go_up,"w")
screen.onkeypress(pad2.go_down,"s")

game_on=True
while game_on:
    ball.move()
    screen.update()
    time.sleep(0.05)
    if ball.ycor()<-300 or ball.ycor()>300:
        ball.bounce_y()

    if (ball.distance(pad) < 60 and ball.xcor()>335) or (ball.distance(pad2) < 60 and ball.xcor()<-335):
        ball.bounce_x()

    if ball.xcor() > 390 :
        ball.reset()
        scoreboard.lpoint()
    elif ball.xcor() <-390:
        ball.reset()
        scoreboard.rpoint()

screen.exitonclick()

