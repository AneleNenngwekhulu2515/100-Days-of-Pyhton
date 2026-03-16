import game_data
import random

print(r""" +-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+
 |H|i|g|h|e|r| |o|r| |L|o|w|e|r|
 +-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+""")

individual_a =random.choice(game_data.celebrities)
print(f"Compare A: {individual_a['name']}, {individual_a['description']}, {individual_a['country']}")
print(r""" _  _  ___ 
( \/ )/ __)
 \  / \__ \
  \/  (___/""")

individual_b = random.choice(game_data.celebrities)

while individual_b == individual_a:
    individual_b = random.choice(game_data.celebrities)



game_over = False
score = 0

while not game_over:
    print(f"Against B: {individual_b['name']}, {individual_b['description']}, {individual_b['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    score = 0

    if individual_a["followers"] > individual_b["followers"]:
        correct_answer = "A"
    else:
        correct_answer = "B"

    if guess == correct_answer:
        score += 1
        print(f"You're right! Score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")

    if guess == correct_answer:
        score += 1
    else:
        game_over = True





