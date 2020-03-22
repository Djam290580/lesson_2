# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
seasons = {
    '1': 'winter',
    '2': 'winter',
    '12': 'winter',
    '3': 'spring',
    '4': 'spring',
    '5': 'spring',
    '6': 'summer',
    '7': 'summer',
    '8': 'summer',
    '9': 'autumn',
    '10': 'autumn',
    '11': 'autumn'
}

month = input('Enter month:  ')
result = f'"Этот месяц относится к {seasons[month]}'
print(result)

# ------------через list-------------
# winter = ['декабрь','январь', 'февраль']
# spring = ['март', 'апрель', 'май']
# summer = ['июнь', 'июль', 'август']
# autumn = ['сентябрь', 'октябрь', 'ноябрь']
# seasons_1 = [winter, spring, summer, autumn]

month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
month = input('Enter month:  ')
result = f'"Этот месяц относится к {seasons_1[month]}'
print(result)
