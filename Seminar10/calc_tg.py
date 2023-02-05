import telebot
import logger
import datetime as d

bot = telebot.TeleBot('')

a = 0
b = 0
ops_real = ['+', '-', '*', '/', '//', '%', '^']
ops_complex = ops_real[:-3]

def calculate(message):
    log_str = d.datetime.now().strftime('%d-%m-%y,%H:%M:%S') + ',' + str(message.from_user.id)
    if message.text.lower() != 'q':
        expression = message.text.replace('^', '**')
        log_str += f',{expression}'
        try:
            result = eval(expression)
            log_str += f',{result}\n'
            logger.add_log_entry(log_str)
            bot.send_message(message.chat.id, result)
            calc(message)
        except:
            result = 'Ошибка!'
            log_str += f',{result}\n'
            logger.add_log_entry(log_str)
            bot.send_message(message.chat.id, result)
            calc(message)
    else:
        result = 'До свидания!'
        log_str += f',{message.text},{result}\n'
        logger.add_log_entry(log_str)
        bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['calc'])
def calc(message):
    bot.send_message(message.chat.id, 'Вас приветствует калькулятор')
    bot.send_message(message.chat.id, f'знаки операций: {ops_real}')
    bot.send_message(message.chat.id, 'введите выражение (поддерживаются комплексные числа), q - выход')
    bot.register_next_step_handler(message, calculate)
bot.infinity_polling()
