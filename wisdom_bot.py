import telebot
import conf
from wisdom_generation import generate_wisdom, is_question, not_question
import random

NOT_QUESTIONS = ['These are not the answers that you seek, acolyte, but rather - action.',
                'Is this why you here?',
                'You shall not think lightly of the Wisdom I am about to bestow upon you.']



telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}
bot = telebot.TeleBot(conf.TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Greetings, neophite. Thou hast come here to hear of my teachings. Ask me a question, and I shall share my wisdom with thou")

@bot.message_handler(func=lambda m: m.endswith('?'))
def answer_question(message):
    bot.send_message(message.chat.id, generate_wisdom())

@bot.message_handler(func=is_question)
def answer_question(message):
    bot.send_message(message.chat.id, generate_wisdom())

@bot.message_handler(func=not_question)
def scorn_insolence(message):
    bot.send_message(message.chat.id, random.choice(NOT_QUESTIONS))

if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
