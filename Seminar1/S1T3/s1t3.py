# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def validate_input(x, y):
    try:
        x = float(x)
        y = float(y)
        return True
    except:
        print('Значение должно быть числом!')
        return False


def print_quadrant(x, y):
    print(f'x={x}; y={y}', sep=';', end=' -> ')
    if x == 0 and y == 0:
        print('Точка лежит в начале координат')
        return
    if x == 0:
        print('Точка лежит на оси X')
    if y == 0:
        print('Точка лежит на оси Y')
    if x > 0 and y > 0:
        print('1')
    if x < 0 and y > 0:
        print('2')
    if x < 0 and y < 0:
        print('3')
    if x > 0 and y < 0:
        print('4')


x, y = input('Введите x->'), input('Введите y->')
if validate_input(x, y):
    print_quadrant(float(x), float(y))
