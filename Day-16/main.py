from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time


my_menu = Menu()
coffee = CoffeeMaker()
bill = MoneyMachine()

while True:
    my_order = input(f"What would you like? ({my_menu.get_items()}): " ).lower()
    if my_order == 'report':
        coffee.report()
    elif my_order == "quit":
        print("Closing: ", end="")
        for i in range(3):
            print(".", end="")
            time.sleep(1)
        print()
        break
    else:
        item_available = my_menu.find_drink(my_order)
        if item_available is None:
            continue
    if coffee.is_resource_sufficient(item_available):
        if bill.make_payment(item_available.cost):
            coffee.make_coffee(item_available)
        else:
            continue