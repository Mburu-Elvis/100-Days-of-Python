'''
a program that allows an user to select a position on a matrix of emojis

it prints the emoji selected
'''


row1 = ["🙃", "😉", "😊"]
row2 = ["😅", "🤣", "😂"]
row3 = ["😎", "🤓", "🧐"]
map = [row1, row2, row3 ]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
position = position.split(" ")
x = int(position[0]) - 1
y = int(position[1]) - 1
print(map[x][y])
print(f"{row1}\n{row2}\n{row3}")