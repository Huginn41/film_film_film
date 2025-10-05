from telebot import types


def search_keyboard():
    """Клавиатура главного меню"""
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="🔄 Найти другой"))
    keyboard.add(types.KeyboardButton(text="🏠 В меню"))

    return keyboard
