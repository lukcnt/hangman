import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

user_choice = input("Make a guess: ")
guess = user_choice.lower()