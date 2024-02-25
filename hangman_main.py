HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

import random

word_list = [
    "pineapple", "elephant", "computer", "galaxy", "butterfly", 
    "kangaroo", "happiness", "adventure", "chocolate", "waterfall", 
    "universe", "laughter", "guitar", "rainbow", "mountain", 
    "friendship", "treasure", "sunshine", "mystery", "victory", 
    "dragon", "magician", "princess", "orchestra", "cathedral", 
    "astronaut", "paradise", "harmony", "fantasy", "discovery"
]
chosen_word = random.choice(word_list)

display = ["_" for _ in chosen_word]
print(display)

game_end = False
lives = 6

while not game_end and lives != 0:
    guess = input("guess a letter: ").lower()
    letter_found = False
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
            letter_found = True
    if not letter_found:
        lives -= 1
        print(HANGMANPICS[6-lives])
        print("WRONG GUESS")
    print(display)
    if "_" not in display:
        game_end = True
        print("You win!")
    elif lives == 0:
        print("You lose!")
