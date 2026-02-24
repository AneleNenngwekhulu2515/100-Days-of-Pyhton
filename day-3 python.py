#python pizza

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
#
# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25
#
# add_pepperoni_on_small_pizza = 2
# add_pepperoni_on_medium_or_large_pizza = 3
# add_extra_cheese = 1
#
# bill = 0
#
# if size == "S":
#     bill+=small_pizza
#     if pepperoni == "Y":
#         bill+=add_pepperoni_on_small_pizza
#     if extra_cheese == "Y":
#         bill+=add_extra_cheese
# elif size == "M":
#     bill += medium_pizza
#     if pepperoni == "Y":
#         bill += add_pepperoni_on_medium_or_large_pizza
#     if extra_cheese == "Y":
#         bill += add_extra_cheese
# elif size == "L":
#     bill += large_pizza
#     if pepperoni == "Y":
#         bill += add_pepperoni_on_medium_or_large_pizza
#     if extra_cheese == "Y":
#         bill += add_extra_cheese
#
# print(f"Your pizza is ${bill}.")


#Treasure chest

print(r"""
      _.--.
    _.-'_:-'||
  _.-'_.-::::'||
.-'_.-::::::'  ||
.'`-.-:::::::'     ||
/.'`;|:::::::'      ||_
||   ||::::::'     _.;._'-._
||   ||:::::'  _.-!oo @.!-._'-.
\'.  ||:::::.-!()oo @!()@.-'_.|
 '.'-;|:.-'.&$@.& ()$%-'o.'\U||
   `>'-.!@%()@'@_%-'_.-o _.|'||
    ||-._'-.@.-'_.-' _.-o  |'||
    ||=[ '-._.-\U/.-'    o |'||
    || '-.]=|| |'|      o  |'||
    ||      || |'|        _| ';
    ||      || |'|    _.-'_.-'
    |'-._    || |'|_.-'_.-'
     '-._'-.  || |' `_.-'
        '-._'-._|| |_.-'
           '-._'|| |'
              '-._|| 
""")

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure!\n")
print("You are at a cross road. Where do you want to go?\n")

direction = input("Type ⬅️'left' or 'right'➡️. \n")
if direction == "right":
    print("Game Over💀" )
else:
    print("You've come to a lake. There is an island in the middle of the lake")
    action = input("Type ⏳'wait' to wait for boat. Type 🏊'swim' to swim across.\n ")
    if action == "swim":
        print("Game Over💀")
    else:
        print("You arrived at the island unharmed. There is a house with 3 doors.")
        color = input("One 🔴red, one 🟡yellow and one 🔵blue. Which colour do you choose?\n")
        if color == "red" or color =="blue":
            print("Game Over💀")
        if color =="yellow":
            print("You have found the hidden treasure, YOU WIN🔥🏆")




