# Множества

empty_set = set()
print(empty_set)
set()
even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)
odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers)

# Преобразование других типов данных с помощью функции set()
print(set('letters'))

# Создадим множество из списка
print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))
# А теперь из кортежа
print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother')))
# Когда вы передаете функции set() словарь, она возвращает только ключи
print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))

'''Проверяем на наличие значения с помощью ключевого слова in'''
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print('+' + name)

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print('++' + name)
'''Комбинации и операторы

Что, если вам нужно проверить наличие сразу нескольких значений множества?
Предположим, вы хотите найти любой напиток, содержащий апельсиновый сок или вермут.
Для этого мы используем оператор пересечения множеств (&):'''

for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']

'''Пересечение множеств (члены обоих множеств)
можно получить с помощью особого пунктуационного
символа & или функции множества intersection()'''

print(bruss & wruss)
print(bruss.intersection(wruss))

'''В этом примере мы получаем объединение (члены обоих множеств),
используя оператор | или функцию множества union()'''

print(bruss | wruss)
print(bruss.union(wruss))

'''Разность множеств (члены только первого множества, но не второго)
можно получить с помощью символа – или функции difference()'''

print(wruss - bruss)
print(wruss.difference(bruss))

'''Для выполнения исключающего ИЛИ
(элементы или первого, или второго множества, но не общие)
используйте оператор ^ или функцию symmetric_difference():'''

print(bruss ^ wruss)
print(bruss.symmetric_difference(wruss))

'''Вы можете проверить, является ли одно множество подмножеством другого
(все члены первого множества являются членами второго),
с помощью оператора <= или функции issubset()'''

print(bruss <= wruss)
print(bruss.issubset(wruss))


'''Для того чтобы стать собственным подмножеством,
второе множество должно содержать все члены первого и несколько других.
Определяется это с помощью оператора <'''

print(bruss < wruss)

'''Множество множеств противоположно подмножеству
(все члены второго множества являются также членами первого).
Для определения этого используется оператор >= или функция issuperset()'''

print(wruss >= bruss)
print(wruss.issuperset(bruss))

'''И наконец, вы можете найти собственное множество множеств
(первое множество содержит все члены второго и несколько других) с помощью оператора >'''

print(wruss > bruss)



