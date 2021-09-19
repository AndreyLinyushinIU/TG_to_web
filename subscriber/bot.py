import telebot
#from models import User

TOKEN = '2018606644:AAHC6DKN8Am7gmCb0XkOtNo-Ae6roPPd8JY'

bot = telebot.TeleBot(TOKEN)

@bot.channel_post_handler(content_types=['text'])
def print_smth(message):
    #User.objects.all() get all records
    #User.objects.filter(usr = 'Andruxa') is a select statement
    print(message.text)

bot.polling()