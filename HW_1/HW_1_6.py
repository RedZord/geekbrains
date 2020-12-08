
curr_distance = int(input('Введите км. 1-ого дня: '))
max_distance = int(input('Введите км. n-ого(крайнего) дня: '))
day = 1

while curr_distance < max_distance:
    day += 1
    curr_distance += curr_distance / 10
print(f'на {day}-й день спортсмен достиг результата — не менее {max_distance} км.')

