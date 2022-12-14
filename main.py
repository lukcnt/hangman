import random
import hangman_art
import hangman_words
import os

print(hangman_art.logo)

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

display = []
for letter in range(len(chosen_word)):
    display.append("_")


lives = 6
wrong_choices = []
end_of_game = False
while not end_of_game:
    user_choice = input("Make a guess: ")
    guess = user_choice.lower()

    os.system("clear")

    position = 0
    for letter in chosen_word:
        position += 1
        if letter == guess:
            display[position -1] = letter

    if guess not in chosen_word:
        if guess in wrong_choices:
            print(f"You've already guessed {guess}.")
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            wrong_choices.append(guess)
            lives -= 1

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
    elif "_" in display and lives == 0:
        end_of_game = True
        os.system("clear")
        print(f"You lose.\nThe word is: {chosen_word}.")

    print(hangman_art.stages[lives])