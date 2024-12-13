# new_dict ={new_key:new_value for (key,value) in dict.items() if test}
# criando um dicionário que transforma cada palavra em um item de uma lista e calcula o comprimento de cada palavra

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list = sentence.split()
result = {word:len(word) for word in list}
print(result)
