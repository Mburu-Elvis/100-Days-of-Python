from art import logo
import os

print(logo)
next_bid = 'yes'
bidders = {}
while next_bid == 'yes':
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    bidders[name] = bid
    next_bid = input("Are there any other bidders? Type 'yes' of 'no'.\n")
    if next_bid == 'no':
        break
    else:
        next_bid = 'yes'
    os.system('clear')


def highest_bidder(bidders_list):
    highest_bid = 0
    bidder = ''

    for key, value in bidders_list.items():
        value = int(value)
        if value > highest_bid:
            bidder = key
            highest_bid = value

    if bidder:
        print(f"The winner is {bidder} with a ${highest_bid} bid")
    else:
        print(f"No bidder")


highest_bidder(bidders)