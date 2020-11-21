import os

def screen_clear():
       # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   # print out some text
auction_people = []
more_people = 'y'
while more_people.lower()=='y' or more_people.lower() =="yes":
    name = input("Enter Your Name : \n")
    bid = float(input("Enter Your Bid : \n"))
    auction_people.append({
        "name":name,
        "bid":bid
    })
    more_people = input("Are There Any Other Bidders : \n")
    screen_clear()
large = 0
for i in range(0,len(auction_people)):
    if auction_people[large]["bid"]<auction_people[i]["bid"]:
        large=i
screen_clear()
name = auction_people[large]["name"]
bid = auction_people[large]["bid"]
print(f"The Winner is {name} with bid of {bid}")
        