"""A roller coaster ticketer

A program that checks a persons eligiblity to ride the roller coater
if eligible it calculates the total bill for a person depending on age and preferences"""


print("Welcome to the rollercoaster")

height = int(input("Enter your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster", "\U0001F604")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us")
    else:
        bill = 12
        print("Adult tickets are $12")
    want_photo = input("Do you want a photo taken? Y or N. ")
    if want_photo == "Y":
        # Add $3 to their bill
        bill += 3
        print("Your total bill is $", bill)
    if want_photo == "N":
        print("Your total bill is $", bill)
else:
    print("You cannot ride the rollercoaster", "\U0001F622")        