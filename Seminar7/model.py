import file_lib
id_count = 0

def is_base_exist(filename):
    return file_lib.is_file_exist(filename)


def create_new_base(filename:str):
    set_id_count(0)
    file_lib.update_txt(str(id_count) + '\n', filename, 'w')


def set_id_count(value:int):
    global id_count
    id_count = value


def get_id_count():
    return id_count

def init_id_count(base:dict):
    keys = list(base.keys())
    if len(keys) > 0:
        set_id_count(max(keys))


def inc_id_count():
    count = id_count + 1
    set_id_count(count)


def add_entry(filename:str, entry:tuple):
    inc_id_count()
    entry = str(id_count) + ':' + ','.join(entry) + '\n'
    file_lib.update_txt(entry, filename, 'a')


def get_entry(entry:str):
    return entry.split(',')

# Формат записи базы:
# {id:[фамилия, имя, отчество, телефон, примечание]}
def get_base_from_file(filename:str):
    raw_base = file_lib.load_txt(filename)
    base = dict()
    for entry in raw_base:
        if ':' in entry:
            key = entry[:entry.index(':')]
            base[int(key)] = (get_entry(entry.removeprefix(key + ':').strip()))
    return base
