# Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from os import system
import random as rnd

def cls():
    system('cls')

def random_list(list_length: int, begin_num: int, end_num: int):
    return [rnd.randint(begin_num, end_num) for _ in range(list_length)]


def main():
    cls()
    print('Программа находит сумму элементов списка, стоящих на нечётной позиции')

    n = 11
    a = 1
    b = 10
    my_list = random_list(n, a, b)

    print(my_list)

    res = sum([v for i, v in enumerate(my_list) if i % 2 > 0])

    print(f'Ответ: {res}')


if __name__ == '__main__':
    main()