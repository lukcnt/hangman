import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
for letter in range(len(chosen_word)):
    display.append("_")

user_choice = input("Make a guess: ")
guess = user_choice.lower()

position = 0
for letter in chosen_word:
    position += 1
    if letter == guess:
        display[position -1] = letter

print(f"{' '.join(display)}")