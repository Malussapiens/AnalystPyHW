# 3. Создайте программу для игры в ""Крестики-нолики"".
from random import randint
from os import system


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


def draw_table(table: list):
    print('-' * 13)
    for i in range(9):
        if table[i] == ' ':
            print(f'| {i+1} ', end='')
        else:
            print(f'| {table[i]} ', end='')
        if (i + 1) % 3 == 0:
            print('|')
            print('-' * 13)

def winner():
    for comb in wins:
        streak = ''
        for pos in comb:
            if table[pos] != ' ':
                streak += table[pos]
        if streak == 'XXX':
            return 'X'
        elif streak == 'OOO':
            return 'O'

def is_vacant(position):
    return table[position - 1] == ' '
    

table = [' ' for _ in range(9)]
print(table)
wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
stop = False
player1, player2 = get_player_names(2)

# жеребьевка
tokens = ('X', 'O')
token = randint(0, 1)
system('cls')
if token == 0:
    print(f'Первым ходит игрок {player1}')
    player1 = (player1, 'X')
    player2 = (player2, 'O')
    turn = 1
else:
    print(f'Первым ходит игрок {player2}')
    player2 = (player2, 'X')
    player1 = (player1, 'O')
    turn = 2
turn_count = 0
draw_table(table)
while not stop:
    if turn == 1:
        while True:
            pos = int(input(f'{player1[0]}, куда поставим {player1[1]}?'))
            if is_vacant(pos) and 1 <= pos <= 9:
                break
            else:
                system('cls')
                draw_table(table)
                print('Эта позиция не подходит!')
        token = player1[1]
        turn = 2
    else:
        while True:
            pos = int(input(f'{player2[0]}, куда поставим {player2[1]}?'))
            if is_vacant(pos) and 1 <= pos <= 9:
                break
            else:
                system('cls')
                draw_table(table)
                print('Эта позиция не подходит!')
        token = player2[1]
        turn = 1
    table[pos - 1] = token
    turn_count += 1
    system('cls')
    draw_table(table)
# проверяем на ничью
    if turn_count > 8:
        print('Ничья!')
        stop = True
# проверяем выигрышные комбинации
    if winner() == 'X':
        if player1[1] == 'X':
            print(f'{player1[0]} выиграл!')
        else:
            print(f'{player2[0]} выиграл!')
        stop = True
    elif winner() == 'O':
        if player1[1] == 'O':
            print(f'{player1[0]} выиграл!')
        else:
            print(f'{player2[0]} выиграл!')
        stop = True