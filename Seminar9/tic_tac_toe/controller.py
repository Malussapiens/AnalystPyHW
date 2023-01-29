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
    if model.validate_pos(pos) and model.set_table_pos(pos, token):
        return 1
    return -1

def bot_move(token:str):
    field = model.get_table()
    pos = -1
    if field[4] == ' ':
        pos = 5
    if pos == -1:
        for comb in wins:
            if field[comb[0]] == field[comb[1]]:
                if field[comb[0]] != ' ' and field[comb[2]] == ' ':
                    pos = comb[2] + 1
                    break
            elif field[comb[1]] == field[comb[2]]:
                if field[comb[1]] != ' ' and field[comb[0]] == ' ':
                    pos = comb[0] + 1
                    break
            elif field[comb[0]] == field[comb[2]]:
                if field[comb[0]] != ' ' and field[comb[1]] == ' ':
                    pos = comb[1] + 1
                    break
        else:
            for i in '1379':
                if field[int(i) - 1] == ' ':
                    pos = i
                    break
    if pos == -1:
        for i in range(len(field)):
            if field[i] == ' ':
                pos = i + 1
    model.set_table_pos(str(pos), token)

def play_game():
    # Инициализация игры
    # список выигрышных комбинаций
    global wins
    global players
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    players = view.get_player_names(1)
    turn_count = 0

    # бросаем монетку
    coin_toss()

    # сообщаем, кто ходит первым
    view.cls()
    view.show_message(f'Первым ходит {players[val][0]}')
    view.get_user_input('Нажмите Enter....')

    # основной цикл игры
    while turn_count < 9:
        player = players[val][0]
        token = players[val][1]
        draw_field()
        # получаем желаемый ход игрока и проверяем на валидность
        msg = f'{player}, куда поставим {token} (1 - 9)?: '
        if val == 1:
            bot_move(token)
        else:
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

if __name__ == '__main__':
    play_game()
