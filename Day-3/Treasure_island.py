'''Treasure Island

Direction a user takes determine where they'll end up'''

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasue Island.\nYour Mission is to find the treasue.")

turn = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()

if turn == "left":
    move = input("You find a canal, will you swim or wait? Type \"wait\" or \"swim\"\n").lower()
    if move == "swim":
        print("Sharks have devoured you\nGame Over.")
    elif move == "wait":
        door = input("You find an abandoned boat and cross the canal,\n\tYou find a light house with three doors which on will you open?\n\t\tType \"Red\", \"Yellow\" or \"Blue\"\n").lower()
        if door == "red" or door == "blue":
            if door == "red":
                print("You entered into the hot room")
            else:
                print("You entered into the cold room")
            print("Game Over.")
        elif door == "yellow":
            print("You found the treasure\nYou Win!")
else:
    print("You fell from a cliff\nGame Over.")