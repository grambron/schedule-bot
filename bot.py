from aiogram import Bot, Dispatcher, executor, types
from node_manager import NodeManager
from keyboards import new_keyboard
import configurer

bot = Bot(configurer.config['BOT']['token'])
dp = Dispatcher(bot)

node_client = NodeManager()


@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    node_client.add_user(message.chat.id, message.from_user.username)
    node = node_client.get_start_node()
    keyboard = new_keyboard(node.buttons)
    await message.answer(node.text, reply_markup=keyboard)


@dp.message_handler(content_types=['text'])
async def send_text(message: types.Message):
    node = node_client.get_node(message)
    keyboard = new_keyboard(node.buttons)
    await message.answer(node.text, reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp)
