from replit import clear

user_bid = {}


def auction_blind(name, bid_price):
    user_bid[name] = bid_price


auction_blind(input("Type your name: "), int(input("Type your bid: $")))

while True:
    other_bids = input("there are other users who want to bid? ('yes'/ 'no') ").strip()
    if other_bids.lower() == "yes":
        clear()
        auction_blind(input("Type your name: "), int(input("Type your bid: $")))
    else:
        break

user = ''
highest = 0
for key in user_bid:
    if user_bid[key] > highest:
        user = key
        highest = user_bid[key]

print(f"The winner is {user} with a bid of {highest}")
