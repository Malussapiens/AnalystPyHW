import telebot
from telebot import types
import model
import view
from random import randint

bot = telebot.TeleBot("")   # вставьте сюда токен для бота

names = []
tokens = []
wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
val = -1
switch = 0
u_move = ''
turn_count = 0

def restart(message):
    bot.send_message(message.chat.id, 'рестарт')
    global names
    global tokens
    global val
    global switch
    global turn_count
    names = []
    tokens = []
    val = -1
    switch = 0
    turn_count = 0
    model.reset_field()

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

# получает ввод от пользователя
def get_user_move(message):
    bot.send_message(message.chat.id, f'user_move: ход {val}, введено: {message.text}')
    global u_move
    u_move = message.text   #сюда кладем ответ игрока
    if model.validate_pos(u_move):
        model.set_table_pos(u_move, names[val][1])
        switch_players()
        game(message)
    else:
        bot.send_message(message.chat.id, f'Некорректный ход!')
        bot.register_next_step_handler(message, get_user_move)


def bot_move(message):
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
    model.set_table_pos(str(pos), names[val][1])
    bot.send_message(message.chat.id, f'Мой ход: {pos}')
    switch_players()
    game(message)  

# Основной цикл игры
def game(message):
    global turn_count
    bot.send_message(message.chat.id, get_field())
    if not is_win():
        if turn_count < 9:
            if val == 1:
                turn_count += 1
                bot_move(message)
            else:
                bot.send_message(message.chat.id, 'Ваш ход?')
                turn_count += 1
                bot.register_next_step_handler(message, get_user_move)
        else:
            bot.send_message(message.chat.id, 'Ничья!')
    else:
        switch_players()
        bot.send_message(message.chat.id, f'Победил {names[val][0]}')
        bot.send_message(message.chat.id, f'Чтобы сыграть еще раз, введите "play"')

# Запрашивает имена игроков и возвращает массив с именами
def get_player_names(message):   
    global names
    names = [message.from_user.first_name, 'Компьютер']

# жеребьевка
def coin_toss():
    global val
    global switch
    global names
    val = randint(0, 1)
    tokens = ('X', 'O')
    if val == 0:
        switch = 1
    else:
        switch = -1
    names[val] = [names[val], tokens[not switch]]
    names[not val] = [names[not val], tokens[abs(switch)]]

# получает игровое поле
def get_field():
    return view.get_field(model.get_table())

# переключение игроков
def switch_players():
    global val
    global switch
    val += switch
    switch *= -1
    


def option(message):
    if message.text.lower() == 'yes':
        restart(message)   
        get_player_names(message)
        coin_toss()
        bot.send_message(message.chat.id, f'Вам достались {names[0][1]}')
        game(message)
    elif message.text.lower() == 'no':
        bot.send_message(message.chat.id, f'Скучаем...')
    else:
        bot.send_message(message.chat.id, f'Я не понимаю тебя. Давай снова.')

def play_game():
    @bot.message_handler(content_types = ["text"]) # вызов функции если тип сообщения - текст
    def controller(message):
        if message.text.lower() == 'play':
            bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, сыграем в крестики-нолики?')
            bot.register_next_step_handler(message, option)
        else:
            bot.send_message(message.chat.id, f'Напиши play')

    bot.infinity_polling()
