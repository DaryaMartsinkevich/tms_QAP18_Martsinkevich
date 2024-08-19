# 1 Напишите функцию is_year_leap, которая принимает число (год) и возвращает true, если год високосный false если нет.

def is_year_leap(year):
    if year % 4 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 400 != 0:
        return False
    else:
        return False

print(is_year_leap((2024)))

# 2 Напишите функцию generate_natural_cubes(n), которая принимает число n и возвращает список, состоящий из кубов
# первых n натуральных чисел. То есть [1**3, 2**3, 3**3, ..., n**3]. Обязательно использование генераторов списков.

def generate_natural_cubes(n):
    return [i ** 3 for i in range(1, n+1)]

print(generate_natural_cubes(6))

# 3 Напишите функцию generate_squares, которая принимает произвольное количество аргументов и возвращает список,
# состоящий из их квадратов.То есть generate_squares(1, 2, 3) -> [1, 4, 9]

def generate_squares(*args):
    return [i * i for i in args]

print(generate_squares(1, 2, 3))

# 4 Напишите функцию get_longest_word, которая на вход принимает текст (только английские слова и пробелы), и
# возвращает самое длинное слово из этого текста. Для разбиения строки на слова используйте функцию split.

def get_longest_word(text):
    word = text.split()
    return max(word, key = len)

text = "I don't understand anything, but everything is very interesting"
print(get_longest_word(text))



