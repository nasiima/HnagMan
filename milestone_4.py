import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        # Step 3
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

# Testing the Hangman class
hangman_game = Hangman(["apple", "banana", "orange", "grape", "kiwi"])
print(f"Word to guess: {hangman_game.word}")
print(f"Word guessed so far: {hangman_game.word_guessed}")
print(f"Number of unique letters: {hangman_game.num_letters}")
print(f"Number of lives: {hangman_game.num_lives}")
print(f"List of guesses: {hangman_game.list_of_guesses}")
