
# Task 1

a = 43
b = 'Dude'
c = False

print(f'{a}, {b}, {c}.')

number = int(input('Введите любое число: '))
string = input('Введите любое число: ')

print(f'{number}, {string}.')

# Task 2

sec = int(input('Введите любое кол-во секунд: '))
minute = sec // 60
hour = minute // 60
sec %= 60
minute %= 60
print(f'{hour}:{minute}:{sec}')

# Task 3

n = input('Введите любое число: ')
n = int(n) + int(n*2) + int(n*3)
print(n)

# Task 4

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

# Task 5

income = int(input('Введите сумму дохода: '))
consump = int(input('Введите сумму расхода: '))

if income > consum:
    print(f'Вы работаете в прибыль!')
    workers = int(input('Введите количество работников: '))
    profit = income - consum
    profitability = profit / income
    profit_worker = profit / workers
    print(f'Прибыль: {profit},\nРентабельность выручки: {profitability},'
          f'\nПрибыль фирмы на одного рабочего: {profit_worker}.')
else:
    print(f'Вы работаете в убыток!!!')

# Task 6

curr_distance = int(input('Введите км. 1-ого дня: '))
max_distance = int(input('Введите км. n-ого(крайнего) дня: '))
day = 1

while curr_distance < max_distance:
    day += 1
    curr_distance += curr_distance / 10
print(f'на {day}-й день спортсмен достиг результата — не менее {max_distance} км.')
