import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (___)
---.__(__)
'''

choices = [rock,paper,scissors]

ans = int(input("Welcome To Rock, Paper And Scissors\nPress '0' for  Rock, '1' for Paper, '2' for Scissor\n"))

cpu = random.randint(0,2)

print("You Chose\n" + choices[ans])
print("\n\n\nCPU Chose\n" + choices[cpu])

if(ans == cpu):
  print("It's A Draw")
elif(ans==0):
  if(cpu==1):
    print("CPU Wins!!!")
  else:
    print("You Win!!!")
elif(ans==1):
  if(cpu==0):
    print("You Win!!!")
  else:
    print("CPU Wins!!!")
else:
  if(cpu==0):
    print("CPU Wins!!!")
  else:
    print("You Win!!!")