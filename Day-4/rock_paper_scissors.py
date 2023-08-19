import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]

x = int(input("What dou you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(choices[x])

comp_gen = random.randint(0, 2)

print(choices[comp_gen])

if x == 0:
    if comp_gen == 2:
        print("You win!")
    elif comp_gen == 1:
        print("You lose!")
    else:
        print("It's a draw")
elif x == 1:
    if comp_gen == 0:
        print("You win")
    elif comp_gen == 1:
        print("It's a draw")
    else:
        print("You lose!")
else:
    if comp_gen == 0:
        print("You lose!")
    elif comp_gen == 1:
        print("You win!")
    else:
        print("It's a draw")