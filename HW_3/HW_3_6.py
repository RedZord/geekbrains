
# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских
# букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(str_words):
    words = str_words.split()
    for elem, word in enumerate(words):
        words[elem] = word.capitalize()
    return ' '.join(words)


words = input('Enter words(separated by space): ')
print(f'{int_func(words)}')
