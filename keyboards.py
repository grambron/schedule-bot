from aiogram import types


def new_keyboard(buttons):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for button in buttons:
        kb.add(types.KeyboardButton(button[0]))
    return kb


def new_inline_keyboard(text):
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="тык", url=text)
    )
