import os
# import telebot
#
# from utils.choicers import Choicer
# from utils.filereaders import JsonChoicesReader
#
try:
    from configs import telegram_settings

    token = telegram_settings.BOT_TOKEN
except Exception:
    token = os.getenv('BOT_TOKEN')
#
# COMMANDS = {
#     'handle_welcome': {
#         'description': 'Начать общаться с ботом',
#         'decorator_kwargs': {
#             'commands': ['start', 'hello'],
#         }
#     },
#     'handle_compliment': {
#         'description': 'Чтобы получить комплимент',
#         'decorator_kwargs': {
#             'commands': ['compliment'],
#         }
#     },
#     'handle_apologize': {
#         'description': 'Чтобы получить извинения',
#         'decorator_kwargs': {
#             'commands': ['apologize'],
#         }
#     }
# }
#
# bot = telebot.TeleBot(token, parse_mode=None)
# bot.set_webhook()
#
# apologize_choicer = Choicer(
#     choices=JsonChoicesReader(filepath='files/apologize.json').read(),
#     default_msg='Какого хера ты вообще меня завляешь много раз извиняться? Этого было не достаточно?'
# )
# compliment_choicer = Choicer(
#     choices=JsonChoicesReader(filepath='files/compliment.json').read(),
#     default_msg='Ты уже получила все комплименты, которые я написал. Новых пока не будет, клацай старые'
# )
#
#
# @bot.message_handler(**COMMANDS['handle_welcome']['decorator_kwargs'])
# def handle_welcome(message):
#     msg = "Привет. Это твой персональный бот с набором команд, которые он понимает:\n"
#     for command_dict in COMMANDS.values():
#         command = command_dict['decorator_kwargs']['commands']
#         description = command_dict['description']
#         command_line = '%s - %s\n'
#         command = '/'.join(command)
#         command_line = command_line % (command, description)
#         msg += command_line
#
#     bot.reply_to(message, msg)
#
#
# @bot.message_handler(**COMMANDS['handle_apologize']['decorator_kwargs'])
# def handle_apologize(message):
#     bot.reply_to(message, apologize_choicer.get_choice())
#
#
# @bot.message_handler(**COMMANDS['handle_compliment']['decorator_kwargs'])
# def handle_compliment(message):
#     bot.reply_to(message, compliment_choicer.get_choice())
#
#
# bot.infinity_polling(skip_pending=True, restart_on_change=True)

import telebot

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
