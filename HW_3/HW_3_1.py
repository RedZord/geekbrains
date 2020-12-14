
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
