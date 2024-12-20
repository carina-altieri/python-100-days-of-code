# Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


random_password = ""

for char in range(0, nr_letters):
    random_password += random.choice(letters)

for char in range(0, nr_symbols):
    random_password += random.choice(numbers)

for char in range(0, nr_symbols):
    random_password += random.choice(symbols)

# transformar em lista
random_password_list = list(random_password)
random.shuffle(random_password_list)


# retornar à string e embaralhar os itens

random_password = "".join(random_password_list)

print(f"Your random password: {random_password}")