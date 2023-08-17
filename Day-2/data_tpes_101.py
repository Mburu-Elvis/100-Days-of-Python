num_char = len(input("What is your name?\n"))

# Type checking
print("input is of type", type(num_char))

# Type Conversion / Casting
new_num_char = str(num_char)
a = str(123)
print("Your name has " + new_num_char + " characters.")
print("Type casted int to string", a)

print(str(70) + str(100))