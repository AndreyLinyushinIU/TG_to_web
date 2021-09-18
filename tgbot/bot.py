import telebot

TOKEN = '2018606644:AAHC6DKN8Am7gmCb0XkOtNo-Ae6roPPd8JY'

bot = telebot.TeleBot(TOKEN)

@bot.channel_post_handler(content_types=['text'])
def print_smth(message):
    print(message)

bot.polling()