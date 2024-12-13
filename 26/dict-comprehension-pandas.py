student_dict = {
    "student": ["Carina", "James", "Lili"],
    "score": [86, 74, 98]
}

import pandas
student_data_frame = pandas.DataFrame
(student_dict)
print(student_data_frame)

# método iterrows - nos permite percorrer as linhas do dataframe ao invés da coluna
for (index, row) in student_data_frame.iterrows():
    if row.student == "Carina":
        print(row.score)