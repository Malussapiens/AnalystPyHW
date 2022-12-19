# 4. Задайте список из N элементов, заполненных числами
# из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


n = int(input('Введите N: -> '))

my_file = open('file.txt', 'r')
pos = my_file.read()
my_file.close()
pos = list(map(int, pos.split('\n')))

list_n = []
for i in range(-n, n+1):
    list_n.append(i)

print(f'Содержимое файла file.txt: {pos}')
print(f'Массив от -N до N: {list_n}')

prod = 1
for i in pos:
    if i >= len(list_n):
        print("Ошибка! Номер позиции превышает длину списка")
        break
    else:
        prod *= list_n[i]
else:
    print('Позиции нумеруются с 0')
    print(f'Сумма чисел на позициях {pos} равна {prod}')
