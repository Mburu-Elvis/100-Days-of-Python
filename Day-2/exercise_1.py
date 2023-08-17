'''A program that adds digits in a 2 digit number'''

num = int(input("Enter a two digit number: "))

num_str = str(num)
if len(num_str) != 2:
    print("Your input is wrong")
else:
    a = int(num_str[0])
    b = int(num_str[1])
    print("The sum of {:d} and {:d} is".format(a, b), a + b)