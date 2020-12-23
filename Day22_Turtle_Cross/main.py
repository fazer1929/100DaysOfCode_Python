from turtle import Screen
from player import Player
from cars import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=640)
screen.bgcolor("black")
screen.tracer(0)
is_game_on = True
screen.title('Turtle Crossing')
screen.listen()
player = Player()
screen.onkeypress(player.move,"Up")
cars=[]
scoreboard = Scoreboard()

while is_game_on:
    screen.update()
    if player.ycor() > 300:
        scoreboard.levelup()
        player.reset()
    time.sleep(0.04)

screen.exitonclick()