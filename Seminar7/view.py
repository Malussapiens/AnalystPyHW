# зададим формат вывода записи (макс. число знаков в поле)

horizontal_line = '-'*114


# Функции вывода информации
def show_horizontal_line():
    print('-'*114)


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
    print(string.strip())


def show_entries(entries:dict, entry_format:tuple):
    for key in entries:
        entry = tuple([key, *entries[key]])
        show_entry(entry, entry_format)


def show_menu(menu_items:list):
    for num, item in enumerate(menu_items, 1):
        print(f'{num} - {item}')

# Функции ввода информации
def get_user_input(prompt:str):
    return input(prompt)
