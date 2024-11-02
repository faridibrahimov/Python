import telebot
from logic import gen_pass
import time, threading, schedule

TOKEN = "8112721866:AAFumIK75Uao7N3VQnmDKVn-S5wewfwBVik"

bot = telebot.TeleBot(TOKEN)
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я бот,котроый поможет тебе. Напиши /help чтобы увидеть какие команды есть")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Команды: /start, /help, /set(Используй /set <seconds> чтобы установить таймер), /unset ,/pass")

@bot.message_handler(commands=['pass'])
def send_welcome(message):
    bot.send_message(message.chat.id, gen_pass(14))

# @bot.message_handler(content_types=['text'])
# def send_welcome(message):
#     if message.text == 'привет':
#         bot.send_message(message.chat.id, 'Привет')
#     elif message.text == 'пока':
#         bot.send_message(message.chat.id, 'Пока')

def beep(chat_id) -> None:
    """Send the beep message."""
    bot.send_message(chat_id, text='Beep!')


@bot.message_handler(commands=['set'])
def set_timer(message):
    args = message.text.split()
    if len(args) > 1 and args[1].isdigit():
        sec = int(args[1])
        schedule.every(sec).seconds.do(beep, message.chat.id).tag(message.chat.id)
    else:
        bot.reply_to(message, 'Usage: /set <seconds>')


@bot.message_handler(commands=['unset'])
def unset_timer(message):
    schedule.clear(message.chat.id)


if __name__ == '__main__':
    threading.Thread(target=bot.infinity_polling, name='bot_infinity_polling', daemon=True).start()
    while True:
        schedule.run_pending()
        time.sleep(1)

bot.polling()