import telebot
from wisdom_generation import generate_wisdom, is_question, not_question
import random
import os

NOT_QUESTIONS = ['These are not the answers that you seek, acolyte, but rather - action.',
                'Tell me what answers you seek.',
                'Wisdom is to be beseeched for. Ask a question.'
                'You shall not think lightly of the Wisdom I am about to bestow upon you. Ask a question and ponder the answer.']

TOKEN = os.environ['TOKEN']

telebot.apihelper.proxy = {'proxy_url':'socks5://geek:socks@t.geekclass.ru:7777'}
bot = telebot.TeleBot(conf.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Greetings, neophite. Thou hast come here to hear of my teachings. Ask me a question, or simply type "/wisdom", and I shall share my wisdom with thou.')

@bot.message_handler(commands=['wisdom'])
def share_wisdom(message):
    bot.send_message(message.chat.id, generate_wisdom())


@bot.message_handler(func=is_question)
def answer_question(message):
    bot.send_message(message.chat.id, generate_wisdom())

@bot.message_handler(func=not_question)
def scorn_insolence(message):
    bot.send_message(message.chat.id, random.choice(NOT_QUESTIONS))

if __name__ == '__main__':
    bot.polling(none_stop=True)
