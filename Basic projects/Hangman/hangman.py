from random import choice
Lives=6
from hangman_words import word_list

chosen_word = choice(word_list)
word_length = len(chosen_word)

print(f'Chossen word is {chosen_word}')

from hangman_art import logo
print(logo)

# To display no. of letter in random word
Display =[]
for Letter in chosen_word:
    Display+='_'
print(Display)

end_of_the_game=False
while not end_of_the_game:
        guess=input("guess a word : ").lower()

        if guess in Display:
         print(f"You've already guessed {guess}")

        # display()

        for Position in range(len(chosen_word)):
          Letter=chosen_word[Position]
          if(guess==Letter):
                Display[Position]=Letter

        if guess not in chosen_word:
              print(f"You guessed {guess}, that's not in the word. You lose a life.")     


        if guess!=Letter:
            Lives-=1
            if Lives==0:
                end_of_the_game=True
                print("YOU LOOSE.")       
        print(Display)
        
        print(f"{' '.join(Display)}")


        if '_' not in Display:
             print("YOU WON")
             break
        from hangman_art import stages
        
        print(stages[Lives])    


