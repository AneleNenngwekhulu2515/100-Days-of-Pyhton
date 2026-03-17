from coffee_machine import MENU, resources

coffee_maker = True

def money(money_recieved, drink_cost):
    # penny = 0.01
    # nickel =0.05
    # dime = 0.10
    # quater = 0.25
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry not enough money. Money refunded")
        return False


while coffee_maker:

    drink = input("What would you like? (espresso/latte/cappucino): ").lower()
    if drink == "off":
        coffee_maker = False

    if drink == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: {resources['water']}ml")

    if drink == "espresso":
        for key, value in MENU["espresso"]["ingredients"].items():
            print(f"{key}: {value}")

            if resources[key] < value:
                print(f"Sorry there is not enough {key}")
            else:
                resources[key] -= value


    if drink == "cappuccino":
        for key, value in MENU["cappuccino"]["ingredients"].items():
            print(f"{key}: {value}")

            if resources[key] < value:
                print(f"Sorry there is not enough {key}")
            else:
                resources[key] -= value


    if drink == "latte":
        for key, value in MENU["latte"]["ingredients"].items():
            print(f"{key}: {value}")

            if resources[key] < value:
                print(f"Sorry there is not enough {key}")
            else:
                resources[key] -= value

    print(resources)



