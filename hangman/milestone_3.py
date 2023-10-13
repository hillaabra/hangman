from milestone_2 import word_to_guess

def check_guess(guess):
  # Check whether the guess is in the word
  if guess.lower() in word_to_guess:
    print(f"Good guess {guess} is in the word.")
  else:
    print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
  while True:
    #Iteratively check if the input is a valid guess
    guess = input("Guess a letter: ")
    # check the input is a single alphabetical character
    if len(guess) == 1 and guess.isalpha():
      break
    else:
      print("Invalid letter. Please, enter a single alphabetical character.")

  check_guess(guess)

print(word_to_guess)
ask_for_input()





