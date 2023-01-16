# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Кодировка данных.
# [T|L], где T — тип последовательности (0 - одиночные символы), а L — длина.
# Если последовательность одинаковых символов, то T не ставим.
# не удалось реализовать алгоритм, работающий с числами и буквами одновременно

import file_lib

def rle_encode(text: str):
    x = 0
    sym_str = ''
    code_str = ''
    if len(src_str) > 1:
        i = 1
        while i <= len(src_str):
            prev_c = src_str[i - 1]
            count = 1
            j = i
            while j < len(src_str) and src_str[j] == prev_c:
                count += 1
                j += 1
            if count == 1:
                x += count
                sym_str = sym_str + prev_c
            else:
                if x > 0:
                    code_str+=f'0{str(x)}{sym_str}'
                    x = 0
                    sym_str = ''
                code_str+=f'{str(count)}{prev_c}'
            i = j
            i += 1
    if x > 0:
        code_str += f'0{str(x)}{sym_str}'
    return code_str


def rle_decode(text: str):
    n = ''
    t = ''
    i = 0
    while i < len(text):
        j = i
        while text[j].isdigit():
            n += text[j]
            j += 1
        if len(n):
            if n[0] != '0':
                t += text[j] * int(n)
            else:
                for k in range(int(n[1:])):
                    t += text[j + k]
            n = ''
        i = j
        i += 1
    return t


src_str = file_lib.load_txt('src_str.txt')
print(f'Исходная строка: {src_str}', len(src_str))

code_str = rle_encode(src_str)
print(f'Закодированная строка: {code_str}', len(code_str))
print(f'Закодированная строка сохранена по пути {file_lib.save_txt(code_str, "code_str.txt")}')

load_str = file_lib.load_txt('code_str.txt')
decode_str = rle_decode(load_str)
print(f'Декодированная строка: {decode_str}')
print(f'Совпадение строк: {src_str == decode_str}')