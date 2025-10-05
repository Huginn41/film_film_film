import telebot
from telebot.types import Message

from settings import tg_key

from tg_API.keyboards.reply import search_menu

bot = telebot.TeleBot(tg_key)


@bot.message_handler(commands=['search'])
def search(message: Message) -> None:
    bot.send_message(message.from_user.id, "Введите название фильма")
