import os
from art import logo

bids = []
keepBidding = True

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def add_bid(name, value):
    bids.append({"name": name, "bid": value})

def find_highest_bidder(bidding_list):
  bid_value = 0
  bid_name = ''
  for value in bidding_list:
      if value["bid"] > bid_value:
          bid_value = value["bid"]
          bid_name = value["name"]
  return print(f"The highest bidder is {bid_name} with the bid of ${bid_value}")

print(logo)

while keepBidding:
    bidder_name = input("What is your name?: ")
    bid_value = int(input("What is your bid? $ "))
    add_bid(bidder_name, bid_value)

    final = input(
        "Another bidder? Type 'yes' to continue bidding or 'no' to finish the auction: "
    )

    if final == 'no':
        keepBidding = False
        clear()
        find_highest_bidder(bids)
    elif final == 'yes':
        clear()
    else:
        clear()
        print("Not a valid option: ")

