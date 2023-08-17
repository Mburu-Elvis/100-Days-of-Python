'''A program to calculate your life weeks

Taking 90 years as the life-expectacy age'''

age = input("What is your current age? ")

age = int(age)

years_left = 90 - age

months = years_left * 12
weeks = years_left * 52
days = years_left * 365

print(f"You have {days} days, {weeks} weeks and {months} months left")