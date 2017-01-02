# Списки

empty_list = [ ]
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
another_empty_list = list()
print(another_empty_list)
print(first_names)

# Функция list() преобразует другие типы данных в списки. В следующем примере строка преобразуется в список, состоящий из односимвольных строк:

list_cat = list('cat')
print(list_cat)

# В этом примере кортеж (этот тип мы рассмотрим сразу после списков) преобразуется в список:

a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

# Преобразовать строку в список при помощи spit

birthday = '1/6/1952'
print(birthday.split('/'))
# Что, если в оригинальной строке содержится несколько включений строки-разделителя подряд? В этом случае в качестве элемента списка вы получите пустую строку:
splitme = 'a/b//c/d///e'
print(splitme.split('/'))
# Если бы вы использовали разделитель //, состоящий из двух символов, то получили бы следующий результат:
splitme = 'a/b//c/d///e'
print(splitme.split('//'))

# Получение элемента с помощью конструкции [смещение]

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])

print(marxes[-1])
print(marxes[-2])
print(marxes[-3])

# Списки списков

small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]

print(all_birds)

# Добавление в список с помощью append

print(marxes)
marxes.append('Zeppo')
print(marxes)

# Объединяем списки с помощью метода extend() или оператора +=

others = ['Gummo', 'Karl']
marxes.extend(others)

print(marxes)

marxes += others

print(marxes)

marxes.append(others)

print(marxes)

# Добавление элемента с помощью функции insert()

marxes.insert(0, 'Puppo')
print(marxes)

# Удаление заданного элемента с помощью функции del

del marxes[-1]

print(marxes)

'''del является оператором Python,
а не методом списка — нельзя написать marxes[-2].del().
Он похож на противоположную присваиванию (=) операцию:
открепляет имя от объекта Python и может освободить память объекта,
если это имя являлось последней ссылкой на нее.'''

# Удаление элемента по значению c помощью функции remove()

print(marxes)
marxes.remove('Puppo')
print(marxes)

# Получение заданного элемента и его удаление с помощью функции pop()

marxes.pop()
print(marxes)
marxes.pop(1)
print(marxes)

# Определение смещения элемента по значению с помощью функции index()

print(marxes.index('Harpo'))

# Проверка на наличие элемента в списке с помощью оператора in

print("Harpo" in marxes)

# Преобразование списка в строку с помощью функции join()

print(', '.join(marxes))
print(marxes)

# Меняем порядок элементов с помощью функции sort()

sorted_marxes = sorted(marxes)
print(sorted_marxes)
marxes.sort(reverse=True)
print(marxes)

'''Опять же b, c и d являются копиями a — это новые объекты,
имеющие свои значения, не связанные с оригинальным списком объектов
[1, 2, 3], на который ссылается a. Изменение a не повлияет на копии b, c и d:'''

a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]