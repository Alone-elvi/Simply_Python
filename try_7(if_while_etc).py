# while

count = 1
while count <= 5:
    print(count)
    count += 1

# break 

'''while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())
'''

# continue

'''while True:
    value = input('Введите номер пожалуйста [q для выхода]')
    if value == 'q':  # Если введено q, выход
        break
    number = int(value)
    if number % 2 == 0:  # нечетное число
        continue
    print(number, "Квадрат введенного числа", number * number)
'''
# Проверяем, завершился ли цикл заранее, с помощью else

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print("Найдено чётное число", number)
        break
    position += 1
else:
    print("Не найдено чётных чисел")

# Включение
print([number - 2 for number in range(1, 6)])
print([number for number in range(1, 6) if number % 2 == 1])

rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for row, col in cells:
    print(row, col)

# Включение словаря
# { выражение_ключа: выражение_значения for выражение in итерабельный объект }

'''Мы запускаем цикл, проходя по каждой из семи букв в строке letters,
и считаем, сколько раз появляется эта буква.
Два наших вызова word.count(letter) — это лишь пустая трата времени,
поскольку нам нужно подсчитать буквы «e» и «t» два раза.
Но когда мы считаем буквы «e» во второй раз, то не причиняем вреда,
поскольку лишь заменяем уже существующую запись в словаре;
то же относится и к подсчету букв «t».
Следующий способ решения задачи более характерен для Python:'''

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

# Включение множества
# { выражение for выражение in итерабельный объект}

a_set = {number for number in range(1, 6) if number % 3 ==1}
print(a_set)