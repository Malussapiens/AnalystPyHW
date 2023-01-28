import model
import view

full_name = ['Фамилия', 'Имя']

main_menu = ['Добавить студента', 'Предметы', 'Оценки', 'Выход']
# stud_menu = ['Вывести список студентов', , 'Вернуться']
subj_menu = ['Добавить предмет в список', 'Вернуться']
marks_menu = ['Вывести оценки студента по ID', 'Поставить оценку', 'Вернуться']

# подготовка данных
model.load_base()

# получает запись от пользователя
def get_student_entry():
    temp = []
    for name in full_name:
        temp.append(view.get_user_input(name))
    return temp

# добавляет запись о студенте в БД
def add_student_entry():
    model.add_student(tuple(get_student_entry()))
    model.init_student_marks(model.get_stud_id_count())

# выводит запись о студенте на экран
def print_student_entry(id:int):
    view.show_entry(model.get_student_entry(id))

# выводит список всех студентов на экран
def print_students_list():
    for key in model.get_students_keys():
        print_student_entry(int(key))

# выводит список предметов на экран
def print_subjects_list():
    for subj in model.get_subjects_list():
        view.show_message(subj)

# добавляет предмет в список предметов
def add_subject():
    subj = view.get_user_input('Введите название предмета: ')
    model.add_subject(subj)
    for key in model.get_students_keys():
        model.set_subj_to_student(key, subj)

# выводит список оценок студента по предмету на экран
def print_student_marks(student_id):
    view.show_message('')
    print_student_entry(student_id)
    for _, subj, marks in model.get_student_marks(student_id):
        view.show_entry((subj, *marks))
    view.show_message('')

# ставит оценку студенту
def set_student_mark(student_id:int, subj:str, mark:int):
    model.set_student_mark(student_id, subj, mark)

# Возвращает выбор пользователя
def get_user_choice(menu:list):
    user_choice = view.get_user_input(f'Выберите действие (1 - {len(menu)}): ')
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if  0 < user_choice <= len(menu):
            return user_choice
    return -1

# получаем выбор из меню
def get_menu_choice(menu:list):
    view.show_menu(menu)
    user_choice = get_user_choice(menu)
    while user_choice < 1:
        view.show_menu(menu)
        view.show_message('Неверный ввод!')
        user_choice = get_user_choice(menu)
    return user_choice

# инициализируем счетчик id
model.init_stud_id_count()
menu = main_menu
def run():
    while True:
        global menu
        # печатаем список студентов
        print_students_list()
        # Печатаем главное меню и ждем ввода пользователя
        user_choice = get_menu_choice(menu)
        # обрабатываем ввод
        # Главное меню
        if user_choice == 1:
            add_student_entry()
        elif user_choice == 2:
            prev_menu = menu
            menu = subj_menu
            # Меню "Предметы"
            while True:
                print_subjects_list()
                user_choice = get_menu_choice(menu)
                if user_choice == 1:
                    add_subject()
                    # print('Добавляем предмет')
                elif user_choice == 2:
                    menu = prev_menu
                    break
        elif user_choice == 3:
            # Меню "Оценки"
            prev_menu = menu
            menu = marks_menu
            while True:
                print_students_list()
                user_choice = get_menu_choice(menu)
                if user_choice == 1:
                    print_student_marks(int(view.get_user_input('Введите ID студента: ')))
                    view.get_user_input('Нажмите "Enter"...')
                elif user_choice == 2:
                    id = int(view.get_user_input('Введите ID студента: '))
                    print_subjects_list()
                    subj = view.get_user_input('Введите название предмета: ')
                    mark = int(view.get_user_input('Введите оценку: '))
                    set_student_mark(id, subj, mark)
                    print_student_marks(id)
                    view.get_user_input('Нажмите "Enter"...')
                elif user_choice == 3:
                    menu = prev_menu
                    break
        elif user_choice == 4:
            print('Выходим!')
            break
