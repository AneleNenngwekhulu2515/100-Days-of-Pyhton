#blackjack game
import random

print("""
██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
""")

cards_deck = [1,2,3,4,5,6,7,8,9,10,11,10,10,10]

cards = []

# computer cards
computer_cards = []
for i in range(2):
    computer_cards.append(random.choice(cards_deck))

print("Computer cards:", computer_cards[0])

# player cards
for n in range(2):
    card = random.choice(cards_deck)
    cards.append(card)

print("Your cards:", cards)

total = sum(cards)
print("Your total:", total)

computer_total = sum(computer_cards)
print("Computer total:", computer_total)

if total > 21:
    print("You lost (over 21)")
elif computer_total > 21 or total > computer_total:
    print("You win!")
elif total < computer_total:
    print("Computer wins")
else:
    print("Draw")



