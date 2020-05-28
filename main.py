import telebot

Token = ('863654335:AAE3IMFm9TNkshA1p3x0wudg2BmAWbqOfYs')
bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, message.text)


bot.polling()
