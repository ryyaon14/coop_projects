
import random
import hangman_words
import hangman_art


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    
  


    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            if letter not in display:
              display[position] = letter
            else:
              
              print("The letter is already there, Try another one ")


    if guess not in chosen_word:
      
        
      
      print('the letter is not there.. try another one : ')
      lives -= 1
      if lives == 0:
          end_of_game = True
          print("You lose.")


    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    print(hangman_art.stages[lives])