import telebot

Token = ('776550937:AAELEr0c3H6dM-9QnlDD-0Q0Fcd65pPyAiM')
bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


bot.polling()
