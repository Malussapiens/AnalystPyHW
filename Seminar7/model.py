import file_lib


def is_base_exist(filename):
    return file_lib.is_file_exist(filename)


def create_base(filename:str):
    file_lib.save_txt('', filename, 'w')


def add_entry(filename:str, entry:tuple):
    entry = ','.join(entry) + '\n'
    file_lib.save_txt(entry, filename, 'a')


def get_entry(entry:str):
    return tuple(entry.split(','))


def load_base(filename:str):
    raw_base = file_lib.load_txt(filename)
    base = []
    for entry in raw_base:
        base.append(get_entry(entry.strip()))
    return base
