# Словари

# Создание словаря с помощью {}

empty_dict = {}
print(empty_dict)

bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
}

print(bierce)

lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(lol)
print(dict(lol))

lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print(lot)
print(dict(lot))

tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print(tol)
print(dict(tol))

los = ['ab', 'cd', 'ef']
print(los)
print(dict(los))

tos = ('ab', 'cd', 'ef')
print(tos)
print(dict(tos))

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
print(pythons)
pythons['Gilliam'] = 'Gerry'
print(pythons)
pythons['Gilliam'] = 'Terry'

print(pythons)

'''Помните, что ключи в словаре должны быть уникальными.
Именно поэтому мы в качестве ключей использовали фамилии,
а не имена — двух участников Monty Python зовут Терри.
Если вы применяете ключ более одного раза, победит последнее значение:'''

some_pythons = {
 'Graham': 'Chapman',
 'John': 'Cleese',
 'Eric': 'Idle',
 'Terry': 'Gilliam',
 'Michael': 'Palin',
 'Terry': 'Jones',
 }
print(some_pythons)

# Объединение словарей с помощью функции update()

others = { 'Marx': 'Groucho', 'Howard': 'Moe' }
pythons.update(others)
print(pythons)

# Удаление элементов по их ключу с помощью del
del pythons['Marx']
print(pythons)
del pythons['Howard']
print(pythons)

# Удаление всех элементов с помощью функции clear()
others.clear()
print(others)

# Проверяем на наличие ключа с помощью in
print('Palin' in pythons)
print('Gilliam' in pythons)

# Получение элемента словаря с помощью конструкции [ключ]
print(pythons['Cleese'])
print(pythons.get('John'))
print(pythons.get('John', 'is none'))

# Получение всех ключей с помощью функции keys()
print(pythons.keys())

# Получить список из словаря
print(list(pythons.keys()))

# Получение всех значений с помощью функции values()
print(pythons.values())

# Получение всех пар «ключ — значение» с помощью функции items()
print(pythons.items())

# Присваиваем значения с помощью оператора =, копируем их с помощью функции copy()
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(signals)
original_signals = signals.copy()
signals['blue'] = 'confuse everyone hahaha'
print(signals)
print(original_signals)
