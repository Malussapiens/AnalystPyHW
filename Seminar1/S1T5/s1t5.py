# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# AB = √((X2-X1)²+(Y2-Y1)²) - формула длины отрезка на координатной плоскости

import math


def validate_input(x, y):
    try:
        x = float(x)
        y = float(y)
        return True
    except:
        print('Значение должно быть числом!')
        return False


print('Введите координаты начала отрезка:')
x1, y1 = input('x->'), input('y->')
print('Введите координаты конца отрезка:')
x2, y2 = input('x->'), input('y->')
if validate_input(x1, y1) and validate_input(x2, y2):
    x1, y1 = float(x1), float(y1)
    x2, y2 = float(x2), float(y2)
    length = ((x2-x1)**2+(y2-y1)**2)**0.5
    
    print(f'A ({x1},{y1}); B({x2},{y2}) -> {float("{0:.3f}".format(length))}')
