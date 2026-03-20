from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money = MoneyMachine()
coffee_maker = CoffeeMaker()
coffee_machine = True

while coffee_machine:
    drink = input("What would you like? (espresso/latte/cappucino): ").lower()
    if drink == "off":
        coffee_machine = False

    if drink == "report":
        print(coffee_maker.report())
        print(money.report())

    found_drink = menu.find_drink(drink)

    if found_drink:
        print("Welcome to the Coffee Machine!")
        money.process_coins()
        money.make_payment(found_drink.cost)


    else:
        print("Sorry that item is not available.")






