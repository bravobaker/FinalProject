import telebot
import conf
from wisdom_generation import generate_wisdom, is_question, not_question
import random
import os
import flask
import time

NOT_QUESTIONS = ['These are not the answers that you seek, acolyte, but rather - action.',
                'Tell me what answers you seek.',
                'Wisdom is to be beseeched for. Ask a question.'
                'You shall not think lightly of the Wisdom I am about to bestow upon you. Ask a question and ponder the answer.']

TOKEN = os.environ['TOKEN']
WEBHOOK_LISTEN = '0.0.0.0'

WEBHOOK_URL_BASE = "https://%s:%s" % (conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (TOKEN)

bot = telebot.TeleBot(TOKEN, threaded=False)

app = flask.Flask(__name__)


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

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=conf.WEBHOOK_HOST + TOKEN)
return "!", 200

if __name__ == "__main__":
server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
