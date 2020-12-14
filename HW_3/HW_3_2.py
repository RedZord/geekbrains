
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
