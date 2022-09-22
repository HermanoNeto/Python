from sys import exit

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


def insert_coins():
    print("Please Insert Coins.")
    inserted_quarters = int(input("How many quarters?: "))
    inserted_dimes = int(input("How many dimes?: "))
    inserted_nickles = int(input("How many nickles?: "))
    inserted_pennies = int(input("How many pennies?: "))
    value = inserted_quarters * 0.25 + inserted_dimes * 0.10 + inserted_nickles * 0.05 + inserted_pennies * 0.01
    return value


def costs(coffee):
    coffee_type = MENU[coffee]
    price = coffee_type["cost"]
    return price


def buy_coffee(order):
    coffee_price = costs(order)
    inserted_money = insert_coins()

    if inserted_money < coffee_price:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = inserted_money - coffee_price
        print(f"Here is ${change:.2f} in change.\nHere is your {order} ☕️. Enjoy!")
        resources["money"] = f"${coffee_price}"


def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        else:
            return True


def make_coffee(ingredients, order):
    resources["water"] -= ingredients["water"]
    resources["coffee"] -= ingredients["coffee"]
    if order == "latte" or "cappuccino":
        resources["milk"] -= ingredients["milk"]
    return


while True:

    order = input("What would you like? (Espresso/ Latte/ Cappuccino): ").strip().lower()
    if order == "report":
        for key in resources:
            print(f"{key}: {resources[key]}")

    elif order == "espresso":
        menu = MENU[order]
        if check_resources(menu["ingredients"]):
            buy_coffee(order)
            make_coffee(menu["ingredients"], order)

    elif order == "latte":
        menu = MENU[order]
        if check_resources(menu["ingredients"]):
            buy_coffee(order)
            make_coffee(menu["ingredients"], order)

    elif order == "cappuccino":
        menu = MENU[order]
        if check_resources(menu["ingredients"]):
            buy_coffee(order)
            make_coffee(menu["ingredients"], order)

    elif order == "off":
        break
