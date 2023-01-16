import os

def load_txt(filename:str):
    file = open(filename, 'r')
    s = file.read()
    file.close()
    return s

def save_txt(text:str, filename:str):
    file = open(filename, 'w')
    file.write(text)
    file.close()
    file_path = ''
    file_path = os.path.abspath(file_path)
    msg = file_path + '\\' + file.name
    return msg