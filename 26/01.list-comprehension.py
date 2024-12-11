# sem list comprehension:
# numbers = [1,2,3] 
# new_list = [] 
# for n in numbers: 
#   add_1 = n + 1 
# new_list.append(add_1)

# com list comprehension:
# numbers = [1,2,3]
# new_list = [n + 1 for n in numbers]]
# [new_item for item in list]

numbers = [1,2,3]
new_numbers = [n + 1 for n in numbers]

name = "Carina"
letters_list = [letter for letter in name]

#  criando uma lista onde cada um dos números de um range(1,5) é o dobro: [2,4,6,8]
# new_list = []
# for n in range(1,5):
#     double_n = n * 2
# new_list.append(double_n)

new_list = [n * 2 for n in range(1,5)]
print(new_list)
