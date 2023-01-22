import view
import model

entry_format = (12, 12, 15, 16, 72)
field_names = ('Фамилия', 'Имя', 'Отчество', 'Телефон', 'Примечание')
entries = []    # сюда будем класть записи из файла БД
base = 'base.txt'   # Имя файла БД


def print_table():
    view.show_head(field_names, entry_format)
    view.show_entries(entries, entry_format)
    view.show_bottom()

def update_table(entry:tuple):
    model.add_entry(base, entry)
    entries.append(entry)

def work():
    # Проверяем наличие файла с БД
    global entries
    if not model.is_base_exist(base):
        print('нашел')
        model.create_base(base) # если не нашли - создаем
    else:
        # иначе - загружаем файл
        entries = model.load_base(base)

    # Печатаем таблицу
    print_table()

    choice = input('Хотите добавить запись? (Да/Нет)')[0].lower()
    if choice == 'д':
        entry = view.get_entry(entry_format, field_names)
        update_table(entry)
        print_table()
        while input('Еще запись? (Да/Нет)')[0].lower() != 'н':
            entry = view.get_entry(entry_format, field_names)
            update_table(entry)
            print_table()
    print('Всего доброго!')

