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

# cards_deck = [1,2,3,4,5,6,7,8,9,10,11,10,10,10]
#
# cards = []
#
# # computer cards
# computer_cards = []
# for i in range(2):
#     computer_cards.append(random.choice(cards_deck))
#
# print("Computer cards:", computer_cards[0])
#
# # player cards
# for n in range(2):
#     card = random.choice(cards_deck)
#     cards.append(card)
#
# print("Your cards:", cards)
#
# total = sum(cards)
# print("Your total:", total)
#
# computer_total = sum(computer_cards)
# print("Computer total:", computer_total)
#
# if total > 21:
#     print("You lost (over 21)")
# elif computer_total > 21 or total > computer_total:
#     print("You win!")
# elif total < computer_total:
#     print("Computer wins")
# else:
#     print("Draw")

def deal_card():
    cards= [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

user_cards = []
computer_cards = []
is_game_over = False


for _ in range(2):
    new_card = deal_card()
    user_cards.append(new_card)
    computer_cards.append(new_card)

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")


    if user_score>21 or user_score==0 or computer_score==0:
        is_game_over = True
    else:
        deal = input("Do you want to draw another card? 'y' or 'n': ").lower()
        if deal == "y":
            drawed_card = deal_card()
            user_cards.append(drawed_card)
            user_score = calculate_score(user_cards)
        elif deal == "n":
            is_game_over = True

while computer_score<17 and computer_score != 0:
    computer_drawed_card = deal_card()
    computer_cards.append(computer_drawed_card)
    computer_score = calculate_score(computer_cards)

    # print(f"Computer cards: {computer_cards[0]}")
    # print(user_cards)

def compare(user_score, computer_score):
    if user_score==computer_score:
        return "Its a Draw"
    if computer_score == 0:
        return "You loose"


















