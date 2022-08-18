import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
for letter in range(len(chosen_word)):
    display.append("_")

lives = 6
end_of_game = False
while not end_of_game:
    user_choice = input("Make a guess: ")
    guess = user_choice.lower()

    position = 0
    for letter in chosen_word:
        position += 1
        if letter == guess:
            display[position -1] = letter

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
    elif "_" in display and lives == 0:
        end_of_game = True
        print(f"You lose.\nThe word is: {chosen_word}.")