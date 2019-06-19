import telebot
import conf
from wisdom_generation import generate_wisdom, is_question, not_question
import random
import os
import flask

NOT_QUESTIONS = ['These are not the answers that you seek, acolyte, but rather - action.',
                'Tell me what answers you seek.',
                'Wisdom is to be beseeched for. Ask a question.'
                'You shall not think lightly of the Wisdom I am about to bestow upon you. Ask a question and ponder the answer.']

WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
TOKEN = os.environ['TOKEN']
WEBHOOK_URL_PATH = "/{}/".format(TOKEN)
WEBHOOK_LISTEN = '0.0.0.0'

bot = telebot.TeleBot(TOKEN, threaded=False)

bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)

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

@app.route("/", methods=['GET', 'HEAD'])
def index():
    return 'ok'

@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)

if __name__ == '__main__':
    app.debug = True
    app.run(host=conf.WEBHOOK_HOST, port=conf.WEBHOOK_PORT)
