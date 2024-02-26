import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#the clear function is chatgpt
    
bids = {}
highest_bid = 0

def find_greater_bid(bids, highest_bid):
    winner = None
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            winner = bidder
    return winner, highest_bid

more_users = True

while more_users:
    clear()

    name = input("Enter your name: ")
    bid = int(input("Enter your bid (in Rs): "))

    bids[name] = bid

    q = input("Are there any other bidders? (y/n): ").lower()

    if q == "n":
        more_users = False


winner, highest_bid = find_greater_bid(bids, highest_bid)
if winner:
    print(f"The winner is {winner} with the highest bid of Rs{highest_bid}")

