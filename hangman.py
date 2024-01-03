import random

from word_list import word_list

class Hangman():
  '''
  A Hangman Game that asks the user for a letter and checks if it is in the word.
  It starts with a default number of lives and a random word from the word_list.

  Parameters:
  ----------
  word_list: list
      List of words to be chosen from for the game
  num_lives: int
      Number of lives, with a default value of 5 at
      initialisation

  Attributes:
  ----------
  num_lives: int
      Initialised with 5 lives, the player loses
      a life with each wrong letter guessed
  word_guessed: list
      A list representing the letters of the word
      to be guessed, with '_' for each letter of
      the word not yet guessed by the player
  _ls_guessed_letters: list
      Protected; a list keeping record the player's
      letter guesses, initialised as an empty list
  '''
  def __init__(self, word_list, num_lives=5):
    '''
    See help(Hangman) for accurate signature
    '''
    # the word to be guessed, picked randomly from __word_list; private
    self.__word_to_guess = random.choice(word_list)
    # a list of the letters of the word, with _ for each letter not yet guessed; private
    self.word_guessed = ['_' for char in self.__word_to_guess]
    # the number of unique letters in the word that have not been guessed yet; private
    self.__num_letters_left_to_guess = len(set(self.__word_to_guess))
    # the number of lives the player has at the start of the game, or left; public
    self.num_lives = num_lives
    # letters guessed by the user so far, initially set to an empty list; protected
    self._ls_guessed_letters = []

  def _update_word_guessed(self, guessed_letter):
    '''
    Protected; this function is used internally to update
    word_guessed, the list representing the letters of the
    word guessed and not yet guessed by the player.

    Arguments:
    ---------
    guessed_letter: str
        The letter guessed by the player
    '''
    for index in range(len(self.__word_to_guess)):
        if self.__word_to_guess[index] == guessed_letter:
         self.word_guessed[index] = guessed_letter

  def _update_num_letters_left_to_guess(self):
    '''
    Protected; this function is used internally
    to update the private attribute keeping count
    of the number of unique letters in the word
    left to be guessed.
    '''
    self.__num_letters_left_to_guess -= 1

  def _update_num_lives(self):
    '''
    Protected; this function is used internally to
    update num_lives, the attribute keeping count of
    the number of lives the player has left.
    '''
    self.num_lives -= 1

  def _update_ls_guessed_letters(self, guessed_letter):
    '''
    Protected; this function is used internally to
    update _ls_guessed_letters with the valid guesses
    of the player during the game.

    Arguments:
    ---------
    guessed_letter: str
        The letter guessed by the user
    '''
    self._ls_guessed_letters.append(guessed_letter)

  def _check_for_guessed_letter_in_word(self, guessed_letter):
    '''
    Protected; this function is used internally to
    check if the letter guessed by the user is in
    the word to be guessed.

    Arguments:
    ---------
    guessed_letter: str
        The letter guessed by the user
    '''
    if guessed_letter in self.__word_to_guess:
      print(f"Good guess! {guessed_letter} is in the word.")
      self._update_word_guessed(guessed_letter)
      self._update_num_letters_left_to_guess()
    else:
      self._update_num_lives()
      print(f"Sorry, {guessed_letter} is not in the word.\nYou have {self.num_lives} lives left.")

  @staticmethod
  def _check_if_input_valid(guessed_letter):
    '''
    This function is used internally to check if
    the user input is a single alphabetical character.

    Arguments:
    ---------
    guessed_letter: str
        The letter guessed by the user

    Returns:
    -------
    bool: True if the input is valid, False otherwise.
    '''
    return len(guessed_letter) == 1 and guessed_letter.isalpha() == True

  def ask_for_input(self):
    '''
    This function prompts the user for an input,
    i.e. to guess a letter that is in the word.
    If the user's input is invalid, the user will be
    prompted to re-input their guess until the input
    is valid.
    '''
    print(" ".join(self.word_guessed))

    while True:
      guessed_letter = input("Guess a letter: ")
      if self._check_if_input_valid(guessed_letter) == False:
        print("Invalid letter. Please, enter a single alphabetical character.")
      elif guessed_letter in self._ls_guessed_letters:
        print("You already tried that letter!")
      else:
        guessed_letter = guessed_letter.lower()
        self._check_for_guessed_letter_in_word(guessed_letter)
        self._update_ls_guessed_letters(guessed_letter)
        break

  def play_game(self):
    '''
    This function starts and ends the game
    when the player either wins or loses.
    '''
    while True:
      if self.num_lives == 0:
        print(f"You lost! The word was {self.__word_to_guess}")
        break
      elif self.__num_letters_left_to_guess > 0:
        self.ask_for_input()
      else:
        print("Congratulations! You won!")
        break

def initialise_game(word_list):
  '''
  This function creates a game instance of the
  Hangman class and initialises the game.

  Arguments:
  ---------
  word_list: list
      A list of words from which the Hangman object
      will choose at random the word to be guessed.
  '''
  game = Hangman(word_list)
  game.play_game()

if __name__ == "__main__":
  initialise_game(word_list)