student_scores = {
    "Harry": 81,
    "Ron":  78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

def grade_score(score):
    '''
    function to grade a student score
    '''

    grade = ''
    if score > 90 and score <= 100:
        grade = 'Outstanding'
    elif score > 80 and score <= 90:
        grade = "Exceeds Expectation"
    elif score > 70 and score <= 80:
        grade = "Acceptable"
    else:
        grade = "Fail"
    return (grade)

for key, value in student_scores.items():
    student_grades[key] = grade_score(value)
    print

print(student_scores)
print(student_grades)