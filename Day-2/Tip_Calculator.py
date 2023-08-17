'''A program to calculate the tip'''

print('Welcome to the tip calculator')
bill = float(input("What is the total bill? $"))
tip_per = int(input("What percetage tip would you like to give? 10, 12 or 15? "))
split = int(input("How many people to split the bill? "))

tip = (tip_per/100)* bill
total_bill = bill + tip
bill_each = round(total_bill / split, 2)

print(f"Each person should pay: ${bill_each}")