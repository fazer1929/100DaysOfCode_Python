import os
import random
import data
import art

def screen_clear():
       # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   # print out some text

score = 0 
opt2 = random.choice(data.data)
while True:
    screen_clear()
    print(art.high_low)
    if score>0:
        print(f"You're Right!! Your Score {score}.\n\n")
    
    opt1 = opt2
    opt2 = random.choice(data.data)
    real_ans = opt1["follower_count"] - opt2["follower_count"]
   
    print(f'Compare A: {opt1["name"]}, a {opt1["description"]}, from {opt1["country"]}.')
    print(art.vs)
    print(f'Compare A: {opt2["name"]}, a {opt2["description"]}, from {opt2["country"]}.')
    ans = input("Who has more followers? Type 'A' or 'B':  ")
    if (real_ans>0 and ans.lower() == 'a') or (real_ans<0 and ans.lower() == 'b'):
        mans = True
    else:
        mans = False
    if mans:
        score+=1
    else:
        screen_clear()
        print(art.high_low)
        print(f"Wrong Ans! Final Score {score}.")  
        break  

