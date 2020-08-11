import telebot


def new_keyboard(buttons):
    kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for button in buttons:
        kb.add(telebot.types.KeyboardButton(button))
    return kb


start = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
start.add(telebot.types.KeyboardButton("Расписание"))