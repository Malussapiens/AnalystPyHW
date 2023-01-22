# зададим формат вывода записи (макс. число знаков в поле)

horizontal_line = '-'*127


# Функции вывода информации
def show_horizontal_line():
    print('-'*127)


def show_head(head_entry:tuple, entry_format:tuple):
    show_horizontal_line()
    show_entry(head_entry, entry_format)
    show_horizontal_line()


def show_bottom():
    show_horizontal_line()


def show_message(msg:str):
    print(msg)


def show_entry(entry:tuple, entry_format:tuple):
    string = ''
    for n, e in enumerate(entry):
        string += str(e).ljust(entry_format[n], ' ')
    print(string)


def show_entries(entries:list, entry_format:tuple):
    for entry in entries:
        show_entry(entry, entry_format)

# Функции ввода информации
def get_field(field_name:str, field_length:int):
    field = input(f'Введите {field_name} (макс. {field_length} символов)')
    while True:
        if 0 < len(field) <= field_length:
            return field
        else:
            print('Некорректное значение!')
            field = input(f'Введите {field_name} (макс. {field_length} символов)')


def get_entry(entry_format, field_names):
    entry = []
    for name, len in zip(field_names, entry_format):
        entry.append(get_field(name, len))
    return tuple(entry)