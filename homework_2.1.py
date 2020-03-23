# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

empty_list = []
diverse_list = ['Hello', 3, True, 20.1, None, -92, [33, 5], (1, 2), {'a': 111}, {99, 35, 24}]

print(empty_list)
print(type(empty_list))
print()

print(diverse_list[6][1])
print(diverse_list)
print(type(diverse_list))
print()

for i in diverse_list:
    print(type(i))
    print(i)




