import random

# list of favourite fruits
word_list = ["lychee", "passionfruit", "cherry", "flat peach", "nectarine"]

# Randomly generate a word from the word list using the random.choice method
word = random.choice(word_list)

# print that word to standard output
print(word)

# Ask the user for an input and assign it to a variable called `guess`
guess = input("Enter a single letter: ")

# Chcek that the input is a single character
if len(guess) == 1 and guess.isalpha():
  print("Good guess!")
else:
  print("Oops! That is not a valid input.")

