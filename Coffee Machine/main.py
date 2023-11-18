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

money = 0
machine_on = True


def check_resource(type_coffee):

    for items in MENU[type_coffee]["ingredients"]:
        if MENU[type_coffee]["ingredients"][items] > resources[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True


def insert_coin():
    paid = 0
    quarter = int(input("How many quarters ? : "))
    dimes = int(input("How many dimes ? :"))
    nickels = int(input("How many nickels ? : "))
    pennies = int(input("How many pennies ? : "))
    paid = quarter * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return round(paid, 2)


def make_coffe(coffee_type):
    for items in MENU[coffee_type]["ingredients"]:
        resources[items] -= MENU[coffee_type]["ingredients"][items]
    print(f"Here is your {coffee_type}. ☕ Enjoy!")


def payment(word,paid_by_user):
    to_pay = MENU[word]["cost"]
    if paid_by_user >= to_pay:
        global money
        money += to_pay
        make_coffe(word)
        if paid_by_user > to_pay:
            print(f"Here is the change ${round(paid_by_user- to_pay, 2)}")
    else:
        print("Sorry that's not enough money. Money refunded.")


while machine_on:
    coffee_choice = (input("What would you like ? (espresso[$1.5]/latte[$2.5]/cappuccino[$3.0]) :- ")).lower()
    if coffee_choice == "off":
        machine_on = False
    elif coffee_choice == "report":
        for ingredient in resources:
            print(f"{ingredient} : {resources[ingredient]} ml")
        print(f"Money: ${money}")
    else:
        if coffee_choice == "latte":
            if check_resource("latte"):
                paid_user = insert_coin()
                payment(coffee_choice,paid_user)
                
        elif coffee_choice == "espresso":
            if check_resource("espresso"):
                paid_user = insert_coin()
                payment(coffee_choice, paid_user)
                
        elif coffee_choice == "cappuccino":
            if check_resource("cappuccino"):
                paid_user = insert_coin()
                payment(coffee_choice, paid_user)
        else:
            print("Error Try Again")
print("Machine Off! ")