name, surname, year_of_birth = input('Введите имя: '), input('Введите фамилию: '), int(input('Введите год рождения: '))
print(name, surname, str(year_of_birth), sep='_')
name, surname = surname, name
print(name, surname, str(int(year_of_birth) + 60), sep='_')