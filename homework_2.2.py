# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

friends = ()
name = input('Введите имена друзей: ')
friends = name
print(friends)
friends[0], friends[2] = friends[1], friends[3]
print(list(friends))

for i in friends:
    print(i)




# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# first_names = ['Максим', 'Иван', 'Петр', 'Владимир', 'Андрей']
# print(weekdays.index('Thursday'))
# weekdays.extend(first_names)
# print(weekdays)
# weekdays[0] = 'Tuesday'
# weekdays[1] = 'Monday'
# weekdays[2] = 'Thursday'
# weekdays[3] = 'Wednesday'
# weekdays[4] = 'Максим'
# weekdays[5] = 'Friday'
# weekdays[6] = 'Петр'
# weekdays[7] = 'Иван'
# weekdays[8] = 'Андрей'
# weekdays[9] = 'Владимир'
# print(weekdays)
