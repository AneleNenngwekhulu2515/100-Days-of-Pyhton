from coffee_machine import MENU, resources

coffee_maker = True
profit = 0

def process_coins():
    print("Please insert coins. ")
    total = 0
    total += int(input("How many quaters? "))* 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def money(money_recieved, drink_cost):

    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry not enough money. Money refunded")
        return False

print("hi  ")
while coffee_maker:

    drink = input("What would you like? (espresso/latte/cappucino): ").lower()
    if drink == "off":
        coffee_maker = False

    if drink == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")

    elif drink in MENU:
        enough_resources = True

        for key, value in MENU[drink]["ingredients"].items():
            print(f"{key}: {value}")

            if resources[key] < value:
                print(f"Sorry there is not enough {key}")
                enough_resources = False

        if enough_resources:
            payment = process_coins()
            if money(payment, MENU[drink]["cost"]):
                for key, value in MENU[drink]["ingredients"].items():
                    resources[key] -= value
                print(f"Here is your {drink} ☕")

    print(resources)

    # if drink == "espresso":
    #     for key, value in MENU["espresso"]["ingredients"].items():
    #         print(f"{key}: {value}")
    #
    #         if resources[key] < value:
    #             print(f"Sorry there is not enough {key}")
    #         else:
    #             resources[key] -= value
    #
    #
    # if drink == "cappuccino":
    #     for key, value in MENU["cappuccino"]["ingredients"].items():
    #         print(f"{key}: {value}")
    #
    #         if resources[key] < value:
    #             print(f"Sorry there is not enough {key}")
    #         else:
    #             resources[key] -= value
    #
    #
    # if drink == "latte":
    #     for key, value in MENU["latte"]["ingredients"].items():
    #         print(f"{key}: {value}")
    #
    #         if resources[key] < value:
    #             print(f"Sorry there is not enough {key}")
    #         else:
    #             resources[key] -= value
    #
    # print(resources)



