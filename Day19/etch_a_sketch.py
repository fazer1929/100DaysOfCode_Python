from turtle import Turtle,Screen

jim = Turtle()
screen = Screen()
screen.bgcolor('black')
jim.pencolor('white')
screen.listen()

def forward():
    jim.forward(10)
def backword():
    jim.back(10)
def left():
    jim.left(5)
def right():
    jim.right(5)

def clear():
    jim.clear()
    jim.penup()
    jim.home()
    jim.pendown()


screen.onkeypress(key='w',fun=forward)
screen.onkeypress(key='a',fun=left)
screen.onkeypress(key='s',fun=backword)
screen.onkeypress(key='d',fun=right)
screen.onkey(key='c',fun=clear)
screen.exitonclick()