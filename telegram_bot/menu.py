from telebot.types import BotCommand, ReplyKeyboardMarkup, KeyboardButton
from .commands import COMMANDS


def set_bot_commands(bot):
    commands = []
    for command, data in COMMANDS.items():
        for c in data['decorator_kwargs']['commands']:
            commands.append(BotCommand(command=c, description=data['description']))
    bot.set_my_commands(commands)


def create_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("/start"))
    markup.add(KeyboardButton("/compliment"), KeyboardButton("/apologize"))
    return markup
