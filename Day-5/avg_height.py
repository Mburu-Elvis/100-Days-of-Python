student_heights = input("Input a list of students heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum = 0
for height in student_heights:
    sum += height
avg = sum / (len(student_heights))
print(f"{avg:.2f}")