import hangman_pics
import random
import hangman_words

chosen_word = random.choice(hangman_words.word_list)

display = ["_" for _ in chosen_word]
print(display)

game_end = False
lives = 6

while not game_end and lives != 0:
    guess = input("guess a letter: ").lower()
    letter_found = False
    if guess in display:
        print("Already guessed bro")
    else:
      for position in range(len(chosen_word)):
          letter = chosen_word[position]
          if guess == letter:
              display[position] = letter
              letter_found = True
      if not letter_found:
          lives -= 1
          print(hangman_pics.HANGMANPICS[6-lives])
          print("WRONG GUESS")
      print(display)

      
    if "_" not in display:
        game_end = True
        print("You win!")
    elif lives == 0:
        print("You lose!")
        print (f"The correct word was {chosen_word}")
