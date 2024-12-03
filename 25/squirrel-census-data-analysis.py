# quantos esquilos de cada cor existem
# coluna: Primary Fur Color
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")
gray_sq = data[data["Primary Fur Color"] == "Gray"]
cinnamon_sq = data[data["Primary Fur Color"] == "Cinnamon"]
black_sq = data[data["Primary Fur Color"] == "Black"]

# criando novo dataframe
data_dictionary = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(gray_sq), len(cinnamon_sq), len(black_sq)]
}
df = pandas.DataFrame(data_dictionary)
df.to_csv("squirrel_count.csv")