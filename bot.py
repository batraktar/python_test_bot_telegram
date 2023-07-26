import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hello, how are you doing?')


@bot.message_handler(content_types=['text'])
def repeat_text(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
