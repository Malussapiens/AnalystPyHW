# 2 Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from s6t2 import cls, random_list


def main():
    cls()
    print('Программа находит произведение пар чисел списка.')
    print('Парой считаем первый и последний элемент, второй и предпоследний')

    n = int(input('Введите длину списка: '))
    a = 1
    b = 10
    my_list = random_list(n, a, b)

    print(my_list)

    res = list(map(lambda _: my_list.pop() * my_list.pop(0), my_list))
    if len(my_list) > 0:
        res.append(my_list.pop() ** 2)

    print(res)


if __name__ == '__main__':
    main()