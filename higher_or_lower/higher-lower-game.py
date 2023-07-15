from art import logo, vs
from game_data import data
import random

import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def format_data(account):
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return(f"{account_name}, a(n) {account_descr} from {account_country}")


def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == 'a'
  else:
    return guess == 'b'

final_score_to_finish = len(data) - 1

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:

  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)
    
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")
  

  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  clear()
  print(logo)
  
  if is_correct:
    score += 1
    print(f"You are right! Current score: {score}")
    account_a = account_b
  else:
    game_should_continue = False
    print(f"Sorry, you are wrong! Final score: {score}")
  
