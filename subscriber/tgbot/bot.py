import telebot
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(user='postgres', password='postgres', host='localhost')
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()
TOKEN = '2018606644:AAHC6DKN8Am7gmCb0XkOtNo-Ae6roPPd8JY'

bot = telebot.TeleBot(TOKEN)

@bot.channel_post_handler(content_types=['text'])
def print_smth(message):
    print(message.text)

bot.polling()