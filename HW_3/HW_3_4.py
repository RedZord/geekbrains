
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
