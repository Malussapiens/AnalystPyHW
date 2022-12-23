# Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from os import system
import random as rnd

def console_clear():
    system('cls')

def random_list(list_length: int, begin_num: int, end_num: int):
    return [rnd.randint(begin_num, end_num) for _ in range(list_length)]


def sum_of_odd_elements(elements: list):    # решение через цикл
    summ = 0
    for i in range(1, n, 2):
        summ += my_list[i]
    return summ


console_clear()
print('Программа находит сумму элементов списка, стоящих на нечётной позиции')
n = 11
a = 1
b = 10
my_list = random_list(n, a, b)
print(my_list)
print(f'Ответ: {sum_of_odd_elements(my_list)}')
# print(sum(my_list[1::2])) #решение через срез