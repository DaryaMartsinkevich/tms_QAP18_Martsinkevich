# 1 Создать lambda функцию, которая принимает на вход имя и выводит его в формате “Hello, {name}”
pow = lambda n: f'Hello, {n}'
print(pow("Darya"))

# 2 Создать lambda функцию, которая принимает на вход список имен и выводит их в формате “Hello, {name}” в другой список
lst = ['Даша', 'Таня', 'Марина', 'Андрей', 'Вадим']

pow = lambda name: [f'Hello, {name}' for name in lst]
lst2 = pow(lst)

print(lst2)

# 1 Напишите генератор который принимает список
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] и озвращает новый список только с положительными числами
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
def numb_generator(numb):
    for i in numb:
        if i > 0:
            yield i

mygenerator = list(numb_generator(numbers))
print(mygenerator)

for i in mygenerator:
    print(i)

# 2 Необходимо составить список чисел которые указывают на длину слов в строке: sentence = "" thequick brown fox jumps
# over the lazy dog"", но только если слово не ""the"" с обработкой исключений
sentence = "the quick brown fox jumps over the lazy dog"
lst = sentence.split()
lengths = []

for word in lst:
    try:
        if word != "the":
            lengths.append(len(word))
        else:
            raise Exception
    except:
        print("There is the")

print(lengths)
