import art
import random
print(art.logo)
print("---------- TO Number Guessing Game ---------")
print("I'm Thinking A Number Between '1' & '100' :\n")
num = random.randint(0,100) + 1
diff = input("Choose A Difficulty, 'easy' or 'hard'\n")
if diff.lower() =='easy':
    tries = 10
else:
    tries = 5



while tries>0:
    print(f"You Have {tries} attempts to guess the number")
    guess = int(input("MAKE A GUESS : "))
    if guess < num:
        tries-=1
        print("Too Low")
    elif guess>num:
        tries-=1
        print("Too High")
    else:
        print("YOU GOT THE NUMBER!! YOU WIN!!")
        break
    print("Guess Again\n\n\n")