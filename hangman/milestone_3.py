
while True:
  guess = input("Guess a letter: ")
  # check the input is a single alphabetical character
  if len(guess) == 1 and guess.isalpha():
    break
  else:
    print("Invalid letter. Please, enter a single alphabetical character.")
