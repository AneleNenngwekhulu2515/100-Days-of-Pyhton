#prime number checker

def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def is_prime(num):
    factors = find_factors(num)
    if len(factors)==2:
        return True
    else:
        return False
print(find_factors(73))
print(is_prime(73))

print(find_factors(75))
print(is_prime(75))

print(r"""
 _   _                 _                  _____                       
| \ | |               | |                / ____|                      
|  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __  __ _ _ __ ___   ___  
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ |/ _` | '_ ` _ \ / _ \ 
| |\  | |_| | | | | | | |_) |  __/ |    | |__| | (_| | | | | | |  __/ 
|_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|_| |_| |_|\___| 

                    NUMBER GUESSING GAME
""")

import random

print("Welcome to the Number Guessing Game!🐍💻")
print("I'm thinking of a number between 1 and 100.")


def random_number():
    chosen_number = random.randint(1, 100)
    return chosen_number


dificulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
easy_counts = 10
hard_counts = 5

guessed = True

#made it a variable, because everytime i called it would create a new random number
number = random_number()


while guessed:
    if dificulty_level == 'easy':
        print(f"You have {easy_counts} attempts remaining to guess the number ")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it!🏆. The number was {number}")
            break
        elif guess > number:
            print("Too high!")
            easy_counts -= 1
        elif guess < number:
            print("Too low!")
            easy_counts -= 1

    if dificulty_level == 'hard':
        print(f"You have {hard_counts} attempts remaining to guess the number ")
        guess = int(input("Make a guess🧠: "))
        if guess == number:
            print(f"You got it!🏆. The number was {number}")
            break
        elif guess > number:
            print("Too high!")
            hard_counts -= 1
        elif guess < number:
            print("Too low!")
            hard_counts -= 1

    # print("Guess:", guess)
    # print("Number:", number)

    if easy_counts==0 or hard_counts==0:
        print("You've run out of attempts😢")
        print("YOU LOST💀")
        print(f"The number was {number}")
        break











