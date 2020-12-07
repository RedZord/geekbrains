
sec = int(input('Введите любое кол-во секунд: '))
minute = sec // 60
hour = minute // 60
sec %= 60
minute %= 60
print(f'{hour}:{minute}:{sec}')
