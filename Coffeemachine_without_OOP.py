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

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO:print report
# TODO:Check if resources are sufficient
# TODO:process the coins
# TODO:check for proper transactions
# TODO:Make the coffee

profit = 0


def sufficient(order):
    """this function checks whether there's enough resources left"""
    for items in order:
        # remember it's equal too here, so it's like a precaution
        if order[items] >= RESOURCES[items]:
            print(f" Sorry there is not enough {items}. ")
            return 0
        elif order[items] <= RESOURCES[items]:
            RESOURCES[items] -= order[items]
            return 1


def calculation(quarters_amt,dimes_amt,nickels_amt,pennies_amt ):
    """This just calculates the total amount of money they've given us"""
    given = quarters_amt * 0.25 + dimes_amt * 0.10 + nickels_amt * 0.05 + pennies_amt * 0.01
    return given


def drink(given, option_cost):
    """It compares the money given and the actual cost, and also adding to the 'wallet'"""
    if given >= option_cost:
        change = total - option_cost
        kash = round(change, 2)
        print(f"Here is ${kash} in change.")
        global profit
        profit += option_cost
        return True
    elif given <= option_cost:
        print("Sorry money is insufficient. Money refunded")
        return False


it_works = True

while it_works:

    option = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if option == 'report':
        print(f"Water:{RESOURCES["water"]}ml")
        print(f"Milk:{RESOURCES["milk"]}ml")
        print(f"Coffee:{RESOURCES["coffee"]}g")
        print(f"Money: ${profit}")
    elif option == 'off':
        it_works = False
    else:
        liquid = MENU[option]
        if sufficient(liquid["ingredients"]) == 1:
            print("Please insert coins.")
            quarters_amt = float(input("How many quarters? "))
            dimes_amt = float(input("How many dimes? "))
            nickels_amt = float(input("How many nickels? "))
            pennies_amt = float(input("How many pennies? "))
            total = calculation(quarters_amt, dimes_amt, nickels_amt, pennies_amt)
            extra_money = drink(total, liquid["cost"])
            print(f"Here is your amazing {option}☕.Enjoy!!")






