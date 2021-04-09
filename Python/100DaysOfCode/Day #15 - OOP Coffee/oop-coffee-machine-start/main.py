from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coin_bot = MoneyMachine()
java_machina = CoffeeMaker()
get_bot = Menu()
system_on = True



while system_on:
    selection = get_bot.get_items()
    choice = input(f"Please make a selection {selection}: ")
    if choice == "off":
        system_on = False
    elif choice == "report":
        java_machina.report()
        coin_bot.report()
    else:
        drink = get_bot.find_drink(choice)
        if java_machina.is_resource_sufficient(drink):
            if coin_bot.make_payment(drink.cost):
                java_machina.make_coffee(drink)