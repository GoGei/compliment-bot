import os
import telebot

from utils.choicers import Choicer
from utils.filereaders import JsonChoicesReader
from utils.utils import (
    reset_user_limits,
    MAX_APOLOGIES_PER_DAY, MAX_COMPLIMENTS_PER_DAY
)
from telegram_bot import menu
from telegram_bot.commands import COMMANDS

try:
    from configs import telegram_settings

    token = telegram_settings.BOT_TOKEN
except Exception:
    token = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(token, parse_mode=None)
bot.set_webhook()

apologize_choicer = Choicer(
    stats_key='apologies',
    day_limit=MAX_APOLOGIES_PER_DAY,
    with_repeat=False,
    choices=JsonChoicesReader(filepath='files/apologize.json').read(),
    default_msg='Я уже извинился всеми доступными мне способами!',
    limited_msg='Какого хера ты вообще меня заставляешь много раз извиняться? Этого было не достаточно?'
)
compliment_choicer = Choicer(
    stats_key='compliments',
    day_limit=MAX_COMPLIMENTS_PER_DAY,
    with_repeat=False,
    choices=JsonChoicesReader(filepath='files/compliment.json').read(),
    default_msg='Ты уже получила все комплименты, которые я написал. Новых пока не будет, клацай старые.',
    limited_msg='Для того, чтобы получить сегодня новые комплименты, нужно написать мне или приди уже ко мне лично!'
)


@bot.message_handler(**COMMANDS['handle_welcome']['decorator_kwargs'])
def handle_welcome(message):
    msg = "Привет. Это твой персональный бот с набором команд, которые он понимает:\n"
    for command_dict in COMMANDS.values():
        command = command_dict['decorator_kwargs']['commands']
        description = command_dict['description']
        command_line = '%s - %s\n'
        command = '/'.join(command)
        command_line = command_line % (command, description)
        msg += command_line
    msg += f'\nВ день ты можешь получит не больше {MAX_COMPLIMENTS_PER_DAY} комплиментов и {MAX_APOLOGIES_PER_DAY} извинений.'
    bot.reply_to(message, msg, reply_markup=menu.create_main_menu())


@bot.message_handler(**COMMANDS['handle_apologize']['decorator_kwargs'])
def handle_apologize(message):
    trusted_nicknames_presented = bool(telegram_settings.BOT_TRUSTED_NICKNAMES)
    user_is_trusted = message.from_user.username in telegram_settings.BOT_TRUSTED_NICKNAMES
    if (trusted_nicknames_presented and user_is_trusted) or (trusted_nicknames_presented is False):
        user_id = message.from_user.id
        bot.reply_to(message, apologize_choicer.get_limited_choice(user_id))
    else:
        bot.reply_to(message, 'Я не понял, а ты ещё кто?')


@bot.message_handler(**COMMANDS['handle_compliment']['decorator_kwargs'])
def handle_compliment(message):
    trusted_nicknames_presented = bool(telegram_settings.BOT_TRUSTED_NICKNAMES)
    user_is_trusted = message.from_user.username in telegram_settings.BOT_TRUSTED_NICKNAMES
    if (trusted_nicknames_presented and user_is_trusted) or (trusted_nicknames_presented is False):
        user_id = message.from_user.id
        bot.reply_to(message, compliment_choicer.get_limited_choice(user_id))
    else:
        bot.reply_to(message, 'Я не понял, а ты ещё кто?')


reset_user_limits()
menu.set_bot_commands(bot=bot)
bot.infinity_polling(skip_pending=True)
