'''
A program to calculate the BMI of a person given the height and weight

It classifies the BMI and prints the class
'''

print("Welcome to the BMI calculator")

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kgs: "))

bmi = round(weight / (height ** 2), )

if bmi < 18.5:
    print(f"You are underweight: your bmi is {bmi}")
elif bmi >= 18.5 and bmi < 25:
    print(f"You have a normal weight,: your bmi is {bmi}")
else:
    if bmi < 30:
        print(f"You are overweight: your bmi is {bmi}")
    elif bmi >= 30 and bmi < 35:
        print(f"You are obese: your bmi is {bmi}")
    else:
        print(f"You are clinically obese: your bmi is {bmi}")