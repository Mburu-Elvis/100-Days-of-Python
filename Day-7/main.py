import random
import hangman_words
import hangman_art


word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
len_word = len(chosen_word)
logo = hangman_art.logo
stages = hangman_art.stages
lives = 6

print(logo)
display = []

for _  in range(len_word):
    display += '_'

end_of_game = False
while not end_of_game and lives:
    guess = input("Guess a letter: ").lower()

    for i in range(len_word):
        if guess == chosen_word[i]:
            display[i] = guess
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lose")
            break
    print(display)

    if '_' not in display:
        end_of_game = True
        print("You win")
    print(stages[lives])
