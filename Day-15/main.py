import coffee

machine = coffee.resources
menu = coffee.MENU

# print(menu['espresso']['ingredients']['water'])

def check_input(coffee_type):

    if coffee_type in menu or coffee_type == 'report':
        return True
    else:
        print(f"Sorry we are currently not providing {coffee_type}")
        return False


def check_resources(coffee_type=dict()):
    if machine['water'] < menu[coffee_type]['ingredients']['water']:
        print("Sorry there is not enough water.")
        return False
    elif machine['coffee'] < menu[coffee_type]['ingredients']['coffee']:
        print("Sorry there is not enought coffee.")
        return False
    elif machine['milk'] < menu[coffee_type]['ingredients']['milk']:
        print("Sorry there is not enought milk.")
        return False
    else:
        return True


def calculate_cost(quarters, dimes, nickels, pennies):
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * (0.01))
    return total


def valid_pay(paid, cost):
    if paid >= cost:
        change = paid - cost
        print(f"Here is ${change:.2f} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(machine, coffee_type):
    machine['coffee'] -= menu[coffee_type]['ingredients']['coffee']
    machine['water'] -=  menu[coffee_type]['ingredients']['water']
    machine['milk'] -= menu[coffee_type]['ingredients']['milk']
    return machine

while (True):
    coffee_type = input("What would you like> (espresso/latte/cappuccino): ").lower()

    valid = check_input(coffee_type=coffee_type)
    if valid == True:
        if coffee_type == 'report':
            for resource, amount in machine.items():
                if resource == 'cost':
                    print(f"{resource}: ${amount:.2f}")
                elif resource == 'coffee':
                    print(f"{resource}: {amount}g")
                else:
                    print(f"{resource}: {amount}ml")
        else:
            if check_resources(coffee_type) == True:
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennys?: "))
                paid_coins = calculate_cost(quarters=quarters, dimes=dimes, nickels=nickels, pennies=pennies)
                pay = valid_pay(paid=paid_coins, cost=menu[coffee_type]['cost'])
                if pay == True:
                    print(f"Here is your {coffee_type} Enjoy!")
                
                machine = make_coffee(machine, coffee_type)
