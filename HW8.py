# 1 Написать обычную функцию для факториала, генератор и рекурсию. Сравнить их время работы
def factorial(n):
    for i in range(4, n-1):
        if i > 0:
            return i

def factorial_generator(n):
    for i in range(n-1):
        if i > 0:
            yield i

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)


import time

factorial_time = time.time()
factorial(4)

generator_time = time.time()
factorial_generator(4)

recursive_time = time.time()
factorial_recursive(4)

print("Время работы факториала: ", factorial_time)
print("Время работы факториала: ", generator_time)
print("Время работы факториала: ", recursive_time)

# 2 Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:
#
def typed(type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            args1 = []
            for i in args:
                if type == 'str':
                    args1.append(str(i))
                elif type == 'int':
                    args1.append(int(i))
                else:
                    args1.append(i)
            return func(*args1)
        return wrapper
    return decorator

@typed(type = 'str')
def add_two_symbols(a, b):
    return a + b

print(add_two_symbols("3", 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))

@typed(type = 'int')
def add_three_symbols(a, b, с):
    return a + b + с

print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))
print(add_three_symbols(0.1, 0.2, 0.4))

