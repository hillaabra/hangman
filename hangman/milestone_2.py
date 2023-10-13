import random

# list of favourite fruits
word_list = ["lychee", "passionfruit", "cherry", "flat peach", "nectarine"]

# Randomly generate a word from the word list using the random.choice method
word_to_guess = random.choice(word_list)

# Ask the user for an input and assign it to a variable called `guess`
def get_user_input():
  letter_guess = input("Enter a single letter: ")
  # check the input is a single alphabetical character
  if len(letter_guess) == 1 and letter_guess.isalpha():
    print("Good guess!")
  else:
    print("Oops! That is not a valid input.")
    get_user_input()

get_user_input()
