from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.level = 1
        self.penup()
        self.show()

    def show(self):
        self.clear()
        self.goto(-300,260)
        self.write(f"Level : {self.level}",align="center",font = ("Courier",18,"normal"))
    
    def win(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER, YOU WIN!!",align="center",font = ("Courier",24,"normal"))
    
    def levelup(self):
        self.level += 1
        if self.level >5:
            self.win()
        else:
            self.show()