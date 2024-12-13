# new_dict ={new_key:new_value for (key,value) in dict.items() if test}

import random
names = ['Alex', 'Beth', 'Caroline', 'Carina', 'Dave', 'Eleanor', 'Fred']
# criando um dicionário que gera uma pontuação aleatória de 1 a 100 para cada um desses nomes
students_score = {student:random.randint(1, 100) for student in names}
passed_students = {student:score for (student,score) in students_score.items() if score >= 60}
print(passed_students)