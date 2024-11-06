MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def calc_coins():
    print("Please, insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def check_resources(drink_ingredients): # recebe um dicionário com as quantidades de cada ingrediente
    '''check if resources are sufficient'''
    for item in drink_ingredients:
        if resources[item] < drink_ingredients[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    if drink_cost > money_received:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        global profit
        profit += drink_cost
        if money_received > drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} in change")
    return True


def make_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


coffee_machine_on = True

while coffee_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        coffee_machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = calc_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])















