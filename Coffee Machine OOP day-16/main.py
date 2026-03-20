from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = True

while coffee_machine:
    drink = input("What would you like? (espresso/latte/cappucino): ").lower()
    if drink == "off":
        coffee_machine = False
    if drink == "report":
        coffee_maker = CoffeeMaker()
        coffee_maker.report()
        print(coffee_maker)
    if drink == menu.find_drink(drink):
        print("Welcome to the Coffee Machine!")






