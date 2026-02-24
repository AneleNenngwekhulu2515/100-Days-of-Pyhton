print("Welcome to the tip calculator!")

bill = float(input("What was your total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?  "))
people = int(input("How many people to split the bill? "))

total_percent = tip / 100 * bill
total_bill = bill + total_percent
total_per_person = round(total_bill / people, 2)

print(f"Each person should pay: ${total_per_person}")