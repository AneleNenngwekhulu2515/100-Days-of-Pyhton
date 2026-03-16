import game_data
import random

print(r""" +-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+
 |H|i|g|h|e|r| |o|r| |L|o|w|e|r|
 +-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+""")

individual_a =random.choice(list(game_data.celebrities))
print(f"Compare A: {individual_a['name']}, {individual_a['description']}, {individual_a['country']}")
game_data.celebrities.remove(individual_a)
print(r""" _  _  ___ 
( \/ )/ __)
 \  / \__ \
  \/  (___/""")

individual_b = random.choice(list(game_data.celebrities))
print(f"Against B: {individual_b['name']}, {individual_b['description']}, {individual_b['country']}")
game_data.celebrities.remove(individual_b)
guess = input("Who has more followers? Type 'A' or 'B': ").upper()


