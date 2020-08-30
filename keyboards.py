from aiogram import types


def new_keyboard(buttons):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for button in buttons:
        kb.add(types.KeyboardButton(button[0]))
    return kb
