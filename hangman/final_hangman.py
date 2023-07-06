import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
hasChosen = []
end_of_game = False
lives = 6
stages = hangman_art.stages

art = hangman_art.logo

print(art)

#Testing code
# print(f'Test, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()


    if guess in hasChosen:
        print(f"\nYou have already guessed {guess}")
    hasChosen.append(guess)

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
        print(f"\n{guess} is not in the word, you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")


    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])