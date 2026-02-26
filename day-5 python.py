import random

lst = []

for i in range(1, 101):

    if i % 3 ==0 and i%5==0:
        print("Fizzbuzz")

    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)


import random

alphabet = [
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T',
    'U','V','W','X','Y','Z'
]

numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password = ""


for i in range(num_letters):
    password += random.choice(alphabet)


for i in range(num_symbols):
    password += random.choice(symbols)


for i in range(num_numbers):
    password += random.choice(numbers)


password_list = list(password)
random.shuffle(password_list)


final_password = "".join(password_list)

print(f"Your password is: {final_password}")

