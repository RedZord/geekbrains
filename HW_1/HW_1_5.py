
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

