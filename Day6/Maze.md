### Today I Made A Basic Robot Script That Can Find The End Of Any Random Maze

#### Here is the Code

`
while not at_goal():
if not right_is_clear():
if front_is_clear():
move()
else:
turn_left()  
 else:
turn_left()
turn_left()
turn_left()
move()

`

#### And Here Is The Website Where It Can Be Run

[Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)
