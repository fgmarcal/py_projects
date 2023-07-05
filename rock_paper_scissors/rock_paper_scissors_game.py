import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]
chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))

if chose > 3 or chose < 0:
    print("End Game, invalid number")
else:
    players_choice = game[chose]
    pc_choice = game[random.randint(0, 2)]

    print("\nYou chose:\n")
    print(players_choice)
    print("\nComputer chose: \n")
    print(pc_choice)

    if players_choice == rock:
        if pc_choice == scissors:
            print("You win!")
        elif pc_choice == paper:
            print("You lose!")
        else:
            print("Draw!")
    elif players_choice == paper:
        if pc_choice == scissors:
            print("You lose!")
        elif pc_choice == rock:
            print("You win!")
        else:
            print("Draw!")
    elif players_choice == scissors:
        if pc_choice == paper:
            print("You win!")
        elif pc_choice == rock:
            print("You lose!")
        else:
            print("Draw!")
