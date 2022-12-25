# 4 Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import os
from random import randint

def get_member(coeff:int, pow:int):
    x = ''
    if coeff == 0:
        return ''
    if pow == 0:
        coeff = str(coeff)
    elif pow > 0:
        if coeff == 1:
            coeff = ''
        else:
            coeff = str(coeff) + '*'
        if pow == 1:
            x = "x"
        else:
            coeff = str(coeff)
            x = 'x**' + str(pow)
    return str(coeff) + x


def get_polynome(pow:int):
    polynome = []
    for _ in range(0, pow + 1):
        coeff = randint(0, 101)
        member = get_member(coeff, pow)
        if member != '':
            polynome.append(member)
        pow -= 1
    return polynome

def save_polynome(polynome:str, filename: str):
    file = open(filename, 'w')
    file.write(polynome)
    file.close()
    poly_path = ''
    poly_path = os.path.abspath(poly_path)
    msg = poly_path + '\\' + file.name
    return msg


os.system('cls')
print('Программа формирует список членов многочлена степени k и записывает их в файл в виде многочлена.')
k = int(input('Введите степень многочлена:'))
polynome = get_polynome(k)

print(f'Список членов многочлена степени {k}:')
print(polynome)
s = ' + '.join(polynome)
print('Многочлен', s)
print('Сохранен в файле:', save_polynome(s, 'polynome.txt'))





    
