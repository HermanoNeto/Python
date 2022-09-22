import pandas as pd

nato_csv = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet=pd.DataFrame(nato_csv)


nato_alphabet_dict={row.letter:row.code for (index, row) in alphabet.iterrows()}


user_word=input("Enter a word: ")


spelled_word=[letter.upper() for letter in user_word]

translation=[nato_alphabet_dict[letter] for letter in spelled_word]


print(translation)
