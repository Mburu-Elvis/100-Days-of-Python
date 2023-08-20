student_scores = input("Input a list of a student scores\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = student_scores[0]
for n in student_scores:
    if n > highest_score:
        highest_score = n
print(f"The highest score in the class is: {highest_score}")