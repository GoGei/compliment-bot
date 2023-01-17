import os
import json
import typing
import random
import telebot

try:
    from configs import telegram_settings

    token = telegram_settings.BOT_TOKEN
except Exception:
    token = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(token)

COMMANDS = [
    {
        'command': ('start', 'hello'),
        'description': 'Начать общаться с ботом'
    },
    {
        'command': 'compliment',
        'description': 'Чтобы получить комплимент',
    },
    {
        'command': 'apologize',
        'description': 'Чтобы получить извинения'
    }
]

ALREADY_SEEN_COMPLIMENTS = set()
ALREADY_SEEN_APOLOGIZE = set()
DEFAULT_COMPLIMENT = 'Ты уже получила все комплименты, которые я написал. Новых пока не будет, клацай старые'
DEFAULT_APOLOGIZE = 'Какого хера ты вообще меня завляешь много раз извиняться? Этого было не достаточно?'


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    msg = "Привет. Это твой персональный бот с набором команд, которые он понимает:\n"
    for command_dict in COMMANDS:
        command = command_dict['command']
        description = command_dict['description']
        command_line = '%s - %s\n'

        if isinstance(command, str):
            command = command
        elif isinstance(command, typing.Iterable):
            command = '/'.join(command)
        else:
            command = str(command)

        command_line = command_line % (command, description)
        msg += command_line
    bot.reply_to(message, msg)


@bot.message_handler(commands=['compliment'])
def send_compliment(message):
    filepath = 'files/compliment.json'
    with open(filepath, mode="r", encoding="utf-8") as file:
        compliments = json.load(file)

    global ALREADY_SEEN_COMPLIMENTS
    global DEFAULT_COMPLIMENT

    while True:
        if len(ALREADY_SEEN_COMPLIMENTS) == len(compliments):
            compliment = DEFAULT_COMPLIMENT
            ALREADY_SEEN_COMPLIMENTS = set()
            break

        compliment = random.choice(compliments)
        if compliment not in ALREADY_SEEN_COMPLIMENTS:
            ALREADY_SEEN_COMPLIMENTS.add(compliment)
            break

    bot.reply_to(message, compliment)


@bot.message_handler(commands=['apologize'])
def send_compliment(message):
    filepath = 'files/apologize.json'
    with open(filepath, mode="r", encoding="utf-8") as file:
        apologizes = json.load(file)

    global ALREADY_SEEN_APOLOGIZE
    global DEFAULT_APOLOGIZE

    while True:
        if len(ALREADY_SEEN_APOLOGIZE) == len(apologizes):
            apologize = DEFAULT_APOLOGIZE
            ALREADY_SEEN_APOLOGIZE = set()
            break

        apologize = random.choice(apologizes)
        if apologize not in ALREADY_SEEN_APOLOGIZE:
            ALREADY_SEEN_APOLOGIZE.add(apologize)
            break

    bot.reply_to(message, apologize)


bot.infinity_polling()
