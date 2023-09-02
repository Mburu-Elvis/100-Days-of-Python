import art
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def check_high(userList=[], compList=[]):
    if sum(userList) > sum(compList):
        return (True)
    else:
        return (False)
def addCard(myList, compList):
    myList.append(random.randint(0, len(cards)))
    compList.append(random.randint(0, len(cards)))

def check_comp_value(compList=[]):
    if sum(compList) < 17:
        compList.append(random.randint(0, len(cards)))

def check_values(userList=[], compList=[]):
    if sum(userList) > 21:
        print("You Lose!")
    elif sum(compList) > 21 and sum(userList) <= 21:
        print("You win!")
    else:
        print("You Lose!")

def if_valid(myList):
    if sum(myList) > 16:
        return (True)
    else:
        return (False)

while play == 'y':
    print(art.logo)

    user_cards = []
    comp_cards = []
    user_cards.append(random.randint(0, len(cards)))
    user_cards.append(random.randint(0, len(cards)))
    comp_cards.append(random.randint(0, len(cards)))

    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {comp_cards[0]}")
    if sum(user_cards) > 21:
        print("You Lose!")
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play == 'y':
            os.system('clear')
            continue
        else:
            break

    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if another_card == 'y':
        addCard(user_cards, comp_cards)
        check_comp_value(compList=comp_cards)
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's cards: {comp_cards}")
        if if_valid(user_cards) == False:
            print("You Lose!")
            play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
            if play == 'y':
                os.system('clear')
                continue
            else:
                break

    else:
        check_comp_value(compList=comp_cards)


    if check_high(userList=user_cards, compList=comp_cards) == True:
        check_values(userList=user_cards, compList=comp_cards)
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's cards: {comp_cards}")
    else:
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's cards: {comp_cards}")
        print("You Lose")
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'y':
        os.system('clear')
        continue
    else:
        break

