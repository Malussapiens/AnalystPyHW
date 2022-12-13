# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

def validate_input(string):
    if string in ('1', '2', '3', '4'):
        return True
    return False


print('Программa по заданному номеру четверти показывает')
print('диапазон возможных координат точек в этой четверти (x и y).')
values = ['x>0; y>0', 'x<0; y>0', 'x<0; y<0', 'x>0; y<0']
quadrant = input('Введите номер четверти (1 - 4):->')
if validate_input(quadrant):
    print(values[int(quadrant)-1])
else:
    print('Введите число от 1 до 4!')
