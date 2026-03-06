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
