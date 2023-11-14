import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
 
        self.word_list = word_list
        self.word = self._get_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def _get_random_word(self):
  
        return random.choice(self.word_list)
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            
            # Loop through each letter in the word
            for i in range(len(self.word)):
                letter = self.word[i]
                
                # Check if the letter is equal to the guess
                if letter == guess:
                    # Replace the corresponding "_" in the word_guessed with the guess
                    self.word_guessed[i] = guess
                    
            # Reduce the variable num_letters by 1
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word.")

 

    def ask_for_input(self):

        while True:
            guess = input("Guess a letter: ").lower()
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)  
                self.list_of_guesses.append(guess)  
                break  

# Example usage:
word_list = ['apple', 'banana', 'orange', 'grape', 'kiwi']
hangman_game = Hangman(word_list)
hangman_game.ask_for_input()
