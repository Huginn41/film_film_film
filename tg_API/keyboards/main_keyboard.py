from telebot import types


def main_keyboard():
    """Клавиатура главного меню"""
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="🎬 Поиск фильмов"))
    return keyboard


if __name__ == 'main':
    main_keyboard()
