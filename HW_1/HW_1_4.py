
user_number = int(input('Введите любое число: '))
max_number = 0

while True:
    tmp = user_number % 10
    user_number //= 10
    if tmp > max_number:
        max_number = tmp
    if user_number < 10:
        print(f'{max_number}')
        break

