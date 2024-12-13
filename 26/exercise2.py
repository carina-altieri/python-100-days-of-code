# criar um dicionário chamado weather_f que pega cada temperatura em graus Celsius e converte em Fahrenheit
# (temp_c * 9/5) + 32 = temp_f

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
temp_c = (weather_c.values())
weather_f = {day:(temp_c * 9/5 + 32) for (day,temp_c) in weather_c.items()}
print(weather_f)
