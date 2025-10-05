import telebot

from settings import tg_key
from telebot.types import Message

bot = telebot.TeleBot(tg_key)

@bot.message_handler(commands=['search'])
def search(message: Message) -> None:
    bot.send_message(message.from_user.id, "Введите название фильма")
