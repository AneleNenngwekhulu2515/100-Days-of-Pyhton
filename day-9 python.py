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
