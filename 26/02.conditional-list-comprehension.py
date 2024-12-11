# new_list = [new_item for item in list if test]
names = ['Alex', 'Beth', 'Caroline', 'Carina', 'Dave', 'Eleanor', 'Fred']
short_names = [name for name in names if len(name) < 5]

upper_long_names = [name.upper() for name in names if len(name) > 5]
print(upper_long_names)