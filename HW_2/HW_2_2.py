
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

