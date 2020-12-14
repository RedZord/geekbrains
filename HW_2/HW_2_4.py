
#   4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_words = input('Enter a list of words(separated by a space): ').split()

for elem in range(len(user_words)):
    if len(user_words[elem]) > 10:
        tmp = user_words[elem]
        user_words[elem] = tmp[:10]
    print(f'{elem + 1}: {user_words[elem]}')
