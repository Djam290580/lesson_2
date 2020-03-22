# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

words_list = input('Enter word: ')

result = words_list.split()
print(result)

for i in enumerate(result, 1):
    print(i)


for i in range(1, len(result)+1):
    print(i, ')', result[i-1])