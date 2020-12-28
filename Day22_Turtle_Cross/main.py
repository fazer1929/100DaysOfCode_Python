from turtle import Screen
from player import Player
from cars import CarManager
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
scoreboard = Scoreboard()
car_manager = CarManager()
while is_game_on:
    screen.update()
    car_manager.move()
    if player.ycor() > 300:
        scoreboard.levelup()
        car_manager.levelup()
        player.reset()
        if scoreboard.level>5:
            is_game_on = False
            
    for car in car_manager.cars:
        if car.distance(player) < 30:
            scoreboard.lose()
            is_game_on = False
    time.sleep(0.04)

screen.exitonclick()