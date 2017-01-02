# Кортежи

# Создание кортежей с помощью оператора ()

empty_tuple = ()
print(empty_tuple)

# Чтобы создать кортеж, содержащий один элемент или более, ставьте после каждого элемента запятую.

one_marx = 'Groucho',
print(one_marx)

# Если в вашем кортеже более одного элемента, ставьте запятую после каждого из них, кроме последнего
marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)
a, b, c = marx_tuple
print(a)
print(b)
print(c)

'''Вы можете использовать кортежи, чтобы обменять значения с помощью одного выражения,
без применения временной переменной'''

password = 'swordfish'
icecream = 'tuttifrutti'
print(password, icecream)
password, icecream = icecream, password
print(password, icecream)

# Функция преобразования tuple() создает кортежи из других объектов

marx_list = ['Groucho', 'Chico', 'Harpo']
tuple_list = tuple(marx_list)
print(tuple_list)