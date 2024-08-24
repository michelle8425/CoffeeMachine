from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO:print report
# TODO:Check if resources are sufficient
# TODO:process the coins
# TODO:check for proper transactions
# TODO:Make the coffee

coffe_machine = CoffeeMaker()
money_maker = MoneyMachine()
menu = Menu()

making_coffee = True

while making_coffee:
    options = menu.get_items()
    choice = input(f"What would you like to drink?({options}):").lower()
    if choice == "off":
        making_coffee = False
    elif choice == "report":
        coffe_machine.report()
        money_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_machine.is_resource_sufficient(drink) == True:
            if money_maker.make_payment(drink.cost):
                coffe_machine.make_coffee(drink)



