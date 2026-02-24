#python pizza

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25

add_pepperoni_on_small_pizza = 2
add_pepperoni_on_medium_or_large_pizza = 3
add_extra_cheese = 1

bill = 0

if size == "S":
    bill+=small_pizza
    if pepperoni == "Y":
        bill+=add_pepperoni_on_small_pizza
    if extra_cheese == "Y":
        bill+=add_extra_cheese
elif size == "M":
    bill += medium_pizza
    if pepperoni == "Y":
        bill += add_pepperoni_on_medium_or_large_pizza
    if extra_cheese == "Y":
        bill += add_extra_cheese
elif size == "L":
    bill += large_pizza
    if pepperoni == "Y":
        bill += add_pepperoni_on_medium_or_large_pizza
    if extra_cheese == "Y":
        bill += add_extra_cheese

print(f"Your pizza is ${bill}.")

