8 * 9
47
print(47)
a = 7
print(a)
b = a
print(b)
print(type(a), type(b), type(47), type(99.9), type('Новый год'))

start = 'Na ' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)

todos = 'get gloves,get mask,give cat vitamins,call ambulance'
print(todos.split())

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ',\n '.join(crypto_list)
print('Found and signing book deals:', "\n" + crypto_string)

poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

print(poem, "\n", poem[:13], len(poem))
# Начинается ли стихотворение с буквосочетания All?
print(poem.startswith('All'))
# Заканчивается ли оно буквосочетанием That's all, folks!?
print(poem.endswith('That\'s all, folks!'))
# Найдем смещение первого включения слова the:
word = 'the'
print(poem.find(word))
# А теперь — последнего:
print(poem.rfind(word))
# Сколько раз встречается трехбуквенное сочетание the?
print(poem.count(word))
# Являются ли все символы стихотворения буквами или цифрами? Нет, в стихотворении имеются еще и знаки препинания.
print(poem.isalnum())

# Регистр и выравнивание

# Удалим символ «.» с обоих концов строки:
setup = 'a duck goes into a bar...'
print(setup.strip('.'))

# Напишем первое слово с большой буквы:

print(setup.capitalize())

# Напишем все слова с большой буквы:

print(setup.title())

# Запишем все слова большими буквами:

print(setup.upper())

# Запишем все слова большими буквами:

print(setup.lower())

# Сменим регистры букв:

print(setup.swapcase())

'''Теперь мы поработаем с функциями выравнивания. Строка выравнивается внутри заданного количества пробелов (в данном примере 30).
Отцентруем строку в промежутке из 30 пробелов:'''

print(setup.center(30))

# Выровняем ее по левому краю:

print(setup.ljust(30))

# А теперь по правому:

print(setup.rjust(30))

# Заменяем символы с помощью функции replace()

print(setup.replace("duck", "marmoset"))

# Заменим максимум 100 включений:

print(setup.replace('a ', 'a famous ', 100))
