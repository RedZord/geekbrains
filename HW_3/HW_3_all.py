
#   1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def division(dividend, divider):
    try:
        result = float(dividend) / float(divider)
    except (ValueError, TypeError):
        return 'Incorrect input!'
    except ZeroDivisionError:  # Не знаю как сделать так чтобы оно
        return 'Divider is zero!'  # реагтровало и когда dividend == 0
    return result


dividend = input('Enter dividend: ')
divider = input('Enter divider: ')

print(division(dividend, divider))


# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def info(name, surname, date, city, email, phone):
    return name, surname, date, city, email, phone


# print(' '.join(list(info(name='Stas',
#                         surname='Lukianov',
#                         date='15.06.2000',
#                         city='Podval',
#                         email='comenda@milo.fu',
#                         phone='88005553535'))))


print(' '.join(list(info(name=input("Enter your name: "),  # Сделал через .join(list())
                         surname=input("Enter your surname: "),  # дабы избавиться от кортежа на выводе
                         date=input("Enter your date of birth: "),
                         city=input("Enter your current city: "),
                         email=input("Enter your email: "),
                         phone=input("Enter your phone number: ")))))


# 3. Реализовать функцию my_func(), которая принимает
# три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def my_func(num1, num2, num3):
    result = 0
    try:
        float(num1)
        float(num2)
        float(num3)
    except (ValueError, TypeError):
        return 'Incorrect input!'

    if num1 > num2 or num1 > num3:
        result += num1
        if num2 > num3:
            result += num2
        else:
            result += num3
    else:
        result = num2 + num3
    return result


# num1 = 3
# num2 = 47
# num3 = 3

num1 = input()
num2 = input()
num3 = input()

print(f'{my_func(num1, num2, num3)}')


# 4. Программа принимает действительное положительное число x и
# целое отрицательное число y. Необходимо выполнить возведение
# числа x в степень y. Задание необходимо реализовать в виде функции
# my_func(x, y). При решении задания необходимо обойтись без
# встроенной функции возведения числа в степень.

def exponent(number, power):
    try:
        number = float(number)
        power = int(power)
    except (ValueError, TypeError):
        return 'Incorrect input!'

    tmp = number
    for i in range(power - 1):
        number *= tmp
    return number


# num = 2
# power = 5

num = input('Enter number: ')
power = input('Enter power: ')

print(f'{exponent(num, power)}')


# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом
# и снова нажать Enter. Сумма вновь введенных чисел будет
# добавляться к уже подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def loop_sum():
    sum_nums = 0
    while True:
        str_nums = input('Enter numbers(separated by space): ')
        if str_nums == 'QT':
            return sum_nums
        try:
            list_nums = [float(elem) for elem in str_nums.split()]
        except (TypeError, ValueError):
            return 'Incorrect input!'
        sum_nums += sum(list_nums)


print(loop_sum())


# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских
# букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(str_words):
    words = str_words.split()
    for elem, word in enumerate(words):
        words[elem] = word.capitalize()
    return ' '.join(words)


words = input('Enter words(separated by space): ')
print(f'{int_func(words)}')
