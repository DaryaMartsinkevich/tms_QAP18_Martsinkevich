# 1. Привести к целому типу - 1.6, 2.99
a = 1.6
b = 2.99
print(int(a))
print(int(b))

# 2. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
str = 'www.my_site.com#about'
str_1 = str.replace("#", "/")
print(str_1)

# 3.Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’
str_2 = "stroka"
str_3 = "ing"
result = str_2 + str_3
print(result)

# 4.В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
str_4 = "Ivanou Ivan"
str_5 = str.replace("Ivanou Ivan", "Ivan Ivanou")
print(str_5)

#5. Напишите программу которая удаляет пробел в начале, в конце строки
str_6 = " Welcom "
str_delite = str.strip()
print(str_delite)

# 6. Создайте словарь, связав его с переменной school, и наполните его данными которые бы отражали "\
#  " количество учащихся в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
school = {
    "1a": 28,
    "2a": 24,
    "3a": 15,
    "4a": 20,
    "5a": 22,
    "6a": 24,
    "7a": 26,
    "8a": 18,
    "9a": 19,
    "10a": 21
}
print(school)

# 7.Создайте список и извлеките из него списка второй элемент.
list_family = ["Gena", "Dasha", "Dima", "Ania"]
print(list_family[1])

# 8.Вывести входит ли строка1 в строку2 (пример: employ и employment )
str_7 = "employ"
str_8 = "employment"
prim = str_7 in str_8
print(str_7 in str_8)

# 9.Вывести нужные символы
# x = "My name is Agent Smith"
# print(x[?]) #y
# print(x[?:?:?]) #nesgt
x = "My name is Agent Smith"
print(x[1])
print(x[3:16:3])

# 10. Есть массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число.
o = [1, 5, 2, 9, 2, 9, 1]
y = []

for i in o:
    if o.count(i) == 1:
        y.append(i)
print(y)

