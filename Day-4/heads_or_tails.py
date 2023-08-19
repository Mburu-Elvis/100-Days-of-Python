import random


test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

rand = random.randint(0, 1)

if rand >= 0.5:
    print("Heads")
else:
    print("Tails")
