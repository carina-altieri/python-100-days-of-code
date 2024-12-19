# entendendo como criar funções que podem aceitar qualquer número de argumentos

#def add(*args): * - aceita qualquer número de argumentos
#    for n in args:
#        print(n)

# criando função chamada "add" que aceita quantos números desejar e soma todos os números que são passados pelo input
def add(*args):
    for n in args:
        return(sum(args)) # soma todos os elementos da tupla args

print(add(3, 5, 6, 8, 9)) # args


# Keyword arguments (kwargs) - basicamente dicionários

# def calculate(**kwargs):
  #  print(kwargs)
    # for key, valu in kwargs.items():
        # print(key)
        # print(value)

        # ou:
    # print(kwargs["add"]) # busca e imprime o nome da chave

def calculate(n, **kwargs): # 2 argumentos, sendo um dicionário
    print(kwargs)
    n += kwargs["add"] # n = n + 3: 2 + 3 = 5
    n *= kwargs["multiply"] #  n = n * 5 = 5 * 5 = 25


calculate(2, add=3, multiply=5) # chaves e valores


class Car:

    def __init__(self, **KW):
        self.make = KW["make"] # atributos make e model (marca e modelo) = palavras-chave
        self.model = KW["model"]

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model, my_car.make)      