import telebot
from telebot.types import Message

from settings import tg_key
from tg_API.keyboards.reply import main_keyboard

bot = telebot.TeleBot(tg_key)


@bot.message_handler(commands=["start", "help"])
def start_message(message: Message):
    welcome_text = """
    <b> Добро пожаловать в бот для поиска фильмов!</b>
    <b>Как использовать:</b>
    <b></b>
    1. Нажмите "🎬 Поиск фильмов /search"
    2. Выберите количество результатов
    3. Введите название фильма
    4. Листайте результаты с помощью кнопок
    """
    bot.send_message(
        message.chat.id,
        welcome_text,
        reply_markup=main_keyboard.main_keyboard(),
        parse_mode='HTML'
    )


if __name__ == "__main__":
    bot.infinity_polling()
    start_message()

