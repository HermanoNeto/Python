import pandas as pd

alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
alpha=pd.DataFrame(alphabet)


nato_dict={row.letter:row.code for (index, row) in alpha.iterrows()}


user_word=input("Enter a word: ")


spelled_word=[letter.upper() for letter in user_word]

translation=[nato_dict[letter] for letter in spelled_word]


print(translation)
