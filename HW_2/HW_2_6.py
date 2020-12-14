
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
