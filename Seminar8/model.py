import file_lib
# Файлы БД
stud_file = 'stud.txt'  # Список студентов
subj_file = 'subj.txt'   # Список предметов
marks_file = 'marks.txt' # Список оценок
file_list = (stud_file, subj_file, marks_file)

# список студентов
# {*student_id:[last_name,name]}
students = dict()

stud_id_count = 0

# Список предметов: [name1, name2, ....]
subjects = list()
# subjects = ['Химия', 'Физика', 'Математика']

# Список оценок студентов по предметам
# [(stud_id, subj_name, [marks])]
stud_marks = list()
# stud_marks = [(1, 'Химия', [5, 4, 3, 5]),
            #   (1, 'Математика', [5, 3, 3]),
            #   (2, 'Физика', [5]),
            #   (2, 'Химия', [3])]

# список оценок
# marks = ['1', '2', '3', '4', '5']

# инициализирует новую БД
def init_new_db():
    for file_name in file_list:
        file_lib.update_txt('', file_name, 'w')


# получить значение счетчика student_id
def get_stud_id_count():
    global stud_id_count
    return stud_id_count

# установка значения счетчика student_id
def set_stud_id_count(value:int):
    global stud_id_count
    stud_id_count = value

# инициализация счетчика student_id
def init_stud_id_count():
    keys = list(students.keys())
    if len(keys) > 0:
        set_stud_id_count(max(keys))

# увеличиваем значение счетчика student_id
def inc_stud_id_count():
    set_stud_id_count(get_stud_id_count() + 1)

# получение списка предметов
def get_subjects_list():
    return tuple(subjects)

# добавляет запись о предмете в список предметов и модифицирует файл БД
def add_subject(subj_name:str):
    if subj_name not in subjects:
        subjects.append(subj_name)
        update_db_file_by_list(get_subj_list_as_str(), subj_file)

# возвращает кортеж с данными о студенте (id, имя, фамилия) по id
def get_student_entry(key):
    return tuple([key, *dict.get(students, key)])

# возвращает кортеж кортежей с данными о студентах
def get_students_keys():
    return tuple(students.keys())
    
# добавляет запись о студенте в список студентов и модифицирует файлы БД
def add_student(full_name:tuple): 
    inc_stud_id_count()
    new_stud_id = get_stud_id_count()
    students[new_stud_id] = list(full_name)
    update_db_file(get_student_entry_as_str(get_student_entry(new_stud_id)), stud_file)    # дописываем файл студентов
    
    # print(get_student_entry_as_str(get_student_entry(new_stud_id)))
    # дописываем файл оценок
    
# возвращает список оценок студента по предмету
def get_student_marks(student_id:int):
    return tuple(filter(lambda x: x[0] == student_id, stud_marks))

# проверяет, есть ли предмет в списке оценок студента
def is_subj_in_list(student_id:int, subj:str):
    return len(list(filter(lambda x: x[1] == subj, get_student_marks(student_id)))) > 0

# добавляет предмет в список оценок студента
def set_subj_to_student(stud_id:int, subj:str):
    if not is_subj_in_list(stud_id, subj):
        set_student_mark(stud_id, subj, 0)
        update_db_file_by_list(get_marks_list_as_str(), marks_file)

# Добавляет предметы из списка предметов в список оценок студента
def init_student_marks(stud_id:int):
    for subj in subjects:
        set_subj_to_student(stud_id, subj)

# добавляет оценку в список оценок студента по предмету
def set_student_mark(student_id:int, subj:str, mark:int=0):
    if mark > 0:
        mark = [mark]
    else:
        mark = []
    entry = [student_id, subj, mark]
    # todo: переписать данный блок кода с учетом функции is_subj_in_list()
    index = list(filter(lambda x: x[1][0] == student_id and x[1][1] == subj, enumerate(stud_marks)))
    if len(index)>0:
        if len(mark) > 0:
            stud_marks[index[0][0]][2].append(*mark)
    else:
        stud_marks.append(tuple(entry))
    update_db_file_by_list(get_marks_list_as_str(), marks_file)

# Работа с файлами
# Проверяет есть файл базы в папке
def is_base_exist(filename):
    return file_lib.is_file_exist(filename)

# Создает новый файл БД
def create_new_base(filename:str):
    file_lib.update_txt(filename, 'w')

# дописывает строку в файл БД
def update_db_file(string:str, filename:str):
    file_lib.update_txt(string, filename, 'a')

# записывает список в файл
def update_db_file_by_list(str_list:list, filename:str):
    file_lib.update_txt('', filename, 'w')
    for string in str_list:
        file_lib.update_txt(string + '\n', filename, 'a')

# Формирует строку для записи в файл БД.
# Формат строки в файле: "stud_id, last_name, name"
def get_student_entry_as_str(entry:dict):
    return ','.join(map(str, entry)) + '\n'

# Формирует строку с предметами из списка
def get_subj_list_as_str():
    return subjects

# Формирует строку с оценками из списка
# Формат строки: "stud_id, subj_name, [marks]"
def get_marks_list_as_str() -> list:
    marks = []
    for entry in stud_marks:
        marks.append(','.join(map(str, entry)))
    return marks

# Формирует список студентов из файла
def get_students_from_file(file_name:str) -> dict:
    global students
    students_txt = file_lib.load_txt(file_name)
    for entry in students_txt:
        entry = entry.strip().split(',')
        key = int(entry.pop(0))
        students[key] = entry

# Получает список предметов из файла
def get_subjects_from_file(file_name:str):
    global subjects
    subjects =  [string.strip() for string in file_lib.load_txt(file_name)]
# [(stud_id, subj_name, [marks])]
# Получает список оценок из файла
def get_marks_from_file(file_name:str):
    global stud_marks
    mrks = list(e.strip().split(',', 2) for e in file_lib.load_txt(file_name))
    # stud_marks = [(int(e1), e2, list(map(int,e3[1:-1].split(',')))) ]
    for (e1, e2, e3) in mrks:
        e3 = e3[1:-1]
        print(e3)
        if len(e3)>0:
            stud_marks.append((int(e1), e2, list(map(int, e3.split(',')))))
        else:
            stud_marks.append((int(e1), e2, list()))
def load_base():
    get_students_from_file(stud_file)
    get_subjects_from_file(subj_file)
    get_marks_from_file(marks_file)




