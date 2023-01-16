# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Решение:
# Если N делится на 29 без остатка, то второй может гарантировать себе выигрыш, дополняя
# ход противника до 29. Если же N не делится на 29 без остатка, то выигрывает
# первый. Он должен сначала взять столько конфет, каков остаток, а потом
# дополнять ход противника до 29.

from os import system
from random import randint

def pause():
    c = input('Нажмите Enter')


def validate_int(num: str):
    return num.isdigit()


def player_stake():
    stake = ''
    while not validate_int(stake):    
        stake = input(f'Сколько конфет возьмете(1 - {stake_limit})? ->')
    return int(stake)


def bot_stake():
    if candies >= stake_limit:
        stake = randint(1, stake_limit)
    else:
        stake = randint(1, candies)
    print(f'Компьютер берет {stake} конфет.')
    return stake


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


def show_score():
    print(f'На кону {candies} конфет')
    print('СЧЕТ:')
    print(f'{player1_name}: {player1_candies} конфет')
    print(f'{player2_name}: {player2_candies} конфет')



# Выбор кол-ва игроков
# Варианты: 1 игрок (с ботом), 2 игрока
game_mode = 0
while game_mode < 1 or game_mode > 2:
    system('cls')
    print('Сколько человек играет?')
    print('1 - один игрок против компьютера')
    print('2 - два игрока')
    game_mode = input('Ваш выбор (1 или 2)?: ')
    if validate_int(game_mode):
        game_mode = int(game_mode)
    else:
        game_mode = 0

# Знакомимся с игроками
system('cls')
print('Давайте знакомиться!')
player_names = get_player_names(game_mode)
player1_name, player2_name = player_names

# Инициализируем переменные
candies = 58
player1_candies = 0
player2_candies = 0
turn = randint(1, 2)
stake_limit = 28

# Приветствие
print(f'{player1_name}, {player2_name}, давайте сыграем в игру.')
print(f'На столе лежит {candies} конфета. Играют два игрока, делая ход друг после друга.')
print(f'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем {stake_limit} конфет.')
print('Все конфеты оппонента достаются сделавшему последний ход.')
print(f'Первым ходит {player_names[turn - 1]}')
pause()


# основной цикл
while candies > 0:
    system('cls')
    show_score()
    if turn == 1:
        print(f'Ход игрока {player1_name}')
        stake = player_stake()
    else:
        print(f'Ход игрока {player2_name}')
        if game_mode == 1:
            system('cls')
            stake = bot_stake()
            pause()
        else:
            print(stake)
            stake = player_stake()
    
    if stake < 1 or stake > stake_limit or stake > candies:
        print('Недопустимый ход!')
        if stake <= candies:
            print(f'Можно брать от 1 до {stake_limit} конфет')
            c = input('Нажмите любую клавишу')
        else:
            print(f'Можно брать от 1 до {candies} конфет')
            c = input('Нажмите Enter')
    else:
        if turn == 1:
            player1_candies += stake
            turn = 2
        else:
            player2_candies += stake
            turn = 1
        candies -= stake
system('cls')
show_score()

# Определяем победителя
if turn == 2:
    print(f'{player1_name} выиграл!')
else:
    print(f'{player2_name} выиграл!')