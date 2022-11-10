student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


def stu(grades, scores):
    for key, value in scores.items():
        if value >= 91:
            grades[key] = "Outsanding"
        elif 81 <= value <= 90:
            grades[key] = "Exceeds Expectations"
        elif 71 <= value <= 80:
            grades[key] = "Acceptable"
        elif value <= 70:
            grades[key] = "Fail"
    return grades


student_grades = {}
student_grades = stu(student_grades, student_scores)

print(student_grades)
