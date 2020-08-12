import telebot
import keyboards
import node_manager
from node_manager import NodeManager
from keyboards import new_keyboard


bot = telebot.TeleBot("1395352900:AAF-V0aHMRuBGUJSF1VmwN0ieesnTSHdvEM")

node_client = NodeManager()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет", reply_markup=keyboards.start)


@bot.message_handler(content_types=['text'])
def send_text(message):
    node = node_client.get_node(message.from_user.id)
    keyboard = new_keyboard(node.buttons)
    bot.send_message(message.chat.id, node.text, reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling()
