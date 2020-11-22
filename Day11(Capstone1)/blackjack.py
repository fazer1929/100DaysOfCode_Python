import random
import art
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def count_sum(cards):
    sum=0
    for i in cards:
        sum+=i
    return sum

def screen_clear():
       # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
print(art.logo + "\n\n")
play = input("Do You Wanna Play A Game Of Blackjack 'y' or 'n' : ")
while play=='y':
    # FIRST CARD DRAW
    cpu_card =[]
    cpu_card.append(random.choice(cards))
    cpu_card.append(random.choice(cards))
    p_card=[]
    p_card.append(random.choice(cards))
    p_card.append(random.choice(cards))
    sum = count_sum(p_card)
    print(f"\tYour Cards Are {p_card}.  Current Score : {sum}")
    print(f"\tDealer's First Card Is {cpu_card[0]}")
    p_sum = count_sum(p_card)
    
    #IF PLAYER HAS NOT LOST ASK FOR CHOICE
    while p_sum<21:
        draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
        #AGREES TO DRAW
        if draw_card=='y':
            card = random.choice(cards)
            # DRAWS AN ACE
            if card == 11:
                #DECIDING TO USE '1' OR '11'
                if p_sum + 11 >21:
                    p_card.append(1)
                else:
                    p_card.append(card)
            
            p_card.append(random.choice(cards))
            p_sum = count_sum(p_card)
            #BUST BY PLAYER
            if p_sum>21:
                print(f"\tYour Final Hand is {p_card}.  Your Score : {p_sum}")        
                print("\tBUST. YOU LOSE!!")
                break
            print(f"\tYour Cards Are {p_card}.  Current Score : {sum}")
            
        #IF PLAYER CHOOSES TO END THE GAME
        else:
            #Show Your Final Hand
            p_sum = count_sum(p_card)
            print(f"\tYour Final Hand is {p_card}.  Your Score : {p_sum}")        
            #Show CPU'S Final Hand IF Less THan 17 draw an other
            c_sum = count_sum(cpu_card)
            #IF SUM IS LESS THAN 17 CPU DRAWS ANOTHER CARD
            while c_sum < 17:
                cpu_card.append(random.choice(cards))
                c_sum = count_sum(cpu_card)
            print(f"\tDealer's Final Hand is {cpu_card}. Dealer's Score : {c_sum}")
            if c_sum > 21:
                print("\tDealer Went Over. YOU WIN!!!!!")
                break
            else:
                if p_sum>c_sum:
                    print("\tYOU WIN!!!!!")
                    break
                elif p_sum==c_sum:
                    print("\tIT'S A DRAW")
                    break
                else:
                    print("\tBUMMER.YOU LOSE!!!!!")
                    break
    play = input("Do You Wanna Play A Game Of Blackjack 'y' or 'n' : ")
    if play =='y':
        screen_clear()
        print(art.logo + "\n\n")
