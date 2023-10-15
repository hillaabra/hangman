import random

class Hangman():
  # initialiser
  def __init__(self, word_list, num_lives=5):
    # the word to be guessed, picked randomly from __word_list
    self.__word_to_guess = random.choice(word_list)
    # a list of the letters of the word, with _ for each letter not yet guessed
    self.word_guessed = ['_' for char in self.__word_to_guess]
    # the number of unique letters in the word that have not been guessed yet
    self.__num_letters_left_to_guess = len(set(self.__word_to_guess))
    # the number of lives the player had at the start of the game
    self.num_lives = num_lives
    # a list of words
    self.__word_list = word_list
    # a list of guesses, initially set to an empty list
    self._ls_guessed_letters = []

  def _check_for_guessed_letter_in_word(self, guessed_letter):
    guessed_letter = guessed_letter.lower()
    if guessed_letter in self.__word_to_guess:
      print(f"Good guessed_letter! {guessed_letter} is in the word.")
      for index in self.__word_to_guess:
        if self.__word_to_guess[index] == guessed_letter:
         self.word_guessed[index] = guessed_letter
      self.__num_letters_left_to_guess -= 1
    else:
      self.num_lives -= 1
      print(f"Sorry, {guessed_letter} is not in the word.\nYou have {self.num_lives} left.")

  def check_if_input_valid(guessed_letter):
    return len(guessed_letter) == 1 and guessed_letter.isalpha() == True

  def ask_for_input(self):
    while True:
      guessed_letter = input("Guess a letter: ")
      if self.check_if_input_valid(guessed_letter) == False:
        print("Invalid letter. Please, enter a single alphabetical character.")
      elif guessed_letter in self._ls_guessed_letters:
        print("You already tried that letter!")
      else:
        self._check_for_guessed_letter_in_word(guessed_letter)
        self._ls_guessed_letters.append(guessed_letter)

test_game = Hangman(["lychee", "passionfruit", "cherry", "flat peach", "nectarine"])
test_game.ask_for_input()