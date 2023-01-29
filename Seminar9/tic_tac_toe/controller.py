# 3. Создайте программу для игры в ""Крестики-нолики"".
import view
import model
from random import randint

def draw_field():
    view.show_field(model.get_table())

# определяет победителя
def is_win():
    for comb in wins:
        streak = ''
        for pos in comb:
            if model.get_table()[pos] != ' ':
                streak += model.get_table()[pos]
        if streak == 'XXX' or streak == 'OOO':
            return True
    return False

# жеребьевка
def coin_toss():
    global val
    global switch
    val = randint(0, 1)
    tokens = ('X', 'O')
    if val == 0:
        switch = 1
    else:
        switch = -1
    players[val] = [players[val], tokens[not switch]]
    players[not val] = [players[not val], tokens[abs(switch)]]

# переключение игроков
def switch_players():
    global val
    global switch
    val += switch
    switch *= -1

def player_move(pos, token:str):
    if model.set_table_pos(pos, token):
        return 1
    return -1

# Инициализация игры
# список выигрышных комбинаций
wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
players = view.get_player_names(2)

def play_game():
    turn_count = 0

    # бросаем монетку
    coin_toss()

    # начинаем
    view.cls()
    view.show_message(f'Первым ходит {players[val][0]}')
    view.get_user_input('Нажмите Enter....')

    while turn_count < 9:
        player = players[val][0]
        token = players[val][1]
        draw_field()
        # получаем желаемый ход игрока и проверяем на валидность
        msg = f'{player}, куда поставим {token} (1 - 9)?: '
        while player_move(view.get_user_input(msg), token) < 0:
            draw_field()
            view.show_message('Неверный ввод! Введите число от 1 до 9.')    
        # проверяем не достигнута ли победа
        if is_win():
            draw_field()
            # поздравляем победителя
            view.show_message(f'Победил {player}!')
            break
        switch_players()
        turn_count += 1
    # если сделано 9 ходов, значит, ничья
    else:
        draw_field()
        view.show_message('Ничья!')
