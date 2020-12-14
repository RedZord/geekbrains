
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
