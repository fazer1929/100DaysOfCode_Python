from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.score()

    def score(self):
        self.clear()

        self.goto(-100,210)
        self.write(self.lscore,align="center",font = ("Courier",48,"normal"))
        
        self.goto(100,210)
        self.write(self.rscore,align="center",font = ("Courier",48,"normal"))

    def lpoint(self):
        self.lscore += 1
        self.score()

    def rpoint(self):
        self.rscore += 1
        self.score()
        