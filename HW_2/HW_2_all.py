
#   1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

data_list = [123, 14.53, 'Hello', 3 + 4j, True,
             [1, 'b'], {'name': 'Stas', 'age': 20}
             ]

for elem in range(len(data_list)):
    print(f'{data_list[elem]} is {type(data_list[elem])}')


#   2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

user_list = input('Enter a list of items(separated by a space): ').split()
elem = 0

while elem < len(user_list) - len(user_list) % 2:
    user_list[elem], user_list[elem + 1] = user_list[elem + 1], user_list[elem]
    elem += 2
print(f'{" ".join(user_list)}')


#   3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

user_month = int(input('Enter month number: '))
months_directory = {
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Autumn',
    10: 'Autumn',
    11: 'Autumn',
    12: 'Winter'
}

months_list = [
    'Winter', 'Winter', 'Spring',
    'Spring', 'Spring', 'Summer',
    'Summer', 'Summer', 'Autumn',
    'Autumn', 'Autumn', 'Winter'
]

print(f'This {months_directory[user_month]} (from directory)')
print(f'This {months_list[user_month - 1]} (from list)')


#   4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_words = input('Enter a list of words(separated by a space): ').split()

for elem in range(len(user_words)):
    if len(user_words[elem]) > 10:
        tmp = user_words[elem]
        user_words[elem] = tmp[:10]
    print(f'{elem + 1}: {user_words[elem]}')


#   5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2, int(input('Enter a number: '))]

for i in range(len(my_list) - 1):
    for j in range(len(my_list) - i - 1):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

my_list.reverse()
print(f'{" ".join([str(i) for i in my_list])}')


#  6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

goods = []
names = []
prices = []
currency = []
quantity = []
units = []

while True:
    add = input('Add product?(y/n): ')
    if add == 'y':
        good = len(goods) + 1, dict(name=input('Product name?: '),
                                    price=input('Price of product?: '),
                                    currency=input('What currency?: '),
                                    quantity=input('Quantity of goods?: '),
                                    unit=input('What units?: '))
        goods.append(good)
    elif add == 'n':
        break
    else:
        print(f'Incorrect answer!')

for product in goods:
    product_data = product[1]
    names.append(product_data['name'])
    prices.append(product_data['price'])
    currency.append(product_data['currency'])
    quantity.append(product_data['quantity'])
    units.append(product_data['unit'])

product_analytics = dict(name=names,
                         price=prices,
                         currency=currency,
                         quantity=quantity,
                         unit=units)

print(f'{product_analytics}')
