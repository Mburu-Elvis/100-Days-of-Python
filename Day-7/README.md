# Day-7

Day 7 of 100 days of code

Implement the hangman game

## Concepts used in the implementation

- ### while loop

This loop enables the game to continuously take use input if the lives of the user are not depleted

- ### for loop

This loop is used to iterate through a list words

The list are loop in two ways

- `for item in items` where item is a single word/list item and items is the list
- `for i range` where i is just an iterable and range is the range to be considered

> in this instance the length of the list thus
`for i in range(len_word)` where `len_word = len(word_list)`

### modules

modules have been used to import extra functions and items to the main program

Example modules:-

- #### random

> it is used to randomly select items

- #### hangman_art

> It contains the graphics for the hangman at each stage

- #### hangman_words

> contains a list of words from which `random` picks from
