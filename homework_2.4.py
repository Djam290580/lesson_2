# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

words_list = input('Enter word: ')
results = words_list.split()
print(results)
print()
for i, result in enumerate(results[:10], 1):
    print(i, result[:10])

print()
print()

for i in range(1, len(results)+1):
    print(i, ')', results[i-1])