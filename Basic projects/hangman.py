import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

Lives=6

word_list=["needle","science","adjective","correct","finally","stood"
"softly","stepped","drive","thrown","diagram","interior"
"addition","necessary","prove","test","chest","limited"
"track","crack","prevent","its","own","mine"
"statement","worse","reason","friend","shinning","serve"
"hold","race","smooth","broke","rubber","variety"
"gather","bark","five","smooth","health","is"]

# Random word choosen to start the game
choosen_word =random.choice(word_list)
print(f'Chossen word is {choosen_word}')

# To display no. of letter in random word
Display =[]
for Letter in choosen_word:
    Display+='_'
print(Display)

end_of_the_game=False
while not end_of_the_game:
        guess=input("guess a word : ").lower()

        # display()

        for Position in range(len(choosen_word)):
          Letter=choosen_word[Position]
          if(guess==Letter):
                Display[Position]=Letter
        if guess!=Letter:
            Lives-=1
            if Lives==0:
                end_of_the_game=True
                print("YOU LOOSE.")       
        print(Display)

        if '_' not in Display:
             print("YOU WON")
             break
        print(stages[Lives])    


