import random
import hangman_art as art
import hangman_words as hw
word = hw.word_list[random.randint(0,len(hw.word_list))]
to_guess = []
isComplete = False

print(art.logo + "\n\n\n\n")

for i in word:
    to_guess.append("_")

lives = 6

while not isComplete:
    guess = input("Enter A Letter :  ").lower()
    for i in range(len(word)):
        if(word[i].lower() == guess):
            to_guess[i] = guess
    
    if guess not in word:
        lives-=1
    
    print(to_guess)
    print(art.stages[lives])

    if lives == 0 :
        print("|||  YOU Lose   |||")
        isComplete = True

    if "_" not in to_guess:
        print("|||  YOU WIN   |||")
        isComplete = True
