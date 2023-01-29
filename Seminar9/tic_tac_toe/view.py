from os import system

def cls():
    system('cls')

# выводит сообщение
def show_message(msg:str):
    print(msg)

# получает ввод от пользователя
def get_user_input(prompt:str):
    return input(prompt)

# рисует игровое поле
def show_field(field:list):
    cls()
    print('-' * 13)
    for i in range(9):
        if field[i] == ' ':
            print(f'| {i+1} ', end='')
        else:
            print(f'| {field[i]} ', end='')
        if (i + 1) % 3 == 0:
            print('|')
            print('-' * 13)

# Запрашивает имена игроков и возвращает массив с именами
def get_player_names(players: int):   
    if players == 1:
        names=['Игрок1', 'Компьютер']
    else:
        names = ['Игрок1', 'Игрок2']
    for i in range(0, players):
        print(f'Привет, {names[i]}, как тебя зовут?')
        player_name = str.strip(input('Введи свое имя: '))
        if player_name != '':
            names[i] = player_name
    return names