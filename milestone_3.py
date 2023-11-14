
import random


word_list = ["apple", "banana", "orange", "grape", "kiwi"]


secret_word = random.choice(word_list)

while True:

    guess = input("Guess a letter: ")


    if guess.isalpha() and len(guess) == 1:

        break
    else:

        print("Invalid letter. Please, enter a single alphabetical character.")


if guess in secret_word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")

print(f"The word was: {secret_word}")