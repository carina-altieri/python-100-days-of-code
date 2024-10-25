# Blind auction project

import art
print(art.logo)

bids = {}
new_bids = True
while new_bids == True:
    name = (input("What is your name?\n")).lower()
    bid = int(input("What is your bid?\n $"))
    continue_bidding = input("Is there any bid to be added? Type 'yes' or 'no'.\n").lower()
    bids[name] = bid
    print("\n" * 100)
    if continue_bidding == "no":
        new_bids = False
        max_bid = bids[max(bids, key=bids.get)]
        print(f"The winner is {name} with the highest bid of ${bid}!")
