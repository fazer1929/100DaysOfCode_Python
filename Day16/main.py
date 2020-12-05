from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
menu = Menu()
coffeMaker = CoffeeMaker()
moneyMachine =  MoneyMachine()

while machine_on:
    options = menu.get_items()
    choice = input(f"Enter Your Drink Choice : {options} : ").lower()
    if choice in options:
        item = menu.find_drink(choice)
        if coffeMaker.is_resource_sufficient(item):
            if moneyMachine.make_payment(item.cost):
                coffeMaker.make_coffee(item)
        else:
            print("Ingredients Insufficient. Try another drink")
    else:
        if choice=='report':
            coffeMaker.report()    
            moneyMachine.report()
        if choice == 'off':
            machine_on=False
    print("\n\n")