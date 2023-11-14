import random


favorite_fruits = ["Apple", "Banana", "Orange", "Strawberry", "Mango"]

word_list = favorite_fruits

word = random.choice(word_list)

print(word)

guess = input("Enter a single letter: ")

print(guess)
