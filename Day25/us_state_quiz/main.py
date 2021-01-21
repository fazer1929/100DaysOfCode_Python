import pandas
import turtle
coors = pandas.read_csv('./50_states.csv')
screen = turtle.Screen()
screen.title("U.S. State Game")
image = 'blank_states_img.gif'
screen.addshape(image)
screen.bgpic(image)
states_guessed = [] 
# turtle.shape(image)
turtle.penup()
turtle.hideturtle()

while(len(states_guessed)<50):
    ans = screen.textinput(title=f"Guess The State ({len(states_guessed)}/50)",prompt="What's The Other State").capitalize()
    x = coors[coors["state"]== ans]['x']
    y = coors[coors["state"]== ans]['y']
    if ans == "Exit":
        break
    try:
        if ans not in states_guessed:
            turtle.goto(int(x),int(y))
            turtle.write(ans,align='center')
            states_guessed.append(ans)

    except:
        continue

missing_states = []
for x in coors.state:
    if x not in states_guessed:
        missing_states.append(x)
df = pandas.DataFrame(missing_states)
df.to_csv("missing_states.csv")
print(missing_states)
screen.bgcolor('black')

turtle.goto(100,100)
turtle.write("YOU WON",align='center')
screen.exitonclick()