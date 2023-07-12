import random
from art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == 'easy':
    return EASY_LEVEL_TURNS
  elif difficulty == 'hard':
    return HARD_LEVEL_TURNS
  else:
    print("Difficulty not selected")

def check_answer(guess, answer, attempts):
  if guess == answer:
    print(f"You got it, the number was {answer}")
  elif guess > answer:
    print("Too high")
    return attempts - 1
  elif guess < answer:
    print("Too low")
    return attempts - 1
         
def game():

  print(logo)
  print("I'm thinking of a number beetween 1 and 100")
  number_generator = random.randint(1,100)
  guess = 0
  turns = set_difficulty()
  # print(f"Testing number: {number_generator}")
  while guess != number_generator:
  
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, number_generator, turns)
    if turns == 0:
      print("You are out of attempts, game over")
      return
    elif guess != number_generator:
      print("Guess again")
      print(f"You have {turns} attempts remaining to guess the number.")
      
game()
