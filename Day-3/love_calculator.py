'''
A program to calculate love between a person and the partner
'''

print("Welcome to the Love Calculator!")

name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

names = name1 + name2
names = names.lower()

a = 0
b = 0
for i in "true":
    a += names.count(i)
for j in "love":
    b += names.count(j)
c = int(str(a) + str(b))

if c < 10 or c > 90:
    print(f"Your score is {c}, you go together like coke and mentos.")
elif c >= 40 and c <= 50:
    print(f"Your score is {c}, you are alright together.")
else:
    print(f"Your score is {c}.")