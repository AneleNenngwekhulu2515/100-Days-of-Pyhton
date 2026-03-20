from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money = MoneyMachine()
coffee_maker = CoffeeMaker()
coffee_machine = True

coffee_maker.report()
money.report()

while coffee_machine:
    drink = input("What would you like? (espresso/latte/cappucino): ").lower()
    if drink == "off":
        coffee_machine = False
    elif drink == "report":
        coffee_maker.report()
        money.report()

    found_drink = menu.find_drink(drink)

    if found_drink:
        print("Welcome to the Coffee Machine!")
        money.make_payment(found_drink.cost)
        if coffee_maker.is_resource_sufficient(found_drink):
            coffee_maker.make_coffee(found_drink)


    else:
        print("Sorry that item is not available.")






