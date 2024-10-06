import random

word_list = ["aardvark", "baboon", "camel"]

# Hangman case
# TODO-1 - Randomly choose word from word list and assign variable chosen_word and print it
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2- Ask the user to guess a letter and assign the letter to variable called guess. make lettter lowercase.
guess = input("Guss the letter: ").lower()
print(guess)

#TODO-3- Check if the letter user guessed is one of the letter in choden word. Print Right if it is, "Wrong" if it's not.

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")