from milestone_2 import word_to_guess

#Iteratively check if the input is a valid guess
while True:
  guess = input("Guess a letter: ")
  # check the input is a single alphabetical character
  if len(guess) == 1 and guess.isalpha():
    # Check whether the guess is in the word
    if guess in word_to_guess:
      print(f"Good guess {guess} is in the word.")
    else:
      print(f"Sorry, {guess} is not in the word. Try again.")
      break
  else:
    print("Invalid letter. Please, enter a single alphabetical character.")

