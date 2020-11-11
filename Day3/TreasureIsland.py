

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("\n\n\n")
ans = input("You are in a middle of forest, you see two paths left and right where do you go\n").lower()
if(ans != "left" and ans != "l"):
    print("You Fell Into A Hole, You're Dead")
else:
    print("\n\n\n")
    ans = input("You See A Lake enter 'wait' to wait for a boat or 'swim' to swim across\n").lower()
    if(ans != "wait"):
        print("You Tried To Swim Across, But A Trout Attacks You, You're Dead!")
    else:
        print("\n\n\n")
        ans = input("You Wait For The Boat, The Boat Arrives In 10mins, You've Successfully Crossed The River.\nNow There's A Cave Which Has Three Mysterious Doors, Choose A Door.\n'yellow', 'red', or 'blue'\n").lower()
        if(ans == 'red'):
            print("The Door Opens\nA Blazing Storm of Fire Comes Your Way And You're Dead")
        elif(ans == "yellow"):
            print("Congratulations You Win!!\nProbabbly The First Win In Your Life.")
        elif(ans == "blue"):
            print("The Door Opens\nAnd You See Something Coming Towards You\nOOPS! Its A Beast And You're Dead\nSAD")
        else:
            print("You're Dead For Being Very VEry VERy VERY Careless")

    