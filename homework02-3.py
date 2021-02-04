seasons = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
month = abs(int(input('Введите номер месяца от 1 до 12: ')))

if month > 12:
    print('Неверное значение.')
else:
    for season, months in seasons.items():
        if month in months:
            print("Месяц относится ко времени года", season)