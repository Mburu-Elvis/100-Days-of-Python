import game_data
import art
import random
import os

logo = art.logo
vs = art.vs
data = game_data.data


def if_equal(id1, id2):
    if id1 == id2:
        id2 += 1
    return id2


def play_game():
    """Function defining the VS game logic """
    score = 0
    idx_1 = random.randint(0, len(data) - 1)
    idx_2 = random.randint(0, len(data) - 1)
    idx_2 = if_equal(idx_1, idx_2)
    account_a = data[idx_1]
    account_b = data[idx_2]
    fail = False

    while (fail == False):
        print(logo)
        print("compare A:", account_a['name'], account_a['description'], 'from', account_a['country'])
        print(vs, "\nAgainst B:", account_b['name'], account_b['description'], 'from', account_b['country'])
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        if choice == 'A':
            if account_a['follower_count'] > account_b['follower_count']:
                score += 1
                print(f"You're right! Current score: {score}")
                idx_1 = idx_1
                account_a = data[idx_1]
                idx_2 = random.randint(0, len(data) - 1)
                idx_2 = if_equal(idx_1, idx_2)
                account_b = data[idx_2]
                os.system('clear')
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                fail = True
        elif choice == 'B':
            if account_a['follower_count'] > account_b['follower_count']:
                score += 1
                print(f"You're right! Current score: {score}")
                idx_1 = idx_2
                account_a = data[idx_1]
                idx_2 = random.randint(0, len(data) - 1)
                idx_2 = if_equal(idx_1, idx_2)
                account_b = data[idx_2]
                os.system('clear')
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                fail = True
        else:
                print(f"Sorry, that's wrong. Final score: {score}")
                fail = True

play_game()
