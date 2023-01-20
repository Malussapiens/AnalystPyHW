# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# AB = √((X2-X1)²+(Y2-Y1)²) - формула длины отрезка на координатной плоскости

import math
from os import system


def get_coords():
    return tuple(map(int, (input('x-> '), input('y-> '))))


def get_segment():
    segment = dict()
    print('Введите координаты начала отрезка:')
    segment['A'] = get_coords()
    print('Введите координаты конца отрезка:')
    segment['B'] = get_coords()
    return segment

def main():
    system('cls')

    segment = get_segment()
    x1, y1 = segment['A']
    x2, y2 = segment['B']
    length = ((x2-x1)**2+(y2-y1)**2)**0.5

    print(f'A ({x1},{y1}); B({x2},{y2}) -> {float("{0:.2f}".format(length))}')

if __name__ == '__main__':
    main()