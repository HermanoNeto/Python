import random
from replit import clear

word_list = ["car", "school", "blue", 'pink','horse', 'dog']
chosen_word = random.choice(word_list)


print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')

word = []
word_length = len(chosen_word)

for n in chosen_word:
    word.append('_')
print(word)


chances = 6

while '_' in word:
    guess = input("Guess a letter: ").lower()

    for posicao in range(word_length):
        letra = chosen_word[posicao]
        if guess in letra:
            word[posicao] = letra

    print(word)

    if not guess in chosen_word:
        chances -= 1

    if chances == 5:
        print('''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''')
    elif chances == 4:
        print('''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''')
    elif chances == 3:
        print('''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''')
    elif chances == 2:
        print('''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''')
    elif chances == 1:
        print('''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''')

    if chances == 0:
        print( '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
        print('You Lost')
        break



    if not '_' in word:
        print('You Win')
        break

print('==========\nGAME OVER.\n==========')
