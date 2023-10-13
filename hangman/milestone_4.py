import random

#word_list = []

class Hangman():
  # initialiser
  def __init__(self, word_list, num_lives=5):
    # the word to be guessed, picked randomly from word_list
    self.word = random.choice(word_list)
    # a list of the letters of the word, with _ for each letter not yet guessed
    self.word_guessed = ['_' for char in self.word]
    # the number of unique letters in the word that have not been guessed yet
    self.num_letters = len(set(self.word).difference(set(self.word_guessed)))
    # the number of lives the player had at the start of the game
    self.num_ives = num_lives
    # a list of words
    self.word_list = word_list
    # a list of guesses, initially set to an empty list
    self.list_of_guesses = []

  def check_guess(self, guess):
    guess.lower()
    if guess in self.word:
      print(f"Good guess! {guess} is in the word.")

