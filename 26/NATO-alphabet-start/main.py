import pandas

#Loop through rows of a data frame
#for (index, row) in dataframe.iterrows():
    #Access index and row
    #Access row.student or row.score

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv("nato_phonetic_alphabet.csv")
df_dict = df.set_index('letter')['code'].to_dict()   # método set_index: define uma ou mais colunas de um DF como o índice, relacionando-a com a outra coluna
print(df_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
type_word = input("Enter a word: ").upper()
letters = list(type_word)
print(letters)

# df_dict["A"] - acessa o valor associado à chave no dicionário. Ex: retorna o código fonético Alfa
new_list = [df_dict[letter] for letter in letters if letter in df_dict]
print(new_list)



