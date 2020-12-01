from data import MENU,resources

choice = ""

def get_resources():
    print(f"Water : {resources['water']}")
    print(f"Milk : {resources['milk']}")
    print(f"Coffee : {resources['coffee']}")
    print(f"Money : {resources['money']}")


def resource_sufficient(choice):
    for i in MENU[choice]["ingredients"] : 
        if resources[i] <= MENU[choice]["ingredients"][i]:
            print(f"Can't Make Coffee. {i.capitalize()} insufficient.")
            return False
        else:
            resources[i]-=MENU[choice]["ingredients"][i]
    return True    

def makechoice(choice):
    if choice in ["espresso","latte","cappuccino"]:
        if resource_sufficient(choice): 
            money = take_money()
            if process_coins(choice,money):
               print(f"Here's Your {choice.capitalize()}. Enjoy!!")
    else:
            get_resources()        
    
def take_money():
    print("Please Insert Coins. ")
    quaters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickels = int(input("How many nickels? : "))
    pennies= int(input("How many pennies? : "))
    total = (pennies*0.01) + (nickels*.05) + (dimes*0.1) + (quaters * 0.5)
    return round(total,2)


def process_coins(choice,money):
    if MENU[choice]["cost"] <= money:
        resources["money"] += money
        print(f"${round(money - MENU[choice]['cost'],2) } returned.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def transaction_successfull():
    pass    

while choice != "off":
    choice = input("What would you like? (espresso[$1.5] / latte[$2.5] / cappuccino[$3.0]): ").lower()
    if choice in ['espresso','latte','cappuccino','report']:
        makechoice(choice)
    elif choice == "off":
        print("Bye Bye! Have A Nice Day.")
        break
    else:
        print("Wrong Choice Entered, PLease Try Again")
    print('\n\n')