import random
import hangman_words
from hangman_art import stages , logo



lives = 6


print (logo)
chosen_word = random.choice(hangman_words.word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

  
    print(f"****************************{lives} /6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

   
    if guess in correct_letters:
        print(f"you've already guessed {guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    

    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True

            
            print(f"***********************IT WAS {chosen_word} *YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    
    print(stages[lives])
