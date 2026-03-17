from coffee_machine import MENU, resources

coffee_maker = False

def money():
    penny = 0.01
    nickel =0.05
    dime = 0.10
    quater = 0.25


while not coffee_maker:
    drink = input("What would you like? (espresso/latte/cappucino): ").lower()

    if drink == "report":
        for key,value in resources.items():
            print(f"{key}: {value}")

    if drink == "espresso":
        for key, value in MENU["espresso"]["ingredients"].items():
            print(f"{key}: {value}")

            if resources[key] < value:
                print(f"Sorry there is not enough {key}")
            else:
                resources[key] -= value

    print(resources)



    # elif drink == "latte":
    #     print(MENU["latte"])
    # elif drink == "cappucino":
    #     print(MENU["cappucino"])

