import random

friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]

random_name = random.choice(friends)

print(random_name)

#Rock, paper , scissors

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor\n"))

#rock =0
rock = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
#paper=1
paper = r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
#scissors = 2
scissors = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]
if player >= 0 and player <= 2:
    print(game_images[player])

computer = random.randint(0,2)
print(f"Computer chose: {computer} ")
print(game_images[computer])

if player == 0 and computer == 0 :
    print("Its a draw")
elif player == 0 and computer == 1:
    print("You lose!")
elif player == 0 and computer == 2:
    print("You win!")

elif player == 1 and computer == 0 :
    print("You win")
elif player == 1 and computer == 1:
    print("Its a draw")
elif player == 1 and computer == 2:
    print("You lose")

elif player == 2 and computer == 0 :
    print("You lose")
elif player == 2 and computer == 1:
    print("You win ")
elif player == 2 and computer == 2:
    print("Its a Draw")
else:
    print("pick a number ")

