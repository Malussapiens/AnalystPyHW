import view
import model

entry_format = (5, 12, 12, 15, 16, 60)
field_names = ('id', 'Фамилия', 'Имя', 'Отчество', 'Телефон', 'Примечание')
entries = dict()    # сюда будем класть записи из файла БД
base_filename = 'base.txt'   # Имя файла БД
menu_items = ['Добавить запись', 'Отсортировать по ID', 'Отсортировать по фамилии', 'Выход']

def get_field(field_name:str, field_length:int):
    field = view.get_user_input(f'Введите {field_name} (макс. {field_length} символов)')
    while True:
        if 0 < len(field) <= field_length:
            return field
        else:
            view.show_message('Некорректное значение!')
            field = view.get_user_input(f'Введите {field_name} (макс. {field_length} символов)')


def get_entry():
    entry = []
    for field_name, field_len in zip(field_names[1:], entry_format[1:]):
        entry.append(get_field(field_name, field_len))
    return tuple(entry)


def get_user_choice():
    while True:
        user_choice = view.get_user_input('Выберите действие: ')
        if user_choice.isdigit():
            if int(user_choice) in range(1, len(menu_items) + 1):
                return user_choice
        view.show_message('Неверный ввод! Попробуйте снова.')


def print_table():
    view.show_head(field_names, entry_format)
    view.show_entries(entries, entry_format)
    view.show_bottom()

def update_table(entry:tuple):
    model.add_entry(base_filename, entry)
    entries[model.get_id_count()] = list(entry)

def add_entry():    
        entry = get_entry()
        update_table(entry)

def sort_by_id():
    global entries
    entries = dict(sorted(entries.items()))
    print_table()

def sort_by_lastname():
    global entries
    entries = dict(sorted(entries.items(), key=lambda item: item[1]))
    print_table()

def work():
    # Проверяем наличие файла с БД
    global entries
    if not model.is_base_exist(base_filename): # если не нашли - создаем
        view.show_message('Файл БД не найден! Создаю новую базу.')
        model.create_new_base(base_filename)
    else:
        # иначе - инициализируем счетчик ID и загружаем файл БД
        entries = model.get_base_from_file(base_filename)
        model.init_id_count(entries)

    # Печатаем таблицу
    print_table()
    print(entries)
    # меню работы с таблицей
    while True:
        view.show_menu(menu_items)
        user_choice = get_user_choice()
        if user_choice == '1':
            add_entry()
            print_table()
            while view.get_user_input('Хотите добавить еще одну запись? (Да/Нет)')[0].lower() != 'н':
                add_entry()
                print_table()
        elif user_choice == '2':
            sort_by_id()
        elif user_choice == '3':
            sort_by_lastname()
        elif user_choice == '4':
            print('Выходим')
            break