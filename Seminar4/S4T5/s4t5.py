# 5 Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import os

def parse_member(member: str):
    s = member.split('*')
    if '' in s:
        s.remove('')
    if 'x' not in s:
        s.append(0)
    if 'x' in s:
        if len(s) == 1:
            s.append(1)
            s.append(1)
        elif len(s) == 2:
            if s.index('x') == 0:
                s.insert(0, 1)
            else:
                s.append(1)
        s.remove('x')
    return s


def parse_members_list(polynome: str):
    members = polynome.split(' + ')
    parse = dict()
    for m in members:
        member = parse_member(m)
        parse[int(member[1])] = int(member[0])
    return parse


def get_member(coeff: int, pow: int):
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


def sum_members(members1: dict, members2: dict):
    members = []
    for k in members2.keys():
        b = members2[k]
        if k in members1.keys():
            a = members1[k]
            members1[k] = (a + b)
        else:
            members1[k] = (b)
    keys = list(members1.keys())
    keys.sort(reverse=True)
    for k in keys:
        members.append(get_member(members1[k], k))
    return members

def load_polynome(filename:str):
    file = open(filename, 'r')
    s = file.read()
    file.close()
    return s

def save_polynome(polynome:str, filename:str):
    file = open(filename, 'w')
    file.write(polynome)
    file.close()
    poly_path = ''
    poly_path = os.path.abspath(poly_path)
    msg = poly_path + '\\' + file.name
    return msg

def main():
    os.system('cls')

    print('Программа загружает два файла с записью многочленов и')
    print('записывает сумму многочленов в отдельный файл (sum_poly.txt)')

    poly1 = load_polynome('poly1.txt')
    poly2 = load_polynome('poly2.txt')

    m1 = parse_members_list(poly1)
    m2 = parse_members_list(poly2)
    sum_mem = sum_members(m1, m2)
    sum_poly = " + ".join(sum_mem)


    print('Сумма многочленов:')
    print(poly1)
    print(poly2)
    print('Равная:')
    print(sum_poly)
    print('Сохранена в файл:', save_polynome(sum_poly, 'sum_poly.txt'))


if __name__ == '__main__':
    main()