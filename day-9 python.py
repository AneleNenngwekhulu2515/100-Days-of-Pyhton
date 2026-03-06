student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for value in student_scores:
    grades = student_scores[value]
    if grades >=91 and grades <=100:
        student_grades[value] = "Outstanding"
    elif grades>=81 and grades <=90:
        student_grades[value] = "Exceeds Expectations"
    elif grades >= 71 and grades <=80:
        student_grades[value] = "Acceptable"
    elif grades <=70:
        student_grades[value] = "Fail"
        print(student_grades)

travel_log = {
    "france": ["paris", "lille", "dijon"],
    "germany": ["strutt", "berlin"]
}

print(travel_log["france"][1])

travel_log = {
    "france": {"num_times_visited":8 , "cities_visited":["strutt", "berlin"] },
    "germany": ["strutt", "berlin"]
}

print(travel_log["france"]["cities_visited"][1])


print("*********************************Bidding Game*********************************")

print(r"""
 █████╗ ██╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
███████║██║   ██║██║        ██║   ██║██║   ██║██╔██╗ ██║
██╔══██║██║   ██║██║        ██║   ██║██║   ██║██║╚██╗██║
██║  ██║╚██████╔╝╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
""")

print("Welcome to the secret auction program.")

bid_over = True
biddings = {}
values = []
while bid_over:

    name = input("What is your name?: \n")
    bid = int(input("What is your bid?: $\n"))
    biddings[name] = bid

    repeat = input("Are there any other bidders? Type 'yes' or 'no' \n")
    if repeat == "yes":
        biddings[name] = bid
    else :
        bid_over = False
print(biddings)

for key in biddings:
    value = biddings[key]
    values.append(value)
print(values)

highest_bid = max(values)
print(highest_bid)

