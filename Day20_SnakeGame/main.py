from turtle import Turtle,Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

player = Snake() 
food = Food()
score_board = ScoreBoard()

screen.onkey(player.turnUp,"Up")
screen.onkey(player.turnDown,"Down")
screen.onkey(player.turnLeft,"Left")
screen.onkey(player.turnRight,"Right")

is_game_on = True
while is_game_on:
    time.sleep(.04)
    screen.update()
    player.move()

    #collision Detection
    if player.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        player.extend()

    #Collision with Tail
    for segment in player.snake_segments[1:]:
        if player.head.distance(segment) < 10:
            is_game_on= False
            score_board.game_over()
    #Wall Wrap
    # print(screen.window_height())
    player.checkWrap(screen.window_width(),screen.window_height())
screen.exitonclick()