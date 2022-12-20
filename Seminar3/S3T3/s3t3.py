# 3 Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from os import system
from random import randint, random


def console_clear():
    system('cls')


def random_list_float(list_length: int, begin_num: int, end_num: int, round_to: int):
    return [round(randint(begin_num, end_num) + random(), round_to) for _ in range(list_length)]


def get_fract(num: float):  # Возвращает дробную часть числа (float)
    num = str(num).split('.')
    res = '0.'
    if int(num[1]) != 0:
        if int(num[0]) < 0:
            res = '-' + res
    res = res + num[1]
    return float(res)


def get_fracts_list(nums: list):    # возвращает список с дробными частями чисел из nums
    fracts = list()
    for num in nums:
        fract = get_fract(num)
        if fract != 0:
            fracts.append(fract)
    return fracts

console_clear()
print('Программа находит разницу между максимальным и минимальным значением')
print('дробной части элементов списка.')
# создаем список длиной 5, заполненный случайными числами от 0 до 10,
# округленными до 2 знаков
nums = random_list_float(5, 0, 10, 2)   

n = list(map(float, nums))
fracts = get_fracts_list(n)
print(f'{nums} -> {max(fracts) - min(fracts)}')
