# with open("weather_data.csv", "r") as weather_data_file:
#    data = weather_data_file.readlines()

# import csv

# with open("weather_data.csv", "r") as weather_data_file:
#    data = csv.reader(weather_data_file) # cria um leitor de csv
#    for row in data:
#        print(row)
 

# with open("weather_data.csv", "r") as weather_data_file:
#    data = csv.reader(weather_data_file) # cria um leitor de csv
#    # next(weather_data_file) - ignora o cabeçalho
#    temperatures = []
#    for row in data: # pegando cada linha dentro de data
#        if row[1] != "temp":
#            temperatures.append(int(row[1])) # as temperaturas estão no índice 1 de cada linha
# print(temperatures)

# lendo arquivos com pandas 
import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data)) # tipo: DataFrame (tabela)

data = pandas.read_csv("weather_data.csv")
# print(type(data["temp"])) # nome da coluna / tipo: Series (coluna)

data_dict = data.to_dict() # convertendo em dicionário
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

# média
print(data["temp"].mean())

# max valor
print(data["temp"].max())

# obter coluna
print(data["condition"])
# ou 
data.condition
data.day
data.temp

# obtendo dados nas linhas do nosso DataFrame
data[data.day == "Monday"]
data[data.temp == data.temp.max()]

monday = data[data.day == "Monday"]
monday.condition
# temperatura de segunda convertida para F
monday_temp_F = float((monday.temp) * 9/5 + 32)
print(monday_temp_F)

# criando dataframes
data_dictionary = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
new_data = pandas.DataFrame(data_dictionary)
new_data.to_csv("new_data.csv")