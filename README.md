# Hangman

> Python Project - [AiCore](https://www.theaicore.com/) (October 2023)

## Overview

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game played on the command line, where the computer chooses a word at random and the user tries to guess it.

In doing this project, I had the opportunity to implement principles of object-oriented programming - such as classes, encapsulation and abstraction - as well as fundamentals of creating programs in Python like importing modules and executing files directly and indirectly while being aware of the built-in `__name__` variable.

## File structure
- **milestone_5.py** contains the game logic
- **word_list.py** is a module containing the list of words
  - *The list in this module currently only consists of five words to test the game logic, but any words of your choosing can be added to that list*

The other .py files in this repo are earlier iterations of code or template files from AiCore which I have left as they are in case they are required for the marking of my project on submission.

## Installation instructions

Open your terminal in a directory of your choosing and clone this repository:

```
git clone https://github.com/hillaabra/hangman.git
```
Get inside the `hangman` directory:
```
cd hangman
```

## Usage

The game is run in the command line without options. To view the project documentation, run the following command on the command line from inside the inner `hangman` directory:

```
python -m pydoc milestone_5
```

## How to play

Start a game of Hangman by running the following command from inside the inner `hangman` directory:
```
$ python milestone_5.py
```

A word will be chosen at random from the `word_list` module and presented as a series of `_`, with each underscore representing a letter of the word, e.g. if the word chosen is 'apple', to begin with, you will see:
```
_ _ _ _ _
```

You'll automatically be prompted to guess a letter at every go. If the letter is contained within the word, you'll see the word to be guessed updated with your guess, e.g., if your guess was 'p', you'd see your progress updated with:
```
_ p p _ _
```

You can only enter one alphabetical letter at a time.

You start the game with 5 lives. You lose a life with each wrong letter guessed. If you make 5 wrong guesses, you lose, and the game ends.

If you guess all the letters in the word, you win the game.

If you guess a letter that you've already guessed, this won't affect your score, but you will be prompted to guess again until you guess a letter you haven't yet guessed in the current game.

Once the game ends, you can play again by re-running the same command above in the command line.


## License

This project is currently unlicensed as it has not yet been made public.