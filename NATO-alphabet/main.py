import pandas as pd

alphabet = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict={row.letter:row.code for (index, row) in alphabet.iterrows()}

def gen_phonetic():
    user_word=input("Enter a word: ").upper()
    try:
        translation=[nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        return gen_phonetic()
    else:
        print(translation)


gen_phonetic()