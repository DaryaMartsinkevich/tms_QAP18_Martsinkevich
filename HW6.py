# 1 Дан файл целых чисел, содержащий не менее четырех элементов. Вывести первый, второй, предпоследний
# и последний элементы данного файла. Если чисел меньше 3 выводить ошибку.
def work_file(numb):
    with open('numb1.txt', 'r') as file:
        numb = file.read().split()

    if len(numb) < 3:
        print('Error')

    else:
        print(numb[0], numb[1], numb[-2], numb[-1])

work_file("numb1.txt")

# 2 Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить
# пустым.

def work_file2(numb):
    with open('numb1.txt', 'r') as file:
        numb = file.read().split()

    f1 = open('numb_even.txt', 'w')
    f2 = open('numb_odd.txt', 'w')

    for i in numb:
        if int(i) % 2 == 0:
            f1.write(i + ' ')
        else:
            f2.write(i + ' ')

    f1.close()
    f2.close()

work_file2("numb1.txt")

# 3 Дан файл вещественных чисел. Заменить в нем все элементы на их
# квадраты.

def work_file3(numb):
    with open('numb1.txt', 'r') as file:
        numb = file.read().split()

    f = open('squares.txt', 'w')

    squar_numb = [float(i) ** 2 for i in numb]

    for i in squar_numb:
        f.write(str(i) + "\n")

    f.close()

work_file3('numb1.txt')

# 4 Даны два файла произвольного типа. Поменять местами их
# содержимое. Файлы должны быть бинарного типа
s = '10, 9, 8, 7, 6'
t = '5, 4, 3, 2, 1'

f = open('numb_bin1.bin', 'wb')
f.write(s.encode('utf-8'))
f.close()

f1 = open('numb_bin2.bin', 'wb')
f1.write(t.encode('utf-8'))
f1.close()

def bin_files(numb_bin1, numb_bin2):
    with open(numb_bin1, 'rb') as file1:
        data1 = file1.read()
    with open(numb_bin2, 'rb') as file2:
        data2 = file2.read()

    with open('numb_bin1.bin', 'wb') as file1:
        file1.write(data2)
    with open('numb_bin2.bin', 'wb') as file2:
        file2.write(data1)

bin_files('numb_bin1.bin', 'numb_bin2.bin')