import os

def get_path():
    return os.path.abspath('')


def is_file_exist(filename):
    try:
        load_txt(filename)
        return True
    except FileNotFoundError:
        return False

# Чтение из файла в массив строк
def load_txt(filename:str):
    file = open(filename, 'r')
    s = file.readlines()
    file.close()
    return s


# Чтение строки из файла
def load_string_txt(filename:str):
    file = open(filename, 'r')
    s = file.readline()
    file.close()
    return s


# Сохранение строки в файл
def update_txt(text:str, filename:str, modifier:str):
    file = open(filename, modifier)
    file.write(text)
    file.close()
    file_path = ''
    file_path = os.path.abspath(file_path)
    msg = file_path + '\\' + file.name
    return msg

# Перезапись файла
