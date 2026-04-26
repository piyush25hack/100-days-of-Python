MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


# Ingredient Check function
def is_resources(order_ingredients):
    """Returns True if resources are sufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# Amount Inserted in the machine
def coins():
    """Returns the calculated coins inserted in the machine"""
    print("Please insert the coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


# Profit / Transaction
def transactions(money_received, drink_cost):
    """Returns True when payment is accepted or False if money is not sufficient"""
    global profit

    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# Make Coffee
def make_coffee(drink_name, order_ingredients):
    """Deduct ingredients and serve coffee"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink_name} ☕ Enjoy!")


is_on = True

while is_on:
    user = input("What would you like to have? (espresso/latte/cappuccino): ").lower()

    if user == "off":
        is_on = False

    elif user == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif user in MENU:
        drink = MENU[user]

        if is_resources(drink["ingredients"]):
            payment = coins()

            if transactions(payment, drink["cost"]):
                make_coffee(user, drink["ingredients"])

    else:
        print("Invalid choice. Please choose espresso, latte, or cappuccino.")