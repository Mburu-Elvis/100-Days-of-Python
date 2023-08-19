import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)


namesAsCSV = input("Give me everybody's name, separated by a comma. \n")

names = namesAsCSV.split(", ")

index = random.randint(0, len(names) -1)

print(names[index], "is going to but the meal today!")